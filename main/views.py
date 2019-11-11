from django.shortcuts import render
from django.http import HttpResponse
from .models import Ingredient
from .forms import SearchForm, ConvertForm
from main.lib.util.converter import US_VOLUME_RATIOS, SI
import json

# Create your views here.
def home(request):
    search_form = SearchForm()
    convert_form = ConvertForm()
    id = request.session.get('id', 1)
    request.session['id'] = id
    ingredient = Ingredient.objects.get(id__exact=id)

    return render(
        request=request,
        template_name="main/home.html",
        context={
            "ingredient": ingredient,
            "search_form": search_form,
            "convert_form": convert_form,
            }
        )

def autocomplete(request):
    if request.is_ajax():
        seq = request.GET.get('term','')
        ingredients = Ingredient.objects.filter(description__icontains=seq).order_by('description')
        results = []
        for ingredient in ingredients:
            ingredient_json = {}
            ingredient_json['id'] = ingredient.id
            ingredient_json['label'] = ingredient.description
            ingredient_json['value'] = ingredient.description
            results.append(ingredient_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    return HttpResponse(data, 'application/json')

def fetch(request):
    if request.is_ajax():
        input = request.GET.get('ingredient', None)
        if (input is not None and
            Ingredient.objects.filter(description__icontains=input).exists()):
            ingredient = Ingredient.objects.filter(description__icontains=input).first()
        else:
            ingredient = Ingredient.objects.get(id__exact=request.session['id'])
        result = {}
        result['category'] = ingredient.category
        result['description'] = ingredient.description
        data = json.dumps(result)
        request.session['id'] = ingredient.id
    return HttpResponse(data, 'application/json')

def convert(request):
    if request.is_ajax():
        amount = request.GET.get('amount', None)
        unit_from = request.GET.get('unit_from', None)
        unit_to = request.GET.get('unit_to', None)

        if (amount is not None and
            unit_from is not None and
            unit_to is not None):
            result = {}
            conversion = (US_VOLUME_RATIOS[unit_from] / US_VOLUME_RATIOS[unit_to]) * float(amount)
            result['amount'] = amount
            result['unit_from'] = unit_from
            result['unit_to'] = unit_to
            result['conversion'] = round(conversion, 4)
            data = json.dumps(result)
    return HttpResponse(data, 'application/json')

def si(request):
    if request.is_ajax():
        amount = request.GET.get('amount', None)
        unit_from = request.GET.get('unit_from', None)
        ingredient = Ingredient.objects.get(id__exact=request.session['id'])
        density = ingredient.density

        if density == 0:
            data = {'fail': 'We do not have this information at the moment'}
            data = json.dumps(data)
        else:
            result = {}
            mass = round(float(amount) * US_VOLUME_RATIOS[unit_from] * SI * density, 4)
            result['amount'] = amount
            result['mass'] = mass
            result['unit'] = unit_from
            data = json.dumps(result)
    return HttpResponse(data, 'application/json')
