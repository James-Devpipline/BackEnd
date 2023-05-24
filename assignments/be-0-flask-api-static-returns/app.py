'''
Simple Flask API Static Returns
For this assignment, you will build a simple Flask API endpoint to return some static data.
[
		{
				"first_name":"John",
				"last_name":"Jonezz",
				"id":1,
				"city":"New York"
		},
		{
				"first_name":"Donna",
				"last_name":"Troy",
				"id":2,
				"city":"San Francisco"
		}
]
Create a list of dictionaries containing data for several users:
Create a simple flask application and make sure it runs without error (the terminal will inform of any errors)
Create an API endpoint /users/get that will return the list of users as a list of dictionaries.
Test the API endpoint using Postman. Verify that you receive the list of users as a JSON response
'''
from flask import Flask, jsonify

app = Flask(__name__)

data = [
	{
		"id": "1",
		"name": "Patrick Valenzuela",
		"phone": "(243) 907-6417",
		"email": "sed.sem.egestas@google.com"
	},
	{
		"id": "2",
		"name": "Macon Cardenas",
		"phone": "(552) 861-2003",
		"email": "molestie@yahoo.couk"
	},
	{
		"id": "3",
		"name": "Montana Wood",
		"phone": "1-823-224-2632",
		"email": "eu.metus@yahoo.ca"
	},
	{
		"id": "4",
		"name": "Tiger Fuentes",
		"phone": "(136) 748-7541",
		"email": "porttitor.tellus@icloud.ca"
	},
	{
		"id": "5",
		"name": "Laith Cline",
		"phone": "1-888-506-5464",
		"email": "porttitor.eros@aol.edu"
	},
	{
		"id": "6",
		"name": "Henry Sloan",
		"phone": "(644) 135-2895",
		"email": "velit.dui@protonmail.edu"
	},
	{
		"id": "7",
		"name": "Andrew Pearson",
		"phone": "(544) 767-1477",
		"email": "ut.pharetra@google.org"
	},
	{
		"id": "8",
		"name": "Samuel Meyer",
		"phone": "1-178-741-3362",
		"email": "duis.sit.amet@protonmail.edu"
	},
	{
		"id": "9",
		"name": "Brooke Fry",
		"phone": "1-858-213-9824",
		"email": "mauris@protonmail.com"
	},
	{
		"id": "10",
		"name": "Molly Haney",
		"phone": "1-337-285-0184",
		"email": "vestibulum.ut.eros@hotmail.couk"
	},
	{
		"id": "11",
		"name": "Amery Pruitt",
		"phone": "1-898-947-9291",
		"email": "vestibulum@outlook.com"
	},
	{
		"id": "12",
		"name": "Wesley Duffy",
		"phone": "(471) 351-3175",
		"email": "gravida@outlook.edu"
	},
	{
		"id": "13",
		"name": "Ali George",
		"phone": "1-221-881-4299",
		"email": "nunc.id@outlook.edu"
	},
	{
		"id": "14",
		"name": "Candice Torres",
		"phone": "1-363-244-1521",
		"email": "ipsum@icloud.com"
	},
	{
		"id": "15",
		"name": "Nomlanga Hatfield",
		"phone": "1-248-588-2272",
		"email": "erat@aol.com"
	},
	{
		"id": "16",
		"name": "Hiroko Williams",
		"phone": "(189) 525-3903",
		"email": "sit.amet@google.ca"
	},
	{
		"id": "17",
		"name": "Wyatt Robinson",
		"phone": "1-637-495-0347",
		"email": "vulputate.posuere@hotmail.net"
	},
	{
		"id": "18",
		"name": "Lucian Pope",
		"phone": "1-823-383-1937",
		"email": "adipiscing.enim@google.net"
	},
	{
		"id": "19",
		"name": "Cole Massey",
		"phone": "(811) 766-5487",
		"email": "lorem.ut@aol.couk"
	},
	{
		"id": "20",
		"name": "Thane Benjamin",
		"phone": "(616) 462-3287",
		"email": "dignissim.lacus.aliquam@hotmail.ca"
	},
	{
		"id": "21",
		"name": "Kylan Buckley",
		"phone": "1-846-813-4158",
		"email": "commodo.tincidunt@yahoo.ca"
	},
	{
		"id": "22",
		"name": "Louis Frost",
		"phone": "(620) 241-6470",
		"email": "hendrerit.neque.in@protonmail.com"
	},
	{
		"id": "23",
		"name": "Philip Stanley",
		"phone": "1-565-246-3549",
		"email": "justo.nec@aol.couk"
	},
	{
		"id": "24",
		"name": "Henry Guerra",
		"phone": "1-687-695-4517",
		"email": "aliquam.nisl@icloud.couk"
	},
	{
		"id": "25",
		"name": "Rahim Alston",
		"phone": "(644) 203-8816",
		"email": "cum@outlook.ca"
	},
	{
		"id": "26",
		"name": "Winifred Collier",
		"phone": "1-439-218-8602",
		"email": "pede.praesent@yahoo.org"
	},
	{
		"id": "27",
		"name": "Elizabeth Sharp",
		"phone": "(791) 681-6318",
		"email": "curabitur.egestas@icloud.couk"
	},
	{
		"id": "28",
		"name": "Drew Dorsey",
		"phone": "1-220-646-7724",
		"email": "justo.proin@icloud.edu"
	},
	{
		"id": "29",
		"name": "Dai Swanson",
		"phone": "(331) 281-1058",
		"email": "pellentesque.tellus@aol.com"
	},
	{
		"id": "30",
		"name": "Lewis Herring",
		"phone": "1-352-322-1533",
		"email": "elit.elit.fermentum@protonmail.net"
	},
	{
		"id": "31",
		"name": "Jerome Park",
		"phone": "(156) 374-8821",
		"email": "amet.risus.donec@yahoo.net"
	},
	{
		"id": "32",
		"name": "Barclay Marsh",
		"phone": "(859) 325-8561",
		"email": "dolor.fusce.mi@aol.edu"
	},
	{
		"id": "33",
		"name": "Melissa Larsen",
		"phone": "1-487-262-8751",
		"email": "vehicula@hotmail.com"
	},
	{
		"id": "34",
		"name": "Melvin Stephens",
		"phone": "(214) 567-2538",
		"email": "arcu@google.org"
	},
	{
		"id": "35",
		"name": "Darryl Myers",
		"phone": "1-474-643-5215",
		"email": "pretium.neque@outlook.edu"
	},
	{
		"id": "36",
		"name": "Jin Gibson",
		"phone": "1-212-471-4882",
		"email": "integer.urna@google.com"
	},
	{
		"id": "37",
		"name": "Myra Foreman",
		"phone": "(615) 477-6346",
		"email": "euismod.in@icloud.couk"
	},
	{
		"id": "38",
		"name": "Garth Valencia",
		"phone": "1-528-630-1567",
		"email": "cursus@google.ca"
	},
	{
		"id": "39",
		"name": "Sean Castaneda",
		"phone": "(323) 588-0088",
		"email": "vel@icloud.com"
	},
	{
		"id": "40",
		"name": "Beverly David",
		"phone": "1-416-834-8776",
		"email": "scelerisque.scelerisque@icloud.org"
	},
	{
		"id": "41",
		"name": "Amena Ingram",
		"phone": "(426) 619-2324",
		"email": "posuere@google.com"
	},
	{
		"id": "42",
		"name": "Kelly Mcbride",
		"phone": "(161) 642-8755",
		"email": "tortor.nibh@icloud.edu"
	},
	{
		"id": "43",
		"name": "Axel Sanders",
		"phone": "(984) 288-6615",
		"email": "dui.suspendisse.ac@yahoo.couk"
	},
	{
		"id": "44",
		"name": "Melvin Branch",
		"phone": "(660) 885-7142",
		"email": "molestie@protonmail.net"
	},
	{
		"id": "45",
		"name": "Samuel Gibbs",
		"phone": "1-488-964-8722",
		"email": "vulputate.eu.odio@hotmail.couk"
	},
	{
		"id": "46",
		"name": "Whilemina Arnold",
		"phone": "1-345-188-9391",
		"email": "non.massa.non@aol.couk"
	},
	{
		"id": "47",
		"name": "Drake Sweeney",
		"phone": "1-857-376-6675",
		"email": "ornare.fusce.mollis@aol.org"
	},
	{
		"id": "48",
		"name": "Merrill Houston",
		"phone": "(229) 746-1332",
		"email": "vivamus.nisi.mauris@yahoo.ca"
	},
	{
		"id": "49",
		"name": "Michael Santos",
		"phone": "1-544-627-7893",
		"email": "auctor.nunc@aol.edu"
	},
	{
		"id": "50",
		"name": "Daquan Nichols",
		"phone": "1-478-690-1505",
		"email": "sem.magna.nec@google.ca"
	},
	{
		"id": "51",
		"name": "Joelle Zimmerman",
		"phone": "(856) 988-0807",
		"email": "id.ante.nunc@hotmail.org"
	},
	{
		"id": "52",
		"name": "Jolie Howard",
		"phone": "1-474-445-1419",
		"email": "semper@outlook.edu"
	},
	{
		"id": "53",
		"name": "Darius Tran",
		"phone": "1-818-926-7705",
		"email": "tristique.neque@hotmail.couk"
	},
	{
		"id": "54",
		"name": "Craig Ferrell",
		"phone": "(321) 471-2043",
		"email": "ut.nulla@hotmail.com"
	},
	{
		"id": "55",
		"name": "Katell Sweet",
		"phone": "(423) 916-1533",
		"email": "donec.sollicitudin.adipiscing@google.net"
	},
	{
		"id": "56",
		"name": "Keegan Decker",
		"phone": "1-685-645-3620",
		"email": "tempor.lorem.eget@aol.couk"
	},
	{
		"id": "57",
		"name": "Nelle Gamble",
		"phone": "1-247-664-2298",
		"email": "luctus.lobortis@outlook.ca"
	},
	{
		"id": "58",
		"name": "Julie Heath",
		"phone": "1-643-628-5653",
		"email": "sem@hotmail.couk"
	},
	{
		"id": "59",
		"name": "Erich Lindsay",
		"phone": "(444) 411-8461",
		"email": "maecenas@icloud.ca"
	},
	{
		"id": "60",
		"name": "Zeph Ortiz",
		"phone": "1-848-566-4682",
		"email": "egestas.a@icloud.org"
	},
	{
		"id": "61",
		"name": "Hyatt Hughes",
		"phone": "(898) 849-9697",
		"email": "turpis.aliquam@google.net"
	},
	{
		"id": "62",
		"name": "Kasimir Wall",
		"phone": "(964) 803-4154",
		"email": "integer.sem.elit@hotmail.couk"
	},
	{
		"id": "63",
		"name": "Joel Gould",
		"phone": "(987) 478-1184",
		"email": "enim.nisl@google.org"
	},
	{
		"id": "64",
		"name": "Quentin Dixon",
		"phone": "(748) 880-5946",
		"email": "phasellus@hotmail.edu"
	},
	{
		"id": "65",
		"name": "Sandra Sykes",
		"phone": "(393) 825-8567",
		"email": "mollis.integer@protonmail.org"
	},
	{
		"id": "66",
		"name": "Tamekah Wilcox",
		"phone": "1-638-781-2296",
		"email": "risus.a@google.net"
	},
	{
		"id": "67",
		"name": "Micah Padilla",
		"phone": "1-436-961-6705",
		"email": "turpis.non.enim@outlook.net"
	},
	{
		"id": "68",
		"name": "Sydnee Weber",
		"phone": "1-234-747-1232",
		"email": "natoque.penatibus.et@yahoo.ca"
	},
	{
		"id": "69",
		"name": "Shaine Decker",
		"phone": "(665) 347-5114",
		"email": "sagittis.lobortis@google.com"
	},
	{
		"id": "70",
		"name": "Nevada Terry",
		"phone": "(782) 185-0266",
		"email": "sed@protonmail.couk"
	},
	{
		"id": "71",
		"name": "Plato Conway",
		"phone": "1-297-575-7518",
		"email": "in.consectetuer@outlook.edu"
	},
	{
		"id": "72",
		"name": "Charissa Figueroa",
		"phone": "1-543-618-7560",
		"email": "amet@hotmail.net"
	},
	{
		"id": "73",
		"name": "Orson Oneal",
		"phone": "(554) 557-0845",
		"email": "id.ante@yahoo.edu"
	},
	{
		"id": "74",
		"name": "Burton Pearson",
		"phone": "(927) 617-7180",
		"email": "non.enim@aol.net"
	},
	{
		"id": "75",
		"name": "Demetrius Mccarthy",
		"phone": "1-818-846-8907",
		"email": "fringilla@outlook.org"
	},
	{
		"id": "76",
		"name": "Mona Lloyd",
		"phone": "(311) 420-4563",
		"email": "a.malesuada@hotmail.couk"
	},
	{
		"id": "77",
		"name": "Bernard Townsend",
		"phone": "1-432-475-2424",
		"email": "dictum.phasellus@outlook.net"
	},
	{
		"id": "78",
		"name": "Kyla Hill",
		"phone": "1-813-768-3713",
		"email": "sed.est.nunc@hotmail.net"
	},
	{
		"id": "79",
		"name": "Rhoda Knapp",
		"phone": "(675) 240-9234",
		"email": "enim.suspendisse@outlook.couk"
	},
	{
		"id": "80",
		"name": "Cassady Gregory",
		"phone": "(218) 244-6265",
		"email": "lorem@google.ca"
	},
	{
		"id": "81",
		"name": "Maryam Browning",
		"phone": "(462) 241-7766",
		"email": "sit.amet@google.com"
	},
	{
		"id": "82",
		"name": "Ivy Blackburn",
		"phone": "(640) 413-6757",
		"email": "enim@yahoo.org"
	},
	{
		"id": "83",
		"name": "Emma Holt",
		"phone": "(964) 744-5317",
		"email": "mauris.eu.turpis@yahoo.net"
	},
	{
		"id": "84",
		"name": "Avram Lowe",
		"phone": "1-854-814-8803",
		"email": "risus.nulla@icloud.net"
	},
	{
		"id": "85",
		"name": "Ivory Levy",
		"phone": "1-756-687-8230",
		"email": "ultrices@hotmail.edu"
	},
	{
		"id": "86",
		"name": "Jacob Yang",
		"phone": "(174) 722-3755",
		"email": "vitae.purus@icloud.org"
	},
	{
		"id": "87",
		"name": "Amal Jimenez",
		"phone": "1-769-188-4599",
		"email": "pellentesque.sed.dictum@icloud.edu"
	},
	{
		"id": "88",
		"name": "Kuame Pollard",
		"phone": "1-235-884-8339",
		"email": "fusce.diam@icloud.net"
	},
	{
		"id": "89",
		"name": "Naomi Clark",
		"phone": "(857) 365-4267",
		"email": "egestas.blandit@yahoo.org"
	},
	{
		"id": "90",
		"name": "Rebecca Callahan",
		"phone": "1-276-826-9261",
		"email": "eros.turpis.non@protonmail.couk"
	},
	{
		"id": "91",
		"name": "Wilma Reeves",
		"phone": "(558) 284-7141",
		"email": "libero.proin@google.ca"
	},
	{
		"id": "92",
		"name": "Florence Harvey",
		"phone": "1-558-547-5458",
		"email": "lobortis.risus.in@google.com"
	},
	{
		"id": "93",
		"name": "Sybill Maldonado",
		"phone": "1-625-630-4324",
		"email": "lacus.pede@google.ca"
	},
	{
		"id": "94",
		"name": "Ryan Poole",
		"phone": "1-827-143-7026",
		"email": "dolor.sit@protonmail.edu"
	},
	{
		"id": "95",
		"name": "Julian Sexton",
		"phone": "(773) 473-5436",
		"email": "vehicula.risus.nulla@outlook.com"
	},
	{
		"id": "96",
		"name": "Christine Alvarez",
		"phone": "(883) 372-8126",
		"email": "metus.in@yahoo.com"
	},
	{
		"id": "97",
		"name": "Isaiah Fleming",
		"phone": "(597) 654-1463",
		"email": "malesuada.integer@hotmail.com"
	},
	{
		"id": "98",
		"name": "Raven Trujillo",
		"phone": "(112) 444-8999",
		"email": "lorem.auctor@google.couk"
	},
	{
		"id": "99",
		"name": "Karleigh Mccarty",
		"phone": "1-442-475-6513",
		"email": "tellus.lorem@google.edu"
	},
	{
		"id": "100",
		"name": "Tad Combs",
		"phone": "1-710-873-3848",
		"email": "aliquam.auctor.velit@icloud.couk"
	}
]

@app.route('/users')
def get_all_users():
    return jsonify(data), 200

@app.route("/users/<id>")
def get_user(id):
    for user in data:
        if user['id'] == id:
            return jsonify(user)
    return jsonify('User does not exist')

if __name__ == "__main__":
    app.run(port="8018", host="0.0.0.0")