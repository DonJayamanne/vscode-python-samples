# Remote Debugging Sample (on the same Machine)

## Setup your remote environment
### Step 1: Open the workspace in your remote environment
* This step will ensure you have setup the program to be executed in the remote environment.

### Step 2: Configure VS Code to use a Python environment
* Open a terminal window
* Type the following command in the terminal window
`virtualenv --python=python3.6 .env`
* Reload VS Code using the command `Reload Window` (from your [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette))
* Open the file `sample.py`
* Select the command `Python: Select Interpteter` and select the Python environment created above (found in `./.env` directory created above)

### Step 3: Install PTVSD version 3.0.0
* Open a terminal using the command [Python: Create Terminal](https://code.visualstudio.com/docs/python/environments#_activating-an-environment-in-the-terminal) (from your [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette))
* Enter the following command in the above terminal
    `python -m pip install ptvsd==3.0.0`

### Step 4: Start program to be debugged
* Run the file `sample.py` in the Python environment containing PTVSD
    * Option 1:
        * Open the file `sample.py`
        * Right click on editor window and select the menu `Run Python File in Terminal`
    * Option 2:
        * Open a terminal using the command [Python: Create Terminal](https://code.visualstudio.com/docs/python/environments#_activating-an-environment-in-the-terminal) (from your [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette))
        * Enter the following command in the above terminal
        `python sample.py`
* Now, the above program is running and waiting for a debugger to attach to it

## Setup your local environment
### Step 1: Open the workspace in your local environment
* This step will ensure you have setup the program to be debugged locally.
* You do not to setup the Python environment locally to debug a remote environment.

### Step 2: Update the IP Address in `launch.json` (`"host": "localhost"`)
* Identify the IP Address of your remote environment.
* Open `.vscode/launch.json` and replace the value of the setting `host` from `localhost` to the IP address identified earlier.

### Step 3: Update the remote folder in `launch.json` (`"remoteRoot": "${workspaceFolder}",`)
* Identify the full path to the directory containing the file `sample.py` in your remote environment.
* Open `.vscode/launch.json` and replace the value of the setting `remoteRoot` from `${workspaceFolder}` to the path identified earlier.

### Step 4: Attach the debugger
* Open `sample.py`
* Add a breakpoint to the line `print("attached")`
* Go into the debugger menu and select `Python: Attach` and press the green arrow icon 
* Wait for around 2 seconds and the debugger should hit at the breakpoint

## Troubleshooting
* Have you started the `sample.py`?
* Check whether the debugger is listening on port 3000 using the commands 
    * Use a command line tool such as `netstat` or any other
    * `netstat -an -p tcp | grep 3000` or `netstat -ano | find "3000"`
* Check whether you are able to connect to the above port
    * Use a command line tool such as `telnet` or `nc` or any other
    * `telnet <Remote IPAddress> 3000` or `nc <Remote IPAddress> 3000`
