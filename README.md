# scriptCreator

usage: scriptCreator.py [-h] [-v] [-n NAME] [-p PARAMETERS]

Default description

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -n NAME, --name NAME  Name of the new project. Output file will be named as
                        name.py [string], default value = newProject
  -p PARAMETERS, --parameters PARAMETERS
                        List with parameters of output sctipt, format:
                        'name:letter:type:default#name:letter:type:default'.
                        If there is not default value for some parameter, type
                        'None' instead of 'default'. [string], no default
                        value'
