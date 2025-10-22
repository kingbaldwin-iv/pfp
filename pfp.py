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
    def process(self, pos, is_bw = False):
        x = np.zeros(self.n)
        y = np.zeros(self.n)
        r = np.zeros(self.n)
        g = np.zeros(self.n)
        b = np.zeros(self.n)
        x[0] = pos[0]
        y[0] = pos[1]
        for i in range(1, self.n):
            v = list(bin(random.randint(1, 32))[2:])
            it = zip([0] * (5-len(v)) + v, [x,y,r,g,b])
            for com, val in it:
                val[i] = val[i-1] + 1 if com == '1' else val[i-1] - 1
        c = list(zip((r % 256) / 255.0,(g % 256) / 255.0,(b % 256) / 255.0))
        if self.is_bw:
            c = list(map(lambda x: 'k' if sum(x) < 2 else 'w',c))
        return x % self.bounds,y % self.bounds,c
    def get_pos(self):
        poses = np.linspace(0,self.bounds//2,self.rounds)
        pss = set()
        for i in poses:
            pss = pss.union({(i,i),(i,self.bounds-i),(self.bounds-i,i),(self.bounds-i,self.bounds-i)})
        return pss
    def plot(self):
        poses = self.get_pos()
        plotable = [self.process(i) for i in poses]
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

