"""
Homework.py
This is an analyses to measure distances between atoms in a molecule.

"""




import numpy
import os
import sys

def calculate_distance(atom1_coord, atom2_coord):#def is used to create a new function with parameters. We are creating function for distance between atoms.
    """
    This function takes the coordinates of two different atoms and uses the distance formula to calculate the distances between
    the atoms in a molecule.
    """
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    bond_length_12 = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return bond_length_12
def bond_check(distance):   #Use arbitrary parameter, NOT a variale already contained within code. That might confuse reader.
    """
    This function checks to see if a distance between two atoms is between 0 and 1.5, so that the Hydrogen1 to Hydrogen2 Bond is
    not displayed. It returns true or false.
    """
    if distance < 0:
        raise NameError(F'Please input a distance({distance}) Greater than 0. Negative numbers are not valid distances.')
    if distance > 0 and distance < 1.5:
        return True
    else:
        return False

def open_xyz(filename):
    """
    This function is to open an xyz file if given the file name as a parameter.
    """

    file_data = numpy.genfromtxt(fname = file_location, skip_header = 2, dtype = 'unicode' )
    symbols = file_data[:,0]
    coordinates = file_data[: , 1:]
    coordinates = coordinates.astype(numpy.float)
    return symbols, coordinates
#file_location = os.path.join('data', 'water.xyz')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise NameError(F'Incorrect input. Please specify an xyz file to be analyzed')
    file_location = sys.argv[1] #Makes any file in python availble following Water.xyz

    symbols, coord = open_xyz(file_location)
    num_atoms = len(symbols)
    for num1 in range(0, num_atoms):
        for num2 in range(0, num_atoms):
            if num1 < num2:
                bond_length_12 = calculate_distance(coord[num1], coord[num2])
                if bond_check(bond_length_12) is True:
                    print(F'{symbols[num1]} to {symbols[num2]} : {bond_length_12:.3f}')


# In[ ]:
