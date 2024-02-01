import time
import sys
import network
import socket
import machine
import select


# Connect to WIFI
# This code is shamelessly plagiaresed form the official rp pico docs

server_id_romer = ('192.168.0.166', 1234)
ssid_romer = 'ROMER_AP_2.4'
password_romer = 'K0van1231'

server_id_usames_phone = ('192.168.43.138', 1234)
ssid_usames_phone = 'NoName'
password_usames_phone = 'osamaawad'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(ssid_usames_phone, password_usames_phone)
#wlan.connect(ssid_romer, password_romer)
 
# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    machine.soft_reset()
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

# set up poller for stdin
poller = select.poll()
poller.register(sys.stdin, select.POLLIN)

while True:
    
    # LET SOCKETS BE BLOCKING AND stdin.readline() be polled
     
    if poller.poll(0):  
            # Read the input sent from the computer into stdin buffer
            data_in = sys.stdin.readline().rstrip("\n")
            
            # Send the output of the calculation to stdout buffer
            sys.stdout.write(str(eval(data_in)))
            time.sleep_ms(50)

    # Listen for connections
    try:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allows pico to connect to the same socket after rebooting if GC didnt kick in
        #s.connect(server_id_romer) # if connecting fails close socket and try again
        s.connect(server_id_usames_phone)
        # send and receive
        data_in = s.recv(512)
        s.sendall( str(eval(data_in)) )
        s.close() 
    except OSError:
        i = 1 # just do nth
    time.sleep_ms(50)
    


