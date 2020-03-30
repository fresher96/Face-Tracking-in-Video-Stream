#!/usr/bin/env python
# coding: utf-8

# # IP WebCam url

# In[1]:


cameraUrl = "http://192.168.0.103:8080/shot.jpg";


# # Mobile Camera Streaming

# In[2]:


import numpy as np;
import requests;
import cherrypy;
import cv2;
import IPython;
from time import sleep;


# In[3]:


class Camera:
    
    def __init__(self, cameraUrl):
        self.url = cameraUrl;
        
    def getFrame(self):
        img_resp = requests.get(self.url);
        return img_resp;


# In[4]:


class CameraWebService(object):
    
    def __init__(self, camera):
        self.camera = camera;
    
    @cherrypy.expose
    def index(self):
        output = self.camera.getFrame();
        return output


# In[5]:


service = CameraWebService(Camera(cameraUrl));


img_resp = service.index()
img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)

img = img_arr;
img = cv2.imdecode(img, cv2.IMREAD_COLOR);
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB);

img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR);
cv2.imshow('img', img);
cv2.waitKey(0);


# In[ ]:


# cherrypy.quickstart(service);

