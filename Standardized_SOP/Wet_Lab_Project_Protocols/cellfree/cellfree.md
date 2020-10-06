# A cheaper cell-free expression system



## Background
While current protocols exist to express proteins using cell extract instead of whole, live cells, they tend to be very expensive, as they require high-energy phosphate compounds, as well as the addition of tRNA. This document consolidates several variants of these protocols which include:
- reduced preparation time
- reduced cost of reagents
- substantial (up to 1mg/ml) yield

*NB:* It remains to be tested on human proteins.

## Protocol Preparation

The cell-free protocol described here requires several solutions:

### Buffer A

We currently have this buffer without the TCEP in the 4C refrigerator. It is filtered.

- 10mM Tris–acetate buffer (pH 8.2)
- 14 mM magnesium acetate
- 60 mM potassium glutamate
- 1mM TCEP

*NB:* TCEP has been substituted for the original protocol, which called for 1 mM dithiothreitol (DTT) containing 0.05% (v/v) 2-mercaptoethanol (2-ME).

### Buffer B (Buffer A without TCEP)
- 10mM Tris–acetate buffer (pH 8.2),
- 14 mM magnesium acetate
- 60 mM potassium glutamate

*NB:* Original protocol called for 1mM DTT

### Expression buffer

#### Bulk reagents:
- 240 mM of HEPES-KOH (pH 8.2)
- 90 mM potassium phosphate dibasic (pH 7.2)
- 90 mM of potassium glutamate
- 80 mM of ammonium acetate
- 8 mM of magnesium acetate
- 2 mM of TCEP

#### Precious reagents:
- 60 mM of glucose [cheap, but need to be careful about autoclaving]
- 2.1 mM each of 20 amino acids
- 34 μg/mL of L-5- formyl-5, 6, 7, 8-tetrahydrofolic acid (folinic acid) [1g for $186]
- 1.2 mM AMP
- 0.85 mM GMP,UMP,CMP* [5 g of each for ~$300 total]
- 27% (v/v) of cell-extract (S12 extract)

**Important notes about precious reagents**
- Glucose solutions should always be autoclaves ASAP, as it is easy for other organisms to grow in them.
- On a first pass, we will use an amino acid mix for cell culture.
 - The papers cited indicated that a higher cysteine concentration was helpful.
- Folinic acid appears to be much more soluble than folic acid, hence its usage

## Preparing the cell-free extract:

### Growth of Bacteria.

- Initiate a culture of BL21 DE3 non-pLysS cells in 1.5L autoinduction media
   - Rosetta2 cells are acceptable here as well
   - It's not yet clear whether this should be conducted in a single culture,
   or should use a starter culture of 25 or 50mL.
- Induce with IPTG
   - Induce at OD600=0.6
- Harvest cells mid-log phase (OD600=4.5)

### Preparation of harvested Cells

- Wash cells in Buffer A 3 times
   - suspend in 20mL buffer/g wet cells
   - centrifuge (speed not given)
- Store wet pellets at -80C

### Thawing cells

- Thaw cells at -4C
- Resuspend 10g thawed cells in 12.7mL buffer B
- Disrupt in french press at 20,000psi
   - Alternatively, use sonication
- Centrifuge crude lysate at 12,000rcf for 10 min
- Pre-incubate mixture at 37C for 30 min
- Store aliquots at -80C

## Cell-free protein production:
This section pertains directly to producing protein once all other components are made.

- Aliquot expression buffer into reaction vessels
   - Should these be 1mL in 1.5mL? The only cited quantity was in 15uL
- Add 6.7 μg/mL of DNA of expression construct
- Incubate at 37C for 180min
   - The references cite methods to extend this, which may prove useful.
- Purify protein using relevant technique.


# Citations
- (Kim, et al. Biotechnology and Bioprocess Engineering 2008, 13: 464-469) for the expression
- (Biotechnol. Prog. 2005, 21, 1146−1153) for the initial NMP version
- (Kim, et al. Biotechnol 2006, 126: 554-561.) for preparing the S12 extract
- Kim et al. combined it with the S12 (non-dialyzed) extract.
