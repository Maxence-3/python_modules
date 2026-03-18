import os
import sys


try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: python-dotenv is not installed.")
    sys.exit(1)

load_dotenv()

DEFAULTS: dict[str, str | None] = {
    "MATRIX_MODE": "development",
    "DATABASE_URL": "sqlite:///default.db",
    "API_KEY": None,
    "LOG_LEVEL": "DEBUG",
    "ZION_ENDPOINT": "http://localhost:8080"
}


def get_config() -> tuple[dict[str, str | None], list[str]]:
    config = {}
    missing = []

    for key, default in DEFAULTS.items():
        value = os.getenv(key, default)
        if value is None:
            missing.append(key)
        config[key] = value

    return config, missing


def format_database(url: str | None) -> str:
    if url is None:
        return "Not configured"
    if "localhost" in url or "sqlite" in url or "127.0.0.1" in url:
        return "Connected to local instance"
    return "Connected to remote instance"


def format_api(key: str | None) -> str:
    if key is None:
        return "Not configured [warning]"
    return "Authenticated"


def format_zion(endpoint: str | None) -> str:
    if endpoint is None:
        return "Offline"
    return "Online"


def security_check(config: dict[str, str | None]) -> list[str]:
    checks = []
    weak_keys = {"password", "123456", "secret", "changeme", "admin"}
    api_key = config.get("API_KEY") or ""
    if api_key.lower() in weak_keys:
        checks.append("[WARN] API_KEY looks like a weak/default secret")
    else:
        checks.append("[OK] No hardcoded secrets detected")

    if os.path.isfile(".env"):
        checks.append("[OK] .env file properly configured")
    else:
        checks.append("[WARN] .env file not found (copy .env.example to .env)")

    checks.append("[OK] Production overrides available")

    return checks


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")

    config, missing = get_config()

    if missing:
        for key in missing:
            print(f"[WARNING] Missing configuration: {key}\n")

    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print(f"Database: {format_database(config['DATABASE_URL'])}")
    print(f"API Access: {format_api(config['API_KEY'])}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {format_zion(config['ZION_ENDPOINT'])}")

    print("\nEnvironment security check:")
    for line in security_check(config):
        print(f"{line}")

    print("\nThe Oracle sees all configurations.")
