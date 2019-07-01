# **Fluorescence Assay- Single Well Format SOP**

### **Assay Design**
Image of the assay design made by Mehtap:

   ![plate_design](https://github.com/choderalab/wetlab-protocols/blob/master/Fluo_Inhibitor_Assay_Single_Well/img/single_well_design.png)
   
   In this image, well A1 contains 0.5 uM of the kinase of interest and well B1 contains an equal volume of buffer. Over the course of 16 D300 dispenses, an inhibitor is dispensed in a logarithmic titration from 8 nM up to 20 uM. This two-well setup is repeated for each ligand:protein pair of interest. 
   
   While in theory, a 96-well plate could support 48 protein:ligand pairs, we have found it best to do each protein:ligand pair in replicate (tipically triplicate). We usually test 4 ligands at a time, as the above image shows. 
   
   One additional caveat: the D300 has a 'priming' command, in which the first dispense of a ligand needs to be greater than 30 nL. For the lowest concentration in our assay (8 nM of a 10 mM ligand stock), this corresponds to 8 nL which is below the priming amount. To compensate for this priming issue, we sacrifice one well of the 96-well plate to dispense a large volume of ligand in each concentration point. 
   
   Below is an example of the typically plate layout we usually use that tests each protein:ligand complex in triplicate and has what we term a 'D300 priming' well:
   
   ![layout](https://github.com/choderalab/wetlab-protocols/blob/master/Fluo_Inhibitor_Assay_Single_Well/img/single_well_layout.png)
   
   Unlike the multiple well format, this format does NOT use DMSO-backfill. 
   
### **Plates Types:**
- Plate material is important! 
- Different plate types have different well bottom materials and/or surface coatings. For example, 4ti-0223 plates have high background fluorescence (~ 2000 rfu) but while 4ti-0234 plates have lower background fluorescence (< 1000 rfu). Corning 3651 plates have high background fluorescence, but are capable of supporting a maximum signal of ~ 50,000 rfu. These have a better signal-to-noise ratio than the 4ti-0223 plates.
- Currently having trouble mixing efficiently in the 384-well plates, so we are using 96-well plates.

### **Buffer:**
- Kinase binding assay buffer from the Revo: 20 mM Tris, 0.5 mM TCEP, pH 8.0 

### **Protein Preparation:**
- We have found that dialyzing the proteins overnight yields smoother fluorescence traces, but dialysis significantly lowers the amount of kinase we have. We usually lose about half of the protein through dialysis. 
- We typically remove an aliquot of protein from the -80C and place the thawed protein in the Mini Dialyzer tubes from Sigma (MWCO 6-8 kDa, CAT 71504-3). The proteins are dialyzed for 2 hours in 1 L of kinase binding assay buffer (made by the Revo). Buffer is exchanged for a fresh 1 L and proteins are left to dialyze overnight. 
- NOTE unlike multiple well assay, protein must be dispensed into the plate BEFORE the Momentum experiment starts. You can write your own script for this or use an existing one.

### **D300 Multiple Dispensing**
- A conversation with Jan Hendrik Prinz, who wrote the drivers for the D300 to be used in EVO, enlightened us to the fact that one D300 script can be written to dispense all concentrations. (Previously we had a separate EVO & D300 script for each concentration point). 
- To use multiple dispensing, we define a separate plate for each concentration point in the D300 script (see image below). The physical layout is the same for each plate, the only thing that changes is the amount of ligand dispensed.
- Once the D300 script has been written, two EVO scripts should be written. The first should have 2 steps for the D300: 1) initialize (this is where the D300 script is selected) 2) Dispense plate blocking. The second script should ONLY have dispense plate blocking. This tricks the D300 into thinking it is dispensing into 16 different plates when in reality it is dispensing into the same plate 16 times. 
- NOTE the D300 fingers do not come out of the cassette until the last 'plate' has been dispensed into. Therefore, if there is any automation issue during the course of the experiment, you will need to use a new cassette since the D300 will have marked these wells as used. 
- NOTE multiple dispensing has timing issues occasionally. It may not dispense after 3-4 hours of carrying out a single script. Keep an eye on each dispense to make sure it is actually dispensing ligand. When it skips, no error is raised so you won't know unless you physically watch it. 

  D300 multiple dispensing plates:
  ![D300_plates](https://github.com/choderalab/wetlab-protocols/blob/master/Fluo_Inhibitor_Assay_Single_Well/img/D300_plates.png)

### **Relevant Scripts**
- EVO:
  - To dispense protein: _WIP_EEG_Kinase_single_wv_protein_dispense.esc_
  - To create compound stockplate: _EXP_CreateCompoundStockPlate_4rows.esc_ (seal plate after running this!)
  - Concentration 1: _WIP_LRL_Kinase_new_single_wv_conc1.esc_ 
  - Concentrations 2-16: _WIP_LRL_Kinase_new_single_wv_conc2_to_16.esc_
- D300: 
  - Use wells 1-4 of a cassette: _EEG_HTFLU_single_well_all_plates_all_wells_1to4_20181024.hpdd_
  - Use wells 5-8 of a cassette: _EEG_HTFLU_single_well_all_plates_all_wells_5to8_20181024.hpdd_
- Infinite:
  - General: _EEG_Kinase_single_wv_20190220.mdfx_
  - For ligands with different fluorescence properties (staurosporine, ponatinib): _EEG_Kinase_single_wv_ima_das_pon_stauro_multiple_gains_20190408.mdfx_
- Momentum Process: _EXP_HT_single_well_binding_assay_D300_multiple_dispensing_ 
- Momentum Experiment: _E_EXP_HT_single_well_binding_assay_D300_multiple_dispensing_

### **Older scripts that do the same/similar thing(s)**
- EVO:
  - To create compound stockplate: _EEG_CreateCompoundStockPlate_4ti0110_4rows_08aug2018.esc_
  - To dispense 16 concentrations of ligand: _WIP_LRL_Kinase_exp_panel_single_wavelength_conc1.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc2.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc3.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc4.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc5.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc6.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc7.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc8.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc9.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc10.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc11.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc12.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc13.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc14.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc15.esc,
  WIP_LRL_Kinase_exp_panel_single_wavelength_conc16.esc_
- D300: _MI_HTFLU_single_well_conc1_20180308.hpdd,
MI_HTFLU_single_well_conc2_20180308.hpdd,
MI_HTFLU_single_well_conc3_20180308.hpdd,
MI_HTFLU_single_well_conc4_20180308.hpdd,
MI_HTFLU_single_well_conc5_20180308.hpdd,
MI_HTFLU_single_well_conc6_20180308.hpdd,
MI_HTFLU_single_well_conc7_20180308.hpdd,
MI_HTFLU_single_well_conc8_20180308.hpdd,
MI_HTFLU_single_well_conc9_20180308.hpdd,
MI_HTFLU_single_well_conc10_20180308.hpdd,
MI_HTFLU_single_well_conc11_20180308.hpdd,
MI_HTFLU_single_well_conc12_20180308.hpdd,
MI_HTFLU_single_well_conc13_20180308.hpdd,
MI_HTFLU_single_well_conc14_20180308.hpdd,
MI_HTFLU_single_well_conc15_20180308.hpdd,
MI_HTFLU_single_well_conc16_20180308.hpdd_,
- Infinite: _WIP_LRL_Kinase_exp_panel_spectra.mdfx,
WIP_LRL_Kinase_exp_panel_spectra_top_only.mdfx,
WIP_EEG_Copy_Kinase_exp_panel_spectra.mdfx_
- Momentum Process: _EXP_HT_single_well_binding_assay_
