from django.urls import path

from .views import index

urlpatterns = [
    path('', index, name='main_page'),
    # path('', MachineListList.as_view(), name='machine_list'),
]