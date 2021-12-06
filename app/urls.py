from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    path('yyygyg',views.ajax_search,name='ajax_search')
]