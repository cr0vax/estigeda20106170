import random
import Image
from linked import Linked

class ConnectedComponents:

    

    def __init__(self, original_image_name):

        # parameters
        self.original_image = Image.open(original_image_name)           # original image
        filename, extension = original_image_name.split(".", 1)         # filename and extension
        self.saved_image_name = filename + '_altered.png'               # saved filename

        # image measures
        self.image_columns = self.original_image.size[0]                # columns
        self.image_lines = self.original_image.size[1]                  # lines

        # initialize labels matrix
        self.labels = [[0 for col in range(self.image_columns)] for row in range(self.image_lines)]

        # initialize label equivalences
        self.equivalences = Linked()
    pass

    def identify_components(self):
        print 'identify_components'

        # first pass
        self.first_pass()

##        self.print_labels()

        #print self.labels

        # second pass
        self.second_pass()

##        self.print_labels()
      
        #print self.labels

        # save image
        self.save_image()

##        print self.equivalences.find(7)

    pass
        
    #----------------------------------
    # runs first pass to detect connected components
    #----------------------------------
    def first_pass(self):
        print 'first_pass'

        # Labels index starting at 1
        nextLabel = 1

        for line in range(self.image_lines):
            for column in range(self.image_columns):
                pixel = (column, line)

                # check if pixel is background
                r, g, b = self.original_image.getpixel(pixel)
                background = (r + g + b > 100)

                # if it's not background
                if (background is False):

                    # check if there are neighbors
                    neighbor_labels = self.has_neighbors(line, column)

                    # if there are no neighbors
                    if len(neighbor_labels) == 0:
                        
                        # create label set
                        self.equivalences.make_set(nextLabel)
                        self.labels[line][column] = nextLabel
                        nextLabel = nextLabel + 1
                    else:
                        
                        # neighbors were found
                        min_label = min(neighbor_labels)                # get the smaller neighbor
                        self.labels[line][column] = min_label           # mark current record in matrix as min label
                        self.equivalences.union(neighbor_labels)
                    pass
                pass
            pass
        pass
    pass

    #----------------------------------
    # runs second pass to connect connected sets
    #----------------------------------
    def second_pass(self):
        print 'second_pass'

        for line in range(self.image_lines):
            for column in range(self.image_columns):

                # not background
                if self.labels[line][column] != 0:
                    # set label with the minimum equivalence
                    self.labels[line][column] = self.equivalences.find(self.labels[line][column])
                pass
            pass
        pass
    pass

    #----------------------------------
    # save image
    #----------------------------------
    def save_image(self):
        print 'save_image'

        rnd = random.randint
        
        # generate label colors
        labelColors = [(rnd(0, 255), rnd(0, 255), rnd(0, 255)) for l in range(0,  len(self.labels))]

        destination_image = Image.new("RGB", (self.image_columns, self.image_lines))
        
        # put pixels in image
        for line in range(self.image_lines):
            for column in range(self.image_columns):                
                if self.labels[line][column] != 0:
                    destination_image.putpixel((column, line), labelColors[self.labels[line][column] - 1])
                    
                    #self.original_image.putpixel((column, line), labelColors[self.labels[line][column] - 1])
                pass
            pass
        pass
    
        # save image
        destination_image.save(self.saved_image_name)

    pass

    #----------------------------------
    # checks if the pixel has neighbors
    #
    # line      - line of the pixel
    # column    - column of the pixel
    #----------------------------------
    def has_neighbors(self, line, column):

        above_line = line - 1
        next_column = column + 1
        previous_column = column - 1

##        print 'al:%d nc:%d pc:%d' % (above_line, next_column, previous_column)

        # LIXO
        #print 'has_neighbors l:%d c:%d' % (line, column)
        neighbor_labels = set()

        # same line
        if previous_column >= 0:
            
            neighbor_W = self.labels[line][previous_column]             # neighbor_W

            if neighbor_W != 0:
                neighbor_labels.add(neighbor_W)
            pass
        pass

        # above line
        if above_line >= 0:

            neighbor_N = self.labels[above_line][column]                # neighbor_N

            if neighbor_N != 0:
                neighbor_labels.add(neighbor_N)

            # next column
            if (next_column >= 0) and (next_column < self.image_columns):
                
                neighbor_NE = self.labels[above_line][next_column]      # neighbor_NE
                if neighbor_NE != 0:
                    neighbor_labels.add(neighbor_NE)

            # previous column
            if previous_column >= 0:
                
                neighbor_NW = self.labels[above_line][previous_column]  # neighbor_NW

                if neighbor_NW != 0:
                    neighbor_labels.add(neighbor_NW)
                pass
            pass
        pass

        # return
        return neighbor_labels
    pass

    def print_labels(self):

        for row in range(len(self.labels)):
            print self.labels[row]
            pass
        pass
    pass
pass