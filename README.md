# Accurate polarimeter based on twisted nematic liquid crystal displays
This repository provides supplementary material to the following paper by Martin Bielak, Robert Stárek, Vojtěch Krčmarský, Michal Mičuda, and Miroslav Ježek:
**Accurate polarization preparation and measurement using a liquid crystal display** (preprint: [arXiv:2001.07120[quant-ph]](https://arxiv.org/abs/2001.07120))

# TNLC device
Our polarimeter (TNLC device) is composed of twisted nematic liquid crystal cells and control electronics.
## Liquid crystal cells
We use cells from the LUMEX LCD-S101D14TR display. The protective and polarizing layers must be removed from the displays. The LCD datasheet is available in [LUMEX LCD-S101D14TR datasheet](https://github.com/BielakM/polarimeter/tree/master/LUMEX%20LCD-S101D14TR%20datasheet).
## Printed circuit board
Eagle schematic for printed circuit board of the TNLC device including a driver is available in [TNLC dev. PCB](https://github.com/BielakM/polarimeter_DEMO/blob/master/TNLC%20dev.%20PCB).
## Polarization analysis simulation
Maximum likelihood reconstruction example is available in [MaxLik](https://github.com/BielakM/polarimeter/tree/master/MaxLik).
In the file [Polarization_analysis_simulation](https://github.com/BielakM/polarimeter/tree/master/Polarization_analysis_simulation)we show an example of reconstruction using waveplates and TNLC device including the TNLC device model and propagation through the system.
