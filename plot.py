import matplotlib.pyplot as plt
import numpy as np


# points pop
def plot(lis, pop):
    """
    Plot data points with the best vector for dimension reduction
    :return:
    """

    xs = [i[0] for i in lis]
    ys = [i[1] for i in lis]
    # plot entries
    plt.plot(xs, ys, '+', color='#777777')

    best = pop[0].gene
    most = [(best[1]/best[0]*i) for i in xs]
    x = np.linspace(0, 60, 100)
    # plot line
    # plt.plot(x, pop[0].gene[0]*x + pop[0].gene[1]*x, color='r', linewidth=.3)
    plt.plot(xs, most, color='r', linewidth=.3)

    pas = [i.gene[0] for i in pop]
    pbs = [i.gene[1] for i in pop]

    # plot results
    plt.scatter(xs, most , s=10, facecolors='none', edgecolors='#5500ff')
    plt.savefig('.//result.png')
    plt.show()


# last = [(pas[i]*xs[i] + pbs[i]*ys[i]) for i in range(len(pop))]













