from django.shortcuts import render


def city(request):
    return render(request, 'city.html')


def district(request):
    return render(request, 'district.html')
