from .elements import create_fire, create_water, create_earth

def healing_potion():
    fire = create_fire()
    water = create_water()
    return(f"Healing potion brewed with {fire} and {water}")

def strength_potion():
    fire = create_fire()
    earth = create_earth()
    return(f"Strength potion brewed with {earth} and {fire}")

def invisibility_potion():
    pass

def wisdom_potion():
    pass