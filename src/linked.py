# -*- coding: utf-8 -*-
from label import Label

class Linked:

    def __init__(self):
        
        self.equivalences = []
        pass
    pass


    #----------------------------------
    # create a new set
    #
    # label_to_add  - label to be added
    #----------------------------------
    def make_set(self, label_to_add):

        # create new set with element label_to_add
        lbl = Label(label_to_add, 0)

        # add set to equivalences list
        self.equivalences.append(lbl)

        pass
    pass

    #----------------------------------
    # joins sets of identified neighbors
    #
    # neighbors     - set containing neighbor labels found
    #----------------------------------
    def union(self, labelx, labely):
        lblx = self.equivalences[labelx-1]
        lbly = self.equivalences[labely-1]

        self.link(self.find_set(lblx), self.find_set(lbly))
    pass

    #----------------------------------
    # links 2 labels
    #
    # labelx - label object to be linked with labely
    # labely - label object to be linked with labelx
    #----------------------------------
    def link(self, labelx, labely):

        if labelx.get_rank() > labely.get_rank():
            labely.set_parent(labelx)
            pass
        else:
            labelx.set_parent(labely)

            if labelx.get_rank() == labely.get_rank():
                labely.set_rank(labely.get_rank() + 1)
                pass
            pass
        pass
    pass

    #----------------------------------
    # Finds the root of the label
    #
    # label_to_find - label to be found
    # return        - parent of label to be found
    #----------------------------------
    def find_set(self, label_to_find):
        
        if label_to_find != label_to_find.get_parent():
            label_to_find.set_parent(self.find_set(label_to_find.get_parent()))
                                     
        return label_to_find.get_parent()
                                     
        pass
    pass

    #----------------------------------
    # Finds equivalent label
    #
    # label_to_find - label to be found
    # return        - label
    #----------------------------------
    def find_minimum(self, label_to_find):

        lbl = self.find_set(self.equivalences[label_to_find - 1])
                                     
        return lbl.get_parent()
                                     
        pass
    pass

pass
