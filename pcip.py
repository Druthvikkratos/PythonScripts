import socket
import platform
import psutil  # type: ignore
from py3nvml.py3nvml import (nvmlInit, nvmlDeviceGetCount, nvmlDeviceGetHandleByIndex,
                             nvmlDeviceGetName, nvmlDeviceGetMemoryInfo, nvmlShutdown, nvmlDeviceGetUtilizationRates)

# System Information
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
system_info = platform.uname()

print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

print("\nSystem Information:")
print(f"System: {system_info.system}")
print(f"Node Name: {system_info.node}")
print(f"Release: {system_info.release}")
print(f"Version: {system_info.version}")
print(f"Machine: {system_info.machine}")
print(f"Processor: {system_info.processor}")

# CPU Information
cpu_info = platform.processor()
cpu_count = psutil.cpu_count(logical=False)
logical_cpu_count = psutil.cpu_count(logical=True)

print("\nCPU Information:")
print(f"Processor: {cpu_info}")
print(f"Physical Cores: {cpu_count}")
print(f"Logical Cores: {logical_cpu_count}")

# Memory Information
memory_info = psutil.virtual_memory()

print("\nMemory Information:")
print(f"Total Memory: {memory_info.total // (1024 ** 3)} GB")
print(f"Available Memory: {memory_info.available // (1024 ** 3)} GB")
print(f"Used Memory: {memory_info.used // (1024 ** 3)} GB")
print(f"Memory Utilization: {memory_info.percent}%")

# Disk Information
disk_info = psutil.disk_usage('/')

print("\nDisk Information:")
print(f"Total Disk Space: {disk_info.total // (1024 ** 3)} GB")
print(f"Used Disk Space: {disk_info.used // (1024 ** 3)} GB")
print(f"Free Disk Space: {disk_info.free // (1024 ** 3)} GB")
print(f"Disk Space Utilization: {disk_info.percent}%")

# GPU Information using py3nvml
try:
    nvmlInit()
    gpu_count = nvmlDeviceGetCount()
    if gpu_count == 0:
        print("\nNo GPU detected.")
    else:
        for i in range(gpu_count):
            handle = nvmlDeviceGetHandleByIndex(i)
            name = nvmlDeviceGetName(handle).decode('utf-8')
            memory = nvmlDeviceGetMemoryInfo(handle)
            utilization = nvmlDeviceGetUtilizationRates(handle)
            
            print(f"\nGPU {i + 1} Information:")
            print(f"Name: {name}")
            print(f"Total Memory: {memory.total // (1024 ** 2)} MB")
            print(f"Free Memory: {memory.free // (1024 ** 2)} MB")
            print(f"Used Memory: {memory.used // (1024 ** 2)} MB")
            print(f"GPU Utilization: {utilization.gpu}%")
            print(f"Memory Utilization: {utilization.memory}%")
    nvmlShutdown()
except Exception as e:
    print(f"\nError fetching GPU information: {e}")
