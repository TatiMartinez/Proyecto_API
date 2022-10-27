from django.urls import path
from .views import IncomingList

urlpatterns= [
    #path('companies/', CompanyView.as_view(), name='companies_list'),
    #path('companies/<int:id>', CompanyView.as_view(), name='companies_process'),
    path('incomings/', IncomingList.as_view(), name='incomings')

]