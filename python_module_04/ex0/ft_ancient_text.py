def recover_ancient_text() -> None:
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        f = open("ancient_fragment.txt", "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    finally:
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    recover_ancient_text()
