AirBnB clone - The console

AirBnB is a complete web application, integrating database storage, a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

THE CONSOLE

It is used to manage the storage of class instances (file.json).

It can be used and executed in interactive and non-interactive mode.

Interactive mode

$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
(hbnb)
(hbnb) quit
$

Non-Interactive Mode

$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$

The following commands are used for storage management and how to use them.
1. help - Shows all allowed commands or gives information about a specific command.

2. quit or EOF - Exits the program

3. create - Creates a new instance.

4. show - Shows a specific instance by its classname and its id.

5. all - Displays all stored instances or all stored instances of a specific class by its classname.

6. update - Updates an instance (adds or modifies attributes) by its classname, id, attribute and its value to add/modify.

7. destroy - Deletes an instance by its classname and its id
