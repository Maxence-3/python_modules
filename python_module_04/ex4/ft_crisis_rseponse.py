def open_file(input_file: str) -> None:
    try:
        with open(input_file, "r") as file:
            _: str = file.read()
        print(f"ROUTINE ACCESS: Attempting access to '{input_file}'")
        print("SUCCESS: Archive recovered - \
''Knowledge preserved for humanity''")
        print("STATUS: Normal operation resumed\n")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attemping access to '{input_file}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print(f"CRISIS ALERT: Attemping access to '{input_file}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    open_file("lost_archive.txt")
    open_file("classified_vault.txt")
    open_file("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")
