
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_city', views.add_city, name='add_city'),
    path('<int:pk>', views.CityDetailView.as_view(), name='details'),
    path('<int:pk>/update', views.CityUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.CityDeleteView.as_view(), name='delete')
]
