# -*- coding: utf-8 -*-
#----------------------------------
# Author:   Bruno Moreira
# Date:     27-12-2010
#----------------------------------
# class pixel
# contains information needed to identify the pixel in the image
# and the label it belongs

# line - line of the pixel in the image
# column - column of the pixel in the image
# label - label the pixel belongs
#----------------------------------

class Pixel:

    line = 0
    column = 0
    label = 0
    color = 0

    def __init__(self, line, column, label, color):

        self.line = line
        self.column = column
        self.label = label
        self.color = color
        
        pass
    pass

    # set's the label of the pixel
    # label - integer value of the label
    def set_label(self, label):
        self.label = label
        pass
    pass

    # get's the label of the pixel
    # returns pixel label
    def get_label(self):
        return self.label
    pass

    # get's the color of the pixel
    # returns pixel color
    def get_color(self):
        return self.color
    pass
pass
