import numpy as np

# unit conversions
MassOfSun = 2e33 # g
MassOfJupiter = 1.898e30 # g
AUinCM = 1.496e13 # cm
kmincm = 1e5 # cm/km
G = 6.674e-8 # gravitational constant in cm^3 g^-1 s^-2

#---------------------------------------------------

# convert kepler data into 
# positions in AU
# velocities in km/s
# star mass in Msun
# planet masses in MJupiter
def convert_kepler_data(planet_data, select_random_ecc=False, use_inclination_3d=False):

    ecc = planet_data['ecc']
    #print('ecc')
    #print(planet_data['ecc'])
    # shall we select a random eccentricity?
    if select_random_ecc:
        ecc_save = []
        for i in range(len(ecc)):
            # for empty values
            u = planet_data['ecc'][i]+planet_data['eeccU'][i]
            l = planet_data['ecc'][i]+planet_data['eeccL'][i]
            if (u > 1): u = 1.0
            if (l < 0): l = 0.0
            ecc_save.append( (u - l) * np.random.random_sample() + l )
            if ecc_save[-1] < 0: ecc_save[-1] = 0.0
            #if ecc_save[-1] > 1: ecc_save[-1] = 1.0
            #print(planet_data['ecc'][i],u,l)
        ecc = ecc_save
        #print(ecc)

    
    a = planet_data['a']
    
    star_mass = np.mean(planet_data['sMass'])#*MassOfSun # say star's mass = average of all measurements
    planet_masses = planet_data['pMass']#*MassOfJupiter

    # now, do some conversions to get "initial" radii and velocities
    # lets assume ~circular orbits (since eccentricities aren't known too well)... then
    planet_initial_position = np.zeros([len(planet_masses),3]) # AU
    planet_initial_velocity = np.zeros([len(planet_masses),3])

    # SOLUTION #1:
    # to calculate initial positions and velocities we are assuming that
    # each orbit is approximately elliptical and that the total mass of the 
    # system ~ the mass of the star
    #for i in range(0,len(planet_masses)):
    #    planet_initial_position[i,:] = [-a[i]*(1.0 - ecc[i]), 0., 0.] # in AU
    #    planet_initial_velocity[i,:] = [0.0,-np.sqrt( G*star_mass*MassOfSun*(1.0-ecc[i])/(a[i]*AUinCM) )/kmincm, 0.]


    # SOLUTION #2: A MORE COMPLICATED ALTERNATIVE SOLUTION:
    # now, we can estimate these orbits as almost circular (since they don't really know much about the ellipticity)
    #  this allows us to get the "phase" offsets of the systems from their time of first transit
    # say "base" is first planet, offset all other planets from there
    planet_initial_position[0,:] = [-a[0]*(1.0 - ecc[0]), 0., 0.] # in AU
    planet_initial_velocity[0,:] = [0.0, -np.sqrt( G*star_mass*MassOfSun*(1.0-ecc[0])/(a[0]*AUinCM) )/kmincm, 0.]
    for i in range(1, len(planet_masses)):
        if use_inclination_3d:
            sigma = planet_data['Incl'][i]#-3
            #print('Inclination angle = ', sigma)
            sin_sigma = np.sin(sigma * np.pi/180.)
            cos_sigma = np.cos(sigma * np.pi/180.)
        else:
            sin_sigma = 1.0
            cos_sigma = 0.0
        dt = np.abs(planet_data['tTime'][i] - planet_data['tTime'][0])
        # what fraction of the orbital time is this?
        fdt = dt/planet_data['Porb'][i]
        theta = 360.0*fdt
        #print(fdt, theta)
        # now assume the orbit is r(theta) like for analytical, and that its circular enough that v ~ const
        r = a[i]*(1.0 - ecc[i])
        planet_initial_position[i,:] = [r*np.cos(theta * np.pi/180.0)*sin_sigma, 
                                        r*np.sin(theta * np.pi/180.0)*sin_sigma, 
                                        r*cos_sigma]
        # here we use v~const and rotate the initial velocity vector to be tangent to planet_initial_position
        vx = -r*np.sin(theta * np.pi/180.0)*sin_sigma
        vy = r*np.cos(theta * np.pi/180.0)*sin_sigma
        # note: here we keep no z-component since it doesn't matter - 
        #   see: https://math.stackexchange.com/questions/137362/how-to-find-perpendicular-vector-to-another-vector
        vmag = np.sqrt( G*star_mass*MassOfSun*(1.0-ecc[i])/(a[i]*AUinCM) )/kmincm
        # renormalize to velocity vector's magnitude
        planet_initial_velocity[i,:] = [vx/np.sqrt(vx*vx+vy*vy)*vmag, vy/np.sqrt(vx*vx+vy*vy)*vmag, 0.0]


    # now, lets add on our defined planets
    planet_masses = planet_masses.tolist()
    planet_initial_position = planet_initial_position.tolist()
    planet_initial_velocity = planet_initial_velocity.tolist()
    #for i in range(0,len(my_planet_masses)):
    #    planet_masses.append(my_planet_masses[i])
    #    planet_initial_position.append(my_planet_initial_position[i,:])
    #    planet_initial_velocity.append(my_planet_initial_velocity[i,:])

    planet_masses = np.array(planet_masses)
    planet_initial_position = np.array(planet_initial_position)
    planet_initial_velocity = np.array(planet_initial_velocity)

    return star_mass, planet_masses, planet_initial_position, planet_initial_velocity, ecc


def read_kepler_data(fileLocation):
    names = ('RowID', 'SysName', 'planetLetter', 'NumberOfPlanets', 'Porb', 
             'ePorbU', 'ePorbL',       'a',             'ea',       'ecc', 
             'eeccU',    'eeccL',    'Incl',           'eInclU',    'eInclL', 
             'pMass',   'epMassU', 'epMassL',          'pMassType', 'sMass', 
             'esMass',  'sRadius', 'esRadiusU',       'esRadiusL',  'tTime', 
             'etTimeU', 'etTimeL')
    formats = ('f4',       'S12',     'S2',               'f4',        'f4',
               'f4',       'f4',      'f4',               'f4',        'f4',
               'f4',       'f4',      'f4',               'f4',        'f4',
               'f4',       'f4',      'f4',               'S8',        'f4',
               'f4',       'f4',      'f4',               'f4',        'f4', 
               'f4',       'f4')
    kepler_data = np.genfromtxt(fileLocation, 
                                comments='#', 
                                delimiter=',', 
                                dtype={'names':names, 
                                       'formats':formats})
    return kepler_data


