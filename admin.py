from django.contrib import admin
from .models import expense_management
from .models import Sign_In

admin.site.register(expense_management)
admin.site.register(Sign_In)