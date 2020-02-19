# Basic-Dev Performance Practice Environment (BETA)

## Quick Start Ubuntu
1. Update Ubuntu repos and install docker and VSCode
```sh
sudo apt -y update
sudo apt -y install docker.io code
```
2. Install necessary VSCode extentions
```sh
code --install-extension ms-vscode-remote.remote-containers
```
3. Give current user docker permissions and reboot
```sh
sudo usermod -aG docker [insert user here]
reboot
```
4. Clone repo, change directory, and open project in VSCode
```sh
git clone --recurse-submodules https://gitlab.com/90COS/public/evaluation-prep/basic-dev-prac-env.git
cd basic-dev-prac-env && code .
```

## Quick Start Windows
1. Download and install [VSCode](https://code.visualstudio.com/)
2. Download and install the Remote-Development, C/C++, Python (Only Remote-Container if using Docker) extentions from the VSCode extentions store. You will need to open VSCode to access this (second from the last icon on the left pane)
3. Turn on Windows Subsystem for Linux (WSL) by following the instructions [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and use Ubuntu 18.04 LTS. Alternatively you can download and install [Docker Desktop](https://www.docker.com/products/docker-desktop) but this will not be an option if running Windows 10 Home. Make sure you share the project directory that you will be mounting the container to (Docker Desktop settings) if choosing this option.
4. (WSL Only) Once WSL is installed, start it by searching for "Ubuntu" in the Windows start menu. Once open the instance will initialize and ask for user information.
5. In WSL (or powershell if using Docker Desktop) Git clone the necessary repo, change directory, and open VSCode
```sh
git clone --recurse-submodules https://gitlab.com/90COS/public/evaluation-prep/basic-dev-prac-env.git
cd basic-dev-prac-env && code .
```
6. (WSL Only) Since WSL does not provision automatically like docker you will need to do this manually running the wsl.sh bash script.
```sh
cd .devcontainer && bash wsl.sh
```

### Next Steps
- (Docker Only) Once the project is open a notification toast will appear in the bottom right corner of the VSCode window. Click "Reopen in Container"
  - (Docker Only) Alternatively you can click the green button at the bottom left of the VSCode window and choose the same option
- (Docker Only) Wait Patiently... It may take 3-8 minutes depending on your hardware and network connection to initialize the container
- Once VSCode is running normally, you will be able to run tasks to execute "Clean", "Build C", and "Compile C". Debugging (third icon from the bottom on the left pane) can be run with the "Test C" or "Test Python" Debug configurations chosen from the dropdown.

NOTE: Running "Test C" (along with any compilation task) and "Test Python" will require you to have the file open and focused on (in view) or the tasks will not run correctly.

## Generating a Practice test
Once the environement is all set up and ready to go you will need to generate an initial practice test. Run the following command in the VSCode console (cntl+shift+`).
```sh
./createPracticeTest.py
```
WARNING: All previously worked on questions will be deleted, so save any work you do not want to lose.

### VSCode Tasks
Click the button labeled "Tasks" in the bottom blue bar to view tasks to execute. The task heirarchy is the following. These tasks are only for C Programming.
```sh
└─ Compile C
│   └─ Build C
└─ Clean 
```

### Features
- Lightweight and opensource C and Python development environment
- C build and compilation with CMake
- Debugging for C and Python
  - gdb debugging for C through VSCode GUI
  - Breakpoints, step through, etc.
  - Variable and Call Stack analysis
- Docker
  - Easy to deploy containerized dev environment
  - Wraps all extensions, libraries, and tools
  - It can be personalize

### Sources
- https://cmake.org/cmake/help/v3.13/
- https://code.visualstudio.com/docs/remote/containers
- https://code.visualstudio.com/docs/remote/containers-advanced
- https://code.visualstudio.com/docs/remote/wsl

# How to Contribute
As this environment is on the path to be used for the official Basic-Dev performance eval, there are many ways with different levels of involvement one can have to make a contribution.
1. If you encounter a problem anywhere, create an issue ticket on this repo. This will highlight the problem to the community and act as a focalpoint to track progress as our team resolves it.
2. Create an issue ticket, create a branch from the ticket, fix the problem, and submit a merge request. Our team will analyze the changes and merge it into the project. 

Our team is small and working on many different projects. Your contribution will help tremendously.
