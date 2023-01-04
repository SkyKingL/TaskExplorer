# 一些全局参数


class Va:
    speed = 2
    gx = "正常"
    lastspeed = 0 # 立即刷新后需回复原速度
    speedflag = 0 # 为1表示已执行过行立即刷新
    pid = 1000000
    cpu_data = []
    gpu_data = []
    bytes_sent = 0
    bytes_recv = 0
    xtb = 0 # 是否小图标的flag
