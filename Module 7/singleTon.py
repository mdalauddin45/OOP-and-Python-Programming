#singleton --> one single instase
#if you want a new instance , you will ger the old one instace

class Singleton:
    __instace = None
    def __init__(self) -> None:
        if Singleton.__instace is None:
            Singleton.__instace = self
        else:
            raise Exception('this is singleton already have an instace , use that one by calling get_instace methode')
    
    @staticmethod
    def get_instace():
        if Singleton.__instace is None:
            Singleton()
        return Singleton.__instace

first = Singleton.get_instace()
second = Singleton.get_instace()
Third = Singleton.get_instace()
print(first)
print(second)
print(Third)

# last=Singleton()