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



def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria = kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {
        'kategoria_user' : kategoria_user,
        'kategoria_produkt' : kategoria_produkt,
        'kategorie' : kategorie
    }
    return render(request, 'kategoria_produkt.html', dane)

def produkt(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'produkt_user' : produkt_user, 'kategorie' : kategorie }
    return render(request, 'produkt.html', dane)




































