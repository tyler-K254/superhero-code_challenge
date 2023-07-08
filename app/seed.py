from models import db, Power, Hero, HeroPower

# Create powers
powers = [
    {'name': 'super strength', 'description': 'gives the wielder super-human strengths'},
    {'name': 'flight', 'description': 'gives the wielder the ability to fly through the skies at supersonic speed'},
    {'name': 'super human senses', 'description': 'allows the wielder to use her senses at a super-human level'},
    {'name': 'elasticity', 'description': 'can stretch the human body to extreme lengths'}
]

for power_data in powers:
    power = Power(**power_data)
    db.session.add(power)

# Create heroes
heroes = [
    {'name': 'Kamala Khan', 'super_name': 'Ms. Marvel'},
    {'name': 'Doreen Green', 'super_name': 'Squirrel Girl'},
    {'name': 'Gwen Stacy', 'super_name': 'Spider-Gwen'},
    {'name': 'Janet Van Dyne', 'super_name': 'The Wasp'},
    {'name': 'Wanda Maximoff', 'super_name': 'Scarlet Witch'},
    {'name': 'Carol Danvers', 'super_name': 'Captain Marvel'},
    {'name': 'Jean Grey', 'super_name': 'Dark Phoenix'},
    {'name': 'Ororo Munroe', 'super_name': 'Storm'},
    {'name': 'Kitty Pryde', 'super_name': 'Shadowcat'},
    {'name': 'Elektra Natchios', 'super_name': 'Elektra'}
]

for hero_data in heroes:
    hero = Hero(**hero_data)
    db.session.add(hero)

# Assign powers to heroes
import random

strengths = ["Strong", "Weak", "Average"]

all_powers = Power.query.all()

for hero in Hero.query.all():
    num_powers = random.randint(1, 3)
    selected_powers = random.sample(all_powers, num_powers)

    for power in selected_powers:
        hero_power = HeroPower(hero=hero, power=power, strength=random.choice(strengths))
        db.session.add(hero_power)

# Commit the changes to the database
db.session.commit()

print("🦸‍♀️ Done seeding!")
