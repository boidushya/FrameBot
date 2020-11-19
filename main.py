# This code was written by Boidushya Bhattacharya and Gustav Wallström (github/sudoxd) on Monday, 26 November 2019 at 20:27 p.m.
# Reddit: https://reddit.com/u/Boidushya
# Facebook: https://facebook.com/soumyadipta.despacito

import cv2
import os
import math
import facebook
import functools
import schedule
import time
import fnmatch
import sys

#You can confing in here
frameDes = f"Unus Annus by Deleted Channel - Frame $curent/$max" # input $curent when 
frameHour = False # When frameHour true, frame upload again in 1 hour
frameDuration = 3 # in minutes
backupFrame = True # frame can move to frame_bkp folder when upload successfully
backupVideo = True # video can move to video_bkp folder when extracting completed
required_fps = 2  # if you want you can change the FPS for your video here
# The more the fps, the more number of frames



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

def clear():
    time.sleep(2)
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
    print("For stoping program, press CTRL+C or Command+C")
    print("")

def extractFrames():
    file = os.listdir('./assets/video')[0]
    videoFile = f"./assets/video/{file}"
    if os.path.exists("./assets/frames/*.jpg"):
        os.remove("./assets/frames/*.jpg")
    vidcap = cv2.VideoCapture(videoFile)
    success, image = vidcap.read()
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    multiplier = round(fps/required_fps)
    x = 0
    if backupFrame == True:
        if not os.path.exists("./assets/video_bkp"):
            os.mkdir('./assets/video_bkp')
        os.replace(videoFile, f'assets/video_bkp/{file}')
    else:
        os.remove(videoFile)

    while success:
        frameId = int(round(vidcap.get(1)))
        success, image = vidcap.read()

        if frameId % multiplier == 0:
            x += 1
            cv2.imwrite(f"assets/frames/frame{int(x):06d}.jpg", image)
    vidcap.release()


@catch_exceptions()
def post():
    dir = os.listdir("./assets/frames")
    # forgot to sort the files before, pls forgive me lol
    dir.sort(key=lambda t: int(t[5:-4]))
    with open("./assets/retain", "a+") as f:
        f.seek(0)
        filled = f.read(1)
        if not filled:
            totalFrames = str(len(dir))
            f.write(totalFrames)
        else:
            f.seek(0)
            totalFrames = str(f.readline())

    currentFrame = f'assets/frames/{dir[0]}'
    currentFrameNumber = str(int(dir[0][5:-4]))
    frameDes1 = frameDes.replace("$curent", str(currentFrameNumber))
    if "$max" in frameDes:
        frameDes1 = frameDes1.replace("$max", str(totalFrames))
    msg = frameDes1
    with open('assets/token.txt', 'r') as token:
        accesstoken = token.readline()
    graph = facebook.GraphAPI(accesstoken)
    post_id = graph.put_photo(image=open(
        currentFrame, 'rb'), message=msg)['post_id']
    print(f"Submitted post with title \"{msg}\" successfully!")
    if backupFrame == True:
        if not os.path.exists("./assets/frame_bkp"):
            os.mkdir('./assets/frame_bkp')
        os.replace(currentFrame, f'assets/frame_bkp/{dir[0]}')
    else:
        os.remove(currentFrame)


if __name__ == '__main__':
    token = open('./assets/token.txt', 'r')
    if token.readline() == "putyourtokenherexdd":
        print("put your access token in assets/token.txt. check generateToken.md for get token")
        sys.exit("error no token")
    if "$curent" not in frameDes:
        print("add $curent when this program working")
        sys.exit("error string")
    if not os.path.exists("./assets/video"):
        os.mkdir('./assets/video')
    dir = os.listdir("./assets/video")
    if len(dir) == 0:
        if not os.path.exists('./assets/frames'):
            os.mkdir('./assets/frames')
        dir = os.listdir("./assets/frames")
        if len(dir) == 0:
            print("add a video in assets/video directory")
            sys.exit("error no video")
        else:
            clear()
    else:
        dir = os.listdir("./assets/frames")
        if len(dir) == 0:
            print("extracting video to frame...")
            if os.path.exists("./assets/retain"):
                os.remove("./assets/retain")
            extractFrames()
            clear()
        else:
            clear()
    # ans = input("Extract Frames?(y/n) \n>")
    # if 'y' in ans.lower():
    #     if os.path.exists("./assets/retain"):
    #         os.remove("./assets/retain")
    #     extractFrames()
    # else:
    #     pass
    if frameHour == True:
        schedule.every().hour.do(post).run()
    else:
        schedule.every(frameDuration).minutes.do(post).run()


    while 1:
        dir = os.listdir("./assets/frames")
        if len(dir) == 0:
            print("")
            sys.exit("all frames uploaded")
        else:
            schedule.run_pending()
            try:
                time.sleep(1)    
            except KeyboardInterrupt:
                print("")
                sys.exit("program stopped by user")