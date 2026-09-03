import subprocess


def get_logged_in_users():

    try:
        result = subprocess.run(
            ["who"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return []

        lines = result.stdout.strip().splitlines()

        return lines

    except Exception as error:
        print(f"Error reading users: {error}")
        return []


def display_users():

    users = get_logged_in_users()

    print("\nCurrently Logged-In Users")
    print("-" * 40)

    if not users:
        print("No logged-in users found.")
    else:
        for user in users:
            print(user)

    return users
