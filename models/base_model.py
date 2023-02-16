#!/usr/bin/python3
""" `BaseModel` class defines methods that can be inherited
"""
from uuid import uuid4
from datetime import date, datetime, timezone
import models


class BaseModel:
    """base model class
    """
    def __init__(self, *args, **kwargs):
        """Initialization of base class
        """

        if kwargs:
            for name, value in kwargs.items():
                if name == "__class__":
                    continue
                if name == "created_at" or name == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, name, value)
        else:
            self.id = str(uuid4())

            dt_now = datetime.now(timezone.utc)
            self.created_at = dt_now
            self.updated_at = dt_now
            models.storage.new(self)

    def __str__(self):
        """returns str representation of basemodel instance
        """
        out = "[{}] ({}) {}"
        out = out.format(self.__class__.__name__, self.id, str(self.__dict__))
        return out

    def save(self):
        """updates `updated_at` instance variabe when called
        """
        self.updated_at = datetime.now(timezone.utc)
        models.storage.save()

    def to_dict(self):
        """ Returns dictionary representation of instance
        """
        dict_rep = dict()
        dict_rep["__class__"] = self.__class__.__name__

        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                dict_rep[k] = v.isoformat()
            else:
                dict_rep[k] = v
        return dict_rep
