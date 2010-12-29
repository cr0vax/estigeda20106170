# -*- coding: utf-8 -*-
from connected_components import ConnectedComponents

# LOADER
def main():
    # global parameters
    original_image_name = "ace.jpg"

    # identify image regions using connected components algorithm
    cc = ConnectedComponents(original_image_name)
    cc.identify_components()

if __name__ == "__main__":
    main()
