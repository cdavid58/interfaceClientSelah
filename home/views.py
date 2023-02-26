from operations.operations import Opertations
from django.http import HttpResponse
from django.shortcuts import render
import json

def Home(request):
	op = Opertations()
	with open('data/colombia.json', encoding="utf8") as file:
		data = json.load(file)
	return render(request,'index.html',{'city':data,'op':op.GetListPropertys(),'cat':op.GetSpace()})


def GetCountry(request):
	if request.is_ajax():
		with open('data/'+str(request.GET['country']).lower()+'.json', encoding="utf8") as file:
			data = json.load(file)
		return HttpResponse(json.dumps(data))

def Details_Property(request,pk):
	op = Opertations().GetDeatilProperty(pk)
	return render(request,'property/details.html',{'op':op,'photos':op['multimedia'],'inf_1':op['information'][0],'inf_2':op['information_extra'][0]})

def Contact(request):
	return render(request,'contact.html')