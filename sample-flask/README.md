# Flask Debugging Sample

### Step 1: Configure VS Code to use a Python environment 
* Open a terminal window
* Type the following command in the terminal window
`virtualenv --python=python3.6 .env`
* Reload VS Code using the command `Reload Window` (from your [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette))
* Open the file `sample.py`
* Select the command `Python: Select Interpteter` and select the Python environment created above (found in `./.env` directory created above)

### Step 2: Install Flask  
* Open a terminal using the command [Python: Create Terminal](https://code.visualstudio.com/docs/python/environments#_activating-an-environment-in-the-terminal) (from your [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette))
* Enter the following command in the above terminal
    `python -m pip install flask`

### Step 3: Launch Flask in debug mode
* Go into the debugger menu and start debugging using the `Python: Flask` debug configuration.
* Wait for Flask to start in the terminal window
* Once started you should see something similar to the following in the terminal window:
```shell
 * Serving Flask app "app"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```

### Step 4: Confirm flask is running
* Open a browser window pointing to the Url that Flask is listening on
* Confirm the output on the browser window is `Hello World!`

### Step 5: Debug Flask
* Open the `app.py` file and add a break point to the line `return "Hello World!"`
* Refresh your browser window.
* The debugger should hit the breakpoint.

### Troubleshooting
* Confirm flask is running in the terminal window.
* Confirm you can see `Hello World!` in the browser widnow.
* Try running flask manually and testing it as follows (in your terminal window):
```shell
$ export FLASK_APP=app.py
$ python -m flask run
 * Serving Flask app "app"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
