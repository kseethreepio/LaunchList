from django.utils.safestring import mark_safe
from django.template import Context, Template
from django.http import HttpResponse

def view_root(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    fMainContent = open('launchlist/content_intro.html')
    content_mainPage = mark_safe(fMainContent.read())
    
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
    
    fMainContent = open('launchlist/content_mission.html')
    content_mainPage = mark_safe(fMainContent.read())
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage}))
    return HttpResponse(html)

def view_spacecraft(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    fMainContent = open('launchlist/content_spacecraft.html')
    content_mainPage = mark_safe(fMainContent.read())
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage}))
    return HttpResponse(html)

def view_launchVehicle(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    fMainContent = open('launchlist/content_launchVehicle.html')
    content_mainPage = mark_safe(fMainContent.read())
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage}))
    return HttpResponse(html)

def view_summary(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    fMainContent = open('launchlist/content_summary.html')
    content_mainPage = mark_safe(fMainContent.read())
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage}))
    return HttpResponse(html)