from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime

import ctypes
import _ctypes
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

    def sendValues(self, joints):
        # Torso
        j1x = joints[PyKinectV2.JointType_Head].Position.x
        j2x = joints[PyKinectV2.JointType_Neck].Position.x
        j3x = joints[PyKinectV2.JointType_SpineMid].Position.x
        j4x = joints[PyKinectV2.JointType_SpineBase].Position.x
        j5x = joints[PyKinectV2.JointType_SpineShoulder].Position.x
        j6x = joints[PyKinectV2.JointType_ShoulderRight].Position.x
        j7x = joints[PyKinectV2.JointType_ShoulderLeft].Position.x
        j8x = joints[PyKinectV2.JointType_HipRight].Position.x
        j9x = joints[PyKinectV2.JointType_HipLeft].Position.x
    
        # Right Arm    
        j10x = joints[PyKinectV2.JointType_ElbowRight].Position.x
        j11x = joints[PyKinectV2.JointType_WristRight].Position.x
        j12x = joints[PyKinectV2.JointType_HandRight].Position.x
        j13x = joints[PyKinectV2.JointType_HandTipRight].Position.x
        j14x = joints[PyKinectV2.JointType_ThumbRight].Position.x

        # Left Arm    
        j15x = joints[PyKinectV2.JointType_ElbowLeft].Position.x
        j16x = joints[PyKinectV2.JointType_WristLeft].Position.x
        j17x = joints[PyKinectV2.JointType_HandLeft].Position.x
        j18x = joints[PyKinectV2.JointType_HandTipLeft].Position.x
        j19x = joints[PyKinectV2.JointType_ThumbLeft].Position.x

        # Right Leg
        j20x = joints[PyKinectV2.JointType_KneeRight].Position.x
        j21x = joints[PyKinectV2.JointType_AnkleRight].Position.x
        j22x = joints[PyKinectV2.JointType_FootRight].Position.x

        # Left Leg
        j23x = joints[PyKinectV2.JointType_KneeLeft].Position.x
        j24x = joints[PyKinectV2.JointType_AnkleLeft].Position.x
        j25x = joints[PyKinectV2.JointType_FootLeft].Position.x

        self._connection.sendall(("%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,"%(j1x,j2x,j3x,j4x,j5x,j6x,j7x,j8x,j9x,j10x,j11x,j12x,j13x,j14x,j15x,j16x,j17x,j18x,j19x,j20x,j21x,j22x,j23x,j24x,j25x)).encode())

        # Torso
        j1y = joints[PyKinectV2.JointType_Head].Position.y
        j2y = joints[PyKinectV2.JointType_Neck].Position.y
        j3y = joints[PyKinectV2.JointType_SpineMid].Position.y
        j4y = joints[PyKinectV2.JointType_SpineBase].Position.y
        j5y = joints[PyKinectV2.JointType_SpineShoulder].Position.y
        j6y = joints[PyKinectV2.JointType_ShoulderRight].Position.y
        j7y = joints[PyKinectV2.JointType_ShoulderLeft].Position.y
        j8y = joints[PyKinectV2.JointType_HipRight].Position.y
        j9y = joints[PyKinectV2.JointType_HipLeft].Position.y
    
        # Right Arm    
        j10y = joints[PyKinectV2.JointType_ElbowRight].Position.y
        j11y = joints[PyKinectV2.JointType_WristRight].Position.y
        j12y = joints[PyKinectV2.JointType_HandRight].Position.y
        j13y = joints[PyKinectV2.JointType_HandTipRight].Position.y
        j14y = joints[PyKinectV2.JointType_ThumbRight].Position.y

        # Left Arm    
        j15y = joints[PyKinectV2.JointType_ElbowLeft].Position.y
        j16y = joints[PyKinectV2.JointType_WristLeft].Position.y
        j17y = joints[PyKinectV2.JointType_HandLeft].Position.y
        j18y = joints[PyKinectV2.JointType_HandTipLeft].Position.y
        j19y = joints[PyKinectV2.JointType_ThumbLeft].Position.y

        # Right Leg
        j20y = joints[PyKinectV2.JointType_KneeRight].Position.y
        j21y = joints[PyKinectV2.JointType_AnkleRight].Position.y
        j22y = joints[PyKinectV2.JointType_FootRight].Position.y

        # Left Leg
        j23y = joints[PyKinectV2.JointType_KneeLeft].Position.y
        j24y = joints[PyKinectV2.JointType_AnkleLeft].Position.y
        j25y = joints[PyKinectV2.JointType_FootLeft].Position.y

        self._connection.sendall(("%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,"%(j1y,j2y,j3y,j4y,j5y,j6y,j7y,j8y,j9y,j10y,j11y,j12y,j13y,j14y,j15y,j16y,j17y,j18y,j19y,j20y,j21y,j22y,j23y,j24y,j25y)).encode())

        # Torso
        j1z = joints[PyKinectV2.JointType_Head].Position.z
        j2z = joints[PyKinectV2.JointType_Neck].Position.z
        j3z = joints[PyKinectV2.JointType_SpineMid].Position.z
        j4z = joints[PyKinectV2.JointType_SpineBase].Position.z
        j5z = joints[PyKinectV2.JointType_SpineShoulder].Position.z
        j6z = joints[PyKinectV2.JointType_ShoulderRight].Position.z
        j7z = joints[PyKinectV2.JointType_ShoulderLeft].Position.z
        j8z = joints[PyKinectV2.JointType_HipRight].Position.z
        j9z = joints[PyKinectV2.JointType_HipLeft].Position.z
    
        # Right Arm    
        j10z = joints[PyKinectV2.JointType_ElbowRight].Position.z
        j11z = joints[PyKinectV2.JointType_WristRight].Position.z
        j12z = joints[PyKinectV2.JointType_HandRight].Position.z
        j13z = joints[PyKinectV2.JointType_HandTipRight].Position.z
        j14z = joints[PyKinectV2.JointType_ThumbRight].Position.z

        # Left Arm    
        j15z = joints[PyKinectV2.JointType_ElbowLeft].Position.z
        j16z = joints[PyKinectV2.JointType_WristLeft].Position.z
        j17z = joints[PyKinectV2.JointType_HandLeft].Position.z
        j18z = joints[PyKinectV2.JointType_HandTipLeft].Position.z
        j19z = joints[PyKinectV2.JointType_ThumbLeft].Position.z

        # Right Leg
        j20z = joints[PyKinectV2.JointType_KneeRight].Position.z
        j21z = joints[PyKinectV2.JointType_AnkleRight].Position.z
        j22z = joints[PyKinectV2.JointType_FootRight].Position.z

        # Left Leg
        j23z = joints[PyKinectV2.JointType_KneeLeft].Position.z
        j24z = joints[PyKinectV2.JointType_AnkleLeft].Position.z
        j25z = joints[PyKinectV2.JointType_FootLeft].Position.z

        self._connection.sendall(("%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4f,%3.4fEOD"%(j1z,j2z,j3z,j4z,j5z,j6z,j7z,j8z,j9z,j10z,j11z,j12z,j13z,j14z,j15z,j16z,j17z,j18z,j19z,j20z,j21z,j22z,j23z,j24z,j25z)).encode())


    def closeConnection(self):
        self._connection.close();




class BodyGameRuntime(object):
    def __init__(self):
        pygame.init()

        # Used to manage how fast the screen updates
        self._clock = pygame.time.Clock()

        # Set the width and height of the screen [width, height]
        self._infoObject = pygame.display.Info()
        self._screen = pygame.display.set_mode((self._infoObject.current_w >> 1, self._infoObject.current_h >> 1), 
                                               pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)

        pygame.display.set_caption("Kinect for Blender v2 server")



        # Kinect runtime object, we want only color and body frames 
        self._kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body)

        # back buffer surface for getting Kinect color frames, 32bit color, width and height equal to the Kinect color frame size
        self._frame_surface = pygame.Surface((self._kinect.color_frame_desc.Width, self._kinect.color_frame_desc.Height), 0, 32)

        print(self._kinect)

        # here we will store skeleton data 
        self._bodies = None

        # Loop until the user clicks the close button.
        self._done = False

        # Used to manage how fast the screen updates
        self._clock = pygame.time.Clock()

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


    def draw_color_frame(self, frame, target_surface):
        target_surface.lock()
        address = self._kinect.surface_as_array(target_surface.get_buffer())
        ctypes.memmove(address, frame.ctypes.data, frame.size)
        del address
        target_surface.unlock()


    def run(self):


        # -------- Main Program Loop -----------
        while not self._done:
            # --- Main event loop
            for event in pygame.event.get(): # User did something (including Ctrl+C)
                if event.type == pygame.QUIT: # If user clicked close
                    self._done = True # Flag that we are done so we exit this loop

                elif event.type == pygame.VIDEORESIZE: # window resized
                    self._screen = pygame.display.set_mode(event.dict['size'], 
                                               pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)

            # --- Getting frames and drawing  
            # --- Woohoo! We've got a color frame! Let's fill out back buffer surface with frame's data 
            if self._kinect.has_new_color_frame():
                frame = self._kinect.get_last_color_frame()
                self.draw_color_frame(frame, self._frame_surface)
                frame = None
                    

            # --- Cool! We have a body frame, so can get skeletons
            if self._kinect.has_new_body_frame(): 
                self._bodies = self._kinect.get_last_body_frame()


            # --- draw skeletons to _frame_surface
            body = None
            if self._bodies is not None: 
                for i in range(0,len(self._bodies.bodies)):
                    if self._bodies.bodies[i].is_tracked: 
                        body = self._bodies.bodies[i]
                    

            if body is not None:
                joints = body.joints 
                print(joints[PyKinectV2.JointType_Head].Position.x)
                self._server.sendValues(joints)
                # convert joint coordinates to color space 
                #joint_points = self._kinect.body_joints_to_color_space(joints)
                #self.draw_body(joints, joint_points)
                
                s = self._server._connection.recv(3)
            else:
                print("no body")
                self._server._connection.sendall("EOD".encode())

                s = self._server._connection.recv(3)

            # --- copy back buffer surface pixels to the screen, resize it if needed and keep aspect ratio
            # --- (screen size may be different from Kinect's color frame size) 
            h_to_w = float(self._frame_surface.get_height()) / self._frame_surface.get_width()
            target_height = int(h_to_w * self._screen.get_width())
            surface_to_draw = pygame.transform.scale(self._frame_surface, (self._screen.get_width(), target_height));
            self._screen.blit(surface_to_draw, (0,0))
            surface_to_draw = None
            pygame.display.update()

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            self._clock.tick(60)



        # Close our Kinect sensor, close the window and quit.
        try:
            self._server.closeConnection()
        finally:
            pass

        # Close our Kinect sensor, close the window and quit.
        self._kinect.close()
        pygame.quit()



__main__ = "Kinect server"
game = BodyGameRuntime();
game.run();

