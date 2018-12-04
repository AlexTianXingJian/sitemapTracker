from django.shortcuts import render


def displayTest(request):

    return render(request, 'testapp/apptest.html' )

