# Enterprise Instructional Technology Canvas Tools

# Getting Started
### Welcome
#### There are a few prerequisites before you can get started:
* Python 3.x.x (I am using 3.7.0)
  * https://www.python.org/downloads/
* UCF's Python Wraper for the Canvas API
  * https://github.com/ucfopen/canvasapi
  * [Read the Docs](http://canvasapi.readthedocs.io/)
  * Clone -> `https://github.com/ucfopen/canvasapi.git` if you would like to contribute to their project
  * Run -> `pip install canvasapi` if you just want to use their project
* config.py for your Canvas installation
  * Using this file will let you store your API key's and switch them out on the fly to match your target environment `Beta/Test/Prod` by commenting out the two you are not intending to run on.
```python
##################################################
#############        config.py       #############
##################################################

#############    Test Environment    #############

# Reset every 3 weeks

# API_URL = "https://Campus.test.instructure.com/"
# API_KEY = "Generated from a user profile in Canvas Test under Approved Integrations"
# domain = "Campus.test.instructure.edu"

#############    Beta Environment    #############

# Reset every week

API_URL = "https://Campus.beta.instructure.com/"
API_KEY = "Generated from a user profile in Canvas Beta under Approved Integrations"
domain = "Campus.beta.instructure.edu"

#############    Prod Environment    #############

# API_URL = "https://Campus.instructure.com/"
# API_KEY = "Generated from a user profile in Canvas Prod under Approved Integrations"
# domain = "Campus.instructure.edu"
```

#### For the common tools I have tried to be sure to prompt for user input instead of using hard coded variables, but be sure that you fully understand the implications of running whatever command you are running.

#### The [Github Desktop](https://desktop.github.com/) client is easy to use and works well. It allows you to keep an up to date copy of the repository, but requires that you have a Github account.


# Updating
#### There are a few things that will need to be updated from time to time:
* Github should update without prompt
* Python:
* PIP: 
* CanvasAPI: 