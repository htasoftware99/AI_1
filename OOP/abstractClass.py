from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def walk():pass

    #@abstractmethod
    def run():pass


class Bird(Animal):
    def __init__(self):
        print("bird")
    
    def walk():
        print("walk")
    
    # def run():
    #     print("run")
b1 = Bird()