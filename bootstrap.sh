#!/usr/bin/env bash

APP_NAME=writersleague
REPO=writersleague
USERNAME=miriad
GIT_PASSWORD=dp0KYgkEckPfqXMbQkg4nvk+SM
USER_PASSWORD=DCRescew343faw3+


# create user
adduser $USERNAME
echo $USER_PASSWORD | passwd $USERNAME --stdin

# read -p "Please Enter Your Real Name: " $REAL_NAME 
# read -p "Please Enter Your User Name: " $USER_NAME 
# useradd -c "${COMMENT}" -m ${USER_NAME} 
# read -p "Please Enter Your Password: " $USER_PASSWORD
# echo -e "$USER_PASSWORD\n$USER_PASSWORD" |passwd "$USER_NAME"
# passwd -e ${USER_NAME}



usermod -aG sudo $USERNAME
sudo usermod -a -G docker $USERNAME

# switch to new user home directory
su - miriad
# mkdir key dir with correct permissions
mkdir ~/.ssh
chmod 700 ~/.ssh
# paste key into authorized_keys file and add permissions
touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

exit

cp ~/.ssh/authorized_keys /home/$USERNAME/.ssh/authorized_keys
chown $USERNAME:$USERNAME /home/$USERNAME/.ssh/authorized_keys
chown $USERNAME:$USERNAME /home/$USERNAME/

# clone the repo
cd /home/$USERNAME
git clone https://sensorseverywhere:$GIT_PASSWORD@gitlab.com/sensorseverywhere/$REPO.git $APP_NAME


git clone https://sensorseverywhere:dp0KYgkEckPfqXMbQkg4nvk+SM@gitlab.com/sensorseverywhere/$REPO.git