from django.shortcuts import render
from .forms import CarForm
from .models import CarModel


# Create your views here.
def index(request):

    # TO VALIDATE DATA AND SAVE IF VALID/ REDO IF NOT
    if(request.method == "POST"):
        carform = CarForm(request.POST)

        if(carform.is_valid()):
            CarModel.objects.create(make=request.POST['make'], model=request.POST['model'], year =request.POST['year'], mpg =request.POST['mpg'])
        else:
            print(carform.errors)
            zoomZoom = CarModel.objects.all()
            context= {
                "errors":carform.errors,
                "zoomZoom":zoomZoom,
                "carform": CarForm(),
        }
            return render(request, "carApp/index.html", context)

    # TO PRINT OBJECTS IN MODEL
    zoomZoom = CarModel.objects.all()
    carform = CarForm()
    context = {
        'zoomZoom': zoomZoom,
        'carform': carform,
    }
    return render(request, "carApp/index.html", context)


# TO OPEN CONGRATS PAGE
def congrats(request):
    return render(request, "carApp/congrats.html")
