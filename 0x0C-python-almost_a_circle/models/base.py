#!/usr/bin/python3
"""base module"""
import json
import os
"""import json module"""


class Base:
    """This class create the “base” of all the classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor of the Base class
        Args:
            id: public instance attribute, holds the argument value
            __nb_objects: increments as instances are created
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Update the class Base by adding the static method
        def to_json_string(list_dictionaries):
        that returns the JSON string representation of list_dictionaries:
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes the JSON string
        representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        if list_objs is None:
            to_str = "[]"
        else:
            to_dict_list = []
            for i in list_objs:
                to_dict_list.append(i.to_dictionary())
            to_str = cls.to_json_string(to_dict_list)

        with open(file_name, 'w', encoding="utf-8") as file:
            written_str = file.write(to_str)

        return written_str

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of the JSON
        string representation json_string"""
        to_str = []
        if json_string is None or len(json_string) == 0:
            return to_str
        else:
            to_str = json.loads(json_string)
            return to_str

    @classmethod
    def create(cls, **dictionary):
        """Method that returns an instance with all attributes already set"""
        dummy_instance = cls(1, 1)

        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        file_name = cls.__name__ + ".json"
        _list = []
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding="utf-8") as file:
                json_string = file.read()

            if json_string:
                dicts = cls.from_json_string(json_string)

            for _dict in dicts:
                instance = cls.create(**_dict)
                _list.append(instance)

            return _list
        else:
            return []