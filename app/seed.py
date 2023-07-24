import random
from app import app, db, Hero, Power, HeroPower

def seed_powers():
    print("🦸‍♀️ Seeding powers...")
    powers_data = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
    ]

    for power_data in powers_data:
        power = Power(**power_data)
        db.session.add(power)

    db.session.commit()
    print("🦸‍♀️ Seeding powers completed.")

def seed_heroes():
    print("🦸‍♀️ Seeding heroes...")
    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Elektra Natchios", "super_name": "Elektra"}
    ]

    for hero_data in heroes_data:
        hero = Hero(**hero_data)
        db.session.add(hero)

    db.session.commit()
    print("🦸‍♀️ Seeding heroes completed.")

def seed_hero_powers():
    print("🦸‍♀️ Adding powers to heroes...")
    strengths = ["Strong", "Weak", "Average"]

    heroes = Hero.query.all()
    powers = Power.query.all()

    for hero in heroes:
        num_powers = random.randint(1, 3)
        random_powers = random.sample(powers, num_powers)

        for power in random_powers:
            strength = random.choice(strengths)
            hero_power = HeroPower(strength=strength, power=power, hero=hero)
            db.session.add(hero_power)

    db.session.commit()
    print("🦸‍♀️ Adding powers to heroes completed.")

def main():
    with app.app_context():
        db.create_all()
        seed_powers()
        seed_heroes()
        seed_hero_powers()

if __name__ == '__main__':
    main()
