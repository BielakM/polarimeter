# Accurate polarimeter based on twisted nematic liquid crystals
This repository provides supplementary material to the following paper by Martin Bielak, Robert Stárek, Vojtěch Krčmarský, Michal Mičuda, and Miroslav Ježek:
**Accurate polarization preparation and measurement using twisted nematic liquid crystal displays** (preprint: [arXiv:2001.07120[quant-ph]](https://arxiv.org/abs/2001.07120))

## Twisted nematic liquid crystal device (TNLCd)
Our polarimeter (TNLC device) is composed of twisted nematic liquid crystal cells and control electronics.
## TNLC cells
We use cells extracted from the LUMEX LCD-S101D14TR display. The protective and polarizing layers must be removed from the displays. The LCD datasheet is available in [LUMEX LCD-S101D14TR datasheet](https://github.com/BielakM/polarimeter/tree/master/TNLCd%20assembly/LUMEX%20LCD-S101D14TR%20datasheet).
## Printed circuit board and electronic driver
Eagle schematic for printed circuit board of the TNLC device including a driver is available in [TNLC dev. PCB](https://github.com/BielakM/polarimeter/tree/master/TNLCd%20assembly/TNLCd%20PCB).
## Polarization analysis
Maximum likelihood reconstruction example using TNLCd is available in [TNLCd_tomography.ipynb](https://github.com/BielakM/polarimeter/blob/master/MaxLik%20polarization%20tomography/TNLCd_tomography.ipynb).
In the folder [Polarization_analysis_simulation](https://github.com/BielakM/polarimeter/tree/master/MaxLik%20polarization%20tomography) we show an examples of reconstruction using waveplates and the TNLC device, including the TNLC device model.
## TNLCd specification
Detailed characterization of the devices are included [TNLCd_specs.md](https://github.com/BielakM/polarimeter/blob/master/Data/TNLCd%20calibration%20sheet/TNLCd_specs.md).
### Transition times analysis
Analysis of the dependence of the transition times on the voltage step for TNLCd "myID_01" is available in [TNLCdanal.py](https://github.com/BielakM/polarimeter/blob/master/Data/TLNCd%20transition%20time%20analysis/TNLCdanal.py). Dependence on the largest voltage step and correspondent transition time are depicted in [transitionalanalysis.png](https://github.com/BielakM/polarimeter/blob/master/Data/TLNCd%20transition%20time%20analysis/transitionanalysis.png) where label "HV" stands for the transition from voltages correspondent with H projection to voltages equal for the V projection etc.
