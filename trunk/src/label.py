# -*- coding: utf-8 -*-

class Label:

    #----------------------------------
    # label constructor
    #
    # label - integer value to be set as label
    # rank - integer vaue with rank to be set
    #----------------------------------
    def __init__(self, label, rank):
        self.label = label
        self.rank = rank
        self.parent = self
        pass
    pass

    #----------------------------------
    # set label parent
    #
    # parent - label objecto to be set as parent
    #----------------------------------
    def set_parent(self, parent):
        self.parent = parent
        pass
    pass

    #----------------------------------
    # set label rank
    #
    # rank - integer value with rank to be set
    #----------------------------------
    def set_rank(self, rank):
        self.rank = rank
        pass
    pass

    #----------------------------------
    # get label parent
    #----------------------------------
    def get_parent(self):
        return self.parent
    pass

    #----------------------------------
    # get label rank
    #----------------------------------
    def get_rank(self):
        return self.rank
    pass

    #----------------------------------
    # get label
    #----------------------------------
    def get_label(self):
        return self.label
    pass
pass
