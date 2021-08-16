from django import http
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import json


json_fata_file_path = '/home/eddie/myGit/django_repos/animals_App/animal_info_env1/animals/main/animals.json'

# Create your views here.
def animal(req, num=0):
    
    if num:
        json_data_file = open(json_fata_file_path, 'r')
        data = json.load(json_data_file)
        json_data_file.close()

        animals_data = data['animals']

        animal_searched = [animal for animal in animals_data if animal['id'] == num]

        if animal_searched:
            return render(req, 'animal.html', {'animal': animal_searched[0]})
        else:
            return HttpResponse('animal not found!')

    else:
        return HttpResponseBadRequest('Animal ID was not sent')

def family(req,num=0):
    
    if num:
        json_data_file = open(json_fata_file_path, 'r')
        data = json.load(json_data_file)
        json_data_file.close()

        families_data = data['families']

        family_searched = [family for family in families_data if family['id'] == num]

        if family_searched:
            animals_data = data['animals']
            animals_in_family = [animal for animal in animals_data if animal['family'] == num]

            return render(req, 'family.html',
                          {'family_animals_list': animals_in_family, 'family_name': family_searched[0]['name']})
        else:
            return HttpResponse('family not found!')

    else:
        return HttpResponseBadRequest('Family ID was not sent')