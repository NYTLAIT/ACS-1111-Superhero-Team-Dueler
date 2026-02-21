# AI A BIT OF THIS

import random
from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team
from arena import Arena


def orig_test_arena():
    arena = Arena()

    # ======================
    # TEAM ONE: Draft
    # ======================
    team_one = Team("Draft")

    himmel = Hero("Himmel", 300)
    himmel.add_weapon(Weapon("Axe", 300))
    himmel.add_armor(Armor("Dwarf Armor", 500))
    team_one.add_hero(himmel)

    groo = Hero("Groo", 120)
    groo.add_ability(Ability("Heal", 1600))
    groo.add_ability(Ability("Basic Fireball", 50))
    team_one.add_hero(groo)

    dread = Hero("Dread", 200)
    dread.add_ability(Ability("Smite", 200))
    dread.add_weapon(Weapon("Long Sword", 200))
    dread.add_armor(Armor("Knight Armor", 250))
    team_one.add_hero(dread)

    # ======================
    # TEAM TWO: Pearl
    # ======================
    team_two = Team("Pearl")

    aesadang = Hero("Aesadang", 120)
    aesadang.add_ability(Ability("Void", 300))
    aesadang.add_ability(Ability("Vanish", 0))
    team_two.add_hero(aesadang)

    char = Hero("Char", 80)
    char.add_ability(Ability("Roots", 100))
    char.add_ability(Ability("Vanish", 600))
    team_two.add_hero(char)

    godam = Hero("Godam", 140)
    godam.add_ability(Ability("Radial", 600))
    godam.add_ability(Ability("Lesser Vanish", 200))
    team_two.add_hero(godam)

    seju = Hero("Seju", 100)
    seju.add_ability(Ability("Money", 800))
    seju.add_ability(Ability("Car", 50))
    seju.add_ability(Ability("Plane", 400))
    seju.add_ability(Ability("Plot", 600))
    team_two.add_hero(seju)

    arena.team_one = team_one
    arena.team_two = team_two

    return arena


def better_test_arena():
    arena = Arena()

    # ======================
    # TEAM ONE: Draft
    # ======================
    team_one = Team("Draft")

    himmel = Hero("Himmel", 400)
    himmel.add_weapon(Weapon("Axe", 120))
    himmel.add_armor(Armor("Dwarf Armor", 80))
    team_one.add_hero(himmel)

    groo = Hero("Groo", 350)
    groo.add_ability(Ability("Heal Burst", 100))
    groo.add_ability(Ability("Fireball", 90))
    groo.add_armor(Armor("Cloth Guard", 60))
    team_one.add_hero(groo)

    dread = Hero("Dread", 450)
    dread.add_ability(Ability("Smite", 110))
    dread.add_weapon(Weapon("Long Sword", 100))
    dread.add_armor(Armor("Knight Armor", 100))
    team_one.add_hero(dread)

    # ======================
    # TEAM TWO: Pearl
    # ======================
    team_two = Team("Pearl")

    aesadang = Hero("Aesadang", 320)
    aesadang.add_ability(Ability("Void Pulse", 100))
    aesadang.add_armor(Armor("Shadow Veil", 70))
    team_two.add_hero(aesadang)

    char = Hero("Char", 300)
    char.add_ability(Ability("Roots", 80))
    char.add_ability(Ability("Ember Strike", 95))
    char.add_armor(Armor("Bark Skin", 60))
    team_two.add_hero(char)

    godam = Hero("Godam", 360)
    godam.add_ability(Ability("Radial Blast", 105))
    godam.add_armor(Armor("Energy Field", 75))
    team_two.add_hero(godam)

    seju = Hero("Seju", 380)
    seju.add_ability(Ability("Money Shot", 110))
    seju.add_ability(Ability("Jet Charge", 90))
    seju.add_armor(Armor("Golden Shield", 85))
    team_two.add_hero(seju)

    arena.team_one = team_one
    arena.team_two = team_two

    return arena


# ==========================
# PYTEST TESTS
# ==========================

def test_arena_battle_integrity():
    random.seed(1)  # makes results repeatable

    arena = build_test_arena()
    arena.team_battle()

    # 1 There must be a winner
    assert arena.current_winner["team"] in (
        arena.team_one.name,
        arena.team_two.name
    )

    # 2 All champions must be alive
    for hero in arena.current_winner["champions"]:
        assert hero.is_alive()

    # 3 Only one team can have living members
    team_one_alive = any(hero.is_alive() for hero in arena.team_one.heroes)
    team_two_alive = any(hero.is_alive() for hero in arena.team_two.heroes)

    assert not (team_one_alive and team_two_alive)


# ==========================
# MANUAL RUN OPTION
# ==========================

if __name__ == "__main__":
    arena = orig_test_arena()
    arena.team_battle()
    arena.show_stats()

    # arena = better_test_arena()
    # arena.team_battle()
    # arena.show_stats()
