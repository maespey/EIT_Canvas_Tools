# Enterprise Instructional Technology Canvas Tools
### Welcome
#### There are a few prerequisites before you can get started:
* Python 3.x.x (I am using 3.7.0)
  * https://www.python.org/downloads/
* UCF's Python Wraper for the Canvas API
  * https://github.com/ucfopen/canvasapi [Read the Docs](http://canvasapi.readthedocs.io/)
  * Clone -> `https://github.com/ucfopen/canvasapi.git` if you would like to contribute to their project
  * Run -> `pip install canvasapi` if you just want to use their project
* config.py for your Canvas installation
```python
#############    Test Environment    #############

Reset every 3 weeks

# API_URL = "https://Campus.test.instructure.com/"
# API_KEY = "Generated from a user profile in Canvas Test under Approved Integrations"
# domain = "Campus.test.instructure.edu"

#############    Beta Environment    #############

Reset every week

API_URL = "https://Campus.beta.instructure.com/"
API_KEY = "Generated from a user profile in Canvas Beta under Approved Integrations"
domain = "Campus.beta.instructure.edu"

#############    Prod Environment    #############

# API_URL = "https://Campus.instructure.com/"
# API_KEY = "Generated from a user profile in Canvas Prod under Approved Integrations"
# domain = "Campus.instructure.edu"
```