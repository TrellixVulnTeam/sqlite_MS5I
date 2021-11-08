from deap import base,creator,tools,algorithms
import random

#最大化問題として設定
creator.create("FitnessMax",base.Fitness, weights = (1.0,))
creator.create("Individual", list, fitness = creator.FitnessMax)

items = {}
items[0] = (5,100)#おにぎり
items[1] = (10,140)#ポテチ
items[2] = (9,150)#お茶
items[3] = (5,130)#コーヒー
items[4] = (5,110)#バナナ
items[5] = (4,90)#パン


def evalknapsack(individual):
    weight = 0.0
    value = 0.0
    for i in range(6):
        weight += items[i] [0] *individual[i]
        value += items[i] [1] *individual[i]
    if weight > 100:
        value =0.0

    return value,

toolbox = base.Toolbox()
toolbox.register("attribute", random.randint, 0,10)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute, 6)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("select",tools.selTournament, tournsize = 5)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutUniformInt, low=0,up=20,indpb=0.2)
toolbox.register("evaluate",evalknapsack)
random.seed(128)
#何世代まで行うか
NGEN = 1000
#集団の個体数
POP = 1000
#交叉確率
CXPB = 0.9
#個体が突然変異を起こす確率
MUTPB = 0.2

pop = toolbox.population(n=POP)

for ind in pop:
    ind.fitness.values = toolbox.evaluate(ind)

hof = tools.ParetoFront()

algorithms.eaSimple(pop, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=NGEN, halloffame=hof)

best_ind = tools.selBest(pop, 1)[0]

print("最もいい個体は　%s で、その時の目的関数の値は %s" % (best_ind, best_ind.fitness.values))