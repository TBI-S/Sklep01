from django.shortcuts import render
from .models import Produkty, Kategoria
from django.http import HttpResponse

# Create your views here.
def index(request):
    #wszystkie = Produkty.objects.all()
    #jeden = Produkty.objects.get(pk=3)
    #kategoria = Produkty.objects.filter(kategoria=1)
    #producent = Produkty.objects.filter(producent=2)
    kategorie = Kategoria.objects.all()
    #null = Produkty.objects.filter(kategoria__isnull=True)
    #return HttpResponse(kategorie)
    dane = {'kategorie' : kategorie}
    return render(request, 'szablon.html', dane)

'''

def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user.nazwa)

def produkt(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    napis = "<h1>" + str(produkt_user) + "</h1>" + \
            "<p>" + str(produkt_user.opis) + "</p>" + \
            "<p>" + str(produkt_user.cena) + "/<p>"
    return HttpResponse(napis)

'''


































