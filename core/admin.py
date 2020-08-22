from django.contrib import admin
from .models import (
    ShrnkUrl,
    Click,
)
# Register your models here.
admin.site.register(ShrnkUrl)
admin.site.register(Click)