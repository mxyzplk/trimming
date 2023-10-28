#
import os


class Mass:
    def __init__(self):
        self.label = ""
        self.weight = 0
        self.cg = 0
        self.xcg = 0
        self.ycg = 0
        self.zcg = 0
        self.ixx = 0
        self.iyy = 0
        self.izz = 0
        self.ixy = 0
        self.iyz = 0
        self.ixz = 0
        self.file_path = None

        self.file_path = None

        self.get_dirs()
        self.read_mass()

    def get_dirs(self):
        # Get the current file's directory
        main_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the resources folder
        resources_dir = os.path.join(main_dir, '../resources')
        self.file_path = os.path.join(resources_dir, './mass.txt')

    def read_mass(self):

        with open(self.file_path, 'r') as file:
            for i in range(12):
                line = file.readline()
                temp = line.split()
                match i:
                    case 0:
                        self.label = temp[0]
                    case 1:
                        self.weight = float(temp[0])
                    case 2:
                        self.cg = float(temp[0])
                    case 3:
                        self.xcg = float(temp[0])
                    case 4:
                        self.ycg = float(temp[0])
                    case 5:
                        self.zcg = float(temp[0])
                    case 6:
                        self.ixx = float(temp[0])
                    case 7:
                        self.iyy = float(temp[0])
                    case 8:
                        self.izz = float(temp[0])
                    case 9:
                        self.ixy = float(temp[0])
                    case 10:
                        self.iyz = float(temp[0])
                    case 11:
                        self.ixz = float(temp[0])
