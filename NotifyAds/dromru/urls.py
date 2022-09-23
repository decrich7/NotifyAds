from django.urls import path

from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('filters/', filters, name='filters'),
    path('new_filter/', new_filter, name='new_filter'),
    path('delete_filter/<int:filter_id>', delete_filter, name='delete_filter'),
    path('stop_filter/<int:filter_id>', stop_filter, name='stop_filter'),
    path('change_filter/<int:filter_id>', change_filter, name='change_filter'),
    path('start_filter/<int:filter_id>', start_filter, name='start_filter')

]


# handler404 = 'views.asd'