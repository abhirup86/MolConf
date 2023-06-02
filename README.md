# MolConf
## Molecular Modeling Tools: Identifying Conformers for the 3XV Molecule
This collection of Python scripts provides comprehensive tools for molecular modeling tasks, such as molecular operations, conformer generation, visualization, and energy calculations. In particular, this project focuses on identifying conformers of the 3XV molecule using RDKit and CREST.

## Description
### The package included the following Python scripts:

1. `imports_and_setup.py`: This script includes all necessary Python package imports and sets up the environment for the remaining scripts. 2. `molecular_operations.py` - Contains functions for performing various operations on molecules such as adding, removing, or modifying atoms and bonds.
3. `conformer_generation_visualization.py` - This script generates conformers (different spatial arrangements of atoms) for a given molecule and provides visualization.
4. `energy_calculations_optimizations.py` - Script for computing the potential energy of a molecule and performing energy minimization (also known as geometry optimization) to find the lowest energy conformer.
5. `plot_energy.py` - Uses matplotlib to plot the potential energy of a molecule as a function of certain variables (such as the dihedral angle).

### Jupyter Notebooks
The project also includes a Jupyter notebook, which guides you through the process of identifying conformers of the 3XV molecule. This includes the creation of conformers using RdKit, optimization with XTB GFN2, and a conformer search using CREST.

## Set Up
### Dependencies
RDKit: Generate and manipulate the molecular structures.
py3Dmol: Visualization of molecular structures.
XTB: optimizing conformers.
CREST: For conformer search.
Plotly: Plot of data.
