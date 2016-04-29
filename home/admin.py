from django.contrib import admin
from home.models import Group,Transaction,Stock
# Register your models here.
admin.site.register(Transaction)
admin.site.register(Group)

admin.site.register(Stock)