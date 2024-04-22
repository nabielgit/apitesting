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
- Make sure Docker engine is Docker-linux in settings.

Execute commands:

To build image, name it using -t pythonpytestapi and -f for Dockerfile 

`docker build -t pythonpytestapi -f Dockerfile .` 

To run, -it interactive terminals, --name for container name, pythonpytestapi is the image name in this case

`docker run -it --name pythonpytestapi pythonpytestapi` 

### Go to Docker desktop application
- Select images 
- Select pythonpytestapi 
- Hit run to create container