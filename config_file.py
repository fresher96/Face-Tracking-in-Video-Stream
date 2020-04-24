

# online setting
# cameraUrl   = 'http://eeba6d36.ngrok.io';
# drive       = 'drive/My Drive/';
# models = ['cnn', 'large'];

# local setting
drive       = 'E:/CLCs/drive/';
cameraUrl   = 'http://192.168.0.103:8080/shot.jpg';
models = ['hog', 'small'];


videoFile   = drive + 'colab/videos/sample4.mp4'
facesDir    = drive + 'colab/faces/'
videosDir   = drive + 'colab/videos/'
outputFile  = drive + 'colab/output.mp4'

def get_configs():
	# online setting
	# cameraUrl   = 'http://eeba6d36.ngrok.io';
	# drive       = 'drive/My Drive/';
	# models = ['cnn', 'large'];

	# local setting
	drive       = 'E:/CLCs/drive/';
	cameraUrl   = 'http://192.168.0.103:8080/shot.jpg';
	models = ['hog', 'small'];


	videoFile   = drive + 'colab/videos/sample4.mp4'
	facesDir    = drive + 'colab/faces/'
	videosDir   = drive + 'colab/videos/'
	outputFile  = drive + 'colab/output.mp4'
	
	ret = {};
	ret['cameraUrl'] = cameraUrl;
	ret['drive'] = drive;
	ret['models'] = models;
	ret['videoFile'] = videoFile;
	ret['outputFile'] = outputFile;

	
	return ret;

