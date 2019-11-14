# **MicroCal PEAQ-ITC Automated**

**Isothermal titration microcalorimetry (ITC)** allows for direct, label-free in-solution measurements of binding affinities and thermodynamics of compounds. This enables the accurate determination of binding constants (KD), reaction stoichiometry (n), enthalpy (ΔH), and entropy (ΔS). Heat is released/absorbed as a result of the redistribution and formation of non-covalent bonds when the interacting molecules go from the free to the bound state which is measured by the ITC instrument.

## **Service Information**

- **Model** Malvern Panalytical MicroCal PEAQ-ITC Automated
- **Serial No.** MAL1175839
- **MSK ID:** _As of 2019 November, there is no MSK ID_
- **Contact:** 1-800-932-0101 option 2; 508-768-6450; <support.us@malvernpanalytical.com>

--------------------------------------------------------------------------------

## **Instrument Breakdown**

### System Overview

![System Overview](https://github.com/choderalab/wetlab-protocols/blob/ITC-SOP-Update/MicroCal%20PEAQ-ITC%20Auto/Primary%20Interior%20Components.png?raw=true) *Source: MicroCal PEAQ-ITC Automated User Manual; Version MAN0575-02-EN-00; page 13

### Primary Interior Components

![Primary Interior Components](https://github.com/choderalab/wetlab-protocols/blob/ITC-SOP-Update/MicroCal%20PEAQ-ITC%20Auto/Primary%20Interior%20Components.png?raw=true) *Source: MicroCal PEAQ-ITC Automated User Manual; Version MAN0575-02-EN-00; page 14

--------------------------------------------------------------------------------

## **Materials**

| Item                                | Supplier            | Part Number           | Purpose                                             |
|:------------------------------------|:--------------------|:----------------------|:----------------------------------------------------|
| D-Tube Dialyzer                     | Novagen             | 71506-3 or 71504-3    | Used in Protein Dialysis                            |
| D-Tube Buoy                         | Novagen             | 71513-3 or 71514-3    | Allow the D-Tube to float in buffer during dialysis |
| 150 mL Rapid-Flow Bottle Top Filter | ThermoFisher        | 290-4520              | To Filter Dialysis Buffer of any particulate        |
| Quantos Dosing Head                 | Metler-Toledo       | QH002-CNMW,QH010-CNMW | Precise dispensing of protein/ligand solids         |
| Dram Vials (amber glass bottles)    | Fisher              | 03-339-23D            | Long-Term storage of Stock solutions                |
| 96 well, 1mL, ITC plate             | Thermo Scientific   | 260251 & 260252       | Consumable used in experiment                       |
| Well plate film, slit seal          | Malvern Panalytical | PQA0001               | Used to cover the ITC Plate after set up            |

### Sample: **Protein Macromolecule -and- Ligand micromolecule**

- **Sample Capacity:** Four 96 Well Plates (384)
- **Sample Volume:** 370 µL
- **Cell Volume:** 200 µL
- **Injection Syringe Volume:** 40 µL

--------------------------------------------------------------------------------

## **Procedures**

### **General Notes**

- Label all bottles (detergent, deionized water, methanol, etc.) with the maker's initials and the date it was changed!
- Leave a note as to when the reference cell was changed and the water runs were done.

  - If changed during maintenance, record on log sheet

- `Use pre-perforated covers on your plates!` Other covers may be too thick and bend the syringes or pieces of the covers may end up getting aspirated and interfere with the experiment.

### **Sample Preparation**

#### Macromolecule Protein Set Up via **Protein Dialysis**

**Phase 1: Dialyze Protein**

1. Order/Prepare the approrpiate ITC Assay buffer via Revo or by hand. Store at 4 ˚C until needed.
2. Pre-wet Novagen D-Tube Dialyzer Midi (MWCO 3.5kDa) [CAT NO. 71506-3; Record LOT] with 800 µL of diH2O and let tube sit ~4 minutes.
3. While the D-Tube Dialyzer was sitting: Dissolve ~5 mg of Macromolecule Protein in 750 µµL of ITC Buffer. Make sure to dissolve the protein completely by slowly pipetting up and down several times, being careful to **not** create bubbles.
4. After a few minutes, remove as much of the 800 µL diH2O as possible from the D-Tube Dialyzer. Then, add the 750 µL of suspended protein to the D-Tube Dialyzer.
5. The screw cap was **CAREFULLY** placed on the D-Tube and **lightly tightened** . The D-Tube is then **carefully** pushed into a foam buoy float so that the foam sat underneath the lip of the tube and the entire dialysis window could still be seen).
6. A beaker filled with ~2L of ITC Assay Buffer, a stir bar, and the D-Tube Dialyzer were placed in the cold room spinning @ 100 rpm for at least 12 hours (overnight).

**Phase 2: Protein Recovery**

1. Remove the Beaker from the cold room the following morning.
2. Carefully, remove as much as dialzyed protein as possible from the D-Tube dialyzer and place into a sterile 1.5 mL eppendorf tube.
3. Spin protein at 4,000 rcf (6526 rpm) for 30 min @ 4 ̊C to remove unfolded protein.
4. Keep the Dialyzed protein on ice and Measure the A280 concentration of the protein (mg/mL) with the Denovix DX11+ Nanodrop using 2 µL of sample.

  - Be sure to use the correct Denovix Presets with the correct Molecular Weight and extinction coefficient for the protein.
  - Take a total of 2 Readings and calculate the average. Utlize the average value to calculate the Molarity of the dialyzed Protein.

5. Calculate the Molarity of the Dialyzed Protein.

  - Molarity=[Concentration]/Molecular Weight

6. Store protein in an amber vial [CAT NO. 03-339-23D] and Label: Contents, date, concentration, intials of creator

`IT IS CRITICAL THAT ALL EXPERIMENTS OCCUR WITHIN THIS DIALYZED ITC ASSAY BUFFER, OTHERWISE THE RESULTS WILL BE SKEWED.` If one runs out of the 2L of ITC Assay Buffer, the entire set up/dialysis procedure needs to be repeated so that all experiments can be performed in the new dialysis buffer

#### Micromolecule Ligand Set Up

**Preperation**

- First, purge the old buffer that was in the Mettler Toledo Quantos lines out of the liquid dosing head with the ITC Assay Buffer (that was not used in the dialysis) several times. Once cleaned, you can hook up the dialysate to the Quantos.
- In addition, Fill a Quantos dosing head (ideally a 2 mL size head) with ligand powder.

  - **At a balance:** tare an empty dosing head
  - **In Z1739 fume hood:** Lay down a "lab bench pad" (to catch accidentally spilled compound) and open the dosing head. Then, carefully open the compound vial, and transfer the contents to the dosing head (use a small spatula to transfer the contents). Close the dosing head securely.

    - Pick up the corners of the lab bench pad and carefully carry back/dispose in the biohazard waste.

  - **Go back to balance:** Place the now filled dosing head on the previously-tared balance and record the mass of the compound contained within the dosing head.

    - Place the dosing head into the dosing head receptacle in the Quantos (making sure it is properly seated on the carrier). Run the **"Write Head" method** to label the dosing head. (More information can be found on this method within the [Mettler Toledo Quantos SOP](https://github.com/choderalab/wetlab-protocols/tree/EAG_SOP-Updates/Standardized_SOP/Wet_Lab_Automation))

**Create Ligand Stock Solution**

1. Utilizing the `GSP stable(04/26/2017)(mg/g)` program on the Quantos Dispense:

  - X g of ligand into Y mL of ITC Dialyzed Buffer.

    - These values are Based on the `choderalab/itctools/itctools/procedures.py` script on GitHub for your specific experiment.

      - _For example_, for the example of measuring the binding affinity between CAII and CBS, 8 g of CBS was used with 14 mL of dialysate.

2. Dissolve the ligand in the ITC Dialyzed Buffer. This may require heavily vortex-ing the solution. If there are still floating particulates in the solution, use the ultrasonic sonicator and place the solution in the bath for ~5-10 minutes.

3. Store the solution following storage recommendations or in the desiccator until needed.

#### Tecan EVO automated Set Up of Plate

Utlizing the `choderalab/itctools/itctools/procedures.py` script, we are able generate two Tecan EVO worklist files (`.gwl`) that can be used to set up a plate for ITC experiments. In addition, an `.csv` spreadhseet is produced that can be uploaded to the MicroCal PEAQ-ITC software that automatically fills in the proper commands for the experiments.

- After uploading the `.gwl` worklists into the EVOWARE software, one must make sure to check the protocol and worktable for possible mistakes. The complete EVOWARE script should run both worklists, then do a 1 minute shake. If concerned about any of the steps in the EVO script/worried about the generated `.gwl` file, it is recommended to run the script with water in all locations before using your actual materials/resources.

  - Current working EVO Script (As of 8 November 2019): `WIP_20191023_ITC_SetUp_EAG_BK` (Script takes ~10-15 minutes per ligand/protein pair)

**Checklist:**

- **Check that the EVO script is correct.**

  - [ ] The `LiHa.gwl` should be added FIRST and then `aLiHa.gwl` is the SECOND worklist.
  - [ ] Make sure there is nothing in the path of the RoMa! (The RoMa moves the ITC Plate from the origin space on the worktable to the inheco.)
  - [ ] There is a 1 minute shake using Inheco 1 (Make sure this is the Inheco that the RoMa moves the plate to.)

- **The physical worktable MATCHES the representation on EVOWARE software.** ![EVO WorkTable](https://github.com/choderalab/wetlab-protocols/blob/ITC-SOP-Update/MicroCal%20PEAQ-ITC%20Auto/Worktable.png?raw=true)

  - [ ] 50 µL DiTi Tips are on Position 1 of Rack at Grid 27.
  - [ ] Source Vial Plate are at Position 2 of Rack at Grid 27.

    - [ ] Position A1 is [Protein]
    - [ ] Position B1 is [Ligand]

      ![Source Vial Holder](https://github.com/choderalab/wetlab-protocols/blob/ITC-SOP-Update/MicroCal%20PEAQ-ITC%20Auto/Source%20Vial%20Holder.png?raw=true)

      _Note:_ THERE IS NO OTHER VIALS IN THE HOLDER. This is important as there is nothing in the way of the RoMa when it moves the ITC plate from the origin location to the inheco.

  - [ ] ITC Destination Plate is at Position 3 of Rack at Grid 43.

### Commonly Used Protocols

The most commonly used script is generated from the [itctools GitHub repository](https://github.com/choderalab/itctools/tree/caii/itctools) (specifically the `experiment.py` script). This python script generates an excel `.xml` spreadsheet that can be imported as an experiment in the MicroCal PEAQ ITC software that automatically defines the cell and syringe sources for each titration series.

- After uploading the `.xml` to the `Experiments` tab on the MicroCal PEAQ-ITC Auto Software, one must make sure to check the finished protocol for possible mistakes.

  **Checklist:**

  - **Set Up Screen is Correct**

    - [ ] Tray Temp is -1 ˚C less than the experiment (Typically 24 ˚C)
    - [ ] Cell Temp is Experiment Temperature (Typically 25 ˚C)
    - [ ] _if used:_ Tube Rack Temp is temperature set to the storage temperature of the protein stored within (Typically 4˚C)

  - **Experiment Tab is Correct**

    - [ ] Experiment has the correct spreadsheet within imported
    - [ ] The correct `General Protocols` are being used (Double check within the `Instrument Set Up` window)

  - When everything looks good, Press `Validate` in toolbar.

    - [ ] Make sure there is enough diH2O, Detergent, and Ethanol present to run the experiment.

      - Reference the window that opens which shows the volume of each liquid consumed and the amount of waste produced by running the experiment.

    - [ ] Make sure there is room within the waste bottle to hold the amount of waste being produced by the experiment

### Calculations

There are only two calculations necessary for the set up/running of an ITC experiment.

**Calculate Molarity of Dialyzed Protein:** Molarity = [Concentration]/molecular_weight

### Interpretation of Results

#### Raw Data

The temperature difference between the sample cell and the reference cell is converted to power and directly read out as raw data. An example of this is shown in the following image (An injection is a )

Each spike, followed by a return to the baseline, is an injection.

#### Results via `itc-tools`

Denote where results are SAVED, type of file (i.e. `.xml`), specific units, if there is a script/tool used to read results, etc. denote all here

--------------------------------------------------------------------------------

## **Quality Control/Preventative Maintenance Protocols**

### **Weekly Maintenance**

It is important to perform weekly maintenance on the MicroCal PEAQ-ITC in order to prevent bacterial growth in the reference cell and clogging of the system lines.

#### Part I: **Refill the Reference Cell**

1. Collect fresh distilled water from the 1745D (wetlab) in a 1.5 mL eppendorf tube.
2. Open Open Tube Rack (Tap `Open Tube Rack` on Touchpad and get the Hamilton Syruinge that is stored there. Close Drawer.
3. Door to instrument (Tap `Open Door` on Touchpad). (Note: Best to also turn on the light within the instrument).
4. Gently insert the syringe into the reference cell until it touches the bottom. Empty the reference cell completely by pulling up on the syringe plunger.
5. Empty the syringe.
6. Pull ~300 µL of **DEGASSED,DISTILLED WATER** into the syringe.
7. Gently refill the cell so that the only bubbles are at the top volume of the syringe. Refil the cell until water spills out over the top of the cell stem.
8. **DISLODGE ANY TRAPPED BUBBLES.** This is IMPORTANT as bubbles can effect the experiments! Dislodging bubbles can be done with several abrupt spurts of the water solution.
9. Lift the tip of the syringe to the cell port (just below the visible portion of the cell port) and remove the excess water solution.
10. Remove the syringe from the reference cell, close/latch the door. Turn off the interior light.
11. Place the glas syringe back into the Tube Rack Drawer.

#### Part II: **Clean the cell**

There are Two Recommended Cleaning Routines:

- Select the `Clean Cell` button in the `System`tab and Run Method.
- Run ITC Run Method: `water`; Automation Method: `Quick Plate`; 1 Sample Group; 1 Sample

  - A water-into-water titration experiment with _at least_ 15 injections of 2 µL each followed by the `Plates Clean` Automation Method.

### **IF THE ITC IS NOT GOING TO BE IN USE FOR SEVERAL WEEKS...** Weekly maintenance can be suspended. As long as the instrument is properly turned off:

1. Remove ALL liquid from the **Reference Cell**
2. Remove ALL liquid from the **Sample Cell** (Select ``)
3. Turn off the instrument (Switch is on the back right)

### Common TroubleShooting

#### Transfer Arm Valve Gets Stuck

**CAUSE:** The valve on the transfer arm connects to waste and comes in contact with the detergent solution (20% Contrad). If the solution appears cloudy, it is too concentrated and needs to be changed immediately; otherwise the too-viscous solution may cause the valve to get stuck.

1. Open ITC software (The instrument will attempt to `home` and fail/show an error. Click `OK` on error.)
2. Open Door to instrument (Tap `Open Door` on Touchpad). The valve causing problems is the furthest rightmost on the back inside of the unit.
3. With a **flathead screwdriver**, unscrew the screws on either side of the valve (Left and right). **Keep the tubes connected to the valve.** Using a pair of **pliers**, twist the silver knobs on top and bottom of the valve until they come loose. Screw the valve back into place and then tighten the silver knobs again. This should realign the valve.

_If Problem Remains:_ There is an older valve near the detergent solution that can be used in case the current one gets stuck and cannot be loosened. (Consult user manual on how to replace.)

#### Initialization & homing fails

**CAUSE:** This can occur from time-to-time (for what feels like little to no reasoning).

1. Shut down the software and turn off the instrument (button is on the bottom back right).
2. Wait ~30 seconds.
3. Turn instrument back on and try again.

_If Problem Remains:_ Refer to the Issue Log, User Manual, or, Contact Malvern Panalytical

### Supplemental Maintenance

| Type of Maintenance      | Frequency          |
|:-------------------------|:-------------------|
| Preventative Maintenance | Yearly (~November) |

### Waste Management/Cleaning

Often, people leave their ITC plates in the room for someone else to dispose. However, we generally just carry them back down to our lab and dispose of them in our waste.

## **References**

- Google Drive Folder of all [ITC Notebooks](https://drive.google.com/drive/folders/1Bi9_VVph2WMIFphzOQZQVk5hD650Lr7V)
- PAPER: [Avoiding accuracy-limiting pitfalls in the study of protein-ligand interactions with isothermal titration calorimetry](https://drive.google.com/open?id=0B075He2poqy1SzZZcktWeGtfV0k)
- [User Manuals](https://drive.google.com/drive/folders/1bBmXvKgpVCpEKrzSJ6JSfZtyGS8SE3Sk)
- [Malvern Learning Center Webpage](https://www.malvernpanalytical.com/en/learn/knowledge-center)
- [Issue Log](https://docs.google.com/document/d/1GzK5D7LE2RcCAvm9taf1UtWvZMfvuvpbdGMtLkL5MhI/edit#)

[3983f2d8]: https://github.com/choderalab/wetlab-protocols/tree/master/Frequent_calculations_during_experiment_preparation "GitHub"
