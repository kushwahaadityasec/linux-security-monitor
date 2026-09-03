import os
import stat


def check_file_permissions(path):

    if not os.path.exists(path):

        return {
            "path": path,
            "exists": False
        }

    permissions = stat.filemode(os.stat(path).st_mode)

    return {
        "path": path,
        "exists": True,
        "permissions": permissions
    }


def display_permission_check(path="/etc/passwd"):

    result = check_file_permissions(path)

    print("\nFile Permission Check")
    print("-" * 40)

    print(f"File       : {result['path']}")
    print(f"Exists     : {result['exists']}")

    if result["exists"]:
        print(f"Permissions: {result['permissions']}")

    return result
