from django.urls import path

from .views import index, MachinesList, MachineDetail, MachineUpdate, MachineCreate, MachineDelete, MaintenanceList, \
    MaintenanceCreate, MaintenanceDetail, MaintenanceUpdate, MaintenanceDelete

urlpatterns = [
    path('', index, name='main_page'),
    path('cars/', MachinesList.as_view(), name='machine_list'),
    path('cars/create/', MachineCreate.as_view(), name='machine_create'),
    path('cars/<int:pk>/', MachineDetail.as_view(), name='machine_detail'),
    path('cars/<int:pk>/delete/', MachineDelete.as_view(), name='machine_delete'),
    path('cars/<int:pk>/update/', MachineUpdate.as_view(), name='machine_update'),
    path('maintenances/', MaintenanceList.as_view(), name='maintenances_list'),
    path('maintenances/create/', MaintenanceCreate.as_view(), name='maintenance_create'),
    path('maintenances/<int:pk>/', MaintenanceDetail.as_view(), name='maintenance_detail'),
    path('maintenances/<int:pk>/update/', MaintenanceUpdate.as_view(), name='maintenance_update'),
    path('maintenances/<int:pk>/delete/', MaintenanceDelete.as_view(), name='maintenance_delete'),

]