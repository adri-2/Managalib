from django.shortcuts import render, get_list_or_404,redirect
from django.http import HttpResponse
from .models import livre, Auteur
from .forms import LivreForm



# Create your views here.

def index(request):
    context = {
       "livres": livre.objects.all() }
    return render(request,"mangalib/index.html",context)
    """
    if request.method == 'POSt':
        form = SomeFrom(request.POST)

        if form.is_valid ():
            return redirect("mangalib:index")
    else:
        form = SomeFrom()
    context = { "form": form}
    return render(request,"mangalib/index.html",context)
    """

def show(request,livre_id): 
    context = {"livre": get_list_or_404(livre,pk=livre_id),
               
            }
    return render(request, "mangalib/show.html", context)


def add_livre(request):
    #auteurs = Auteur.objects.get(nom= "Akira Toriyama" )
    #livres = livre.objects.create(titre = "Dragon Ball Z", quantity=4,auteur=auteurs)
    #livres = livre.objects.create(titre = "Dragon Ball", quantity=4,auteur=auteurs)
    #livres = livre.objects.create(titre = "Dragon Ball GT", quantity=4,auteur=auteurs)
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mangalib:index")
    else:
        form = LivreForm()
    context = {"form": form}
    return render(request,"mangalib/livre-form.html",context)

def edit_livre(request,livre_id):
    livres = livre.objects.get(pk=livre_id)
    if request.method == 'POST':
        form = LivreForm(request.POST,instance=livres)
        if form.is_valid():
            form.save()
            return redirect("mangalib:index")
    else:
        form = LivreForm(instance=livres)
    return render(request,"mangalib/livre-form.html",{"form": form})


def del_livre(request,livre_id):
    book = livre.objects.get(pk=livre_id)
    book.delete()
    return redirect("mangalib:index")
