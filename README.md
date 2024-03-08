# 0x00. AirBnB clone - The console
![AirBnB logo pic](hbnb.png)

## Welcome to the AirBnB clone project!

# DESCRIPTON
This project is going to be the first out of three stages of us creating the full AirBnB clone, where we foucus in this project on the storage part where we can recieve data and store it properly in order for us to be able to access it whenever we want.

# DESCRIPTION OF THE COMMAND INTERPRETER
The command interpreter is the part of the project that allows you to interact with the storage entity directly, givving you access to the data stored in the data base with the ability to alter it freely. This project mainly and only uses Python an ddeals with JSON data.

## HOW TO START THE CONSOLE
To start the console, run the command ```./console``` in your current working directory, where you originally cloned the repo.
After that, you will see a prompt displayed on the left side of the screen ```(hbnb) ```, where then you can start using the console.

> Note that this console was made assuming that all data will be enterd following some set rules:
> 1. You can assume arguments are always in the right order
> 2. all arguments are separated by a space
> 3. A string argument with a space must be between double quote
> 4. The error management starts from the first argument to the last one

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
Below are some usage cases and examples that will cover any edge cases while using the above commands with or without the correct format and syntax.

#### create
##### (```create <class_name>```)
```
(hbnb) create
** class name missing **
(hbnb) create MyClass
** class doesn't exist **
(hbnb) create BaseModel
2ec04bb6-96e1-4529-8be1-f7d8be8f7714
(hbnb)
```

#### all:
##### (```all```, ```all <class_name>```, and ```<class_name>.all()```)
```
(hbnb) all MyModel
** class doesn't exist **
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': 
'49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) all
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': 
'49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}", "[User] 
(38f22813-2753-4d42-b37c-57a17f1e4f88) {'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'created_at': datetime.datetime(2017, 9, 28, 
21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'email': 'airbnb@mail.com', 'first_name': 
'Betty', 'last_name': 'Bar', 'password': 'root'}"]
(hbnb) User.all()
["[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'created_at': datetime.datetime(2017, 
9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'email': 'airbnb@mail.com', 
'first_name': 'Betty', 'last_name': 'Bar', 'password': 'root'}"]
```

#### show:
##### (```show <class_name> <instance_id>``` and ```<class_name>.show(<instance_id>)```)
```
(hbnb) show
** class name missing **
(hbnb) show MyClass
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel 1234567890-abcd
** no instance found **
(hbnb) show BaseModel 2858b4ca-9085-4b02-a48c-b326bdb5c192
[BaseModel] (2858b4ca-9085-4b02-a48c-b326bdb5c192) {'id': '2858b4ca-9085-4b02-a48c-b326bdb5c192', 'created_at': datetime.datetime
(2024, 3, 8, 20, 13, 8, 903587), 'updated_at': datetime.datetime(2024, 3, 8, 20, 13, 8, 903609)}
```

#### destroy:
##### (```destroy <class_name> <instance_id>``` and ```<class_name>.destroy(<instance_id>)```)
```
(hbnb) destroy
** class name missing **
(hbnb) destroy RandomClass
** class doesn't exist **
(hbnb) destroy BaseModel
** instance id missing **
(hbnb) destroy BaseModel 1234567890-abcd
** no instance found **
(hbnb) destroy BaseModel 2858b4ca-9085-4b02-a48c-b326bdb5c192
(hbnb) 
```

```
(hbnb) all User
[]
(hbnb) create User
5f962e54-92af-4a88-9c64-4428a8f7e14e
(hbnb) show User 5f962e54-92af-4a88-9c64-4428a8f7e14e
[User] (5f962e54-92af-4a88-9c64-4428a8f7e14e) {'id': '5f962e54-92af-4a88-9c64-4428a8f7e14e', 'created_at': datetime.datetime(2024, 3, 
8, 20, 27, 34, 63576), 'updated_at': datetime.datetime(2024, 3, 8, 20, 27, 34, 63601)}
(hbnb) destroy User 5f962e54-92af-4a88-9c64-4428a8f7e14e
(hbnb) show User 5f962e54-92af-4a88-9c64-4428a8f7e14e
** no instance found **
(hbnb) all User
[]
(hbnb) 
```

#### update:
##### (
##### ```update <class_name> <instance_id> <attr_name> <attr_value>```,
##### ```<class_name>.update(<instance_id> <attr_name> <attr_value>)```,
##### ```<class_name>.update(<instance_id> <dictionary representation>)```
##### )
```
(hbnb) update
** class name missing **
(hbnb) update MyClass
** class doesn't exist **
(hbnb) update BaseModel
** instance id missing **
(hbnb) update BaseModel 12345678900-abcd
** no instance found **
(hbnb) update BaseModel 6ca80215-4cc7-4e51-afc4-cfedb0eb7a82
** attribute name missing **
(hbnb) update BaseModel 6ca80215-4cc7-4e51-afc4-cfedb0eb7a82 name
** value missing **
(hbnb) update BaseModel 6ca80215-4cc7-4e51-afc4-cfedb0eb7a82 name ali
(hbnb)
```

```
(hbnb) all
[]
(hbnb) create BaseModel
6ca80215-4cc7-4e51-afc4-cfedb0eb7a82
(hbnb) show BaseModel 6ca80215-4cc7-4e51-afc4-cfedb0eb7a82
[BaseModel] (6ca80215-4cc7-4e51-afc4-cfedb0eb7a82) {'id': '6ca80215-4cc7-4e51-afc4-cfedb0eb7a82', 'created_at': datetime.datetime
(2024, 3, 8, 20, 41, 2, 48633), 'updated_at': datetime.datetime(2024, 3, 8, 20, 41, 2, 48676)}
(hbnb) update BaseModel 6ca80215-4cc7-4e51-afc4-cfedb0eb7a82 name ali
(hbnb) show BaseModel 6ca80215-4cc7-4e51-afc4-cfedb0eb7a82
[BaseModel] (6ca80215-4cc7-4e51-afc4-cfedb0eb7a82) {'id': '6ca80215-4cc7-4e51-afc4-cfedb0eb7a82', 'created_at': datetime.datetime
(2024, 3, 8, 20, 41, 2, 48633), 'updated_at': datetime.datetime(2024, 3, 8, 20, 41, 2, 48676), 'name': 'ali'}
(hbnb)
```

```
(hbnb) all
["[BaseModel] (6ca80215-4cc7-4e51-afc4-cfedb0eb7a82) {'id': '6ca80215-4cc7-4e51-afc4-cfedb0eb7a82', 'created_at': datetime.datetime
(2024, 3, 8, 20, 41, 2, 48633), 'updated_at': datetime.datetime(2024, 3, 8, 20, 41, 2, 48676), 'name': 'ali'}", "[BaseModel] 
(2ec04bb6-96e1-4529-8be1-f7d8be8f7714) {'id': '2ec04bb6-96e1-4529-8be1-f7d8be8f7714', 'created_at': datetime.datetime(2024, 3, 8, 20, 
47, 40, 27181), 'updated_at': datetime.datetime(2024, 3, 8, 20, 47, 40, 27203)}"]
(hbnb) BaseModel.update(6ca80215-4cc7-4e51-afc4-cfedb0eb7a82, {'name': 'ali', 'age': 50, 'rating': 8.2})
(hbnb) show BaseModel 6ca80215-4cc7-4e51-afc4-cfedb0eb7a82
[BaseModel] (6ca80215-4cc7-4e51-afc4-cfedb0eb7a82) {'id': '6ca80215-4cc7-4e51-afc4-cfedb0eb7a82', 'created_at': datetime.datetime
(2024, 3, 8, 20, 41, 2, 48633), 'updated_at': datetime.datetime(2024, 3, 8, 20, 41, 2, 48676), 'name': 'ali', 'age': 50, 'rating': 8.
2}
```
