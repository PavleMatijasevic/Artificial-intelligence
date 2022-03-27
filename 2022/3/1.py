# astar

import json



# lista povezanosti gradova
with open("cities.json","r") as f:
    adj_list = dict(json.load(f))

#for neighbour, weight in adj_list['Arad']:
#    print(neighbour, weight)


# heuristika za usmeravanje
def h(n):
    H = {
            'Oradea': 380,
            'Zerind': 374,
            'Arad': 366,
            'Timisoara' : 329,
            'Lugoj' : 244,
            'Mehadia' : 241,
            'Drobeta' : 242,
            'Sibiu' : 253,
            'Fagaras': 176,
            'Rimnicu Vilacea' : 193,
            'Pitesti' : 100,
            'Craiova' : 160,
            'Buchares' : 0
    }
    return H[n] if n in H else 400


def get_next_node(open_set, heuristic_guess):
    v = None

    min_distance = float('inf')
    for node in open_set:
        if node in heuristic_guess:
            guess = heuristic_guess[node]
            if guess < min_distance:
                min_distance = guess
                v = node
    return v



def astar(adj_list, start_node, target_node, h):
    # otvoreni skup gde drzim cvorove cije potomke nisam jos sve posetio
    open_set = set([start_node])

    # mapa u kojoj cuvam cvor:roditelj, pocetni nema roditelja!
    parents = {}
    parents[start_node] = None
    
    #indikator zaustavljanja petlje
    path_found = False
    
    # mapa u kojoj cuvam grad:min_rastojanje od pocetnog do njega
    cheapest_path = {v:float('inf') for v in adj_list}
    cheapest_path[start_node] = 0

    heuristic_guess = {v:float('inf') for v in adj_list}
    heuristic_guess[start_node] = h(start_node)

    while len(open_set) > 0:
        current_node = get_next_node(open_set, heuristic_guess)
        if current_node == target_node:
            path_found = True
            break
        open_set.remove(current_node)
        for (neighbour_node, weight) in adj_list[current_node]:
            new_cheapest_path = cheapest_path[current_node] + weight
        
            if new_cheapest_path < cheapest_path[neighbour_node]:
                parents[neighbour_node] = current_node
                cheapest_path[neighbour_node] = new_cheapest_path
                heuristic_guess[neighbour_node] = new_cheapest_path + h(neighbour_node)

                if neighbour_node is not open_set:
                    open_set.add(neighbour_node)
    path = []
    if path_found:
        while target_node is not None:
            path.append(target_node)
            target_node = parents[target_node]
        path.reverse()
    return path


start_node = 'Buchares'
target_node = 'Oradea'
path = astar(adj_list, start_node, target_node, h)
print(path)











