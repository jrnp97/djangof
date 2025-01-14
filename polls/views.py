from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.views import View # <- CLASE PADRE
# Create your views here.
# Filosofia DRY: Don't repeat yourself

# VIEW
from polls.models import Question, Deudor


def index(request):

    return HttpResponse('Hola D & D')


# 1. Cree la view: SIEMPRE SIEMPRE Tiene que retornar un HttpResponse
def primer_template(request):

    kiko = "valor"
    valores = (
        "verder",
        "azul",
        "amarillo",
        "rojo",
    )
    return render(
        request,
        # Server rendering
        template_name='polls/index.html',
        context={'name': kiko, 'colores': valores}
    )

class PrimerTemplate(View):
    def get(self, request):
        return render(
            request,
            template_name='polls/index.html',
        )


def template_raw(request):
    kiko = "valor"
    valores = ("verder", "azul", "amarillo", "rojo",)
    respuesta = loader.render_to_string(
        template_name='polls/index.html',
        context={'name': kiko, 'colores': valores},
        request=request,
    )
    return HttpResponse(respuesta)


def kiko(request):
    return HttpResponse('KIKO')


def db_interact(request):
    questions = Question.objects.all()
    return render(
        request=request,
        template_name='polls/question.html',
        context={
            'questions': questions,
        }
    )


from .forms import GoogleForm, DeudorForm

def form_test(request):
    questions = Question.objects.all()
    form = GoogleForm()
    dform = DeudorForm()
    return render(
        request=request,
        template_name='polls/question.html',
        context={
            'questions': questions,
            'form': form,
            'dform': dform,
        }
    )


# 1. View

# forms: Utilizas instancias
from .forms import ConvertForm
def conversor_monedas(request):
    print("HOLA ESTOY EXECUTANDO!!!")
    print("REQUEST: ", request)
    if request.method == 'POST':
        form = ConvertForm(request.POST)
        if form.is_valid():
            print("DATOS VALIDOS!!!!")
    else:
        form = ConvertForm()
    return render(
        request=request,
        template_name='polls/conversor.html',
        context={
            'form': form,
        },
    )

# 1. CBV [Class-Based Views]: Mejorar el codigo en terminos de lectura
# 2. Ayudar a reducir la cantidade de codigo gracias a las capacidades de reutilizacion de codigo que tenemos en POO.
# 3. Ayudar a reducir el codigo utilizando herencia.



# 1. View
class ConversorCBV(View):
    template = 'polls/conversor.html'

    def __render(self, context, request):
        context.update({'titulo': 'JAIME'})
        return render(
            request=request, template_name=self.template, context=context
        )
    def post(self, request):
        form = ConvertForm(request.POST)
        if form.is_valid():
            print("DATOS VALIDOS!!!!")
        return self.__render(
            request=request,
            context={'form': form},
        )
    def get(self, request):
        form = ConvertForm()
        return self.__render(
            request=request,
            context={'form': form},
        )


class ConversorNew(ConversorCBV):
    template = 'polls/conversor_new.html'

# Django como es tu mejor amigo
# Generic Views: Que son CBV con comportamiendo genericos para su re-uso
# 1. Caso donde simplemente quieres renderizar um template: TemplateView
# 2. Caso donde simplemente quieres renderizar un template y un formulario: FormView

from django.views.generic import TemplateView, FormView


class PrimerTemplateCBV(TemplateView):
    template_name = 'polls/index.html'


class ConversorCBVTWO(FormView):
    form_class = ConvertForm
    template_name = 'polls/conversor.html'


## CRUD Deudores

from django.views.generic import ListView, CreateView, DetailView

class DeudoresList(ListView):
    model = Deudor
    template_name = 'polls/lista_deudores.html'
    context_object_name = 'deudores'

from django.urls import reverse_lazy


class DeudoresCreate(CreateView):
    form_class = DeudorForm
    template_name = 'polls/crear_deudor.html'
    success_url = reverse_lazy('lista_deudores')


class DeudoresDetail(DetailView):
    model = Deudor
    template_name = 'polls/detail_deudor.html'
    pk_url_kwarg = 'id'


def update_deudor(request, id):
    deudor = Deudor.objects.get(id=id)
    if request.method == 'POST':
        form = DeudorForm(request.POST, instance=deudor)
        if form.is_valid():
            # Actualizar el deudor
            form.save()
            print("IS VALID")
            return redirect('lista_deudores')
    else:
        form = DeudorForm(instance=deudor)
    return render(
        request=request,
        template_name='polls/crear_deudor.html',
        context={
            'form': form,
            'update': True,
            'deudor': deudor,
        }
    )


def delete_deudor(request, id):
    deudor = Deudor.objects.get(id=id)
    deudor.delete()
    return redirect('lista_deudores')
