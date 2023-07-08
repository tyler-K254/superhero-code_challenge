#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''


@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_data = [{'id': hero.id, 'name': hero.name, 'super_name': hero.super_name} for hero in heroes]
    return jsonify(heroes_data)

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        hero_data = hero.to_dict(include_powers=True)
        return jsonify(hero_data)
    else:
        return jsonify({'error': 'Hero not found'}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_data = [{'id': power.id, 'name': power.name, 'description': power.description} for power in powers]
    return jsonify(powers_data)

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        power_data = {'id': power.id, 'name': power.name, 'description': power.description}
        return jsonify(power_data)
    else:
        return jsonify({'error': 'Power not found'}), 404

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if power:
        data = request.get_json()
        description = data.get('description')
        if description:
            power.description = description
            db.session.commit()
            return jsonify(power.to_dict())
        else:
            return jsonify({'error': 'Invalid request'}), 400
    else:
        return jsonify({'error': 'Power not found'}), 404

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    strength = data.get('strength')
    power_id = data.get('power_id')
    hero_id = data.get('hero_id')

    if strength and power_id and hero_id:
        power = Power.query.get(power_id)
        hero = Hero.query.get(hero_id)

        if power and hero:
            hero_power = HeroPower(strength=strength, power=power, hero=hero)
            db.session.add(hero_power)
            db.session.commit()
            hero_data = hero.to_dict(include_powers=True)
            return jsonify(hero_data), 201
        else:
            return jsonify({'error': 'Invalid power or hero'}), 400
    else:
        return jsonify({'error': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(port=5555)