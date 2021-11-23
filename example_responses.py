
def get_params():
    params = {
    'carrier': 1811,  # MHz
    'channels': 12,  # just 12 channels XD
    'Bandwith': 100,  # Mhz per channel
    }

    return params


def get_calc(lat_min, lat_max, long_min, long_max, users):
    calc = {
        'min_SNR': 6,  # dB
        'min_SINR': 0,  # dB
        'grid': 100,  # m
        'lat_min': lat_min,
        'lat_max': lat_max,
        'long_min': long_min,
        'long_max': long_max,
        'users': users  # contains all users in system
    }

    return calc


def get_register(long, lat, nf, prx, gt, gr, channel, aclr1, aclr2):
    register = {
        'long': long,
        'lat': lat,
        'nf': nf,
        'prx': prx,
        'gt': gt,
        'gr': gr,
        'channel': channel,
        'aclr1': aclr1,
        'aclr2': aclr2
    }

    return register

# USER -> KONTROLER
# data = register
#
# # KONTROLER -> OBLICZANIE
# data = {'userid': 0, 'params': params, 'calc': calc, 'register': register}  # userid is unique for every user in system
#
# # OBLICZANIE -> KONTROLER
# to_return = {user.userid: 0 for user in data['users']}  # calculated SINR for userid instead of 0
