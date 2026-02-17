import random
from typing import Union, Optional, Dict
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory

class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.creature_names = ['Dragon', 'Goblin', 'Elf', 'Dwarf', 'Orc']
        self.spell_names = ['Fireball', 'Lightning Bolt', 'Ice Storm', 'Heal']
        self.artifacts_names = ['Mana Ring', 'Staff of Power', 'Magic Crystal']
    
    def create_creature(self, name_or_power: Optional[Union[str, int]] = None):
        if isinstance(name_or_power, str):
            name = name_or_power
            power = random.randint(1, 10)
        elif isinstance(name_or_power, int):
            name = random.choice(self.creature_names)
            power = name_or_power
        else:
            name = random.choice(self.creature_names)
            power = random.randint(1, 10)
        
        full_name = f"{name} Warrior" if name == "Goblin" else f"Fire {name}"
        return CreatureCard(full_name, power, "rare", 5, 5)
    
    def create_spell(self, name_or_power: Optional[Union[str, int]] = None):
        if isinstance(name_or_power, str):
            name = name_or_power
            power = random.randint(1, 10)
        elif isinstance(name_or_power, int):
            name = random.choice(self.spell_names)
            power = name_or_power
        else:
            name = random.choice(self.spell_names)
            power = random.randint(1, 10)

        return SpellCard(name, power, "rare", "tkt")
    
    def create_artifact(self, name_or_power: Optional[Union[str, int]] = None):
        if isinstance(name_or_power, str):
            name = name_or_power
            power = random.randint(1, 10)
        elif isinstance(name_or_power, int):
            name = random.choice(self.artifacts_names)
            power = name_or_power
        else:
            name = random.choice(self.artifacts_names)
            power = random.randint(1, 10)

        return ArtifactCard(name, power)
    
    def create_themed_deck(self, size: int) -> Dict:
        deck = {
            'creatures': [],
            'spells': [],
            'artifacts': []
        }

        num_creatures = int(size * 0.5)
        num_spells = int(size * 0.3)
        num_artifacts = size - num_creatures - num_spells

        for _ in range(num_creatures):
            deck['creatures'].append(self.create_creature())
        
        for _ in range(num_spells):
            deck['spells'].append(self.create_spell())
        
        for _ in range(num_artifacts):
            deck['artifacts'].append(self.create_artifact())
        
        return deck

    def get_supported_types(self) -> Dict:
        return {'creatures': ['dragon', 'goblin'], 'spells': ['fireball'], 'artifacts': ['mana_ring']}
