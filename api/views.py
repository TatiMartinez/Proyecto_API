from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
#from .models import Company
import json
from .models import Incoming
from .src import  userMessage


# Create your views here.
"""
class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            companies=list(Company.objects.filter(id=id).values())
            if len(companies)> 0:
                company=companies[0]
                datos= {'message': "Success", 'companies': company}
            else:
                datos= {'message': "Companies not found.."}
            return JsonResponse(datos)
        else:
            companies= list(Company.objects.values())
            if len(companies)>0:
                datos= {'message': "Success", 'companies': companies}
            else:
                datos= {'message': "Companies not found.."}
        return JsonResponse(datos)


    def post(self, request):
        # print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Company.objects.create(name=jd['name'],website=jd['website'],foundation=jd['foundation'])
        datos= {'message': "Success"}
        return JsonResponse(datos)


    def put(self, request, id):
        jd= json.loads(request.body)
        companies=list(Company.objects.filter(id=id).values())
        if len(companies)> 0:
            company= Company.objects.get(id=id)
            company.name=jd['name']
            company.website=jd['website']
            company.foundation=jd['foundation']
            company.save()
            datos= {'message': "Success"}
        else:
            datos= {'message': "Companies not found.."}
        return JsonResponse(datos)


    def delete(self, request,id):
        companies=list(Company.objects.filter(id=id).values())
        if len(companies)> 0:
            Company.objects.filter(id=id).delete()
            datos= {'message': "Success"}


        else:
            datos= {'message': "Companies not found.."}
        return JsonResponse(datos)

"""
class IncomingList(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    """def get(self, request, id=0):
        if (id>0):
            incomings=list(Incoming.objects.filter(id=id).values())
            if len(incomings)> 0:
                incoming=incomings[0]
                datos= {'message': "Success", 'incomings': incoming}
            else:
                datos= {'message': "incomings not found.."}
            return JsonResponse(datos)
        else:
            incomings= list(Incoming.objects.values())
            if len(incomings)>0:
                datos= {'message': "Success", 'incomings': incomings}
            else:
                datos= {'message': "incomings not found.."}
        return JsonResponse(datos)
    """

    def post(self, request):
        print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        result= Incoming.objects.create(conversationId=jd['conversationId'],payload=jd['payload'])
        print("result", result.pk)
        result.botResponse = userMessage(conversationId=jd['conversationId'],payload=jd['payload'])
        result.save()
        datos= {'message': "Success", "botResponse": result.botResponse}
        return JsonResponse(datos)


    #def put(self, request, id):
        pass

    #def delete(self, request,id):
        pass



