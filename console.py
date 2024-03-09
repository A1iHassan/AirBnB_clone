#!/usr/bin/env python3
"""a module that contains the entry
point of the console
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.__init__ import storage


def isfloat(x):
    """
    checks if a string represents a float

    Return:
        True - False
    """
    try:
        x = float(x)
        return True
    except ValueError:
        return False


def isint(x):
    """
    checks if a string represents an int

    Return:
        True - False
    """
    try:
        x = int(x)
        return True
    except ValueError:
        return False


class HBNBCommand(cmd.Cmd):
    """
    an entry point for the console
    a custom class that inherits from the cmd class
    """

    classes = ["BaseModel", "User", "City",
               "State", "Place", "Review", "Amenity"]
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """executes when quitting the console"""
        print("")
        return True

    def emptyline(self):
        pass

    def default(self, line):
        """
        sets the default behavior of the console and how
        it interacts with given commands
        """
        if '.' in line:
            arg1, arg2 = line.split('.', 1)
            if arg1 not in self.__class__.classes:
                print("** class doesn't exist **")
            elif "all" in arg2:
                self.do_all(arg1)
            elif "count" in arg2:
                x = storage.all().keys()
                count = 0
                for i in x:
                    if arg1 in i:
                        count += 1
                print(count)
            elif "show" in arg2:
                id = arg2[arg2.index('(') + 1:arg2.index(')')]
                text = f"{arg1} {id}"
                self.do_show(text)
            elif "destroy" in arg2:
                id = arg2[arg2.index('(') + 1:arg2.index(')')]
                text = f"{arg1} {id}"
                self.do_destroy(text)
            elif "update" in arg2:
                text = arg2[arg2.index('(') + 1:arg2.index(')')]
                if text == "":
                    print("** instance id missing **")
                elif not "," in text:
                    print("** attribute name missing **")
                else:
                    _id, _ = text.split(", ", 1)
                    if not _id:
                        print("** instance id missing **")
                    else:
                        try:
                            _dict = arg2[arg2.index('{') + 1:arg2.index('}')]
                            pairs = _dict.split(", ")
                            _dict = dict()
                            for i in pairs:
                                key, value = i.split(":")
                                if '"' in key:
                                    key = key.split('"')[1]
                                elif "'" in key:
                                    key = key.split("'")[1]
                                if '"' in value:
                                    value = value.split('"')[1]
                                elif "'" in value:
                                    value = value.split("'")[1]
                                else:
                                    if isint(value):
                                        value = int(value)
                                    elif isfloat(value):
                                        value = float(value)
                                _dict[key] = value
                            for key, value in _dict.items():
                                x = f"{arg1} {_id} {key} {value}"
                                self.do_update(x)
                        except ValueError:
                            x = f"{arg1} " + ''.join([i for i in text
                                                    if i != ','
                                                    and i != '"' and i != "'"])
                            self.do_update(x)

    def do_create(self, arg):
        """Creates a new instance of the given class object ,
        saves it (to the JSON file) and prints the id

        Args:
            arg: user input (class name)
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.__class__.classes:
            print("** class doesn't exist **")
        else:
            if arg == "BaseModel":
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            elif arg == "User":
                new_instance = User()
                new_instance.save()
                print(new_instance.id)
            elif arg == "State":
                new_instance = State()
                new_instance.save()
                print(new_instance.id)
            elif arg == "City":
                new_instance = City()
                new_instance.save()
                print(new_instance.id)
            elif arg == "Place":
                new_instance = Place()
                new_instance.save()
                print(new_instance.id)
            elif arg == "Review":
                new_instance = Review()
                new_instance.save()
                print(new_instance.id)
            elif arg == "Amenity":
                new_instance = Amenity()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id

        Args:
            args: user input
        """
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in self.__class__.classes:
            print("** class doesn't exist **")
        elif len(args_list) != 2:
            print("** instance id missing **")
        else:
            x = storage.all()
            i = 1
            _key = f"{args_list[0]}.{args_list[1]}"
            for key, value in x.items():
                if key == _key and "BaseModel" in key:
                    i = 0
                    y = BaseModel(**value)
                    print(y)
                elif key == _key and "User" in key:
                    i = 0
                    y = User(**value)
                    print(y)
                elif key == _key and "City" in key:
                    i = 0
                    y = City(**value)
                    print(y)
                elif key == _key and "State" in key:
                    i = 0
                    y = State(**value)
                    print(y)
                elif key == _key and "Place" in key:
                    i = 0
                    y = Place(**value)
                    print(y)
                elif key == _key and "Review" in key:
                    i = 0
                    y = Review(**value)
                    print(y)
                elif key == _key and "Amenity" in key:
                    i = 0
                    y = Amenity(**value)
                    print(y)
            if i:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class
        name and id (save the change into the JSON file
        """
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in self.__class__.classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            x = storage.all()
            i = 1
            _key = f"{args_list[0]}.{args_list[1]}"
            for pair in x.items():
                if pair[0] == _key:
                    i = 0
                    del x[_key]
                    storage.save()
                    break
            if i:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all
        BaseModel or $ all
        """
        if not arg:
            a = [str(BaseModel(**value))
                 for key, value in storage.all().items() if "BaseModel" in key]
            b = [str(User(**value))
                 for key, value in storage.all().items() if "User" in key]
            c = [str(City(**value))
                 for key, value in storage.all().items() if "City" in key]
            d = [str(State(**value))
                 for key, value in storage.all().items() if "State" in key]
            e = [str(Place(**value))
                 for key, value in storage.all().items() if "Place" in key]
            f = [str(Review(**value))
                 for key, value in storage.all().items() if "Review" in key]
            g = [str(Amenity(**value))
                 for key, value in storage.all().items() if "Amenity" in key]
            z = [*a, *b, *c, *d, *e, *f, *g]
            print(z)
        elif arg == "BaseModel":
            x = [str(BaseModel(**value))
                 for key, value in storage.all().items()
                 if "BaseModel" in key]
            print(x)
        elif arg == "User":
            y = [str(User(**value))
                 for key, value in storage.all().items()
                 if "User" in key]
            print(y)
        elif arg == "City":
            y = [str(City(**value))
                 for key, value in storage.all().items()
                 if "City" in key]
            print(y)
        elif arg == "State":
            y = [str(State(**value))
                 for key, value in storage.all().items()
                 if "State" in key]
            print(y)
        elif arg == "Place":
            y = [str(Place(**value))
                 for key, value in storage.all().items()
                 if "Place" in key]
            print(y)
        elif arg == "Review":
            y = [str(Review(**value))
                 for key, value in storage.all().items()
                 if "Review" in key]
            print(y)
        elif arg == "Amenity":
            y = [str(Amenity(**value))
                 for key, value in storage.all().items()
                 if "Amenity" in key]
            print(y)
        else:
            print("** class doesn't exist **")
        storage.save()

    def do_update(self, args):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute (save
        the change into the JSON file)

        Args:
            arg: user input
        """
        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] not in self.__class__.classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif not (f"{arg[0]}.{arg[1]}" in storage.all().keys()):
            print("** no instance found **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            x = storage.all()
            if arg[3].isdigit():
                arg[3] = int(arg[3])
            elif isfloat(arg[3]):
                arg[3] = float(arg[3])
            x[f"{arg[0]}.{arg[1]}"][arg[2]] = arg[3]
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
