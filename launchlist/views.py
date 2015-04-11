from django.template import Context, Template
from django.http import HttpResponse

def view_root(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    content_mainPage = "This will be an awesome homepage soon."
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage}))
    return HttpResponse(html)

def view_intro(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    content_mainPage = "This will be the intro page."
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage}))
    return HttpResponse(html)

def view_mission(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    content_mainPage = "This will be the mission page."
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage}))
    return HttpResponse(html)

def view_spacecraft(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    content_mainPage = "This will be the spacecraft page."
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage}))
    return HttpResponse(html)

def view_launchVehicle(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    content_mainPage = "This will be the launch vehicle page."
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage}))
    return HttpResponse(html)

def view_summary(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    content_mainPage = "This will be the summary page."
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage}))
    return HttpResponse(html)