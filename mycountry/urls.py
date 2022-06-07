from django.urls import path,include
from .import views

urlpatterns = [
    
    path('',views.india,name='india'),
    path('kerala/',views.kerala,name='kerala'),
    path('goa/',views.goa,name='goa'),
    path('kashmir/',views.kashmir,name='kashmir'),
    path('assam/',views.assam,name='assam'),
    path('rajasthan/',views.rajasthan,name='rajasthan'),
    path('ketch/',views.ketch,name='ketch'),
    path('men/',views.men,name='men'),
    path('women/',views.women,name='women')
]