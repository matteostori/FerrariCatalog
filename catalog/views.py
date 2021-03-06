from os import listdir
from os.path import join

from django.shortcuts import render
from django.views import generic

from FerrariCatalog.settings import BASE_DIR, STATIC_URL

from .models import Car, Pilot


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_cars = Car.objects.all().count()
    num_pilots = Pilot.objects.all().count()

    num_cars_y= Car.objects.filter(color__exact='yl').count()
    num_cars_r= Car.objects.filter(color__exact='rd').count()
    num_cars_b= Car.objects.filter(color__exact='bk').count()
    num_cars_bl= Car.objects.filter(color__exact='bl').count()

    context = {
        'num_cars': num_cars,
        'num_pilots': num_pilots,
        'num_cars_y': num_cars_y,
        'num_cars_r': num_cars_r,
        'num_cars_b': num_cars_b,
        'num_cars_bl': num_cars_bl,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

#about page
def about(request):
    return render(request, 'about.html')

#simple view for listing all cars (paginated)
class CarsListView(generic.ListView):
    paginate_by = 8
    model = Car

#detailed view of each car
class CarsDetailView(generic.DetailView):
    model = Car
    
    def get_context_data(self, **kwargs):
        context = super(CarsDetailView, self).get_context_data(**kwargs)
        images_list = []
        carimage_set = context['object'].carimage_set.all()
        if len(carimage_set) > 0:
            imagepath = carimage_set[0].path
            imagepath_dir = join(BASE_DIR, 'catalog/') + STATIC_URL + '/img/' + imagepath
            for f in listdir(imagepath_dir):
                images_list.append('img/' + imagepath + '/' + f)
             
            context['image_list'] = images_list
            
        return context
        
    
#simple view for listing all pilots (paginated)
class PilotListView(generic.ListView):
    paginate_by = 8
    model = Pilot

#detailed view of each pilot
class PilotsDetailView(generic.DetailView):
    model = Pilot