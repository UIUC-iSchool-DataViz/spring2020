import numpy as np
import math



# unit conversions
MassOfSun = 2e33 # g
MassOfJupiter = 1.898e30 # g
AUinCM = 1.496e13 # cm
kmincm = 1e5 # cm/km
G = 6.674e-8 # gravitational constant in cm^3 g^-1 s^-2



#---------------------------------------------------




#---------------------------------------------------
# Numerical solution with Hermite
#---------------------------------------------------

# from: http://wiki.tomabel.org/index.php?title=Gravitational_N-body_Problem
def acc(r,m,eps):
    a = np.zeros((len(r),3))
    for i in range(len(r)):
        for j in range(len(r)):
            ra2 = ((r[i,:]-r[j,:])**2).sum()
            if (i != j):
                a[i,:] += -(r[i,:]-r[j,:])*m[j]/(ra2**1.5) 
    return a # return acceleration
 
def Jerks(r,v,m,eps):
    Je = np.zeros((len(r),3))
    for i in range(len(r)):
        for j in range(len(r)):
            if (i != j):
                ra2 = ((r[i,:]-r[j,:])**2).sum() # dot product
                Je[i,:] += - ( (v[i,:]-v[j,:])/ra2**1.5  \
                     - 3.*(((v[i,:]-v[j,:])*(r[i,:]-r[j,:])).sum())/(ra2**2.5) *(r[i,:]-r[j,:]) )* m[j] 
    return Je;
 
def HermiteUpdate(dt, r, v, m):
    a = acc(r, m, 0)          # current acceleration
    adot = Jerks(r,v,m,0)     # current jerks
    rp = r + dt*v + dt**2/2 * a + dt**3/6* adot   # predict
    vp = v + dt*a + dt**2/2 * adot
    ap = acc(rp,m,0)          # predicted acceleration
    adotp = Jerks(rp,vp,m,0)  # predicted jerks 
    vp = v + dt/2*(a+ap) - dt**2/12*(adotp-adot)  # correct
    rp = r + dt/2*(v + vp) - dt**2/10 * (ap-a)
 
    return rp,vp
 
def CenterOfMass(r,m):
    CoM = np.zeros(3)
    Mtot= m.sum()
    for i in range(3):
        CoM[i] = (r[:,i]*m).sum()/Mtot
    return CoM
 
def CenterOfMassVelocity(v,m):
    vcom = np.zeros(3)
    Mtot= m.sum()
    for i in range(3):
        vcom[i] = (v[:,i]*m).sum()/Mtot
    return vcom
 
def PotentialEnergy(r,m):
    Phi = np.zeros(len(r))
    for i in range(len(r)):
        for j in range(len(r)):
            ra = math.sqrt(((r[i,:]-r[j,:])**2).sum())
            if (i != j):
                Phi[i] += -m[i]*m[j]/ra 
    return 0.5*Phi.sum()
 
def KineticEnergy(v,m):
    KE = 0.
    for i in range(3): 
        KE += 0.5*(m * (v[:,i]*v[:,i]) ).sum()
    return KE



def convert_to_nbody_units(planet_masses, star_mass, planet_initial_position, planet_initial_velocity, t_end):
    '''
    This will convert masses, positions and velocities into N-body units for numerical stability.
    '''

    # combine all masses & put all in same units (grams)
    masses = (planet_masses*MassOfJupiter).tolist()
    masses.append(star_mass*MassOfSun)
    masses = np.array(masses)

    # combine initial positions
    initial_positions = (planet_initial_position).tolist()
    initial_positions.append([0.0, 0.0, 0.0]) # star starts at (0,0,0)
    initial_positions = np.array(initial_positions)

    # combine initial velocities
    initial_velocities = (planet_initial_velocity).tolist()
    initial_velocities.append([0.0, 0.0, 0.0]) # star starts at (0,0,0) velocity
    initial_velocities = np.array(initial_velocities)

    N=len(masses) # number of bodies
    m = np.ones(N)/N
    m[N-1] = 1.0 # normalize by star's mass
    for i in range(0,N-1):
        m[i]= masses[i]/masses[N-1]

    # ok, now renormalize the positions by the "typical" length scale
    l = 0.0
    for i in range(0,N):
        l += np.sqrt( initial_positions[i,0]**2.+initial_positions[i,1]**2.+initial_positions[i,1]**2. )

    # l = average distance
    l /= N

    r = initial_positions/l
    r -= CenterOfMass(r,m)

    # note: since G is in "real" units, we multiply l and initial velocities by "real" units
    v = initial_velocities*kmincm/np.sqrt( G*masses.sum()/(l*AUinCM) )
    v = v - CenterOfMassVelocity(v,m) # CoM does not move

    tfinal = t_end/( (l*AUinCM)/np.sqrt(G*masses.sum()/(l*AUinCM)) ) # so, this is in weird N-body units: [l/sqrt( G*(M)/l )] where M = sum of all masses ~ star_mass

    #print(t_end, t_end*(l*AUinCM)/np.sqrt(G*masses.sum()/(l*AUinCM))) # units of time
    N = int(N)
    return r, v, tfinal, N, m, masses, l



    
def convert_to_physical_units(r_res, v_res, time, masses, l):
    '''
    Convert input quantities from N-body to physical units
    '''    
    N=len(masses) # number of bodies
    # ok, now renormalize the positions by the "typical" length scale
    #l = 0.0
    #initial_positions = r_res[:,:,0]
    #for i in range(0,N):
    #    l += np.sqrt( initial_positions[i,0]**2.+initial_positions[i,1]**2.+initial_positions[i,1]**2. )

    # l = average distance
    #l /= N

    r_res *= l # into AU

    v_res /= (kmincm/np.sqrt( G*masses.sum()/(l*AUinCM) ))

    t_h = time*( (l*AUinCM)/np.sqrt(G*masses.sum()/(l*AUinCM)) ) # units of years

    return r_res, v_res, t_h




def read_in_planet_data(save_file):
    inarr = np.genfromtxt(save_file, delimiter=',')

    # first, lets figure out what "N" (the number of planets) is
    N = (inarr.shape[1]-2)/6 # the "6" = x/y/z + vx/vy/vz entries
    N = int(N)

    # create position, velocity, time and energy arrays
    r_res = np.zeros( [N, 3, inarr.shape[0]] )
    v_res = np.zeros( [N, 3, inarr.shape[0]] )
    t_h = np.zeros( [inarr.shape[0]] )
    e_h = np.zeros( [inarr.shape[0]] )

    # now fill our arrays
    for ti in range(0,len(t_h)):
        t_h[int(ti)] = inarr[int(ti),0]
        # fill position
        for j in range(0, N):
            r_res[j,0,int(ti)] = inarr[int(ti),1+j*3]
            r_res[j,1,int(ti)] = inarr[int(ti),1+j*3+1]
            r_res[j,2,int(ti)] = inarr[int(ti),1+j*3+2]
        # fill velociint(ti)es
        for j in range(0, N):
            v_res[j,0,int(ti)] = inarr[int(ti),N*3+1+j*3]
            v_res[j,1,int(ti)] = inarr[int(ti),N*3+1+j*3+1]
            v_res[j,2,int(ti)] = inarr[int(ti),N*3+1+j*3+2]
        # finally, fill energy
        e_h[int(ti)] = inarr[int(ti), inarr.shape[1]-1]

    # for plotting also create the "average radius"
    l = 0.0
    for i in range(0,N):
        l += np.sqrt( r_res[i,0,:].max()**2 + r_res[i,1,:].max()**2 + r_res[i,2,:].max()**2 )

    # l = average distance
    l /= N

    return t_h, r_res, v_res, e_h, N



# NOTE: this is nearly the same as that for reading the planet data
def read_in_galaxy_data(save_file):
    inarr = np.genfromtxt(save_file, delimiter=',')
    # first, lets figure out what "N" (the number of planets) is
    N = (inarr.shape[1]-2)/(3+3+1) # the "6" = x/y/z + vx/vy/vz + part_type entries, 2 because: time, energy
    N = int(N)

    # create position, velocity, time and energy arrays
    r_res = np.zeros( [N, 3, inarr.shape[0]] )
    v_res = np.zeros( [N, 3, inarr.shape[0]] )
    t_h = np.zeros( [inarr.shape[0]] )
    e_h = np.zeros( [inarr.shape[0]] )
    part_type = np.zeros( [N, inarr.shape[0]] )

    # now fill
    for ti in range(0,len(t_h)):
        t_h[int(ti)] = inarr[int(ti),0]
        # fill position
        for j in range(0, N):
            r_res[j,0,int(ti)] = inarr[int(ti),1+j*3]
            r_res[j,1,int(ti)] = inarr[int(ti),1+j*3+1]
            r_res[j,2,int(ti)] = inarr[int(ti),1+j*3+2]
        # fill velocities
        for j in range(0, N):
            v_res[j,0,int(ti)] = inarr[int(ti),N*3+1+j*3]
            v_res[j,1,int(ti)] = inarr[int(ti),N*3+1+j*3+1]
            v_res[j,2,int(ti)] = inarr[int(ti),N*3+1+j*3+2]
            part_type[j,int(ti)] = inarr[int(ti), N*3*2+1+j]
        # finally, fill energy
        e_h[int(ti)] = inarr[int(ti), inarr.shape[1]-1]


    # for plotting also create the "average radius"
    l = 0.0
    for i in range(0,N):
        l += np.sqrt( r_res[i,0,:].max()**2 + r_res[i,1,:].max()**2 + r_res[i,2,:].max()**2 )

    # l = average distance
    l /= N

    return t_h, r_res, v_res, e_h, N, part_type

# ------------ Galaxy stuffs -------------

# the function that writes the PLY file

# ply exporter modifed from Tomer Nussbaum, for questions contact either one of us, Tomer: tussbaum@gmail.com
# this just puts your x/y/z positions into the proper format
def write_particles_ply(dst_filename, particles_x, particles_y, particles_z, color_vec):
    f_par = open(dst_filename+'.ply','w')
    nv = len(particles_x[0][:])*len(particles_x)
    f_par.write('ply\nformat ascii 1.0\ncomment Created by vertex2ply pyScript 21122015\n'+\
                'element vertex ' + str(nv) +'\n'+\
                'property float x\n' +\
                'property float y\n' +\
                'property float z\n' +\
                'property uchar red\n' +\
                'property uchar green\n' +\
                'property uchar blue\n' +\
                'element face 0\n' +\
                'property list uchar uint vertex_indices\n' +\
                'end_header\n')
    
    #print(color_vec)
    for i in range(len(color_vec)): # this is the length of color
        for j in range(len(particles_x[i][:])):
            f_par.write('%.6g %.6g %.6g '  % (particles_x[i][j], particles_y[i][j], particles_z[i][j]) + str(color_vec[i][0]) + ' ' + str(color_vec[i][1]) + ' ' + str(color_vec[i][2]) + '\n')
    f_par.close()


def write_galaxy_snap(r_res, part_type, colors, Nplot, outdir, galaxy_ply_name):
    # formatting for output writing of file
    xs = []
    ys = []
    zs = []
    for i in range(0,len(colors)):
        xs.append( r_res[part_type[:,Nplot]-1 == i ,0,Nplot] )
        ys.append( r_res[part_type[:,Nplot]-1 == i,1,Nplot] )
        zs.append( r_res[part_type[:,Nplot]-1 == i,2,Nplot] )

    # name of output ply file, will be NAME.ply
    write_particles_ply(outdir+galaxy_ply_name, xs, ys, zs, colors)

    print('Wrote: ' + outdir+galaxy_ply_name)


