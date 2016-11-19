# interface-utilization

A tool written in python for getting Utilization of the given Interface.
Parses /proc/net/dev to display statistics.

Usage:
  python intutil.py -i <interface> 
  Options:
  -k  Displays Traffic in Kbps (Default Mbps)
  
Sample Output:
  $ python intutil.py -i eth0 -k
Rx:      12.50 Kbps,   Tx:       4.23 Kbps,   MaxRx:      12.50 Kbps,   MaxTx:       4.23 kbps   RxAvg:      12.50 Kbps   TxAvg:       4.23 Kbps
Rx:      10.14 Kbps,   Tx:       1.83 Kbps,   MaxRx:      12.50 Kbps,   MaxTx:       4.23 kbps   RxAvg:      11.32 Kbps   TxAvg:       3.03 Kbps
Rx:      10.90 Kbps,   Tx:       1.75 Kbps,   MaxRx:      12.50 Kbps,   MaxTx:       4.23 kbps   RxAvg:      11.18 Kbps   TxAvg:       2.61 Kbps
Rx:       6.41 Kbps,   Tx:       3.06 Kbps,   MaxRx:      12.50 Kbps,   MaxTx:       4.23 kbps   RxAvg:       9.99 Kbps   TxAvg:       2.72 Kbps
Rx:      11.65 Kbps,   Tx:       1.74 Kbps,   MaxRx:      12.50 Kbps,   MaxTx:       4.23 kbps   RxAvg:      10.32 Kbps   TxAvg:       2.52 Kbps
Rx:       8.21 Kbps,   Tx:       5.44 Kbps,   MaxRx:      12.50 Kbps,   MaxTx:       5.44 kbps   RxAvg:       9.97 Kbps   TxAvg:       3.01 Kbps
