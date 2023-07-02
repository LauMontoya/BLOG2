from django.contrib import admin
from django.urls import path
from weblog.views import saludo, segunda_vista, hoy, minombre, testingtemplate, curso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('segunda_vista/', segunda_vista),
    path('hoy/', hoy),
    path('minombre/<nombre>', minombre),
    path('testingtemplate/', testingtemplate),
    path('curso/', curso)
]
