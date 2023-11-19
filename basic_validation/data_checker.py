import pyhepmc
import numpy as np

# Change run number
hepmc_file = "../../run_data/run_13/Events/run_01/tag_1_pythia8_events.hepmc"

def mev_to_gev(mev):				# pT values are in MeV,
	return mev * 10**-3			    # converting to GeV

with pyhepmc.open(hepmc_file) as f:
    for all_events in f:
        pass

def get_smu(event):
    p = event.numpy.particles
    i = np.abs(p.pid) == 2000013
    i &= p.status == 23
    px = p.px
    py = p.py
    pz = p.pz
    e = p.e
    return [ [ px[i] ], [ py[i] ], [ pz[i] ], [ e[i] ] ]

smuon = get_smu(all_events)

smu_px = smuon[0]
smu_py = smuon[1]
smu_pz = smuon[2]
smu_e = smuon[3]

def get_pT(x, y):
    val = []
    for i in enumerate(x):
        val.append( np.sqrt( (x[i] * x[i]) + (y[i] * y[i]) ) )
    return val

def get_y(e, z):
    return (0.5 * ( np.log( (e + z) / (e - z) ) ) )

def get_phi(x, y):
    return np.arctan2( y / x )

smu_pT = get_pT(smu_px, smu_py)
smu_y = get_y(smu_e, smu_z)
smu_phi = get_phi(smu_px, smu_py)

print('Total number of smuons:',num_particles)

# TABLE 

print('Property\t\t\tmin\t\t\tmax')

# --- pT ---
print('pT\t\t\t',np.min(smu_pT),'\t\t\t',np.max(smu_pT))

# --- eta ---
print('rapidity\t\t\t',np.min(smu_y),'\t\t\t',np.max(smu_y))

# --- phi ---
print('phi\t\t\t',np.min(smu_phi),'\t\t\t',np.max(smu_phi))

