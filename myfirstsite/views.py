from django.shortcuts import render
def homepage_render(request):
    page= render(request, 'homepage.html')
    return page

def randompage_render(request):
   import random
   nb = random.randint(0,100)
   context = {"nombre_aleatoire":nb}
   page = render(request, 'random.html',context)
   return page

def annuairepage_render(request):
   people = ["gege","theo","lucie","luc","lucas","lucas"]
   context = {"contact_list":people}    
   page = render(request, 'annuaire.html',context)
   return page

def accesspage_render(request):
    context={"access":True} 
    page=render(request, 'access.html',context)
    return page

def biopage_render(request,username):
    context={"nom":username}
    page=render(request, 'bio.html',context)
    return page

def motdepasse_render(request):
    if request.method == 'GET':
        page = render(request, 'motdepasse.html')
        return page
    if request.method == 'POST':
        mp = request.POST['motdepasse']
        if mp == 'azerty':
            from django.http import HttpResponse
            return HttpResponse("Bravo !")
        else:
            page = render(request, 'motdepasse.html')
        return page