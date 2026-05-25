import pulp

problema = pulp.LpProblem('organizar_salas',pulp.LpMinimize)

t1_101 = pulp.LpVariable("t1_101", lowBound=0,upBound=1,cat="Integer")
t1_102 = pulp.LpVariable("t1_102", lowBound=0,upBound=1,cat="Integer")
t1_201 = pulp.LpVariable("t1_201", lowBound=0,upBound=1,cat="Integer")
t2_101 = pulp.LpVariable("t2_101", lowBound=0,upBound=1,cat="Integer")
t2_102 = pulp.LpVariable("t2_102", lowBound=0,upBound=1,cat="Integer")
t2_201 = pulp.LpVariable("t2_201", lowBound=0,upBound=1,cat="Integer")
t3_101 = pulp.LpVariable("t3_101", lowBound=0,upBound=1,cat="Integer")
t3_102 = pulp.LpVariable("t3_102", lowBound=0,upBound=1,cat="Integer")
t3_201 = pulp.LpVariable("t3_201", lowBound=0,upBound=1,cat="Integer")

problema += (45 -((t1_101*40)+(t2_101*20)+(t3_101*30))) +(30 -((t1_102*40)+(t2_102*20)+(t3_102*30))) +(40 -((t1_201*40)+(t2_201*20)+(t3_201*30)))

problema += 45 -((t1_101*40)+(t2_101*20)+(t3_101*30)) >=0

problema += 30 -((t1_102*40)+(t2_102*20)+(t3_102*30)) >=0

problema += 40 -((t1_201*40)+(t2_201*20)+(t3_201*30)) >=0



problema += t1_101 + t2_101 + t3_101 <= 1

problema += t1_102 + t2_102 + t3_102 <= 1

problema += t1_201 + t2_201 + t3_201 <= 1



problema += t1_101 + t1_102 + t1_201 == 1

problema += t2_101 + t2_102 + t2_201 == 1

problema += t3_101 + t3_102 + t3_201 == 1



problema += t1_201 == 0
problema.solve()

fim = pulp.LpStatus[problema.status]

if fim != "Optimal":
 print("A organização sobre essas condições foi impossível")
 input("Aperte enter para fechar")
 exit()

salas_turmas = {'101': ['t1_101', 't2_101', 't3_101'], '102': ['t1_102', 't2_102', 't3_102'], '201': ['t1_201', 't2_201', 't3_201']}

salas_ocupadas = {}

for s in salas_turmas:
 salas_ocupadas[s] = ""
 while len(salas_turmas[s]) != 0:
  if eval(salas_turmas[s][0]).value() == 1:
   temp = salas_turmas[s][0]
   temp = temp.split("_")
   temp = temp[0]
   salas_ocupadas[s] = temp
   salas_turmas[s] = []

  else:
   salas_turmas[s].pop(0)

print(salas_ocupadas)
input("Aperte enter para fechar")