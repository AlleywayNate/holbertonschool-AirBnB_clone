# Airbnb Clone

---
## Description

Project attempts to clone the the AirBnB application and website, starting with the console.

---

### Interactive CLI

* This project uses python library, `cmd` to run tests in an interactive command
  line interface. To begin tests with the CLI, run this script:

```
$ ./console.py
```

#### For a detailed description of all tests, run these commands in the CLI:

```
(hbnb) help help
List available commands with "help" or detailed help with "help cmd".
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help create

        Creates a new instance of a specified class and prints
        instance's unique id

```

* Tests in the CLI may also be executed with this syntax:

  * **destroy:** `<class name>.destroy(<id>)`

  * **update:** `<class name>.update(<id>, <attribute name>, <attribute value>)`

---

## Testing

This project uses python library, `unittest` to run tests on all python files.
All unittests are in the `./tests` directory with the command:

  * `$ python3 -m unittest discover -v ./tests/`



## Authors

* Nathen Williams - https://github.com/AlleywayNate
* Paul Stewart - https://github.com/PStewart1