from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm


def index(request):
    return render(request, "adminapp/index.html")


# READ
def admin_users(request):
    context = {"users": User.objects.all()}
    return render(request, "adminapp/admin-users-read.html", context)


# CREATE
def admin_users_create(request):
    if request.method == "POST":
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admin_staff:admin_users"))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {"form": form}
    return render(request, "adminapp/admin-users-create.html", context)


# UPDATE
def admin_users_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Данные успешно сохраненны!")
            return HttpResponseRedirect(reverse("admin_staff:admin_users"))
        else:
            print(form.errors)
    else:
        form = UserAdminProfileForm(instance=user)
    context = {"form": form, "user": user}
    return render(request, "adminapp/admin-users-update-delete.html", context)


# DELETE
def admin_users_delete(request):
    pass
