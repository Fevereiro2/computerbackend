import platform
import psutil

def system_info():
    system = platform.system()
    print(f'Operating System: {system}')

    if system == "Linux":
        info = psutil.virtual_memory()
        print(f'Total RAM: {info.total / (1024.0 ** 3):.2f} GB')

        # da print a todos os processos 
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            print(proc.info)
    print(f'Disk: {psutil.disk_io_counters(perdisk=True)}')
    print(f'NetWork: {psutil.net_if_addrs()}')
    print(f'Operating System Version: {platform.release()}')
    print(f'Machine: {platform.machine()}')
    print(f'Processor: {platform.processor()}')