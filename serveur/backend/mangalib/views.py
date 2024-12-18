from django.shortcuts import render, get_list_or_404,redirect
from django.http import HttpResponse
from .models import Livre, Auteur
from .forms import LivreForm
from rest_framework.viewsets import ModelViewSet
from .serializers import AuteurSrializer,LivreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# class LivreViewset(ModelViewSet):
#     queryset=livre.objects.all()
#     serializer_class=LivreSerializer

@api_view(['GET'])
def allBooks(request):
    livres = Livre.objects.all()
    serialization =LivreSerializer(livres,many=True)
    return Response(serialization.data)


@api_view(['GET'])
def showBooks(request,livre_id): 
    livre =  Livre.objects.get(pk=livre_id)
    serializer = LivreSerializer(livre)
    return Response(serializer.data)


@api_view(['POST'])
def addBooks(request):
    serializer = LivreSerializer(data = request.data,many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateBook(request,id):
    book = Livre.objects.get(id=id)
    serializer = LivreSerializer(instance=book,date=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delBook(request,id):
    book=Livre.objects.get(id=id)
    book.delete()
    return Response('Livre supprime !!')




# def index(request):
#     context = {
#        "livres": livre.objects.all() }
#     return render(request,"mangalib/index.html",context)
    # """
    # if request.method == 'POSt':
    #     form = SomeFrom(request.POST)

    #     if form.is_valid ():
    #         return redirect("mangalib:index")
    # else:
    #     form = SomeFrom()
    # context = { "form": form}
    # return render(request,"mangalib/index.html",context)
    # """

# def show(request,livre_id): 
#     context = {"livre": get_list_or_404(livre,pk=livre_id),
               
#             }
#     return render(request, "mangalib/show.html", context)


# def add_livre(request):
#     #auteurs = Auteur.objects.get(nom= "Akira Toriyama" )
#     #livres = livre.objects.create(titre = "Dragon Ball Z", quantity=4,auteur=auteurs)
#     #livres = livre.objects.create(titre = "Dragon Ball", quantity=4,auteur=auteurs)
#     #livres = livre.objects.create(titre = "Dragon Ball GT", quantity=4,auteur=auteurs)
#     if request.method == 'POST':
#         form = LivreForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("mangalib:index")
#     else:
#         form = LivreForm()
#     context = {"form": form}
#     return render(request,"mangalib/livre-form.html",context)

# def edit_livre(request,livre_id):
#     livres = livre.objects.get(pk=livre_id)
#     if request.method == 'POST':
#         form = LivreForm(request.POST,instance=livres)
#         if form.is_valid():
#             form.save()
#             return redirect("mangalib:index")
#     else:
#         form = LivreForm(instance=livres)
#     return render(request,"mangalib/livre-form.html",{"form": form})


# def del_livre(request,livre_id):
#     book = livre.objects.get(pk=livre_id)
#     book.delete()
#     return redirect("mangalib:index")
