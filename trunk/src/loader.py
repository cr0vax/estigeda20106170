# -*- coding: utf-8 -*-
from connected_components import ConnectedComponents
import time

# LOADER
def main():
    # global parameters
    original_image_name = ["Silver Ball Bearings.jpg"]
##                           "ace.jpg",
##                           "alicate.jpg"]

    # identify image regions using connected components algorithm
    lista = []

    for a in range(len(original_image_name)):
        print original_image_name[a]
        
        for i in range(1):
            start = time.clock()
            cc = ConnectedComponents(original_image_name[a])
            cc.identify_components()
            end = time.clock()

        lista.append(end-start)
        print 'Media: %r' % (sum(lista) / len(lista))

if __name__ == "__main__":
    main()
