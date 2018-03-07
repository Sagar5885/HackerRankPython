graph = {'0':{'1':1,'2':4}, '1':{'2':1, '3':3}, '2':{'3':1, '4':5}, '3':{'4':1, '5':8}, '4':{'5':1}}

def dijkstra(graph, start, end):

    D = {} #Final Destination Dictionary
    P = {} #Predecessor Dictionary

    #Fill the dictionaries with the default values;
    for node in graph.keys():
        D[node] = -1 #vertices are unreachable
        P[node] = "" #vertices have no predecessors


    D[start] = 0 #The start vertex needs no move
    unseen_nodes = graph.keys() #All nodes are unseen

    while(len(unseen_nodes) > 0):
        #Select the node with the lowest value in D
        shortest = None
        node = ''

        for temp_node in unseen_nodes:
            if shortest == None:
                shortest = D[temp_node]
                node = temp_node
            elif D[temp_node] < shortest:
                shortest = D[temp_node]
                node = temp_node

        #Remove the selected node from unseen_nodes
        unseen_nodes.remove(node)

        #For each child (ie: connected vertex) of the current node
        for child_node, child_value in graph[node].item():
            if D[child_node] < D[node] + child_value:
                D[child_node] = D[node] + child_value
                #To go to child node, you have to go through node
                P[child_node] = node

    #Set a clean path
    path = []

    #We begin from end
    node = end

    #while we are not arrived at the begining
    while not (node == start):
        if path.count(node) == 0:
            path.insert(0, node) #Insert the predecessor of the current node
            node = P[node] #the current node becomes its predecessor
        else:
            break

    path.insert(0, start) #Finally insert the start vertex
    return path



dijkstra(graph, '0', '5')
