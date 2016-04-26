# This program prompts user for concentration, molecular_weight and desired molarity
# and outputs the amount of volume needed for the desired molarity.

# Get molecular_weight and extinction coefficient from Peanut.
# Get concentration from the Denovix in mg/mL.

# Src WT: MW 32689.6 Da, epsilon 52370 M^-1 cm^-1 from Sept. 3 2014
# Src T338I: MW 33,507.5 Da, epsilon 52370 M^-1 cm^-1
# Abl D382N: MW 33273.1 Da, epsilon 62340 M^-1 cm^-1 => Cys residues reduced
# Abl D382N/T334I: MW 33285.2, epsilon 62340 M^-1 cm^-1 => Cys residues reduced
# p38 MK14: MW 41293.2 Da, 49850 M^-1 cm^-1 => Cys residues reduced
# CAII bovine: MW 29113.7 Da, 50420 M^-1 cm^-1

Src_WT = 32689.6
Src_T338I = 33507.5
Abl_D382N = 33273.1
Abl_D382N_T334I = 33285.2
p38_MK14 = 41293.2
CAII_bovine = 29113.7

concentration = input("What is the concentration of the protein in mg/mL? ")
molecular_weight = input("What is the name or molecular weight of the protein? ")
molarity_input = input("At what concentration you need the protein, 1 uM or 0.5 uM (molarity)? ")
molarity_2 = molarity_input * 0.0000010

molarity_1 = (concentration / molecular_weight)
volume_1 = round(((0.014 * molarity_2 / molarity_1) * 1000000), 1) 
buffer_1000 = round(1000 - volume_1) 

print "You will need %r uL of your protein and 13.%r mL of buffer for it to be at %r uM." % (
    volume_1, buffer_1000, molarity_input)