class CharactersByHouseResponseMock:
    @staticmethod
    def get(houses_name):
        if houses_name == 'Gryffindor':
            return [
                {
                    "name": "Harry Potter",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "31-07-1980",
                    "yearOfBirth": 1980,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "green",
                    "hairColour": "black",
                    "wand": {
                        "wood": "holly",
                        "core": "phoenix feather",
                        "length": 11
                    },
                    "patronus": "stag",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Daniel Radcliffe",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/harry.jpg"
                },
                {
                    "name": "Hermione Granger",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "19-09-1979",
                    "yearOfBirth": 1979,
                    "wizard": True,
                    "ancestry": "muggleborn",
                    "eyeColour": "brown",
                    "hairColour": "brown",
                    "wand": {
                        "wood": "vine",
                        "core": "dragon heartstring",
                        "length": None
                    },
                    "patronus": "otter",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Emma Watson",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/hermione.jpeg"
                },
                {
                    "name": "Ron Weasley",
                    "alternate_names": [
                        "Dragomir Despard"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "01-03-1980",
                    "yearOfBirth": 1980,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "blue",
                    "hairColour": "red",
                    "wand": {
                        "wood": "willow",
                        "core": "unicorn tail-hair",
                        "length": 14
                    },
                    "patronus": "Jack Russell terrier",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Rupert Grint",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/ron.jpg"
                },
                {
                    "name": "Minerva McGonagall",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "04-10-1925",
                    "yearOfBirth": 1925,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "black",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "tabby cat",
                    "hogwartsStudent": False,
                    "hogwartsStaff": True,
                    "actor": "Dame Maggie Smith",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/mcgonagall.jpg"
                },
                {
                    "name": "Rubeus Hagrid",
                    "alternate_names": [

                    ],
                    "species": "half-giant",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "06-12-1928",
                    "yearOfBirth": 1928,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "black",
                    "hairColour": "black",
                    "wand": {
                        "wood": "oak",
                        "core": "",
                        "length": 16
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": True,
                    "actor": "Robbie Coltrane",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/hagrid.png"
                },
                {
                    "name": "Neville Longbottom",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "30-07-1980",
                    "yearOfBirth": 1980,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "blonde",
                    "wand": {
                        "wood": "cherry",
                        "core": "unicorn tail-hair",
                        "length": 13
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Matthew Lewis",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/neville.jpg"
                },
                {
                    "name": "Ginny Weasley",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "11-08-1981",
                    "yearOfBirth": 1981,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "brown",
                    "hairColour": "red",
                    "wand": {
                        "wood": "yew",
                        "core": "",
                        "length": None
                    },
                    "patronus": "horse",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Bonnie Wright",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/ginny.jpg"
                },
                {
                    "name": "Sirius Black",
                    "alternate_names": [
                        "Padfoot",
                        "Snuffles"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "03-11-1959",
                    "yearOfBirth": 1959,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "grey",
                    "hairColour": "black",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "hare",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Gary Oldman",
                    "alternate_actors": [
                        "James Walters",
                        "Rohan Gotobed"
                    ],
                    "alive": False,
                    "image": "https://hp-api.herokuapp.com/images/sirius.JPG"
                },
                {
                    "name": "Remus Lupin",
                    "alternate_names": [
                        "Professor Lupin",
                        "Moony",
                        "Remus John Lupin"
                    ],
                    "species": "werewolf",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "10-03-1960",
                    "yearOfBirth": 1960,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "green",
                    "hairColour": "brown",
                    "wand": {
                        "wood": "cypress",
                        "core": "unicorn tail-hair",
                        "length": 10.25
                    },
                    "patronus": "wolf",
                    "hogwartsStudent": False,
                    "hogwartsStaff": True,
                    "actor": "David Thewlis",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": "https://hp-api.herokuapp.com/images/lupin.jpg"
                },
                {
                    "name": "Arthur Weasley",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "06-02-1950",
                    "yearOfBirth": 1950,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "blue",
                    "hairColour": "red",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "weasel",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Mark Williams",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/arthur.jpg"
                },
                {
                    "name": "Lily Potter",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "muggleborn",
                    "eyeColour": "green",
                    "hairColour": "",
                    "wand": {
                        "wood": "willow",
                        "core": "",
                        "length": 10.25
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Geraldine Somerville",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "James Potter",
                    "alternate_names": [
                        "Prongs"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "black",
                    "wand": {
                        "wood": "mahogany",
                        "core": "",
                        "length": 11
                    },
                    "patronus": "stag",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Adrian Rawlins",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Albus Dumbledore",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": 0,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "blue",
                    "hairColour": "silver",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": True,
                    "actor": "Richard Harris",
                    "alternate_actors": [
                        "Michael Gambon"
                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Molly Weasley",
                    "alternate_names": [
                        "Molly Prewett",
                        "Mollywabbles"
                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "red",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Julie Walters",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Percy Weasley",
                    "alternate_names": [
                        "Perce",
                        "Percy Ignatius Weasley",
                        "Weatherby"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "red",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Chris Rankin",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Fred Weasley",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "red",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "James Phelps",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "George Weasley",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "red",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Oliver Phelps",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Lee Jordan",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Luke Youngblood",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Bill Weasley",
                    "alternate_names": [
                        "William Arthur Weasley"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "red",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Richard Fish",
                    "alternate_actors": [
                        "Domhnall Gleeson"
                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Charlie Weasley",
                    "alternate_names": [
                        "Charles Weasley"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "red",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Alex Crockford",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Lavender Brown",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Kathleen Cauley",
                    "alternate_actors": [
                        "Jennifer Smith",
                        "Jessie Cave"
                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Seamus Finnegan",
                    "alternate_names": [
                        "O'Flaherty"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "",
                    "hairColour": "sandy",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Devon Murray",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Parvati Patil",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Sitara Shah",
                    "alternate_actors": [
                        "Shefali Chowdhury"
                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Nearly Headless Nick",
                    "alternate_names": [
                        "Sir Nicholas de Mimsy-Porpington",
                        "Sir Nicholas",
                        "Nick"
                    ],
                    "species": "ghost",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "John Cleese",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Angelina Johnson",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Danielle Tabor",
                    "alternate_actors": [
                        "Tiana Benjamin"
                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Alicia Spinet",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Leilah Sutherland",
                    "alternate_actors": [
                        "Rochelle Douglas"
                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Katie Bell",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Emily Dale",
                    "alternate_actors": [
                        "Georgina Leonidas"
                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Celestina Warbeck",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "larch",
                        "core": "phoenix feather",
                        "length": 10.5
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Colin Creevey",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "muggleborn",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Hugh Mitchell",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Peter Pettigrew",
                    "alternate_names": [
                        "Wormtail",
                        "Scabbers",
                        "Wormy"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "chestnut",
                        "core": "dragon heartstring",
                        "length": 9.25
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Timothy Spall",
                    "alternate_actors": [
                        "Charles Hughes"
                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Natalie McDonald",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Eloise Midgen",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Samantha Clinch",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Aberforth Dumbledore",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "blue",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "goat",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Jim McManus",
                    "alternate_actors": [
                        "Ciarán Hinds"
                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Euan Abercrombie",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Kenneth Towler",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Vicky Frobisher",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Geoffrey Hooper",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Andrew Kirke",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Jack Sloper",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Romilda Vane",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "dark",
                    "hairColour": "black",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Anna Shaffer",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Cormac McLaggen",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Freddie Stroma",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Demelza Robins",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Katy Huxley-Golden",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Jimmy Peakes",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Ritchie Coote",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Ashley Virgil",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Lily Potter",
                    "alternate_names": [
                        "Lily Luna Potter"
                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "",
                    "hairColour": "red",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Daphne de Beistegui",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "James Potter",
                    "alternate_names": [
                        "James Sirius Potter"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Will Dunn",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Rose Weasley",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Gryffindor",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "",
                    "hairColour": "red",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Helena Barlow",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                }
            ]
        elif houses_name == 'Ravenclaw':
            return [
                {
                    "name": "Cho Chang",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "brown",
                    "hairColour": "black",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "swan",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Katie Leung",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/cho.jpg"
                },
                {
                    "name": "Luna Lovegood",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Ravenclaw",
                    "dateOfBirth": "13-02-1981",
                    "yearOfBirth": 1981,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "grey",
                    "hairColour": "blonde",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "hare",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Evanna Lynch",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/luna.jpg"
                },
                {
                    "name": "Terry Boot",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Kevin Lee Yi",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Mandy Brocklehurst",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Christina Petrou",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Padma Patil",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Sharon Sandhu",
                    "alternate_actors": [
                        "Afshan Azad"
                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Lisa Turpin",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Filius Flitwick",
                    "alternate_names": [
                        "Professor Flitwick"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": True,
                    "actor": "Warwick Davis",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Moaning Myrtle",
                    "alternate_names": [
                        "Myrtle Elizabeth Warren"
                    ],
                    "species": "ghost",
                    "gender": "female",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "muggleborn",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Shirley Henderson",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Penelope Clearwater",
                    "alternate_names": [
                        "Penny"
                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Gemma Padley",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Stewart Ackerley",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Orla Quirke",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Fawcett",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Alex Argenti",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Stebbins",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Anthony Goldstein",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Michael Corner",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Ryan Nelson",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Zacharias Smith",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "blond",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Nick Shirm",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Marietta Edgecombe",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "blonde",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Bradley",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Roger Davies",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Henry Lloyd-Hughes",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Eddie Carmichael",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Marcus Belby",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Robert Knox",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Xenophilius Lovegood",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Ravenclaw",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "white",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Rhys Ifans",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                }
            ]
        elif houses_name == 'Slytherin':
            return [
                {
                    "name": "Draco Malfoy",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "05-06-1980",
                    "yearOfBirth": 1980,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "grey",
                    "hairColour": "blonde",
                    "wand": {
                        "wood": "hawthorn",
                        "core": "unicorn tail-hair",
                        "length": 10
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Tom Felton",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/draco.jpg"
                },
                {
                    "name": "Severus Snape",
                    "alternate_names": [
                        "Half-Blood Prince"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "09-01-1960",
                    "yearOfBirth": 1960,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "black",
                    "hairColour": "black",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "doe",
                    "hogwartsStudent": False,
                    "hogwartsStaff": True,
                    "actor": "Alan Rickman",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": "https://hp-api.herokuapp.com/images/snape.jpg"
                },
                {
                    "name": "Bellatrix Lestrange",
                    "alternate_names": [
                        "Bella"
                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": 1951,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "brown",
                    "hairColour": "black",
                    "wand": {
                        "wood": "walnut",
                        "core": "dragon heartstring",
                        "length": 12.75
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Helena Bonham Carter",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": "https://hp-api.herokuapp.com/images/bellatrix.jpg"
                },
                {
                    "name": "Lord Voldemort",
                    "alternate_names": [
                        "Tom Marvolo Riddle"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "31-12-1926",
                    "yearOfBirth": 1926,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "red",
                    "hairColour": "bald",
                    "wand": {
                        "wood": "yew",
                        "core": "phoenix feather",
                        "length": 13.5
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Ralph Fiennes",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": "https://hp-api.herokuapp.com/images/voldemort.jpg"
                },
                {
                    "name": "Horace Slughorn",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "green",
                    "hairColour": "blonde",
                    "wand": {
                        "wood": "cedar",
                        "core": "dragon heartstring",
                        "length": 10.25
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": True,
                    "actor": "Jim Broadbent",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/slughorn.JPG"
                },
                {
                    "name": "Dolores Umbridge",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "brown",
                    "hairColour": "grey",
                    "wand": {
                        "wood": "birch",
                        "core": "dragon heartstring",
                        "length": 8
                    },
                    "patronus": "persian cat",
                    "hogwartsStudent": False,
                    "hogwartsStaff": True,
                    "actor": "Imelda Staunton",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/umbridge.jpg"
                },
                {
                    "name": "Lucius Malfoy",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": 1954,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "grey",
                    "hairColour": "blonde",
                    "wand": {
                        "wood": "elm",
                        "core": "dragon heartstring",
                        "length": 18
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Jason Isaacs",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/lucius.jpg"
                },
                {
                    "name": "Vincent Crabbe",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "black",
                    "hairColour": "black",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Jamie Waylett",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": "https://hp-api.herokuapp.com/images/crabbe.jpg"
                },
                {
                    "name": "Gregory Goyle",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "brown",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Josh Herdman",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": "https://hp-api.herokuapp.com/images/goyle.jpg"
                },
                {
                    "name": "Millicent Bulstrode",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Helen Stuart",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Theodore Nott",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Pansy Parkinson",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Genevieve Gaunt",
                    "alternate_actors": [
                        "Lauren Shotton",
                        "Scarlett Byrne"
                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Blaise Zabini",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Louis Cordice",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Bloody Baron",
                    "alternate_names": [

                    ],
                    "species": "ghost",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Terence Bayler",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Marcus Flint",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Jamie Yeates",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Adrian Pucey",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Scot Fearn",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Miles Bletchley",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "David Churchyard",
                    "alternate_actors": [
                        "Amy Puglia"
                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Terrence Higgs",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Will Theakston",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Milicent Bullstroude",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "black",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Helen Stuart",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Cassius Warrington",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Ashley Hull",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Graham Montague",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Peregrine Derrick",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Lucian Bole",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Walden Macnair",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "black",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Peter Best",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Malcolm Baddock",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Graham Pritchard",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Evan Rosier",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Wilkes",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Avery",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Richard Rosson",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Mulciber",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Alphard Black",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Regulus Black",
                    "alternate_names": [
                        "Regulus Arcturus Black"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "black",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Tom Moorcroft",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Phineas Nigelus Black",
                    "alternate_names": [
                        "Professor Phineas Nigellus Black"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "John Atterbury",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Araminta Meliflua Black",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Andromeda Tonks",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "brown",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Rodolphus Lestrange",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Rabastan Lestrange",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Daphne Greengrass",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Vaisey",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "dark",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Harper",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Urquhart",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Amycus Carrow",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Ralph Ineson",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Alecto Carrow",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Suzie Toase",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Scabior",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Nick Moran",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Albus Severus Potter",
                    "alternate_names": [
                        "Al"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "green",
                    "hairColour": "black",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Arthur Bowen",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Scorpius Malfoy",
                    "alternate_names": [
                        "Scorpius Hyperion Malfoy"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Slytherin",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "pure-blood",
                    "eyeColour": "grey",
                    "hairColour": "blond",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Bertie Gilbert",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                }
            ]
        else:
            return [
                {
                    "name": "Cedric Diggory",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": 1977,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "grey",
                    "hairColour": "brown",
                    "wand": {
                        "wood": "ash",
                        "core": "unicorn hair",
                        "length": 12.25
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Robert Pattinson",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": "https://hp-api.herokuapp.com/images/cedric.png"
                },
                {
                    "name": "Fat Friar",
                    "alternate_names": [

                    ],
                    "species": "ghost",
                    "gender": "male",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Simon Fisher-Becker",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Hannah Abbott",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "",
                    "hairColour": "blonde",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Charlotte Skeoch",
                    "alternate_actors": [
                        "Louisa Warren"
                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Susan Bones",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Eleanor Columbus",
                    "alternate_actors": [
                        "Emma Jayne-Corboz"
                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Justin Finch-Fletchley",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "muggleborn",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Edward Randell",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Pomona Sprout",
                    "alternate_names": [
                        "Professor Sprout"
                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": True,
                    "actor": "Miriam Margolyes",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Ernie Macmillan",
                    "alternate_names": [
                        "Ernest Macmillan"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "blond",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "boar",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Louis Doyle",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Eleanor Branstone",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Owen Cauldwell",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Laura Madley",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Kevin Whitby",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Summers",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Nymphadora Tonks",
                    "alternate_names": [
                        "Dora",
                        "Nymphadora Lupin"
                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "brown",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Natalia Tena",
                    "alternate_actors": [

                    ],
                    "alive": False,
                    "image": ""
                },
                {
                    "name": "Rose Zeller",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Summerby",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Leanne",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "female",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "Isabella Laughland",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Cadwallader",
                    "alternate_names": [

                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": True,
                    "hogwartsStaff": False,
                    "actor": "",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                },
                {
                    "name": "Ted Lupin",
                    "alternate_names": [
                        "Edward Remus Teddy Lupin"
                    ],
                    "species": "human",
                    "gender": "male",
                    "house": "Hufflepuff",
                    "dateOfBirth": "",
                    "yearOfBirth": None,
                    "wizard": True,
                    "ancestry": "half-blood",
                    "eyeColour": "",
                    "hairColour": "",
                    "wand": {
                        "wood": "",
                        "core": "",
                        "length": None
                    },
                    "patronus": "",
                    "hogwartsStudent": False,
                    "hogwartsStaff": False,
                    "actor": "Luke Newberry",
                    "alternate_actors": [

                    ],
                    "alive": True,
                    "image": ""
                }
            ]
