import time
import platform
import requests
import psutil
from colorama import Fore, Style, init

init(autoreset=True)


def print_header():
    print(Fore.CYAN + "=" * 40)
    print(Fore.CYAN + " VS Code Netbook Test App")
    print(Fore.CYAN + "=" * 40)


def system_info():
    print(Fore.YELLOW + "\nSystem information:")
    print("OS:", platform.system(), platform.release())
    print("Python:", platform.python_version())
    print("CPU cores:", psutil.cpu_count(logical=True))
    print("RAM total:", round(psutil.virtual_memory().total / 1024 / 1024, 1), "MB")


def cpu_test():
    print(Fore.YELLOW + "\nCPU test (simple loop)...")
    start = time.time()

    total = 0
    for i in range(5_000_000):
        total += i

    duration = time.time() - start
    print("Result:", total)
    print("Time:", round(duration, 2), "seconds")


def memory_test():
    print(Fore.YELLOW + "\nMemory usage:")
    mem = psutil.virtual_memory()
    print("Used:", round(mem.used / 1024 / 1024, 1), "MB")
    print("Available:", round(mem.available / 1024 / 1024, 1), "MB")


def network_test():
    print(Fore.YELLOW + "\nNetwork test (HTTP request)...")
    try:
        response = requests.get("https://httpbin.org/get", timeout=5)
        print("Status code:", response.status_code)
        print("Response size:", len(response.text), "chars")
    except requests.RequestException as e:
        print(Fore.RED + "Network error:", e)


def main():
    print_header()
    system_info()
    cpu_test()
    memory_test()
    network_test()
    print(Fore.GREEN + "\nTest completed successfully ✔")


if __name__ == "__main__":
    main()
