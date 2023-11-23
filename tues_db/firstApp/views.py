from django.forms import model_to_dict
from django.http.response import JsonResponse

from .models import Person


# not the best way, but sufficient for now
def serialize(model):
    d = model_to_dict(model)
    d["id_card"] = model_to_dict(model.id_card)
    return d


def all_people(request):
    all = Person.objects.select_related("id_card").filter()
    r = [serialize(p) for p in all]
    return JsonResponse(data=r, safe=False)
