#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd
import numpy as np
from collections import defaultdict
from queue import Queue
import math


# In[58]:


def r1_r2(l: dict, A: np.array) -> dict:
    for row in A:
        l[row[0]][0] += 1
        l[row[1]][1] += 1
    return l


# In[59]:


def r1_r2_r3_r4(l: dict, A: np.array) -> dict:
    for row in A:
        main = row[0]
        sub = row[1]
        l[main][0] += 1
        l[sub][1] += 1
        for subrow in A:
            if subrow[0] == sub:
                l[main][2] += 1
                l[subrow[1]][3] += 1
    return l


# In[60]:


def r5(d: dict, A: np.array) -> dict:
    q = Queue()
    q.put(1)
    r5 = {}
    while not q.empty():
        main = q.get()
        l = []
        for row in A:
            if row[0] == main:
                l.append(row[1])
                q.put(row[1])
        if len(l) > 1:
            for elem in l:
                d[elem][4] += l.__len__() - 1
    return d


# In[61]:


def entr(graph: np.array) -> float:
    def set_def():
        return [0, 0, 0, 0, 0]
    l = defdict(set_def)
    r1_r2_r3_r4(l, graph)
    r5(l, graph)
    l = pd.DataFrame(l)
    l = l.to_numpy().T
    print(f"Матрица связности графа A = \n{l}")
    n = len(l)
    s = 0.0
    for elem in l:
        for cond in elem:
            if cond > 0:
                p = cond / (n - 1)
                logp = math.log10(p)
                s += p * logp
    return -s


# In[62]:


def pipeline(files: list):
    for i, file in enumerate(files):
        A = pd.read_csv(file).to_numpy()
        print(f"№ {i+1} ")
        entropy = entropy_calc(A)
        print(f"Энтропия = {entropy:.4f} \n")


# In[63]:


file = task4.csv
pipeline(files)

