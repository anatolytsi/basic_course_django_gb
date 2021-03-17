from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from authapp.models import User
from mainapp.models import Product, ProductCategory
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductAdminForm, ProductCategoryAdminForm


@user_passes_test(lambda u: u.is_superuser, login_url="/")
def index(request):
    return render(request, "adminapp/index.html")


# READ
class UserListView(ListView):
    model = User
    template_name = "adminapp/admin-users-read.html"

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url="/"))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# CREATE
class UserCreateView(CreateView):
    model = User
    template_name = "adminapp/admin-users-create.html"
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy("admin_staff:admin_users")

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url="/"))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


# UPDATE
class UserUpdateView(UpdateView):
    model = User
    template_name = "adminapp/admin-users-update-delete.html"
    form_class = UserAdminProfileForm
    success_url = reverse_lazy("admin_staff:admin_users")

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data()
        context["title"] = "GeekShop - Редактирование пользователя"
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url="/"))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


# DELETE
class UserDeleteView(DeleteView):
    model = User
    template_name = "adminapp/admin-users-update-delete.html"
    success_url = reverse_lazy("admin_staff:admin_users")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url="/"))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)


# READ
class ProductListView(ListView):
    model = Product
    template_name = "adminapp/admin-products-read.html"

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url="/"))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)


# CREATE
class ProductCreateView(CreateView):
    model = Product
    template_name = "adminapp/admin-products-create.html"
    form_class = ProductAdminForm
    success_url = reverse_lazy("admin_staff:admin_products")

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url="/"))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreateView, self).dispatch(request, *args, **kwargs)


# UPDATE
class ProductUpdateView(UpdateView):
    model = Product
    template_name = "adminapp/admin-products-update-delete.html"
    form_class = ProductAdminForm
    success_url = reverse_lazy("admin_staff:admin_products")

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data()
        context["title"] = "GeekShop - Редактирование товара"
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url="/"))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)


# DELETE
class ProductDeleteView(DeleteView):
    model = Product
    template_name = "adminapp/admin-products-update-delete.html"
    success_url = reverse_lazy("admin_staff:admin_products")

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url="/"))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)


# # READ
# @user_passes_test(lambda u: u.is_superuser, login_url="/")
# def admin_products(request):
#     context = {"products": Product.objects.all()}
#     return render(request, "adminapp/admin-products-read.html", context)
#
#
# # CREATE
# @user_passes_test(lambda u: u.is_superuser, login_url="/")
# def admin_products_create(request):
#     if request.method == "POST":
#         form = ProductAdminForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("admin_staff:admin_products"))
#         else:
#             print(form.errors)
#     else:
#         form = ProductAdminForm()
#     context = {"form": form}
#     return render(request, "adminapp/admin-products-create.html", context)
#
#
# # UPDATE
# @user_passes_test(lambda u: u.is_superuser, login_url="/")
# def admin_products_update(request, product_id):
#     product = Product.objects.get(id=product_id)
#     if request.method == "POST":
#         form = ProductAdminForm(data=request.POST, files=request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Данные успешно сохраненны!")
#             return HttpResponseRedirect(reverse("admin_staff:admin_products"))
#         else:
#             print(form.errors)
#     else:
#         form = ProductAdminForm(instance=product)
#     context = {"form": form, "product": product}
#     return render(request, "adminapp/admin-products-update-delete.html", context)
#
#
# # DELETE
# @user_passes_test(lambda u: u.is_superuser, login_url="/")
# def admin_products_delete(request, product_id):
#     product = Product.objects.get(id=product_id)
#     product.delete()
#     return HttpResponseRedirect(reverse("admin_staff:admin_products"))


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
