# -*- coding: utf-8 -*-
import random
import Image
from connected_components import ConnectedComponents

class ProcessImage:

    #----------------------------------
    # process image constructor
    #----------------------------------
    def __init__(self, original_image_name):
        
        # parameters
        self.original_image = Image.open(original_image_name)           # original image
        dot, filename, extension = original_image_name.split(".")       # filename and extension
        self.saved_image_name = filename + '_processed.png'             # saved filename
        self.not_background_pixels = 0
        self.total_labels = 0

        # image measures
        self.image_columns = self.original_image.size[0]                # columns
        self.image_lines = self.original_image.size[1]                  # lines
        
        pass
    pass

    #----------------------------------
    # Return not background pixels
    #----------------------------------
    def get_not_background_pixels(self):
        return self.not_background_pixels
        pass
    pass

    #----------------------------------
    # identify labels
    #----------------------------------
    def identify_labels(self):

        # identify connected components
        cc = ConnectedComponents(self.original_image)

        # get generated labels
        self.labels = cc.get_labels()

        # get not background pixels counter
        self.not_background_pixels = cc.get_not_background_pixels()

        # get total labels counter
        self.total_labels = cc.get_total_labels()
        pass
    pass

    #----------------------------------
    # save image
    #----------------------------------
    def save_image(self):

        rnd = random.randint
        
        # generate label colors
        labelColors = [(rnd(0, 255), rnd(0, 255), rnd(0, 255)) for l in range(0,  self.total_labels - 1)]

        # create destination image
        destination_image = Image.new("RGB", (self.image_columns, self.image_lines))
        
        # put pixels in image
        for line in range(self.image_lines):
            for column in range(self.image_columns):                
                if self.labels[line][column] != 0:
                    destination_image.putpixel((column, line), labelColors[self.labels[line][column]- 1])
                pass
            pass
        pass
    
        # save image
        destination_image.save('.' + self.saved_image_name)

    pass
pass
