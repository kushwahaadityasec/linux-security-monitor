import shutil


def get_disk_usage():

    total, used, free = shutil.disk_usage("/")

    used_percentage = (used / total) * 100

    return {
        "total_gb": total / (1024 ** 3),
        "used_gb": used / (1024 ** 3),
        "free_gb": free / (1024 ** 3),
        "used_percentage": used_percentage
    }


def display_disk_usage():

    data = get_disk_usage()

    print("\nDisk Usage")
    print("-" * 40)

    print(f"Total : {data['total_gb']:.2f} GB")
    print(f"Used  : {data['used_gb']:.2f} GB")
    print(f"Free  : {data['free_gb']:.2f} GB")
    print(f"Usage : {data['used_percentage']:.2f}%")

    return data
