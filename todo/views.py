from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ToBeDone


def main(request):

    still_to_do = ToBeDone.objects.all()

    return render(request, 'main.html', {'all': still_to_do})


def add(request):
    if request.method == "POST":
        to_doo = request.POST["todo"]
        if len(to_doo) > 0:
            a = ToBeDone(to_do=to_doo)
            a.save()
            return redirect("/")
        else:
            messages.info(request, "Invalid Entry")
            return redirect("/")

    else:
        return redirect("/")


def delete_todo(request, i):
    ToBeDone.objects.filter(to_do=i).delete()
    return redirect("/")