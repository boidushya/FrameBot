import cv2
from os.path import realpath as path
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
    if not os.path.exists('frames'):
        os.mkdir('frames')
    file = os.listdir('assets/video')[0]
    videoFile = path(f"assets/video/{file}")
    Rate = 5
    cap = cv2.VideoCapture(videoFile)
    frameRate = cap.get(Rate)
    x=1
    while(cap.isOpened()):
        frameId = cap.get(1)
        ret, frame = cap.read()
        if (ret != True):
            break
        if (int(frameId) % int(math.floor(frameRate)) == 0):
            filename = path(f"frames/frame{int(x):04}.jpg")
            x+=1
            cv2.imwrite(filename, frame)

        cap.release()
        print("Frames extracted successfully!")

@catch_exceptions()
def post(dir = os.listdir("frames")):
    with open("assets/retain","a+") as f:
        f.seek(0)
        filled = f.read(1)
        if not filled:
            totalFrames = str(len(dir))
            f.write(totalFrames)
        else:
            f.seek(0)
            totalFrames = str(f.readline())

    currentFrame = path(f'frames/{dir[0]}')
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
    schedule.every().hour.do(post).run()

    while 1:
        schedule.run_pending()
        time.sleep(1)
