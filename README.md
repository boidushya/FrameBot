# FrameBot

## Requirements
* Download Python3 from https://www.python.org/downloads/
* Install according to your operating system, check [here](https://realpython.com/installing-python)
* Install required packages `sudo pip3 install -r requirements.txt`

## How to use:
* Make a page on facebook
* ~~Head over to http://maxbots.ddns.net/token/ and get the access token for your page~~
* [Checkout this tutorial](tutorial/generateToken.md)
* Copy the token and paste it in assets/token.txt
* Place the video in assets/video
* Open main.py in Code application (or NotePad), and configuration in the space provided (read [this](tutorial/configuration.md) for information)
* Open your Terminal/Powershell(as administrator)/Command Prompt(as administrator) in the main folder of this repository
* Run `python3 main.py` if you're using Windows, or `sudo python3 main.py` if you're using Mac/Linux
* Enjoy!

## Warning!
* After setting everything up you have to host the bot somewhere, i.e, let it run by itself without having to close the script. Preferably you could do it on a VPS like Amazon's EC2/Lambda and Google Cloud, although I personally would prefer EC2 with Amazon Linux(CentOS 7).

**Note** : You can also host it in your PC/laptop but it will tremendously slow your workflow. An old laptop/pc/raspberry pi is ideal as well
* As of now the script can only process single episodes/movies. The source code for whole series can be obtained by supporting me at https://www.patreon.com/etjfo
* Don't hesitate to hit me up here if you face any problems or if you donated at semolini#2344 (discord)
* When extracting the video, there will be an error on the [following link](https://github.com/numpy/numpy/issues/16744). ~~To fix this, install numpy version 1.19.3 by running the command `sudo pip3 install numpy==1.19.3`~~ nummpy 1.19.3 now installed in requirements.txt

**Most Importantly** : DO NOT TRY TO SCHEDULE IT MANUALLY FOR EVERY ONE MINUTE! There is a reason why I set it to 1 hour.
You can set it to a MINIMUM of 30 minutes if you like, **DO NOT TRY TO SET IT TO 1 MINUTE OR 5 MINUTES WHATSOEVER**

If anything happens to your facebook account after lowering time interval any further, ***I'M NOT RESPONSIBLE***
