from django.shortcuts import render
from .models import Empleado
from django.views import View
from django.http import JsonResponse
from django.forms.models import model_to_dict


# Create your views here.
class EmpleadoList(View):
    def get(self, request):
        empleado_list = Empleado.objects.all()
        return JsonResponse(list(empleado_list.values()), safe=False)


class EmpleadoDetail(View):
    def get(self, request, pk):
        if pk:
            empleado = Empleado.objects.get(id=pk)
            if empleado:
                return JsonResponse(model_to_dict(empleado))
            else:
                return JsonResponse({"message": "El Empleado no existe."})
        else:
            return JsonResponse({"message": "Parametro incorrecto."})


class EmpleadoCrear(View):
    def post(self, request):
        nuevo_empleado = Empleado.create(
            nombre=request.POST.get("nombre"),
            apellido=request.POST.get("apellido"),
            tipo_documento=int(request.POST.get("tipo_documento")),
            documento=request.POST.get("documento"),
            area=int(request.POST.get("area")),
        )
        nuevo_empleado.save()

        return JsonResponse({"message": "Empleado creado"})
