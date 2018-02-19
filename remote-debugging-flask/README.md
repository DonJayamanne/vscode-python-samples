# Remote Debugging Sample (on the same Machine)

## Setup your remote environment
### Step 1: Open the workspace in your remote environment
* This step will ensure you have setup Flask to be executed in the remote environment.

### Step 2: Configure VS Code to use a Python environment
* Open a terminal window
* Type the following command in the terminal window
`virtualenv --python=python3.6 .env`
* Reload VS Code using the command `Reload Window` (from your [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette))
* Open the file `app.py`
* Select the command `Python: Select Interpteter` and select the Python environment created above (found in `./.env` directory created above)

### Step 3: Install Flask and PTVSD version 3.0.0
* Open a terminal using the command [Python: Create Terminal](https://code.visualstudio.com/docs/python/environments#_activating-an-environment-in-the-terminal) (from your [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette))
* Enter the following command in the above terminal
    `python -m pip install flask ptvsd==3.0.0`

### Step 4: Start flask to be debugged
* Run the Flask application
    * Option 1:
        * Go into the debugger menu and start debugging using the `Python: Flask` debug configuration.
    * Option 2:
        * Open a terminal using the command [Python: Create Terminal](https://code.visualstudio.com/docs/python/environments#_activating-an-environment-in-the-terminal) (from your [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette))
        * Enter the following command in the above terminal
            `export FLASK_APP=app.py`
            `python -m flask run`
* Wait for Flask to start in the terminal window
* Once started you should see a message similar to the following in the terminal window:
```shell
 * Serving Flask app "app"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```

## Setup your local environment
### Step 1: Confirme flask is running
* Identify the IP Address of your remote environment.
* Open a browser window pointing to the Url that Flask is listening on (replacing the IP Address in the url)
* Confirm the output on the browser window is `Hello World!`

### Step 2: Open the workspace in your local environment
* This step will ensure you have your local environment setup to debug the remote flask application.
* You do not to setup the Python environment or Flask locally to debug a remote environment.

### Step 2: Update the IP Address in `launch.json` (`"host": "localhost"`)
* Identify the IP Address of your remote environment.
* Open `.vscode/launch.json` and replace the value of the setting `host` from `localhost` to the IP address identified earlier.

### Step 3: Update the remote folder in `launch.json` (`"remoteRoot": "${workspaceFolder}",`)
* Identify the full path to the directory containing the file `sample.py` in your remote environment.
* Open `.vscode/launch.json` and replace the value of the setting `remoteRoot` from `${workspaceFolder}` to the path identified earlier.

### Step 4: Attach the debugger
* Go into the debugger menu and select `Python: Attach` and press the green arrow icon 
* Open the `app.py` file and add a break point to the line `return "Hello World!"`
* Refresh your browser window.
* The breakpoint should now hit.
