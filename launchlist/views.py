from django.http import HttpResponse

def view_root(request):
    return HttpResponse("This will be an awesome homepage soon.")

def view_intro(request):
    return HttpResponse("This will be the intro page.")

def view_mission(request):
    return HttpResponse("This will be the mission page.")

def view_spacecraft(request):
    return HttpResponse("This will be the spacecraft page.")

def view_launchVehicle(request):
    return HttpResponse("This will be the launch vehicle page.")

def view_summary(request):
    return HttpResponse("This will be the summary page.")