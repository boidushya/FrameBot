#This code was written by Boidushya Bhattacharya on Monday, 26 November 2019 at 20:27 p.m.
#Reddit: https://reddit.com/u/Boidushya
#Facebook: https://facebook.com/soumyadipta.despacito

import cv2
import os
import math
import facebook
import functools
import schedule
import time

def catch_exceptions(cancel_on_failure=False):
    def catch_exceptions_decorator(job_func):
        @functools.wraps(job_func)
        def wrapper(*args, **kwargs):
            try:
                return job_func(*args, **kwargs)
            except:
                import traceback
                print(traceback.format_exc())
                if cancel_on_failure:
                    return schedule.CancelJob
        return wrapper
    return catch_exceptions_decorator

def extractFrames():
    file = os.listdir('assets/video')[0]
    videoFile = f"assets/video/{file}"
    if not os.path.exists('assets/frames'):
        os.mkdir('assets/frames')
    vidcap = cv2.VideoCapture(videoFile)
    success,image = vidcap.read()
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    required_fps =2 #if you want you can change the FPS for your video here
    #The more the fps, the more number of frames
    multiplier = round(fps/required_fps)
    x=0

    while success:
        frameId = int(round(vidcap.get(1)))
        success, image = vidcap.read()

        if frameId % multiplier == 0:
            x+=1
            cv2.imwrite(f"assets/frames/frame{int(x):04}.jpg", image)

    vidcap.release()


@catch_exceptions()
def post(dir = os.listdir("assets/frames")):
    with open("assets/retain","a+") as f:
        f.seek(0)
        filled = f.read(1)
        if not filled:
            totalFrames = str(len(dir))
            f.write(totalFrames)
        else:
            f.seek(0)
            totalFrames = str(f.readline())

    currentFrame = f'assets/frames/{dir[0]}'
    currentFrameNumber = str(int(currentFrame[-8:-4]))
    msg = f"Frame {currentFrameNumber} out of {str(totalFrames)}"
    with open('assets/token.txt','r') as token:
        accesstoken = token.readline()
    graph = facebook.GraphAPI(accesstoken)
    post_id = graph.put_photo(image=open(currentFrame, 'rb'),message = msg)['post_id']
    print(f"Submitted post with title \"{msg}\" successfully!")
    os.remove(currentFrame)

if __name__ == '__main__':
    ans = input("Extract Frames?(y/n) \n>")
    if 'y' in ans.lower():
        extractFrames()
    else:
        pass
    schedule.every().minute.do(post).run()

    while 1:
        schedule.run_pending()
        time.sleep(1)
