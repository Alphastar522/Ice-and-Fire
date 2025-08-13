import math
import random

# Starter Pokémon data: name, evolutions, base stats, evolution levels
STARTERS = {
    # Kanto
    "Bulbasaur": [
        {"name": "Bulbasaur", "base_stats": {"HP": 45, "Attack": 49, "Defense": 49, "Sp. Atk": 65, "Sp. Def": 65, "Speed": 45}, "evo_level": 16},
        {"name": "Ivysaur", "base_stats": {"HP": 60, "Attack": 62, "Defense": 63, "Sp. Atk": 80, "Sp. Def": 80, "Speed": 60}, "evo_level": 32},
        {"name": "Venusaur", "base_stats": {"HP": 80, "Attack": 82, "Defense": 83, "Sp. Atk": 100, "Sp. Def": 100, "Speed": 80}, "evo_level": None},
    ],
    "Charmander": [
        {"name": "Charmander", "base_stats": {"HP": 39, "Attack": 52, "Defense": 43, "Sp. Atk": 60, "Sp. Def": 50, "Speed": 65}, "evo_level": 16},
        {"name": "Charmeleon", "base_stats": {"HP": 58, "Attack": 64, "Defense": 58, "Sp. Atk": 80, "Sp. Def": 65, "Speed": 80}, "evo_level": 36},
        {"name": "Charizard", "base_stats": {"HP": 78, "Attack": 84, "Defense": 78, "Sp. Atk": 109, "Sp. Def": 85, "Speed": 100}, "evo_level": None},
    ],
    "Squirtle": [
        {"name": "Squirtle", "base_stats": {"HP": 44, "Attack": 48, "Defense": 65, "Sp. Atk": 50, "Sp. Def": 64, "Speed": 43}, "evo_level": 16},
        {"name": "Wartortle", "base_stats": {"HP": 59, "Attack": 63, "Defense": 80, "Sp. Atk": 65, "Sp. Def": 80, "Speed": 58}, "evo_level": 36},
        {"name": "Blastoise", "base_stats": {"HP": 79, "Attack": 83, "Defense": 100, "Sp. Atk": 85, "Sp. Def": 105, "Speed": 78}, "evo_level": None},
    ],
    # Johto
    "Chikorita": [
        {"name": "Chikorita", "base_stats": {"HP": 45, "Attack": 49, "Defense": 65, "Sp. Atk": 49, "Sp. Def": 65, "Speed": 45}, "evo_level": 16},
        {"name": "Bayleef", "base_stats": {"HP": 60, "Attack": 62, "Defense": 80, "Sp. Atk": 63, "Sp. Def": 80, "Speed": 60}, "evo_level": 32},
        {"name": "Meganium", "base_stats": {"HP": 80, "Attack": 82, "Defense": 100, "Sp. Atk": 83, "Sp. Def": 100, "Speed": 80}, "evo_level": None},
    ],
    "Cyndaquil": [
        {"name": "Cyndaquil", "base_stats": {"HP": 39, "Attack": 52, "Defense": 43, "Sp. Atk": 60, "Sp. Def": 50, "Speed": 65}, "evo_level": 14},
        {"name": "Quilava", "base_stats": {"HP": 58, "Attack": 64, "Defense": 58, "Sp. Atk": 80, "Sp. Def": 65, "Speed": 80}, "evo_level": 36},
        {"name": "Typhlosion", "base_stats": {"HP": 78, "Attack": 84, "Defense": 78, "Sp. Atk": 109, "Sp. Def": 85, "Speed": 100}, "evo_level": None},
    ],
    "Totodile": [
        {"name": "Totodile", "base_stats": {"HP": 50, "Attack": 65, "Defense": 64, "Sp. Atk": 44, "Sp. Def": 48, "Speed": 43}, "evo_level": 18},
        {"name": "Croconaw", "base_stats": {"HP": 65, "Attack": 80, "Defense": 80, "Sp. Atk": 59, "Sp. Def": 63, "Speed": 58}, "evo_level": 30},
        {"name": "Feraligatr", "base_stats": {"HP": 85, "Attack": 105, "Defense": 100, "Sp. Atk": 79, "Sp. Def": 83, "Speed": 78}, "evo_level": None},
    ],
    # Sinnoh
    "Turtwig": [
        {"name": "Turtwig", "base_stats": {"HP": 55, "Attack": 68, "Defense": 64, "Sp. Atk": 45, "Sp. Def": 55, "Speed": 31}, "evo_level": 18},
        {"name": "Grotle", "base_stats": {"HP": 75, "Attack": 89, "Defense": 85, "Sp. Atk": 55, "Sp. Def": 65, "Speed": 36}, "evo_level": 32},
        {"name": "Torterra", "base_stats": {"HP": 95, "Attack": 109, "Defense": 105, "Sp. Atk": 75, "Sp. Def": 85, "Speed": 56}, "evo_level": None},
    ],
    "Chimchar": [
        {"name": "Chimchar", "base_stats": {"HP": 44, "Attack": 58, "Defense": 44, "Sp. Atk": 58, "Sp. Def": 44, "Speed": 61}, "evo_level": 14},
        {"name": "Monferno", "base_stats": {"HP": 64, "Attack": 78, "Defense": 52, "Sp. Atk": 78, "Sp. Def": 52, "Speed": 81}, "evo_level": 36},
        {"name": "Infernape", "base_stats": {"HP": 76, "Attack": 104, "Defense": 71, "Sp. Atk": 104, "Sp. Def": 71, "Speed": 108}, "evo_level": None},
    ],
    "Piplup": [
        {"name": "Piplup", "base_stats": {"HP": 53, "Attack": 51, "Defense": 53, "Sp. Atk": 61, "Sp. Def": 56, "Speed": 40}, "evo_level": 16},
        {"name": "Prinplup", "base_stats": {"HP": 64, "Attack": 66, "Defense": 68, "Sp. Atk": 81, "Sp. Def": 76, "Speed": 50}, "evo_level": 36},
        {"name": "Empoleon", "base_stats": {"HP": 84, "Attack": 86, "Defense": 88, "Sp. Atk": 111, "Sp. Def": 101, "Speed": 60}, "evo_level": None},
    ],
    # Unova
    "Snivy": [
        {"name": "Snivy", "base_stats": {"HP": 45, "Attack": 45, "Defense": 55, "Sp. Atk": 45, "Sp. Def": 55, "Speed": 63}, "evo_level": 17},
        {"name": "Servine", "base_stats": {"HP": 60, "Attack": 60, "Defense": 75, "Sp. Atk": 60, "Sp. Def": 75, "Speed": 83}, "evo_level": 36},
        {"name": "Serperior", "base_stats": {"HP": 75, "Attack": 75, "Defense": 95, "Sp. Atk": 75, "Sp. Def": 95, "Speed": 113}, "evo_level": None},
    ],
    "Tepig": [
        {"name": "Tepig", "base_stats": {"HP": 65, "Attack": 63, "Defense": 45, "Sp. Atk": 45, "Sp. Def": 45, "Speed": 45}, "evo_level": 17},
        {"name": "Pignite", "base_stats": {"HP": 90, "Attack": 93, "Defense": 55, "Sp. Atk": 70, "Sp. Def": 55, "Speed": 55}, "evo_level": 36},
        {"name": "Emboar", "base_stats": {"HP": 110, "Attack": 123, "Defense": 65, "Sp. Atk": 100, "Sp. Def": 65, "Speed": 65}, "evo_level": None},
    ],
    "Oshawott": [
        {"name": "Oshawott", "base_stats": {"HP": 55, "Attack": 55, "Defense": 45, "Sp. Atk": 63, "Sp. Def": 45, "Speed": 45}, "evo_level": 17},
        {"name": "Dewott", "base_stats": {"HP": 75, "Attack": 75, "Defense": 60, "Sp. Atk": 83, "Sp. Def": 60, "Speed": 60}, "evo_level": 36},
        {"name": "Samurott", "base_stats": {"HP": 95, "Attack": 100, "Defense": 85, "Sp. Atk": 108, "Sp. Def": 70, "Speed": 70}, "evo_level": None},
    ],
    # Kalos
    "Chespin": [
        {"name": "Chespin", "base_stats": {"HP": 56, "Attack": 61, "Defense": 65, "Sp. Atk": 48, "Sp. Def": 45, "Speed": 38}, "evo_level": 16},
        {"name": "Quilladin", "base_stats": {"HP": 61, "Attack": 78, "Defense": 95, "Sp. Atk": 56, "Sp. Def": 58, "Speed": 57}, "evo_level": 36},
        {"name": "Chesnaught", "base_stats": {"HP": 88, "Attack": 107, "Defense": 122, "Sp. Atk": 74, "Sp. Def": 75, "Speed": 64}, "evo_level": None},
    ],
    "Fennekin": [
        {"name": "Fennekin", "base_stats": {"HP": 40, "Attack": 45, "Defense": 40, "Sp. Atk": 62, "Sp. Def": 60, "Speed": 60}, "evo_level": 16},
        {"name": "Braixen", "base_stats": {"HP": 59, "Attack": 59, "Defense": 58, "Sp. Atk": 90, "Sp. Def": 70, "Speed": 73}, "evo_level": 36},
        {"name": "Delphox", "base_stats": {"HP": 75, "Attack": 69, "Defense": 72, "Sp. Atk": 114, "Sp. Def": 100, "Speed": 104}, "evo_level": None},
    ],
    "Froakie": [
        {"name": "Froakie", "base_stats": {"HP": 41, "Attack": 56, "Defense": 40, "Sp. Atk": 62, "Sp. Def": 44, "Speed": 71}, "evo_level": 16},
        {"name": "Frogadier", "base_stats": {"HP": 54, "Attack": 63, "Defense": 52, "Sp. Atk": 83, "Sp. Def": 56, "Speed": 97}, "evo_level": 36},
        {"name": "Greninja", "base_stats": {"HP": 72, "Attack": 95, "Defense": 67, "Sp. Atk": 103, "Sp. Def": 71, "Speed": 122}, "evo_level": None},
    ],
    # Alola
    "Rowlet": [
        {"name": "Rowlet", "base_stats": {"HP": 68, "Attack": 55, "Defense": 55, "Sp. Atk": 50, "Sp. Def": 50, "Speed": 42}, "evo_level": 17},
        {"name": "Dartrix", "base_stats": {"HP": 78, "Attack": 75, "Defense": 75, "Sp. Atk": 70, "Sp. Def": 70, "Speed": 52}, "evo_level": 34},
        {"name": "Decidueye", "base_stats": {"HP": 78, "Attack": 107, "Defense": 75, "Sp. Atk": 100, "Sp. Def": 100, "Speed": 70}, "evo_level": None},
    ],
    "Litten": [
        {"name": "Litten", "base_stats": {"HP": 45, "Attack": 65, "Defense": 40, "Sp. Atk": 60, "Sp. Def": 40, "Speed": 70}, "evo_level": 17},
        {"name": "Torracat", "base_stats": {"HP": 65, "Attack": 85, "Defense": 50, "Sp. Atk": 80, "Sp. Def": 50, "Speed": 90}, "evo_level": 34},
        {"name": "Incineroar", "base_stats": {"HP": 95, "Attack": 115, "Defense": 90, "Sp. Atk": 80, "Sp. Def": 90, "Speed": 60}, "evo_level": None},
    ],
    "Popplio": [
        {"name": "Popplio", "base_stats": {"HP": 50, "Attack": 54, "Defense": 54, "Sp. Atk": 66, "Sp. Def": 56, "Speed": 40}, "evo_level": 17},
        {"name": "Brionne", "base_stats": {"HP": 60, "Attack": 69, "Defense": 69, "Sp. Atk": 91, "Sp. Def": 81, "Speed": 50}, "evo_level": 34},
        {"name": "Primarina", "base_stats": {"HP": 80, "Attack": 74, "Defense": 74, "Sp. Atk": 126, "Sp. Def": 116, "Speed": 60}, "evo_level": None},
    ],
    # Galar
    "Grookey": [
        {"name": "Grookey", "base_stats": {"HP": 50, "Attack": 65, "Defense": 50, "Sp. Atk": 40, "Sp. Def": 40, "Speed": 65}, "evo_level": 16},
        {"name": "Thwackey", "base_stats": {"HP": 70, "Attack": 85, "Defense": 70, "Sp. Atk": 55, "Sp. Def": 60, "Speed": 80}, "evo_level": 35},
        {"name": "Rillaboom", "base_stats": {"HP": 100, "Attack": 125, "Defense": 90, "Sp. Atk": 60, "Sp. Def": 70, "Speed": 85}, "evo_level": None},
    ],
    "Scorbunny": [
        {"name": "Scorbunny", "base_stats": {"HP": 50, "Attack": 71, "Defense": 40, "Sp. Atk": 40, "Sp. Def": 40, "Speed": 69}, "evo_level": 16},
        {"name": "Raboot", "base_stats": {"HP": 65, "Attack": 86, "Defense": 60, "Sp. Atk": 55, "Sp. Def": 60, "Speed": 94}, "evo_level": 35},
        {"name": "Cinderace", "base_stats": {"HP": 80, "Attack": 116, "Defense": 75, "Sp. Atk": 65, "Sp. Def": 75, "Speed": 119}, "evo_level": None},
    ],
    "Sobble": [
        {"name": "Sobble", "base_stats": {"HP": 50, "Attack": 40, "Defense": 40, "Sp. Atk": 70, "Sp. Def": 40, "Speed": 70}, "evo_level": 16},
        {"name": "Drizzile", "base_stats": {"HP": 65, "Attack": 60, "Defense": 55, "Sp. Atk": 95, "Sp. Def": 55, "Speed": 90}, "evo_level": 35},
        {"name": "Inteleon", "base_stats": {"HP": 70, "Attack": 85, "Defense": 65, "Sp. Atk": 125, "Sp. Def": 65, "Speed": 120}, "evo_level": None},
    ],
    # All Eevee and its evolutions.
    "Eevee": [
        {"name": "Eevee", "base_stats": {"HP": 55, "Attack": 55, "Defense": 50, "Sp. Atk": 45, "Sp. Def": 65, "Speed": 55}, "evo_level": None},
        {"name": "Vaporeon", "base_stats": {"HP": 130, "Attack": 65, "Defense": 60, "Sp. Atk": 110, "Sp. Def": 95, "Speed": 65}, "evo_level": 1},
        {"name": "Jolteon", "base_stats": {"HP": 65, "Attack": 65, "Defense": 60, "Sp. Atk": 110, "Sp. Def": 95, "Speed": 130}, "evo_level": 1},
        {"name": "Flareon", "base_stats": {"HP": 65, "Attack": 130, "Defense": 60, "Sp. Atk": 95, "Sp. Def": 110, "Speed": 65}, "evo_level": 1},
        {"name": "Espeon", "base_stats": {"HP": 65, "Attack": 65, "Defense": 60, "Sp. Atk": 130, "Sp. Def": 95, "Speed": 110}, "evo_level": 1},
        {"name": "Umbreon", "base_stats": {"HP": 95, "Attack": 65, "Defense": 110, "Sp. Atk": 60, "Sp. Def": 130, "Speed": 65}, "evo_level": 1},
        {"name": "Leafeon", "base_stats": {"HP": 65, "Attack": 110, "Defense": 130, "Sp. Atk": 60, "Sp. Def": 65, "Speed": 95}, "evo_level": 1},
        {"name": "Glaceon", "base_stats": {"HP": 65, "Attack": 60, "Defense": 110, "Sp. Atk": 130, "Sp. Def": 95, "Speed": 65}, "evo_level": 1},
        {"name": "Sylveon", "base_stats": {"HP": 95, "Attack": 65, "Defense": 65, "Sp. Atk": 110, "Sp. Def": 130, "Speed": 60}, "evo_level": 1},
    ],
}

# EV yield data for a selection of common Kanto Pokémon
# Format: "Pokémon_name": {"stat": ev_amount}
EV_YIELDS = {
    "Caterpie": {"HP": 1},
    "Weedle": {"Speed": 1},
    "Pidgey": {"Speed": 1},
    "Rattata": {"Speed": 1},
    "Spearow": {"Speed": 1},
    "Ekans": {"Attack": 1},
    "Pikachu": {"Speed": 2},
    "Sandshrew": {"Defense": 1},
    "Nidoran(f)": {"HP": 1},
    "Nidoran(m)": {"Attack": 1},
    "Clefairy": {"HP": 2},
    "Vulpix": {"Speed": 1},
    "Jigglypuff": {"HP": 2},
    "Zubat": {"Speed": 1},
    "Oddish": {"Sp. Atk": 1},
    "Paras": {"Attack": 1},
    "Venonat": {"Sp. Def": 1},
    "Diglett": {"Speed": 1},
    "Meowth": {"Speed": 1},
    "Psyduck": {"Sp. Atk": 1},
    "Mankey": {"Attack": 1},
    "Growlithe": {"Attack": 1},
    "Poliwag": {"Speed": 1},
    "Abra": {"Sp. Atk": 1},
    "Machop": {"Attack": 1},
    "Bellsprout": {"Attack": 1},
    "Tentacool": {"Sp. Def": 1},
    "Geodude": {"Defense": 1},
    "Magnemite": {"Sp. Atk": 1},
    "Farfetch'd": {"Attack": 1},
    "Doduo": {"Attack": 1},
    "Seel": {"Sp. Def": 1},
    "Grimer": {"HP": 1},
    "Shellder": {"Defense": 1},
    "Gastly": {"Sp. Atk": 1},
    "Onix": {"Defense": 1},
    "Drowzee": {"HP": 1},
    "Krabby": {"Attack": 1},
    "Voltorb": {"Speed": 1},
    "Exeggcute": {"HP": 1},
    "Cubone": {"Defense": 1},
    "Lickitung": {"HP": 2},
    "Koffing": {"Defense": 1},
    "Rhyhorn": {"Attack": 1},
    "Chansey": {"HP": 2},
    "Horsea": {"Sp. Atk": 1},
    "Goldeen": {"Attack": 1},
    "Staryu": {"Speed": 1},
    "Scyther": {"Attack": 1},
    "Magikarp": {"Speed": 1},
    "Eevee": {"Sp. Def": 1},
    "Porygon": {"Sp. Atk": 1},
    "Omanyte": {"Defense": 1},
    "Kabuto": {"Defense": 1},
    "Aerodactyl": {"Speed": 1},
    "Snorlax": {"HP": 2},
    "Dratini": {"Attack": 1},
}

# Complete nature data with stat multipliers
NATURES = {
    # Natures that boost Attack
    "Lonely": {"Attack": 1.1, "Defense": 0.9, "HP": 1.0, "Sp. Atk": 1.0, "Sp. Def": 1.0, "Speed": 1.0},
    "Adamant": {"Attack": 1.1, "Sp. Atk": 0.9, "HP": 1.0, "Defense": 1.0, "Sp. Def": 1.0, "Speed": 1.0},
    "Naughty": {"Attack": 1.1, "Sp. Def": 0.9, "HP": 1.0, "Defense": 1.0, "Sp. Atk": 1.0, "Speed": 1.0},
    "Brave": {"Attack": 1.1, "Speed": 0.9, "HP": 1.0, "Defense": 1.0, "Sp. Atk": 1.0, "Sp. Def": 1.0},

    # Natures that boost Defense
    "Bold": {"Defense": 1.1, "Attack": 0.9, "HP": 1.0, "Sp. Atk": 1.0, "Sp. Def": 1.0, "Speed": 1.0},
    "Relaxed": {"Defense": 1.1, "Speed": 0.9, "HP": 1.0, "Attack": 1.0, "Sp. Atk": 1.0, "Sp. Def": 1.0},
    "Impish": {"Defense": 1.1, "Sp. Atk": 0.9, "HP": 1.0, "Attack": 1.0, "Sp. Def": 1.0, "Speed": 1.0},
    "Lax": {"Defense": 1.1, "Sp. Def": 0.9, "HP": 1.0, "Attack": 1.0, "Sp. Atk": 1.0, "Speed": 1.0},

    # Natures that boost Special Attack
    "Timid": {"Speed": 1.1, "Attack": 0.9, "HP": 1.0, "Defense": 1.0, "Sp. Atk": 1.0, "Sp. Def": 1.0},
    "Hasty": {"Speed": 1.1, "Defense": 0.9, "HP": 1.0, "Attack": 1.0, "Sp. Atk": 1.0, "Sp. Def": 1.0},
    "Jolly": {"Speed": 1.1, "Sp. Atk": 0.9, "HP": 1.0, "Attack": 1.0, "Defense": 1.0, "Sp. Def": 1.0},
    "Naive": {"Speed": 1.1, "Sp. Def": 0.9, "HP": 1.0, "Attack": 1.0, "Defense": 1.0, "Sp. Atk": 1.0},

    # Natures that boost Special Defense
    "Modest": {"Sp. Atk": 1.1, "Attack": 0.9, "HP": 1.0, "Defense": 1.0, "Sp. Def": 1.0, "Speed": 1.0},
    "Mild": {"Sp. Atk": 1.1, "Defense": 0.9, "HP": 1.0, "Attack": 1.0, "Sp. Def": 1.0, "Speed": 1.0},
    "Rash": {"Sp. Atk": 1.1, "Sp. Def": 0.9, "HP": 1.0, "Attack": 1.0, "Defense": 1.0, "Speed": 1.0},
    "Quiet": {"Sp. Atk": 1.1, "Speed": 0.9, "HP": 1.0, "Attack": 1.0, "Defense": 1.0, "Sp. Def": 1.0},
    
    # Natures that boost Speed
    "Calm": {"Sp. Def": 1.1, "Attack": 0.9, "HP": 1.0, "Defense": 1.0, "Sp. Atk": 1.0, "Speed": 1.0},
    "Gentle": {"Sp. Def": 1.1, "Defense": 0.9, "HP": 1.0, "Attack": 1.0, "Sp. Atk": 1.0, "Speed": 1.0},
    "Sassy": {"Sp. Def": 1.1, "Speed": 0.9, "HP": 1.0, "Attack": 1.0, "Defense": 1.0, "Sp. Atk": 1.0},
    "Careful": {"Sp. Def": 1.1, "Sp. Atk": 0.9, "HP": 1.0, "Attack": 1.0, "Defense": 1.0, "Speed": 1.0},

    # Neutral Natures (no stat changes)
    "Hardy": {"HP": 1.0, "Attack": 1.0, "Defense": 1.0, "Sp. Atk": 1.0, "Sp. Def": 1.0, "Speed": 1.0},
    "Docile": {"HP": 1.0, "Attack": 1.0, "Defense": 1.0, "Sp. Atk": 1.0, "Sp. Def": 1.0, "Speed": 1.0},
    "Serious": {"HP": 1.0, "Attack": 1.0, "Defense": 1.0, "Sp. Atk": 1.0, "Sp. Def": 1.0, "Speed": 1.0},
    "Bashful": {"HP": 1.0, "Attack": 1.0, "Defense": 1.0, "Sp. Atk": 1.0, "Sp. Def": 1.0, "Speed": 1.0},
    "Quirky": {"HP": 1.0, "Attack": 1.0, "Defense": 1.0, "Sp. Atk": 1.0, "Sp. Def": 1.0, "Speed": 1.0},
}


def calc_realistic_stat(base, level, iv, ev, nature_multiplier, is_hp=False):
    """
    Calculates a Pokémon's real stat based on its base stat, level, IVs, EVs, and nature.
    This formula is valid for Generation 3 games and newer.
    """
    ev_modifier = ev // 4
    core_stat = math.floor(0.01 * (2 * base + iv + ev_modifier) * level)
    
    if is_hp:
        return core_stat + level + 10
    else:
        return math.floor((core_stat + 5) * nature_multiplier)


def get_stats(pokemon, level, ivs, evs, nature):
    """
    Calculates all stats for a Pokémon at a given level, with specified IVs, EVs, and nature.
    """
    stats = {}
    nature_multipliers = NATURES.get(nature, {})
    
    for stat, base in pokemon["base_stats"].items():
        iv = ivs.get(stat, 0)
        ev = evs.get(stat, 0)
        nature_multiplier = nature_multipliers.get(stat, 1.0)
        
        if stat == "HP":
            stats[stat] = calc_realistic_stat(base, level, iv, ev, 1.0, is_hp=True)
        else:
            stats[stat] = calc_realistic_stat(base, level, iv, ev, nature_multiplier)
            
    return stats


def main():
    """
    Main function to run the Pokéstat program with battle record EV input.
    """
    print("Welcome to the Pokéstat program! Please select a Pokémon.")
    print("Available Pokémon:")
    for name in STARTERS:
        print(f"- {name}")

    starter_input = input("Enter Pokémon name: ")
    starter_input_clean = starter_input.strip().lower().replace(' ', '')
    starter = None
    for key in STARTERS:
        key_clean = key.lower().replace(' ', '')
        if starter_input_clean == key_clean:
            starter = key
            break

    if not starter:
        print("Invalid Pokémon name. Please try again.")
        return

    # Get level with validation
    while True:
        try:
            level = int(input("Enter level (1-100): "))
            if not (1 <= level <= 100):
                raise ValueError
            break
        except ValueError:
            print("Invalid level. Please enter a number between 1 and 100.")

    # Randomly generate IVs
    ivs = {}
    for stat in ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]:
        ivs[stat] = random.randint(0, 31)

    # Randomly generate a nature
    nature = random.choice(list(NATURES.keys()))

    # Get battle record to determine EVs
    evs = {stat: 0 for stat in ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]}
    total_evs = 0
    print("\nNow, enter the Pokémon you have defeated. Type 'done' to finish.")
    
    while True:
        if total_evs >= 510:
            print("You have reached the maximum of 510 EVs!")
            break
        
        battle_input = input("Enter Pokémon defeated ('done' to finish): ")
        battle_input = battle_input.strip()
        
        if battle_input.lower() == 'done':
            break

        battled_pokemon_evs = EV_YIELDS.get(battle_input)
        if battled_pokemon_evs:
            for stat, ev_gain in battled_pokemon_evs.items():
                if evs[stat] < 252:
                    evs[stat] += ev_gain
                    total_evs += ev_gain
                    if evs[stat] > 252:
                        overage = evs[stat] - 252
                        evs[stat] = 252
                        total_evs -= overage
                        print(f"** {stat} EV reached the maximum of 252. Overage was removed. **")
                    if total_evs > 510:
                        overage = total_evs - 510
                        evs[stat] -= overage
                        total_evs = 510
                        print(f"** Total EVs reached the maximum of 510. Overage was removed. **")
        else:
            print("Invalid Pokémon name. Please try again.")

    # Eevee evolution logic
    if starter == "Eevee":
        while True:
            evo_choice = input(f"\nYour Eevee is at level {level}. Has it evolved? (yes/no): ").lower().strip()
            if evo_choice == 'no':
                current_stage = STARTERS["Eevee"][0]
                break
            elif evo_choice == 'yes':
                print("Which Eeveelution did you choose?")
                print("1. Vaporeon")
                print("2. Jolteon")
                print("3. Flareon")
                print("4. Espeon")
                print("5. Umbreon")
                print("6. Leafeon")
                print("7. Glaceon")
                print("8. Sylveon")
                
                evo_map = {
                    "1": "Vaporeon", "2": "Jolteon", "3": "Flareon", "4": "Espeon", 
                    "5": "Umbreon", "6": "Leafeon", "7": "Glaceon", "8": "Sylveon"
                }

                while True:
                    evo_number = input("Enter the number of the evolution: ")
                    chosen_evo_name = evo_map.get(evo_number)
                    if chosen_evo_name:
                        for evo_data in STARTERS["Eevee"]:
                            if evo_data["name"] == chosen_evo_name:
                                current_stage = evo_data
                                break
                        break
                    else:
                        print("Invalid number. Please enter a number from 1 to 8.")
                break
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")
    else:
        # Determine the current evolutionary stage based on level for non-Eevee Pokémon
        stages = STARTERS[starter]
        current_stage = stages[0]
        for stage in stages:
            if stage["evo_level"] is not None and level >= stage["evo_level"]:
                current_stage = stage


    print(f"\nAt level {level}, your {starter} is a {current_stage['name']}!")
    
    # Calculate and display final stats
    stats = get_stats(current_stage, level, ivs, evs, nature)
    print("\n--- Calculated Final Stats ---")
    print(f"Nature: {nature}")
    for stat, value in stats.items():
        print(f"  {stat}: {value}")

if __name__ == "__main__":
    main()