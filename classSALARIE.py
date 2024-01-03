from abc import ABCMeta, abstractmethod
import random

class SALARIER(metaclass = ABCMeta):
    counter = 0
    def __init__(self,nom=0,NumSEC=0,EtatCivil=0,Adress=0,Salair=0):
        self.__nom = nom
        self.__NumSEC = NumSEC
        self.__EtatCivil = EtatCivil
        self.__Adress = Adress
        self.__salair = Salair
        SALARIER.counter += 1
    #getters
    @property
    def getcount (self):
       return self.counter
    @property
    def getnom(self):
        return self.__nom
    @property
    def getNumSEC(self):
        return self.__NumSEC
    @property
    def getEtatCivil(self):
        return self.__EtatCivil
    @property
    def getAdress(self):
        return self.__Adress
    @property
    def getSalair (self):
        return self.__salair
    #setters 
    def setnom (self,nom):
           self.__nom = nom
    def setnum (self,NumSEC):
           self.__NumSEC = NumSEC
    def setec (self,EtatCivil):
           self.__EtatCivil = EtatCivil
    def setadr (self,Adress):
           self.__Adress = Adress
    def setsalaire (self,salair):
           self.__salair = salair
    #Methods
           
    @abstractmethod
    def SalairTotal(self):
        pass
    @abstractmethod
    def __eq__(self):
        pass
    def Matricule(self):
        Matricule = random.randint(1,999999)
        return Matricule
    def __str__(self):
        print (f"--Name : {self.getnom} \nMatricule :{self.Matricule()} \nThe security number : {self.getNumSEC} \nCivil status {self.getEtatCivil} \nThe Address {self.getAdress} \nBase Salary : {self.getSalair} MAD" )

class PATRON(SALARIER):
    def __init__(self, nom=0, NumSEC=0, EtatCivil=0, Adress=0, Salair=0 ,prime=0):
        super().__init__(nom, NumSEC, EtatCivil, Adress, Salair)
        self.__prime = prime
    #getter
    @property
    def getprime(self):
        return self.__prime
    def setprime(self,Prim):
        self.__prime = Prim
    def SalairTotal(self):
        return self.getprime+self.getSalair
    def __str__(self):
        super().__str__()
        print(f"Total Salary of boss {self.SalairTotal()} DH")
    
    def __eq__(self, other):
        if self.Matricule() == other.Matricule() and self.getSalair == other.getSalair:
           return True
        else:
            return False
class VENDEUSE(SALARIER):
    def __init__(self, nom=0, NumSEC=0, EtatCivil=0, Adress=0, Salair=0, comission=0, SuperH=0):
        super().__init__(nom, NumSEC, EtatCivil, Adress, Salair)
        self.comission = comission
        self.superH = SuperH
    @property
    def getComission(self):
        return self.comission 
    @property
    def getSuperH(self):
        return self.superH
    def SalairTotal(self):
        return self.getSalair+self.getComission
    def __str__(self):
        super().__str__()
        print(f"the Total Salary of the seller {self.SalairTotal()} DH \nUpper hierarchy {self.getSuperH}")
    def __eq__(self, other):
        return super().__eq__(other)
    
class Caisiere(SALARIER):
    def __init__(self, nom=0, NumSEC=0, EtatCivil=0, Adress=0, Salair=0, superH=0):
        super().__init__(nom, NumSEC, EtatCivil, Adress, Salair)
        self.superH = superH
    def getSuperH(self):
        return self.superH
    def SalairTotal(self):
        return self.getSalair
    def __str__(self):
        super().__str__()
        print(f"Upper hierarchy {self.getSuperH()}")
    def __eq__(self, other):
        return super().__eq__(other)
    



patron1 = PATRON("ahmed",122,"Single","azli",20000,1000)
patron2 = PATRON("ali",221,"married","iziki",20000,900)
patron1.__str__()
print(patron2.__eq__(patron1))
v1 = VENDEUSE("Wissal",99,"Single","lbadiaa",6000,100,"hamid njar")
v1.__str__()
C1=Caisiere("FARAH",88,"married","lmhamid",2500,"moha")
C1.__str__()
        

         
