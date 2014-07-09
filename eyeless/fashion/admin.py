from django.contrib import admin
from fashion.models import EyelessUser, EyelessStylist, EyelessPost, EyelessMessage

# Register your models here.
admin.site.register(EyelessUser)
admin.site.register(EyelessStylist)
admin.site.register(EyelessPost)
admin.site.register(EyelessMessage)