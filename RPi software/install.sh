sudo mkdir /usr/Weather_service
sudo mv RPi\ software/main_ACM0.py /usr/Weather_service
sudo mv RPi\ software/autorun.sh /usr/Weather_service
sudo mkdir /usr/Weather_service/Data
sudo touch /usr/Weather_service/Data/data.txt
sudo mv RPi\ software/croninfo /etc
sudo crontab croninfo 

