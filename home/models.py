from django.db import models
from django.contrib.auth.models import User
from registration.signals import user_registered
from django.utils import timezone
import pandas as pd

Data = pd.read_csv("Data.txt",delimiter=" ")


# Create your models here.
class Group(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, unique=True)
    GroupName = models.CharField(max_length = 100)
    Cash = float(1000000000)
    AllAsset = {}
    

    def __str__(self):
        return self.GroupName
    def UpdateAcount(self):
        trans = self.transaction_set.all()
        self.AllAsset={}
        self.Cash=float(1000000000)
        for each in trans:
            if each.TransType.lower()=="buy":
                self.Cash -= each.Volume*each.PriceAtTrans
                if self.AllAsset.has_key(each.StockOfTrans.StockName):
                    self.AllAsset[each.StockOfTrans.StockName] += each.Volume
                else:
                    self.AllAsset[each.StockOfTrans.StockName] = each.Volume
            if each.TransType.lower()=="sell":
                self.Cash += each.Volume*each.PriceAtTrans
                self.AllAsset[each.StockOfTrans.StockName] -= each.Volume
        for name,vo in self.AllAsset.items():
            if vo==0:
                del self.AllAsset[name]

#    def AddAsset(self,name,volume):
#        self.AllAsset[name]=volume
#    def DeleteAsset(self,name,volume):
#        self.AllAsset[name]=self.AllAsset[name]-volume
#        if self.AllAsset[name]==0:
#            del self.AllAsset[name]
 
def user_registered_callback(sender, user, request, **kwargs):
    profile = Group(user = user)
    profile.GroupName = str(request.POST["GroupName"])
    profile.save()
 
user_registered.connect(user_registered_callback)


class Stock(models.Model):
    StockName = models.CharField(max_length = 100)
        
    def __str__(self):
        return self.StockName
    def Get_Price(self,):
        time = str(timezone.now())[11:16]
        print time,self.StockName
        a=Data[Data['Ticker']==self.StockName][Data['Date']==time]['Close']
        if len(a)>0:
            return float(a)
        else:
            return float(666)
        

    def Get_data(self):
        time = str(timezone.now())[11:16]
        prices = Data[Data['Ticker']==self.StockName][Data['Date']<time]["Close"].tolist()
        l =[['Days', 'Stock Price']]
        i=0
        for price in prices:
            i+=1
            l.append([i,round(price,3)])
        print l
        return l
        
        
class Transaction(models.Model):
    ByGroup = models.ForeignKey(Group, on_delete = models.CASCADE)
    TransType = models.CharField(max_length =10)
    StockOfTrans = models.ForeignKey(Stock, on_delete = models.CASCADE)
    Volume = models.FloatField(max_length = 10)
    PriceAtTrans = models.FloatField(max_length = 10)
    
    def __str__(self):
        return self.TransType+" "+str(self.Volume)+" "+self.StockOfTrans.StockName

    def Get_Current_Price(self):
        return self.StockOfTrans.Get_Price()
    
    def Set_PriceAtTrans(self):
        self.PriceAtTrans = self.Get_Current_Price()
    
        
    