def create_new_unit() -> None:
    print("Initializing new storage unit: new_discovery.txt")

    f = open("new_discovery.txt", "w")

    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")

    entry: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]

    for entry_line in entry:
        f.write(entry_line + "\n")
        print(entry_line)
    f.close()

    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    create_new_unit()
