from django.shortcuts import render, redirect
from .models import City

from .forms import CityForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.

def index(request):
    city = City.objects.order_by('city')
    return render(request, 'main/index.html', {'city': city})


class CityDetailView(DetailView):
    model = City
    template_name = 'main/details_view.html'
    context_object_name = 'table_data'



class CityUpdateView(UpdateView):
    model = City
    template_name = 'main/add_city.html'

    form_class = CityForm


class CityDeleteView(DeleteView):
    model = City
    success_url = '/'
    template_name = 'main/city_delete.html'



def add_city(request):
    error = ''
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Wrong data, an example to entering data - 2023-07-25 15:45'

    form = CityForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/add_city.html', data)