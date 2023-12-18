import pandas as pd
import numpy as np
from collections import OrderedDict
import sys

np.set_printoptions(threshold=sys.maxsize)
names = ['out','in']
graph = pd.read_csv("Project3 Dataset/graph_3.txt", header = None, names=names)



def hits_algorithms(df):
    
    # find the unique hubs
    unique_items = pd.unique(df[['out','in']].values.ravel('K'))
    unique_items = np.sort(unique_items)
    n = len(unique_items)
    hubs_counts = OrderedDict()
    roots_counts = OrderedDict()


    total_score = df.shape[0]
    # calculate the number of occurence
    for element in unique_items:
        hubs_counts[element] = 0
        roots_counts[element] = 0 
        try:
            hubs_counts[element] = (df['out'].value_counts()[element])
        except:
            pass
        try:
            roots_counts[element] = (df['in'].value_counts()[element]) 
        except:
            pass
    # print(list(roots_counts.values()))
    hubs = np.array(list(roots_counts.values()))
    roots = np.array(list(hubs_counts.values()))
    for iter in range(30):

        # new_roots = roots
        # new_hubs = hubs

        hubs = hubs / np.sum(hubs)
        roots = roots / np.sum(roots)        

    
    return hubs, roots



def pagerank_algorithms(df):
    
    # find the unique hubs
    unique_items =pd.unique(df[['out','in']].values.ravel('K'))
    unique_items = np.sort(unique_items)
    n = len(unique_items)  
    d = 0.10
    hubs_counts= OrderedDict()
    outdegree_list = []
    pagerank_dict ={}


    for element in unique_items:
        hubs_counts[element] = 0
        outdegree_list.append(df['out'][df['in'] == element].tolist())
        pagerank_dict[element] = 1/n
        try:
            hubs_counts[element] = (df['out'].value_counts()[element])
        except:
            pass

    pagerank = np.full(n, 1/n)    
    
    for iter in range(30):
        new_pagerank = np.zeros(n)
        for i, list in enumerate(outdegree_list):
            for j, element in enumerate(list):
                new_pagerank[i] += pagerank_dict[element] / hubs_counts[element]
        pagerank = (d/n) + (1-d)*new_pagerank

        for i,element in enumerate(unique_items):
            pagerank_dict[element] = pagerank[i]
        
    pagerank = pagerank/pagerank.sum()
    
    return pagerank
    
    


def simrank_algorithms(df):
    unique_items = pd.unique(df[['out','in']].values.ravel('K'))
    unique_items = np.sort(unique_items)
    n = len(unique_items)
    c = 0.7
    roots_counts = OrderedDict()
    outdegree_list = []

    for element in unique_items:
        roots_counts[element] = 0
        outdegree_list.append(df['out'][df['in'] == element].tolist())
        try:
            roots_counts[element] = (df['out'].value_counts()[element])
        except:
            pass

    simrank = np.zeros((n,n))
    for iter in range(30):
        new_simrank = np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                if unique_items[i] == unique_items[j]:
                    new_simrank[i,j] = 1.0
                else:
                    inlink_a = outdegree_list[i]
                    inlink_b = outdegree_list[j]
                    combination = []

                    inlink_simrank = 0.0
                    for a in inlink_a:
                        for b in inlink_b:
                            combination.append([a,b])
                    
                    for pair in combination:
                        if not pair:
                            continue
                        else:
                            inlink_simrank += simrank[(pair[0]-1),(pair[1]-1)]

                    if roots_counts[unique_items[i]] == 0 or roots_counts[unique_items[j]] == 0 or inlink_simrank == 0:
                        new_simrank[i,j] = 0
                    else:
                        new_simrank[i,j] =(c/(roots_counts[unique_items[i]]*roots_counts[unique_items[j]]))*inlink_simrank

        simrank = new_simrank
    
    return simrank
                








    