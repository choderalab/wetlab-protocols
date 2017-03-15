MANUAL PROTOCOL A

A. **Transformation into Rosetta DE3 pLysS cells**			

Adapted from a protocol sent to us from the MacroLab's Chris Jeans. It is adapted slightly from this official protocol:
https://www.med.unc.edu/pharm/sondeklab/files/resource-files/manuels/novagen_competent_cells2

SUMMARY:

With this transformation protocol introduce your plasmid of choice into Rosetta DE3 pLysS cells for protein expression. Co-transformation instructions included.

TIMING: 2 HRs + OVERNIGHT

MATERIALS:

- Plasmid(s)
  - Plasmid with gene destined for overexpression in pET vector (e.g. Src WT kinase domain in pET28a vector) 
  - Plasmid with phosphatase (e.g. YopH in pET coexpression vector)
- Cells
  - Competetent Rosetta2 DE3 pLysS cells from -80ºC
- SOC media
- Plates
  - With appropriate antibiotic for both vectors. (e.g. Kan for the Src plasmid and Spec for the YopH plasmid)
- EVO script
  - `ric20_42_heat`

PROTOCOL:

1.	Allow a tube of 100 uL of Rosetta DE3 pLysS (shelf 2 of -80ºC) competent cells to thaw for **5 minutes on ice**. Run EVO script currently called `ric20_42_heat` to preheat ric20. 
2.	Add 1 uL of each plasmid (at about 10-70 ng/ul) directly to the 100 uL cells on ice(30 ng/uL of p235 #4 plasmid of my diluted aliquot and 30 ng/uL of my diluted YopH aliquot. Now both in ‘Lucelenie’s minipreps box’. ) Double check concentration in Denovix.
3.	Gently flick tube twice to mix, then leave the tube on **ice for 30 min**.
4.	Heat shock the tubes for exactly **30 s in 42ºC** using a ric20 on the EVO (script `ric20_42_heat` has been prepared for this purpose). 
5.	Place cells back on **ice for 3 mins**.
6.	Add 900 uL of 2xYT medium to tubes and incubated them at **37ºC for 1 hour** while shaking.
7.	Leave Kan-Spec plates at 37ºC since the beginning of the protocol. Spread 120 uL of cells onto the plates with a sterile spreader.
8.	Incubate plates **overnight at 37ºC** (there is a plate incubator near Rosen lab: Rm 1717).


NOTES:

 - If colonies do not appear: check that you used the right antiboitics, check temperatures of incubators, or the amount of DNA. In practice it actually seems to be the amount of cells plated that can be the problem! According to Chris Jeans:

> You'll want to set up a few plates with different volumes of cells to get one that gives plenty of well-spaced colonies. Plating around 40 ul of our cells will give maybe 100 colonies.

 - Note that right now with this protocol, we have only gotten 2 colonies in the two attempts it has worked. The second time the amount of medium added to the cells was 700 uL, and 200 uL of the cells were plated. We did not see any colonies when using 80 uL pre-heated SOC media during the one hour incubation. 
