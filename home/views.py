from django.shortcuts import render
from forms import OrderForm,SearchForm
from models import Stock,Transaction
import jsonpickle

# Create your views here.
import numpy as np
def home(request):
    context = {"result": 5}
    return render(request, "Home.html", context)

def GroupProfile(request):
    RequestUser = request.user
    RequestGroup = RequestUser.group
    RequestGroup.UpdateAcount()
    GroupAsset = RequestGroup.AllAsset
    array = []
    for name,volume in GroupAsset.items():
        stock = Stock.objects.filter(StockName=name)[0]
        array.append([name,volume,stock.Get_Price()])
    context = {
        "GroupName":getattr(RequestGroup, 'GroupName'),
        "Array":array,
        "Cash":RequestUser.group.Cash
        
    }
    return render(request, "Overview.html", context)
    

def BeginToTrade(request):
    RequestUser = request.user
    RequestGroup = RequestUser.group
    context={
        "form":SearchForm(),
        "sear":True
    }
    if request.method=="POST":
        Post = request.POST.dict()
        if Post.has_key("StockName"):
            StockName=str(Post["StockName"])
        else:
            StockName=""
        if Post.has_key("Volume"):
            Volume=Post["Volume"]
        else:
            Volume=0
        if Post.has_key("TransactionType"):
            TransactionType=Post["TransactionType"]
        else:
            TransactionType=None
        print Post

        context={
            "form":OrderForm(),
            "sear":False
            
            }
        
        stock = Stock.objects.filter(StockName=StockName)
        if len(stock)==0:
            print "123123"
            stock = Stock(StockName=StockName)
            stock.save()
            context["StockData"] = jsonpickle.encode(stock.Get_data())
        else:
             context["StockData"] = jsonpickle.encode(stock[0].Get_data())

        if Volume!="" and TransactionType != None:
            RequestUser.group.UpdateAcount()
            stockprice = stock[0].Get_Price()
            if TransactionType=="buy":
                if RequestUser.group.Cash >= stockprice*float(Volume):
                    RequestGroup.transaction_set.create(TransType = TransactionType,StockOfTrans = stock[0], Volume=Volume, PriceAtTrans=stock[0].Get_Price() )
                    context["mess"] = "Succesfully making transaction"
                else:
                    context["mess"] = "You don't have enough money"
            else:
                asset = RequestUser.group.AllAsset
                if asset[StockName] >= float(Volume):
                    RequestGroup.transaction_set.create(TransType = TransactionType,StockOfTrans = stock[0], Volume=Volume, PriceAtTrans=stock[0].Get_Price() )
                    context["mess"] = "Succesfully making transaction"
                else:
                    context["mess"] = "You don't have enough this stock to sell"
        
    return render(request, "BeginToTrade.html", context)


def ShowTransactions(request):
    RequestUser = request.user
    RequestGroup = RequestUser.group
    Transactions = RequestGroup.transaction_set.all()
    array = []
    for tran in Transactions:
        array.append([
            str(getattr(tran, 'TransType')),
            str(getattr(tran, 'StockOfTrans')),
            str(getattr(tran, 'PriceAtTrans')),
            str(tran.Get_Current_Price()), 
            str(getattr(tran, 'Volume'))]
        )
    context = {
        "array":array   
    
    }
    return render(request, "Transaction.html", context)





