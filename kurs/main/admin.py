from django.contrib import admin

from .models import  news_model

from .models import  group_2342
from .models import  group_2341
from .models import  group_2321
from .models import  group_2322
from .models import  group_2361
from .models import  group_2371

from .models import  group_2121M
from .models import  group_2161M
from .models import  group_2171M
from .models import  group_2122M
from .models import  group_2261M

admin.site.register(news_model)

admin.site.register(group_2342)
admin.site.register(group_2341)
admin.site.register(group_2321)
admin.site.register(group_2322)
admin.site.register(group_2361)
admin.site.register(group_2371)

admin.site.register(group_2171M)
admin.site.register(group_2161M)
admin.site.register(group_2121M)
admin.site.register(group_2122M)
admin.site.register(group_2261M)