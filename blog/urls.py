from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.home, name="home"),

    path('index.html', views.home,  name="home"),

    path('Chat.html', views.Chat,  name="Chat"),

    path('Chien.html', views.Chien,  name="Chien"),

    path('Oiseau.html', views.Oiseau,  name="Oiseau"),

    path('contacts.html', views.contacts,  name="contacts"),

    path('adopt', views.adopt, name='adopt'),

]
