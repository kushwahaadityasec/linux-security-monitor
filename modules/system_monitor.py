import platform
import subprocess


def get_system_information():

    information = {}

    information["hostname"] = platform.node()
    information["system"] = platform.system()
    information["release"] = platform.release()
    information["architecture"] = platform.machine()

    try:
        result = subprocess.run(
            ["uptime", "-p"],
            capture_output=True,
            text=True
        )

        information["uptime"] = result.stdout.strip()

    except Exception:
        information["uptime"] = "Unavailable"

    return information


def display_system_information():

    data = get_system_information()

    print("\nSystem Information")
    print("-" * 40)

    for key, value in data.items():
        print(f"{key.title():15}: {value}")

    return data
