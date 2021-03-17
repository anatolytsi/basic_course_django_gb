from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from mainapp.models import Product, ProductCategory
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductAdminForm, ProductCategoryAdminForm


@user_passes_test(lambda u: u.is_superuser, login_url="/")
def index(request):
    return render(request, "adminapp/index.html")


# READ
@user_passes_test(lambda u: u.is_superuser, login_url="/")
def admin_users(request):
    context = {"users": User.objects.all()}
    return render(request, "adminapp/admin-users-read.html", context)


# CREATE
@user_passes_test(lambda u: u.is_superuser, login_url="/")
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
@user_passes_test(lambda u: u.is_superuser, login_url="/")
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
@user_passes_test(lambda u: u.is_superuser, login_url="/")
def admin_users_delete(request, user_id):
    user = User.objects.get(id=user_id)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse("admin_staff:admin_users"))


# READ
@user_passes_test(lambda u: u.is_superuser, login_url="/")
def admin_products(request):
    context = {"products": Product.objects.all()}
    return render(request, "adminapp/admin-products-read.html", context)


# CREATE
@user_passes_test(lambda u: u.is_superuser, login_url="/")
def admin_products_create(request):
    if request.method == "POST":
        form = ProductAdminForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admin_staff:admin_products"))
        else:
            print(form.errors)
    else:
        form = ProductAdminForm()
    context = {"form": form}
    return render(request, "adminapp/admin-products-create.html", context)


# UPDATE
@user_passes_test(lambda u: u.is_superuser, login_url="/")
def admin_products_update(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        form = ProductAdminForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Данные успешно сохраненны!")
            return HttpResponseRedirect(reverse("admin_staff:admin_products"))
        else:
            print(form.errors)
    else:
        form = ProductAdminForm(instance=product)
    context = {"form": form, "product": product}
    return render(request, "adminapp/admin-products-update-delete.html", context)


# DELETE
@user_passes_test(lambda u: u.is_superuser, login_url="/")
def admin_products_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect(reverse("admin_staff:admin_products"))


# READ
@user_passes_test(lambda u: u.is_superuser, login_url="/")
def admin_categories(request):
    context = {"categories": ProductCategory.objects.all()}
    return render(request, "adminapp/admin-categories-read.html", context)


# CREATE
@user_passes_test(lambda u: u.is_superuser, login_url="/")
def admin_categories_create(request):
    if request.method == "POST":
        form = ProductCategoryAdminForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admin_staff:admin_categories"))
        else:
            print(form.errors)
    else:
        form = ProductCategoryAdminForm()
    context = {"form": form}
    return render(request, "adminapp/admin-categories-create.html", context)


# UPDATE
@user_passes_test(lambda u: u.is_superuser, login_url="/")
def admin_categories_update(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    if request.method == "POST":
        form = ProductCategoryAdminForm(data=request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Данные успешно сохраненны!")
            return HttpResponseRedirect(reverse("admin_staff:admin_categories"))
        else:
            print(form.errors)
    else:
        form = ProductCategoryAdminForm(instance=category)
    context = {"form": form, "category": category}
    return render(request, "adminapp/admin-categories-update-delete.html", context)


# DELETE
@user_passes_test(lambda u: u.is_superuser, login_url="/")
def admin_categories_delete(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    category.delete()
    return HttpResponseRedirect(reverse("admin_staff:admin_categories"))
