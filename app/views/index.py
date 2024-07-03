from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpRequest
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.contrib import messages
from globals.decorators import tenant_config


class IndexView (View) : 
    
    @tenant_config
    def get(self, request:HttpRequest, **kwargs) : 
        
        if not kwargs['has_tenant'] :
            return render(request, 'index.html')

        tenant_name = kwargs['tenant']['name']
        action = Action(
            url=MAIN_URL + f'/host/get/{tenant_name}/{request.path[1::]}'
        )
        action.get()

        if not action.is_valid:
            return render(request,'404.html')
        
        body = action.req.content
        
        # NOTE: this only read html and css files.
        if "<!DOCTYPE html>" in str(body).split('\n')[0] :
            response = HttpResponse(
                content=body,
                content_type='text/html'
            )
        else:
            response = HttpResponse(
                content=body,
                content_type='text/css'
            )
        
        return response