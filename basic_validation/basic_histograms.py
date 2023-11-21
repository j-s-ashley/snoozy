import pyhepmc
import matplotlib.pyplot as plt
import numpy as np

# Change run number
hepmc_file = "../../run_data/run_13/Events/run_01/tag_1_pythia8_events.hepmc"

with pyhepmc.open(hepmc_file) as f:
    for all_events in f:
        pass

# High-efficiency loop over event record
# See scikit-hep.org/pyhepmc/examples/processing.html (Method 3)
def get_smuons(event):
    p = event.numpy.particles
    i = np.abs(p.pid) == 2000013
    i &= p.status == 23 # this will ONLY work on run_13 data (see Issue 1)
    pid = p.pid
    px = p.px
    py = p.py
    pz = p.pz
    e = p.e
    return [ [pid[i]], [px[i]], [py[i]], [pz[i]], [e[i]] ]

def mev_to_gev(mev):				# pT values are in MeV,
	return mev * 10**-3			    # converting to GeV

def get_pT(x, y):
    return mev_to_gev( np.sqrt( (x * x) + (y * y) ) )

def get_phi(x, y):
    return np.arctan2(y / x)

def get_eta(z, e):
    return 0.5 * np.log( (e + z) / (e - z) )

pos_particle_pts = []
pos_particle_etas = []
pos_particle_phis = []

neg_particle_pts = []
neg_particle_etas = []
neg_particle_phis = []

num_particles = 0

smuons = get_smuons(all_events)

# TO DO
#     Loop over smuons to fill pos_, neg_ lists. 
#     (Ought to only take one loop)
#     Look into direct pull for¤0¤0¤0¤0¤0¤0¤0¤0¤0¤0¤0 pT, eta, phi

# HISTOGRAM STUFF
tags = ['Positively charged smuons', 'Negatively charged smuons']

# --- pT ---
pT_num_bins = 20
pTs = [pos_particle_pts, neg_particle_pts]

plt.hist(pTs, bins=pT_num_bins, histtype='bar', label=tags, stacked=True)
#plt.hist(neg_particle_pts, bins=pT_num_bins, histtype='step', label='Negatively charged smuons', stacked=True)

plt.xlabel('pT [GeV]')
plt.ylabel('Number of Smuons')
plt.legend()
plt.title('Smuon pT')

plt.grid(color='c')

plt.savefig('Smuon_pT.pdf', bbox_inches='tight')
plt.savefig('Smuon_pT.png', bbox_inches='tight')
plt.clf()

# --- eta ---
etas = [pos_particle_etas, neg_particle_etas]
plt.hist(etas, histtype='bar', label=tags, stacked=True)
#plt.hist(neg_particle_etas, histtype='step', label='Negatively charged smuons', stacked=True)

plt.xlabel('$\eta$')
plt.ylabel('Number of Smuons')
plt.legend()
plt.title('Smuon $\eta$')

plt.grid(color='c')

plt.savefig('Smuon_eta.pdf', bbox_inches='tight')
plt.savefig('Smuon_eta.png', bbox_inches='tight')
plt.clf()

# --- phi ---
phi_range = ( -(np.pi), np.pi )
phis = [pos_particle_phis, neg_particle_phis]

plt.hist(phis, range=phi_range, histtype='bar', label=tags, stacked=True)
#plt.hist(neg_particle_phis, range=phi_range, histtype='step', label='Negatively charged smuons', stacked=True)

plt.xlabel('$\phi$')
plt.ylabel('Number of Smuons')
plt.legend()
plt.title('Smuon $\phi$')

plt.grid(color='c')

plt.savefig('Smuon_phi.pdf', bbox_inches='tight')
plt.savefig('Smuon_phi.png', bbox_inches='tight')

