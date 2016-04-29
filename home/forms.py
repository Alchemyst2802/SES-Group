from registration.forms import RegistrationForm
from django import forms
from models import Transaction
import Choise as ch
class ExRegistrationForm(RegistrationForm):
    GroupName = forms.CharField()

#STOCK_CHOICES = (
#    ("AAA", ("AAA")),
#    ("ABT", ("ABT"))
#)
RELEVANCE_CHOICES = (
    ("buy", ("Buy")),
    ("sell", ("Sell"))
)
class SearchForm(forms.Form):
    StockName = forms.ChoiceField(choices = ch.STOCK_CHOICES , label='StockName')


class OrderForm(forms.Form):
    StockName = forms.ChoiceField(choices = ch.STOCK_CHOICES , label='StockName')
    Volume = forms.FloatField(label ='Volume') 
    TransactionType=forms.ChoiceField(choices=RELEVANCE_CHOICES,label ='Transaction Type')
    