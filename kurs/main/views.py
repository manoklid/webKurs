from django.shortcuts import render


from .models import  group_2342, group_2341,group_2321,group_2322,group_2361, group_2371, group_2121M,group_2161M, group_2171M,group_2122M,group_2261M,news_model





def index(request):

    news = list(news_model.objects.values())
    return render(request, 'main/index.html',{'news':news})

def g2341(request):
    upper_week = list(group_2341.objects.exclude(week=2).values())
    bottom_week= list(group_2341.objects.exclude(week=1).values())
    name=group_2341._meta.db_table
    return render(request, 'main/tableTemp.html', {'up': upper_week,'bot':bottom_week,'name':name})

def g2342(request):
    upper_week = list(group_2342.objects.exclude(week=2).values())
    bottom_week= list(group_2342.objects.exclude(week=1).values())
    name = group_2342._meta.db_table
    return render(request, 'main/tableTemp.html', {'up': upper_week,'bot':bottom_week,'name':name})

def g2321(request):
    upper_week = list(group_2321.objects.exclude(week=2).values())
    bottom_week= list(group_2321.objects.exclude(week=1).values())
    name = group_2321._meta.db_table
    return render(request,'main/tableTemp.html', {'up': upper_week,'bot':bottom_week,'name':name})

def g2322(request):
    upper_week = list(group_2322.objects.exclude(week=2).values())
    bottom_week= list(group_2322.objects.exclude(week=1).values())
    name = group_2322._meta.db_table
    return render(request,'main/tableTemp.html', {'up': upper_week,'bot':bottom_week,'name':name})

def g2361(request):
    upper_week = list(group_2361.objects.exclude(week=2).values())
    bottom_week= list(group_2361.objects.exclude(week=1).values())
    name = group_2361._meta.db_table
    return render(request,'main/tableTemp.html', {'up': upper_week,'bot':bottom_week,'name':name})

def g2371(request):
    upper_week = list(group_2371.objects.exclude(week=2).values())
    bottom_week= list(group_2371.objects.exclude(week=1).values())
    name = group_2371._meta.db_table
    return render(request,'main/tableTemp.html', {'up': upper_week,'bot':bottom_week,'name':name})


def g2261M(request):
    upper_week = list(group_2261M.objects.exclude(week=2).values())
    bottom_week= list(group_2261M.objects.exclude(week=1).values())
    name = group_2261M._meta.db_table
    return render(request,'main/tableTemp.html', {'up': upper_week,'bot':bottom_week,'name':name})

def g2121M(request):
    upper_week = list(group_2121M.objects.exclude(week=2).values())
    bottom_week= list(group_2121M.objects.exclude(week=1).values())
    name = group_2121M._meta.db_table
    return render(request,'main/tableTemp.html', {'up': upper_week,'bot':bottom_week,'name':name})

def g2122M(request):
    upper_week = list(group_2122M.objects.exclude(week=2).values())
    bottom_week= list(group_2122M.objects.exclude(week=1).values())
    name = group_2122M._meta.db_table
    return render(request,'main/tableTemp.html', {'up': upper_week,'bot':bottom_week,'name':name})

def g2161M(request):
    upper_week = list(group_2161M.objects.exclude(week=2).values())
    bottom_week= list(group_2161M.objects.exclude(week=1).values())
    name = group_2161M._meta.db_table
    return render(request,'main/tableTemp.html', {'up': upper_week,'bot':bottom_week,'name':name})

def g2171M(request):
    upper_week = list(group_2171M.objects.exclude(week=2).values())
    bottom_week= list(group_2171M.objects.exclude(week=1).values())
    name = group_2171M._meta.db_table
    return render(request,'main/tableTemp.html', {'up': upper_week,'bot':bottom_week,'name':name})