# -*- coding: utf-8 -*-
from linked import Linked

class ConnectedComponents:

    #----------------------------------
    # connected components constructor
    #----------------------------------
    def __init__(self, original_image):

        # image
        self.image = original_image

        # image measures
        self.image_columns = self.image.size[0]                # columns
        self.image_lines = self.image.size[1]                  # lines

        # initilize not background counter
        self.not_background_pixels = 0

        # initialize labels matrix
        self.labels = [[0 for col in range(self.image_columns)] for row in range(self.image_lines)]

        # initialize label equivalences
        self.equivalences = Linked()

        # identify components
        self.identify_components()
    pass

    #----------------------------------
    # return labels
    #----------------------------------
    def get_labels(self):
        return self.labels
    pass

    #----------------------------------
    # return total labels identified
    #----------------------------------
    def get_total_labels(self):
        return self.nextLabel
    pass

    #----------------------------------
    # return not background pixels
    #----------------------------------
    def get_not_background_pixels(self):
        return self.not_background_pixels
    pass

    #----------------------------------
    # Identify components of the image
    #----------------------------------
    def identify_components(self):

        # first pass
        self.first_pass()
        
        # second pass
        self.second_pass()

    pass
        
    #----------------------------------
    # runs first pass to detect connected components
    #----------------------------------
    def first_pass(self):

        # Labels index starting at 1
        self.nextLabel = 1

        for line in range(self.image_lines):
            l = line
            for column in range(self.image_columns):
                c = column
                pixel = (c, l)

                # check if pixel is background
                r, g, b = self.image.getpixel(pixel)
                background = int((r + g + b) / (3.0)) > 200

                # if it's not background
                if (background is False):
                    # increment not background pixels counter
                    self.not_background_pixels = self.not_background_pixels + 1

                    # check if there are neighbors
                    neighbor_labels = self.has_neighbors(l, c)

                    # if there are no neighbors
                    if len(neighbor_labels) == 0:
                        
                        # create label set
                        self.equivalences.make_set(self.nextLabel)
                        self.labels[l][c] = self.nextLabel
                        self.nextLabel = self.nextLabel + 1
                    else:
                        
                        # neighbors were found
                        min_label = min(neighbor_labels)            # get the smaller neighbor
                        self.labels[l][c] = min_label               # mark current record in matrix as min label

                        for i in neighbor_labels:
                            self.equivalences.union(min_label, i)
                    pass
                pass
            pass
        pass
    pass

    #----------------------------------
    # runs second pass to connect connected sets
    #----------------------------------
    def second_pass(self):

        for line in range(self.image_lines):
            for column in range(self.image_columns):

                # not background
                if self.labels[line][column] != 0:
                    # set label with the minimum equivalence
                    self.labels[line][column] = self.equivalences.find_minimum(self.labels[line][column])
                pass
            pass
        pass
    pass

    #----------------------------------
    # checks if the pixel has neighbors
    #
    # line      - line of the pixel
    # column    - column of the pixel
    #----------------------------------
    def has_neighbors(self, line, column):

        # define positions relative to current pixel
        above_line = line - 1
        next_column = column + 1
        previous_column = column - 1

        # set containing neighbor labels
        neighbor_labels = set()

        # same line
        neighbor_W = self.labels[line][previous_column]                 # neighbor_W

        if neighbor_W != 0:
            neighbor_labels.add(neighbor_W)
        pass

        # above line
        if above_line >= 0:

            neighbor_N = self.labels[above_line][column]                # neighbor_N

            if neighbor_N != 0:
                neighbor_labels.add(neighbor_N)

            # previous column
            if (previous_column >= 0):
                neighbor_NW = self.labels[above_line][previous_column]  # neighbor_NW
                if neighbor_NW != 0:
                    neighbor_labels.add(neighbor_NW)
                    pass
                pass
            pass

            # next column
            if (next_column > 0) and (next_column < self.image_columns):
                neighbor_NE = self.labels[above_line][next_column]      # neighbor_NE
                if neighbor_NE != 0:
                    neighbor_labels.add(neighbor_NE)
        pass

        # return
        return neighbor_labels
    pass
pass
