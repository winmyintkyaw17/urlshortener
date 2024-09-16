from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="home"),
    path('url/list', views.url_list, name="url_list"),
    path('url/<int:id>',views.sg_url, name="sg_url" )
]