MANUAL PROTOCOL C

C. **Large Scale Protein Purification**

Adapted from:
Seeliger lab Src Expression Protocol.
MacroLab Expression Protocols for p235, p480, p556.

SUMMARY:

This purification protocol describes a two step purification in which your His-tagged protein of choiced is purified from a cell pellet, and the His-tag is removed using TEV protease.

TIMING: ~2 DAYS

MATERIALS:
- Cell pellet from PROTOCOL B
- Centrifuge bottles
- 0.2 µm filter

BUFFERS:

**Nickel Buffer A**
25 mM Tris pH 8.0, 500 mM Na Cl, 5% Glycerol, 20 mM Imidazole

**Nickel Buffer B**
25 mM Tris pH 8.0, 500 mM Na Cl, 5% Glycerol, 400 mM Imidazole

**Desalting Buffer**
25 mM Tris, pH 8.0, 100 mM NaCl, 5% Glycerol, 1 mM DTT (or equiv)

**IEX Buffer A**
25 mM Tris, pH 8.0, 5% Glycerol, 1 mM DTT (or equiv)

**IEX Buffer B**
25 mM Tris, pH 8.0, 1M NaCl, 5% Glycerol, 1 mM DTT (or equiv)

EQUIPMENT: Avestin Homogenizer, NGC BioRad and columns, Caliper GXII and chips and reagents, Centrifuge, Denovix.

This protocol is preceded by Manual Protocol B: Large Scale Protein Expression (1 DAY).

PROTOCOL:

1.	Keep Avestin C3 Homogenizer’s cell compartment at 4ºC the night before using it. Break cells with the homogenizer **3x at ~15 kpsi**. (Be sure to wash and store homogenizer properly.)  Collect a LYSATE sample for a gel.
2.	Spin down cell debris for 40 minutes at 4ºC 30 000 g in SA600 rotor (or equivalent for available rotor). Collect a SUPERNATANT sample for a gel.
3.	Load clarified lysate onto *5mL HisTrap FF Column*, pre-equilibrated with Nickel Buffer A, at 2-3 mL/min. Collect a FLOW THROUGH sample for a gel.
4.	Wash resin with 5 column volumes **Nickel Buffer A**. Collect a WASH sample for a gel. Elute in ‘gradient’ with **Nickel Buffer B**.  Fraction collector will collect NI FRACTIONS, which will subsequently be run on a gel.
5.	Check samples in Caliper. Pool fractions with protein in them. Buffer exchange on *HiPrep 26/10 Desalting Column* into **Desalting Buffer**. Collect a DESALT sample for a gel
6.	Add 1:20 mass ratio TEV protease to pooled samples. Incubate at **overnight for 4ºC** or (RT for 2 hours).
7.	After incubation with TEV filter with 0.2 µm filter. Collect CLEAVED and CLEAVED_FILT samples for a gel. Run samples on the Caliper to check cleavage.
8.	Dilute cleaved protein twofold with **IEX Buffer A**, load samples onto *5 mL Q FF column*, pre-equilibrated in **IEX Buffer A**. Elute with salt gradient (0-50% over 14 column volumes) with **IEX Buffer B**. Fraction collector will collect IEX FRACTIONS. Run fractions on Caliper.
9.	Measure protein concentration in Denovix. Aliquot and freeze protein at -20ºC. 

NOTES:

- We had several problems with the right settings on the BioRad NGC during the first run through of this protocol. The final methods will be noted here when they are error-free. If you are making new scripts be particularly careful of the sample application step: do you have the correct port? are you loading the sample directly onto the column and not the sample loop? have you given the method the correct sample volume?
- Record gel images, and final concentration, and any observations.



