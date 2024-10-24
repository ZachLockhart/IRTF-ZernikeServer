#!/usr/bin/env python3

'''

zern 2024-10-24 10:29:00 1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,1.0,5.0


'''


import socket
import re
import argparse

# Server setup
HOST = '0.0.0.0'  # Listen on all available interfaces
DEFAULT_PORT = 8000       # Port number

def process_command(command):
    # Define regex to match the command format: zern [timestamp] [X1,Y1,X2,Y2,...X10,Y10]
    pattern = r"^zern\s+\[\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\]\s+\[([0-9.,\s\-]+)\]$"
    match = re.match(pattern, command.strip())

    if not match:
        return "Invalid command format!"

    # Extract the comma-separated values
    values_str = match.group(1)

    # Split the values and convert them to float
    values = [float(v) for v in values_str.split(',')]

    if len(values) != 20:
        return "Expected 10 pairs of X,Y values!"

    # Separate X and Y values
    X_values = values[::2]  # Every second value starting from 0 (X1, X2, ..., X10)
    Y_values = values[1::2]  # Every second value starting from 1 (Y1, Y2, ..., Y10)

    for iii in range(10):
        print("v" + str(iii) + ": " + str(X_values[iii]) + ", " + str(Y_values[iii]))

    return X_values, Y_values

def start_server(port):
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, port))
        s.listen()

        print(f"Server listening on {HOST}:{port}")

        while True:
            # Accept a connection
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024).decode()  # Receive and decode the incoming data

                if not data:
                    break

                print(f"Received command: {data}")

                # Process the received command
                result = process_command(data)

                if isinstance(result, tuple):
                    X_values, Y_values = result
                    response = f"X values: {X_values}\nY values: {Y_values}"
                else:
                    response = result

                # Send back the response
                conn.sendall(response.encode())

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Simple TCP Server for Zern Command")
    parser.add_argument('--port', type=int, default=DEFAULT_PORT, help="Port number to listen on")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Start the server using the specified or default port
    start_server(args.port)
