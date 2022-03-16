from django.shortcuts import render


from .models import  group_2342, group_2341,group_2321,group_2322,group_2361, group_2371, group_2121M,group_2161M, group_2171M,group_2122M,group_2261M,news_model



def abstract_group_view(request,group):
    upper_week = list(group.objects.exclude(week=2).values())
    bottom_week = list(group.objects.exclude(week=1).values())
    name = group._meta.db_table
    return render(request, 'main/tableTemp.html', {'up': upper_week, 'bot': bottom_week, 'name': name})


def index(request):
    news = list(news_model.objects.values())
    return render(request, 'main/index.html',{'news':news})



def g2341(request):
    return abstract_group_view(request,group_2341)

def g2342(request):
    return abstract_group_view(request, group_2342)

def g2321(request):
    return abstract_group_view(request, group_2321)

def g2322(request):
    return abstract_group_view(request, group_2322)

def g2361(request):
    return abstract_group_view(request, group_2361)

def g2371(request):
    return abstract_group_view(request, group_2371)

def g2261M(request):
    return abstract_group_view(request, group_2261M)


#группы без данных в бд
def g2121M(request):
    return abstract_group_view(request, group_2121M)

def g2122M(request):
    return abstract_group_view(request, group_2122M)

def g2161M(request):
    return abstract_group_view(request, group_2161M)

def g2171M(request):
    return abstract_group_view(request, group_2171M)