#This script can be used to calculate the amount of solid (in g) needed to make a buffer at a desired pH.

#The user will be prompted for the desired pH of the solution, the pKa of the conjugate acid/base pair at the desired temperature, the desired concentration of the solution, and the molecular weight of the compounds.

#user defined variables
pH = float(input("What is the desired pH of your buffer?"))
pH_ = float(pH)
pKa = float(input("What is the pKa of the conjugate acid/base pair at the temperature of your buffer?"))
pKa_ = float(pKa)
conc = float(input("What is the desired concentration of your buffer (in M)?"))
conc_ = float(conc)

#MWinfo for conjugate acid/base (if loop accepts names or numbers)
#HA is the conjugate acid
#A- is the conjugate base
MW_HA = input("What is the name or molecular weight of the acid (ie sodium phosphate monobasic dihydrate)?")
if MW_HA == "sodium phosphate monobasic dihydrate":
    MW_HA = 156
elif MW_HA == "sodium phosphate dibasic anhydrous":
    MW_HA = 141.96
else:
    MW_HA = float(MW_HA)
MW_A = input("What is the name or molecular weight of the base (ie sodium phosphate dibasic anhydrous)?")
if MW_A == "sodium phosphate monobasic dihydrate":
    MW_A = 156
elif MW_A == "sodium phosphate dibasic anhydrous":
    MW_A = 141.96
else:
    MW_A = float(MW_HA)

#Henderson-Hasselbalch equation general form: pH = pKa + log([A-]/[HA])
#Henderson-Hasselbalch equation solved for [A-]/[HA] (named "raw_ratio")
raw_ratio = 10**(pH_ - pKa_)

#Find relative amounts of A- and HA assuming that A- = raw_ratio and HA = 1 (from [A-]/[HA])
raw_A= float(raw_ratio)
raw_HA = 1
raw_total = raw_A + raw_HA

A = raw_A/raw_total
HA = raw_HA/raw_total

#Find desired molarity of A- and HA
M_A = conc_ * A
M_HA = conc_ * HA

#Find moles (assuming 1L of buffer)
mol_A = M_A * 1
mol_HA = M_HA * 1

#Find g using MW
g_A = mol_A * MW_A
g_HA = mol_HA * MW_HA

string = "You will need {a} g/L of A- and {b} g/L of HA to make a buffer of {c}M at pH {d}.".format(a = round(g_A , 4), b = round(g_HA , 4), c = conc_, d = pH_)
print (string)
