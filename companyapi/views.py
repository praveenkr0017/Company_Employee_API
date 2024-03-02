
from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home page is requested")
    # return HttpResponse("<h2>Yes!!!This is the homepage you are looking for.!!!<h2>")
    freinds = ['Bauwa','Kauwa','Pauwa','Nauwa','Chhauwa']
    return JsonResponse(freinds,safe = False)