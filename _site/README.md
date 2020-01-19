# Course Template

This repository is a template for managing coursework using GitHub pages.  It
uses the theme [dinky](https://github.com/pages-themes/dinky),
[nbviewer.js](https://github.com/kokes/nbviewer.js), and
[reveal.js](https://revealjs.com/) for presenting material.

For each week of class, create a subdirectory `weekZZ` (where `ZZ` is the week
of the class) and place any `.ipynb` and `.md` files in that directory.
Lectures can utilize the layout `lecture`, which will present them in revealjs.

## Instructions to get started:

For basic class info, modify: _data/class.yml, _includes/class_info.html and _config.yml

For your github repo -  make sure to turn on github pages and make sure it shows the correct github.io location.  
Do this under __Settings__ for this repo. For example, this one is USERNAME.github.io/CLASSNUMBER:
![](assets/ghpages.png)


## For each lesson:

For each day or week (a single lesson) of class, create a subdirectory `lessonZZ` (where `ZZ` is the day
of the class) and place any `.ipynb` and `.md` files in that directory.
Lectures can utilize the layout `lecture`, which will present them in revealjs.

## To build:

General instructions about how to build websites locally using jekyll can be found [right here](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/).

Key build command (to be run in repo directory): __bundle exec jekyll serve__