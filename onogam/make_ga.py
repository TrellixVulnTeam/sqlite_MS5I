import random
from deap import base,creator,tools,algorithms

#最大化問題として設定
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("a",random.randint,0,10)
toolbox.register("init",tools.initRepeat, creator.Individual, toolbox.a,2)

x = tools.initRepeat(creator.Individual,random.random,4)
#y = tools.
algorithms.eaSimple(population=1,toolbox=toolbox,cxpb=0.9,mutpb=0.1,ngen=50,halloffame=tools.ParetoFront())