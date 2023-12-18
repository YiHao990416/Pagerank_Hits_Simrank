import pandas as pd
import numpy as np
import os
from algorithms import *
import networkx as networkx
import matplotlib.pyplot as plt
import re
from utils import output_graph
import sys
np.set_printoptions(threshold=sys.maxsize)

def main():
    for filename in os.listdir("./Project3 Dataset"):
        

        df = pd.DataFrame()
        node_edge = []
        names = ['out','in']
        if filename.startswith('ibm'):
            with open("Project3 Dataset/ibm-5000.txt", 'r') as f: 
                for line in f.readlines():
                    line = line.strip()
                    edge = line.split()[1:]
                    node_edge.append(edge)
            df = pd.DataFrame(node_edge, columns = names)    
        
        else:
            df = pd.read_csv(f"Project3 Dataset/{filename}", header = None, names=names)
            node_edge= df.values.tolist()
        
        
        

        output_graph(filename, df)



   



        # names = ['out','in']
        # graph = pd.read_csv(f"Project3 Dataset/{filename}", header = None, names=names)

main()
