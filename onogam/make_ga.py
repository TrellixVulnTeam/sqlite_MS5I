import random
from deap import base,creator,tools,algorithms

#最大化問題として設定
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("a",random.randint,0,10)
toolbox.register("init",tools.initRepeat, creator.Individual, toolbox.a,2)
toolbox.register("population", tools.initRepeat, list, toolbox.init)
toolbox.register("select", tools.selTournament, tournsize=5)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutUniformInt, low=0, up=20,indpd =0.2)



x = tools.initRepeat(creator.Individual,random.random,4)
#y = tools.
print(x)