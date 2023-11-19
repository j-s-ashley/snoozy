import pyhepmc
from particle import literals as lp
import numpy as np

hepmc_file = "../../run_data/run_15/Events/run_01/tag_1_pythia8_events.hepmc"

with pyhepmc.open(hepmc_file) as f:
    for all_events in f:
        pass

def sum_energy_of_protons(event):
    p = event.numpy.particles
    ma = np.abs(p.pid) == lp.proton.pdgid
    ma &= p.status == 4
    e = p.e
    return np.sum(e[ma])

print( sum_energy_of_protons(all_events) )
