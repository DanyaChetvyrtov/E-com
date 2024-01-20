from django.urls import path
import myapp.views as views


app_name = "myapp"
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:correct_product_id>/", views.index_item, name="detail"),
    path("add_item/", views.add_item, name="add_item"),
    path("update_item/<int:correct_product_id>", views.update_item, name="update_item"),
    path("delete_item/<int:correct_product_id>", views.delete_item, name="delete_item"),
]
