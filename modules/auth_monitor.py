import subprocess
import re


def get_authentication_logs():
    """
    Collect authentication-related logs using journalctl.
    """

    try:
        result = subprocess.run(
            ["journalctl", "--no-pager", "-o", "short-iso"],
            capture_output=True,
            text=True,
            timeout=20
        )

        if result.returncode != 0:
            return []

        return result.stdout.splitlines()

    except Exception as error:
        print(f"Error reading authentication logs: {error}")
        return []


def analyze_authentication_logs():
    """
    Analyze logs for authentication events.
    """

    logs = get_authentication_logs()

    failed = []
    successful = []

    for line in logs:

        lower_line = line.lower()

        if "failed password" in lower_line:
            failed.append(line)

        elif "authentication failure" in lower_line:
            failed.append(line)

        elif "accepted password" in lower_line:
            successful.append(line)

        elif "accepted publickey" in lower_line:
            successful.append(line)

    return {
        "failed_logins": failed,
        "successful_logins": successful
    }


def display_authentication_summary():

    data = analyze_authentication_logs()

    print("\nAuthentication Monitoring")
    print("-" * 40)

    print(f"Failed authentication events : {len(data['failed_logins'])}")
    print(f"Successful authentication     : {len(data['successful_logins'])}")

    return data
