# Pre-requesites:
- Install python
- On Mac download and install homebrew first

### Inside terminal once brew is installed:
- `brew info` , to check if brew is installed
- `brew install python3`, use homebrew to install latest version of python and pip

### check python installed by running command in terminal:
- `python3 -version`

### Install packages needed to run test in command terminal:
- `pip3 install -U pytest`, to install pytest
- `pip3 install requests`, to install requests packages
- `pip3 install pytest-html`, to install html test execution reporter

### run from terminal
- `pytest -v -s --html=report.html --self-contained-html`

## Install and build Docker
- Create a file called Dockerfile in local directory.
- Download and Install Docker Desktop.
- Go to settings in Docker desktop. Go to builds, make sure it is set to Desktop-linux in settings.

### Execute commands in terminal:

To build image, name it using -t pythonpytestapi and -f for Dockerfile 

`docker build -t pythonpytestapi -f Dockerfile .` 

To run, -it interactive terminals, --name for container name, pythonpytestapi is the image name in this case

`docker run -it --name pythonpytestapi pythonpytestapi` 

### Go to Docker desktop application
- Select Images 
- Select pythonpytestapi 
- Hit run to create container
- Go to Containers
- Select container and hit run