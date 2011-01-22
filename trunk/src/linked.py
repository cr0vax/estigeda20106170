# -*- coding: utf-8 -*-
class Linked:

    def __init__(self):
        
        self.equivalences = []
        pass
    pass

    #----------------------------------
    # joins sets of identified neighbors
    #
    # label_to_find - label to be found
    # return        - minimum equivalent label for the label to be found
    #----------------------------------
    def find(self, label_to_find):
        return min(self.equivalences[label_to_find - 1])
        pass
    pass

    #----------------------------------
    # create a new set
    #
    # label_to_add  - label to be added
    #----------------------------------
    def make_set(self, label_to_add):

        # create new set with element label_to_add
        new_set = set()
        new_set.add(label_to_add)

        # add set to equivalences list
        self.equivalences.append(new_set)

        pass
    pass

    #----------------------------------
    # joins sets of identified neighbors
    #
    # neighbors     - set containing neighbor labels found
    #----------------------------------
    def union(self, neighbors):
        # prepare set of labels
        new_set = set()

        # build new set with neighbor elements
        for n in neighbors:
            new_set.update(self.equivalences[n-1])

        # add set to all identified labels
        for n in new_set:
            self.equivalences[n-1].update(new_set)
        pass
    pass

pass
