

## set your configureations in this file
## no need to change `get_configs` function


database 	= './database/';
db_images 	= database + 'Images/';
db_faces 	= database + 'Face.json';
db_person 	= database + 'Person.json';
db_presence = database + 'Presence.json';


# online setting
# cameraUrl   = 'http://eeba6d36.ngrok.io';
# drive       = 'drive/My Drive/';
# models 		= ['cnn', 'large'];

# local setting
drive       = 'E:/CLCs/drive/';
cameraUrl   = 'http://192.168.0.103:8080/shot.jpg';
models 		= ['hog', 'small'];


videoFile   = drive + 'colab/videos/sample4.mp4'
facesDir    = drive + 'colab/faces/'
videosDir   = drive + 'colab/videos/'
outputFile  = drive + 'colab/output.mp4'





def get_configs():

	ret = {};

	ret['database'] 	= database;
	ret['db_images'] 	= db_images;
	ret['db_faces'] 	= db_faces;
	ret['db_person'] 	= db_person;
	ret['db_presence'] 	= db_presence;

	ret['cameraUrl'] 	= cameraUrl;
	ret['drive'] 		= drive;
	ret['models'] 		= models;

	ret['videoFile'] 	= videoFile;
	ret['facesDir'] 	= facesDir;
	ret['videosDir'] 	= videosDir;
	ret['outputFile'] 	= outputFile;

	
	return ret;

