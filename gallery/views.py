# Create your views here.
import os
from django.core.context_processors import request  
from django.shortcuts import render_to_response  
from django.template.context import Context, RequestContext  

def home(request):
    c = Context({
                 "WHO": "WORLD!!!",
                 "IMG": os.listdir('/Users/vanzhiganov/Sites/pyGallery/videocam')
    })
    return render_to_response("home.html", c, context_instance=RequestContext(request))
