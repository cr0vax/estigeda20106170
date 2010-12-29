import random
import Image

class ConnectedComponents:

    linked = []
    image = []

    
    def __init__(self, original_image_name):

        print 'aqui'
        # parameters
        self.original_image = Image.open(original_image_name)
        filename, extension = original_image_name.split(".", 1)
        self.saved_image_name = filename + '_altered.' + extension

        # image measures
        self.image_columns = self.original_image.size[0]
        self.image_lines = self.original_image.size[1]

        # initialize labels matrix
        self.labels = [[0 for col in range(self.image_columns)] for row in range(self.image_lines)]

    pass

    def identify_components(self):
        print 'identify_components'
        # first pass
        self.first_pass()
        
        # second pass
        self.second_pass()

        # save image
        self.save_image()

    pass

    #print 'Image_Columns: %d Image_Lines: %d' % (image_columns, image_lines)

    #----------------------------------
    # save image
    #----------------------------------
    def save_image(self):
        print 'save_image'

        rnd = random.randint
        # generate label colors
        labelColors = [(rnd(0, 255), rnd(0, 255), rnd(0, 255)) for l in range(0,  self.nextLabel)]
        labelColors[0] = (0,0,0)

        # put pixels in image
        for line in range(self.image_lines):
            for column in range(self.image_columns):
                    
                self.original_image.putpixel((column, line), labelColors[self.labels[line][column]])
            pass
        pass

        # save image
        self.original_image.save(self.saved_image_name)

    pass
        
    #----------------------------------
    # runs first pass to detect connected components
    #----------------------------------
    def first_pass(self):

        self.nextLabel = 1
        print 'first_pass'
        for line in range(self.image_lines):
            for column in range(self.image_columns):
                pixel = (column, line)
                r, g, b = self.original_image.getpixel(pixel)
                
                background = self.is_background(r, g, b)

                # if it's not background
                if (background is False):
                    #print 'C:%d  L:%d  B:%d' % (column, line, background)

                    # check if there are neighbors
                    neighbor_labels = self.has_neighbors(line, column)

                    # if there are no neighbors
                    if len(neighbor_labels) == 0:
                        # linked[nextLabel] = 
                        self.labels[line][column] = self.nextLabel
                        self.nextLabel = self.nextLabel + 1
                    else:
                        # neighbors were found
                        #print neighbor_labels
                        #print min(neighbor_labels)
                        self.labels[line][column] = min(neighbor_labels)
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
        pass
    pass

    #----------------------------------
    # check if it's background based on
    # rgb color of the pixel
    #
    # r - RED value
    # g - GREEN value
    # b - BLUE value
    # returns true if it's classified as background
    #----------------------------------
    def is_background(self, r, g, b):

        # checks if it's black
        if (r + g + b < 100):
            background = False
            pass
        else:
            background = True
        pass

        # return
        return background
    pass

    #----------------------------------
    # checks if the pixel has neighbors
    #
    # image     - the image itself
    # line      - line of the pixel
    # column    - column of the pixel
    #----------------------------------
    def has_neighbors(self, line, column):

        # LIXO
        #print 'has_neighbors l:%d c:%d' % (line, column)
        neighbor_labels = []

        # same line
        if column != 0:
            # neighbor_W
            neighbor_W = self.labels[line][column-1]

            if neighbor_W != 0:
                neighbor_labels.append(neighbor_W)
            pass
        pass

        # above line
        if line != 0:
            # neighbor_N
            neighbor_N = self.labels[line-1][column]

            if neighbor_N != 0:
                neighbor_labels.append(neighbor_N)
                
            # neighbor_NE
            neighbor_NE = self.labels[line-1][column+1]

            if neighbor_NE != 0:
                neighbor_labels.append(neighbor_NE)
            
            if column > 0:
                # neighbor_NW
                neighbor_NW = self.labels[line-1][column-1]

                if neighbor_NW != 0:
                    neighbor_labels.append(neighbor_NW)
                pass
            pass
        pass

        # return
        if sum(neighbor_labels) > 0:
            return neighbor_labels
        else:
            return []
        pass
    pass
pass
