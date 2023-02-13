AirBnB clone - The console
The console is the first part of the AirBnB clone project which aims to deploy a simple copy of the AirBnB website to cover all fundamental concepts of the ALX School higher level programming track.

Overview
This first part of the project focuses on creating a command interpreter that allows to:

create the data model.
manage (create, update and destroy) objects via a console.
store and persist objects to a file (JSON file).
Files and Directories
/models directory constains all classes used for the project.
basemodel.py file contains the base class (BaseModel) of all models in the project:

user.py - file contains the User class.
state.py - file contains the State class.
city.py - file contains the Cityclass.
amenity.py - file contains the Amenity class.
place.py - file contains the Place class.
review.py - file contains the Review class.
/models/engine directory contains the class that handles JSON serialization and deserialization.
file_storage.py - file contains FileStorage class.

/tests directory contains all unit test cases for this project.

console.py the console contains the entry point of the command interpreter.


|── console.py
├── models/
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   |── user.py
│   └── engine/
│       └── file_storage.py
└── tests/
    |── test_console.py
    └── test_models/
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        |── test_user.py
        └── test_engine/
            └── test_file_storage.py
Environment and Execution
This project was interpreted/compiled and tested on Ubuntu 20.04 LTS using python3 (version 3.8.5).

To use the console you must have python3 installed and the repository cloned
(https://github.com/jo-esign/AirBnB_clone.git)

To start the console you only need to run ./console in the root of the repository.

The console works like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

AUTHORS
=======
Joy Matthew | Github: jo-esign


