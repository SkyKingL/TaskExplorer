import pynvml

class gpu:
    server_info_list = []
    UNIT = 1024 * 1024
    pynvml.nvmlInit()  # 初始化
    gpu_device_count = pynvml.nvmlDeviceGetCount()  # 获取Nvidia GPU块数
    for gpu_index in range(gpu_device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_index)  # 获取GPU i的handle，后续通过handle来处理
        memery_info = pynvml.nvmlDeviceGetMemoryInfo(handle)  # 通过handle获取GPU 的信息
        server_info_list.append(
            {
                "gpu_id": gpu_index,  # gpu id
                "total": int(memery_info.total / UNIT),  # gpu 总内存
                "used": int(memery_info.used / UNIT),  # gpu使用内存
                "utilization": pynvml.nvmlDeviceGetUtilizationRates(handle).gpu  # 使用率
            }
        )
        gpu_name = str(pynvml.nvmlDeviceGetName(handle))
        gpu_util_rate = pynvml.nvmlDeviceGetUtilizationRates(handle).gpu
        gpu_memory_rate = pynvml.nvmlDeviceGetUtilizationRates(handle).memory
        # print(f"第 %d 张卡：{gpu_index}" )
        # print(f"显卡名：{gpu_name}")
        # print(f"内存总容量：{memery_info.total / UNIT} MB")
        # print(f"使用容量：{memery_info.total / UNIT}MB")
        # print(f"剩余容量：{memery_info.total / UNIT}MB")
        # print(f"显存空闲率：{memery_info.free / memery_info.total}")
        # print(f"供电水平：{gpu_power_state}")
        # print(f"gpu计算核心满速使用率：{gpu_util_rate}")
        # print(f"gpu内存读写满速使用率：{gpu_memory_rate}")
        # print(f"内存占用率：{memery_info.used / memery_info.total}")

    pynvml.nvmlShutdown()  # 关闭管理工具
