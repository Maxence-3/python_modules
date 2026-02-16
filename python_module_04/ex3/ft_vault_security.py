def open_file() -> None:
    print("Initiating secure vault access...")
    with open("data.txt", "r") as file:
        print("Vault connection established with failsafe protocols\n")
        content: str = file.read()
        print("SECURE EXTRACTION:")
        print(content)
    data: str = "[CLASSIFIED] New security protocols archived"
    with open("data.txt", "w") as file:
        file.write(data)
    print("\nSECURE PRESERVATION:")
    print(data)
    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    open_file()
