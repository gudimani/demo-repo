import networkx as nx
import random
graph = nx.Graph()
graph.add_nodes_from([0, 1, 2, 3, 4])
graph.add_edges_from([(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4)])
nx.draw(graph, with_labels=True, font_weight='bold')
collision_domain  = {0:[0,1,2],1:[2,3,4]}
common_nodes = set.intersection(*collision_domain.values())
for i in graph.nodes(data=False):
    
    for q_len in range(1):
        
        src = i
        dest = random.randrange(0,4)
        print("Source",src,"destination",dest)
        for key,values in collision_domain.items():
                if (src in values):
                    source_key = key
                    print('source_key',source_key)
                    if src == 2 and dest == any(collision_domain[key]) or any(collision_domain[key]):
                        if dest in values:
                            dest_key= key
                            source_key = dest_key
                            print('Domain of source 2',source_key)
                    if src == (any(collision_domain[key]) or any(collision_domain[key])) and dest == 2:
                        if dest in values:
                            dest_key = source_key
                            print('Domain of destination 2', dest_key)

                        
                if dest in values:
                    dest_key = key
                    print('dest_key',dest_key)

        if source_key == dest_key:
            print('same domain')
            
        else:
            source_nodes = collision_domain[source_key]
            dest_nodes = collision_domain[dest_key]
            print('source nodes',source_nodes)
            print('dest nodes',dest_nodes)
            for node in source_nodes:
                if node in dest_nodes:
                    print('Common Node', node)
                    next_hop = node
            print(next_hop)
            

                
                

            
                   
                

            
