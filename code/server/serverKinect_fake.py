import random
import pygame
import sys

import socket
import sys
import os

PORT = 6660

class KinectBodyServer(object):
    def __init__(self):
        
        self._connection = None
        self._clientAddress = None
        self._socket = None

        # Create a UDS socket
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        print("server on localhost")
        self._socket.bind(("",PORT))

        # Listen for incoming connections
        self._socket.listen(1)

    def waitForConnection(self):
        # Wait for a connection
        print("waiting for a connection")
        self._connection, self._clientAddress = self._socket.accept()

    def sendValues(self):
        amp = 0.01

        n1 = amp*float(random.randint(0,100))/40000.0
        n2 = amp*float(random.randint(0,100))/40000.0
        n3 = amp*float(random.randint(0,100))/40000.0
        n4 = amp*float(random.randint(0,100))/40000.0
        n5 = amp*float(random.randint(0,100))/40000.0


        # Torso
        j1x = 0.0 + n1
        j2x = 0.0 + n1 + n2
        j3x = 0.0 + n1 + n2 + n3
        j4x = 0.0 - n1 
        j5x = 0.0 - n1 + n2
        j6x = 0.15 - n1 + n2 + n3
        j7x = -0.15 + n1
        j8x = 0.1 + n1 - n2
        j9x = -0.1 + n1 - n2 + n3
    
        # Right Arm    
        j10x = 0.25 + n1
        j11x = 0.3 - n1 - n2
        j12x = 0.3 - n1 - n2 + n3
        j13x = 0.31 + n1
        j14x = 0.29 + n1 + n2

        # Left Arm    
        j15x = -0.25 + n1 + n2 - n3
        j16x = -0.3 + n1
        j17x = -0.3 + n1 + n2
        j18x = -0.31 + n1 + n2 - n3
        j19x = -0.29 + n1

        # Right Leg
        j20x = 0.2 + n1 + n2
        j21x = 0.2 + n1 + n2 - n3
        j22x = 0.25 - n1

        # Left Leg
        j23x = -0.2 - n1 + n2
        j24x = -0.2 - n1 + n2 - n3
        j25x = -0.25 + n1

        self._connection.sendall(("%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,"%(j1x,j2x,j3x,j4x,j5x,j6x,j7x,j8x,j9x,j10x,j11x,j12x,j13x,j14x,j15x,j16x,j17x,j18x,j19x,j20x,j21x,j22x,j23x,j24x,j25x)).encode())

        # Torso
        j1y = 0.7 + n1
        j2y = 0.6 + n1 + n2
        j3y = 0.3 - n1 + n2 - n3
        j4y = 0.0 + n1
        j5y = 0.55 + n1 - n2
        j6y = 0.55 + n1 - n2 + n3
        j7y = 0.55 + n1
        j8y = -0.1 + n1 - n2
        j9y = -0.1 + n1 - n2 + n3
    
        # Right Arm    
        j10y = 0.3 + n1
        j11y = 0.0 - n1 + n2
        j12y = -0.1 + n1 + n2 + n3
        j13y = -0.15 - n1
        j14y = -0.15 + n1 + n2

        # Left Arm    
        j15y = 0.3 + n1 - n2 + n3
        j16y = 0.0 + n1
        j17y = -0.1 + n1 + n2
        j18y = -0.15 + n1 + n2 + n3
        j19y = -0.15 + n1

        # Right Leg
        j20y = -0.3 + n1 - n2
        j21y = -0.6 + n1 + n2 + n3
        j22y = -0.65 + n1

        # Left Leg
        j23y = -0.3 + n1 + n2
        j24y = -0.6 + n1 + n2 + n3
        j25y = -0.65 + n1

        self._connection.sendall(("%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,"%(j1y,j2y,j3y,j4y,j5y,j6y,j7y,j8y,j9y,j10y,j11y,j12y,j13y,j14y,j15y,j16y,j17y,j18y,j19y,j20y,j21y,j22y,j23y,j24y,j25y)).encode())

        # Torso
        j1z = 0.1 + n4 + n5
        j2z = 0.075 + n4 + n2 + n3
        j3z = 0.025 + n4
        j4z = 0.0 + n4 + n2
        j5z = 0.0 + n4 + n2 + n3
        j6z = 0.0 + n4
        j7z = 0.0 + n4 + n5
        j8z = 0.0 + n4 + n2 + n3
        j9z = 0.0 + n4
    
        # Right Arm    
        j10z = 0.0 + n4 - n2
        j11z = 0.0 + n4 - n2 + n3
        j12z = 0.0 + n4
        j13z = 0.0 + n4 - n2
        j14z = 0.0 + n4 + n2 + n3

        # Left Arm    
        j15z = 0.0 + n4
        j16z = 0.0 + n4 + n5
        j17z = 0.0 + n4 - n5 + n3
        j18z = 0.0 + n4
        j19z = 0.0 + n4 + n2

        # Right Leg
        j20z = 0.0 + n4 + n5 + n3
        j21z = 0.0 + n4
        j22z = 0.0 + n4 - n5

        # Left Leg
        j23z = 0.0 + n4 + n5 + n3
        j24z = 0.0 + n4
        j25z = 0.0 + n4 + n5

        self._connection.sendall(("%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4fEOD"%(j1z,j2z,j3z,j4z,j5z,j6z,j7z,j8z,j9z,j10z,j11z,j12z,j13z,j14z,j15z,j16z,j17z,j18z,j19z,j20z,j21z,j22z,j23z,j24z,j25z)).encode())


    def closeConnection(self):
        self._connection.close();




class BodyGameRuntime(object):
    def __init__(self):
        pygame.init()


        # Loop until the user clicks the close button.
        self._done = False


        # Torso
        # PyKinectV2.JointType_Head -> PyKinectV2.JointType_Neck
        # PyKinectV2.JointType_Neck -> PyKinectV2.JointType_SpineShoulder);
        # PyKinectV2.JointType_SpineShoulder -> PyKinectV2.JointType_SpineMid);
        # PyKinectV2.JointType_SpineMid -> PyKinectV2.JointType_SpineBase);
        # PyKinectV2.JointType_SpineShoulder -> PyKinectV2.JointType_ShoulderRight);
        # PyKinectV2.JointType_SpineShoulder -> PyKinectV2.JointType_ShoulderLeft);
        # PyKinectV2.JointType_SpineBase -> PyKinectV2.JointType_HipRight);
        # PyKinectV2.JointType_SpineBase -> PyKinectV2.JointType_HipLeft);
    
        # Right Arm    
        # PyKinectV2.JointType_ShoulderRight -> PyKinectV2.JointType_ElbowRight);
        # PyKinectV2.JointType_ElbowRight -> PyKinectV2.JointType_WristRight);
        # PyKinectV2.JointType_WristRight -> PyKinectV2.JointType_HandRight);
        # PyKinectV2.JointType_HandRight -> PyKinectV2.JointType_HandTipRight);
        # PyKinectV2.JointType_WristRight -> PyKinectV2.JointType_ThumbRight);

        # Left Arm
        # PyKinectV2.JointType_ShoulderLeft -> PyKinectV2.JointType_ElbowLeft);
        # PyKinectV2.JointType_ElbowLeft -> PyKinectV2.JointType_WristLeft);
        # PyKinectV2.JointType_WristLeft -> PyKinectV2.JointType_HandLeft);
        # PyKinectV2.JointType_HandLeft -> PyKinectV2.JointType_HandTipLeft);
        # PyKinectV2.JointType_WristLeft -> PyKinectV2.JointType_ThumbLeft);

        # Right Leg
        # PyKinectV2.JointType_HipRight -> PyKinectV2.JointType_KneeRight);
        # PyKinectV2.JointType_KneeRight -> PyKinectV2.JointType_AnkleRight);
        # PyKinectV2.JointType_AnkleRight -> PyKinectV2.JointType_FootRight);

        # Left Leg
        # PyKinectV2.JointType_HipLeft -> PyKinectV2.JointType_KneeLeft);
        # PyKinectV2.JointType_KneeLeft -> PyKinectV2.JointType_AnkleLeft);
        # PyKinectV2.JointType_AnkleLeft -> PyKinectV2.JointType_FootLeft);


        self._server = KinectBodyServer()

        self._server.waitForConnection()



    def run(self):


        # -------- Main Program Loop -----------
        while not self._done:
            # --- Main event loop
            for event in pygame.event.get(): # User did something (including Ctrl+C)
                if event.type == pygame.QUIT: # If user clicked close
                    self._done = True # Flag that we are done so we exit this loop

                    

            self._server.sendValues()

            s = self._server._connection.recv(3)


        # Close our Kinect sensor, close the window and quit.
        try:
            self._server.closeConnection()
        finally:
            pass

        pygame.quit()



__main__ = "Kinect server (fake)"
game = BodyGameRuntime();
game.run();

