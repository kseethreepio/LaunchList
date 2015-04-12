from django.utils.safestring import mark_safe
from django.template import Context, Template, RequestContext
from django.template.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import * 
from launchlist.models import *
from launchlist.itemdict import *

buttonDict = {
    'root': [["next", "/mission/"], ["back", None], ],
    'intro': [["next", "/mission/"], ["back", None]],
    'mission': [["next", "/spacecraft/"], ["back", "/intro/"]],
    'spacecraft': [["next", "/vehicle/"], ["back", "/mission/"]],
    'vehicle': [["next", "/summary/"],["back", "/spacecraft/"]],
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
        return html, None
    elif (buttonsOnCurrentPage[0][1] == None):
        # If there's no 'next' page, create a back button and start over button
        ending_page = True
        html = tButtonView.render(Context({'ending_page': ending_page, 'backURL': buttonsOnCurrentPage[1][1]}))
        return html, None
    else:
        # Otherwise, create both a back and next button
        regular_page = True        
        html = tButtonView.render(Context({'regular_page': regular_page, 'backURL': buttonsOnCurrentPage[1][1], 'nextURL': buttonsOnCurrentPage[0][1]}))
        return html, buttonsOnCurrentPage[0][1]
    
    # return html

# TODO: Deprecated... remove this view
# def view_root(request):
#     fDefaultPageTemplate = open('launchlist/defaultPage.html')
#     tCurrentView = Template(fDefaultPageTemplate.read())
#     fDefaultPageTemplate.close()
#
#     fMainContent = open('launchlist/content_intro.html')
#     content_mainPage = mark_safe(fMainContent.read())
#
#     navButtons = create_nav_buttons("root")
#
#     html = tCurrentView.render(Context({'content_mainPage': content_mainPage, 'navButtons': navButtons}))
#     return HttpResponse(html)

def view_intro(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    fMainContent = open('launchlist/content_intro.html')
    content_mainPage = mark_safe(fMainContent.read())
    
    navButtons = create_nav_buttons("intro")
    
    # Initializing session vars to default values
    request.session['missiontarget'] = "Not selected"
    request.session['spacecraft'] = "Not selected"
    request.session['launchvehicle'] = "Not selected"
    
    html = tCurrentView.render(Context({'content_mainPage': content_mainPage, 'navButtons': navButtons[0]}))
    return HttpResponse(html)

def view_mission(request):
    fDefaultPageTemplate = open('launchlist/defaultForm.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()

    fMainContent = open('launchlist/content_mission.html')
    content_mainPage = mark_safe(fMainContent.read())

    navButtons = create_nav_buttons("mission")

    html = tCurrentView.render(RequestContext(request, {'content_mainPage': content_mainPage,'form_name': "mission", 'navButtons': navButtons[0]}))
    # html = tCurrentView.render(Context({'content_mainPage': content_mainPage, 'form_name': "mission", 'navButtons': navButtons}))
    return HttpResponse(html)

def view_spacecraft(request):
    fDefaultPageTemplate = open('launchlist/defaultForm.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    fMainContent = open('launchlist/content_spacecraft.html')
    content_mainPage = mark_safe(fMainContent.read())

    navButtons = create_nav_buttons("spacecraft")
    
    html = tCurrentView.render(RequestContext(request, {'content_mainPage': content_mainPage, 'form_name': "spacecraft", 'navButtons': navButtons[0]}))
    return HttpResponse(html)

def view_launchVehicle(request):
    fDefaultPageTemplate = open('launchlist/defaultForm.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    fMainContent = open('launchlist/content_launchVehicle.html')
    content_mainPage = mark_safe(fMainContent.read())

    navButtons = create_nav_buttons("vehicle")
    
    html = tCurrentView.render(RequestContext(request, {'content_mainPage': content_mainPage, 'form_name': "lv", 'navButtons': navButtons[0]}))
    return HttpResponse(html)

def view_summary(request):
    selection_mission = request.session['missiontarget']
    selection_mission = selection_mission.replace("'","")
    selection_spacecraft = request.session['spacecraft']
    selection_spacecraft = selection_spacecraft.replace("'","")
    selection_launchvehicle = request.session['launchVehicle']
    selection_launchvehicle = selection_launchvehicle.replace("'","")

    fDefaultPageTemplate = open('launchlist/defaultSummary.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()
    
    navButtons = create_nav_buttons("summary")
    
    templateLoadParams = {
        'navButtons': navButtons[0],
        'selection_missionTarget': selection_mission.replace("mission","Mission #"),   # Make the summary text a little nicer,
        'selection_spacecraft': selection_spacecraft.replace("spacecraft","Spacecraft #"),
        'selection_lv': selection_launchvehicle.replace("lv","Launch Vehicle #"),
        'selected_missionScience': dict_missions[selection_mission]['science'],
        'selected_missionDeltaV': dict_missions[selection_mission]['deltaV'],
        'selected_spacecraftScience': dict_spacecraft[selection_spacecraft]['science'],
        'selected_spacecraftCost': dict_spacecraft[selection_spacecraft]['cost'],
        'selected_spacecraftMass': dict_spacecraft[selection_spacecraft]['mass'],
        'selected_spacecraftBT': dict_spacecraft[selection_spacecraft]['buildtime'],
        'selected_lvCost': dict_launchvehicles[selection_launchvehicle]['cost'],
        'selected_lvGTO': dict_launchvehicles[selection_launchvehicle]['gto']
    }
    
    html = tCurrentView.render(RequestContext(request, templateLoadParams))
    return HttpResponse(html)

def view_test(request):
    fDefaultPageTemplate = open('launchlist/defaultPage.html')
    tCurrentView = Template(fDefaultPageTemplate.read())
    fDefaultPageTemplate.close()

    # Sessions testing
    # content_mainPage = request.session['foo']

    # DB testing
    # content_mainPage = "This is text."
    # missionFoo = missiontarget(name_missiontarget="Name", desc_missiontarget="Target", stat_m_size=9, stat_m_deltav=1.25, stat_m_sciencescore=8)
    # missionFoo.save()
    # allStuff = missiontarget.objects.all()

    html = tCurrentView.render(Context({'content_mainPage': content_mainPage}))
    return HttpResponse(html)
    
def recordInput(request):
    try:
        if 'mission' in request.POST:
            request.session['missiontarget'] = "%r" % request.POST['mission']
            nextPage = '/spacecraft/'
        elif 'spacecraft' in request.POST:
            request.session['spacecraft'] = "%r" % request.POST['spacecraft']
            nextPage = '/vehicle/'
        elif 'launchVehicle' in request.POST:
            request.session['launchVehicle'] = "%r" % request.POST['launchVehicle']
            nextPage = '/summary/'
        return redirect(nextPage)
    
    except UnboundLocalError:
        return HttpResponse("Please click the 'Back' button in your browser and make a selection on the previous page.")
    
    # message = "Mission target is: %s<br />" % request.session['missiontarget']
    # message += "Spacecraft is: %s<br />" % request.session['spacecraft']
    # message += "Launch vehicle is: %s<br />" % request.session['launchvehicle']
    # message += "<br />Done processing."
    #
    # return HttpResponse(message)