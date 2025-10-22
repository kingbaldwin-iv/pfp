#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["numpy", "matplotlib"]
# ///

import numpy as np
import random
import matplotlib.pyplot as plt
class Plotter:
    def __init__(self,rounds,n,bounds,is_bw = False):
        self.rounds = rounds
        self.n = n
        self.is_bw = is_bw
        self.bounds = bounds
    def process(self, pos = None, is_bw = False):
        x = np.zeros(self.n)
        y = np.zeros(self.n)
        r = np.zeros(self.n)
        g = np.zeros(self.n)
        b = np.zeros(self.n)
        if pos is None:
            x[0] = random.randint(0,self.bounds)
            y[0] = random.randint(0,self.bounds)
        else:
            x[0] = pos[0]
            y[0] = pos[1]
        for i in range(1, self.n):
            v = list(bin(random.randint(1, 32))[2:])
            v = [0] * (5-len(v)) + v
            it = zip(v, [x,y,r,g,b])
            for com, val in (it):
                if com == '1':
                    val[i] = val[i-1] + 1
                else:
                    val[i] = val[i-1] - 1
        x = x % self.bounds
        y = y % self.bounds
        r = r % 256
        g = g % 256
        b = b % 256
        r = r / 255.0
        g = g / 255.0
        b = b / 255.0
        c = list(zip(r,g,b))
        if self.is_bw:
            c = list(map(lambda x: 'k' if sum(x) < 2 else 'w',c))
        return x,y,c
    def get_pos(self):
        poses = np.linspace(0,self.bounds//2,self.rounds)
        pss = set()
        for i in poses:
            pss.add((i,i))
            pss.add((i,self.bounds-i))
            pss.add((self.bounds-i,i))
            pss.add((self.bounds-i,self.bounds-i))
        return pss
    def plot(self):
        poses = self.get_pos()
        plotable = list()
        for i in poses:
            plotable.append(self.process(i))
        plt.title(f"5D Random Walk ({self.n} steps)")
        for x,y,c in plotable:
            plt.scatter(x,y,color=c,s=1)
        ax = plt.gca()
        ax.set_xlim([0, self.bounds])
        ax.set_ylim([0, self.bounds])
        plt.savefig("qq.pdf",format="pdf")
        plt.show()




#plotter = Plotter(rounds=8,n=100000,bounds=1000)
#plotter.plot()
plotter = Plotter(rounds=8,n=100000,bounds=1000,is_bw=True)
plotter.plot()


