#graph = {'0':{'1':1,'2':4}, '1':{'2':1, '3':3}, '2':{'3':1, '4':5}, '3':{'4':1, '5':8}, '4':{'5':1}}
import self as self

graph = {"0":{"1":1,"2":4}, "1":{"2":1, "3":3}, "2":{"3":1, "4":5}, "3":{"4":1, "5":8}, "4":{"5":1}, "5":{}}

def dijkstra(graph, start, end):
    shortest_path = {}
    predecessors = {}
    unseennodes = graph
    infinity = 9999999
    path = []

    for node in unseennodes:
        shortest_path[node] = infinity
    shortest_path[start] = 0

    while unseennodes:
        minNode = None
        for node in unseennodes:
            if minNode is None:
                minNode = node
            elif shortest_path[node] < shortest_path[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if (weight + shortest_path[minNode] < shortest_path[childNode]):
                shortest_path[childNode] = weight + shortest_path[minNode]
                predecessors[childNode] = minNode
        unseennodes.pop(minNode)

    currentNode = end
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessors[currentNode]
        except KeyError:
            print(KeyError)
            break
    if(shortest_path[end] != infinity):
        print(shortest_path[end])
        #print(path)

dijkstra(graph, "0", "5")