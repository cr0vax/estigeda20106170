# -*- coding: utf-8 -*-

class components:
    
    def __init__(self, graph):
        self.set = []               # creates a new empty list of sets
        self.rank = []              # creates a new empty list of ranks
        self.graph = graph
        pass
    pass


##CONNECTED-COMPONENTS(G)
##1 for each vertex v ∈ V[G]
##2 do MAKE-SET(v)
##3 for each edge (u, v) ∈ E[G]
##4 do if FIND-SET(u) = FIND-SET(v)
##5 then UNION(u, v)


    # CONNECTED_COMPONENTS
    #
    # identifies 
    # set_u integer value containing set to be compared
    # set_v integer value containing set to be compared
    # returns true if components are the same
    
    def connected_components(self):

        for vertex in self.graph.get_vertexes:
            make_set(vertex)
            pass
        pass

        # TODO
        for edge in self.graph

        pass
    pass
        

##SAME-COMPONENT(u, v)
##1 if FIND-SET(u) = FIND-SET(v)
##2 then return TRUE
##3 else return FALSE

    # SAME_COMPONENT
    # set_u integer value containing set to be compared
    # set_v integer value containing set to be compared
    # returns true if components are the same
    
    def same_component(self, set_u, set_v):
        if find_set(set_u) = find_set(set_v):
            return true
        else:
            return false
        pass
    pass

##MAKE-SET(x)
##1 p[x] ← x
##2 rank[x] ← 0

    # MAKE_SET
    # set_x integer value containing set to be made

    def make_set(self, set_x):
        self.set[set_x] = set_x
        self.rank[set_x] = 0
        pass
    pass

##UNION(x, y)
##1 LINK(FIND-SET(x), FIND-SET(y))

    # UNION
    # set_x integer value containing set to be found
    # returns a pointer to the representative of the unique set containing set_x

    def union(self, set_x, set_y):
        link(find_set(set_x), find_set(set_y))
        pass
    pass

##LINK(x, y)
##1 if rank[x] > rank[y]
##2 then p[y] ← x
##3 else p[x] ← y
##4 if rank[x] = rank[y]
##5 then rank[y]← rank[y] + 1

    # LINK
    # set_x integer value containing set to be linked
    # set_y integer value containing set to be linked

    def link(self, set_x, set_y):
        if self.rank[set_x] > self.rank[set_y]:
            self.set[set_y] = set_x
            pass
        else:
            self.set[set_x] = set_y
            pass
        pass

        if self.rank[set_x] = self.rank[set_y]:
            self.rank[y] = self.rank[y] + 1
            pass
        pass
    pass

##The FIND-SET procedure with path compression is quite simple.
##FIND-SET(x)
##1 if x = p[x]
##2 then p[x] ← FIND-SET(p[x])
##3 return p[x]

    # FIND_SET
    # set_x integer value containing set to be found
    # returns a pointer to the representative of the unique set containing set_x

    def find_set(self, set_x):
        if set_x != self.set[set_x]:
            self.set[set_x] = find_set(self.set[set_x])
            pass
        pass
    
    return self.set[set_x]

pass
