from django.urls import path

from adminapp.views import (index, admin_users, admin_users_create, admin_users_update, admin_users_delete)
from adminapp.views import (admin_products, admin_products_create, admin_products_update, admin_products_delete)
from adminapp.views import (admin_categories, admin_categories_create, admin_categories_update, admin_categories_delete)

app_name = 'adminapp'

urlpatterns = [
    path("", index, name="index"),
    path("users/", admin_users, name="admin_users"),
    path("users-create/", admin_users_create, name="admin_users_create"),
    path("users-update/<int:user_id>/", admin_users_update, name="admin_users_update"),
    path("users-delete/<int:user_id>/", admin_users_delete, name="admin_users_delete"),
    path("products/", admin_products, name="admin_products"),
    path("products-create/", admin_products_create, name="admin_products_create"),
    path("products-update/<int:product_id>/", admin_products_update, name="admin_products_update"),
    path("products-delete/<int:product_id>/", admin_products_delete, name="admin_products_delete"),
    path("categories/", admin_categories, name="admin_categories"),
    path("categories-create/", admin_categories_create, name="admin_categories_create"),
    path("categories-update/<int:category_id>/", admin_categories_update, name="admin_categories_update"),
    path("categories-delete/<int:category_id>/", admin_categories_delete, name="admin_categories_delete"),
]
