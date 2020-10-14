from django.contrib import admin
from django.urls import path
from . import views

app_name = 'todo_list'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', views.home, name='home'),
    path('delete/<list_id>', views.delete, name="delete"),
    path('cross_off/<list_id>', views.cross_off, name="cross_off"),
    path('uncross/<list_id>', views.uncross, name="uncross"),
    path('edit/<list_id>', views.edit, name="edit"),
]
