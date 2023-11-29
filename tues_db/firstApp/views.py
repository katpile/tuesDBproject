from django.forms import model_to_dict
from django.http.response import JsonResponse
from django.db import connection
from .models import Person
from django.shortcuts import render


# not the best way, but sufficient for now
def serialize(model):
    d = model_to_dict(model)
    d["id_card"] = model_to_dict(model.id_card)
    return d


def all_people(request):
    all = Person.objects.select_related("id_card").filter()
    r = [serialize(p) for p in all]
    return JsonResponse(data=r, safe=False)


def simple_form_inj(request):
    if request.method == "GET":
        return render(request, "simple_form_injection.html", context={})
    if request.method == "POST":
        print(request.POST)
        with connection.cursor() as c:
            # ' or 1=1--
            r = c.execute(
                "select * from \"firstApp_person\" where first_name ='" + request.POST['first_name'] + "'")
            all_rows = c.fetchall()
            return JsonResponse(data={"data": all_rows})
    return JsonResponse(data={})
