# melodic_deeplearning_setting

## 편의 소프트웨어(chrome,Anydesk,Visual Studio Code, terminator) 설치

### Chrome 설치
```
$ wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
$ sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
$ sudo apt-get update
$ sudo apt-get install google-chrome-stable
$ sudo rm -rf /etc/apt/sources.list.d/google.list
$ sudo apt-get clean
$ sudo apt-get update
```

### Anydesk 설치

```
$ sudo apt update
$ sudo apt -y upgrade
$ wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | sudo apt-key add -
$ echo "deb http://deb.anydesk.com/ all main" | sudo tee /etc/apt/sources.list.d/anydesk-stable.list
$ sudo apt update
$ sudo apt install anydesk
```

### Visual Studio Code 설치

> ➔ Ubuntu Software Click ➔ 검색창에 'code' 입력 ➔ ‘Visual Studio Code’ ➔ 사용자 비밀번호 입력  ➔ 'install' Click
> ➔  'Unable to install "Visual Studio Code": snap "code" has "install-snap" change in progress' 문구 발생 시 다음과 같이 터미널 창에서 실행
```
$ snap changes
```
> 이후 기다리거나 다시 다운로드 하면 정상 설치 됨


### terminator 설치
```
$ sudo apt-get install terminator
```

## 외장 그래픽 카드 설치

### 최신버전 CUDA Toolkit 설치

[Nvidia 주소](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=18.04&target_type=deb_local)

```
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
$ sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
$ wget https://developer.download.nvidia.com/compute/cuda/11.6.0/local_installers/cuda-repo-ubuntu1804-11-6-local_11.6.0-510.39.01-1_amd64.deb
$ sudo dpkg -i cuda-repo-ubuntu1804-11-6-local_11.6.0-510.39.01-1_amd64.deb
$ sudo apt-key add /var/cuda-repo-ubuntu1804-11-6-local/7fa2af80.pub
$ sudo apt-get update
$ sudo apt-get -y install cuda
```

### CUDA Toolkit 11.5.1 설치 (GTX 3060 기준으로 진행 시)
[CUDA Toolkit 이전 버전 주소](https://developer.nvidia.com/cuda-toolkit-archive)   
[Nvidia 주소](https://developer.nvidia.com/cuda-11-5-1-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=18.04&target_type=deb_local)

```
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
$ sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
$ wget https://developer.download.nvidia.com/compute/cuda/11.5.1/local_installers/cuda-repo-ubuntu1804-11-5-local_11.5.1-495.29.05-1_amd64.deb
$ sudo dpkg -i cuda-repo-ubuntu1804-11-5-local_11.5.1-495.29.05-1_amd64.deb
$ sudo apt-key add /var/cuda-repo-ubuntu1804-11-5-local/7fa2af80.pub
$ sudo apt-get update
$ sudo apt-get -y install cuda
```
Nvidia & Cuda Toolkit 버전 확인
```
$ nvcc -V
$ nvidia-smi
```
그래픽카드 경로 작성
```
$ vim ~/.bashrc
```
> * NVIDIA CUDA toolkit   
> export PATH=/usr/local/cuda-11/bin:$PATH   
> export LD_LIBRARY_PATH=/usr/local/cuda-11/lib64
```
$ source ~/.bashrc
```
### CUDADNN 11.5 설치

[Nvidia developer 공식 홈페이지](https://developer.nvidia.com/cudnn)
> Login ➔ Download cuDNN Click ➔ 'I Agree To the Terms of the cuDNN Software License Agreement' Check   
> ➔ Download 하단 'Archived cuDNN Releases' Click ➔ 'Download cuDNN v8.3.1 (November 22nd, 2021), for CUDA 11.5' Click
> ➔ 'Local Installer for Linux x86_64 (Tar)' Download
```
$ cd Downloads/
$  tar -xvf cudnn-linux-x86_64-8.3.2.44_cuda11.5-archive.tar.xz
#cudnn  관련 파일 위치 cuda 디렉토리로 이동
$ sudo cp cudnn-*-archive/include/cudnn*.h /usr/local/cuda/include
$ sudo cp -P cudnn-*-archive/lib/libcudnn* /usr/local/cuda/lib64
$ sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*

$ sudo ldconfig

# cudnn check version

>8.0 dlgk
$ cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
>8.0 dltkd
$ cat /usr/local/cuda/include/cudnn_version.h | grep CUDNN_MAJOR -A 2
```

## Anaconda install
[Anaconda 공식 홈페이지](https://www.anaconda.com/products/individual)   
[Anaconda 이전 버전 주소](repo.anaconda.com/archive/)   
> Anaconda 공식 홈페이지 ➔ download Click 

```
$ cd Downloads/
$ chmod -R 777 *
$ bash Anaconda3-2021.11-Linux-x86_64.sh
```
> 'Please, press ENTER to continue' 문구가 나오면 Enter ➔ 'Do you accept the license terms? [yes|no]' 문구가 나오면 'yes'라고 터미널 창에 입력
> ➔ 그다음 ENTER를 눌러 기본 경로로 설치 진행 (설치 경로 입력 가능) ➔ 이후  'by running conda init? [yes|no]' 문구가 나오면 'yes'를 눌러 anaconda 초기화 진행

```
no change /root/anaconda3/condabin/conda
no change /root/anaconda3/bin/conda
no change /root/anaconda3/bin/conda-env
no change /root/anaconda3/bin/activate
no change /root/anaconda3/bin/deactivate
no change /root/anaconda3/etc/profile.d/conda.sh
no change /root/anaconda3/etc/fish/conf.d/conda.fish
no change /root/anaconda3/shell/condabin/Conda.psm1
no change /root/anaconda3/shell/condabin/conda-hook.ps1
no change /root/anaconda3/lib/python3.8/site-packages/xontrib/conda.xsh
no change /root/anaconda3/etc/profile.d/conda.csh
no change /root/.bashrc 
No action taken. 
If you'd prefer that conda's base environment not be activated on startup, set the auto_activate_base parameter to false: 
conda config --set auto_activate_base false 
Thank you for installing Anaconda3! 
=========================================================================== 
Working with Python and Jupyter notebooks is a breeze with PyCharm 
Professional! Code completion, Notebook debugger, VCS support, SSH, Docker, 
Databases, and more! Get a free trial at: https://www.anaconda.com/pycharm

$ 
```

### Anaconda 경로 수정
```
$ vim ~/.bashrc
```
> 설치 후 bashrc에는 다음과 같이 작성이 되어있을텐데, 이후 python default가 anaconda로 잡히는 현상이 일어나 다음과 같이만 적고   
> export PATH=/root/anaconda3/bin:$PATH 문구는 따로 작성 안함
```
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/kmw/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/kmw/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/kmw/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/kmw/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

```
$ source ~/.bashrc
```
### Anaconda auto starting False Setting
> 새 터미널 창을 열때마다 Anaconda 연결 되는 현상 해제 (앞에 base 콘다 환경으로 들어가는 현상) 
```
$ conda config --set auto_activate_base False
$ source ~/.bashrc
```
### Anaconda Uninstall (필요 시)

```
$ conda install anaconda-clean
$ anaconda-clean
$ rm -rf ~/anaconda3
$ rm -rf ~/.anaconda_backup
```

## ROS(Melodic) 설치

```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
$ sudo apt update
$ sudo apt install ros-melodic-desktop-full
$ apt search ros-melodic
$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
$ sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
$ sudo apt install python-rosdep
$ sudo rosdep init
$ rosdep update
$ roscore
$ sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace
$ cd ..
$ catkin_make
$ pip install -U catkin_tools
```

## bashrc command input

```
alias eb='code . ~/.bashrc'
alias sb='source ~/.bashrc'
alias cs='cd ~/catkin_ws/src'
alias cm='cd ~/catkin_ws && catkin_make'
```


## Husky_ur3 설치

> https://github.com/QualiaT/husky_ur3_simulator 참조


## cnn 필요 패키지 설치

```
# yaml install

$ pip install pyyaml

# rospkg install

$ pip install -U rospkg

# cv2 install

$ sudo apt install build-essential cmake git pkg-config libgtk-3-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev gfortran openexr libatlas-base-dev python3-dev python3-numpy libtbyab2 libtbb-dev libdc1394-22-dev
$ mkdir ~/opencv && cd ~/opencv
$ git clone https://github.com/opencv/opencv.git
$ git clone https://github.com/opencv/opencv_contrib.git
$ cd ~/opencv/opencv
$ mkdir build && cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv/opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON .. 
$ sudo make -j8
$ sudo make install

# cv_Bridge install

$ sudo apt-get install python3-pip python3-yaml
$ sudo pip3 install rospkg catkin_pkg
$ cd
$ mv ~/catkin_ws/src/ ~/backup/
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ git clone -b melodic https://github.com/ros-perception/vision_opencv.git
$ cd ..
$ catkin_init
$ catkin clean -y
$ catkin_make --only-pkg-with-deps vision_opencv -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so
$ catkin_make install
$ source install/setup.bas --extend
$ rm -rf ~/catkin_ws/build
$ rm -rf ~/catkin_ws/devel
$ cd src/
$ sudo rm -rf vision_opencv
$ cp -arpf ~/backup/src ~/catkin_ws
$ rm -rf ~/backup/src/
$ cd ~/catkin_ws/
$ catkin_make
$ sb
```

# ocr-rcnn install

> https://github.com/supertigim/elevator_buttons_recognition.git 참조

```
$ git clone https://hub.com/supertigim/elevator_buttons_recognition.git
$ cd ~/catkin_ws/
$ catkin_make 
$ ~/catkin_ws/src/deep_pakage/scripts

>> ocr-rcnn README 참조 (conda 생성)

$ conda create -n detection python=3.7 pyqt=5
$ conda activate detection
$ pip install -r requirements.txt 
$ cd addons
$ cd labelImg 
$ pip install -r requirements/requirements-linux-python3.txt

# 여기부터는 꼭 해야하는지 확인 필요

$ cd ../..
$ sudo apt-get install protobuf-compiler
$ cd models/research
$ wget -O protobuf.zip https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip
$ unzip protobuf.zip
$ protoc object_detection/protos/*.proto --python_out=.
$ export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

```


# yolo darknet_ros 설치

> https://github.com/leggedrobotics/darknet_ros 참조
> 본인 GPU에 맞게 darknet ros cmakelists 에 수정 필요
> 3060의 경우 https://en.wikipedia.org/wiki/CUDA#Supported_GPUs 확인해보면 Compute capability 가 8.6임을 확인할 수 있다.
> 이에 맞게 darknet ros cmakelists 23 line cuda nvcc flags 부분에
> -gencode arch=compute_86,code=sm_86 입력

$ cd catkin_workspace/src
$ git clone --recursive git@github.com:leggedrobotics/darknet_ros.git
$ cd ../
$ catkin_make -DCMAKE_BUILD_TYPE=Release
$ rospack profile

# object tracker, push_button, audio_saying 등 실행 스크립트 설치

> object tracker 의 상세 설명이 필요한 경우 https://github.com/QualiaT/object_tracker 참조

$ git clone https://github.com/petterdu/melodic_deeplearning_setting.git

