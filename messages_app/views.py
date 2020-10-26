from django.shortcuts import render, redirect, HttpResponse
from messages_app.models import *

# Create your views here.
def index(request):
    context = {
        'messages': Messages.objects.all(),
        
    }
    return render(request, 'messages.html', context)

def post_message(request):
    Messages.objects.create(message=request.POST['message'], user=Users.objects.get(id=request.session['user_id']))
    return redirect('/wall')

def post_comment(request):
    Comments.objects.create(comment=request.POST['comment'], user=Users.objects.get(id=request.session['user_id']), message=Messages.objects.get(id=request.POST['message_id']))
    
    return redirect('/wall')