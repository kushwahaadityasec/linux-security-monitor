from datetime import datetime

from modules.system_monitor import (
    display_system_information
)

from modules.auth_monitor import (
    display_authentication_summary
)

from modules.user_monitor import (
    display_users
)

from modules.network_monitor import (
    display_network_information
)

from modules.disk_monitor import (
    display_disk_usage
)

from modules.permission_monitor import (
    display_permission_check
)

from modules.log_analyzer import (
    generate_alerts,
    display_alerts
)


def generate_report(
    system,
    authentication,
    users,
    network,
    disk,
    permissions,
    alerts
):

    filename = (
        "reports/security_report_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".txt"
    )

    with open(filename, "w") as report:

        report.write("=" * 60 + "\n")
        report.write("LINUX SECURITY MONITORING REPORT\n")
        report.write("=" * 60 + "\n\n")

        report.write(
            "Generated: "
            + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + "\n\n"
        )

        report.write("SYSTEM INFORMATION\n")
        report.write("-" * 40 + "\n")

        for key, value in system.items():

            report.write(
                f"{key.title():15}: {value}\n"
            )

        report.write("\nAUTHENTICATION\n")
        report.write("-" * 40 + "\n")

        report.write(
            f"Failed events    : "
            f"{len(authentication['failed_logins'])}\n"
        )

        report.write(
            f"Successful events: "
            f"{len(authentication['successful_logins'])}\n"
        )

        report.write("\nLOGGED-IN USERS\n")
        report.write("-" * 40 + "\n")

        for user in users:

            report.write(user + "\n")

        report.write("\nNETWORK INFORMATION\n")
        report.write("-" * 40 + "\n")

        report.write(network + "\n")

        report.write("\nDISK USAGE\n")
        report.write("-" * 40 + "\n")

        report.write(
            f"Total : {disk['total_gb']:.2f} GB\n"
        )

        report.write(
            f"Used  : {disk['used_gb']:.2f} GB\n"
        )

        report.write(
            f"Free  : {disk['free_gb']:.2f} GB\n"
        )

        report.write(
            f"Usage : {disk['used_percentage']:.2f}%\n"
        )

        report.write("\nPERMISSION CHECK\n")
        report.write("-" * 40 + "\n")

        report.write(
            f"File       : {permissions['path']}\n"
        )

        report.write(
            f"Exists     : {permissions['exists']}\n"
        )

        if permissions["exists"]:

            report.write(
                f"Permissions: "
                f"{permissions['permissions']}\n"
            )

        report.write("\nSECURITY ALERTS\n")
        report.write("-" * 40 + "\n")

        for alert in alerts:

            report.write(
                f"[{alert['severity']}] "
                f"{alert['message']}\n"
            )

    return filename


def main():

    print("\n")
    print("=" * 60)
    print("       LINUX SECURITY MONITOR")
    print("=" * 60)

    system = display_system_information()

    authentication = display_authentication_summary()

    users = display_users()

    network = display_network_information()

    disk = display_disk_usage()

    permissions = display_permission_check()

    alerts = generate_alerts(authentication)

    display_alerts(alerts)

    report = generate_report(
        system,
        authentication,
        users,
        network,
        disk,
        permissions,
        alerts
    )

    print("\n")
    print("=" * 60)
    print("Security report generated:")
    print(report)
    print("=" * 60)


if __name__ == "__main__":
    main()
