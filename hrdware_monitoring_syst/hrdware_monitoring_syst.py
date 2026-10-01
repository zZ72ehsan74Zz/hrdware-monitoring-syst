import threading, psutil, time
from datetime import datetime

cpu_file, memory_file, disk_file = "cpu.log", "memory.log", "disk.log"


def get_user_input():
    while True:
        try:
            samples, interval = int(input("Enter samples: ")), int(input("Enter interval: "))
            if samples <= 0 or interval < 0:
                print(f"[ERR] samples must be > 0 and interval must be >= 0")
                continue
            return samples, interval
        except ValueError:
            print(f"[ERR] Invalid value, please enter only numbers‼️")


def get_disk_path():
    while True:
        path = input("Enter drive letter (c.d.e.g,...): ").strip().upper()
        full_path = f"{path}:\\"
        try:
            psutil.disk_usage(full_path)
            return full_path
        except Exception:
            print("[ERR] Please enter a valid drive letter (C, D, E, G, ...)‼️")


def get_time_stamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def monitor_cpu(samples, interval, file_name):
    name = threading.current_thread().name
    with open(file_name, "w", encoding="utf-8") as cf:
        psutil.cpu_percent(interval=None)  # warm-up
        for _ in range(samples):
            ts = get_time_stamp()
            cpu = psutil.cpu_percent(interval=None)
            line = f"{ts} | CPU Usage: {cpu}%\n"
            cf.write(line)
            cf.flush()
            time.sleep(interval)

    print(f"Monitor {name} finished✅")


def monitor_memory(samples, interval, file_name):
    name = threading.current_thread().name
    with open(file_name, "w", encoding="utf-8") as mf:
        for _ in range(samples):
            ts = get_time_stamp()
            memory = psutil.virtual_memory()
            percent = memory.percent
            used = memory.used
            total = memory.total
            line = (
                f"{ts} | {name} Usage: {percent}% | "
                f"Used: {used / (1024 ** 3):.2f} GB | "
                f"Total: {total / (1024 ** 3):.2f} GB\n"
            )
            mf.write(line)
            mf.flush()
            time.sleep(interval)

    print(f"Monitor {name} finished✅")


def monitor_disk(samples, interval, path, file_name):
    name = threading.current_thread().name
    with open(file_name, "w", encoding="utf-8") as df:
        for _ in range(samples):
            ts = get_time_stamp()
            disk = psutil.disk_usage(path)
            percent = disk.percent
            used = disk.used
            total = disk.total
            line = (
                f"{ts} | {name} Usage({path}) {percent}% | "
                f"Used: {used / (1024 ** 3):.2f} GB | "
                f"Total: {total / (1024 ** 3):.2f} GB\n"
            )
            df.write(line)
            df.flush()
            time.sleep(interval)

    print(f"Monitor {name} finished✅")


def main():
    samples, interval = get_user_input()
    path = get_disk_path()
    threads = [
        threading.Thread(target=monitor_cpu, args=(samples, interval, cpu_file), name="CPU"),
        threading.Thread(target=monitor_memory, args=(samples, interval, memory_file), name="Memory"),
        threading.Thread(target=monitor_disk, args=(samples, interval, path, disk_file), name="Disk")
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Monitor Main finished. Log files successfully created: cpu.log, memory.log, disk.log✅")


if __name__ == "__main__":
    main()
