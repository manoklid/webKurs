from django.contrib import admin

from .models import  group_2342, group_2341,group_2321,group_2322,group_2361, group_2371, group_2121M,group_2161M, group_2171M,group_2122M,group_2261M,news_model
#login: admin
#password: 12345
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