# How to use Caliper LabChip GXII for DNA electrophoresis

Link to [HT DNA User Guide](https://www.bioneer.co.kr/literatures/manual/instrument/LabChip%20GX%20HT%20DNA%20USER%20GUIDE%20VERSION%202.pdf)  
Link to [LabChip® GX DNA Quick Guide](https://www.perkinelmer.com/lab-solutions/resources/docs/44-161519GDE_DNA_5K_Quick_Guide.pdf)

### Materials:
- Blue HT DNA Express LabChip (Perkin Elmer) - stored in 4°C fridge
- HT DNA Express Reagent Kit (Perkin Elmer)  - stored in 4°C fridge
- Caliper cloth wipe - wetlab drawer or Caliper box
- 2 ml 70% isopropanol -  stored in solvent cabinet
- Perkin Elmer 0.2 mL Ladder Tube - stored in Caliper box
- Perkin Elmer Buffer Tube - stored in Caliper box
- DNA samples (2 µL each)
- 1X DNA Sample buffer - solution DNA is stored in prior to electrophoresis; often H20 or Elution Buffer (EB)
- Sample plate: 4ti-0960, 96 well PCR plate (purple) 
## 


## Chip preparation

1. Take out blue HT DNA LabChip and HT 5K DNA express Reagent Kit from 4°C fridge and let equilibriate to room temperature for 30 minutes.
2. Follow DNA Chip Preparation instructions found below from the LabChip® GX DNA Quick Guide and use the reverse pipetting technique to avoid bubbles:	
<img width="704" alt="screen shot 2017-04-06 at 4 21 09 pm" src="https://github.com/choderalab/wetlab-protocols/blob/Caliper_DNA_Chip_Protocol/Caliper-LabChip-GXII/images/image1.png">  

* Numbers in wells indicates volume of reagent in µL which needs to be added to each well. 
* Label the reagents with opening date and also label remaining Gel-dye and destaining solutions since they can be reused within 3 weeks of preparation.

3. Store HT DNA Express Reagent Kit in 4°C fridge. HT 5K DNA Express Reagent Kit contains the reagents to run three chip preparations. Each chip preparation is enough to run a 96-well plate. 

## Sample, ladder and buffer preparation 
1. In the provided 0.2 mL Ladder Tube, add 12 µL DNA Ladder to 108 µL of your 1X DNA sample buffer. (This 1X DNA sample buffer is the solution the DNA is currently stored in, most likely H20 or EB)
2. Add 750 µL of your 1X DNA sample buffer to the provided Buffer Tube.
3. Prepare the DNA samples directly onto the 4ti-0960 plate. After using the nanodrop to find the concentrations of your DNA insert, you should dilute your DNA samples to the recommended concentration of 0.25 ng/µL – 50 ng/µL in the 1X DNA sample buffer. 
* Recommended sample volumes are 25 µL for a 384-well plate or 40 µL for a 96-well plate.

## Inserting chip and samples to instrument
![insert_samples](https://cloud.githubusercontent.com/assets/8997658/24775584/89bc89f0-1aeb-11e7-9e15-bc69856f63ef.png)

* Step 3: After pressing **CHIP** botton, the cartridge (black rectangle) should eject itself half-way out. If it doesn't eject, wait until the movement is finished and pull gently to eject the cartridge fully. 
* Step 4: 
	* Press the cartridge latch (in the front of cartridge) up until the upper flap is released and you can open the cartridge.
	* Insert the chip making sure sipper goes through the hole in the cartridge and press the chip into place completely before closing the cover. 
	* Press down to lock the latch in place.
	* Push the cartridge into the instrument.
	
	
![insert_chip_small](https://cloud.githubusercontent.com/assets/8997658/24804010/0bc59a4c-1b7b-11e7-9138-47e267b01873.png)

## Running the electrophoresis
Connect to Caliper PC with TeamViewer via Momentum PC.  
	IP: 10.0.1.15  
	Username: caliper  
	Password: password  
1. Start the LabChip GX software.
2. On the main screen, click on the Run button in the upper left corner of the LabChip GX Software.
3. The Start Run dialog box will pop up with tabs listed as Output, Run and Advanced.
4. In the Run Tab, select the appropriate assay type, wells containing samples, operator name, and plate name.  
For HT DNA assays appropriate assay types are:  
	- HT DNA 1K: For sizing of DNA fragments in 25 to 1000 base pair range.
	- HT DNA 5K: For sizing of DNA fragments in 100 to 5000 base pair range. Fastest analysis time
per sample.
	- HT DNA 12K: For sizing of DNA fragments in 100 to 12000 base pair range.
5. In the Output Tab select the destination of the file, the filename convention and any additional data to
autoexport.
6. In the Advanced Tab, select the number of times each well is sampled, the inclusion of any sample names
and any expected peaks.
7. Click Start to begin the run.

* It takes 5 minutes to prime the gel and 10 minutes to run 10 samples and a ladder sample (shown below).
<img width="696" alt="screen shot 2017-04-06 at 4 48 09 pm" src="https://github.com/choderalab/wetlab-protocols/blob/Caliper_DNA_Chip_Protocol/Caliper-LabChip-GXII/images/image2.png">


## Clean-up and storage

* Although not recommended by the vendor, the DNA Chip can be reused with the remaining reagents overnight in 4C fridge to use the next day. If less than a full plate of samples were run, there is usually enough reagent left to run another electrophoresis run. The chip needs to be primed and used the next day. After two days of usage, the chip must be properly cleaned and washed (described below) before long time storage.

After use, the chip must be cleaned, washed and stored in the chip container.
1. Aspirate the reagents from each well of the chip.
2. Each active well (1, 3, 4, 7, 8, and 10) should be rinsed and aspirated twice, using millipore water.
3. Add 100 µL of HT DNA Storage Buffer (white cap) found in the HT DNA Express Reagent Kit to all the active wells.
4. **Run WASH:** Place the chip in the LabChip GX instrument and click the Wash button in the left corner of the LabChip
GX Software. (This wash program should run for 5 minutes. If longer, stop the program and restart the wash program.)
5. Remove the chip from the instrument and place it in its plastic storage container. Add 100 uL of Storage Buffer to well 1. Cover the wells with parafilm to prevent buffer evaporation and store at 4 °C. 
* Storage of a chip with dry wells may cause it to become clogged. 
