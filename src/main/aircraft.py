import os
from mass import Mass
#
#  Example: F-16
#  Source: Brian Stevens & Frank Lewis - Aircraft Control and Simulation
#
#


class Aircraft:
    def __init__(self):
        # Reference Geometry
        self.s = 0
        self.c = 0
        self.b = 0

        # Paths
        self.file_path = None

        self.get_dirs()
        self.read_geometry()

    def get_dirs(self):
        # Get the current file's directory
        main_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the resources folder
        resources_dir = os.path.join(main_dir, '../resources')
        self.file_path = os.path.join(resources_dir, './basic_data.txt')


    def read_geometry(self):
        with open(self.file_path, 'r') as file:
            for i in range(12):
                line = file.readline()
                temp = line.split()
                match i:
                    case 0:
                        self.s = float(temp[0])
                    case 1:
                        self.b = float(temp[0])
                    case 2:
                        self.c = float(temp[0])
