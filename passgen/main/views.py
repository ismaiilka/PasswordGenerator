from django.shortcuts import render
from random import choice, randrange

LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SPECIAL = '!@#$%^&*'


def index(request):
    return render(request, 'main/index.html', {'request': request})


def password(request):
    result = ""
    alphabet = LOWERCASE
    nums = int(request.GET.get('min_numbers'))
    special = int(request.GET.get('min_special'))
    length = int(request.GET.get('length'))
    if special + nums > length:
        return render(request, 'main/password.html', {'result': 'Задайте корректно входные данные'})
    if not request.GET.get('numbers') and nums > 0:
        return render(request, 'main/password.html', {'result': 'Задайте корректно входные данные'})
    if not request.GET.get('special') and special > 0:
        return render(request, 'main/password.html', {'result': 'Задайте корректно входные данные'})
    if request.GET.get('uppercase'):
        alphabet += UPPERCASE
    if request.GET.get('numbers'):
        alphabet += NUMBERS
    if request.GET.get('special'):
        alphabet += SPECIAL
    for _ in range(length):
        result += choice(alphabet)
    used = []
    for _ in range(nums):
        while (rand_n := randrange(length)) in used:
            rand_n = randrange(length)
        used.append(rand_n)
        result = result[:rand_n] + choice(NUMBERS) + result[rand_n + 1:]
    for _ in range(special):
        while (rand_n := randrange(length)) in used:
            rand_n = randrange(length)
        used.append(rand_n)
        result = result[:rand_n] + choice(SPECIAL) + result[rand_n + 1:]
    return render(request, 'main/password.html', {'result': result})