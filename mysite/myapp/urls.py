from django.urls import path
import myapp.views as views


app_name = "myapp"
urlpatterns = [
    path("", views.index),
    path("<int:correct_product_id>/", views.index_item, name="detail"),
]
