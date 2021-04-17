<!-- # Playlister
https://github.com/squeaky1273/Playlister/blob/master/proposal.md
<br> -->
# Welcome to <img src=https://raw.githubusercontent.com/squeaky1273/Playlister/master/playlist/static/playlist/logo.png width="75"> myTunes
<h3>We are a playlister that allows music lovers from all around to share their favorite playlists of any genre. https://playlister-p-r.herokuapp.com/ </h3>
<br>

* [ Getting Started. ](#start)
    * [ Prerequisites. ](#pre)
        * [ Environment. ](#env)
    * [ Installing. ](#install)
        * [ Cloning Repo. ](#clone)
* [ Running the tests. ](#test)
* [ Built With. ](#built)
* [ Docker ](#docker)
* [ Author(s). ](#author(s))
* [ Acknowledgment. ](#credit)

<a name="start"></a>
## Getting Started

These instructions will help you get the project up and running on your machine.

<a name="pre"></a>
<h3>Prerequisites</h3>

* Must have Git
* Must have a GitHub account
* Must have Python 3.7.4 installed

<a name="env"></a>
<h4>Environment</h4>

    * brew install python3
    * python3 -m pip install Django
    * python3 -m django --version

<a name="install"></a>
<h3>Installing</h3>

<a name="clone"></a>
<h4>Cloning Repo</h4>

    * git clone https://github.com/squeaky1273/Playlister.git
    * cd playlist
    * rm -rf .git
    * git init
    * git remote add origin https://github.com/YOUR_GITHUB_USERNAME/Playlister

<a name="test"></a>
## Running the tests

Run the tests for this project from the command line using:

    * python3 manage.py test

<a name="built"></a>
## Built With

* Django 2.2.8 - web framework
* Python 3.7.4 - language used to write code
* Bootstrap 4 - website styling
* CSS -  website styling
* HTML - website styling
* Heroku - website host
* Docker - deploy onto personal domain

<a name="docker"></a>
## Docker

### Build
```
docker build -t tunes .
```
### Run
```
docker run -p 8080:8080 --rm --name mytunes tunes
```
### Health Check
Sending ```GET``` request to ```/health``` should return ```{"Status": "200 OK"}```


<a name="author(s)"></a>
## Author(s)

Padyn Riddell - <i>Initial work</i> - Make School Student and BEW concentration

<a name="credit"></a>
## Acknowledgment

* God - Thank you for giving the ability to have opportunties to build code and go to school.
* Mom & family - Thank you for beliving in me and being encouraging.
* Meredith - Thank you for helping me with any issues that I had with implementing code.
