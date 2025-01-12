from django.urls import path,include
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('libre',views.LivreViewset)
app_name = "mangalib"

# urlpatterns = [
#     path('',views.index, name='index'),  # manga/
#     path('<int:livre_id>/',views.show,name= 'show'),   # manga/<id>
#     path('ajouter_livre/',views.add_livre,name='add_livre'),
#     path('modifie_livre/<int:livre_id>/',views.edit_livre,name='edit_livre'),
#     path('suprime_livre/<int:livre_id>/',views.del_livre,name='del_livre'),
# ]

# urlpatterns = [
#     path('livre/', include(router.urls)), 
# ]

urlpatterns = [
    path("", views.index_view, name="index"),
    path("static/livres/", views.index_view, name="index"),
    path("static/about/", views.index_view, name="index"),
    path("static/", views.index_view, name="index"),
    #  path("", views.index_view, name="index"),
    path('livre/', views.allBooks), 
    path('livre/<int:livre_id>/',views.showBooks), 
    path('addBooks/',views.addBooks),
    path('update/<int:id>/',views.updateBook),
    path('delete/<int:id>/',views.delBook),
]