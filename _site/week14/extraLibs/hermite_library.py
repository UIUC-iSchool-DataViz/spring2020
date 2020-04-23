import numpy as np
import math

# Units
# unit conversions
MassOfSun = 2e33 # g
MassOfJupiter = 1.898e30 # g
AUinCM = 1.496e13 # cm
kmincm = 1e5 # cm/km
G = 6.674e-8 # gravitational constant in cm^3 g^-1 s^-2

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


# now, make sure v perpendicular to position
def make_initial_v_perp(planet_initial_velocity, planet_initial_position):
    for i in range(0,len(planet_initial_velocity)):
        # get the magnitude of the vector
        v = planet_initial_velocity[i]
        r = planet_initial_position[i]
        print('v before:')
        print(v)
        magv = v.dot(v)
        magr = r.dot(r)
        planet_initial_velocity[i,0] = -planet_initial_position[i,1]
        planet_initial_velocity[i,1] = planet_initial_position[i,0]
        # now, make sure the magnitude is that of the velocity, not radial vector
        planet_initial_velocity[i] *= magv/magr
        print('planet init vel')
        print(planet_initial_velocity)
    return planet_initial_velocity


# unit conversion
def convert_units(planet_masses, star_mass, planet_initial_position, planet_initial_velocity):
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

    return masses, initial_positions, initial_velocities


# do the calculation
def do_hermite(star_mass, planet_masses, planet_initial_position,
               planet_initial_velocity, tfinal=20.5, Nsteps = 880,
               threeDee = False):
    # for 2d
    if not threeDee:
        # make sure we are doing motion in x/y plane
        for i in range(0,len(planet_masses)):
            planet_initial_position[i,2] = 0.0
            planet_initial_velocity[i,2] = 0.0


    
    #planet_initial_velocity = make_initial_v_perp(planet_initial_velocity,
    #                                              planet_initial_position)

    masses, initial_positions, initial_velocities = convert_units(planet_masses,
                                                                  star_mass,
                                                                  planet_initial_position,
                                                                  planet_initial_velocity)

    N=len(masses) # number of bodies
    m = np.ones(N)/N
    m[N-1] = 1.0 # normalize by the last mass in the list
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

    #print('tfinal before is ', tfinal)
    tfinal = tfinal/((l*AUinCM)/np.sqrt(G*masses.sum()/(l*AUinCM)))
    #print('tfinal is ', tfinal)
    
    # note: since G is in "real" units, we multiply l and initial velocities by "real" units
    v = initial_velocities*kmincm/np.sqrt( G*masses.sum()/(l*AUinCM) )
    v = v - CenterOfMassVelocity(v,m) # CoM does not move


    #tfinal = 20.5 # so, this is in weird N-body units: [l/sqrt( G*(M)/l )] where M = sum of all masses ~ star_mass
    #Nsteps = 880 # number of steps over for our integration
    r_res = np.zeros((N,3,Nsteps))
    v_res = np.zeros((N,3,Nsteps))

    dt = tfinal/(Nsteps-1)  # fixed time steps
    time = np.zeros(Nsteps)
    r_res[:,:,0] = r.copy()
    v_res[:,:,0] = v.copy()
    Phi= np.zeros(Nsteps)
    KE = np.zeros(Nsteps)
    Phi[0] = PotentialEnergy(r,m)
    KE[0]  = KineticEnergy(v,m)
    for i in range(1,Nsteps):
        (r_res[:,:,i],v_res[:,:,i]) = HermiteUpdate(dt, r_res[:,:,i-1], v_res[:,:,i-1], m)
        time[i] = time[i-1] + dt
        Phi[i] = PotentialEnergy(r_res[:,:,i],m)
        KE[i]  = KineticEnergy(v_res[:,:,i],m)


    # back into physical units
    #r_res *= l/AUinCM
    r_res *= l # into AU

    # for 2nd particle
    x_h = r_res[1,0,:]
    y_h = r_res[1,1,:]

    t_h = time*(l*AUinCM)/np.sqrt(G*masses.sum()/(l*AUinCM)) # units of time

    e_h = Phi + KE

    return r_res, v_res, t_h, e_h


# do the calculation
# masses in Msun
# initial_positions in AU
# initial_velocities in km/s
def do_hermite_galaxies(masses, initial_positions,
                       initial_velocities, tfinal=20.5*1e8, Nsteps = 880):

    N=len(masses) # number of bodies
    m = np.ones(N)/N
    m[N-1] = 1.0 # normalize by star's mass
    for i in range(0,N-1):
        m[i]= masses[i]/masses[N-1]
        
    #print('I am here')

    # ok, now renormalize the positions by the "typical" length scale
    l = 0.0
    for i in range(0,N):
        l += np.sqrt( initial_positions[i,0]**2.+initial_positions[i,1]**2.+initial_positions[i,1]**2. )

    # l = average distance
    l /= N

    # let's convert to n-body units
    #t_h = time*(l*AUinCM)/np.sqrt(G*masses.sum()/(l*AUinCM)) # units of time
    tfinal = tfinal/((l*AUinCM)/np.sqrt(G*masses.sum()/(l*AUinCM)))

    r = initial_positions/l
    r -= CenterOfMass(r,m)


    # note: since G is in "real" units, we multiply l and initial velocities by "real" units
    v = initial_velocities*kmincm/np.sqrt( G*masses.sum()/(l*AUinCM) )
    v = v - CenterOfMassVelocity(v,m) # CoM does not move


    #tfinal = 20.5 # so, this is in weird N-body units: [l/sqrt( G*(M)/l )] where M = sum of all masses ~ star_mass
    #Nsteps = 880 # number of steps over for our integration
    r_res = np.zeros((N,3,Nsteps))
    v_res = np.zeros((N,3,Nsteps))

    dt = tfinal/(Nsteps-1)  # fixed time steps
    time = np.zeros(Nsteps)
    r_res[:,:,0] = r.copy()
    v_res[:,:,0] = v.copy()
    Phi= np.zeros(Nsteps)
    KE = np.zeros(Nsteps)
    Phi[0] = PotentialEnergy(r,m)
    KE[0]  = KineticEnergy(v,m)
    for i in range(1,Nsteps):
        #print(' on step ', i)
        (r_res[:,:,i],v_res[:,:,i]) = HermiteUpdate(dt, r_res[:,:,i-1], v_res[:,:,i-1], m)
        time[i] = time[i-1] + dt
        Phi[i] = PotentialEnergy(r_res[:,:,i],m)
        KE[i]  = KineticEnergy(v_res[:,:,i],m)


    # back into physical units
    #r_res *= l/AUinCM
    r_res *= l # into AU
    r_res /= 2.063e+8 # into kpc

    # for 2nd particle
    x_h = r_res[1,0,:]
    y_h = r_res[1,1,:]

    t_h = time*(l*AUinCM)/np.sqrt(G*masses.sum()/(l*AUinCM)) # units of time

    e_h = Phi + KE
    # normalize
    e_h = e_h/e_h[0]

    return r_res, v_res, t_h, e_h # AU, km/s, seconds, normalized



# Euler's method 2D calculations
def calcAcc(mj, ri, rj):
    mag_r = np.sqrt( (ri[0]-rj[0])**2 \
                    +(ri[1]-rj[1])**2 )
    mag_a = -G*mj/mag_r**2
    # unit vector points from particle 1 -> particle 2
    unitVector = (ri - rj)/mag_r
    # return
    return mag_a*unitVector

# energy
def calcE(m1, m2, r1, r2, v1, v2):
    mag_r = np.sqrt( (r1-r2).dot(r1-r2) )
    return 0.5*(m1*v1.dot(v1) + m2*v2.dot(v2)) - G*m1*m2/mag_r

# angular momentum
def calcL(m1, m2, r1, r2, v1, v2):
    #print(r1, v1, np.cross(r1,v1))
    L = m1*np.cross(r1,v1) + m2*np.cross(r2,v2)
    #mag_L = np.sqrt( L.dot(L) )
    # for 2D
    mag_L = np.sqrt(L*L)
    return mag_L

# this only works for 2 bodies, but it does the euler solution
# M1 = in solar masses
# M2 = in solar masses
# r_0 = in AU
# v_0 in km/s
def do_euler_2body(M1, M2, r_0, v_0, n_steps, delta_t):
    # conversions
    M1 = M1*MassOfSun
    M2 = M2*MassOfSun
    v_0 = v_0*kmincm
    r_0 = r_0*AUinCM

    # Do the Euler's calculation
    ri = r_0
    vi = v_0

    # initial value
    r = [r_0]
    v = [v_0]
    E = [calcE(M1,M2, ri[0,:], ri[1,:], vi[0,:],vi[1,:])]
    L = [calcL(M1,M2, ri[0,:], ri[1,:], vi[0,:],vi[1,:])]
    t = [0] # time = 0

    for i in range(n_steps):
        # use function to grab ag on particle 1
        ag1 = calcAcc(M2, ri[0,:], ri[1,:])
        ag2 = calcAcc(M1, ri[1,:], ri[0,:])

        # for ease, let's create a acceleration vector
        ag = np.array([ag1, ag2])

        # update new position and velocity
        ri1 = ri + vi*delta_t
        vi1 = vi + ag*delta_t

        # append to r vector
        r.append(ri1)
        v.append(vi1)

        # add E, L, t
        t.append(t[-1]+delta_t)
        newE = calcE(M1,M2, ri[0,:], ri[1,:], vi[0,:],vi[1,:])
        newL = calcL(M1,M2, ri[0,:], ri[1,:], vi[0,:],vi[1,:])
        E.append(newE)
        L.append(newL)

        # replace stuff
        ri = ri1
        vi = vi1

    # format outputs
    # r to array
    r = np.array(r)
    v = np.array(v)
    #print(type(r))
    E = np.array(E)
    L = np.array(L)
    # in percentages
    startE = E[0]; startL = L[0]
    E = (E - E[0])/startE
    L = (L - L[0])/startL

    return r/AUinCM, v/kmincm, t, E # AU, km/s, seconds, normalized


# order is:
# t_h
# e_h
# 3*planets - r_h
# 3*planets - v_h
def read_hermite_solution_from_file(filename):

    myout = np.genfromtxt(filename, 
                          delimiter=",")
    
    # get shapes of things
    nObjects = int((myout.shape[1]-2)/(3+3))
    r_h = np.zeros([nObjects, 3, myout.shape[0]])
    v_h = np.zeros([nObjects, 3, myout.shape[0]])
    
    t_h = myout[:,0]
    e_h = myout[:,1]
    for i in range(r_h.shape[0]):
        r_h[i,0,:] = myout[:,2+i*r_h.shape[1]]
        r_h[i,1,:] = myout[:,2+i*r_h.shape[1]+1]
        r_h[i,2,:] = myout[:,2+i*r_h.shape[1]+2]

    # now, v_h's
    #print('break')
    for i in range(r_h.shape[0]):
        v_h[i,0,:] = myout[:,2+r_h.shape[1]*r_h.shape[0] +i*r_h.shape[1]]
        v_h[i,1,:] = myout[:,2+r_h.shape[1]*r_h.shape[0] +i*r_h.shape[1]+1]
        v_h[i,2,:] = myout[:,2+r_h.shape[1]*r_h.shape[0] +i*r_h.shape[1]+2]

    return t_h, e_h, r_h, v_h
        

def save_hermite_solution_to_file(filename, t_h, e_h, r_h, v_h):
    # reshape out array
    # t_h, e_h, 3*#planets, 3*#planets
    myout = np.zeros([len(t_h),1+1+r_h.shape[0]*r_h.shape[1]+v_h.shape[0]*v_h.shape[1]])

    myout[:,0] = t_h
    myout[:,1] = e_h
    for i in range(r_h.shape[0]):
        #print(2+i*r_h.shape[1],2+i*r_h.shape[1]+1, 2+i*r_h.shape[1]+2)
        myout[:,2+i*r_h.shape[1]] = r_h[i,0,:]
        myout[:,2+i*r_h.shape[1]+1] = r_h[i,1,:]
        myout[:,2+i*r_h.shape[1]+2] = r_h[i,2,:]

    # now, v_h's
    #print('break')
    for i in range(r_h.shape[0]):
        #print(2+r_h.shape[1]*r_h.shape[0] +i*r_h.shape[1], 2+r_h.shape[1]*r_h.shape[0] +i*r_h.shape[1]+1, 
        #     2+r_h.shape[1]*r_h.shape[0] +i*r_h.shape[1]+2)
        myout[:,2+r_h.shape[1]*r_h.shape[0] +i*r_h.shape[1]] = v_h[i,0,:]
        myout[:,2+r_h.shape[1]*r_h.shape[0] +i*r_h.shape[1]+1] = v_h[i,1,:]
        myout[:,2+r_h.shape[1]*r_h.shape[0] +i*r_h.shape[1]+2] = v_h[i,2,:]

    np.savetxt(filename, myout, delimiter=',') 
