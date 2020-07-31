from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.


a = chr(2017)
b = chr(2018)
c = chr(2019)

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>En quelle année le support Django 1.8 s'est-t-il arrété ?</h1>

        <a href="http://localhost:8000/blog/articles/""" + a + """">2017</a>
        <a href="http://localhost:8000/blog/articles/2018">2018</a>
        <a href="http://localhost:8000/blog/articles/2019">2019</a>
    """)

def view_article(request, id_article):
    """ 
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse(
        "Vous avez demandé l'article n° {0} !".format(id_article)    
    )

def view_article(request, id_article):
    if id_article > 100:
        raise Http404

    return redirect(view_redirection)

def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")