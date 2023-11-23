# snoozy
Second version of a basic particle physics simulation and data analysis sandbox.
Version one caught fire.

Smuon generation via [MadGraph](https://madgraph.phys.ucl.ac.be) (showering via [Pythia8](https://pythia.org)), data parsing using [LHEReader](https://pypi.org/project/lhereader/), [PyLHE](https://pypi.org/project/pylhe), and [PyHEPMC](https://pypi.org/project/pyhepmc/).
Data visualization with [Matplotlib](https://matplotlib.org).

For still-smouldering v1 info, see [j-s-ashley/sleeper](https://github.com/j-s-ashley/sleeper).

# Basic Validation
<details>
<summary>basic_histograms.py</summary>

This [file](https://github.com/j-s-ashley/snoozy/blob/validation/basic_validation/basic_histograms.py) reads in the .hepmc file produced in a run and outputs histograms for the run's smuon pT, eta, and phi. 

Dependencies:

* pyhepmc
* matplotlib.pyplot
* numpy

As of November 2023, this is my primary "Did I do the thing?" checker. 

</details>

<details>
<summary>data_checker.py and proton_p.py</summary>

These files are useful for cross checks of data sets. 

[data_checker.py](https://github.com/j-s-ashley/snoozy/blob/validation/basic_validation/data_checker.py) calculates the pT, eta, and phi of signal smuons in a different way than basic_histograms.py. 

Of the files listed in this section, this one is the most likely to be broken.

Dependencies:

* pyhepmc
* numpy

[proton_p.py](https://github.com/j-s-ashley/snoozy/blob/validation/basic_validation/proton_p.py) calculates the center mass energy of the protons involved in the initial collision. This was originally used to confirm that the .hepmc file was providing data in units of MeV.

Dependencies:

* pyhepmc
* particle 
* numpy

</details>

<details>
<summary>pltmv.sh and unpack.sh</summary>

These bash scripts are pure quality of life improvements. I got tired of manually unpacking compressed files from each run and shuffling plots around. I'll probably end up replacing pltmv.sh with a more specific output line in the MadGraph generation process, but for now this works.

</details>
