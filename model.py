from functools import total_ordering

@total_ordering
class Valuta:
    nev: str
    jeloles: str
    __arfolyam:  float

    def __init__(self, nev:str, jeloles:str, __arfolyam:float) -> None:
        self.nev = nev
        self.jeloles = jeloles
        self.__arfolyam = __arfolyam

    @property
    def arf(self):
        return self.__arfolyam

    @arf.setter
    def modosit(self, value:float):
        self.__arfolyam = value

    def __repr__(self) -> str:
        return self.nev + ", " + self.jeloles + ", " + str(self.__arfolyam)

    def __str__(self) -> str:
        return self.jeloles + " (" + self.nev + "): $" + str(self.__arfolyam)

    def __eq__(self, o: object) -> bool:
        if not isinstance(self, Valuta):
            return NotImplemented
        elif self.__arfolyam == o.__arfolyam and self.nev == o.nev  and self.jeloles == o.jeloles:
            return True
        else:
            return False
    def __lt__(self, o):
        if isinstance(self, Valuta):
            return self.__arfolyam > o.__arfolyam and self.nev > o.nev and self.jeloles > o.jeloles
        return False

class Crypto(Valuta):
    __name: str

    def __init__(self, nev: str, jeloles: str, arfolyam: float, name:str) -> None:
        super().__init__(nev, jeloles, arfolyam)
        self.__name = name
    @property
    def tervezo(self):
        return self.__name

    @tervezo.setter
    def tervezo_setter(self, value):
        self.__name = value
        return self.__name

    def __repr__(self) -> str:
        return super().__repr__() +", "+ self.__name

    def __str__(self) -> str:
        return super().__str__() + ", @"+ self.__name

    @staticmethod
    def erosebb(l:list, arfolyam: float) -> list:
        eredmeny = []
        for i in range(len(l)):
            if i > arfolyam:
                eredmeny.append(i)
        return eredmeny



