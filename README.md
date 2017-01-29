# A Sample BATS PITCH Implementation

This repository contains a sample implementation of a parser for [BATS PITCH messages](documentation/BATS_PITCH_Specification.pdf) called *BATS PITCH Implementation*. For convencience, the parser is accessible via a web frontend.

The implementation also provides an [analysis](#summary-screen-with-analysis) about the actual lines read from the uploaded file and the eventual BATS PITCH messages detected therein.



[TOC]



## Environment Requirements and Setup

BATS PITCH Implementation is written in [Python 2.7.9](https://www.python.org/downloads/release/python-279/) and uses the web framework [django 1.8.2](https://docs.djangoproject.com/en/1.8/releases/1.8.2/). We highly recommend the use of a Python *virtualenv* in conjunction with *pip* as the primary package manager. Let us remark that this setting was also used during development.


With Python and pip pre-installed, execute
```
cd scripts 
./bootstrap_environment.sh
```
to bootstrap the environment.

This will subsequently install

1. the ``virtualenv`` package
2. the virtualenv ``bats_pitch_implementation``
3. all required site-packages listed in ``requirements.txt`` in the previously created ``bats_pitch_implementation`` virtualenv



## Starting BATS PITCH Implementation

The ``scripts`` directory also contains a Bash script for starting the django development server on a given port. The script is basically a wrapper around the `python manage.py runserver <port>` command. To start the server on port 8000 execute the commands
```
cd scripts 
./run_webserver.sh 8000
```



## Accessing BATS PITCH Implementation

Assuming BATS PITCH Implementation has been started on port 8000, as outlined in [Starting BATS PITCH Implementation](#starting-bats-web), the BATS PITCH Implementation server can be accessed at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).



## Stopping BATS PITCH Implementation

In order to stop the BATS PITCH Implementation server, simply press Control-C as you normally would to shut down any django development server.

The BATS PITCH Implementation server is not running in the background on purpose to keep things simple during development.



## Running the Tests

The ``scripts`` directory also contains a Bash script for running all tests in

- ``bats_pitch`` and
- ``bats_pitch_web``

The script is basically a wrapper around the `python manage.py test <package.to.test>` command.

To start the tests execute the commands
```
cd scripts 
./run_all_tests.sh
```
The script executes all tests in verbose mode and quits without any further action required.



## Available BATS PITCH Implementation Screens

Depending on the state, BATS PITCH Implementation offers up to five conceptionally different screens. The design is inspired by the BATS homepage and reuses CSS files contained therein. All images and CSS files used are the sole property of BATS.

All screens share the functionality that clicking on the BATS logo or on the text 'BATS PITCH Implementation' takes the user back to the [File Upload Screen](#file-upload-screen).


### File Upload Screen

The initial screen when accessing BATS PITCH Implementation is similar to the following screenshot

<center>
	![Startpage](documentation/startpage.jpg)
</center>

Here, a user can select a GZip file which is eventually uploaded for analysis when clicking on 'Upload and Analyze'.


### Invalid Form Screen

In case a user does not select a file for upload, an error message will be displayed that is similar to the following screen
<center>
	![Invalid Form Screen](documentation/invalid_form.jpg)
</center>


### Invalid GZip Screen

In case a user uploads a file which is not a valid GZip file, an error message will be displayed that is similar to the following screen
<center>
	![Invalid GZip Screen](documentation/invalid_gzip_file.jpg)
</center>


### Summary Screen with Analysis

In case a user uploads a valid GZip file, a screen gets returned which provides a summary of the BATS PITCH messages detected in the file. By default, this screen will also contain an analysis about the actual lines read from the file and the eventual messages detected. Here, the display is similar to the following screen
<center>
	![Summary Screen with Analysis](documentation/file_evaluation_with_analysis.jpg)
</center>


### Summary Screen without Analysis

The analysis section in the Summary screen can also be disabled by setting
```
IS_INCLUDING_ANALYSIS_IN_RETURNED_HTML = False
```
in `settings.py` in the *bats_pitch_implementation* directory. In this case, the display is similar to the following screen
<center>
	![Summary Screen without Analysis](documentation/file_evaluation_without_analysis.jpg)
</center>



## Technical Notes

### Tools Used

BATS PITCH Implementation has been developed on a MacBook running Mac OS X 10.6.8. For Python and django development, PyCharm 4.5.1 has been used.


### Package Overview

BATS PITCH Implementation is composed of a django project called `bats_pitch_implementation`, a django app called `bats_pitch_web`, and a Python package called `bats_pitch`.


#### The `bats_coding_exercise` django Project

The `bats_pitch_implementation` is a standard django project which contains only one custom URL entry that leads to the single `bats_pitch_web` view and also serves static content.


#### The `bats_pitch_web` django App

The `bats_pitch_web` django app is a standard django app which contains a custom form for handling the uploaded file that is rendered in the corresponding view. Let us remark that there are no models as they are not required at this stage of BATS PITCH Implementation.


#### The `bats_pitch` Python Package

The `bats_pitch` Python package consists of two Python subpackages named `data_types` and `message_types`.

##### The `data_types` Python Package

The `data_types` package implements all data types specified in the [BATS PITCH messages specification](documentation/BATS_PITCH_Specification.pdf); this also includes the `Price` message.

##### The `message_types` Python Package

The `message_types` package implements all message types specified in the [BATS PITCH messages specification](documentation/BATS_PITCH_Specification.pdf). Here, the data types that are provided by the `data_types` package are used.



## Testing

All packages and sub-packages described above have their individual tests. These involve unittests as well as django tests. A great emphasis was put on making the production code robust against accidental changes.

This especially applies to the `bats_pitch` package which defines the core of BATS PITCH Implementation. Here, additional *'sanity checks'* are included in the tests as well as in the implementation which eventually ensure that
 - all messages are composed of pairwise disjoint but aligned data types
 - All messages are composed of fields whose length matches the length of the underlying data type
 - All messages have distinct names
 - Every message type only occurs once in the list of known message types



## Future Enhancements

This section lists future enhancements in several areas.


### Deployment

Currently, the deployment process requires a working environment as described above. Future enhancements would see a bootstrapping of the environment, i.e. creating a virtualenv with pip on board and installing all necessary dependencies on the fly. Here, the key is automation which eventually allows for fast deployment.

BATS PITCH Implementation is currently running on the django development server. While this is acceptable during development, the actual deployment should be done on an real web server like nginx with Gunicorn running BATS PITCH Implementation. Moreover, static files should also be handled by an nginx server as it can do this task much more efficient. Ideally, a CDN would be used for this task.


### Testing

While the current code has unittests and django tests in place, the code is still lacking functional testing on the UI. Future enhancements would include Selenium tests to ensure UI functionality.

Moreover, additional sanity checks would certainly help the maintainability of the `bats_pitch` package. The earlier errors are detected, the cheaper it is to fix them usually!


### UI Improvements

The analysis section currently needs to be enabled/disabled via `settings.py`. Future enhancements would allow to set the corresponding flag directly in the form. In the meantime, a Javascript toggle for the 'Analysis' section would allow for a less space-consuming screen design.

BATS PITCH Implementation is currently written as a standard django app which operates in the request/response loop. Future enhancements would involve migrating the app to AngularJS and making it a SPA.

While the current CSS is directly written and maintained in the static files directory, future enhancements would see the use of LESS for reusable CSS code generation.


### Security

The current implementation of BATS PITCH Implementation might be vulnerable to security attacks via malicious file uploads. There is currently no file size limit enforced on upload, for example. Future enhancements would focus on securing BATS PITCH Implementation against security vulnerabilities.
