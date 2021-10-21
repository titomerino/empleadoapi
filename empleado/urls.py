from django.urls import path
from .views import EmpleadoCrear, EmpleadoList, EmpleadoDetail

urlpatterns = [
     path('empleado/', EmpleadoList.as_view(), name="empleado_list"),
     path('empleado/<int:pk>', EmpleadoDetail.as_view(), name="empleado_detail"),
     path('empleado/crear', EmpleadoCrear.as_view(), name="empleado_crear"),
]
