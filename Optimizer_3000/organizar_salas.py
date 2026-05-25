temp = open('grupo_turmas.txt','r',encoding='utf-8')
valor = temp.read()
valor = eval(valor)
temp.close()
grupo_turmas = valor # exemplo {'t1':{'turmas':['1p_eng_software','3p_eng_software'],'num_alunos':40,'pcd':True},'t2':{'turmas':['1p_arquiterura','3p_arquitetura'],'num_alunos':20,'pcd':False}}

temp = open('salas.txt','r',encoding='utf-8')
valor = temp.read()
valor = eval(valor)
temp.close()

salas = valor #exemplo {'101':45,'102':30}

num_alunos = [] # Separa o número de alunos para ser utilizado depois no programa
for i in grupo_turmas:
 num_alunos.append(grupo_turmas[i]['num_alunos'])

 
#O txt será o novo programa que irá rodar e retornar o resultado
txt = """import pulp\n
problema = pulp.LpProblem('organizar_salas',pulp.LpMinimize)\n\n"""
salas_turmas = {} # Relação de cada sala com cada turma exemplo sala 101 turmas t1_101 e t2_101

temp5 = "\n\nproblema += " #Seguindo a moda do futuro, irei coletar a restrição para pcd logo aqui na formação das variáveis
for t in grupo_turmas:
 for s in salas:
  temp = t+'_'+s #turma_sala
  txt = txt + f'{temp} = pulp.LpVariable("{temp}", lowBound=0,upBound=1,cat="Integer")\n'
  if s not in salas_turmas:
   salas_turmas[s] = []
  if s in salas_turmas:
   salas_turmas[s].append(temp)
  if s[0] !='1' and grupo_turmas[t]['pcd'] == True: # Caso a sala não termine em um e a turma tenha pcd marcado como verdadeiro.
   temp5 = temp5 + temp+' + '

temp5 = temp5[:-3]
temp5 = temp5 + ' == 0'

if temp5 == "\n\nproblema  == 0": # Nesse caso, nenhum dos grupos de turmas possúi pcd como True
 temp5 = ""



temp = "\nproblema += " # Constroi a função utilizando as salas relacionadas com as turmas e o número de alunos

temp2 = "\n\n" # Eu vou aproveitar esse for para conseguir a primeira restrição no caso que a sala não pode ter mais alunos que sua capacidade

temp3 = "\n\n" #Continuando com a nova moda de otimização, eu vou também utilizar o temp3 para obter a restrição de uma sala só pode ser ocupada por um grupo de turmas
for a in salas_turmas:
 temp = temp +f'({salas[a]} -(' # 2**(capacidade da sala - numero alunos na turma) [a fórmula anterior não tinha o 2**(resultado) 
 temp2 = temp2 + f'problema += {salas[a]} -(' # A nova fórmula foi escolhida para fazer com que o programa escolhece o resultado válido com o menor número de espaços vazios individuais nas salas.
 temp3 = temp3 +f'problema += '
 for b in range(0,len(salas_turmas[a])):
  
  temp = temp +f'({salas_turmas[a][b]}*{num_alunos[b]})+' # turma*numero_alunos  + outraturma*numero_alunos
  temp2 = temp2 +f'({salas_turmas[a][b]}*{num_alunos[b]})+'
  temp3 = temp3 +f'{salas_turmas[a][b]} + ' #coloca o nome de todas as turmas referentes a uma mesma sala
  
 temp = temp[:-1] #Retira o '+' no final do texto
 temp = temp +')) +'
 temp2 = temp2[:-1]
 temp2 = temp2 +') >=0\n\n'
 temp3 = temp3[:-3]
 temp3 = temp3 +' <= 1\n\n'
temp = temp[:-2] # retira o ' +' no final do processo

txt = txt + temp # temp é adicionado ao txt que se tornará o programa python no futuro

# Agora vamos para as restrições

# A primeira das restrições é que as salas não podem ter mais alunos que sua capacidade
txt = txt + temp2 # Aproveitei do for anterior para construir essa restrição assim aumentando a velocidade de processamento.

# A segunda restrição é que não apenas um grupo de turmas pode ficar em uma sala, porém uma sala pode ficar vazia, ou seja o somatório das variáveis de turma de uma sala específica deve ser <= 1
txt = txt + temp3 # Seguindo a nova moda de otimizar, assim como no temp2 o temp3 também usa o for acima para obter a restrição.

# A terceira restrição é que um grupo de turmas deve estart alocado em pelomenos uma sala e no máximo uma sala, por exemplo: t1_101 +t1_102 == 1
temp4 = "\n\n" # Ironicamente o temp4 veio depois do temp5, esse é da restrição que um grupo de turmas deve ocupar no mínimo uma sala e no máximo uma sala

for t in grupo_turmas: # gera uma linha com todas as variáveis de possibilidade de uma determinada turma
 temp4 = temp4 + 'problema += '
 for s in salas:
  temp4 = temp4 +f'{t}_{s} + '
 temp4 = temp4[:-3]
 temp4 = temp4 + ' == 1\n\n'

txt = txt + temp4
# A última restrição é que, se o grupo de turmas possuir pcd, ela só pode ficar no primeiro andar
txt = txt + temp5

txt = txt +'\n'
txt = txt +'problema.solve()\n\n'
txt = txt +'fim = pulp.LpStatus[problema.status]\n\n'
txt = txt +'if fim != "Optimal":\n'#se o valor for diferente de "Optimal" ou seja, não foi possível encontrar uma solução optima:
txt = txt +' print("A organização sobre essas condições foi impossível")\n'
txt = txt +' input("Aperte enter para fechar")\n'
txt = txt +' exit()\n\n' # Ele vai parar aqui


txt = txt + f"salas_turmas = {salas_turmas}\n\n" # Aqui coloquei a relação das salas com as turmas para então ver que turma ficou com que sala.
txt = txt + 'salas_ocupadas = {}\n\n'
txt = txt +'for s in salas_turmas:\n'
txt = txt +' salas_ocupadas[s] = ""\n'
txt = txt +' while len(salas_turmas[s]) != 0:\n'
txt = txt +'  if eval(salas_turmas[s][0]).value() == 1:\n' # Confere se a turma foi selecionada
txt = txt +'   temp = salas_turmas[s][0]\n'
txt = txt +'   temp = temp.split("_")\n'
txt = txt +'   temp = temp[0]\n' # Se sim ela é adicionada ao dicionário com o valor da turma exemplo se t1_101 for == 1, t1 será guardado no dicionário com a chave '101' 

txt = txt +'   salas_ocupadas[s] = temp\n'
txt = txt +'   salas_turmas[s] = []\n\n'

txt = txt +'  else:\n'
txt = txt +'   salas_turmas[s].pop(0)\n\n'
txt = txt +'print(salas_ocupadas)\n'
txt = txt +'input("Aperte enter para fechar")'



#print(txt)
x = open('resolver_problema_salas.py','w',encoding='utf-8')
x.write(txt)
x.close()

#print(salas_turmas)
#print(num_alunos)
