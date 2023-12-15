import pyhepmc
import matplotlib.pyplot as plt
import numpy as np

# Change run number
hepmc_file = "../../run_data/run_17/Events/run_01/tag_1_pythia8_events.hepmc"

pos_particle_pts = []
pos_particle_etas = []
pos_particle_phis = []

neg_particle_pts = []
neg_particle_etas = []
neg_particle_phis = []

def mev_to_gev(mev):				# pT values are in MeV,
	return mev * 10**-3			    # converting to GeV

def get_final_muon_descendant(particle):
    # Get the final state muon descendant of a given particle.
    # Check if the particle itself is a final state muon
    if particle.status == 1 and abs(particle.pid) == 13:
        return particle
    # If the particle has an end vertex, check its descendants recursively
    elif particle.end_vertex:
        for p in particle.end_vertex.particles_out:
            final_muon = get_final_muon_descendant(p)
            if final_muon is not None:
                return final_muon
    # If the particle is not a final state muon and does not have an end vertex, return None
    return None

num_particles = 0

target = 13 # signal particle id
ancestor = 2000013 # id of parent of signal particle

with pyhepmc.open(hepmc_file) as f:
    for event in f:
        for particle in event.particles:
            momentum = particle.momentum
            pt = momentum.pt()
            # Check if the particle is a muon produced by a decaying 2000013 or -2000013
            if abs(particle.pid) == 13 and particle.production_vertex and any(p.pid in [2000013, -2000013] for p in particle.production_vertex.particles_in):
                # Get the final muon descendant of the muon
                final_muon = get_final_muon_descendant(particle)
                if final_muon is not None:
                    if particle.pid == target:
                        num_particles += 1
                        p_pt = mev_to_gev( particle.momentum.pt() )
                        pos_particle_pts.append(p_pt)
                        p_eta = particle.momentum.eta()
                        pos_particle_etas.append(p_eta)
                        p_phi = particle.momentum.phi()
                        pos_particle_phis.append(p_phi)
                    elif particle.pid == -target:
                        num_particles += 1
                        n_pt = mev_to_gev( particle.momentum.pt() )
                        neg_particle_pts.append(n_pt)
                        n_eta = particle.momentum.eta()
                        neg_particle_etas.append(n_eta)
                        n_phi = particle.momentum.phi()
                        neg_particle_phis.append(n_phi)

# HISTOGRAM STUFF
tags = ['Positively charged muons', 'Negatively charged muons']

# --- pT ---
pTs = [pos_particle_pts, neg_particle_pts]

pT_num_bins = np.linspace(0, 3000, 50)

plt.hist(pTs, bins=pT_num_bins, histtype='bar', label=tags, stacked=True, edgecolor='black')

plt.xlabel('pT [GeV]')
plt.ylabel('Number of Muons')
plt.title('Muon pT')

plt.legend()
plt.grid(color='c')

plt.savefig('muon_pT.png', bbox_inches='tight')
plt.clf()

# --- eta ---
etas = [pos_particle_etas, neg_particle_etas]
eta_extrema = max (np.abs( np.min(etas) ), np.max(etas) )
eta_num_bins = np.linspace( -5, 5 )

plt.hist(etas, bins=eta_num_bins, histtype='bar', label=tags, stacked=True, edgecolor='black')

plt.xlabel('$\eta$')
plt.ylabel('Number of Muons')
plt.title('Muon $\eta$')

plt.legend()
plt.grid(color='c')

plt.savefig('muon_eta.png', bbox_inches='tight')
plt.clf()

# --- phi ---
phis = [pos_particle_phis, neg_particle_phis]

phi_num_bins = np.linspace( -np.pi, np.pi, 32 )

plt.hist(phis, bins=phi_num_bins, histtype='bar', label=tags, stacked=True, edgecolor='black')

plt.xlabel('$\phi$')
plt.ylabel('Number of Muons')
plt.title('Muon $\phi$')

plt.legend()
plt.grid(color='c')

plt.savefig('muon_phi.png', bbox_inches='tight')

# --- misc ---
print(num_particles,'muons generated')
print(np.max(pTs),'max pT')
print(eta_extrema,'eta extremum')
print(np.sum(phis) / num_particles,'average phi')
