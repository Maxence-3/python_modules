import sys


def chanel_communication_tester() -> None:
    archivist_id: str = input("Input Stream active. Enter archivist ID: ")
    status_report: str = input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"\n[STANDARD] Archive status from \
{archivist_id}: {status_report}\n")
    sys.stderr.write("[ALERT] System diagnostic: \
Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    chanel_communication_tester()
    print("\nThree-channel communication test successful.")
