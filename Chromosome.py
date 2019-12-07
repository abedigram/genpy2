import random
import statistics
import numpy as np


class Chromosome:
    def __init__(self, chromosome_length, min, max):
        # Todo create a random list for genes between min and max below
        self.gene = []
        for i in range(chromosome_length):
            self.gene.append(random.uniform(min, max))
        self.score = 0

    def evaluate(self, points):
        """
        Update Score Field Here
        """
        # Todo

        self.normalize()

        temp = []
        for i in points:
            temp.append(self.gene[0]*i[0] + self.gene[1]*i[1])
        self.score = statistics.stdev(temp)

    def normalize(self):
        a = self.gene[0]
        b = self.gene[1]

        self.gene[0] = a / np.sqrt(a**2 + b**2)
        self.gene[1] = b / np.sqrt(a**2 + b**2)