

# Face Tracking and Recognition in Video Stream
Python code for face tracking and recognition in video streams
using [face_recognition](https://github.com/ageitgey/face_recognition)
and open-cv.


## Run Instructions
1. Specify your configurations in `configs.json`.
2. If you are using `mode = online`, run `runipy lunch_service.ipynb`.
3. Run `runipy main.ipynb`


## Database Schema
- Image  
A directory that contains one photo of each person you want to recognize.
Accepted extensions: `.jpg`, `.jpeg`, `.png`.
Image name will be considered as the person's name.

- Face(id, embedding)  
JSON file that stores faces' embeddings.
If this file is empty, run `runipy images2embeddings.ipynb`.

- Person(id, face_id, name)  
JSON file of people's information with their corresponding faces.
If this file is empty, run `runipy images2embeddings.ipynb`.

- Presence(id, face_id, person_id, name, timestamp_first, timestamp_last)  
CSV file that stores presence information in the input video stream.

- Demo  
A directory that contains `Presence.csv` output for some demo samples.


## Configurations
Specify your configurations in `configs.json`.
- `database`: Database directory path.
- `db_image`: Database/Image directory path.
- `db_face`: Database/Face faces json file path.
- `db_person`: Database/Person people json file path.
- `db_presence`: Database/Presence presence csv file path.
- `camera_url`: The url to fetch frames from the video stream if `mode` is `online` or `local`.
- `camera_url2`: The local url to fetch frames from the video stream if `mode` is `online`.
Later, we expose this url to a the public url `camera_url`.
- `drive`: The url of your google drive in case you want to use google colab.
- `face_locations_model`: `hog` (simple model) or `cnn` (complex model).
- `face_encodings_model`: `small` (simple model) or `large` (complex model).
- `video_file`: Video file path if `mode` is `file`.
- `output_file`: Output file path to store the resulting video stream.
- `frames_to_enter`: Minimum number of consecutive frames in order to log a person in.
- `frames_to_exit`: Maximum number of consecutive frames after which the absence of a person will log him out.
- `tolerance`: If the distance between the closest face in the database and the face in the video is less that `tolerance`,
we consider it a match. Otherwise, we say that the face isn't a recognized person.
- `colab`: `True` or `False` whether running on google colab or not, if so, loads the configurations from `configs_colab.json`.
- `mode`: One value from `online`, `local`, `file`, `webcam`.
Otherwise, it's equivalent to using `mode=file`.


## Extending the Code
In order to use other types of video streams (e.g. security camera),
you can extend `VideoStreamBase` or `LocalVideoStream`
and override `getImage() -> numpy.ndarray` method
to define the procedure of getting a new frame.
Let's name the new class `SecurityCamera()`,
then simple do:  
```python
video = FaceDetector(SecurityCamera()); # if you override `VideoStreamBase` (works best in notebook or colab)
video = LocalFaceDetector(SecurityCamera()); # if you override `LocalVideoStream` (works best locally as it uses cv2.imshow)
video.download(display=True, limit=1000);
# display=True to display the video while downloading it
# limit=1000 to record 1000 frames
```


## Demos
[Online demo](https://i.imgur.com/2K3IZtj.mp4):
`mode=online`, using android camera, executed on colab.

[File demo](https://imgur.com/ur1eyb5.mp4):
`mode=file`, output presence file `zuhair-demo.csv`.

[Webcam demo](https://imgur.com/DaWxRIM.mp4):
`mode=webcam`, output presence file `simple-demo.csv`.

[Real-life video demo](https://youtu.be/sNtJhgIojtU):
`mode=file`, output presence file `contest-demo.csv`, executed on colab.


## Some Tips & Tricks
To run `mode=local`, download `IP Webcam` app on your phone.
Lunch the service in the app, let's refer to it by `ip_webcam:port`.
Set `camera_url` to `ip_webcam:port/shot.jpg`.
Run the code.

To run `mode=online`, download `IP Webcam` app on your phone.
Lunch the service in the app, let's refer to it by `ip_webcam:port`.
Expose this service on a public url
(using `ngrock` for example, by running
`winpty ngrok http port` or `ngrok http port`).  
In `configs.json` set `camera_url2 = ip_webcam:port/shot.jpg`,
`camera_url = ` the public url (e.g. `http://6e3a33e5.ngrok.io`).  
Lunch RESTful API service to expose mobile's camera
to the public url by running
`runipy lunch_service.ipynb`,
i.e. to forward `camera_url -> camera_url2`.
Run the code.





