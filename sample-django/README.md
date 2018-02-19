# Django Debugging Sample

**Note:**
This sample uses Python 3.6 and Django 2.0   
This is a sample Django application created using [tutorial](https://docs.djangoproject.com/en/2.0/intro/tutorial01/) on the Django website

### Step 1: Configure VS Code to use a Python environment 
* Open a terminal window
* Type the following command in the terminal window
`virtualenv --python=python3.6 .env`
* Reload VS Code using the command `Reload Window` (from your [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette))
* Open the file `sample.py`
* Select the command `Python: Select Interpteter` and select the Python environment created above (found in `./.env` directory created above)

### Step 2: Install Django
* Open a terminal using the command [Python: Create Terminal](https://code.visualstudio.com/docs/python/environments#_activating-an-environment-in-the-terminal) (from your [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette))
* Enter the following command in the above terminal
    `python -m pip install -r requirements.txt`

### Step 3: Launch Django in debug mode
* Go into the debugger menu and start debugging using the `Python: Django` debug configuration.
* Wait for Django to start in the terminal window
* Once started you should see something similar to the following in the terminal window:
```shell
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Step 4: Confirm Django is running
* Open a browser window pointing to the Url that Django is listening on
* Confirm Django home page appears
* Next navigate to the `polls` page ([http://127.0.0.1:8000/polls](http://127.0.0.1:8000/polls))
* Confirm the output on the browser window is `Hello, world. You're at the polls index.`

### Step 5: Debug Django
* Open the `polls/views.py` file and add a break point to the line `return HttpResponse("Hello, world. You're at the polls index.")`  
* Refresh your browser window.
* The debugger should hit the breakpoint.
