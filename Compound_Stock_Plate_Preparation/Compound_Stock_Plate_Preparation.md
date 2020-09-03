# A simple protocol to create 10mM DMSO stock plates.

This protocol fills 4ti0110 plates with 10mM DMSO stocks. Each well is filled with 100uL of stock solution. The plate then gets sealed (this seal can be pierced in other experiments). 

![alt text](img/compoundsetup.png "Compound_setup.png")

## Relevant Scripts
- Momentum Process: WIP_JDC_PrepareCompoundStockPlates_4ti0110
- Momentum Experiment: E_WIP_JDC_PrepareCompoundStockPlates_4ti0110
- EVO Scripts: WIP_LR_CreateCompoundStockPlates_05oct2015.esc

## Procedure
![alt text](img/EVO_deck.png "EVO_deck.png")

- Run maintenance scripts MAINT_Wash and MAINT_Rehome on EVO.
- Type in barcode information in the WIP_JDC_PrepareCompoundStockPlates_4ti0110 Momentum process.
- Place 1 clean 4ti_0110 (96 well, clear plate) in the Stack 3 of the cytomat (Nest 1). 
- Place 1000uL SBS DiTis in the 43 position of EVO. (Red rectangle) 
- Place the 10mM DMSO stock vial holder (Source Plate) in the 27 postion of EVO. (Purple rectangle)
- Run Momentum Script. E_WIP_JDC_PrepareCompoundStockPlates_4ti0110
- Record waste in waste carboy tally and time Stock Vials spent open in plate stable inventory.

## Alternative scripts
To make only 6 columns:

- Run Momentum Script E_EXP_PrepareCompoundStockPlates_4ti0110
- This uses EVO Script EXP_CreateCompoundStockPlate_6cols.esc

To make only 4 rows and 6 columns:

- Run Momentum Script E_EXP_PrepareCompoundStockPlates_4ti0110_4rows
- This uses EVO Script EXP_CreateCompoundStockPlate_6cols_4rows.esc

To make 8 rows (4 rows x2 for an experiment with 2 proteins, and 4 ligands), 6 columns by default
This uses only 4 vials of ligand, but fills 8 rows.
- Run Momentum Script E_EXP_PrepareCompoundStockPlates_4ti0110_8rows_2proteins
- Use the EVO Script EXP_CreateCompoundStockPlate_8rows_2proteins


## Storage
- Store in room temperature PlateStable.
- Compound stock plates should be kept only for a couple of weeks at most.
