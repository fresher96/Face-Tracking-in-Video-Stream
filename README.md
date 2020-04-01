
# Face Tracking and Recognition in Video Streams
Python code for face tracking and recognition in video streams using [face_recognition](https://github.com/ageitgey/face_recognition) and open-cv.  
[Google Colab Link](https://colab.research.google.com/drive/1BR4EzaLE-qEzzRp05VvMxiBj5gDd84-n)

The directory `FaceDir` should contain, for each person that you want to recognize, an image of his/her face.

You can use this code to track and recognize these people (unrecognized people's faces will be tracked too) in any video stream.

We implemented this functionality for the following video streams:
- Offline Setting: uses a video file.
- Laptop Webcam Setting: uses laptop embedded webcam.
- Online Setting: uses `cameraUrl` to get frames from the video stream when `cameraUrl` is accessible online. E.g. `cameraUrl = http://my-stream.com`).
- Local Setting: uses `cameraUrl` to get frames from the video stream when `cameraUrl` is on the same local network. E.g. connected webcam, connected mobile phone through hotspot, `cameraUrl = 192.168.0.103:8080/shot.jpg`).

In order to use other types of video streams (e.g. security camera), you can extend `VideoStreamBase` or `LocalVideoStream` and override `getImage() -> numpy.ndarray` method to define the procedure of getting a new frame.





## Example of running the code using mobile's camera
1. On your phone, download `IP Webcam` app.
2. Run `IP Webcam` server. Let's name its IP `ip_webcam`.
3. Let `cameraUrl` be equal to:
    - `ip_webcam:port/shot.jpg` if it is on the same local network.
    - A public IP that is a proxy to get to `ip_webcam`.  
      For example, you can use `ngrok.com` to do this:  
      - Launch RESTful API by running:  
        `url='ip_webcam:port/shot.jpg' runipy main.ipynb`
      - Make this API accessible online by running:  
        `winpty ngrok http 8080`  
        And let `cameraUrl` equals the resulting public url (e.g. `http://eeba6d36.ngrok.io`).
5. Run the corresponding code in the notebook `AIR0_project.ipynb` using jupyter or colab.



## Demo
![Follow below link if the file didn't load](https://i.imgur.com/PIfeTZO.gif)  
[demo](https://i.imgur.com/PIfeTZO.gif)

