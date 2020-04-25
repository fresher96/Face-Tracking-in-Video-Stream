
import config_file;
import import_ipynb;
import main;

if __name__ == '__main__':
    configs = config_file.readConfigs();

    mode = configs['mode']
    print('mode:', mode);

    if(mode == 'online'):
        pass;
    elif(mode == 'offline'):
        pass;
    elif(mode == 'webcam'):
        pass;
    else:
        video = LocalFaceDetector(WebCam());
        video.download(display=True, limit=1000);

