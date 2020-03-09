import numpy as np
def get_ids_and_names(states_map):
    ids = []
    state_names = []
    state_data_vec = states_map.map_data['objects']['subunits']['geometries']
    for i in range(len(state_data_vec)):
        if state_data_vec[i]['properties'] is not None:
            state_names.append(state_data_vec[i]['properties']['name'])
            ids.append(state_data_vec[i]['id'])
    return np.array(ids), np.array(state_names)
