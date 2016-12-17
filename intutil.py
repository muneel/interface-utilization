#!usr/bin/env python
import re
import time
import sys
import signal
import getopt


def signal_handler(signal, frame):
    # For Handling CTRL+C Gracefully
    print("\n")
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# A regular expression which separates the interesting fields and saves them in named groups
regexp = r"""
  \s*                     # a interface line  starts with none, one or more whitespaces
  (?P<interface>[a-z][a-z]*[0-9]+[a-z0-9.]*):\s+  # the name of the interface followed by a colon and spaces
  (?P<rx_bytes>\d+)\s+    # the number of received bytes and one or more whitespaces
  (?P<rx_packets>\d+)\s+  # the number of received packets and one or more whitespaces
  (?P<rx_errors>\d+)\s+   # the number of receive errors and one or more whitespaces
  (?P<rx_drop>\d+)\s+      # the number of dropped rx packets and ...
  (?P<rx_fifo>\d+)\s+      # rx fifo
  (?P<rx_frame>\d+)\s+     # rx frame
  (?P<rx_compr>\d+)\s+     # rx compressed
  (?P<rx_multicast>\d+)\s+ # rx multicast
  (?P<tx_bytes>\d+)\s+    # the number of transmitted bytes and one or more whitespaces
  (?P<tx_packets>\d+)\s+  # the number of transmitted packets and one or more whitespaces
  (?P<tx_errors>\d+)\s+   # the number of transmit errors and one or more whitespaces
  (?P<tx_drop>\d+)\s+      # the number of dropped tx packets and ...
  (?P<tx_fifo>\d+)\s+      # tx fifo
  (?P<tx_frame>\d+)\s+     # tx frame
  (?P<tx_compr>\d+)\s+     # tx compressed
  (?P<tx_multicast>\d+)\s* # tx multicast
"""

pattern = re.compile(regexp, re.VERBOSE)


def get_bytes(interface_name):
    '''returns tuple of (rx_bytes, tx_bytes) '''
    with open('/proc/net/dev', 'r') as f:
        a = f.readline()
        while(a):
            m = pattern.search(a)
            # the regexp matched
            # look for the needed interface and return the rx_bytes and tx_bytes
            if m:
                if m.group('interface') == interface_name:
                    return (m.group('rx_bytes'), m.group('tx_bytes'))
            a = f.readline()


def run_util(interface, kbps=None):
    tx_max_rate, rx_max_rate = (0, 0)
    rx_avg, tx_avg, n = (0, 0, 0)
    div = 1000000
    if kbps is None:
        div = 1000000
    else:
        div = 1000
    while True:
        # last_time  = time.time()
        last_bytes = get_bytes(interface)
        if last_bytes is None:
            print 'interface "%s" missing' % interface
            sys.exit(0)
        time.sleep(1)
        now_bytes = get_bytes(interface)
        rx_rate = (((float(now_bytes[0]) - float(last_bytes[0])) * 8) / div)
        tx_rate = (((float(now_bytes[1]) - float(last_bytes[1])) * 8) / div)
        n += 1
        rx_avg = ((rx_avg * (n - 1)) + rx_rate) / n
        tx_avg = ((tx_avg * (n - 1)) + tx_rate) / n
        if rx_rate > rx_max_rate:
            rx_max_rate = rx_rate
        if tx_rate > tx_max_rate:
            tx_max_rate = tx_rate
        if kbps is None:
            print "Rx: %7.2f Mbps,   Tx: %7.2f Mbps,   MaxRx: %7.2f Mbps,   MaxTx: %7.2f Mbps   RxAvg: %7.2f Mbps"\
                  "   TxAvg: %7.2f Mbps" % (rx_rate, tx_rate, rx_max_rate, tx_max_rate, rx_avg, tx_avg)
        else:
            print "Rx: %10.2f Kbps,   Tx: %10.2f Kbps,   MaxRx: %10.2f Kbps,   MaxTx: %10.2f kbps   RxAvg: %10.2f Kbps"\
                  "   TxAvg: %10.2f Kbps" % (rx_rate, tx_rate, rx_max_rate, tx_max_rate, rx_avg, tx_avg)


def main(argv):
    interface = None
    kbps = None
    try:
        opts, args = getopt.getopt(argv, "hki:", ["interface="])
    except getopt.GetoptError:
        print '\nTry intutil.py -h\n'
        sys.exit(2)
    if len(opts) != 0:
        for opt, arg in opts:
            if opt == '-h':
                print '\nUsage:\n  python intutil.py -i <interface>\n  Options:\n  -k    Displays in Kbps\n'
            elif opt in ("-i", "--interface"):
                interface = arg
            elif opt == "-k":
                kbps = True
        if interface is not None:
            run_util(interface, kbps)
    else:
        print '\n  Missing Arguments use -h for help\n'

def run_main():
    main(sys.argv[1:])

if __name__ == "__main__":run_main()
