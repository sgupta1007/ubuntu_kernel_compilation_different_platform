# ubuntu_kernel_compilation_different_platform
linux kernel is compiled in normal machine,virtual machine and docker and performance is observed

RUN dependencies.sh for compiling code in virtual machine or native machine
RUN dependencies_docker.sh for compiling code in docker platform

RUN pip install -r requirements.txt to install dependencies

RUN main.py to execute run for 1 time
RUN 5times main.py to analyse result for particular platform
