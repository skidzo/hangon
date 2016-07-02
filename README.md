install vagrant
---------------

mkdir my-dev
cd my-dev
vagrant init larryli/vivid64

edit the Vagrantfile:
  config.vm.network "public_network"

  # If true, then any SSH connections made will enable agent forwarding.
  # Default value: false
  config.ssh.forward_agent = true
  config.ssh.forward_x11 = true


  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "1024"]
  end

#####################################################
cd my-dev
vagrant up
vagrant ssh
#####################################################
everything is done inside a virtual machine

1. Kivy-Install-Process

sudo apt-get install xterm

sudo apt-get update
sudo apt-get install build-essential libssl-dev libffi-dev python-dev python-pip

sudo apt-get install -y \
    python-pip \
    build-essential \
    git \
    python \
    python-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev

sudo add-apt-repository ppa:kivy-team/kivy
sudo apt-get update
sudo apt-get install python-kivy

now test mini-kivy app  (Should run !!!)

2. buildozer-Install Process

sudo pip install --upgrade cython==0.21
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install build-essential ccache git libncurses5:i386 libstdc++6:i386 libgtk2.0-0:i386 libpangox-1.0-0:i386 libpangoxft-1.0-0:i386 libidn11:i386 python2.7 python2.7-dev openjdk-7-jdk unzip zlib1g-dev zlib1g:i386

sudo apt-get install python3-pip
pip3 install --upgrade buildozer

goto project folder
-------------------

copy .spec file
export PATH=/home/vagrant/.local/bin:$PATH
run:
buildozer -v android debug

#######################################################
outside the virtual machine (USB-Debugging)
adb devices
cd my-dev/myproject/bin
adb install -r test.apk
adb logcat -d | grep -w python