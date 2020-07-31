from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.

one_year_in_seconds = 31536000

def home(request):
    return render(request, 'blog/accueil.html')



def view_articles(request, id_articles):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    
    if id_articles == 0: # si id_article = 0, redirection
        return redirect(view_redirection)

    if id_articles < 10:  # si id_article inférieur a 10 : affichage
        return HttpResponse(
            "Vous avez demandé l'article n° {0} !".format(id_articles)    
        )
    else: # si id_article supérieur a 10 : erreur 404
        raise Http404

    

def view_redirection(request):
    return HttpResponse("L'article 0 n'existe pas !! Vous avez été redirigé.")


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2
    # couleurs = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
    couleurs = {
    'FF0000':'rouge', 
    'ED7F10':'orange', 
    'FFFF00':'jaune', 
    '00FF00':'vert', 
    '0000FF':'bleu', 
    '4B0082':'indigo', 
    '660099':'violet',
}

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())