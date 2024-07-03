from django.views import View
from django.shortcuts import render, redirect
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.contrib import messages
from globals.decorators import login_required

class ProfileView (View) : 
    
    @login_required
    def get(self, request, **kwargs) : 

        close_site = request.GET.get('close_site', None)
        open_site = request.GET.get('active_site', None)

        if close_site:
            action = Action(
                url=MAIN_URL + f'/host/inactive/{close_site}/',
                headers=kwargs['headers']
            )
            action.patch()
            return redirect('profile')
        
        if open_site :
            action = Action(
                url=MAIN_URL + f'/host/active/{open_site}/',
                headers=kwargs['headers']
            )
            action.patch()
            return redirect('profile')

        action = Action(
            url = MAIN_URL + '/host/get/',
            headers=kwargs['headers']
        )
        action.get()
        respones = action.json_data()

        context = {
            'sites' : respones
        }
        return render(request,'profile.html', context)
        
    

    @login_required
    def post (self, request, **kwargs) : 
        data = {
            'name' : request.POST.get('name',None),
        }
        files = {
            'file' : request.FILES.get('file', None)
        }
        action = Action(
            url=MAIN_URL + '/host/create/',
            headers=kwargs['headers'],
            data=data
        )
        action.files = files

        action.post()

        if not action.is_valid:
            print(action.json_data())
            messages.error(request,'an error accoured')
        else:
            messages.success(request,'your site has been hosting successfully')

        return redirect('profile')