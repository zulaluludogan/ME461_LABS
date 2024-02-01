#!/usr/bin/env python3

import sys
import serial
import socket
from optparse import OptionParser

server_ip = '192.168.43.138'              
PORT = 1234  

# Class for handling serial communications
class Serial_Talker:
    
    TERMINATOR = '\n'.encode('UTF8')

    def __init__(self, timeout=1):
        """
        Initiates Serial Connection
        """
        self.serial = serial.Serial('/dev/ttyACM0', 115200, timeout=timeout)

    def send(self, text: str):
        """
        Sends Encoded Serial Data to PICO
        """
        line = '%s\n' % text
        self.serial.write(line.encode('utf-8'))
       
    def receive(self) -> str:
        """
        Receives and Decodes Result from PICO

        return: string representing result
        """
        line = self.serial.read_until(self.TERMINATOR)
        return line.decode('UTF8').strip()

    def close(self):
        """
        Ends Serial Communications and Frees Resources
        """
        self.serial.close()


if __name__ == "__main__":

    # Parse the Input just like Bugra Hoca
    parser = OptionParser()
    (options, args) = parser.parse_args()

    # Check if there is enough argumeents
    if len(args) == 0 or (len(args) == 1 and args[-1] == "s"):
        print("You need to supply an expression.\n \
              Please Try Again")
        sys.exit()
        
    if args[-1] != 'w':
        
        #talk.send('\x02')
        #talk.send('\x04')

        s_talker = Serial_Talker()         

        # Remove the s otherwise an error gets raised
        if args[-1] == 's': args.pop() 
        
        # Send an argument and wait for the response
        for argument in args:
            s_talker.send(argument)
            print(s_talker.receive())
        
        s_talker.close()
    
    elif args[-1] == 'w':

        retrieved_results = [] # not necessary but whatever it can stay

        args.pop() # remove the w at the end
        args = args[::-1] # reverse the order for ease of use later
        len_args = len(args) # store it becasue we are gonna be popping later
        
        # an infinite loop is needed to open and close since pico(client) might start before comp(server)
        while True: # open socket, send, close socket. 
            try:        
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # this basically means IDC about garbage collection
                    
                    # classical socket stuff
                    s.bind((server_ip, PORT))
                    s.listen(1)
                    conn, addr = s.accept()
                    
                    # send receive and display
                    conn.sendall(args.pop().encode('utf-8'))
                    x = conn.recv(1024).decode('utf-8') 
                    retrieved_results.append(x)
                    print(x)
                    s.close()

                    # break if correct number of responses is received otherwise keep looping
                    if len(retrieved_results) == len_args:
                        break

            except Exception as e:
                print('error')
        
        




    
    
