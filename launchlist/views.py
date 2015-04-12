from django.utils.safestring import mark_safe
from django.template import Context, Template
from django.http import HttpResponse

buttonDict = {
    'root': [["next", "/mission/"], ["back", None]],
    'intro': [["next", "/mission/"], ["back", None]],
    'mission': [["next", "/spacecraft/"], ["back", "/intro/"]],
    'spacecraft': [["next", "/vehicle/"], ["back", "/mission/"]],
    'vehicle': [["next", "/summary/"],["back", "/spacecraft"]],
    'summary': [["next", None], ["back", "/vehicle/"]]
}

def create_nav_buttons(pageName):
    # Make sure nothing left over from previous call
    starting_page = False
    ending_page = False
    regular_page = True
    
    buttonsOnCurrentPage = buttonDict[pageName]

    fButtonTemplate = open('launchlist/buttonTemplate.html')
    tButtonView = Template(fButtonTemplate.read())
    fButtonTemplate.close()
    
    # Get the URL for the 'back' button (first in the dict value entry)
    if (buttonsOnCurrentPage[1][1] == None):
        # If there's no 'back' button, create a 'start' button
        starting_page = True        
        html = tButtonView.render(Context({'starting_page': starting_page, 'nextURL': buttonsOnCurrentPage[0][1]}))
    elif (buttonsOnCurrentPage[0][1] == None):
        # If there's no 'next' page, create a back button and start over button
        ending_page = True
        html = tButtonView.render(Context({'ending_page': ending_page, 'backURL': buttonsOnCurrentPage[1][1]}))
    else:
        # Otherwise, create both a back and next button
        regular_page = True        
        html = tButtonView.render(Context({'regular_page': regular_page, 'backURL': buttonsOnCurrentPage[1][1], 'nextURL': buttonsOnCurrentPage[0][1]}))
    
    return html

def view_root(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    fMainContent = open('launchlist/content_intro.html')
    content_mainPage = mark_safe(fMainContent.read())
    
    navButtons = create_nav_buttons("root")
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage, 'navButtons': navButtons}))
    return HttpResponse(html)

def view_intro(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    fMainContent = open('launchlist/content_intro.html')
    content_mainPage = mark_safe(fMainContent.read())
    
    navButtons = create_nav_buttons("intro")
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage, 'navButtons': navButtons}))
    return HttpResponse(html)

def view_mission(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    fMainContent = open('launchlist/content_mission.html')
    content_mainPage = mark_safe(fMainContent.read())
    
    navButtons = create_nav_buttons("mission")
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage, 'navButtons': navButtons}))
    return HttpResponse(html)

def view_spacecraft(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    fMainContent = open('launchlist/content_spacecraft.html')
    content_mainPage = mark_safe(fMainContent.read())

    navButtons = create_nav_buttons("spacecraft")
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage, 'navButtons': navButtons}))
    return HttpResponse(html)

def view_launchVehicle(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    fMainContent = open('launchlist/content_launchVehicle.html')
    content_mainPage = mark_safe(fMainContent.read())

    navButtons = create_nav_buttons("vehicle")
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage, 'navButtons': navButtons}))
    return HttpResponse(html)

def view_summary(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    fMainContent = open('launchlist/content_summary.html')
    content_mainPage = mark_safe(fMainContent.read())
    
    navButtons = create_nav_buttons("summary")
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage, 'navButtons': navButtons}))
    return HttpResponse(html)