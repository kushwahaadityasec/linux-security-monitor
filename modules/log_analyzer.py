from config import FAILED_LOGIN_THRESHOLD


def generate_alerts(auth_data):

    alerts = []

    failed_count = len(auth_data["failed_logins"])

    if failed_count >= FAILED_LOGIN_THRESHOLD:

        alerts.append({
            "severity": "HIGH",
            "message": (
                f"Multiple authentication failures detected: "
                f"{failed_count} events"
            )
        })

    elif failed_count > 0:

        alerts.append({
            "severity": "MEDIUM",
            "message": (
                f"Authentication failures detected: "
                f"{failed_count} events"
            )
        })

    else:

        alerts.append({
            "severity": "LOW",
            "message": "No authentication failures detected."
        })

    return alerts


def display_alerts(alerts):

    print("\nSecurity Alerts")
    print("-" * 40)

    for alert in alerts:

        print(
            f"[{alert['severity']}] "
            f"{alert['message']}"
        )
