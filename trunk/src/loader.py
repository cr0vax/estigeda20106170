# -*- coding: utf-8 -*-
import Image
#from graph import graph

#----------------------------------
# check if it's background based on
# rgb color of the pixel
#
# r - RED value
# g - GREEN value
# b - BLUE value
# returns true if it's classified as background
#----------------------------------
def is_background(r, g, b):

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
#def has_neighbors(image_width, pixel_id, line, column):
def has_neighbors(labels, line, column):

##    neighbor_W = pixel_id - 1
##    neighbor_NW = pixe_id - image_width + 1
##    neighbor_N = pixel_id - image_width + 1
##    neighbor_NE = pixel_id - image_width + 1

    # LIXO
    print 'has_neighbors l:%d c:%d' % (line, column)
    neighbor_labels = []

    # same line
    if column != 0:
        # neighbor_W
        neighbor_W = labels[line][column-1]

        if neighbor_W != 0:
            neighbor_labels.append(neighbor_W)
        pass
    pass

    # above line
    if line != 0:
        # neighbor_N
        neighbor_N = labels[line-1][column]

        if neighbor_N != 0:
            neighbor_labels.append(neighbor_N)
            
        # neighbor_NE
        neighbor_NE = labels[line-1][column+1]

        if neighbor_NE != 0:
            neighbor_labels.append(neighbor_NE)
        
        if column > 0:
            # neighbor_NW
            neighbor_NW = labels[line-1][column-1]

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

# LOADER
def main():
    # global parameters
    original_image_name = "original.jpg"
    saved_image_name = "alterado.jpg"
    linked = []
    nextLabel = 1

    ##############################
    # read image
    ##############################
    original_image = Image.open(original_image_name)

    ##############################
    # TODO: identify connected components
    ##############################

    # image measures
    image_columns = original_image.size[0]
    image_lines = original_image.size[1]

    print 'Image_Columns: %d Image_Lines: %d' % (image_columns, image_lines)

    # image labels
    labels = [[0 for col in range(image_columns)] for row in range(image_lines)]
        
    print labels
    ##############################
    # FIRST PASS
    ##############################
    for line in range(image_lines):
        for column in range(image_columns):
            pixel = (column, line)
            r, g, b = original_image.getpixel(pixel)

            background = is_background(r, g, b)

            # LIXO
            print 'L:%d C:%d' % (line, column)

            # if it's not background
            if (background is False):
                #print 'C:%d  L:%d  B:%d' % (column, line, background)

                # check if there are neighbors
                neighbor_labels = has_neighbors(labels, line, column)

                # if there are no neighbors
                if len(neighbor_labels) == 0:
                    # linked[nextLabel] = 
                    labels[line][column] = nextLabel
                    nextLabel = nextLabel + 1
                    pass
                else:
                    # neighbors were found
                    print neighbor_labels
                    print min(neighbor_labels)
                    labels[line][column] = min(neighbor_labels)
                    pass
                pass
            pass
        pass
    pass

    # LIXO
    print labels

    ##############################
    # TODO: SECOND PASS
    ##############################
    
    ##############################
    # save image
    ##############################
    original_image.save(saved_image_name)

if __name__ == "__main__":
    main()
