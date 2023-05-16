from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {
        "id": "1",
        "name": "Jar Jar",
        "planet": "Naboo",
        "affiliation": "Sith"
    },
    {
        "id": "2",
        "name": "Obi Wan",
        "planet": "Stewjon",
        "affiliation": "Jedi"
    },
    {
        "id": "3",
        "name": "Anakin Skywalker",
        "planet": "Tatooine",
        "affiliation": "Jedi"
    }
]	

@app.route('/hello')
def say_hello():
    return jsonify("Hello World!")

@app.route('/all_sw')
def get_all_users():
    return jsonify(data), 200

@app.route("/starwars/<id>") ## the <id> is a slug made variable named id
def get_user_by_id(id):
    for user in data:
        if user['id'] == id:
            return jsonify(user)
    return jsonify('User does not exist')


if __name__ == "__main__":
    app.run(port="8018", host="0.0.0.0")

