# Pre-requesites:
- Install python
- On Mac download and install homebrew first

### Inside terminal once brew is installed:
- `brew info` , to check if brew is installed
- `brew install python3`, use homebrew to installs latest version of python and pip

### check python installed by running command in terminal:
- `python3 -version`

### Install packages needed to run test in command terminal:
- `pip3 install -U pytest`, to install pytest
- `pip3 install requests`, to install requests packages
- `pip3 install pytest-html`, to install html test execution reporter

### run from terminal
- `pytest -v -s --html=report.html --self-contained-html`
