from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from organizar_salas import gerar_organizador
from resolver_problema_salas import organizar_salas
# Create your views here.
@login_required
def home(request):
    if request.method =="GET":
        return render(request, 'core/home.html')
    else:
        return redirect('resultados')


def logout_view(request):
    logout(request)

    return redirect('login')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    

    form = LoginForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        
    return render(request, 'core/login.html', {
        'form': form
    })


def register_view(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        
    return render(request, 'core/register.html', {
        'form': form
    })

def resultados_view(request):
    if request.method =="POST":
        return redirect('home')
    x = open("grupo_turmas.txt","r",encoding="utf-8")
    turmas = x.read()
    x.close()
    turmas = eval(turmas)
    x = open("salas.txt","r",encoding="utf-8")
    salas = x.read()
    x.close()
    salas = eval(salas)
    gerar_organizador(turmas,salas)
    dados = organizar_salas()
    semana = {"1":{},"2":{},"3":{},"4":{},"5":{}} # dicionário
    if dados == {}:
        return redirect ('home') # organização impossível
    for d in dados:
        if dados[d] == "":
            pass
        elif d.split('_')[-1] =="1":
            semana["1"][d[:-2]] =dados[d] #[:-2] remove o _[numero]
        elif d.split('_')[-1] =="2":
            semana["2"][d[:-2]] =dados[d]  
        elif d.split('_')[-1] =="3":
            semana["3"][d[:-2]] =dados[d]  
        elif d.split('_')[-1] =="4":
            semana["4"][d[:-2]] =dados[d]
        elif d.split('_')[-1] =="5":
            semana["5"][d[:-2]] =dados[d]
        else:# Na teoria esse caso é impossível porém se algo assim ocorrer ele irá ignorar
            pass

    calendario_final = []
    # o calendario_final é uma lista do conteúdo que o calendário teria
    # O calendário vai conter a relação das salas com as ocupações que tem na semana exemplo {"101":{"1":"N/A","2":"1p_eng_software,3p_eng_software",}}
    # Caso a sala esteja vazia o valor será N/A caso esteja preenchida, todas as turmas que fazem parte irão estar presentes.
    calendario = {}
    for s in salas:
        calendario = {"sala":s} # adiciona a própria sala para consulta
        if s in semana["1"]:
            calendario["1"] = str(turmas[semana["1"][s]]['turmas'])[1:-1]# remove o [ e o ] da lista dos integrandes dos grupos de turmas
        else:
            calendario["1"] = "N/A"

        if s in semana["2"]:
            calendario["2"] = str(turmas[semana["2"][s]]['turmas'])[1:-1]
        else:
            calendario["2"] = "N/A"

        if s in semana["3"]:
            calendario["3"] = str(turmas[semana["3"][s]]['turmas'])[1:-1]
        else:
            calendario["3"] = "N/A"


        if s in semana["4"]:
            calendario["4"] = str(turmas[semana["4"][s]]['turmas'])[1:-1]
        else:
            calendario["4"] = "N/A"

        if s in semana["5"]:
            calendario["5"] = str(turmas[semana["5"][s]]['turmas'])[1:-1]
        else:
            calendario["5"] = "N/A"
            
        calendario_final.append(calendario)

            
    print(calendario_final)
    return render(request,'core/resultados.html',{"calendario":calendario_final})
