import subprocess


def get_network_information():

    try:

        result = subprocess.run(
            ["ip", "-brief", "address"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return "Unable to retrieve network information."

        return result.stdout.strip()

    except Exception as error:
        return f"Network error: {error}"


def display_network_information():

    network = get_network_information()

    print("\nNetwork Information")
    print("-" * 40)

    print(network)

    return network
