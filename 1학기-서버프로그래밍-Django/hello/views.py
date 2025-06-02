from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Hacsam
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import viewsets
from .serializers import HacsamSerializer


# Create your views here.
class StudentListView(ListView):
    model = Hacsam
    paginate_by = 6


class StudentCreateView(CreateView):
    model = Hacsam
    fields = ['name', 'birthday', 'stdnum', 'major', 'email']
    success_url = reverse_lazy('list')
    template_name = 'hello/hacsam_create.html'


class StudentDetailView(DetailView):
    model = Hacsam


class StudentUpdateView(UpdateView):
    model = Hacsam
    fields = ['name', 'birthday', 'stdnum', 'major', 'email']
    success_url = reverse_lazy('list')
    template_name_suffix = '_update'


class StudentDeleteView(DeleteView):
    model = Hacsam
    success_url = reverse_lazy('list')
    template_name = 'hello/hacsam_delete.html'


# API Model
@csrf_exempt
def ApiStudent_list(request):
    if request.method == 'GET':
        Hacsams = list(Hacsam.objects.values())
        return JsonResponse(Hacsams, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        Hacsams = Hacsam.objects.create(
            name=data.get('name'),
            birthday=data.get('birthday'),
            stdnum=data.get('stdnum'),
            major=data.get('major'),
            email=data.get('email')
        )
        return JsonResponse({'id': Hacsams.id, 'status': 'created'})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def ApiStudent_detail(request, Hacsam_id):
    try:
        hacsam = Hacsam.objects.get(id=Hacsam_id)
    except Hacsam.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)

    if request.method == 'GET':
        return JsonResponse({'id': hacsam.id, 'name': hacsam.name, 'birthday': hacsam.birthday,
                             'stdnum': hacsam.stdnum, 'major': hacsam.major, 'email': hacsam.email})

    elif request.method == 'PUT':
        data = json.loads(request.body)
        hacsam.name = data.get('name', hacsam.name)
        hacsam.birthday = data.get('birthday', hacsam.birthday)
        hacsam.stdnum = data.get('stdnum', hacsam.stdnum)
        hacsam.major = data.get('major', hacsam.major)
        hacsam.email = data.get('email', hacsam.email)
        hacsam.save()
        return JsonResponse({'status': 'updated'})

    elif request.method == 'DELETE':
        hacsam.delete()
        return JsonResponse({'status': 'deleted'})

    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])

# APIview 구현
class HacsamViewSet(viewsets.ModelViewSet):
    queryset = Hacsam.objects.all()
    serializer_class = HacsamSerializer
    permission_classes = [IsAuthenticated] # 인증된 사용자만 가능

    def perfrom_create(self, serializer):
        serializer.save(user=self.request.user) # 로그인한 유저 자동 연결
