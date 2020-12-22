from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(MovieForm)
admin.site.register(Tickets)
admin.site.register(Contact)
# admin.site.register(TicketsForm)
# admin.site.register(MyModel, MyModelAdmin)