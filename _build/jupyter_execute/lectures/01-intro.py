#!/usr/bin/env python
# coding: utf-8

# # Introduction to CSS

# ## Goals of this lecture
# 
# - Quick introductions/logistics.
# - Introduction to CSS: What is it and why does it matter?
# - Overview of course content.

# ## Course Logistics: CSS 1
# 
# **Teaching Team**:
# - Instructor: [Sean Trott](https://seantrott.github.io/): Assistant Teaching Professor in [Cognitive Science](https://cogsci.ucsd.edu/) and [CSS](https://css.ucsd.edu/).  
# - TAs: ... (**todo**)
# 
# **When/Where?**:
# - Lecture: MWF 9-10 AM, Center 212 (also podcasted).  
# - Coding Lab Sections (ERCA 117): 
#    - Tuesday, 12-1:50, 2-3:50
#    - Wednesday: 1-2:50
#    - Friday: 12:-1:50
#    
# [**Course Website**](https://seantrott.github.io/css1_ucsd/intro.html).
# 

# ## What is CSS?
# 
# In a nutshell, [Computational Social Science](https://en.wikipedia.org/wiki/Computational_social_science) focuses on **computational approaches** to **social science**.
# 
# At UCSD, [Social Sciences](https://socialsciences.ucsd.edu/) encompasses many disciplines:
# 
# - Economics.
# - Political Science.
# - Cognitive Science. 
# - Urban Studies and Planning.
# 
# And [many more](https://socialsciences.ucsd.edu/about/org-chart.html)!

# ### What is social science?
# 
# **Social Science** refers to a domain of study: social phenomena.  
# 
# - Encompasses many **scales**: human psychology, language, economic behavior, political systems.  
# - Can involve many **approaches**: qualitative interviews, statistical analysis, simulations.  

# ### What is computation?
# 
# [**Computation**](https://en.wikipedia.org/wiki/Computation) is *calculation* using well-defined steps, e.g., an *algorithm*.
# 
# - A *computer* is anything that implements these well-defined steps.  
# - Historically, the term "computer" used to refer to *people*!
# 
# A **programming language** is a way to get a computer to do these things for you.  
# 
# - Can *automate* processes: speed things up!  
# - Can perform computations at *scale*.  
# - Can *share* with others.  

# ## CSS Inspirations
# 
# - CSS often involves analysis of **large-scale datasets** using computational and statistical tools.  
# - A key part of this approach is **programming**, e.g., in Python.  
# - Can yield important theoretical and practical **insights**.  

# ### Economic mobility
# 
# Recent work by [Raj Chetty](https://rajchetty.com/) used a combination of **social network data** and **Census data** to demonstrate a link between:
# 
# - The **Economic Connectedness** of a neighborhood.  
# - How much **Upward Mobility** exists in a neighborhood.
# 
# *Jackson et al. (2022)*:
# 
# ![title](../img/lectures/intro/chetty_2022.png)

# ### Policing and Racial Justice
# 
# Work by [Dan Jurafsky and colleagues](https://www.pnas.org/doi/full/10.1073/pnas.1702413114#fig01) using **body-cam footage** has demonstrated racial disparities in how respectfully police officers speak to community members during routine traffic stops.
# 
# *Jurafsky et al. (2017)*:
# 
# ![title](../img/lectures/intro/jurafsky_2017.png)

# ## Course Overview
# 
# The goal of this course is to teach you:
# 
# - **Computational thinking**: how to approach problems and devise solutions from a computational perspective.  
# - **Python programming**: how to implement those solutions in the Python programming language. 

# ### What is Python?
# 
# - Python is a **programming language**. 
#   - It's a way to "do" computation.  
# - Python is also an **ecosystem**.
#   - A particular computational approach with its own community and practices.  
# 

# ### Why Python?
# 
# - Strong **community**: many [open source](https://en.wikipedia.org/wiki/Open_source) packages for **scientific computing**. 
# - **Human focused**: [Zen of Python](https://peps.python.org/pep-0020/).  
# - Python is **widely used**. 
# 
# ![title](../img/lectures/intro/python.png)

# ### What does Python look like?

# In[1]:


variable_string = "This is a string"
print(variable_string)


# In[2]:


variable_integer1 = 50
variable_integer1


# In[3]:


variable_integer2 = 10
variable_integer2 + variable_integer1


# ## What will this course look like?
# 
# This section covers:
# 
# - Overview of course structure.  
# - Overview of topics.  
# - Overview of grading and assessment criteria. 
# 
# See the [syllabus page](https://seantrott.github.io/css1_ucsd/course/syllabus.html) for more details!

# ### Course Structure
# 
# Class time is divided into *lecture* and *section*.
# 
# - Lecture is a time to **introduce**, **explain**, and **demonstrate** new concepts.  
# - Section is a time to **practice** and **develop fluency** with these concepts.  
# 

# ### Overview of topics
# 
# Note that this course will involve many new *concepts* and *software tools*. Students come from all sorts of backgrounds with different levels of experience, but our goal is to help you learn Python from the "ground up".
# 
# - Common tools/software for Python programming, e.g., [Jupyter notebooks](https://jupyter.org/).  
# - Python basics, e.g., [variables](https://www.w3schools.com/python/python_variables.asp), [conditional statements ("if/else")](https://realpython.com/python-conditional-statements/), and [functions](https://www.w3schools.com/python/python_functions.asp).  
# - Working with **sequences**, such as [lists](https://www.w3schools.com/python/python_lists.asp).  
# - Packages for scientific computing, such as [`pandas`](https://pandas.pydata.org/), [`numpy`](https://numpy.org/), and [`seaborn`](https://seaborn.pydata.org/).  

# ### Grading and Assessments
# 
# - Each week (except Week 0) will have a **coding lab** due Friday; these are graded for *completion*.  
# - There are also **four problem sets**, which will be auto-graded for *correctness*.  
# - There is also a **final project**––like a big, more coherent problem set.
# 
# | Grade Component | Percentage of Final Grade |
# | --------------- | ------------------------- |
# | 10 Coding Labs | 50% (5% each) |
# | 4 Problem Sets | 32% (8% each) |
# | 1 Final Project| 18% |

# ### Extra credit
# 
# There will be at least one option for **2%** extra credit––filling out an introductory survey about:
# 
# - Experience/comfort with programming.  
# - Major (or intended major).  
# - Other background information.

# ### Answers to FAQ
# 
# - There are **no prerequisites** for this course.  
# - There are **no midterms** or **final exam**.
# 
# [See the FAQ page](https://seantrott.github.io/css1_ucsd/course/expectations.html#) for more information.

# ### Academic Integrity
# 
# From the syllabus:
# 
# > Please turn in your own work. While you are encouraged to work together on some assignments (e.g., on [labs](../labs/overview.md)), you should still understand the code you've submitted. Problem sets and final project should be completed independently.
# 
# > Please review academic integrity policies [here](http://academicintegrity.ucsd.edu). Cheating and plagiarism are unfair to other students and ultimately to yourself, and you will be penalized if caught. Instead, if you're struggling with something, please come to office hours and ask for help! 
# 

# ## Welcome to CSS!
