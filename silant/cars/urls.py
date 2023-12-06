from django.urls import path

from .views import index, MachinesList, MachineDetail, MachineUpdate, MachineCreate, MachineDelete

urlpatterns = [
    path('', index, name='main_page'),
    path('cars/', MachinesList.as_view(), name='machine_list'),
    path('cars/create/', MachineCreate.as_view(), name='machine_create'),
    path('cars/<int:pk>/', MachineDetail.as_view(), name='machine_detail'),
    path('cars/<int:pk>/delete/', MachineDelete.as_view(), name='machine_delete'),
    path('cars/<int:pk>/update/', MachineUpdate.as_view(), name='machine_update'),
]