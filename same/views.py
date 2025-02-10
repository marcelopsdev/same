from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from apps.same.models import ArquivamentoSame
from apps.same.forms import SameFormCreate, SameUpadateForm
from django.contrib.auth.models import User
from apps.states_and_cities.models import City


class SamaList(ListView):
    model = ArquivamentoSame

    def get_context_data(self, **kwargs):
        context = super(SamaList, self).get_context_data(**kwargs)
        search_same = self.request.GET.get('search_same')        
        if self.request.method == 'GET':
            if search_same != None:
                if search_same.rfind('1') or search_same.rfind('2') or search_same.rfind('3') or search_same.rfind('4') or search_same.rfind('5') or search_same.rfind('6') or search_same.rfind('7') or search_same.rfind('8') or search_same.rfind('9') or search_same.rfind('0'):                
                    queryset_same = ArquivamentoSame.objects.filter(num_prontuario=search_same)
                    context['queryset_same'] = queryset_same                
                elif search_same == str:
                    queryset_same = ArquivamentoSame.objects.filter(nome_paciente=search_same)
                    context['queryset_same'] = queryset_same
            else:
                context['queryset_same'] = None
        return context


class SamaCreate(CreateView):
    model = ArquivamentoSame
    form_class = SameFormCreate

    def get_form_kwargs(self):
        kwargs = super(SamaCreate, self).get_form_kwargs() 
        if User.is_authenticated:
            user = self.request.user
            kwargs.update({
                'user': user
                })
        return kwargs

class SamaUpdate(UpdateView):
    model = ArquivamentoSame
    form_class = SameUpadateForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['queryset_cityes'] = City.objects.all()
        return context

class SameDetailView(DetailView):
    model = ArquivamentoSame

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        identificador = self.kwargs.get('pk')
        print(type(identificador),identificador)
        context['queryset_imprimir'] = ArquivamentoSame.objects.filter(id=identificador)
        return context
