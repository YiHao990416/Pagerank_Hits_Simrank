import pandas as pd
import numpy as np
from collections import OrderedDict
names = ['out','in']
graph = pd.read_csv("Project3 Dataset/graph_1.txt", header = None, names=names)



def hits_algorithms(df):
    
    # find the unique hubs
    unique_items = pd.unique(df[['out','in']].values.ravel('K'))
    unique_items = np.sort(unique_items)
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
    
    roots_counts = np.array(list(roots_counts.values()))
    hubs_counts = np.array(list(hubs_counts.values()))
    
    print(hubs_counts)
    print(roots_counts)

    for i in range(10):
        roots_score = (np.sum(np.square(roots_counts)))**(1/2)
        hubs_score = (np.sum(np.square(hubs_counts)))**(1/2)

        roots_counts = np.divide(roots_counts, roots_score)
        hubs_counts = np.divide(hubs_counts, hubs_score)
    
    print(hubs_counts)
    print(roots_counts)

    

# hits_algorithms(graph)



def pagerank_algorithms(df):
    
    # find the unique hubs
    unique_items =pd.unique(df[['out','in']].values.ravel('K'))
    unique_items = np.sort(unique_items)
    n = len(unique_items)  
    d = 0.10
    hubs_counts= OrderedDict()
    outdegree_list = []
    pagerank = []

    for element in unique_items:
        hubs_counts[element] = 0
        outdegree_list.append(df['out'][df['in'] == element].tolist())
        pagerank.append(1/n)
        try:
            hubs_counts[element] = (df['out'].value_counts()[element])
        except:
            pass

    data = {"node": unique_items,'rank': pagerank, 'outlink':list(hubs_counts.values())}
    new_df = pd.DataFrame(data)

    # def generate_pagerank(df):

    #     for i,list in enumerate(outdegree_list):
    #         score = 0
    #         for element in list:
    #             score += float(df['rank'][df['node'] == element].values / df['outlink'][df['node'] == element].values)

    #         score = d/n + (1-d)*score
    #         df.iloc[i,1] = score

    #     return new_df    
        

        
    def generate_pagerank(df,pagerank):
        new_pagerank = []
        for i in range(n):
            df.iloc[i,1] = pagerank[i]
        print(new_df)
        for i,list in enumerate(outdegree_list):
            score = 0
            for element in list:
                score += float((df['rank'][df['node'] == element]).values / (df['outlink'][df['node'] == element]).values)
                
            score = (d/n) + (1-d)*score
            
            new_pagerank.append(score)

        return new_pagerank


    
    pagerank1 = generate_pagerank(new_df,pagerank)
    print(pagerank1)









pagerank_algorithms(graph)

# def simrank_algorithms(df):

    