import re
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, cpf):
        assert (isinstance(name, str))
        assert (isinstance(age, int))
        self.__name = name
        self.__age = age
        self.__cpf = re.sub('[^0-9]', '', str(cpf))

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def cpf(self):
        return self.__cpf

    def get_formatted_cpf(self):
        return f"{self.__cpf[0:2]}.{self.__cpf[3:5]}.{self.__cpf[6:8]}-{self.__cpf[9:10]}"

    @abstractmethod
    def total_amount(self):
        ...

    def __eq_(self, other):
        return self.__cpf == other.__cpf
