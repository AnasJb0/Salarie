from abc import ABC,abstractmethod

class Salarie(ABC):
    _counteur = 0

    def __init__(self, nom="", num_sc=0, etat_civil="", adresse="",salba=0):
        Salarie._counteur += 1
        self._matricule = Salarie._counteur
        self._nom = nom
        self._num_sc = num_sc
        self._etat_civil = etat_civil
        self._adresse = adresse
        self._salba=salba
     
    #Getters    
    @property   
    def Getnom(self):
        return self._nom
    
    @property  
    def Getnum(self):
        return self._num_sc
    
    @property  
    def Getetat(self):
        return self._etat_civil
    
    @property  
    def GetAdresse(self) :
        return self._adresse
    
    @property  
    def Getsalba(self) :
        return self._salba
    
    @property
    def Getcounteur(self) :
        return self._counteur
    
    #setters
    def Setnom(self,new_nom) :
        self._nom=new_nom
        
    def Setnum(self,new_num) :
        self._num=new_num
        
    def Setetat(self,new_etat) :
        self._etat=new_etat
        
    def Setadresse(self,new_adresse) :
        self._adresse=new_adresse
        
    def Setsalba(self,new_salba) :
        self._salba=new_salba
        
    #methodes     
    def __str__(self):
        return print(f"Le matricule : {self._matricule} ,Le nom : {self.Getnom}, le numero de securite : {self.Getnum},L'etat civile : {self.Getetat},L'adresse : {self.GetAdresse},Salaire de base : {self.Getsalba}")

    @abstractmethod
    def Salaire():
        pass
    
    def __eq__(self, other):
        if self._matricule==other._matricule and self.Salaire==other.Salaire :
            return "both are equal."
        else:
            return "the two are not equal."


class Patron(Salarie):
    def __init__(self, nom, num_secu, etat_civil, adresse, salba, prime_risque):
        super().__init__(nom, num_secu, etat_civil, adresse, salba)
        self.__prime_risque = prime_risque
        
    def Getprime(self) :
        return self.__prime_risque
    
    def Setprime(self,new_prime) :
        self.__prime_risque=new_prime
        

    def Salaire(self):
        prix=self._salba+self.__prime_risque
        return prix
    
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __str__(self):
        return super().__str__(),print(f"Salaire : {self.Salaire()}")
    

class Vendeur(Salarie):
    def __init__(self, nom, num_secu, etat_civil,adresse,salba, commission, superieur):
        super().__init__(nom, num_secu, etat_civil, adresse,salba)
        self.__commission = commission
        self.__superieur = superieur
        
    def Getcom(self) :
        return self.__commission
    
    def Setcom(self,new_com) :
        self.__commission=new_com
    
    def Getsup(self) :
        return self.__superieur
    
    def Setsup(self,new_sup) :
        self.__superieur=new_sup
    
    def Salaire(self) :
        prix=self._salba+self.__commission
        return prix
        
    def __str__(self):
        return super().__str__(),print(f"Salaire : {self.Salaire()}")
    
    def __eq__(self, other):
        return super().__eq__(other)
        

class Caissiere(Salarie):
    def __init__(self, nom, num_secu, etat_civil, adresse,salba, superieur):
        super().__init__(nom, num_secu, etat_civil, adresse,salba)
        self.superieur = superieur

    def Salaire(self):
        prix=self._salba
        return prix

    def __str__(self):
        return super().__str__(),print(f"Salaire : {self.Salaire()}")
    def __eq__(self, other):
        return super().__eq__(other)
    
patron = Patron("anas",5424,"marier","darhom",5555,200)
vendeur = Vendeur("soulaiman",5522,"marier","darhom",6000,500,"yassine")
patron.__str__()
print(patron.__eq__(vendeur))
caissier =Caissiere("zata",3358,"marier","darhoom",2000,"belhaf")
print("---------------------------------------------------------")
vendeur.__str__()
print(vendeur.__eq__(caissier))
print("---------------------------------------------------------")
caissier.__str__()
print(caissier.__eq__(patron))
print("---------------------------------------------------------")



