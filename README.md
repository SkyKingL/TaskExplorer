[初步设计(没有小图标)的展示](https://www.bilibili.com/video/BV1RK411i7Bq/?share_source=copy_web&vd_source=e5931cacd02470163649ff1370189c5f)

<p><strong>目录</strong></p>
<p><a href="#_Toc123657921">1 总体设计</a></p>
<p><a href="#_Toc123657922">1.1 设计流程</a></p>
<p><a href="#_Toc123657923">1.2 模块设计</a></p>
<p><a href="#_Toc123657924">2 详细设计</a></p>
<p><a href="#_Toc123657925">2.1 用户界面设计</a></p>
<p><a href="#_Toc123657926">2.1.1 主窗口设计</a></p>
<p><a href="#_Toc123657927">2.1.2 子窗口设计</a></p>
<p><a href="#_Toc123657928">2.2 数据获取</a></p>
<p><a href="#_Toc123657929">2.2.1 用户状态数据</a></p>
<p><a href="#_Toc123657930">2.2.2 应用程序及进程数据</a></p>
<p><a href="#_Toc123657931">2.2.3 数据的插入</a></p>
<p><a href="#_Toc123657932">2.3 实时更新</a></p>
<p><a href="#_Toc123657933">2.4 菜单</a></p>
<p><a href="#_Toc123657934">2.4.1 文件(F)&mdash;&mdash;运行新任务、退出管理器</a></p>
<p><a href="#_Toc123657935">2.4.2 选项(O)&mdash;&mdash;置于顶层</a></p>
<p><a href="#_Toc123657936">2.4.3 查看(V)&mdash;&mdash;更新速度、立即刷新</a></p>
<p><a href="#_Toc123657937">2.4.4 查看(V)&mdash;&mdash;小图标、详细列表</a></p>
<p><a href="#_Toc123657938">2.4.5 关机(U)&mdash;&mdash;关机</a></p>
<p><a href="#_Toc123657939">2.4.6 关机(U)&mdash;&mdash;注销</a></p>
<p><a href="#_Toc123657940">2.4.7 帮助(H)&mdash;&mdash;关于</a></p>
<p><a href="#_Toc123657941">2.5 性能页的设计</a></p>
<p><a href="#_Toc123657942">2.5.1 GPU性能图</a></p>
<p><a href="#_Toc123657943">2.5.2 CPU性能图</a></p>
<p><a href="#_Toc123657944">2.5.3 网络数据</a></p>
<p><a href="#_Toc123657945">2.6右键菜单&mdash;&mdash;切换进程、结束进程</a></p>
<p>&nbsp;</p>
<p><strong><br /> </strong></p>
<h1><a name="_Toc123566313"></a><a name="_Toc123657921"></a>1 总体设计</h1>
<p><a name="_Toc123566314"></a><a name="_Toc123657922"></a>1.1设计流程</p>
<p>针对选定的题目&mdash;&mdash;实现Windows系统任务管理器，我们经过多次讨论，最终选定python为开发语言。选择原因：一是小组6个成员中大部分同学在大创中使用的语言是python，对该语言比较熟悉；二是经过调研，我们发现python中有一些库正好可以是实现系统监控，性能分析，进程管理。</p>
<p>设计流程：首先使用Qt Designer进行UI界面设计，设计完成后将.ui文件转换为.py文件供python程序调用。然后根据题目要求，主要采用控件点击事件触发函数运⾏的⽅式进行响应设计。</p>
<p><a name="_Toc123566315"></a><a name="_Toc123657923"></a>1.2模块设计</p>
<p>我们对Windows10下的任务管理器进行了研究，再比对题目中要求我们实现的功能，从而确定了我们任务管理器的功能模块设计，其中有一些改进和创新。</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>图1.1 原任务管理器功能模块</p>
<p>&nbsp;</p>

<p>&nbsp;</p>
<p>图1.2 改进后的任务管理器功能模块</p>
<p>改进之处：实时状态监控中加入了GPU状态、网络状态和磁盘使用状态，同时在功能设计中增加了对数据更新速度的控制。</p>
<p>&nbsp;</p>
<h1><a name="_Toc123566316"></a><a name="_Toc123657924"></a>2详细设计</h1>
<p><a name="_Toc123566317"></a><a name="_Toc123657925"></a>2.1用户界面设计</p>
<p><a name="_Toc123566318"></a><a name="_Toc123657926"></a>2.1.1主窗口设计</p>
<p>我们使用Qt Designer进行了用户界面设计。Qt Designer是PyQt程序UI界面的实现工具，使用Qt Designer可以拖拽、点击完成GUI界面设计，并且设计完成的.ui程序可以转换成.py文件供python程序调用。下面是对所使用控件的介绍：</p>
<p>QMenuBar、QMenu、QAction: QMenuBar就是所有窗口的菜单栏，在此基础上添加不同的QMenu和QAction；QMenu是菜单栏里面菜单，可以显示文本和图标，但是并不负责执行操作，有点类似label的作用；QAction是Qt 将用户与界面进行交互的元素抽象为一种&ldquo;动作&rdquo;。所设计菜单的逻辑结构：文件(F)&mdash;&mdash;运行新任务、退出管理器，选项(O)&mdash;&mdash;置于顶层，查看(V)&mdash;&mdash;立即刷新、更新速度(子菜单：高、正常、低)、关机(U)&mdash;&mdash;关机、注销，帮助(H)&mdash;&mdash;关于。</p>
<p>QTabWidget：一种带标签页的窗口，在这种类型的窗口中可以存储多个子窗口，每个子窗口的显示可以通过对应的标签进行切换。用此控件实现了应用程序及进程、用户、性能这三页的切换。</p>
<p>QTableWidget：一种表格控件，类似于我们经常使用的 Excel 表格，可以将数据以表格的方式展示给用户，在应用程序及进程页和用户页使用了该控件。应用程序及进程页的逻辑结构：映像名称、PID、状态、优先级、内存使用、线程数；用户页的逻辑结构：用户名称、CPU、内存、磁盘。</p>
<p>QLabel：用于显示文本或图像，不提供用户交互功能。用于显示进程数、CPU使用率、更新速度等文本信息。</p>
<p>PlotWidget: 在该控件上可通过pyqtgraph.PlotGraph.plot()函数作图。在性能页，使用它完成了CPU利用率和GPU利用率实时图像的绘制。</p>
<p>除了对界面中各控件的布局设计，我们还对控件进行了命名，为了在编码过程中更好得调用控件，如运行新任务&mdash;&mdash;New_Task、CPU使用率&mdash;&mdash;CPU_Use、关机&mdash;&mdash;Shut_Down。同时为了提升美观，对一些控件插入了特别的样式。</p>
<p>界面设计结果如下：</p>
<p>图2.1 主窗口(1)</p>
<p>图2.2 主窗口(2)</p>
<p>&nbsp;</p>
<p>图2.3 主窗口(3)</p>
<p>&nbsp;</p>
<p>而后使用在pycharm上配置好的pyuic工具，将.ui文件转化为.py文件，即通过TE.ui转换生成TU_ui.py。</p>
<p>&nbsp;</p>
<p><a name="_Toc123566319"></a><a name="_Toc123657927"></a>2.1.2子窗口设计</p>
<p>一些功能需要弹出子窗口，如运行新任务和切换进程这两个模块。同样是先用QT Designer设计，而后由.ui文件生成.py文件。下面是对部分所使用控件的介绍：</p>
<p>QLineEdit：允许用户使用一组有用的编辑功能输入和编辑单行纯文本，包括撤消和重做、剪切和粘贴以及拖放。在运行新任务和切换进程中都需要用户进行输入操作，故用到此控件。</p>
<p>QPushButton：是实际开发中最常使用的一种按钮。</p>
<p>界面设计结果如下：</p>
<p>图2.4 子窗口(1)</p>
<p>图2.5 子窗口(2)</p>
<p><a name="_Toc123566320"></a><a name="_Toc123657928"></a>2.2数据获取</p>
<p><a name="_Toc123566321"></a><a name="_Toc123657929"></a>2.2.1用户状态数据</p>
<ul>
	<li>关键数据结构</li>
</ul>
<p>主要的package为getpass,psutil,time,gpu,pyQt5。</p>
<ol>
	<li>getuser() #获取电脑的用户名</li>
	<li>cpu_percent() #获取CPU使用率</li>
	<li>virtual_memory() #获取内存信息</li>
	<li>virtual_memory().total #总体内存</li>
	<li>virtual_memory().used#已使用内存</li>
	<li>virtual_memory().free#空闲内存</li>
	<li>mewrate= float(mem.used/mem.total) #内存使⽤率</li>
	<li>disk_usage('/').percent #磁盘使⽤率</li>
	<li>disk_usage('/').free #磁盘剩余容量</li>
	<li>disk_usage('/').used #磁盘已使用容量</li>
	<li>disk_usage('/').total #磁盘总容量</li>
</ol>
<ul>
	<li>设计流图</li>
</ul>
<p>图2.6 用户数据获取设计流图</p>
<p>&nbsp;</p>
<ul>
	<li>代码展示</li>
</ul>
<p>功能介绍：通过getpass,psutil,time,gpu等package，获取当前所运行的电脑用户信息，包括用户名，内存信息，磁盘信息等，将获取到的信息发送至所设计的用户UI接口，对接数据，进行信息的展示。</p>
<p><strong># Refresh_user.py &gt; UserThread</strong><strong>类</strong></p>
<p>from common import *</p>
<p>import getpass, psutil, time</p>
<p>from PyQt5.QtCore import QThread, pyqtSignal, QObject</p>
<p>from gpu import gpu</p>
<p>&nbsp;</p>
<p>class UserThread(QObject):</p>
<p>&nbsp;&nbsp;&nbsp; # 通过类成员对象定义信号</p>
<p>&nbsp;&nbsp;&nbsp; update_user = pyqtSignal(tuple)</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp; # 处理业务逻辑 user</p>
<p>&nbsp;&nbsp;&nbsp; def run_user(self):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; while True:</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; usep = psutil.cpu_percent(interval=1)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Va.cpu_data.append(usep)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Va.gpu_data.append(gpu.gpu_memory_rate)</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; key_info, net_in, net_out = self.get_rate(self.get_key)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a = str(getpass.getuser())</p>
<p>&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b = ' cpu 使⽤率：' + str(usep) + '%'</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; mem = psutil.virtual_memory()</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; mewrate = float(mem.used / mem.total)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; c = ' 总体内存：' + str(round(mem.total / 1024.0 / 1024.0 / 1024.0, 2)) + \</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'G\n 使⽤内存：' + str(round(mem.used / 1024.0 / 1024.0 / 1024.0, 2)) + \</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'G\n 空闲内存：' + str(round(mem.free / 1024.0 / 1024.0 / 1024.0, 2)) + \</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'G\n 使⽤率：' + str(round(mewrate * 100, 1)) + '%'</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = ' 硬盘使⽤率：' + str(round(psutil.disk_usage('/').percent, 1)) + \</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; '%\n 剩余容量：' + str(round(psutil.disk_usage('/').free / 1024.0 / 1024.0 / 1024.0, 2)) + \</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'G\n 使⽤容量：' + str(round(psutil.disk_usage('/').used / 1024.0 / 1024.0 / 1024.0, 2)) + \</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'G\n 总容量：' + str(round(psutil.disk_usage('/').total / 1024.0 / 1024.0 / 1024.0, 2)) + 'G'</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x = (a, b, c, d)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.update_user.emit(x)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; time.sleep(Va.speed)</p>
<p>&nbsp;</p>
<ul>
	<li>运行结果展示</li>
</ul>
<p>图2.7 用户页运行结果</p>
<p>&nbsp;</p>
<p><a name="_Toc123566322"></a><a name="_Toc123657930"></a>2.2.2应用程序及进程数据</p>
<ul>
	<li>关键数据结构</li>
</ul>
<ol>
	<li>pids（）//获得所有进程的 PID 值</li>
	<li>pid（）//获得当前进程的PID</li>
	<li>name()//获得当前进程的名字</li>
	<li>status()//获得当前进程的状态</li>
	<li>nice()//获得当前进程的优先级</li>
	<li>memory_info()//获得当前进程的占用内存大小</li>
	<li>num_threads()//获得当前进程的⼦线程个数</li>
</ol>
<p>&nbsp;</p>
<ul>
	<li>设计流图</li>
</ul>
<p>图2.8 应用程序及进程数据获取设计流图</p>
<p>&nbsp;</p>
<ul>
	<li>代码展示</li>
</ul>
<p><strong># Refresh_Process.py &gt; ProcessThread</strong><strong>类</strong></p>
<p>from PyQt5.QtCore import QThread, pyqtSignal, QObject</p>
<p>from PyQt5.QtGui import QPixmap</p>
<p>import win32gui</p>
<p>from ctypes import windll</p>
<p>import time</p>
<p>import psutil</p>
<p>from common import Va</p>
<p>&nbsp;</p>
<p>class ProcessThread(QObject):</p>
<p>&nbsp;&nbsp;&nbsp; # 通过类成员对象定义信号</p>
<p>&nbsp;&nbsp;&nbsp; update_process = pyqtSignal(tuple)</p>
<p>&nbsp;&nbsp;&nbsp; # 用于每次更新后控制写入行的位置</p>
<p>&nbsp;&nbsp;&nbsp; # 处理业务逻辑 process</p>
<p>&nbsp;&nbsp;&nbsp; def run_process(self):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; while True:</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for jci in psutil.pids():</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # windows有一些进程访问权限不够,做个容错处理</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; try:</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; process = psutil.Process(jci)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a = str(process.name()) # 映像名称</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; b = str(process.pid)&nbsp;&nbsp;&nbsp; # PID</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; c = str(process.status())&nbsp;&nbsp; # 状态</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = str(process.nice()) # 优先级</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = self.ex(d)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; e = str(round(process.memory_info().rss / 1024. / 1024.,2)) + 'MB' # 内存大小</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;f = str(process.num_threads())&nbsp; # 线程数</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x = (a, b, c, d, e, f)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.update_process.emit(x)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; pass</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x = ("end", "end")</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.update_process.emit(x)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; time.sleep(Va.speed)</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp; def ex(self, d):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if d == "Priority.ABOVE_NORMAL_PRIORITY_CLASS":</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = "较高"</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; elif d == "Priority.BELOW_NORMAL_PRIORITY_CLASS":</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = "较低"</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; elif d == "Priority.HIGH_PRIORITY_CLASS":</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = "最高"</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; elif d == "Priority.IDLE_PRIORITY_CLASS":</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = "空闲"</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; elif d == "Priority.NORMAL_PRIORITY_CLASS":</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = "正常"</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; elif d == "Priority.PROCESS_MODE_BACKGROUND_BEGIN":</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = "开始后台模式"</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; elif d == "PROCESS_MODE_BACKGROUND_END":</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = "结束后台模式"</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else:</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = "实时"</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return d</p>
<p>&nbsp;</p>
<ul>
	<li>原理介绍</li>
</ul>
<p>该代码实现的功能是应用进程及进程页数据的获取，主要用到的是psutil包。首先定义ProcessThread(QObject)类，方便在其他文件中被调用从而实现功能。ProcessThread类有一个类成员update_process，通过类成员对象定义信号，用于每次更新后控制写入行的位置。接着定义了一个类方法run_process，用以处理业务逻辑 process。在run_process方法中，首先通过psutil.pids()函数获取所有进程的pid。接着for循环所有进程，依次调用process.name()、process.pid（）、process.status()、process.nice()、process.memory_info()、process.num_threads()函数，获得当前进程的PID、映像名称、状态优先级、占用内存大小（MB）、⼦线程个数，然后递交。其中，在获取当前进程优先级时，返回的信息并不直观（如Priority.HIGH_PRIORITY_CLASS等，具体见下图），所以在下面定义了一个ex(self, d)方法，用于将函数返回的信息转化成直观的优先级信息。由于windows有一些进程访问权限不够,所以在编写代码时进行了容错处理，如果进程因权限不够获取不了，那就放弃获取。在for循环结束后插入（end，end）元组，用于后续统计进程总个数用。</p>
<p>图2.9 优先级信息的映射</p>
<p>&nbsp;</p>
<ul>
	<li>效果展示</li>
</ul>
<p>图2.10 应用程序及进程页运行结果</p>
<p>&nbsp;</p>
<p><a name="_Toc123657931"></a>2.2.3 数据的插入</p>
<p>以应用程序及用户数据的插入表中为例。</p>
<ul>
	<li>关键数据结构</li>
</ul>
<p>主要的Python模块是PyQt5，psutil，win32gui。涉及的主要函数或数据：</p>
<ol>
	<li>msg</li>
</ol>
<p>QTableWidget接收的数据结构，其为一个进程的一组信息，在Python中使用tuple结构存储</p>
<ol start="2">
	<li>PyQt5.QWidgets.QTableWidgetItem(...)</li>
</ol>
<p>根据Qt信号与槽机制，将接收的信号数据msg，转为QTableWidgetItem对象，以便将数据在QTableWidget中显示。其一个重载构造函数可以同时接收QICon类的对象和字符串，在GUI上能同时显示图标和字符串</p>
<ol start="3">
	<li>PyQt5.QWidgets .QTableWidget.setItem(...)</li>
</ol>
<p>将QTableWidgetItem放置在表格指定位置上展示。</p>
<ol start="4">
	<li>psutil.Process(...)</li>
</ol>
<p>根据进程pid获取Process类对象，该类将进程的一些信息，如pid、进程名称、状态等作为类的数据成员或成员函数，需要时调用相关数据成员或成员函数即可。</p>
<ol start="5">
	<li>psutil.Process.cmdline(...)</li>
</ol>
<p>Windows系统运行进程，使用命令行进行命令批处理，从而能打开软件，创建进程并运行。该函数能获得进程在命令行的命令，返回值是列表，第一个元素是进程的exe文件的绝对路径，其余元素是exe的命令行参数。</p>
<ol start="6">
	<li>win32gui.ExtractIconEx(...)</li>
</ol>
<p>该函数根据exe文件绝对路径，获取exe的大小图标句柄。</p>
<ol start="7">
	<li>PyQt5.QtWinExtras.QtWin.fromHICON(...)</li>
</ol>
<p>该函数根据图标句柄，返回QPixmap类对象。</p>
<ol start="8">
	<li>PyQt5.QtGui.QIcon(...)</li>
</ol>
<p>QIcon类的一个重载构造函数，能够接收QPixmap类对象作为参数，从而定义一个QICon对象</p>
<p>&nbsp;</p>
<ul>
	<li>设计流图</li>
</ul>
<p>图2.11 数据插入设计流图</p>
<ul>
	<li>代码展示</li>
</ul>
<p>功能介绍：通过PyQt5、psutil、win32gui等Python模块，将进程有关的一些信息，比如pid、进程名称、小图标等信息放在GUI上显示，同时统计显示出的进程数量。</p>
<p><strong>run_ui.py &gt; MainWindow </strong><strong>类</strong><strong> &gt; Insert_Process</strong><strong>函数</strong></p>
<p>&nbsp; &nbsp; # 应用程序及进程页</p>
<p>&nbsp; &nbsp; def Insert_Process(self, msg):</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; processpage = self.ui.tableWidget</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; processpage.setRowCount(150)</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; j = self.cnt</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; #用一个特殊元组表示已经获取所有进程</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; if msg[0] == "end":</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # 统计结束，P_Num标签写入进程数</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; self.ui.P_num.setText("进程数: " + str(self.cnt))</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; self.cnt = 0</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;# 详细列表显示</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; if Va.xtb == 0:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; for i in range(1, 6):</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; processpage.setColumnHidden(i, False)</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; for i in range(6):</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if i == 0:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; processpage.setColumnWidth(i, 180)</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; processpage.setColumnWidth(i, 100)</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; else:&nbsp;&nbsp; # 只显示小图标</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; for i in range(1, 6):</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; processpage.setColumnHidden(i,True)</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; processpage.setColumnWidth(0, 700)</p>
<p>&nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; for i in range(6):</p>
<p>&nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; data = QTableWidgetItem(msg[i]) if i != 0 else \</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;QTableWidgetItem(QIcon(getPixmap(int(msg[1]), large=False)), msg[i])</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; processpage.setItem(j, i, data)</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # data.setTextColor("green") &nbsp;# 设置单元格文本颜色</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; data.setForeground(QBrush(Qt.GlobalColor.darkGreen))</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; data.setTextAlignment(QtCore.Qt.AlignCenter) &nbsp;# 设置单元格居中</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; processpage.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed) &nbsp;# 设置表格所有列固定宽度</p>
<p>&nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; processpage.resizeRowsToContents() &nbsp;# 使行高跟随内容改变</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; processpage.verticalHeader().setVisible(False) &nbsp;# 隐藏垂直标题</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; # processpage.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) &nbsp;# 设置表格所有列按比例随窗口自动缩放</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; self.cnt = self.cnt + 1</p>
<p><a name="_Toc123657932"></a>2.3实时更新</p>
<ul>
	<li>原理</li>
</ul>
<p>实现数据的实时更新，使用了信号与槽机制。信号槽机制与Windows下消息机制类似，消息机制是基于回调函数，Qt中用信号与槽来代替函数指针，使程序更安全简洁。信号和槽机制是 Qt 的核心机制，可以让编程人员将互不相关的对象绑定在一起，实现对象之间的通信。</p>
<p>信号：当对象改变其状态时，信号就由该对象发射 (emit) 出去，而且对象只负责发送信号，它不知道另一端是谁在接收这个信号。这样就做到了真正的信息封装，能确保对象被当作一个真正的软件组件来使用。</p>
<p>槽：用于接收信号，而且槽只是普通的对象成员函数。一个槽并不知道是否有任何信号与自己相连接。而且对象并不了解具体的通信机制。</p>
<p>信号与槽的连接：所有从 QObject 或其子类 ( 例如 Qwidget ) 派生的类都能够包含信号和槽。因为信号与槽的连接是通过 QObject 的 connect() 成员函数来实现的。</p>
<p>在本工程中使用了pygtSignal接口实现信号与槽机制，其介绍如下图2.11。</p>
<p>图2.12 pygtSignal接口的使用</p>
<p>&nbsp;</p>
<ul>
	<li>代码展示</li>
</ul>
<p>以应用程序及进程页的实时更新为例</p>
<p><strong># Refresh_Process.py &gt; ProcessThread</strong><strong>函数</strong></p>
<p>class ProcessThread(QObject):</p>
<p># 通过类成员对象定义信号</p>
<p>&nbsp;&nbsp;&nbsp; update_process = pyqtSignal(tuple)</p>
<p>&nbsp;&nbsp;&nbsp; # 用于每次更新后控制写入行的位置</p>
<p>&nbsp;&nbsp;&nbsp; # 处理业务逻辑 process</p>
<p>&nbsp;&nbsp;&nbsp; def run_process(self):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; while True:</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for jci in psutil.pids():</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # windows有一些进程访问权限不够,做个容错处理</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; try:</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; process = psutil.Process(jci)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a = str(process.name()) # 映像名称</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; b = str(process.pid)&nbsp;&nbsp;&nbsp; # PID</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; c = str(process.status())&nbsp;&nbsp; # 状态</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = str(process.nice()) # 优先级</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = self.ex(d)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; e = str(round(process.memory_info().rss / 1024. / 1024.,2)) + 'MB' # 内存大小</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; f = str(process.num_threads())&nbsp; # 线程数</p>
<p>&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x = (a, b, c, d, e, f)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.update_process.emit(x)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; pass</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x = ("end", "end")</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.update_process.emit(x)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; time.sleep(Va.speed)</p>
<p>&nbsp;</p>
<p><strong># run_ui.py</strong></p>
<p># 在def __init__(self)中调用</p>
<p>&nbsp;&nbsp;&nbsp; def refresh_process(self):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 创建线程</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.backend_1 = ProcessThread()</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 连接信号</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.cnt = 0</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.backend_1.update_process.connect(self.Insert_Process)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.thread_1 = QThread()</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;self.backend_1.moveToThread(self.thread_1)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 开始线程</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.thread_1.started.connect(self.backend_1.run_process)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.thread_1.start()</p>
<p># 应用程序及进程页</p>
<p>&nbsp;&nbsp;&nbsp; def Insert_Process(self, msg):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; processpage = self.ui.tableWidget</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; processpage.setRowCount(150)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; j = self.cnt</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #用一个特殊元组表示已经获取所有进程</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if msg[0] == "end":</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 统计结束，P_Num标签写入进程数</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.ui.P_num.setText("进程数: " + str(self.cnt))</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.cnt = 0</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if Va.xtb == 0:</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for i in range(1, 6):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; processpage.setColumnHidden(i, False)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for i in range(6):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if i == 0:</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; processpage.setColumnWidth(i, 180)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else:</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; processpage.setColumnWidth(i, 100)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else:</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for i in range(1, 6):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; processpage.setColumnHidden(i,True)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; processpage.setColumnWidth(0, 700)</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for i in range(6):</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data = QTableWidgetItem(msg[i]) if i != 0 else \</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; QTableWidgetItem(QIcon(getPixmap(int(msg[1]), large=False)), msg[1])</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; processpage.setItem(j, i, data)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # data.setTextColor("green")&nbsp; # 设置单元格文本颜色</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data.setForeground(QBrush(Qt.GlobalColor.darkGreen))</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data.setTextAlignment(QtCore.Qt.AlignCenter)&nbsp; # 设置单元格居中</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; processpage.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)&nbsp; # 设置表格所有列固定宽度</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; processpage.resizeRowsToContents()&nbsp; # 使行高跟随内容改变</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; processpage.verticalHeader().setVisible(False)&nbsp; # 隐藏垂直标题</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.cnt = self.cnt + 1</p>
<p>&nbsp;</p>
<p><a name="_Toc123657933"></a>2.4 菜单</p>
<p><a name="_Toc123657934"></a>2.4.1 文件(F)&mdash;&mdash;运行新任务、退出管理器</p>
<ul>
	<li>关键数据结构</li>
</ul>
<ol>
	<li>exit() #退出当前进行的程序任务</li>
	<li>connect() #鼠标点击触发事件</li>
	<li>ShellExecute() #打开外部程序或文件，执行所选择新任务</li>
</ol>
<p>&nbsp;</p>
<ul>
	<li>运行流程图</li>
</ul>
<p>图2.13 文件菜单运行流程图</p>
<p>&nbsp;</p>
<ul>
	<li>代码展示</li>
</ul>
<p>功能介绍：点击菜单目录下的&ldquo;文件（F）&rdquo;，可以选择&ldquo;运行新任务&rdquo;，打开电脑中的外部程序或文件；选择&ldquo;退出管理器&rdquo;即退出管理器程序任务。</p>
<p>图2.14 文件菜单</p>
<p>&nbsp;</p>
<p><strong># run_ui.py</strong></p>
<p># 文件(F)&mdash;&mdash;退出管理器</p>
<p>self.ui.Exit.triggered.connect(File.exitui) #exitui()，调用时没加括号，说明仅调用功能，不返回结果</p>
<p># 文件(F)&mdash;&mdash;运行新任务</p>
<p>self.ui.New_Task.triggered.connect(self.serve_win) #serve_win(),调用时没加括号，说明仅调用功能，不返回结果</p>
<p>&nbsp;</p>
<p># 运行新任务的交互窗口</p>
<p>def serve_win(self):</p>
<p>&nbsp; # self.form2 = QtWidgets.QWidget()</p>
<p>self.form2 = Serve_Window()</p>
<p>self.form2.show()</p>
<p>&nbsp;</p>
<p>class File:</p>
<p>&nbsp;&nbsp;&nbsp; def exitui(self):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; time.sleep(1)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print('退出管理器...')</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sys.exit()</p>
<p><strong>&nbsp;</strong></p>
<p><strong># RunTaskWin.py</strong></p>
<p>import win32api</p>
<p>from PySide2.QtWidgets import *</p>
<p>from win_ui import Ui_Form</p>
<p># 进程管理</p>
<p>class Serve_Window(QWidget):</p>
<p>&nbsp;&nbsp;&nbsp; def __init__(self):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 基本初始化</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; super().__init__()</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.ui = Ui_Form()</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.ui.setupUi(self)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.setWindowTitle("运行新任务")</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 给需要使用的控件声明好所需函数</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.ui.run.clicked.connect(self.startp)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 浏览文件目录</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.ui.lookup.clicked.connect(self.lookup)</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp; def lookup(self):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; filePath, _ = QFileDialog.getOpenFileName(</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;self,&nbsp; # 父窗口对象</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "选择你要运行的文件",&nbsp; # 标题</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; r"data",&nbsp; # 起始目录</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "(*.*)"&nbsp; # 选择类型过滤项，过滤内容在括号中 #*.*所有文件</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.ui.enter.setText(filePath)</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp; # 运行新任务（新建进程）</p>
<p>&nbsp;&nbsp;&nbsp; def startp(self):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; task = self.ui.enter.text()</p>
<p>&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;print(task)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 不为空</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if(len(task)!=0 and task.isspace()==False):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; win32api.ShellExecute(0, 'open', task, '', '', 1)</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 正常执行后退出窗口</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.close()</p>
<p><strong>&nbsp;</strong></p>
<ul>
	<li>效果展示</li>
</ul>
<p>图2.15 运行新任务效果展示</p>
<p>图2.16 退出管理器效果展示</p>
<p><a name="_Toc123657935"></a>2.4.2 选项(O)&mdash;&mdash;置于顶层</p>
<p>(1) 原理</p>
<p>使用self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)可以设置窗口置顶，使用self.setWindowFlags(QtCore.Qt.Widget)可以取消窗口置顶。</p>
<p>&nbsp;</p>
<p>(2) 代码展示</p>
<p><strong>run_ui.py &gt; MainWindow </strong><strong>类</strong><strong> &gt; __init__</strong><strong>函数</strong></p>
<p># 选项(O)&mdash;&mdash;置于顶层<br /> # self.flag 是True&mdash;&mdash;非置顶，是False&mdash;&mdash;置顶<br /> self.flag = True<br /> self.ui.Always_Front.triggered.connect(self.show_front)</p>
<p><strong>run_ui.py &gt; MainWindow </strong><strong>类</strong><strong> &gt; show_front</strong><strong>函数</strong></p>
<p>def show_front(self):<br /> &nbsp;&nbsp;&nbsp; # 置于顶层<br /> &nbsp;&nbsp;&nbsp; if(self.flag):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.flag = False<br /> &nbsp;&nbsp;&nbsp; # 取消置顶<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.setWindowFlags(QtCore.Qt.Widget)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.flag = True<br /> &nbsp;&nbsp;&nbsp; self.show()</p>
<p><a name="_Toc123657936"></a>2.4.3 查看(V)&mdash;&mdash;更新速度、立即刷新</p>
<p>(1)原理</p>
<p>所有的更新都在Refresh_Process.py和Refresh_user.py中，其中time.sleep(Va.speed)即每次获取数据后的延迟。实现对Va.speed的变化即实现更新速度的变化。其中Va来自于common.py，该类中的数据作为全局变量为各模块服务。而立即刷新的实现即使得Va.speed在短时间内特别小，刷新之后需恢复原速度。</p>
<p>(2)代码展示</p>
<p><strong>run_ui.py &gt; MainWindow </strong><strong>类</strong><strong> &gt; show_front</strong><strong>函数</strong></p>
<p><strong>common.py &gt; Va </strong><strong>类</strong></p>
<p># 一些全局参数<br /> class Va:<br /> &nbsp;&nbsp;&nbsp; speed = 2<br /> &nbsp;&nbsp;&nbsp; gx = "正常"<br /> &nbsp;&nbsp;&nbsp; lastspeed = 0 # 立即刷新后需回复原速度</p>
<p>speedflag = 0 # 为1表示已执行过行立即刷新<br /> &nbsp;&nbsp;&nbsp; pid = 1000000<br /> &nbsp;&nbsp;&nbsp; cpu_data = []<br /> &nbsp;&nbsp;&nbsp; gpu_data = []<br /> &nbsp;&nbsp;&nbsp; bytes_sent = 0<br /> &nbsp;&nbsp;&nbsp; bytes_recv = 0<br /> &nbsp;&nbsp;&nbsp; xtb = 0 # 是否小图标的flag</p>
<p><strong>run_ui.py &gt; MainWindow </strong><strong>类</strong><strong> &gt;</strong> <strong>quick_refresh</strong><strong>函数</strong></p>
<p># 立即刷新</p>
<p>def quick_refresh(self):<br /> &nbsp;&nbsp;&nbsp; Va.speed = 0.5</p>
<p><strong>run_ui.py &gt; MainWindow </strong><strong>类</strong><strong> &gt;</strong> <strong>Insert_user</strong><strong>函数</strong></p>
<p>if Va.speed != 0.5:<br /> &nbsp;&nbsp;&nbsp; Va.lastspeed = Va.speed # 记录上一次不是立即刷新的速度，同时保证已经刷新过<br /> elif Va.speed == 0.5 and Va.speedflag ==0:<br /> &nbsp;&nbsp;&nbsp; Va.speedflag = 1 #如果是立即刷新对应的速度，这次刷新执行后就可以将速度调整回来<br /> &nbsp;&nbsp;&nbsp; return<br /> elif Va.speed == 0.5 and Va.speedflag == 1:<br /> &nbsp;&nbsp;&nbsp; Va.speed = Va.lastspeed<br /> &nbsp;&nbsp;&nbsp; Va.speedflag = 0</p>
<p><br /> <br /> # 把&ldquo;更新速度&rdquo;标签也更新<br /> if Va.speed == 1:<br /> &nbsp;&nbsp;&nbsp; Va.gx = "高"<br /> elif Va.speed == 2:<br /> &nbsp;&nbsp;&nbsp; Va.gx = "正常"<br /> elif Va.speed == 3:<br /> &nbsp;&nbsp;&nbsp; Va.gx = "低"<br /> self.ui.speed.setText("更新速度：" + Va.gx)</p>
<p>&nbsp;</p>
<p>(3)设计流图</p>
<p>(4)运行结果</p>
<p>图2.17 更新速度效果展示</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><a name="_Toc123657937"></a>2.4.4 查看(V)&mdash;&mdash;小图标、详细列表</p>
<p>(1)关键数据结构</p>
<p>主要Python模块&mdash;&mdash;PyQt5。涉及的主要函数和变量：</p>
<ol>
	<li>Va.xtb</li>
</ol>
<p>用来设置隐藏列还是显示列。点击菜单项&ldquo;小图标&rdquo;时，xtb设为1。</p>
<ol start="2">
	<li>PyQt5.QWidgets.QTableWidget.setColumnHidden(...)</li>
</ol>
<p>将QTableWidget的某一列，设置为显示或者隐藏</p>
<ol start="3">
	<li>PyQt5.QWidgets.QTableWidget.setColumnWith(...)</li>
</ol>
<p>设置QTableWidget的某一列的列宽</p>
<p>(2) 设计流图</p>
<p>图2.18 查看&mdash;&mdash;小图标和详细列表设计流图</p>
<p>（3）代码展示</p>
<p>功能介绍：点击菜单项&ldquo;小图标&rdquo;，将进程页面的信息，只留下有关&ldquo;图标+进程名&rdquo;的一列，隐藏其他列。而点击详细列表，则将应用程序及进程相关信息全部展示出来。</p>
<p><strong><br /> </strong></p>
<p><strong>getPixMap.py</strong></p>
<p>import psutil<br /> from PyQt5.QtGui import QPixmap<br /> from PyQt5.QtWinExtras import QtWin<br /> <br /> import win32gui</p>
<p><br /> # function getPixmap<br /> # args: pid(int), large(bool)<br /> #&nbsp;&nbsp; pid: process id<br /> #&nbsp;&nbsp; large: return large or small icon handles<br /> # return: PyQt5.QtGui.QPixmap<br /> def getPixmap(pid: int, large=False) -&gt; QPixmap:<br /> &nbsp;&nbsp;&nbsp; try:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; exe = psutil.Process(pid).cmdline()[0]<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 使用 win32gui 从进程对应的 exe 文件提取图标<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # large 为大图标句柄列表，small 为小图标句柄列表<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; piconLarge, piconSmall = win32gui.ExtractIconEx(exe, 0)<br /> &nbsp;&nbsp;&nbsp; except:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return QPixmap("mr.png")<br /> <br /> &nbsp;&nbsp;&nbsp; if large:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 没有图标的进程，需要设置个统一的默认图标<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if len(piconLarge) == 0:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return QPixmap("icon.png")<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 释放小图标句柄<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for s in piconSmall:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; win32gui.DestroyIcon(s)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 获得大图标的QPixmap<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; pixmap = QtWin.fromHICON(piconLarge[0])<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 释放大图标句柄，避免长时间内未释放的图标句柄过多<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for l in piconLarge:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;win32gui.DestroyIcon(l)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return pixmap<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br /> &nbsp;&nbsp;&nbsp; if len(piconSmall) == 0:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return QPixmap("mr.png")<br /> <br /> &nbsp;&nbsp;&nbsp; # 释放大图标句柄<br /> &nbsp;&nbsp;&nbsp; for l in piconLarge:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; win32gui.DestroyIcon(l)<br /> &nbsp;&nbsp;&nbsp; # 获得小图标的QPixmap<br /> &nbsp;&nbsp;&nbsp; pixmap = QtWin.fromHICON(piconSmall[0])<br /> &nbsp; &nbsp;&nbsp;# 释放小图标句柄<br /> &nbsp;&nbsp;&nbsp; for s in piconSmall:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; win32gui.DestroyIcon(s)<br /> &nbsp;&nbsp;&nbsp; return pixmap</p>
<p><strong>&nbsp;</strong></p>
<p><strong>run_ui.py &gt; MainWindow</strong><strong>类 &gt;__init__</strong><strong>函数</strong></p>
<p># 查看(V)&mdash;&mdash;小图标<br /> self.ui.S_Icon.triggered.connect(self.S_Icon)<br /> <br /> # 查看(V)&mdash;&mdash;详细列表<br /> self.ui.full_list.triggered.connect(self.full_list)</p>
<p><strong>run_ui.py &gt; MainWindow</strong><strong>类 &gt; S_Icon</strong><strong>函数</strong></p>
<p># 小图标<br /> def S_Icon(self):<br /> &nbsp;&nbsp;&nbsp; Va.xtb = 1</p>
<p><strong>run_ui.py &gt; MainWindow</strong><strong>类 &gt; full_list</strong><strong>函数</strong></p>
<p># 详细列表<br /> def full_list(self):<br /> &nbsp;&nbsp;&nbsp; Va.xtb = 0</p>
<p><strong>run_ui.py &gt; MainWindow</strong><strong>类 &gt; Insert_Process</strong><strong>函数</strong></p>
<p># 注：有关隐藏的上下文代码在应用程序及进程页的数据插入部分，只显示相关功能的代码</p>
<p>if Va.xtb == 0:<br /> &nbsp;&nbsp;&nbsp; for i in range(1, 6):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; processpage.setColumnHidden(i, False)<br /> &nbsp;&nbsp;&nbsp; for i in range(6):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if i == 0:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; processpage.setColumnWidth(i, 180)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; processpage.setColumnWidth(i, 100)<br /> else:<br /> &nbsp;&nbsp;&nbsp; for i in range(1, 6):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;processpage.setColumnHidden(i,True)<br /> &nbsp;&nbsp;&nbsp; processpage.setColumnWidth(0, 700)</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>(4)效果展示</p>
<p>图2.19 查看&mdash;&mdash;小图标效果展示</p>
<p>图2.20 查看&mdash;&mdash;详细列表效果展示</p>
<p>&nbsp;</p>
<p><a name="_Toc123657938"></a>2.4.5 关机(U)&mdash;&mdash;关机</p>
<p>(1) 关键函数</p>
<p>os.system('shutdown /s /t 0')&nbsp; //设置关机倒计时为0秒</p>
<p>&nbsp;</p>
<p>(2) 设计流图</p>
<p>图2.21 关机(U)&mdash;&mdash;关机设计流图</p>
<p>(3) 原理介绍</p>
<p>system函数可以将字符串转化成命令在服务器上运行，os.system('shutdown /s /t 0') 语句可以设置关机倒计时为0秒，从而实现关机功能。其中，在用户点击关机后程序会进行询问，默认设置是NO操作，防止用户因为误触而导致意外关机。</p>
<p><strong>&nbsp;</strong></p>
<p>(4) 代码展示</p>
<p><strong>run_ui.py &gt; MainWindow</strong><strong>类 &gt;</strong><strong> guanji</strong><strong>函数</strong></p>
<p># 关机&mdash;&mdash;设置弹窗<br /> def guanji(self):<br /> &nbsp;&nbsp;&nbsp; msgBox = QMessageBox()<br /> &nbsp;&nbsp;&nbsp; msgBox.setWindowTitle("关机")<br /> &nbsp;&nbsp;&nbsp; msgBox.setText("确定要关机吗？")<br /> &nbsp;&nbsp;&nbsp; msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)<br /> &nbsp;&nbsp;&nbsp; msgBox.setDefaultButton(QMessageBox.No) #默认是No<br /> &nbsp;&nbsp;&nbsp; ret = msgBox.exec_()<br /> &nbsp;&nbsp;&nbsp; if ret == QMessageBox.Yes:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Save was clicked<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print('确定')<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 立即关机<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;os.system('shutdown /s /t 0')<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # cancel was clicked<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print('取消')</p>
<p>(5) 效果展示</p>
<p>图2.22 关机(U)&mdash;&mdash;关机效果展示</p>
<p><a name="_Toc123657939"></a>2.4.6 关机(U)&mdash;&mdash;注销</p>
<p>(1) 关键函数</p>
<p>os.system('shutdown /l /t 0') //设置注销倒计时为0秒</p>
<p><strong>&nbsp;</strong></p>
<p>(2) 设计流图</p>
<p>图2.23 关机(U)&mdash;注销设计流图</p>
<p>(3) 原理介绍</p>
<p>注销的原理与关机的原理类似。system函数可以将字符串转化成命令在服务器上运行，os.system('shutdown /l /t 0') 语句可以设置注销倒计时为0秒，从而实现注销功能。其中，在用户点击注销后程序会进行询问，默认设置是NO操作，防止用户因为误触而导致意外注销。</p>
<p>&nbsp;</p>
<p>(4) 代码展示</p>
<p><strong>run_ui.py &gt; MainWindow</strong><strong>类 &gt; zhuxiao</strong><strong>函数</strong></p>
<p># 注销&mdash;&mdash;设置弹窗<br /> def zhuxiao(self):<br /> &nbsp;&nbsp;&nbsp; msgBox = QMessageBox()<br /> &nbsp;&nbsp;&nbsp; msgBox.setWindowTitle("注销")<br /> &nbsp;&nbsp;&nbsp; msgBox.setText("确定要注销吗？")<br /> &nbsp;&nbsp;&nbsp; msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)<br /> &nbsp;&nbsp;&nbsp; msgBox.setDefaultButton(QMessageBox.No)&nbsp; # 默认是No<br /> &nbsp;&nbsp;&nbsp; ret = msgBox.exec_()<br /> &nbsp;&nbsp;&nbsp; if ret == QMessageBox.Yes:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Save was clicked<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print('确定')<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 立即注销<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # os.system('shutdown /l /t 0')<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # cancel was clicked<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print('取消')</p>
<ul>
	<li>运行结果展示</li>
</ul>
<table>
	<tbody>
		<tr>
			<td width="114">&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
	</tbody>
</table>

<p>图2.24 关机(U)&mdash;&mdash;注销效果展示</p>
<p><a name="_Toc123657940"></a>2.4.7 帮助(H)&mdash;&mdash;关于</p>
<p>(1) 关键数据结构</p>
<p>webbrowser.open() #打开对应的网址</p>
<p>(2) 设计流图</p>
<p>图2.25 帮助(H)&mdash;&mdash;关于设计流图</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>(3) 代码展示</p>
<p>功能介绍：通过接收用户的鼠标点击事件，将界面跳转到Github官方网站，用户可在此处查找遇到的问题以及想要了解的信息。</p>
<p>&nbsp;</p>
<p>#帮助(H)&mdash;&mdash;关于</p>
<p><strong>run_ui.py &gt; MainWindow</strong><strong>类 &gt; __init__</strong><strong>函数</strong></p>
<p>self.ui.About.triggered.connect(self.openurl)</p>
<p><strong>run_ui.py &gt; MainWindow</strong><strong>类 &gt; openurl</strong><strong>函数</strong></p>
<p>def openurl(self):<br /> &nbsp;&nbsp;&nbsp; webbrowser.open("https://github.com/SkyKingL/TaskExplorer/tree/master")</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>（4）效果展示</p>
<p>点击后跳转至：</p>
<p>图2.26 帮助(H)&mdash;&mdash;关于效果展示</p>
<p>&nbsp;</p>
<p><a name="_Toc123657941"></a>2.5性能页的设计</p>
<p><a name="_Toc123657942"></a>2.5.1 GPU性能图</p>
<p>(1) 关键数据结构</p>
<p>主要的package为：psutil,time,gpu,pyqt5,pynvml</p>
<ol>
	<li>pynvml库获取电脑GPU的各种信息并做监视：</li>
	<li>nvmlDeviceGetMemoryInfo(handle) # 通过handle获取GPU 的信息</li>
	<li>nvmlDeviceGetName(handle) # 通过handle获取显卡名</li>
</ol>
<p>&nbsp;</p>
<p>2.self.ui.GPU_Plot.plot()&nbsp;&nbsp; #根据现有数组绘制GPU性能折线图，并显示出来</p>
<p>&nbsp;</p>
<p>(2) 原理解释</p>
<p>通过pynvml,psutil,gpu等package，获取本电脑的显卡名称，显存空闲率和gpu内存读写满速使用率等各种信息，并将获取到的gpu内存读写满速利用率，通过函数以折线图的形式显示出来，和GPU的其它各种信息，一起发送至所涉及的UI接口，进行信息显示。</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>(3) 设计流图</p>
<p>图2.27 GPU性能图绘制设计流图</p>
<p>(4) 代码展示</p>
<p><strong>gpu.py</strong></p>
<p>import pynvml</p>
<p>&nbsp;</p>
<p>class gpu:</p>
<p>&nbsp;&nbsp;&nbsp; server_info_list = []</p>
<p>&nbsp;&nbsp;&nbsp; UNIT = 1024 * 1024</p>
<p>&nbsp;&nbsp;&nbsp; pynvml.nvmlInit()&nbsp; # 初始化</p>
<p>&nbsp; &nbsp;&nbsp;gpu_device_count = pynvml.nvmlDeviceGetCount()&nbsp; # 获取Nvidia GPU块数</p>
<p>&nbsp;&nbsp;&nbsp; for gpu_index in range(gpu_device_count):</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_index)&nbsp; # 获取GPU i的handle，后续通过handle来处理</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; memery_info = pynvml.nvmlDeviceGetMemoryInfo(handle)&nbsp; # 通过handle获取GPU 的信息</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; server_info_list.append(</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "gpu_id": gpu_index,&nbsp; # gpu id</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "total": int(memery_info.total / UNIT),&nbsp; # gpu 总内存</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "used": int(memery_info.used / UNIT),&nbsp; # gpu使用内存</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "utilization": pynvml.nvmlDeviceGetUtilizationRates(handle).gpu&nbsp; # 使用率</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; gpu_name = str(pynvml.nvmlDeviceGetName(handle))</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; gpu_memory_rate = pynvml.nvmlDeviceGetUtilizationRates(handle).memory</p>
<p>pynvml.nvmlShutdown()&nbsp; # 关闭管理工具</p>
<p><strong>Refresh_user.py &gt; UserThread类 &gt; run_user函数</strong></p>
<p>Va.gpu_data.append(gpu.gpu_memory_rate)</p>
<p><strong><br /> </strong></p>
<p><strong>run_ui.py &gt; MainWindow</strong><strong>类 &gt; Insert_user函数</strong></p>
<p># 画性能图 在绘图控件中绘制图形</p>
<p>self.ui.label_2.setText("显卡名：" + gpu.gpu_name)</p>
<p>self.ui.label_3.setText("显存空闲率：" + str(round(gpu.memery_info.free / gpu.memery_info.total * 100, 2)) + '%')</p>
<p>self.ui.GPU_Plot.plot(Va.gpu_data)</p>
<p><a name="_Toc123657943"></a>2.5.2 CPU性能图</p>
<p>CPU性能图的绘制比较简单，在Refresh_user.py中获取最新CPU数据：</p>
<p>usep = psutil.cpu_percent(interval=1)<br /> <br /> Va.cpu_data.append(usep)</p>
<p>再在run_ui.py的Insert_user函数中进行新数据的插入即可：</p>
<p># 画性能图 在绘图控件中绘制图形<br /> self.ui.CPU_record_Plot.plot(Va.cpu_data)</p>
<p><a name="_Toc123657944"></a>2.5.3网络数据</p>
<p>(1) 关键数据结构</p>
<p>主要的package为：psutil,time,pyqt5，主要函数：</p>
<ol>
	<li>def get_key(self) &nbsp;#获取网卡名称以及各网卡的发送和接收速率</li>
</ol>
<p>&nbsp;</p>
<p>(2) 设计流图</p>
<p>图2.28 网络数据设计流图</p>
<p>&nbsp;</p>
<p>(3) 代码展示</p>
<p>通过get_key函数获取了各网卡的名称、接收速率和发送速率，并筛选只要WLAN的网络信息，将得到的信息通过UI接口显示出来&nbsp;&nbsp; 。</p>
<p><strong>Refresh_user.py </strong><strong>&gt; UserThread类 &gt; get_key函数</strong></p>
<p>def get_key(self):<br /> &nbsp;&nbsp;&nbsp; key_info = psutil.net_io_counters(pernic=True).keys()&nbsp; # 获取网卡名称<br /> &nbsp;&nbsp;&nbsp; recv = {}<br /> &nbsp;&nbsp;&nbsp; sent = {}<br /> &nbsp;&nbsp;&nbsp; for key in key_info:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)&nbsp; # 各网卡接收的字节数<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)&nbsp; # 各网卡发送的字节数<br /> &nbsp;&nbsp;&nbsp; return key_info, recv, sent</p>
<p><strong>Refresh_user.py </strong><strong>&gt; UserThread类 &gt; run_user函数</strong></p>
<p>key_info, net_in, net_out = self.get_rate(self.get_key)<br /> <br /> for key in key_info:<br /> &nbsp;&nbsp;&nbsp; # 获取WLAN的网络信息即可<br /> &nbsp;&nbsp;&nbsp; if key == 'WLAN':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Va.bytes_sent = round(net_in.get(key), 2)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Va.bytes_recv = round(net_out.get(key), 2)</p>
<p><strong>run_ui.py &gt; MainWindow</strong><strong>类 &gt; Insert_user</strong><strong>函数</strong></p>
<p>self.ui.sent.setText(str(round(Va.bytes_sent, 2)) + " KB/s")<br /> self.ui.recv.setText(str(round(Va.bytes_recv, 2)) + " KB/s")</p>
<p>&nbsp;</p>
<p>(4) 效果展示</p>
<p>图2.29 性能页效果展示</p>
<p><a name="_Toc123657945"></a>2.6右键菜单&mdash;&mdash;切换进程、结束进程</p>
<p>（1）功能介绍</p>
<p>在应用程序及进程页，使得表格可以拥有右键菜单功能。并设计右键菜单的内容为&ldquo;切换至&rdquo;和&ldquo;结束进程&rdquo;</p>
<p>&nbsp;</p>
<p>（2）代码解释&mdash;&mdash;功能设计</p>
<p># 右键菜单<br /> # 应用程序及进程 tableWidget 允许右键菜单<br /> self.ui.tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)<br /> send_option_1 = QAction(self.ui.tableWidget)<br /> send_option_1.setText("切换至")<br /> send_option_1.triggered.connect(self.change_win)&nbsp; # 点击菜单中的&ldquo;切换进程&rdquo;执行的函数<br /> <br /> # 左键点击后获取表格中数据<br /> self.ui.tableWidget.itemClicked.connect(self.infos)<br /> <br /> send_option_2 = QAction(self.ui.tableWidget)<br /> send_option_2.setText("结束进程")<br /> send_option_2.triggered.connect(self.killPid)&nbsp; # 点击菜单中的&ldquo;切换进程&rdquo;执行的函数</p>
<p>（3）原理解释&mdash;&mdash;结束进程</p>
<p>左键点击表格中任意位置后会将其数据捕获。我们点击PID列后再右键，即可在获取PID数据的前提下进行进程的切换和结束。其中有一定局限性，即只有左键点击PID列后才能执行右键菜单中的功能，其他列的点击均无效。针对此局限性已做异常处理，即通过对Va.pid这个全局变量的判断与赋值来使得只有PID列有效。</p>
<p>（4）代码解释&mdash;&mdash;结束进程</p>
<p># 终止进程<br /> def killPid(self):<br /> &nbsp;&nbsp;&nbsp; if (Va.pid != 1000000):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 防止控制台输出乱码<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; os.system("chcp 65001 &gt; nul")<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # taskkill命令强制结束进程<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; s = "taskkill /im " + str(Va.pid) + " /f"<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; os.system(s)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Va.pid = 1000000</p>
<p>（5）原理解释&mdash;&mdash;切换进程</p>
<p>切换进程，即杀死原进程再运行新进程,由于程序未设置路径不合法的异常处理，需先运行指定新进程再杀死原进程（指定的新进程有问题就会抛出异常）。切换进程会产生一个新的窗口，则需要写一个类来运行此窗口，由于相似性，这里使用菜单中&ldquo;运行新任务&rdquo;已设计好的UI即可。</p>
<p>（6）代码展示</p>
<p><strong>ChangePid.py</strong></p>
<p>import os<br /> import win32api<br /> from PyQt5.QtWidgets import *<br /> from win_ui import Ui_Form<br /> from common import Va<br /> # 进程管理&mdash;&mdash;切换进程<br /> class Change_Win(QWidget):<br /> &nbsp;&nbsp;&nbsp; def __init__(self):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 基本初始化<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; super().__init__()<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.ui = Ui_Form()<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.ui.setupUi(self)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.setWindowTitle("切换进程")<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;self.ui.label_2.setText("切换至：")<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 给需要使用的控件声明好所需函数<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.ui.run.clicked.connect(self.startp)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 浏览文件目录<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.ui.lookup.clicked.connect(self.lookup)<br /> <br /> &nbsp;&nbsp;&nbsp; def lookup(self):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; filePath, _ = QFileDialog.getOpenFileName(<br /> &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self,&nbsp; # 父窗口对象<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "选择你要运行的文件",&nbsp; # 标题<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; r"data",&nbsp; # 起始目录<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "(*.*)"&nbsp; # 选择类型过滤项，过滤内容在括号中 #*.*所有文件<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )<br /> &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;self.ui.enter.setText(filePath)<br /> <br /> &nbsp;&nbsp;&nbsp; # 切换进程&mdash;&mdash;杀死原进程再运行新进程<br /> &nbsp;&nbsp;&nbsp; # 由于程序未设置路径不合法的异常处理<br /> &nbsp;&nbsp;&nbsp; # 先运行指定新进程再杀死原进程（指定的新进程有问题就会抛出异常）<br /> &nbsp;&nbsp;&nbsp; def startp(self):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; task = self.ui.enter.text()<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print(task)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 不为空<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if(len(task)!=0 and task.isspace()==False and Va.pid != 1000000):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; win32api.ShellExecute(0, 'open', task, '', '', 1)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 防止控制台输出乱码<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; os.system("chcp 65001 &gt; nul")<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # taskkill命令强制结束进程<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; s = "taskkill /im " + str(Va.pid) + " /f"<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;os.system(s)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Va.pid = 1000000<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # 正常执行后退出窗口<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.close()</p>
<p>在run_ui中对应的函数change_win，功能即对此窗口进行实例化后运行：</p>
<p># 运行切换进程的交互窗口<br /> def change_win(self):<br /> &nbsp;&nbsp;&nbsp; self.form3 = Change_Win()<br /> &nbsp;&nbsp;&nbsp; self.form3.show()</p>
<p>&nbsp;</p>
<p>（7）效果展示</p>
<p>图2.30 结束进程效果展示</p>
<p>&nbsp;</p>
<p>图2.31 切换进程效果展示</p>
<h1>&nbsp;</h1>
<p>&nbsp;</p>
