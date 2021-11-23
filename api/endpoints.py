def root():
    return {
        'message': "Hello, that's a root node of API, please send request to a proper node :)",
        'avail_nodes':
            {
                'params': "/api/v0.1/dsa/params",
                'calc': "/api/v0.1/dsa/calc/{lat_min}{lat_max}{long_min}{long_max}",
                'register': "/api/v0.1/dsa/register/{long}{lat}{nf}{prx}{gt}{gr}{channel}{aclr1}{aclr2}"}
    }


def get_params():
    return {
        'carrier': 1811,  # MHz
        'channels': 12,  # just 12 channels XD
        'bandwidth': 100,  # Mhz per channel
    }


def post_calc(lat_min, lat_max, long_min, long_max):
    users = list()  # get existing users with data from database
    return {
        'min_SNR': 6,  # dB
        'min_SINR': 0,  # dB
        'grid': 100,  # m
        'lat_min': lat_min,
        'lat_max': lat_max,
        'long_min': long_min,
        'long_max': long_max,
        'users': users  # contains all users in system
    }


def post_register(long, lat, nf, prx, gt, gr, channel, aclr1, aclr2):
    return {
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
