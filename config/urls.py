from django.contrib import admin
from django.urls import path
from principal import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.inicio, name='inicio'),
     # Al dejar las comillas vacías, esta es la "Home"
     path('curso/<int:curso_id>/', views.detalle_curso, name='detalle'),
]
