def open_file():
    print("Initiating secure vault access...")
    with open("data.txt", "r") as file:
        print("Vault connection established with failsafe protocols\n")
        content = file.read()
        print("SECURE EXTRACTION:")
        print(content)
    with open("data.txt", "w") as file:
        file.write("[CLASSIFIED] New security protocols archived")
    with open("data.txt", "r") as file:
        content = file.read()
        print("\nSECURE PRESERVATION:")
        print(content)
        print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    open_file()