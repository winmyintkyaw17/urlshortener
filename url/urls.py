from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="home"),
    path('<str:hash_code>', views.url_short, name ="url_short"),
    path('url/list', views.url_list, name="url_list"),
    path('url/update/<int:id>',views.update_url, name="update_url" ),
    path('url/delete/<int:id>',views.delete_url, name="delete_url")
]