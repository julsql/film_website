from django.shortcuts import render
from forms import RechercheForm
import recherche


# Create your views here.
def home(request):
    infos = recherche.alea()
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = RechercheForm(request.POST)

        if form.is_valid():
            id = request.POST.get('id')
            titre = request.POST.get('titre')
            real = request.POST.get('real')
            lang = request.POST.get('lang')
            date = request.POST.get('date')
            duree = request.POST.get('duree')
            color = request.POST.get('color')
            voix = request.POST.get('voix')
            disque = request.POST.get('disque')
            type = request.POST.get('type')
            acteurs = request.POST.get('acteurs')

            infos = recherche.recherche_film(id, titre, real, lang, date, duree, color, voix, disque,
                                           type, acteurs)
            print(id, titre, real, lang, date, duree, color, voix, disque,
                  type, acteurs)
            return render(request, 'main/filmrecherche.html', {'form': form, 'infos': infos})
        return render(request, 'main/filmrecherche.html', {'form': form, 'infos': infos})
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = RechercheForm()

    return render(request, 'main/home.html', {'form': form, 'infos': infos})


def filmrecherche(request):

    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = RechercheForm(request.POST)

        if form.is_valid():
            id = request.POST.get('id')
            titre = request.POST.get('titre')
            real = request.POST.get('real')
            lang = request.POST.get('lang')
            date = request.POST.get('date')
            duree = request.POST.get('duree')
            color = request.POST.get('color')
            voix = request.POST.get('voix')
            disque = request.POST.get('disque')
            type = request.POST.get('type')
            acteurs = request.POST.get('acteurs')
            print(id, titre, real, lang, date, duree, color, voix, disque,
                                           type, acteurs)

            infos = recherche.recherche_film(id, titre, real, lang, date, duree, color, voix, disque,
                                           type, acteurs)
            return render(request, 'main/filmrecherche.html', {'form': form, 'infos': infos})
        infos = recherche.recherche_film()
        return render(request, 'main/filmrecherche.html', {'form': form, 'infos': infos})
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = RechercheForm()
    infos = recherche.recherche_film()
    return render(request, 'main/filmrecherche.html', {'form': form, 'infos': infos})


def pagefilm(request, id):
    infos = recherche.page(id)
    return render(request, 'main/pagefilm.html', infos)


def statistiques(request):
    infos = recherche.stat()
    return render(request, 'main/statistiques.html', infos)
