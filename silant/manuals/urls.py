from django.urls import path

from .views import get_manuals, TechnicalList, EngineList, TransmissionList, DrivingBridgeList, SteeredBridgeList, \
    MaintenanceList, NodeFailureList, MethodList, ServiceList, TechnicalDetail, TechnicalManualCreate, \
    TechnicalManualDelete, TechnicalManualUpdate, EngineDetail, EngineManualUpdate, EngineManualDelete, \
    EngineManualCreate, TransmissionManualCreate, TransmissionDetail, TransmissionManualDelete, \
    TransmissionManualUpdate, DrivingBridgeManualCreate, DrivingBridgeDetail, DrivingBridgeManualUpdate, \
    DrivingBridgeManualDelete, SteeredBridgeManualCreate, SteeredBridgeDetail, SteeredBridgeManualUpdate, \
    SteeredBridgeManualDelete, MaintenanceManualCreate, MaintenanceDetail, MaintenanceManualUpdate, \
    MaintenanceManualDelete, NodeFailureManualCreate, NodeFailureDetail, NodeFailureManualUpdate, \
    NodeFailureManualDelete, MethodManualCreate, MethodDetail, MethodManualUpdate, MethodManualDelete

urlpatterns = [
    path('', get_manuals, name='manuals'),
    path('technical/', TechnicalList.as_view(), name='manual_tech_list'),
    path('technical/create/', TechnicalManualCreate.as_view(), name='manual_tech_create'),
    path('technical/<int:pk>/', TechnicalDetail.as_view(), name='manual_tech_detail'),
    path('technical/<int:pk>/delete/', TechnicalManualDelete.as_view(), name='manual_tech_delete'),
    path('technical/<int:pk>/update/', TechnicalManualUpdate.as_view(), name='manual_tech_update'),
    path('engine/', EngineList.as_view(), name='manual_engine_list'),
    path('engine/create/', EngineManualCreate.as_view(), name='manual_engine_create'),
    path('engine/<int:pk>/', EngineDetail.as_view(), name='manual_engine_detail'),
    path('engine/<int:pk>/update/', EngineManualUpdate.as_view(), name='manual_engine_update'),
    path('engine/<int:pk>/delete/', EngineManualDelete.as_view(), name='manual_engine_delete'),
    path('transmission/', TransmissionList.as_view(), name='manual_transmission_list'),
    path('transmission/create/', TransmissionManualCreate.as_view(), name='manual_transmission_create'),
    path('transmission/<int:pk>/', TransmissionDetail.as_view(), name='manual_transmission_detail'),
    path('transmission/<int:pk>/update/', TransmissionManualUpdate.as_view(), name='manual_transmission_update'),
    path('transmission/<int:pk>/delete/', TransmissionManualDelete.as_view(), name='manual_transmission_delete'),
    path('driving_bridge/', DrivingBridgeList.as_view(), name='manual_driving_list'),
    path('driving_bridge/create/', DrivingBridgeManualCreate.as_view(), name='manual_driving_bridge_create'),
    path('driving_bridge/<int:pk>/', DrivingBridgeDetail.as_view(), name='manual_driving_bridge_detail'),
    path('driving_bridge/<int:pk>/update/', DrivingBridgeManualUpdate.as_view(), name='manual_driving_bridge_update'),
    path('driving_bridge/<int:pk>/delete/', DrivingBridgeManualDelete.as_view(), name='manual_driving_bridge_delete'),
    path('steered_bridge/', SteeredBridgeList.as_view(), name='manual_steered_list'),
    path('steered_bridge/create/', SteeredBridgeManualCreate.as_view(), name='manual_steered_bridge_create'),
    path('steered_bridge/<int:pk>/', SteeredBridgeDetail.as_view(), name='manual_steered_bridge_detail'),
    path('steered_bridge/<int:pk>/update/', SteeredBridgeManualUpdate.as_view(), name='manual_steered_bridge_update'),
    path('steered_bridge/<int:pk>/delete/', SteeredBridgeManualDelete.as_view(), name='manual_steered_bridge_delete'),
    path('maintenance/', MaintenanceList.as_view(), name='manual_maintenance_list'),
    path('maintenance/create/', MaintenanceManualCreate.as_view(), name='manual_maintenance_create'),
    path('maintenance/<int:pk>/', MaintenanceDetail.as_view(), name='manual_maintenance_detail'),
    path('maintenance/<int:pk>/update/', MaintenanceManualUpdate.as_view(), name='manual_maintenance_update'),
    path('maintenance/<int:pk>/delete/', MaintenanceManualDelete.as_view(), name='manual_maintenance_delete'),
    path('node_failure/', NodeFailureList.as_view(), name='manual_failure_list'),
    path('node_failure/create/', NodeFailureManualCreate.as_view(), name='manual_node_failure_create'),
    path('node_failure/<int:pk>/', NodeFailureDetail.as_view(), name='manual_node_failure_detail'),
    path('node_failure/<int:pk>/update/', NodeFailureManualUpdate.as_view(), name='manual_node_failure_update'),
    path('node_failure/<int:pk>/delete/', NodeFailureManualDelete.as_view(), name='manual_node_failure_delete'),
    path('recovery_method/', MethodList.as_view(), name='manual_recovery_list'),
    path('recovery_method/create/', MethodManualCreate.as_view(), name='manual_recovery_method_create'),
    path('recovery_method/<int:pk>/', MethodDetail.as_view(), name='manual_recovery_method_detail'),
    path('recovery_method/<int:pk>/update/', MethodManualUpdate.as_view(), name='manual_recovery_method_update'),
    path('recovery_method/<int:pk>/delete/', MethodManualDelete.as_view(), name='manual_recovery_method_delete'),

]