class Linked:

    def __init__(self):
        
        self.equivalences = []
        pass
    pass

    def find(self, label_to_find):
        return min(self.equivalences[label_to_find - 1])
        pass
    pass

##    function MakeSet(x)
##    x.parent := x
    def make_set(self, label_to_add):
##        print 'make_set'

        # create new set with element label_to_add
        new_set = set()
        new_set.add(label_to_add)

        # add set to equivalences list
        self.equivalences.append(new_set)

        pass
    pass

##    function Union(x, y)
##        xRoot := Find(x)
##        yRoot := Find(y)
##        xRoot.parent := yRoot
##
    def union(self, min_label, neighbors):
        new_set = set()

        # build new set with neighbor elements
        for n in neighbors:
            new_set.add(n)

        for n in neighbors:
            self.equivalences[n-1].update(new_set)
        
        # add elements to equivalences
##        self.equivalences[min_label-1].update(new_set)
##        self.equivalences[max(neighbors) - 1].update(new_set)

##        if max(neighbors) == 7:
##            print 'Linked.union'
##            print neighbors
##            print min_label
##            print new_set
##            print self.equivalences

        pass
    pass

pass
