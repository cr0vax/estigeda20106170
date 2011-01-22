# -*- coding: utf-8 -*-
import time
from process_image import ProcessImage

# LOADER
def main():
    # global parameters
    original_image_name = ["01_225x255.jpg",
                           "02_272x272.jpg",
                           "03_300x300.jpg",
                           "04_381x378.jpg",
                           "05_500x500.jpg",
                           "06_630x475.jpg",
                           "07_662x533.jpg",
                           "08_600x600.jpg",
                           "09_755x582.jpg",
                           "10_1024x768.jpg"]

    images_folder = './images/'

    # starts procedure
    print 'Procedure sarted'
    
    # overall stats file
    m = open(images_folder + 'overall_stats.txt','w')
        
    # identify image regions using connected components algorithm
    for a in range(len(original_image_name)):
        lista = []
        f = open(images_folder + original_image_name[a] + '_stats.txt','w')
        print >>f, original_image_name[a]
        print original_image_name[a]

        pi = ProcessImage(images_folder + original_image_name[a])

        for i in range(100):

            # record start time
            start = time.clock()

            # identify images
            pi.identify_labels()

            # record end time
            end = time.clock()

            # add time spent to list
            lista.append(end-start)
            pass
        pass

        # not background pixels
        print >>f, pi.get_not_background_pixels()
        
        # save image
        pi.save_image()

        # print stats to file
        i = 1
        for row in lista:
            print >>f, '%d|%r' % (i, row)
            i = i + 1
        pass

        # calculate mean
        mean = sum(lista) / len(lista)
        print >>m, '%d|%r' % (pi.get_not_background_pixels(), mean)
    pass

    # Ends procedure
    print 'Procedure ended'
pass

if __name__ == "__main__":
    main()
