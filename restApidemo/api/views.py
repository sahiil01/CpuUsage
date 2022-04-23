from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import CpuDataSerializer
from django.http import HttpResponse
from django.shortcuts import render
from .models import CpuData
import io


# Create your views here.
@csrf_exempt
def CpuDataApi(request):
    if request.method == "GET":
        # json_data = request.body
        # stream = io.ByteIo(json_data)
        # pythondata = JSONParser().parse(stream)

        cpuObject = CpuData.objects.all()
        serializer = CpuDataSerializer(cpuObject, many=True)
        json_data = JSONRenderer().render(serializer.data)

        return HttpResponse(json_data, content_type="application/json")

    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = CpuDataSerializer(data=pythondata)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            response = {"msg": "data uploaded"}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type="application/json")

        response = {"msg": "data not uploaded"}
        json_data = JSONRenderer().render(response)
        return HttpResponse(json_data, content_type="application/json")
