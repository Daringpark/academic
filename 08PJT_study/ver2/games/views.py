from django.shortcuts import render
from .models import GameSession
import random as rd


# Create your views here.
def index(request):
    # 1. session creation
    # 2. pk 저장
    # 3. render
    target_number = rd.randint(1, 100)
    game_session = GameSession.objects.create(target_number = target_number)
    context = {
        'session_pk' : game_session.pk,
        'user_guess_number' : game_session.user_guess_number,
        'target_number' : game_session.target_number,
        
    }
    return render(request, 'games/index.html', context)


# METHOD POST -> response, redirect
from django.http import JsonResponse
def guess(request, session_pk):
    now_session = GameSession.objects.get(pk = session_pk)
    user_guess = int(request.POST.get('userGuess'))


    if user_guess < 1 or user_guess > 100:
        message = '1에서 100까지의 수를 입력해주세요.'
    elif user_guess > now_session.target_number:
        message = '큰 수입니다! 더 작은 수를 입력하세요!'
        now_session.counting_trial += 1
        now_session.user_guess_number = user_guess
        now_session.save()
    elif user_guess < now_session.target_number:
        message = '작은 수입니다! 더 큰 수를 입력하세요!'
        now_session.counting_trial += 1
        now_session.user_guess_number = user_guess
        now_session.save()
    elif user_guess == now_session.target_number:
        message = '정답입니다!!'

    context = {
        'message': message,
        'attempts': now_session.counting_trial,
        'is_correct' : user_guess == now_session.target_number
    }
    
    return JsonResponse(context)