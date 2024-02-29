from django.shortcuts import render, get_list_or_404,redirect
from django.http import HttpResponse
from .models import livre, Auteur

# Create your views here.

def index(request):
    context = {
        "livres": livre.objects.all() }
    return render(request,"mangalib/index.html",context)

def show(request,livre_id): 
    context = {"livre": get_list_or_404(livre,pk=livre_id),
               
            }
    return render(request, "mangalib/show.html", context)


def add_livre(request):
    auteurs = Auteur.objects.get(nom= "Akira Toriyama" )
    livres = livre.objects.create(titre = "Dragon Ball Z", quantity=4,auteur=auteurs)
    livres = livre.objects.create(titre = "Dragon Ball", quantity=4,auteur=auteurs)
    livres = livre.objects.create(titre = "Dragon Ball GT", quantity=4,auteur=auteurs)

    return redirect("mangalib:index")

def edit_livre(request):
    book = livre.objects.get(titre = "Dragon Ball")
    book.titre = "Dragon Ball Super"
    book.save()
    return redirect("mangalib:index")

def del_livre(request):
    book = livre.objects.filter(titre__startswith = "Dragon Ball" )
    book.delete()
    return redirect("mangalib:index")
