import pulp

problema = pulp.LpProblem('organizar_salas',pulp.LpMinimize)

t1_101_1 = pulp.LpVariable("t1_101_1", lowBound=0,upBound=1,cat="Integer")
t1_102_1 = pulp.LpVariable("t1_102_1", lowBound=0,upBound=1,cat="Integer")
t1_201_1 = pulp.LpVariable("t1_201_1", lowBound=0,upBound=1,cat="Integer")
t1_101_2 = pulp.LpVariable("t1_101_2", lowBound=0,upBound=1,cat="Integer")
t1_102_2 = pulp.LpVariable("t1_102_2", lowBound=0,upBound=1,cat="Integer")
t1_201_2 = pulp.LpVariable("t1_201_2", lowBound=0,upBound=1,cat="Integer")
t1_101_3 = pulp.LpVariable("t1_101_3", lowBound=0,upBound=1,cat="Integer")
t1_102_3 = pulp.LpVariable("t1_102_3", lowBound=0,upBound=1,cat="Integer")
t1_201_3 = pulp.LpVariable("t1_201_3", lowBound=0,upBound=1,cat="Integer")
t1_101_4 = pulp.LpVariable("t1_101_4", lowBound=0,upBound=1,cat="Integer")
t1_102_4 = pulp.LpVariable("t1_102_4", lowBound=0,upBound=1,cat="Integer")
t1_201_4 = pulp.LpVariable("t1_201_4", lowBound=0,upBound=1,cat="Integer")
t1_101_5 = pulp.LpVariable("t1_101_5", lowBound=0,upBound=1,cat="Integer")
t1_102_5 = pulp.LpVariable("t1_102_5", lowBound=0,upBound=1,cat="Integer")
t1_201_5 = pulp.LpVariable("t1_201_5", lowBound=0,upBound=1,cat="Integer")
t2_101_1 = pulp.LpVariable("t2_101_1", lowBound=0,upBound=1,cat="Integer")
t2_102_1 = pulp.LpVariable("t2_102_1", lowBound=0,upBound=1,cat="Integer")
t2_201_1 = pulp.LpVariable("t2_201_1", lowBound=0,upBound=1,cat="Integer")
t2_101_2 = pulp.LpVariable("t2_101_2", lowBound=0,upBound=1,cat="Integer")
t2_102_2 = pulp.LpVariable("t2_102_2", lowBound=0,upBound=1,cat="Integer")
t2_201_2 = pulp.LpVariable("t2_201_2", lowBound=0,upBound=1,cat="Integer")
t2_101_3 = pulp.LpVariable("t2_101_3", lowBound=0,upBound=1,cat="Integer")
t2_102_3 = pulp.LpVariable("t2_102_3", lowBound=0,upBound=1,cat="Integer")
t2_201_3 = pulp.LpVariable("t2_201_3", lowBound=0,upBound=1,cat="Integer")
t2_101_4 = pulp.LpVariable("t2_101_4", lowBound=0,upBound=1,cat="Integer")
t2_102_4 = pulp.LpVariable("t2_102_4", lowBound=0,upBound=1,cat="Integer")
t2_201_4 = pulp.LpVariable("t2_201_4", lowBound=0,upBound=1,cat="Integer")
t2_101_5 = pulp.LpVariable("t2_101_5", lowBound=0,upBound=1,cat="Integer")
t2_102_5 = pulp.LpVariable("t2_102_5", lowBound=0,upBound=1,cat="Integer")
t2_201_5 = pulp.LpVariable("t2_201_5", lowBound=0,upBound=1,cat="Integer")
t3_101_1 = pulp.LpVariable("t3_101_1", lowBound=0,upBound=1,cat="Integer")
t3_102_1 = pulp.LpVariable("t3_102_1", lowBound=0,upBound=1,cat="Integer")
t3_201_1 = pulp.LpVariable("t3_201_1", lowBound=0,upBound=1,cat="Integer")
t3_101_2 = pulp.LpVariable("t3_101_2", lowBound=0,upBound=1,cat="Integer")
t3_102_2 = pulp.LpVariable("t3_102_2", lowBound=0,upBound=1,cat="Integer")
t3_201_2 = pulp.LpVariable("t3_201_2", lowBound=0,upBound=1,cat="Integer")
t3_101_3 = pulp.LpVariable("t3_101_3", lowBound=0,upBound=1,cat="Integer")
t3_102_3 = pulp.LpVariable("t3_102_3", lowBound=0,upBound=1,cat="Integer")
t3_201_3 = pulp.LpVariable("t3_201_3", lowBound=0,upBound=1,cat="Integer")
t3_101_4 = pulp.LpVariable("t3_101_4", lowBound=0,upBound=1,cat="Integer")
t3_102_4 = pulp.LpVariable("t3_102_4", lowBound=0,upBound=1,cat="Integer")
t3_201_4 = pulp.LpVariable("t3_201_4", lowBound=0,upBound=1,cat="Integer")
t3_101_5 = pulp.LpVariable("t3_101_5", lowBound=0,upBound=1,cat="Integer")
t3_102_5 = pulp.LpVariable("t3_102_5", lowBound=0,upBound=1,cat="Integer")
t3_201_5 = pulp.LpVariable("t3_201_5", lowBound=0,upBound=1,cat="Integer")
t4_101_1 = pulp.LpVariable("t4_101_1", lowBound=0,upBound=1,cat="Integer")
t4_102_1 = pulp.LpVariable("t4_102_1", lowBound=0,upBound=1,cat="Integer")
t4_201_1 = pulp.LpVariable("t4_201_1", lowBound=0,upBound=1,cat="Integer")
t4_101_2 = pulp.LpVariable("t4_101_2", lowBound=0,upBound=1,cat="Integer")
t4_102_2 = pulp.LpVariable("t4_102_2", lowBound=0,upBound=1,cat="Integer")
t4_201_2 = pulp.LpVariable("t4_201_2", lowBound=0,upBound=1,cat="Integer")
t4_101_3 = pulp.LpVariable("t4_101_3", lowBound=0,upBound=1,cat="Integer")
t4_102_3 = pulp.LpVariable("t4_102_3", lowBound=0,upBound=1,cat="Integer")
t4_201_3 = pulp.LpVariable("t4_201_3", lowBound=0,upBound=1,cat="Integer")
t4_101_4 = pulp.LpVariable("t4_101_4", lowBound=0,upBound=1,cat="Integer")
t4_102_4 = pulp.LpVariable("t4_102_4", lowBound=0,upBound=1,cat="Integer")
t4_201_4 = pulp.LpVariable("t4_201_4", lowBound=0,upBound=1,cat="Integer")
t4_101_5 = pulp.LpVariable("t4_101_5", lowBound=0,upBound=1,cat="Integer")
t4_102_5 = pulp.LpVariable("t4_102_5", lowBound=0,upBound=1,cat="Integer")
t4_201_5 = pulp.LpVariable("t4_201_5", lowBound=0,upBound=1,cat="Integer")

problema += (45 -((t1_101_1*40)+(t2_101_1*20)+(t3_101_1*30)+(t4_101_1*30))) +(30 -((t1_102_1*40)+(t2_102_1*20)+(t3_102_1*30)+(t4_102_1*30))) +(40 -((t1_201_1*40)+(t2_201_1*20)+(t3_201_1*30)+(t4_201_1*30))) +(45 -((t1_101_2*40)+(t2_101_2*20)+(t3_101_2*30)+(t4_101_2*30))) +(30 -((t1_102_2*40)+(t2_102_2*20)+(t3_102_2*30)+(t4_102_2*30))) +(40 -((t1_201_2*40)+(t2_201_2*20)+(t3_201_2*30)+(t4_201_2*30))) +(45 -((t1_101_3*40)+(t2_101_3*20)+(t3_101_3*30)+(t4_101_3*30))) +(30 -((t1_102_3*40)+(t2_102_3*20)+(t3_102_3*30)+(t4_102_3*30))) +(40 -((t1_201_3*40)+(t2_201_3*20)+(t3_201_3*30)+(t4_201_3*30))) +(45 -((t1_101_4*40)+(t2_101_4*20)+(t3_101_4*30)+(t4_101_4*30))) +(30 -((t1_102_4*40)+(t2_102_4*20)+(t3_102_4*30)+(t4_102_4*30))) +(40 -((t1_201_4*40)+(t2_201_4*20)+(t3_201_4*30)+(t4_201_4*30))) +(45 -((t1_101_5*40)+(t2_101_5*20)+(t3_101_5*30)+(t4_101_5*30))) +(30 -((t1_102_5*40)+(t2_102_5*20)+(t3_102_5*30)+(t4_102_5*30))) +(40 -((t1_201_5*40)+(t2_201_5*20)+(t3_201_5*30)+(t4_201_5*30)))

problema += 45 -((t1_101_1*40)+(t2_101_1*20)+(t3_101_1*30)+(t4_101_1*30)) >=0

problema += 30 -((t1_102_1*40)+(t2_102_1*20)+(t3_102_1*30)+(t4_102_1*30)) >=0

problema += 40 -((t1_201_1*40)+(t2_201_1*20)+(t3_201_1*30)+(t4_201_1*30)) >=0

problema += 45 -((t1_101_2*40)+(t2_101_2*20)+(t3_101_2*30)+(t4_101_2*30)) >=0

problema += 30 -((t1_102_2*40)+(t2_102_2*20)+(t3_102_2*30)+(t4_102_2*30)) >=0

problema += 40 -((t1_201_2*40)+(t2_201_2*20)+(t3_201_2*30)+(t4_201_2*30)) >=0

problema += 45 -((t1_101_3*40)+(t2_101_3*20)+(t3_101_3*30)+(t4_101_3*30)) >=0

problema += 30 -((t1_102_3*40)+(t2_102_3*20)+(t3_102_3*30)+(t4_102_3*30)) >=0

problema += 40 -((t1_201_3*40)+(t2_201_3*20)+(t3_201_3*30)+(t4_201_3*30)) >=0

problema += 45 -((t1_101_4*40)+(t2_101_4*20)+(t3_101_4*30)+(t4_101_4*30)) >=0

problema += 30 -((t1_102_4*40)+(t2_102_4*20)+(t3_102_4*30)+(t4_102_4*30)) >=0

problema += 40 -((t1_201_4*40)+(t2_201_4*20)+(t3_201_4*30)+(t4_201_4*30)) >=0

problema += 45 -((t1_101_5*40)+(t2_101_5*20)+(t3_101_5*30)+(t4_101_5*30)) >=0

problema += 30 -((t1_102_5*40)+(t2_102_5*20)+(t3_102_5*30)+(t4_102_5*30)) >=0

problema += 40 -((t1_201_5*40)+(t2_201_5*20)+(t3_201_5*30)+(t4_201_5*30)) >=0



problema += t1_101_1 + t2_101_1 + t3_101_1 + t4_101_1 <= 1

problema += t1_102_1 + t2_102_1 + t3_102_1 + t4_102_1 <= 1

problema += t1_201_1 + t2_201_1 + t3_201_1 + t4_201_1 <= 1

problema += t1_101_2 + t2_101_2 + t3_101_2 + t4_101_2 <= 1

problema += t1_102_2 + t2_102_2 + t3_102_2 + t4_102_2 <= 1

problema += t1_201_2 + t2_201_2 + t3_201_2 + t4_201_2 <= 1

problema += t1_101_3 + t2_101_3 + t3_101_3 + t4_101_3 <= 1

problema += t1_102_3 + t2_102_3 + t3_102_3 + t4_102_3 <= 1

problema += t1_201_3 + t2_201_3 + t3_201_3 + t4_201_3 <= 1

problema += t1_101_4 + t2_101_4 + t3_101_4 + t4_101_4 <= 1

problema += t1_102_4 + t2_102_4 + t3_102_4 + t4_102_4 <= 1

problema += t1_201_4 + t2_201_4 + t3_201_4 + t4_201_4 <= 1

problema += t1_101_5 + t2_101_5 + t3_101_5 + t4_101_5 <= 1

problema += t1_102_5 + t2_102_5 + t3_102_5 + t4_102_5 <= 1

problema += t1_201_5 + t2_201_5 + t3_201_5 + t4_201_5 <= 1



problema += t1_101_1 + t1_102_1 + t1_201_1 + t1_101_2 + t1_102_2 + t1_201_2 + t1_101_3 + t1_102_3 + t1_201_3 + t1_101_4 + t1_102_4 + t1_201_4 + t1_101_5 + t1_102_5 + t1_201_5 == 3

problema += t2_101_1 + t2_102_1 + t2_201_1 + t2_101_2 + t2_102_2 + t2_201_2 + t2_101_3 + t2_102_3 + t2_201_3 + t2_101_4 + t2_102_4 + t2_201_4 + t2_101_5 + t2_102_5 + t2_201_5 == 2

problema += t3_101_1 + t3_102_1 + t3_201_1 + t3_101_2 + t3_102_2 + t3_201_2 + t3_101_3 + t3_102_3 + t3_201_3 + t3_101_4 + t3_102_4 + t3_201_4 + t3_101_5 + t3_102_5 + t3_201_5 == 2

problema += t4_101_1 + t4_102_1 + t4_201_1 + t4_101_2 + t4_102_2 + t4_201_2 + t4_101_3 + t4_102_3 + t4_201_3 + t4_101_4 + t4_102_4 + t4_201_4 + t4_101_5 + t4_102_5 + t4_201_5 == 2



problema += t1_101_1 + t1_102_1 + t1_201_1 <=1
problema += t1_101_2 + t1_102_2 + t1_201_2 <=1
problema += t1_101_3 + t1_102_3 + t1_201_3 <=1
problema += t1_101_4 + t1_102_4 + t1_201_4 <=1
problema += t1_101_5 + t1_102_5 + t1_201_5 <=1


problema += t2_101_1 + t2_102_1 + t2_201_1 <=1
problema += t2_101_2 + t2_102_2 + t2_201_2 <=1
problema += t2_101_3 + t2_102_3 + t2_201_3 <=1
problema += t2_101_4 + t2_102_4 + t2_201_4 <=1
problema += t2_101_5 + t2_102_5 + t2_201_5 <=1


problema += t3_101_1 + t3_102_1 + t3_201_1 <=1
problema += t3_101_2 + t3_102_2 + t3_201_2 <=1
problema += t3_101_3 + t3_102_3 + t3_201_3 <=1
problema += t3_101_4 + t3_102_4 + t3_201_4 <=1
problema += t3_101_5 + t3_102_5 + t3_201_5 <=1


problema += t4_101_1 + t4_102_1 + t4_201_1 <=1
problema += t4_101_2 + t4_102_2 + t4_201_2 <=1
problema += t4_101_3 + t4_102_3 + t4_201_3 <=1
problema += t4_101_4 + t4_102_4 + t4_201_4 <=1
problema += t4_101_5 + t4_102_5 + t4_201_5 <=1




problema += t1_201_1 + t1_201_2 + t1_201_3 + t1_201_4 + t1_201_5 == 0
problema.solve()

fim = pulp.LpStatus[problema.status]

if fim != "Optimal":
 print("A organização sobre essas condições foi impossível")
 input("Aperte enter para fechar")
 exit()

salas_turmas = {'101_1': ['t1_101_1', 't2_101_1', 't3_101_1', 't4_101_1'], '102_1': ['t1_102_1', 't2_102_1', 't3_102_1', 't4_102_1'], '201_1': ['t1_201_1', 't2_201_1', 't3_201_1', 't4_201_1'], '101_2': ['t1_101_2', 't2_101_2', 't3_101_2', 't4_101_2'], '102_2': ['t1_102_2', 't2_102_2', 't3_102_2', 't4_102_2'], '201_2': ['t1_201_2', 't2_201_2', 't3_201_2', 't4_201_2'], '101_3': ['t1_101_3', 't2_101_3', 't3_101_3', 't4_101_3'], '102_3': ['t1_102_3', 't2_102_3', 't3_102_3', 't4_102_3'], '201_3': ['t1_201_3', 't2_201_3', 't3_201_3', 't4_201_3'], '101_4': ['t1_101_4', 't2_101_4', 't3_101_4', 't4_101_4'], '102_4': ['t1_102_4', 't2_102_4', 't3_102_4', 't4_102_4'], '201_4': ['t1_201_4', 't2_201_4', 't3_201_4', 't4_201_4'], '101_5': ['t1_101_5', 't2_101_5', 't3_101_5', 't4_101_5'], '102_5': ['t1_102_5', 't2_102_5', 't3_102_5', 't4_102_5'], '201_5': ['t1_201_5', 't2_201_5', 't3_201_5', 't4_201_5']}

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