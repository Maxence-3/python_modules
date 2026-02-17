import alchemy

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    result = alchemy.elements.create_fire()
    print(f"alchemy.elements.create_fire(): {result}")
    result = alchemy.elements.create_water()
    print(f"alchemy.elements.create_water(): {result}")
    result = alchemy.elements.create_earth()
    print(f"alchemy.elements.create_earth(): {result}")
    result = alchemy.elements.create_air()
    print(f"alchemy.elements.create_air(): {result}")

    print("\nTesting package-level access (controlled by __init__.py)")
    try:
        result = alchemy.create_fire()
        print(f"alchemy.create_fire(): {result}")
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        result = alchemy.create_water()
        print(f"alchemy.create_water(): {result}")
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_earth(): ", end="")
        alchemy.create_earth()
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_air(): ", end="")
        alchemy.create_air()
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
