import re
from algorithms import *
import sys
np.set_printoptions(threshold=sys.maxsize)

def output_graph(filename, df):

    match = filename.split('.')
    output_name = match[0]

    array_hubs, array_authority = hits_algorithms(df)
    np.savetxt(f'./results/{output_name}/{output_name}_HITS_hubs.txt',array_hubs,newline =' ' , fmt='%1.3f')
    # f =  open(f'./results/{output_name}/{output_name}_HITS_hubs.txt','w')
    # f.write(content)
    # f.close()

    # content = array_authority
    np.savetxt(f'./results/{output_name}/{output_name}_HITS_authority.txt',array_authority,newline =' ', fmt='%1.3f')
    # f =  open(f'./results/{output_name}/{output_name}_HITS_authority.txt','w')
    # f.write(content)
    # f.close()

    array = pagerank_algorithms(df)
    np.savetxt(f'./results/{output_name}/{output_name}_PageRank.txt',array,newline =' ', fmt='%1.3f')
    # content = array
    # f =  open(f'./results/{output_name}/{output_name}_PageRank.txt','w')
    # f.write(content)
    # f.close()
    if filename.startswith('ibm') or filename.startswith('graph_6'):
        pass
    else:
        array = simrank_algorithms(df)
        np.savetxt(f'./results/{output_name}/{output_name}_SimRank.txt',array,newline ='\n', fmt='%1.3f')
        # content = array
        # f =  open(f'./results/{output_name}/{output_name}_SimRank.txt','w')
        # f.write(content)
        # f.close()

