from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.

one_year_in_seconds = 31536000


def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """

    """boucle "for" en Javascript pour que le calcul se fasse coté client et non coté serveur"""

    return HttpResponse("""
        <meta charset="UTF-8">
        <h1>Choisir un article entre 1 et 10</h1>

        <script>
        for (var i = 0; i <= 11; i++) {
            document.write ('<a href="http://localhost:8000/blog/articles/' + i + '"> Article n°' + i + '</a><br>')
        }
        </script>
    """
    )


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

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())