# %% [markdown]
# # **Secondary Experiment**: Intro

# %% [markdown]
# ## Objectives
# - Data Representation & Structure
#   - Rich curriculum representation w/ year, immediacy, **credit hours** 🆇
#     - possibly reverse-prerequisite. (calculation possibly trivial by utilizing immediacy — subtract from max of local capstone depths)
#   - Softly enforced rank rule for Graphviz 🆇
#     - make co-reqs [not add a new rank](https://stackoverflow.com/questions/22756929/graphviz-make-edges-not-affecting-the-hierarchy-of-nodes). ✅
#     - Free-standing course (or course couple): calculate average year of each rank (=column), get their average year, attach to closest match.
#       - Implementation difficulty: ?
#         - Is **fetching** rank possible? Or is graphviz an in-only interface. 
#         - Should energy minimization, path-overlap minimization, and placement in-housed to be able to do this? 😭
#     - Sorting (year-by-year group) 🆇
#       - in the ideal case, courses will be compressed to where curriculum is 6-7 semesters long. 
#       - then we start to de-compress it by using credit-hour calculations
#       - eventually need to give users the ability to manually adjust (drag) courses. 
#         - no way I can implement that ...
# - Aesthetics
#   - decision: Do make use of gradient by immediacy. only capstone is special color. ✅
#     - Color according to completion 🆇
#   - **title, credit hour label (honestly for dev as much as for users)** 🆇
#   - make font work 🆇
# - Interactivity (where we left off in preliminary experiment) ✅
#   - completion-aware graph drawing ✅

# %% [markdown]
# ### Coming Up

# %% [markdown]
# - Course & pre-requisite database pulled from OSCAR/GT-Scheduler/Degreeworks
#   - Option 1: Interactive editor / administrator page
#   - Option 2: Richer curriculum representation in Excel (options functionality)
#     - whole system (may) need to accommodate this: Humanities are redundant so dict may not be best, etc
# - In final UI, users are able to know whether courses are available in the given semester or not by using OSCAR info. 
#   - i.e., can choose lorraine to learn that it's available. or check historical availability patterns.
#   - if they include summer, then following assumed semesters move along together

# %% [markdown]
# # 0. Setup

# %%
import pandas as pd
import numpy as np

filename = 'me.csv'

df = pd.read_csv(filename)

# %%
# regex-based string -> list conversion
import re

curriculum = {}

# immediate explicit pre-requisites
for i in range(df.shape[0]):
    if pd.isna(df.iloc[i,0]): # NaN
        curriculum[df.iloc[i,1]] = []
    else: # pre-reqs exist. put them into list
        curriculum[df.iloc[i,1]] = re.split('\, ', df.iloc[i,0]) 

# %%
verbose = False # DEBUG

def treeshake(curriculum):
    curr = curriculum.copy()
    
    # iterate over each course in curriculum
    for course, pre_reqs in curriculum.items():
        if verbose: print('new case:', course) # DEBUG
        
        # introductory course
        if not pre_reqs: continue

        # set of implicit prerequisites
        seen = set()

        # fetch implicit prerequisite (depth 1)
        for (idx, explicit) in enumerate(pre_reqs):
            # handle co-req 
            exp = explicit[:-1] if explicit[-1] == '*' else explicit

            # introductory explicit
            if not curr[exp]: continue 
            # important to keep this line. removing this breaks the whole thing

            # 
            for (jdx, implicit) in enumerate(curr[exp]):
                # if idx == jdx: continue # unsure if necessary / helpful. TEST BOTH WAYS.
                # if candidate not in seen:  # Note: doesn't seem necessary because set is unique anyway.
                seen.add(implicit)
                    # curriculum[course].pop(idx)
        
        if verbose: print('implicit:', seen)
        # if an implicit prerequisite is made explicit (redundancy), remove the explicit.
        for (idx, target) in enumerate(pre_reqs):
            if target in seen: 
                curr[course].pop(idx)
                if verbose: print('DELETED:', target)

    return curr

# %%
curriculum = treeshake(curriculum)

# %%
simple_curr = curriculum

# %% [markdown]
# # **1. Data Representation & Graph Structure**

# %%
def infer_year(name):
    searched = re.search("\ [0-9]", name)
    if searched: return int(searched.group()[1]) # the second char of search result

# %%
def calc_immediacy(name): # recursive AND divergent. gonna be a memory hog.
    # if completed, return 0 (here because of optimization)
    if curr[name]['done']: return 0 # colorscheme is 1-indexed. a hack. but hard otherwise because of string casting. 

    # if no pre-req, return 0
    prereqs = curr[name]['prqs']
    if not prereqs: return 0 # see note above # delete both of these note of this line returns 0

    a = [] # dumb name?
    for prereq in prereqs: 
        # does co-req mess up immediacy calculation? or cause infinite loops?
        if prereq[-1]=='*': a.append(calc_immediacy(prereq[:-1]) + 1) 
        else: a.append(calc_immediacy(prereq) + 1) 

    return max(a)

# %% [markdown]
# Possible optimization: initialize immediacy to None. Note that we iteratively compute immediacies. If all explicit pre-reqs confronted by a higher-up class has already been determined (i.e., not None but rather 0/1/2/3...), then go ahead and take the max rather than recursing all the way through zero depth. This way, compute time increases linearly not quadratically (though there still are inefficients because we're using conditionals).

# %%
curr = {}

for course, item in simple_curr.items():
    curr[course] = {}
    curr[course]['prqs'] = item
    curr[course]['year'] = infer_year(course)
    curr[course]['done'] = False

for course, item in simple_curr.items():
    curr[course]['immediacy'] = calc_immediacy(course)

# %%
curr

# %% [markdown]
# # **2. Aesthetics**

# %% [markdown]
# Design References:
# - [Black/white, modern, great use of thickness and scale](https://graphviz.org/Gallery/directed/psg.svg)
# 
# 

# %% [markdown]
# Thinking about UI
# - Mouseover → highlight relevant incoming, outgoing pre-reqs

# %% [markdown]
# ## **2.1. Colors**

# %% [markdown]
# Resources
# - [Color Converter](https://convertingcolors.com/rgb-color-92_87_120.html?search=RGB(92,%2087,%20120))
# 
# OG Graphviz Documentation
# - [Background Color](https://graphviz.org/docs/attrs/bgcolor/)
# - [Color](https://graphviz.org/docs/attr-types/color/)
# - [Border/Fill Color](https://stackoverflow.com/questions/9106079/graphviz-how-to-change-border-color)
# 
# Python-specific Graphviz Documentation
# - [Read the Docs](https://graphviz.readthedocs.io/en/stable/index.html)

# %% [markdown]
# To-Do
# - Arrow thickness, brightness optimization

# %%
# color utils

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

# rgb_to_hex((255, 255, 195)) # test

def hex_to_rgb(value):
    value = value.lstrip('#')
    return tuple(int(value[i:i+2], 16) for i in range(0, 6, 2))

# hex_to_rgb("FF65BA") # test

def glow(base, highlight):
    # need to mix color so that highlight is weaker — something like 0.2

    hw = 0.35  # highlight weight
    bw = 1-hw # base weight

    r,g,b = hex_to_rgb(base)
    u,v,w = hex_to_rgb(highlight)
    r,g,b = (int(bw*r+hw*u), int(bw*g+hw*v), int(bw*b+hw*w))

    hl = '#' + rgb_to_hex((r,g,b)).upper()

    return base+';'+'0.9:'+hl 
    # the number doesn't matter when doing radial. i think. at least when only with two numbers -> only two number is possible.

# test line?

# %%
# COLOR BANK
# not perfect. let's keep improving this.

# backgrounds
base = '#2A2556'
base_dark = '#101C4D'
nodebg = '#333163'

# bright things
font = '#F5EEE8'
arrow = '#AFABB4' # '#9B97BA' # '#827EA0'
# weakwhite = #827EA0 # maybe.

# colorful things
green = '#ADB766'
# yellow = 
orange = '#AB706E'
lightblue = '#89AFA3'
blue = '#497797'



# %%
import graphviz

# %%
def get_graph():
    # graph
    c = graphviz.Digraph('Curriculum') # format='jpg' # filename='process.gv'
    c.attr(rankdir='LR') # make this horizontal. (important)
    c.attr(style='radial')
    c.attr(bgcolor=base+';0.5:'+base_dark) # DEBUG
    c.attr(fontname='Helvetica') # DOESN'T WORK. Why?

    # node defaults
    c.node_attr['shape'] = 'box'
    c.node_attr['style'] = 'rounded, filled, radial'
    # border
    c.node_attr['color'] = orange
    c.node_attr['penwidth'] = '2.5'
    c.node_attr['colorscheme']='ylgnbu9' # colorbrewer scheme
    # fill
    c.node_attr['fillcolor'] = glow(base_dark, orange) # '#333163' # '#292759' # DEBUG
    # font
    c.node_attr['fontcolor'] = font
    c.node_attr['fontsize'] = '12'

    # edge defaults
    c.edge_attr['color'] = arrow # arrow # arrow color
    c.edge_attr['arrowsize'] = '0.75'

    return c

# %%
def draw_scheme(curriculum):
    # TODO: add outlines to edge
    # gonna be a good idea to implement colorscheme darkmode! capstone becomes filled.
    
    # GRAPH
    c = graphviz.Digraph('Curriculum') # format='jpg' # filename='process.gv'
    c.attr(rankdir='LR') # make this horizontal. (important)

    # node defaults
    c.node_attr['shape'] = 'box'
    c.node_attr['style'] = 'rounded, filled, radial'
    c.node_attr['colorscheme']= 'spectral11' # 'ylgnbu9' # colorbrewer scheme
    offset = 3
    # border
    c.node_attr['color'] = 'black'
    c.node_attr['penwidth'] = '1.5'
    # fill
    # c.node_attr['fillcolor'] # UNIQUE
    # font
    c.node_attr['fontsize'] = '12'


    # edge defaults
    # c.edge_attr['color'] # UNIQUE
    c.edge_attr['arrowsize'] = '0.65'
    c.edge_attr['colorscheme']= 'spectral11' # 'ylgnbu9' # colorbrewer scheme
    c.edge_attr['penwidth'] = '3'
    # irrelevant parameters were pruned; fetch original @ draw_normal

    # DRAWING

    # iterate upon each course
    for course, content in curriculum.items():
        prqs, year, done, imme = list(content.values()) # i love dicts
        # print(course, prqs, year, done, imme) # DEBUG

        # done (i.e., not drawn)
        if done: continue

        # make the node!
        c.node(course, fillcolor=str(imme+offset))

        # introductory (i.e., no pre-req)
        if not prqs: continue

        # has pre-reqs
        else:
            for prq in prqs:
        
                # co-req
                if prq[-1] == '*': 
                    # Note: I'd love to make an alias of prq here with * removed, but I'm worried about mutation.
                    # c.node(prq[:-1], color=str(imme+1))
                    if curriculum[prq[:-1]]['done']: continue
                    c.edge(prq[:-1], course, constraint='false', color=str(imme+offset), style='dashed')
                
                # pre-req
                else: 
                    # c.node(prq, color=str(imme+1))
                    if curriculum[prq]['done']: continue
                    c.edge(prq, course, color=str(imme+offset), style='solid')

    c.render(filename='dots/g4.gv')
    
    return c

# draw_scheme(curr)

# %%
def draw_normal(curriculum):
    
    c = get_graph()

    # iterate upon each course
    for course, content in curriculum.items():
        prqs, year, done, imme = content['prqs'], content['year'], content['done'], content['immediacy'] # what a hack.
        # print(course, prqs, year, done, imme) # DEBUG
    
        c.node(course, color=str(imme+1)) # fillcolor=glow(base_dark, green))


        # introductory course
        if not prqs: continue
            # ensures that introductory courses exist
        

        # has pre-reqs
        else:
            for prq in prqs:
        
                # co-req
                if prq[-1] == '*': 
                    # c.node(prq[:-1], color=str(imme+1))
                    c.edge(prq[:-1], course, color=lightblue)
                
                # pre-req
                else: 
                    # c.node(prq, color=str(imme+1))
                    c.edge(prq, course)
    return c

# %% [markdown]
# # **3. Interactivity**

# %%
from ipywidgets import widgets
from IPython.display import display

# %% [markdown]
# > Keep this as list or make it dict? 🤔 Considering case of curriculum deviation (where user's taken non-degree-counting courses) and scalability (dict faster), **dict** it is.

# %%
# Nx4 matrix(?) of checkboxes representing completed courses
completion = {} 
for course in curr.keys(): completion[course] = widgets.Checkbox(description=course)
width = 4; height = len(completion)//width+1 # boundary case ain't perfect but still
columns = []
for i in range(width): columns.append(widgets.VBox(list(completion.values())[height*i:height*(i+1)])) # saturate the columns
hbox = widgets.HBox([*columns]) # dot operator unpacks an iterable
# button: apply checkbox state to curr
button = widgets.Button(description='Apply Changes', button_style='info', icon='check'); 

def apply_completion(button): # mutable. trivial.
    for course, content in curr.items():
        content['done'] = completion[course].value

button.on_click(apply_completion)

# %%
# display(widgets.VBox([widgets.Label('Check your completed courses.'), hbox, button]))

# %% [markdown]
# [Fuck Jupyter...](https://gist.github.com/pbugnion/5bb7878ff212a0116f0f1fbc9f431a5c) Switching to Colab a good idea? Nevermind, Jupyter good... **Still switch to Colab?**

# %% [markdown]
# **`complete_course()`**
# 
# Let's make it non-mutable. Nah let's make it mutable.
# 
# Pseudocode:
# - if a completed course is within curriculum, find and delete all occurrence of it as a pre-req.
# - if it has a pre-req (not a co-req), delete all of its pre-reqs too.

# %% [markdown]
# # **A. Output Screen**

# %%
# curr

# %%
display(widgets.VBox([widgets.Label('Check your completed courses.'), hbox, button]))

# %%
gv = draw_scheme(curr)

# %%
print('a')


