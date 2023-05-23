import psycopg2
from flask import Flask, request, jsonify

conn = psycopg2.connect("dbname='sportsteams'")
cursor = conn.cursor()

def create_all():
    print("Creating Tables")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS NFLTeams (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL, 
    mascot VARCHAR NOT NULL, 
    city VARCHAR, 
    state VARCHAR, 
    championshipsWon SMALLINT DEFAULT 0
    );
    """)

    conn.commit()

create_all()

app = Flask(__name__)

@app.route('/whatsmyageagain', methods=["POST", "GET", "PUT", "DELETE"])
def request_with_method():
  if request.method == 'GET': 
    return jsonify("Whats my age again? (That was a GET)"), 200
  elif request.method == 'POST':
    return jsonify("You've got POST") , 200  
  elif request.method == 'PUT':
    return jsonify("Put it on which table?"), 200
  else:
    return jsonify("Use deactivate instead"), 405

@app.route('/team/add', methods=["POST"])
def user_add():
    data = request.form if request.form else request.json
    
    name = data.get('name')
    if not name:
        return jsonify("Name is required"),40
    
    mascot = data.get('mascot')
    if not mascot:
       return jsonify("Mascot is req"), 400
    
    city = data.get('city')
    state = data.get('state')

    championshipsWon = data.get('championshipsWons')
    if championshipsWon.isnumeric():
       if int(championshipsWon) > 1 or int(championshipsWon) < 0:
          return jsonify("championshipsWon must be a 1 or a 0"), 400
    else:
        return jsonify("championshipsWon must be a number"), 400

    cursor.execute("INSERT INTO NFLTeams (name, mascot, city, state, championshipsWon) VALUES (%s, %s, %s, %s, %s)", [name, mascot, city, state, championshipsWon])
    conn.commit()
    return jsonify(data), 200

@app.route('/team/get/<id>', methods={"GET"})
def get_team_by_id(id):
   cursor.execute("SELECT * FROM NFLTeams WHERE id = %s", [id])
   result = cursor.fetchone()
   if not result:
      return jsonify("Team is not in db"), 400
   
   result_dict = {
      'id': result(0),
      'name':result(1),
      'mascot': result(2),
      'city': result(3),
      'championshipsWon':result(4)
   }
   return jsonify(result_dict), 200

@app.route("/teams/get", methods=["GET"])
def get_all_teams():
   cursor.execute("SELECT id, name, mascot, city, state, championshipsWon FROM NFLTeams")
   results = cursor.fetchall()
   if not results:
      return jsonify("No teams in db"), 400
   
   end_result = []
   for result in results:
        result_dict = {
            'id': result(0),
            'name':result(1),
            'mascot': result(2),
            'city': result(3),
            'championshipsWon':result(4)
        }
        end_result.append(result_dict)

   return jsonify(end_result), 200

if __name__ == "__main__":
    app.run(port="8086", host="0.0.0.0")
    # host="0.0.0.0" will create a network accessable address, so you can test things from another device