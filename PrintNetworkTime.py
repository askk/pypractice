import ntplib
from time import ctime


def print_network_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    print("ntp time: " + ctime(response.tx_time))


if __name__ == '__main__':
    print_network_time()