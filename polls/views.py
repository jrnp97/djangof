from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# Filosofia DRY: Don't repeat yourself

# VIEW
from polls.models import Question


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
