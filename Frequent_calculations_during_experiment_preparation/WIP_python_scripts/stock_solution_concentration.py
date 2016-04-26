# This program prompts user for the molecular weight of the solute and density of the solvent 
# to create a 10mM stock solution.

bosutinib= 530.45 
bosutinib_isomer= 530.45 
erlotinib= 429.90 
Gefitinib= 446.90 
imatinib = 589.71 
ponatinib= 532.56
dasatinib = 488.01 
diaminoquinazoline = 160.18 


molecular_weight = input("What is the name or molecular weight of the solute? ")
solvent_density  = input("What is the density of the solvent? ")

solute_mass = (0.1 * molecular_weight)
solvent_mass = (10.0 * solvent_density)
solution_concentration = round((solute_mass / solvent_mass), 2)

print "You will need to prepare a solution of %r mg/g to make a 10 mM stock solution of your compound." % (
    solution_concentration)