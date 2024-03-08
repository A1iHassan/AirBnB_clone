# 0x00. AirBnB clone - The console
![AirBnB logo pic](hbnb.png)

## Welcome to the AirBnB clone project!

# DESCRIPTON
This project

# DESCRIPTION OF THE COMMAND INTERPRETER
The command interpreter is the part of the project that allows you to interact with the storage entity directly, givving you access to the data stored in the data base with the ability to alter it freely.

## HOW TO START THE CONSOLE
To start the console, run the command ```./console``` in your current working directory, where you originally cloned the repo.
After that, you will see a prompt displayed on the left side of the screen ```(hbnb) ```, where then you can start using the console.

## HOW TO USE THE CONSOLE
There are plenty of commands that you can run through the console that can serve you with lots of functionalities and processes.
The below table shows the available commands to be used:
| **COMMAND** | **FUNCTIONALITY** |
|-------------|-------------------|
| ```create <class_name>``` | creates a new instance of the given class name, saves it to the JSON file, and prints out its id |
| ```all``` | prints out a list of all saved instances of all available class names |
| ```all <class_name>``` | prints out a list of all saved instances of the given class name |
| ```show <class_name> <instance_id>``` | prints out the specific class instance that matches the class name and instance id given |
| ```destroy <class_name> <instance_id>``` | deletes the specific instance that matches the class name and instance id given, from the data base |
| ```update <class_name> <instance_id> <attr_name> <attr_value>``` | updates the specific attribute that matches all given information with its corresponding new value. If the attribute doesn't exist, it will be created |
| ```<class_name>.all()``` | same behavior as ```all <class_name>``` |
| ```<class_name>.show(<instance_id>)``` | same behavior of ```show <class_name> <instance_id>``` |
| ```<class_name>.destroy(<instance_id>)``` | same behavior as ```destroy <class_name> <instance_id>``` |
| ```<class_name>.update(<instance_id> <attr_name> <attr_value>)``` | same behavior as ```update <class_name> <instance_id> <attr_name> <attr_value>``` |
| ```<class_name>.update(<instance_id> <dictionary representation>)``` | performs a ```.update()``` process on each key\value pair in the given dictionary |

## EXAMPLES
Below are some usage cases and examples that will cover any edge cases while using the above commands with or without the correct format and syntax

#### all

##### ```all```, ```all <class_name>```, and ```<class_name>.all()```

```
(hbnb) all MyModel
** class doesn't exist **
```
