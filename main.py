
import networkx as nx
import matplotlib.pyplot as plt
import random


def select_seed(graph, ch, l=5):
    if ch == 2:
        degree = nx.degree_centrality(graph)
        sort_degree = sorted(degree.items(), reverse=True, key=lambda x: x[1])
        return [x[0] for x in sort_degree][:l]
    elif ch == 1:
        rank = nx.pagerank(graph)
        sort_rank = sorted(rank.items(), reverse=True, key=lambda x: x[1])
        return [x[0] for x in sort_rank][:l]
        
    elif ch == 3:
        rank = nx.betweenness_centrality(graph)
        sort_betweenness = sorted(rank.items(), reverse=True, key=lambda x: x[1])
        return [x[0] for x in sort_betweenness][:l]
        
    elif ch == 4:
        rank = nx.closeness_centrality(graph)
        sort_closeness = sorted(rank.items(), reverse=True, key=lambda x: x[1])
        return [x[0] for x in sort_closeness][:l]
        
    elif ch == 5:
        rank = nx.eigenvector_centrality(graph)
        sort_eigen = sorted(rank.items(), reverse=True, key=lambda x: x[1])
        return [x[0] for x in sort_eigen][:l]
        
    elif ch == 6:
        nx.draw(graph)
        plt.show()
        return []
    else:
        print("Invalid Choice")
        return []


def check1(g, lst):
    inn = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9]
    for i in inn:
        a = independent_cascade(g, lst, inn=i)
        b = independent_cascade(g, lst, inn=i)
        c = independent_cascade(g, lst, inn=i)
        print(i, (len(a)+len(b)+len(c))/3)


def count_neighbours(g, lst):
    inf = []
    for node in lst:
        count = 0
        for n in g.neighbors(node):
            inf.append(n)
            count += 1
        # print("Number of nodes influenced by",node,"is",count)
    return list(set(inf))


def independent_cascade(g, seed, inn=0.5):
    just_inf=list(seed)
    influenced=list(seed)
    while True:
        if len(just_inf) == 0:
            return influenced
        temp = []
        for each in just_inf:
            for each1 in g.neighbors(each):
                ran = random.uniform(0, 1)
                if (ran < inn) and (each1 not in influenced) and (each1 not in temp):
                    temp.append(each1)
        influenced.extend(temp)
        just_inf = temp


G = nx.Graph()
db_name = input("Database name: ")
try:
    d = open(f"Dataset\{db_name}.csv")
    graph = nx.parse_edgelist(d, create_using=G, delimiter=",")
    degree_list = []
    rank_list = []
    print("Choose 1 for Pagerank")
    print("Choose 2 for Degree Centrality")
    print("Choose 3 for Betweenness Centrality")
    print("Choose 4 for Closeness Centrality")
    print("Choose 5 for Eigenvector Centrality")
    print("Choose 6 to draw Graph")

    choice = int(input("Give the number of seed selection: "))
    no_of_seed=0
    if(choice!=6):
        no_of_seed = int(input("No of seed to be selected: "))

    degree_list = select_seed(graph, choice, no_of_seed)
    if len(degree_list) != 0:
        print(degree_list)
        choice1 = input("Please type Y/N to calculate the number nodes influenced.")
        if choice1 == "y" or choice1 == "Y":
            inf = []
            print("Choose 1 for Independent Cascading")
            print("Choose 2 for Count Neighbours")
            choice_f =  int(input())
            if choice_f == 1:
                inf = independent_cascade(graph, degree_list)
            elif choice_f == 2:
                inf = count_neighbours(graph, degree_list)
            else:
                print("Invalid Choice")
            print("Number of influenced nodes:", len(inf))
            # print(inf)
            # print(graph.edges)
except:
    print("Invalid DataSet") 
