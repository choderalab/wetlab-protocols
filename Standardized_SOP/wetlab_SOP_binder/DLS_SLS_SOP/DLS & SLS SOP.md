# **Dynamic/Static Light Scattering SOP**

### **Instrument:** 
   Wyatt DynaPro III (located in the Heller Lab on the 18th floor, password Wyatt123)
### **Software:** 
  Dynamics 7.8.0.26

### **Plates:**
- Can use 384-well or 96-well plates
- The settings for this SOP were done using a 96-well plate (the 4ti-0223), defined in the program as **96 Flat Bottom Greiner Oct 2018**
- To use the 96-well plate, **_make sure to use the 9.0 mm adapter!_** Otherwise, the other adapter is fine (7.5 mm?)
- Minimum volume for 96 well plate is 60uL.
- Image of the defined settings:

   ![plate](https://github.com/choderalab/wetlab-protocols/blob/master/wetlab_SOP_binder/DLS_SLS_SOP/images/plate.png)

### **Settings Tabs:**
#### **Fixed Parameters**
- We weren't concerned about particle size (just that particles were forming) so we changed the peak radius low cutoff from 0.5 to 0.1. This helps detect smaller particles, which Mehtap had found useful in previous experiments.
- Image of the settings for this tab:

   ![fixed_params](https://github.com/choderalab/wetlab-protocols/blob/master/wetlab_SOP_binder/DLS_SLS_SOP/images/fixed_params.png)

#### **Instrument Parameters:**
- We weren't worried about our samples evaporating/absorbing water so we read the plates without any seal or oil droplets.
- We tried various acquisition times and found that 5 second acquisitions worked best for our purpose. Hanan suggests using shorter acquisition time, 1 second, to look for nanoparticle formation. 
- We did 5 acquisitions of 5 seconds each for each well. 
- We got the best data when we turned auto-attenuation on. This enables the instrument to adjust the laser power during the experiment. **Note:** We got an error when using auto-attenuation in the experiment designer tab, which is one reason we switched to using Event Schedule (described below).
- Our experiment was a fixed temp experiment at 25C
- Image of the settings for this tab:

   ![instrument_params](https://github.com/choderalab/wetlab-protocols/blob/master/wetlab_SOP_binder/DLS_SLS_SOP/images/instrument_params.png)

#### **Sample:**
- We reasoned that our buffer was relatively similar to water/an aqueous solution and that DMSO content had a negligible effect on solvent, so we kept water. 
- The rest of the information here is used to calculate particle size and create correlation plots, which we did not adjust.
- Image of the settings for this tab:

   ![sample](https://github.com/choderalab/wetlab-protocols/blob/master/wetlab_SOP_binder/DLS_SLS_SOP/images/sample.png)

#### **Experiment Designer:**
- This tab we did not use. It is designed for scheduling multiple reads/high-throughput experiments. We got better results with the Event Schedule tab.

#### **Event Schedule:**
- We optimized our protocol with ponatinib, which precipitates in aqueous solution. As a result, we found that we had to set the laser power to 10%, or else an error of 'scattering intensity too high' kept occurring. Enabling auto-attenuation allows the instrument to adjust the laser power for each read to optimize the output for each well. 
- A copy of our protocol:
  - Sets laser power to 10%
  - Enables auto-attenuation
  - Takes 5 acqusitions of 5 seconds each for each well
  - Sets the interior temp of the instrument to 25C
  - Take images of the wells (we used this to confirm if we saw any precipiation on the bottom of the wells)
  - Start at A1
  - Do the following loop 96 times
    - Collect data, label measurement as well #, and move to next well
  - Save data as file name
  - Turn laser power off
- **_IMPORTANT to turn laser off at the end of each experiment!_**
- Image of our protocol:

   ![protocol](https://github.com/choderalab/wetlab-protocols/blob/master/wetlab_SOP_binder/DLS_SLS_SOP/images/protocol.png)
- The above protocol is a preset which can be found in the ChoderaLab folder on the Wyatt computer. 


###### **Links**
**Manual & Notes:** [click here](https://drive.google.com/drive/folders/1Xeypb6MHBMH-DtyhyhJ167ITKI6SkZzM)
