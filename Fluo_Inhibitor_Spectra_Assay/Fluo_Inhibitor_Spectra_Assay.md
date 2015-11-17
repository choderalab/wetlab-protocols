
This protocol fills one plate with alternating rows of Protein in Buffer (1 uM Src) and just Buffer. Each well is 100 uL and dispensed using single pipetting in two 96 well plates. Ligands are then added to rows A, C, E, G in a half log dilution starting from 20 uM using the D300. The rest of the rows are filled with DMSO. The plate then gets shaken to mix, centrifuged and the fluorescence read.

##Relevant Scripts
- Momentum Process: WIP_LRL_FLU_Spectra
- Momentum Experiment: E_WIP_LRL_FLU_Spectra
- EVO Scripts: WIP_LRL_FLU_Spectra_1_2_diff_carrier.esc, WIP_LRL_FLU_Spectra_3_4_diff_carrier.esc, WIP_LRL_FLU_Spectra_5_6_diff_carrier.esc and WIP_LRL_FLU_Spectra_7_8_diff_carrier.esc
- D300 Scripts: LRL_Src_Bos_2rows_1_2 2015-09-11 1048.DATA.xml, LRL_Src_Bos_2rows_3_4 2015-09-15 1029.DATA.xml, LRL_Src_Bos_2rows_5_6 2015-09-15 1030.DATA.xml and LRL_Src_Bos_2rows_5_6 2015-09-15 1030.DATA.xml and LRL_Src_Bos_2rows_7_8 2015-09-15 1031.DATA.xml 
- Infinite Script: EXP_FLU_Spectra_1_2.mdfx, EXP_FLU_Spectra_3_4.mdfx, EXP_FLU_Spectra_5_6.mdfx and EXP_FLU_Spectra_7_8.mdfx

##Procedure
- Prepare 14 mL of 1 µM Src (9.6 should be enough for two experiments, but good to have over) in Kinase Buffer (in fridge).
- Use tube from either -80ºC.
- Spin down (5000 rcf for 10 min at 4C).
- Measure concentration using denovix (Src should be preprogrammed).
- Convert to moles (MW of Src is 32.5 kDa).
- Add appropriate amount to total 14 mL.
- Run maintenance script MAINT_Wash on EVO.
- Load Kinase Buffer into 100 mL trough, Protein into 25 mL trough, fresh D300 chip (Purple rectangle), 50 uL SBS DiTis (red rectangle) and appropriate Compound Stock Plate (Green rectangle).
![alt text](img/EVO_deck.png "EVO_deck.png")
- Place 1 clean 4ti_0234 (96 well, clear) plate in Stack 4 of cytomat (Nest 1).
- Run Momentum Script. Make sure to name the four infinite output files accordingly.
- Infinite results file will be output to Google Drive (choderalab/automation/protocols/infinite/results).
- Using assaytools run xml2png4scans-spectra.py on output xml files.

###Kinase Buffer Instructions (if needed)

To make 2L of 20 mM Tris 0.5 mM TCEP pH 8:

####Materials:
- TCEP: Biosynth C1818 Lot 0000009688 MW 286.65 g/mol
- 1M Tris pH 8: Fisher Bioreagents BP1758-500 Lot 135742
- 1L graduated cylinder
- 2 x 2L glass beaker

####Preparation:
- add 40 mL of 1M Tris pH 8 to graduated cylinder
- add 286.65 mg TCEP to graduated cylinder [actual: 288.2 mg]
- fill up cylinder to 2L with ddH2O (Purelab Ultra)
- add stir bar to graduated cylinder and stir to dissolve TCEP
- transfer everything to 2L glass beaker on stir plate and adjust pH to pH 8 by titration with conc HCl or NaOH [initial pH was ~7.81; final pH was 7.99 after adding 10% NaOH dropwise]
- filter into sterile container