---
layout: syllabus
title: Syllabus
---

# Course Description

Data visualization is crucial to conveying information drawn from models,
observations or investigations. This course will provide an overview of
historical and modern techniques for visualizing data, drawing on
quantitative, statistical, and network-focused datasets. Topics will include
construction of communicative visualizations, the modern software ecosystem
of visualization, and techniques for aggregation and interpretation of data
through visualization. Particular attention will be paid to the Python
ecosystem and multi-dimensional quantitative datasets. 

# Land Acknowledgment

As a land-grant institution, the University of Illinois at Urbana-Champaign has
a responsibility to acknowledge the historical context in which it exists. In
order to remind ourselves and our community, we will begin this event with the
following statement. We are currently on the lands of the Peoria, Kaskaskia,
Peankashaw, Wea, Miami, Mascoutin, Odawa, Sauk, Mesquaki, Kickapoo, Potawatomi,
Ojibwe, and Chickasaw Nations. It is necessary for us to acknowledge these
Native Nations and for us to work with them as we move forward as an
institution. Over the next 150 years, we will be a vibrant community inclusive
of all our differences, with Native peoples at the core of our efforts.

[More information can be found on the Chancellor's
Website.](https://chancellor.illinois.edu/land_acknowledgement.html)

## Course Overview

This course is designed to give practical advice to students on
communicating data through visualization.  This will involve a considerable
amount of programming, and typically this programming will be done in Python.
For the most part, our data will be quantitative and multi-dimensional.  The
course will aim to provide both an understanding of what data visualizations
communicate and a set of tools for constructing them yourself.

The course will follow a common pattern within each three-hour instructional
session.  The first 60-90 minutes will be focused on lecture, where concepts
and tools will be introduced; typically, each class will focus on one type of
visualization or class of visualization.  The remaining time will include
exploration of a dataset, which may be independent or in groups, and then a
wrap-up session at the end.

Students are expected to have laptops with them, as well as access to Python
installations, and will be encouraged to participate in class.  Homework will
be assigned and collected utilizing the Jupyter nbgrader extension or through
other methods specified at time of submission like Moodle.

The central themes of the course are:

1. What are the components of an effective visualization of quantitative data?
2. What tools and ecosystems are available for visualizing data?
3. What systems can be put in place to generate visualizations rapidly and with
   high-fidelity representation?

## Pre- and Co-requisites

None, although basic Python programming experience is assumed.  A brief
introduction to Python will be presented during the course.

# Course Materials

There is no required textbook for this course.  All course materials will be posted to
the GitHub repository at https://github.com/UIUC-iSchool-DataViz/spring2020 .

A list of Python libraries week-by-week and tips on how to install them <a href="https://github.com/UIUC-iSchool-DataViz/spring2020/blob/master/week01/test_imports_week01.ipynb">can be found by clicking this link</a>.

**Optional** textbook [Visualization Analysis and Design by Tamara Munzner](https://www.amazon.com/gp/product/1466508914/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

As the course progresses, a list of recommended readings will be generated for
each class.  These will be included in the course materials repository, and
students are encouraged to fork that repository and issue pull requests to add
suggested readings.

# Topic Calendar & Optional Reading

Below is an approximate outline of the course and **optional** reading for each week.
This course is always under development and  the
course outline below is subject to some flexibility; students will be encouraged
to provide feedback on the topics covered, particularly toward the end.  Topics
that are of particular interest will be emphasized.

**Optional texts:**
 * <a href="https://www.amazon.com/Visualization-Analysis-Design-AK-Peters/dp/1466508914/ref=sr_1_2?crid=1WC409BVX1489&keywords=visualization+analysis+and+design&qid=1580082878&sprefix=visualization%2Caps%2C158&sr=8-2">Visualization Analysis & Design, Tamara Munzner</a>
 * Edward Tufte wrote a series of visualization books that are often thought of as foundational to the field.  These include <a href="https://www.amazon.com/Visual-Display-Quantitative-Information/dp/0961392142/ref=sr_1_1?keywords=edward+tufte+books&qid=1580082986&sr=8-1">The Visual Display of Quantitative Information</a>, <a href="https://www.amazon.com/Beautiful-Evidence-Edward-R-Tufte/dp/0961392177/ref=sr_1_2?keywords=edward+tufte+books&qid=1580082986&sr=8-2">Beautiful Evidence</a>, <a href="https://www.amazon.com/Envisioning-Information-Edward-R-Tufte/dp/0961392118/ref=sr_1_3?keywords=edward+tufte+books&qid=1580082986&sr=8-3">Envisioning Information</a>, and <a href="https://www.amazon.com/Visual-Explanations-Quantities-Evidence-Narrative/dp/0961392126/ref=sr_1_4?keywords=edward+tufte+books&qid=1580082986&sr=8-4">Visual Explanations: Images and Quantities, Evidence and Narrative<a>
 * There is a free online book, <a href="https://serialmentor.com/dataviz/">Fundamentals of Data Visualization by Claus O. Wilke</a> that provies a lot of nice examples and serves as an intro to Tamara Munzner's book.  It has an <a href="https://serialmentor.com/dataviz/bibliography.html">annotated bibliography at the end</a> that gives a few references for books in data viz that include programming. It is built from the linked <a href="https://github.com/clauswilke/dataviz">GitHub repo</a>.  Note that this book is focused on static (not interactive) visualizations.
 * Additional references will be added as needed.

Acronyms for books:
 * VAD: Visualization Analysis & Design
 * FDA: Fundamentals of Data Visualization

**Course Outline and *Optional* Reading List**

| Week 1 | Introduction, syllabus, examples, and some basics | 1. VAD, Ch. 1: What's Viz, and Why Do It? <br> 2. <a href="https://serialmentor.com/dataviz/introduction.html">FDA, Ch. 1: Introduction</a> & <a href="https://serialmentor.com/dataviz/proportional-ink.html">FDA, Ch. 17: The principle of proportional ink</a> <br> 3. <a href="https://medium.com/multiple-views-visualization-research-explained/same-data-multiple-perspectives-curse-of-knowledge-in-visual-data-communication-d827c381f936">Same Data, Multiple Perspectives</a>
| Week 2 | Data storage & Operations | 1. VAD, Ch. 2: What: Data Abstraction <br> 2. <a href="https://serialmentor.com/dataviz/aesthetic-mapping.html">FDA, Ch. 2: Visualizing data: Mapping data onto aesthetics</a> <br> 3. <a href="https://github.com/jnaiman/IS-452AO-Fall2019/blob/master/Lectures/Week-10-JSONandCSV.ipynb">IS452's intro to CSV files (bottom of page)</a> <br> 4. <a href="https://github.com/jnaiman/IS-452AO-Fall2019/blob/master/Lectures/Week-09-Dictionaries.ipynb">IS452's Intro to Dictionaries</a> <br> 5. <a href="https://pandas.pydata.org/pandas-docs/stable/">Pandas Docs</a> & <a href="https://docs.scipy.org/doc/numpy/reference/">NumPy Docs</a> 
| Week 3 | Types of Viz and color, colormaps | 1. VAD, Ch. 10: Map Color and Other Channels <br> 2. <a href="https://serialmentor.com/dataviz/color-basics.html">FDA, Ch. 4: Color scales</a> <br> 3. <a href="https://www.csc2.ncsu.edu/faculty/healey/PP/">Perception in Visualization (pay attention to the parts about color)</a>  <br> 4. <a href="https://jiffyclub.github.io/palettable/#documentation">Palettable Docs</a>
| Week 4 | Beginning Interactivity | 1. <a href="https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Basics.html">Intro to ipywidgets</a> <br> 2. <a href="https://github.com/jupyter-widgets/ipywidgets/blob/master/docs/source/examples/Index.ipynb">Example Widgets Notebooks</a> <br> 3. VAD Ch. 7: Arrange Tables <br> 4. <a href="https://serialmentor.com/dataviz/histograms-density-plots.html">FDA, Visualizing distributions: Histograms and density plots</a> <br>  
| Week 5 | Distributions, Engines |  1. <a href="https://www.youtube.com/watch?v=rraXF0EjRC8">Video about bqplot</a> <br> 2. <a href="https://towardsdatascience.com/a-comprehensive-guide-to-the-grammar-of-graphics-for-effective-visualization-of-multi-dimensional-1f92b4ed4149">An introduction to Grammar of Graphics</a> <br> 3. <a href="https://ipywidgets.readthedocs.io/en/latest/">ipywidgets Docs</a>; <a href="https://traitlets.readthedocs.io/en/stable/">Traitlets Docs</a>; <a href="https://bqplot.readthedocs.io/en/latest/">bqplot Docs</a>
| Week 6 | Dashboards & Maps with bqplot | 1. VAD Ch. 8: Arrange Spatial Data <br> 2. VAD Ch. 11: Manipulate View <br> 3. <a href="https://serialmentor.com/dataviz/geospatial-data.html">FDA, Ch. 15: Visualizing geospatial data</a>
| Week 7 | More with maps - bqplot, cartopy, ipyleaflet, geopandas | 1. VAD Ch. 8: Arrange Spatial Data <br> 2. <a href="https://serialmentor.com/dataviz/geospatial-data.html">FDA, Ch. 15: Visualizing geospatial data</a> <br> 3. <a href="https://scitools.org.uk/cartopy/docs/latest/">Cartopy docs</a>; <a href="https://ipyleaflet.readthedocs.io/en/latest/">ipyleaflet docs</a>; <a href="https://geopandas.org/">Geopandas Docs</a>
| Week 8 | Break | None
| Week 9 | Network Viz & Word cloud Viz | 1. VAD Ch. 9: Arrange Networks and Trees
| Week 10 | Designing for the web with Python & Javascript (JS) | 1. <a href="https://alpha.iodide.io/">Iodide Docs</a> - in particular: <a href="https://iodide-project.github.io/docs/key_concepts/">key concepts</a> & <a href="https://iodide-project.github.io/docs/iomd/">IOMD format</a> <br> 2. <a href="https://www.codecademy.com/learn/introduction-to-javascript">Intro to Javascript</a> <br> 3. <a href="https://serialmentor.com/dataviz/directory-of-visualizations.html">FDA, Ch. 5: Directory of visualizations</a>
| Week 11 | Designing for the web with Python & Javascript, Web dev | 1. <a href="https://medium.com/multiple-views-visualization-research-explained/same-data-multiple-perspectives-curse-of-knowledge-in-visual-data-communication-d827c381f936">Same Data, Multiple Perspectives</a> <br> 2. <a href="https://alpha.iodide.io/">Iodide Docs</a> <br> 3. <a href="https://vega.github.io/vega-lite/docs/">vega-lite docs</a> - in particular: <a href="https://vega.github.io/vega-lite/docs/transform.html">Vega-lite transformations</a> & <a href="https://vega.github.io/vega-lite/docs/selection.html">Vega-lite selections</a> <br> 4. <a href="https://idyll-lang.org/docs"> Idyll Docs</a>
| Week 12 | More javascript & web dev <br> <br> Guest lecture about scientific & cinematic viz from <a href="http://avl.ncsa.illinois.edu/">AVL</a> | 1. <a href="https://idyll-lang.org/docs"> Idyll Docs</a> - in particular: <a href="https://idyll-lang.org/docs/components">Built in</a>/<a href="https://idyll-lang.org/docs/components/npm">npm installed</a> components
| Week 13 | Scientific visualization | 1. <a href="https://yt-project.org/">yt docs</a>
| Week 14 | Volume rendering for scientific viz, more with Idyll, Publishing Viz | 1. <a href="https://yt-project.org/">yt docs</a> <br> 2. <a href="https://yt-project.org/doc/visualizing/volume_rendering.html">yt Volume Rendering Tutorial</a> <br> 3. <a href="https://idyll-lang.org/docs"> Idyll Docs</a>
| Week 15 | Idyll + d3.js, course wrap up! | 1. <a href="https://github.com/d3/d3/wiki">d3.js docs</a>


# About Your Instructor

Jill Naiman's background is in theoretical and computational astrophysics with a current research emphasis on scientific data visualization and the digitization of historical scientific images and text.  She is currently a Visiting Scholar at the Advanced Visualization Lab at the National Center for Supercomputing Applications.  She is currently involved in projects related to increasing access to industry-standard special effects software for scientists - more info can be found <a href="http://ytini.com">here</a> and <a href="http://astroblend.com">here</a>.  Information about her astrophysical research and outreach efforts can be found <a href="http://astronaiman.com">here</a>.

# Library Resources

| http://www.library.illinois.edu/lis/ |
| lislib@library.illinois.edu          |
| Phone: (217) 300-8439                |

# Writing and Bibliographic Style Resources
The campus-wide Writers Workshop provides free consultations. For more
information see <http://www.cws.illinois.edu/workshop/> The iSchool
has a Writing Resources Moodle site
<https://courses.ischool.illinois.edu/course/view.php?id=1705> and
iSchool writing coaches also offer free consultations.


# Academic Integrity

Please review and reflect on the academic integrity policy of the University of Illinois,
<http://admin.illinois.edu/policy/code/article1_part4_1-401.html> to which we subscribe.
By turning in materials for review, you certify that all work presented is your own and
has been done by you independently, or as a member of a designated group for group assignments.
If, in the course of your writing, you use the words or ideas of another writer, proper
acknowledgment must be given (using APA, Chicago, or MLA style). Not to do so is to commit
plagiarism, a form of academic dishonesty. If you are not absolutely clear on what constitutes
plagiarism and how to cite sources appropriately, now is the time to learn. Please ask me!
Please be aware that the consequences for plagiarism or other forms of academic dishonesty
will be severe. Students who violate university standards of academic integrity are
subject to disciplinary action, including a reduced grade, failure in the course, and
suspension or dismissal from the University.

# Statement of Inclusion

[Inclusive Illinois Committee Diversity Statement](http://www.inclusiveillinois.illinois.edu/supporting_docs/Inclusive%20Illinois%20Diversity%20Statement.pdf)

As the state's premier public university, the University of Illinois
at Urbana-Champaign's core mission is to serve the interests of the
diverse people of the state of Illinois and beyond. The institution
thus values inclusion and a pluralistic learning and research
environment, one which we respect the varied perspectives and lived
experiences of a diverse community and global workforce. We support
diversity of worldviews, histories, and cultural knowledge across a
range of social groups including race, ethnicity, gender identity,
sexual orientation, abilities, economic class, religion, and their
intersections.

# Accessibility Statement
To obtain accessibility-related academic adjustments and/or auxiliary
aids, students with disabilities must contact the course instructor
and the [Disability Resources and Educational Services](http://disability.illinois.edu/) (DRES) as soon
as possible.  To contact DRES you may visit 1207 S. Oak St.,
Champaign, call (217) 333-4603 (V/TTY), or e-mail a message to
disability@illinois.edu.

# Assignments and Evaluation

Students will be graded based on a combination of assignments (70%: 40% standard prose/code assignments and
30% weekly visualization reports) and a final
project (30%).  The final project will be a capstone to the course, and will
have greater flexibility in software packages and data sources.  This project
will be introduced in Week 8.

**In summary, your grades consist of:**

| 40% | Standard assignments in prose or code form
| 30% | Weekly visualization reports
| 30% | Final project


Assignments in this course will be a mixture of coding/visualization work and
written work.  These two may not be distinct assignments; students will be
asked to describe their code and justify choices for making decisions with
respect to visualizations.

Students are expected, unless otherwise instructed, to be the principal authors
of their code.  This does not mean they may not investigate resources such as
StackOverflow, package documentation, etc; however, they *must* cite when
resources (especially StackOverflow and other "recipe" sites) are utilized.

Assignments will take two forms, and will be given at the end of each class.
Students will have until the following class to turn these in; assignments will
be collected electronically.

 * The first type of assignment will be a written document, constituting 
   either a brief literature review or an analysis of a visualization or
   set of visualizations.  The parameters for these assignments will be given
   during class, but will typically involve a critique of a visualization,
   including citing relevant works in the visualization literature.
 * The second type of assignment will be a hands-on, code-based assignment.
   Students will be provided either a dataset *or* a class of datasets from
   which they can choose, and construct one or multiple mechanisms of drawing
   information out of this visually.  These will be submitted in the form of
   Jupyter notebooks.  Each visualization must be accompanied by narrative
   description from the student describing why design decisions were made.

The submission process for homeworks will be described by example during class
before any homeworks are to be submitted.

Each assignment will be 50% "correctness" and 50% the narrative description of
the process.  "Correctness" in this case indicates that the code runs without
issue, results are produced, and each component of the assignment is completed.
The narrative description of the process will be graded on grammar (less so) and
completeness (more so).

### Grading Policy

All assignments are required for all students. Completing all assignments is
not a guarantee of a passing grade.  All work must be completed in order to
pass this class. Late or incomplete assignments will not be given full credit
unless the student has contacted the instructor prior to the due date of the
assignment (or in the case of emergencies, as soon as practicable).


**Grading Scale:**

| 94-100       | A
| 90-93        | A-
| 87-89        | B+
| 83-86        | B
| 80-82        | B-
| 77-79        | C+
| 73-76        | C
| 70-72        | C-
| 67-69        | D+
| 63-66        | D
| 60-62        | D-
| 59 and below | F

### Incompletes

Students must request an incomplete grade from the instructor. The instructor
and student will agree on a due date for completion of coursework and the
student must file an Incomplete Form signed by the student, the instructor, and
the student’s academic advisor with the School’s records representative. More
information on incompletes is available here:
<http://webdocs.ischool.illinois.edu/registration/incomplete_grade_form.pdf>

### Attendance Policy

Students are required to attend each class, and if they are unable to do so
must notify the instructor and TA in advance and request an excused absence.
Participation in class -- in the form of comments, questions, and discussion --
is expected.


## Emergency Response: Run, Hide, Fight

Emergencies can happen anywhere and at any time. It is important that
we take a minute to prepare for a situation in which our safety or
even our lives could depend on our ability to react quickly. When
we’re faced with any kind of emergency – like fire, severe weather or
if someone is trying to hurt you – we have three options: Run, hide or
fight.


### Run

Leaving the area quickly is the best option if it is safe to do so.

- Take time now to learn the different ways to leave your building.
- Leave personal items behind.
- Assist those who need help, but consider whether doing so puts
  yourself at risk.
- Alert authorities of the emergency when it is safe to do so.

### Hide

When you can’t or don’t want to run, take shelter indoors.

- Take time now to learn different ways to seek shelter in your building.
- If severe weather is imminent, go to the nearest indoor storm refuge area.
- If someone is trying to hurt you and you can’t evacuate, get to a place
  where you can’t be seen, lock or barricade your area, silence your
  phone, don’t make any noise and don’t come out until you receive an
  Illini-Alert indicating it is safe to do so.

### Fight

As a last resort, you may need to fight to increase your chances of
survival.

- Think about what kind of common items are in your area which you
  can use to defend yourself.
- Team up with others to fight if the situation allows.
- Mentally prepare yourself – you may be in a fight for your life.

Please be aware of persons with disabilities who may need additional
assistance in emergency situations.


### Other resources

- [police.illinois.edu/safe](http://police.illinois.edu/safe) for more
  information on how to prepare for emergencies, including how to run,
  hide or fight and building floor plans that can show you safe areas.
- [emergency.illinois.edu](http://emergency.illinois.edu) to sign up for
  Illini-Alert text messages.
- Follow the University of Illinois Police Department on Twitter and
  Facebook to get regular updates about campus safety.
