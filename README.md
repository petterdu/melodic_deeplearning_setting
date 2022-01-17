# melodic_deeplearning_setting

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
$ nvidia -smi
```
그래픽카드 경로 작성
```
vim ~/.bashrc
```
>* NVIDIA CUDA toolkit   
> export PATH=/usr/local/cuda-11/bin:$PATH   
> export LD_LIBRARY_PATH=/usr/local/cuda-11/lib64
```
source ~/.bashrc
```
### CUDADNN 11.5 설치

[Nvidia developer 공식 홈페이지](https://developer.nvidia.com/cudnn)
> Login > Download cuDNN Click > 'I Agree To the Terms of the cuDNN Software License Agreement' Check   
> > Download 하단 'Archived cuDNN Releases' Click > 'Download cuDNN v8.3.1 (November 22nd, 2021), for CUDA 11.5' Click
> > 'Local Installer for Linux x86_64 (Tar)' Download
