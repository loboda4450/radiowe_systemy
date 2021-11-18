params = {
    'carrier': 1811,  # MHz
    'channels': 12,  # just 12 channels XD
    'Bandwith': 100,  # Mhz per channel
}

calc = {
    'min_SNR': 6,  # dB
    'min_SINR': 0,  # dB
    'grid': 100,  # m
    'lat_min': 0.0,
    'lat_max': 0.0,
    'long_min': 0.0,
    'long_max': 0.0,
    'users': []  # contains all users in system
}

register = {
    'long': 0.0,
    'lat': 0.0,
    'nf': 0.0,
    'prx': 0.0,
    'gt': 0.0,
    'gr': 0.0,
    'channel': 0,
    'aclr1': 0.0,
    'aclr2': 0.0
}

# USER -> KONTROLER
data = register

# KONTROLER -> OBLICZANIE
data = {'userid': 0, 'params': params, 'calc': calc, 'register': register}  # userid is unique for every user in system

# OBLICZANIE -> KONTROLER
to_return = {user.userid: 0 for user in data['users']}  # calculated SINR for userid instead of 0
