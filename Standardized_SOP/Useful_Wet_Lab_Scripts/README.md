# Useful Wetlab Python Scripts

This is a collection of scripts commonly used within the ChoderaLab wetlab. These scripts are useful in assisting  the set up of different procedures.

## Listed scripts
* **Compound_Stock_Plate_Preparation**
  - This protocol fills 4ti0110 plates with 10mM DMSO stocks. Each well is filled with 100µL of stock solution. The plate then gets sealed (this seal can be pierced in other experiments).
* **Frequent_calculations_during_experiment_preparation**
  - This is a collection of "work in progress" scripts used to quickly calculate different concentrations. Including:
    - **edited_protein_volume_calculation.py**
  		- This program prompts user for concentration, molecular_weight and desired molarity and outputs the amount of volume needed for the desired molarity.
	  		- This program is slightly more expansive then the original (includes more proteins pre-loaded within the code)
    - **protein_volume_calculation.py**
      - The original program used for prompts user for concentration, molecular_weight and desired molarity and outputs the amount of volume needed for the desired molarity.
    - **stock_solution_concentration.py**
      - This program prompts user for the molecular weight of a solute and density of the solvent to create a 10mM stock solution.
