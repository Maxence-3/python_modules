import alchemy

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): ", end="")
    alchemy.elements.create_fire()
    print(f"alchemy.elements.create_water(): ", end="")
    alchemy.elements.create_water()
    print(f"alchemy.elements.create_earth(): ", end="")
    alchemy.elements.create_earth()
    print(f"alchemy.elements.create_air(): ", end="")
    alchemy.elements.create_air()

    print("\nTesting package-level access (controlled by __init__.py)")
    try:
        print("alchemy.create_fire(): ", end="")
        alchemy.create_fire()
    except AttributeError as e:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_water(): ", end="")
        alchemy.create_water()
    except AttributeError as e:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_earth(): ", end="")
        alchemy.create_earth()
    except AttributeError as e:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_air(): ", end="")
        alchemy.create_air()
    except AttributeError as e:
        print("AttributeError - not exposed")

print("\nPackage metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")