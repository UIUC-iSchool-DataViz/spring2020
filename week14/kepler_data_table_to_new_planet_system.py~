import pandas as pd
import numpy as np


# file of dataout
# host star name
def read_convert_new_system(filename, name):
    planets = pd.read_csv(filename, sep=",", comment="#")

    # only select entries with this name
    mask = planets['pl_hostname'] == name
    ecc = planets['pl_orbeccen'][mask]
    a = planets['pl_orbsmax'][mask]
    Porb = planets['pl_orbper'][mask]
    Incl = planets['pl_orbincl'][mask]
    sMass = planets['st_mass'][mask]
    pMass = planets['pl_bmassj'][mask]
    tTime = planets['pl_orbtper'][mask]

    # now convert to kepler data dictionary
    # only entries we really need to use in the convert_kepler_data function
    kepler_data = {}

    kepler_data['SysName'] = name
    kepler_data['NumberOfPlanets'] = len(a) 
    kepler_data['Porb'] = Porb.values
    kepler_data['a']=a.values
    kepler_data['ecc']=ecc.values
    kepler_data['Incl']=Incl.values
    kepler_data['pMass']=pMass.values
    kepler_data['sMass']=sMass.values
    kepler_data['tTime']=tTime.values

    return kepler_data
