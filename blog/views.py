from pickle import FALSE
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Animal, Adopteur

# Create your views here.


def home(request):
    return render(request, 'index.html', {})


def Chat(request):

    animals = Animal.objects.filter(Categorie="CHAT", Adopte=False)
    return render(request, 'Chat.html', {'animals': animals})


def Chien(request):
    animals = Animal.objects.filter(Categorie="CHIEN", Adopte=False)
    return render(request, 'Chien.html',  {'animals': animals})


def Oiseau(request):
    animals = Animal.objects.filter(Categorie="Oiseau", Adopte=False)
    return render(request, 'Oiseau.html',  {'animals': animals})


def contacts(request):
    return render(request, 'contacts.html', {})


def adopt(request):
    if request.method == 'POST':
        Nom = request.POST["Nom"]
        prenom = request.POST["prenom"]
        cin = request.POST["cin"]
        salaire = int(request.POST["salaire"])
        logement = request.POST["logement"]
        famille = request.POST["famille"]
        adresse = request.POST["adresse"]
        tel = request.POST["tel"]
        idA = request.POST["idA"]

        adp = Adopteur(Nom=Nom, Prenom=prenom, Cin=cin, SalaireMensuelle=salaire, Jardin=logement,
                       SituationFamiliale=famille, Address=adresse, phoneNumber=tel, IdA=idA)
        adp.save()

        Animal.objects.filter(IdA=idA).update(Adopte=True)

    else:
        print("eeeeeee--------")
      # animals = Animal.objects.all()  # .filter("Categorie", "CHAT")
    return render(request, 'index.html', {'message': "Adoption enregistrée !"})
