import numpy as np
import pandas as pd
names = ['index','out','in']
edges =[]
with open("Project3 Dataset/ibm-5000.txt", 'r') as f: 
    for line in f.readlines():
        line = line.strip()
        edge = line.split()[1:]
        edges.append(edge)

