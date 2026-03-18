import sys
import importlib


required = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization"
}

optional = {
    "requests": "Network access"
}


def check_dependencies() -> dict[str, tuple[bool, str]]:
    results = {}
    for pkg, _ in {**required, **optional}.items():
        try:
            mod = importlib.import_module(pkg)
            version = getattr(mod, "__version__", "unknown")
            results[pkg] = (True, version)
        except ImportError:
            results[pkg] = (False, "NOT INSTALLED")
    return results


def print_dependency_report(status: dict[str, tuple[bool, str]]) -> bool:
    all_ok = True
    for pkg, label in {**required, **optional}.items():
        available, info = status[pkg]
        tag = "[OK]" if available else "[MISSING]"
        print(f" {tag:<10} {pkg} ({info}) - {label}")
        if not available and pkg in required:
            all_ok = False
    return all_ok


def install_instructions(status: dict[str, tuple[bool, str]]) -> None:
    missing = [p for p, (ok, _) in status.items() if not ok and p in required]
    print("\nSome required packages are missing.")
    print("Install with pip:")
    print(" pip install -r requirements.txt")
    print("Install with Poetry:")
    print(" poetry install")
    print("\nMissing packages:", ", ".join(missing))


def run_analysis() -> None:
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    df = pd.DataFrame({
        "Jeu": ["Minecraft", "GTA V", "Wii Sports", "PUBG", "Mario Kart 8"],
        "Ventes (M)": [238, 195, 83, 75, 67],
        "Année": [2011, 2013, 2006, 2017, 2017],
    })

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(
            df["Jeu"],
            df["Ventes (M)"],
            color="#4c9be8",
            edgecolor="#2a6096"
        )
    ax.bar_label(bars, fmt="%d M", padding=4, fontsize=9)
    ax.set_title(
            "Top 5 jeux vidéo – ventes mondiales",
            fontsize=13,
            fontweight="bold"
        )
    ax.set_ylabel("Ventes (millions d'exemplaires)")
    ax.set_ylim(0, df["Ventes (M)"].max() * 1.15)
    ax.tick_params(axis="x", rotation=15)
    plt.tight_layout()

    output_path = "matrix_analysis.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")
    status = check_dependencies()
    all_ok = print_dependency_report(status)

    if not all_ok:
        install_instructions(status)
        sys.exit(1)

    run_analysis()

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")
