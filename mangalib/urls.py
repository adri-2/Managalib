from django.urls import path
from . import views

app_name = "mangalib"

urlpatterns = [
    path('mangalib/',views.index, name='index'),  # manga/
    path('<int:livre_id>/',views.show,name= 'show'),   # manga/<id>
    path('ajouter_livre/',views.add_livre,name='add_livre'),
    path('modifie_livre/<int:livre_id>/',views.edit_livre,name='edit_livre'),
    path('suprime_livre/<int:livre_id>/',views.del_livre,name='del_livre'),
]