# Django Debugging Sample

**Note:**
This sample uses Python 3.6 and Django 2.0   
This is a sample Django application created using [tutorial](https://docs.djangoproject.com/en/2.0/intro/tutorial01/) on the Django website

## Setup your remote environment
### Step 1: Build docker image and run it
* Open a temrinal window
* Type the following command in the terminal window
`docker build -t remote-debugging-docker-django .`
* Type the following command in the terminal window
`docker run -it -p 3000:3000 -p 8000:8000 remote-debugging-docker-django`
* Wait for Django to start in the container
* Once started you should see something similar to the following in the terminal window:
```shell
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Step 2: Confirm Django is running
* Open a browser window pointing to the Url that Django is listening on
* Confirm Django home page appears
* Next navigate to the `polls` page ([http://127.0.0.1:8000/polls](http://127.0.0.1:8000/polls))
* Confirm the output on the browser window is `Hello, world. You're at the polls index.`

## Setup your local environment
### Step 1: Open the workspace in your local environment
* This step will ensure you have setup the program to be debugged locally.
* You do not to setup the Python environment locally to debug a remote environment.

### Step 2: Attach the debugger
* Go into the debugger menu and select `Python: Attach` and press the green arrow icon 

### Step 3: Debug Django
* Open the `polls/views.py` file and add a break point to the line `return HttpResponse("Hello, world. You're at the polls index.")`  
* Refresh your browser window.
* The debugger should hit the breakpoint.
