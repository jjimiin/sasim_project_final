from django.contrib import admin
from .models import Post, Contact_Post, Contact_Contact

# Register your models here.
admin.site.register(Post)
admin.site.register(Contact_Post)
admin.site.register(Contact_Contact)
