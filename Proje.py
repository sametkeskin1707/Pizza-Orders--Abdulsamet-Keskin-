import csv
import datetime
import pandas as pd

df = pd.read_csv(r'c:/Users/Monster/Downloads\metin.csv')
print(df)

class Pizza():
    def __init__(self , isim , component , cost , description):
      print("Pizza sitesine hoşgeldin")
      self.isim = isim
      self.component=component
      self.cost=cost
      self.description=description
    def get_cost(self):
       return self.component.get_cost() + \
         Pizza.get_cost(self)
    def get_description(self):
       return self.component.get_description() + \
         ' ' + Pizza.get_description(self)
  
   ## Margarita = Pizza("margarita" , "et" , 3, "the are so many et var") vs . diye tüm tüm seçenekler girilebilir 
   
   
class Klasik(Pizza):
  def __init__(self, fiyati , get_description):
      self.fiyati = fiyati
      self.get_description=get_description
      
class Margarita(Pizza):
    def  __init__(self,fiyati,get_description):
          self.fiyati = fiyati 
          self.get_description=self.get_description
class Sade(Pizza):
    def  __init__(self,fiyati,get_description):
        self.fiyati = fiyati 
        self.get_description=get_description
      
class İtalyan(Pizza):
    def  __init__(self,fiyati,description):
        self.fiyati = fiyati 
        self.get_description=get_description
    ## moherotti = İtalyan(22,"that so goof")
          
          
          
     
 class Decorator():
    def get_cost(self):
    return self.component.get_cost() + \
       Pizza.get_cost(self)


    

import datetime
datetime.datetime.now()
siparis_zamani = datetime.datetime.now()
number=input("Please write number? ")
isim=input("Please write name")
TC_Kimlik=input("Please write tc no")
Kredi_no=input("Please write kreni no")
Kredi_passwd=input("Please write kredi passwd")
print(number , isim , TC_Kimlik , Kredi_no , Kredi_passwd , siparis_zamani)

# kullanıcıdan isim, TC kimlik numarası, kredi kartı numarası ve kredi kartı şifresi istemektedir

