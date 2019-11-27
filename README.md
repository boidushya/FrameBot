# FrameBot

## Requirements
* Python3 Download Python3 from https://www.python.org/downloads/
* OpenCV pip install opencv-python
* Facebook-SDK pip install facebook-sdk
* Schedule pip install schedule

## How to use:
* Make a page on facebook
* Head over to http://maxbots.ddns.net/token/ and get the access token for your page
* Copy the token and paste it in assets/token.txt
* Place the video in assets/video
* Open your Terminal/Powershell(as administrator)/Command Prompt(as administrator) in the main folder of this repository
* Run python3 main.py or sudo python3 main.py if you are on a Mac/Linux
* Enjoy!

## Warning!
* After setting everything up you have to host the bot somewhere, i.e, let it run by itself without having to close the script. Preferably you could do it on a VPS like Amazon's EC2/Lambda and Google Cloud, although I personally would prefer EC2 with Ubuntu. Here's some helpful documentation regarding EC2
**Note** : You can also host it in your PC/laptop but it will tremendously slow your workflow. An old laptop/pc is ideal as well
* As of now the script can only process single episodes/movies. The source code for whole series can be obtained by becoming my patreon at https://www.patreon.com/etjfo
* Don't hesitate to hit me up here if you face any problems
