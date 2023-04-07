from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Message
import json


def home(request):
    user = request.user
    users = User.objects.exclude(id=user.id)
    messages = Message.objects.filter(recipient=user)
    return render(request, 'home.html', {'user': user, 'users': users, 'messages': messages})


@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        sender_id = request.user.id
        recipient_id = json.loads(request.body)['recipient']
        message_text = json.loads(request.body)['text']

        message = Message.objects.create(sender_id=sender_id, recipient_id=recipient_id, text=message_text)

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
