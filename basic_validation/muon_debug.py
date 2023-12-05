import pyhepmc
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

def is_signal(parents, family, ancestor):
    for p in parents:
        if abs(p.id) == ancestor:
            return True
        if abs(p.id) != family:
            continue
        parents = p.production_vertex.particles_in
    return False

num_particles = 0

family = 13 # signal particle id
ancestor = 2000013 # target parent id

with pyhepmc.open(hepmc_file) as f:
    for i, event in enumerate(f):
        
        # Begin looping over event record
        for particle in event.particles:

            # If the particle is a final-state muon, get parents
            if abs(particle.pid) == family  and particle.status == 1:
                flag = is_signal(particle.production_vertex.particles_in, family, ancestor)

                # If not signal, move on; else, pull data
                if flag == False:
                    continue
                if particle.pid == family:
                    num_particles += 1
                    p_pt = mev_to_gev( particle.momentum.pt() )
                    pos_particle_pts.append(p_pt)
                    p_eta = particle.momentum.eta()
                    pos_particle_etas.append(p_eta)
                    p_phi = particle.momentum.phi()
                    pos_particle_phis.append(p_phi)
                elif particle.pid == -family:
                    num_particles += 1
                    n_pt = mev_to_gev( particle.momentum.pt() )
                    neg_particle_pts.append(n_pt)
                    n_eta = particle.momentum.eta()
                    neg_particle_etas.append(n_eta)
                    n_phi = particle.momentum.phi()
                    neg_particle_phis.append(n_phi)

# --- pT ---
pTs = [pos_particle_pts, neg_particle_pts]

# --- eta ---
etas = [pos_particle_etas, neg_particle_etas]

# --- phi ---
phis = [pos_particle_phis, neg_particle_phis]

# --- misc ---
print(num_particles,'muons generated')

print('properties: [[positive values], [negative values]]')
print(f'pTs: {pTs}')
print(f'etas: {etas}')
print(f'phis: {phis}')
