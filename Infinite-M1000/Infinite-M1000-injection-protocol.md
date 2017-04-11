# Infinite M1000 Injection Protocol
Link to [Infinite M1000 Manual](https://drive.google.com/a/choderalab.org/file/d/0BykO-ZGQb9DHa1NmOGpkLThpZ2c/view?usp=sharing)  

Infinite injector module can be used for kinetic binding assays. Here, I will describe general protocol for using injector module and its maintanence.

Since we don't use injector module frequently Tecan recommended us to leave the tubings empty when the instrument is not in use. So when we want to set up with a new experiment we have to start with priming.
![injector_module](https://cloud.githubusercontent.com/assets/8997658/24927948/a4edb618-1ece-11e7-86f0-207840af27aa.png)
Fig 1. Components of Infinite injector module.

**WARNING!** Never wash, prime or backflush when injector carrier is in Infinite Injector Port! Change carrier to service position first. 
* **Priming** refers to filling the tubing of the module with source liquid. It should be done before washing to fill the tubes with water and before running a script to fill the tubes with reagent.  
* **Washing** refers to pumping water through tubing and injectors to clean the system. Washing of both injectors with water must be done before and after running each experiment script. 
* **Backflush** refers to pumping liquid left in tubing back to reagent container.

### Stepwise protocol for using Infinite injectors
1. **Take injector carrier to service position**
    As in Fig 1 (left), put a waste beaker under.
 
2. **Prime with water**
    Fill both channel A and B bottles with MilliQ water.
    Insert injector tubes to bottles.
    Start iControl software and use Settings>Injector window to control
priming and washing.
![image](https://cloud.githubusercontent.com/assets/8997658/24928669/363342c6-1ed1-11e7-990d-5e3a4ff4249a.png)
    Prime with 1000 uL volume and 200 ul/sec speed.
3. **Wash with water (10 cycle)**
    Wash both channels with 10 cycles of 1000 uL water and 200 ul/sec speed.
4. **Prime with reagent**
    Insert the reagent container (microfuge or falcon tube) to pump A or B.
    Calculate enough reagent volume to cover 100 uL tubing dead-volume, priming volume and injection volume of the experiment.
    Secure with holder strip.
    Insert injector tube.
![bottles](https://cloud.githubusercontent.com/assets/8997658/24927945/a268d8d2-1ece-11e7-9894-5ed1549a0288.png)
    Prime with 1000 uL volume and 200 ul/sec speed.
    You shouldn't see any bubbles at the end of priming.
5. **Insert injector carrier into Infinite through injector port.**
    Shown in Fig 1 (right).
6. **Switch iControl output format to Excel Workbook.**
    You must change destination option in Settings>Result Presentation>General to "New Workbook". 
    Excel output file is mandatory for any script that has **kinetic cycle** function.  
![image](https://cloud.githubusercontent.com/assets/8997658/24929417/d9d7f064-1ed3-11e7-9be8-8310e8f1f9b1.png)
    If you forget to do this you will get an object instance error about Excel output and the run will be interrupted after the 1st injection.
7. **Prepare and run your script.**
    **Inject** function is for injecting a single well and a "well" strip must preceed "inject" strip.
    **Dispense** function is for injecting a subset of wells in a plate. Enabling "Read time like dispense time" is recommended to aligns Infinite reads to time of injection of each well.
![image](https://cloud.githubusercontent.com/assets/8997658/24929684/ca2fba06-1ed4-11e7-9957-ef837d41aae2.png)
8. **Remove your plate.**
9. **Wipe waste tub in plate tray with kimwipe.**
    Waste tub is the black indented rectangle at the back of plate tray.
    5 uL of liquid before each plate injection gets dispensed here.
10. **After run take the carrier to service position with a waste beaker.**
11. **Backflush liquid left in tubing back to reagent buffer (optional).**
    Useful to save reagent since tubing dead volume is 100 uL.
    Use Settings>Injector>Backflush tab to execute this.
12. **Replace reagent container with water bottle.**
13. **Wash with water (10 cycle).**
    Wash both channels with 10 pump volumes (1 ml/cycle, 10 cycles).
    If you will use the injector module withing 1 week you can leave the instrument after this step, with water inside the tubes.
14. **Short wash to aspirate air.**
    For leaving instrument for longer times than a week, it is better to leave tubing empty. 
    Take out the water bottles and wash again both pumps aspirating air (1-2 cycles only.)
15. **Save your excel output manually.**
16. **Switch back to default iControl output settings.**
    Remember to return destination option in Settings>Result Presentation>General back to "XML output" when you are done. Otherwise this will disrupt other automation scripts.
![image](https://cloud.githubusercontent.com/assets/8997658/24930304/125c765a-1ed7-11e7-96bb-a74f4805c71b.png)
