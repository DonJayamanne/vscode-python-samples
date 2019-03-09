# Remote Debugging Sample (on the same Machine)

## Setup your remote environment
### Step 1: Build docker image and run it
* Open a terminal window
* Type the following command in the terminal window
`docker build -t remote-debugging-docker .`
* Type the following command in the terminal window
`docker run -it -p 3000:3000 remote-debugging-docker`
* Confirm the following is displayed in the terminal window
`Waiting to attach`

## Setup your local environment
### Step 1: Open the workspace in your local environment
* This step will ensure you have setup the program to be debugged locally.
* You do not to setup the Python environment locally to debug a remote environment.

### Step 2: Attach the debugger
* Open `sample.py`
* Add a breakpoint to the line `print("attached")`
* Go into the debugger menu and select `Python: Attach` and press the green arrow icon 
* Wait for around 2 seconds and the debugger should hit at the breakpoint
