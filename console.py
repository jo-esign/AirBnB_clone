#!/usr/bin/python3
""" `HBNBCommand` class includes methods
for console utility application
"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models import storage
import re
import shlex


objs = {"BaseModel": BaseModel,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        "User": User,
        "State": State,
        }


class HBNBCommand(cmd.Cmd):
    """hbnb class
    """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """ Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """ combination of Ctr D to exit the program
        """
        return True

    def emptyline(self):
        """ Doesn't execute anything
        """
        pass

    def do_create(self, args):
        """ Creates a new instance of Basemodel
        arg: Class name
        """
        if len(args) == 0 or args is None:
            print("** class name missing **")
            return

        if args in objs:
            inst = eval(str(args) + "()")
            inst.save()
            print(inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of an instance
            arg 1: class name | arg 2: obj id
        """
        if len(args) == 0 or args is None:
            print("** class name missing **")
            return
        input = shlex.split(args)
        if len(input) < 2:
            print("""** instance id missing **""")
            return
        class_name, obj_id = input[0], input[1]
        if class_name == " " or None:
            print("** class name missing **")
        if class_name not in objs:
            print("** class doesn't exist **")
            return
        if obj_id == " " or None:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, obj_id)
        storage_cache = storage.all()

        if key in storage_cache:
            print(storage_cache[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Prints the string representation of an instance
            arg 1: class name | arg 2: obj id
        """
        if len(args) == 0 or args is None:
            print("** class name missing **")
            return
        input = args.split(" ")
        if len(input) < 2:
            print("""** instance id missing **""")
            return
        class_name, obj_id = input[0], input[1]
        if class_name == " " or None:
            print("** class name missing **")
        if class_name not in objs:
            print("** class doesn't exist **")
            return
        if obj_id == " " or None:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, obj_id)
        storage_cache = storage.all()

        if key in storage_cache:
            del storage_cache[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """
        Prints string representation of all instances
        args (optional): class name
        """
        storage_cache = storage.all()
        objects = []
        if args == "":
            for key in storage_cache:
                objects.append(str(storage_cache[key]))
            print(objects)
        else:
            try:
                arg = args.split()
                eval(arg[0])
                for obj in storage_cache:
                    _dict = storage_cache[obj].to_dict()
                    if _dict['__class__'] == arg[0]:
                        objects.append(str(storage_cache[obj]))
                print(objects)
            except Exception:
                print("** class doesn't exist **")

    def do_update(self, args):
        """ Updates an instance based on the class name and id
        Usage: update <class name> <id> <attribute name>
        "<attribute value>"
        """
        # args = args.split()
        args = shlex.split(args)
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if len(args) == 4:
            class_name, obj_id = args[0], args[1]
            attr_name = args[2]
            # attr_value = " ".join(args[3:]).replace('"', '"')
            attr_value = args[3]
            storage_cache = storage.all()
            key = "{}.{}".format(class_name, obj_id)

            for obj_id in storage_cache.keys():
                if obj_id == key:
                    setattr(storage_cache[obj_id], attr_name, attr_value)
                    storage.save()
                    return
            print("** no instance found **")

    def do_count(self, args):
        """ returns the number of instances of a given class
        """
        count = 0
        for obj in storage.all().values():
            if args == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        if arg is None:
            return

        cmdPattern ="^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)"
        paramsPattern = """^"([^"]+)"(?:,\s*(?:"([^"]+)"|(\{[^}]+\}))(?:,\s*(?:("?[^"]+"?)))?)?"""
        m = re.match(cmdPattern, arg)
        if not m:
            super().default(arg)
            return
        mName, method, params = m.groups()
        m = re.match(paramsPattern, params)
        params = [item for item in m.groups() if item] if m else []

        cmd = " ".join([mName] + params)

        if method == 'all':
            return self.do_all(cmd)

        if method == 'count':
            return self.do_count(cmd)

        if method == 'show':
            return self.do_show(cmd)

        if method == 'destroy':
            return self.do_destroy(cmd)

        if method == 'update':
            return self.do_update(cmd)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
