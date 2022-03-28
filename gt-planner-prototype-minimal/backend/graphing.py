import graphviz


def calculate_immediacy(curr, name): # recursive AND divergent. gonna be a memory hog.
    # if completed, return 0 (here because of optimization)
    if curr[name]['done']: return 0 # colorscheme is 1-indexed. a hack. but hard otherwise because of string casting. 

    # if no pre-req, return 0
    prereqs = curr[name]['prqs']
    if not prereqs: return 0 # see note above # delete both of these note of this line returns 0

    a = [] # dumb name?
    for prereq in prereqs: 
        # does co-req mess up immediacy calculation? or cause infinite loops?
        if prereq[-1]=='*': a.append(calculate_immediacy(curr, prereq[:-1]) + 1) 
        else: a.append(calculate_immediacy(curr, prereq) + 1) 

    return max(a)


def update_immediacies(curr): # probably mutable
    for course, item in curr.items():
        curr[course]['immediacy'] = calculate_immediacy(curr, course)


# dictionary implementation for in vivo user customization possibility (aka working with json)

# colorful = {'completed_node': , 
#             'immediate_node': , 
#             'normal_node'   : [], 
#             'capstone_node' : , 
#             'completed_edge': , 
#             'immediate_edge': , 
#             'normal_edge'   : }

# colorful_border = {}



# more complex may still be good (i.e., linking parameters by dict omittance.) (ex. assume completed_edge to be slightly darkened completed_node if not explicitly set)
# designing a good api is hard!
# just make sure that the following is true:
# 1. json-based, easy (reduced-parameter) customization is possible
# 2. gradient border is possible
# 3. class information may be used in determining color
# since this introduces behavior beyond state (i.e., not a state machine anymore), class with one inheritance seems the best.
# also realize that function calls are a lot more expensive than data access (may not be true), so state-based (dict) implementation is better in perf
# premature optimization = root of all evil. let's go w class

class Theme: 
    def __init__(self, palette): pass
    def outline(self, course, immediacy, completed, capstone): pass
    def node(self, course, immediacy, completed, capstone): pass
    def edge(self, course, immediacy, completed): pass

black_white_yellow_palette = {
                     'border'        : '#888888',
                     'completed_node': '#008000', 
                     'immediate_node': '#FEE715', 
                     'normal_node'   : '#000000', 
                     'capstone_node' : '#600060', 
                     'normal_edge'   : '#a0a0a0'}

class black_white_yellow(Theme):
    def __init__(self, palette): 
        self.palette = palette
        self.node_attributes = {'fontcolor': 'white'}

    # instead of making border the same color as fill, let's rather make it possible to `node_attr` using theme class
    def border(self, course=None, immediacy=0, completed=False, capstone=False):
        if immediacy == 0: return str(self.palette['immediate_node'])
        else: return str(self.palette['border'])


    def node(self, course=None, immediacy=0, completed=False, capstone=False): 
        if completed: return str(self.palette['completed_node']) # not sure if this is even needed.
        elif immediacy == 0: return str(self.palette['immediate_node'])
        elif capstone: return str(self.palette['capstone_node'])
        else: return str(self.palette['normal_node'])

    # 슈발 이것도 draw가 쓰게 시키려면 또 복잡해지네... 어케 해야 하는겨 ㅠ,ㅠ
    # 콜백? 그냥 identifier keyword만 주고 ('immediate', 'capstone', 이렇게?)
    def fontcolor(self, course=None, immediacy=0, completed=False, capstone=False):
        # really just depends on nodecolor
        if completed or immediacy == 0: return '#000000'
        else: return 'white'

    def edge(self, course=None, immediacy=0, completed=False): 
        if completed: return str(self.palette['completed_node']) # darken a bit
        elif immediacy == 0: return str(self.palette['immediate_node']) # darken a bit
        else: return str(self.palette['normal_edge'])
# turning a behavioral system into state system is called baking.
# unsure about baking possibility considering the likely importance of differentiating major-oriented classes

# but actually it's possible to create an intelligent, flexible single class instead of relying on subclasses
# where it smartly infers behaviors depending on the explicitness of palette definition


bwy = black_white_yellow(black_white_yellow_palette)


def draw(curriculum, theme):
    # TODO: implement border colors
    # TODO: add borders to edge
    #     not sure if possible

    # GRAPH
    c = graphviz.Digraph('Curriculum') # format='jpg' # filename='process.gv'
    c.attr(rankdir='LR') # make this horizontal. (important)
    c.attr(bgcolor='transparent')

    # node defaults
    c.node_attr['shape'] = 'box'
    c.node_attr['style'] = 'rounded, filled'
    # border
    c.node_attr['color'] = 'black'
    c.node_attr['penwidth'] = '0.5'
    # font
    # c.node_attr['fontname'] = 'Roboto Serif'
    c.node_attr['fontsize'] = '10'
    # theme attributes
    if theme.node_attributes: 
        for key, value in theme.node_attributes.items():
            c.node_attr[key] = value

    # edge defaults
    c.edge_attr['arrowsize'] = '0.65'
    c.edge_attr['penwidth'] = '1.5'

    # DRAWING

    # iterate upon each course
    for course, content in curriculum.items():
        prqs, year, done, imme = list(content.values()) # i love dicts
        # print(course, prqs, year, done, imme) # DEBUG

        # done (i.e., not drawn)
        if done: continue

        # make the node!
        c.node(course, fillcolor=theme.node(course, imme, done), color=theme.border(course, imme, done), fontcolor=theme.fontcolor(course, imme))

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
                    c.edge(prq[:-1], course, constraint='false', color=theme.edge(prq[:-1], imme-1), style='dashed')
                
                # pre-req
                else: 
                    # c.node(prq, color=str(imme+1))
                    if curriculum[prq]['done']: continue
                    c.edge(prq, course, color=theme.edge(prq, imme-1), style='solid')
    
    return c


def return_str(graph):
    return str(graph)


# Drawing Workflow
def get_dot_source(curr):
    # process immediacy
    update_immediacies(curr)

    # draw graph
    c = draw(curr, bwy)

    # return as string
    return str(c)


if __name__ == "__main__":
    from data import default_curriculums
    test_curr = default_curriculums['ME']
    print(get_dot_source(test_curr))
