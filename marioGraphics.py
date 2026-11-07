'''
GUIDING PRINCIPLE (DUALITY)
-projections involving points are POINTS
-sections involving points are LINES
-swapping: a,b=b,a
# BASIC COLORS
WHITE    = (255,255,255); GRAY     = (128,128,128); SILVER   = (192,192,192); BLACK    = (  0,  0,  0)
MAROON   = (128,  0,  0); RED      = (255,  0,  0); PURPLE   = (128,  0,128); FUCHSIA  = (255,  0,255)
GREEN    = (  0,128,  0); LIME     = (  0,255,  0); OLIVE    = (128,128,  0); YELLOW   = (255,255,  0)
NAVY     = (  0,  0,128); BLUE     = (  0,  0,255); TEAL     = (  0,128,128); AQUA     = (  0,255,255)
'''
"""
    ELLIPSE (center, radii)

    x = e.c.x + e.rx * cos(t)
    y = e.c.y + e.ry * sin(t)
"""
from sys import *
from math import *
from os import *
from random import *
from string import *
from time import *
from datetime import *
from calendar import *
from inspect import *
from fractions import *
from copy import *
from marioConsole import *

if version() == 2:
    from Tkinter import *
elif version() == 3:
    from tkinter import *

#------------------------------- HTML-STYLE COLORS
# RED
INDIANRED      = (205, 92, 92); LIGHTCORAL      = (240,128,128); SALMON        = (250,128,114); DARKSALMON     = (233,150,122); LIGHTSALMON          = (255,160,122); CRIMSON         = (220, 20, 60); RED         	= (255,  0,  0); FIREBRICK         = (178, 34, 34); DARKRED         = (139,  0,  0)
# PINK
PINK           = (255,192,203); LIGHTPINK       = (255,182,193); HOTPINK       = (255,105,180); DEEPPINK       = (255, 20,147); MEDIUMVIOLETRED      = (199, 21,133); PALEVIOLETRED   = (219,112,147)
# ORANGE
LIGHTSALMON    = (255,160,122); CORAL           = (255,127, 80); TOMATO        = (255, 99, 71); ORANGERED      = (255, 69,  0); DARKORANGE           = (255,140,  0); ORANGE          = (255,165,  0)
# YELLOW
GOLD           = (255,215,  0); YELLOW          = (255,255,  0); LIGHTYELLOW   = (255,255,224); LEMONCHIFFON   = (255,250,205); LIGHTGOLDENRODYELLOW = (250,250,210); PAPAYAWHIP      = (255,239,213); MOCCASIN         = (255,228,181); PEACHPUFF         = (255,218,185); PALEGOLDENROD   = (238,232,170); KHAKI           = (240,230,140); DARKKHAKI        = (189,183,107)
# PURPLE
LAVENDER       = (230,230,250); THISTLE         = (216,191,216); PLUM          = (221,160,221); VIOLET         = (238,130,238); ORCHID               = (218,112,214); FUCHSIA         = (255,  0,255); MAGENTA          = (255,  0,255); MEDIUMORCHID      = (186, 85,211); MEDIUMPURPLE    = (147,112,219); BLUEVIOLET      = (138, 43,226); DARKVIOLET       = (148,  0,211); DARKORCHID        = (153, 50,204); DARKMAGENTA    = (139,  0,139); PURPLE         = (128,  0,128); INDIGO          = ( 75,  0,130); SLATEBLUE       = (106, 90,205); DARKSLATEBLUE   = ( 72, 61,139); MEDIUMSLATEBLUE = (123,104,238)
# GREEN
GREENYELLOW    = (173,255, 47); CHARTREUSE      = (127,255,  0); LAWNGREEN     = (124,252,  0); LIME           = (  0,255,  0); LIMEGREEN            = ( 50,205, 50); PALEGREEN       = (152,251,152); LIGHTGREEN       = (144,238,144); MEDIUMSPRINGGREEN = (  0,250,154); SPRINGGREEN     = (  0,255,127); MEDIUMSEAGREEN  = ( 60,179,113); SEAGREEN         = ( 46,139, 87); FORESTGREEN       = ( 34,139, 34); GREEN          = (  0,128,  0); DARKGREEN      = (  0,100,  0); YELLOWGREEN     = (154,205, 50); OLIVEDRAB       = (107,142, 35); OLIVE           = (128,128,  0); DARKOLIVEGREEN  = ( 85,107, 47); MEDIUMAQUAMARINE = (102,205,170); DARKSEAGREEN   = (143,188,143); LIGHTSEAGREEN    = ( 32,178,170); DARKCYAN     = (  0,139,139); TEAL       = (  0,128,128)
# BLUE
AQUA           = (  0,255,255); CYAN            = (  0,255,255); LIGHTCYAN     = (224,255,255); PALETURQUOISE  = (175,238,238); AQUAMARINE           = (127,255,212); TURQUOISE       = ( 64,224,208); MEDIUMTURQUOISE  = ( 72,209,204); DARKTURQUOISE     = (  0,206,209); CADETBLUE       = ( 95,158,160); STEELBLUE       = ( 70,130,180); LIGHTSTEELBLUE   = (176,196,222); POWDERBLUE        = (176,224,230); LIGHTBLUE      = (173,216,230); SKYBLUE        = (135,206,235); LIGHTSKYBLUE    = (135,206,250); DEEPSKYBLUE     = (  0,191,255); DODGERBLUE      = ( 30,144,255); CORNFLOWERBLUE  = (100,149,237); MEDIUMSLATEBLUE  = (123,104,238); ROYALBLUE      = ( 65,105,225); BLUE             = (  0,  0,255); MEDIUMBLUE   = (  0,  0,205); DARKBLUE   = (  0,  0,139); NAVY    = (  0,  0,128); MIDNIGHTBLUE   = ( 25, 25,112)
# BROWN
CORNSILK       = (255,248,220); BLANCHEDALMOND  = (255,235,205); BISQUE        = (255,228,196); NAVAJOWHITE    = (255,222,173); WHEAT                = (245,222,179); BURLYWOOD       = (222,184,135); TAN              = (210,180,140); DRAB              = (210,180,140); ROSYBROWN       = (188,143,143); SANDYBROWN      = (244,164, 96); GOLDENROD        = (218,165, 32); DARKGOLDENROD     = (184,134, 11); PERU           = (205,133, 63); CHOCOLATE      = (210,105, 30); SADDLEBROWN     = (139, 69, 19); SIENNA          = (160, 82, 45); BROWN           = (165, 42, 42); MAROON          = (128,  0,  0)
# WHITE
WHITE          = (255,255,255); SNOW            = (255,250,250); HONEYDEW      = (240,255,240); MINTCREAM      = (245,255,250); AZURE                = (240,255,255); ALICEBLUE       = (240,248,255); GHOSTWHITE       = (248,248,255); WHITESMOKE        = (245,245,245); SEASHELL        = (255,245,238); BEIGE           = (245,245,220); OLDLACE          = (253,245,230); FLORALWHITE       = (255,250,240); IVORY          = (255,255,240); ANTIQUEWHITE   = (250,235,215); LINEN           = (250,240,230); LAVENDERBLUSH   = (255,240,245); MISTYROSE       = (255,228,225)
# GREY
GAINSBORO      = (220,220,220); LIGHTGRAY       = (211,211,211); LIGHTGREY     = (211,211,211); SILVER         = (192,192,192); DARKGRAY             = (169,169,169); DARKGREY        = (169,169,169); GRAY             = (128,128,128); GREY              = (128,128,128); DIMGRAY         = (105,105,105); DIMGREY         = (105,105,105); LIGHTSLATEGRAY   = (119,136,153); LIGHTSLATEGREY    = (119,136,153); SLATEGRAY      = (112,128,144); SLATEGREY      = (112,128,144); DARKSLATEGRAY   = ( 47, 79, 79); DARKSLATEGREY   = ( 47, 79, 79); BLACK           = (  0,  0,  0)
'''
COLORS = ()
# RED
COLORS = COLORS + (INDIANRED,LIGHTCORAL,SALMON,DARKSALMON,LIGHTSALMON,CRIMSON,RED,FIREBRICK,DARKRED)
# PINK
COLORS = COLORS + (PINK,LIGHTPINK,HOTPINK,DEEPPINK,MEDIUMVIOLETRED,PALEVIOLETRED)
# ORANGE
COLORS = COLORS + (LIGHTSALMON,CORAL,TOMATO,ORANGERED,DARKORANGE,ORANGE)
# YELLOW
COLORS = COLORS + (GOLD,YELLOW,LIGHTYELLOW,LEMONCHIFFON,LIGHTGOLDENRODYELLOW,PAPAYAWHIP,MOCCASIN,PEACHPUFF,PALEGOLDENROD,KHAKI,DARKKHAKI)
# PURPLE
COLORS = COLORS + (LAVENDER,THISTLE,PLUM,VIOLET,ORCHID,FUCHSIA,MAGENTA,MEDIUMORCHID,MEDIUMPURPLE,BLUEVIOLET,DARKVIOLET,21DARKORCHID,DARKMAGENTA,PURPLE,INDIGO,SLATEBLUE,DARKSLATEBLUE,MEDIUMSLATEBLUE)
# GREEN
COLORS = COLORS + (GREENYELLOW,CHARTREUSE,LAWNGREEN,LIME,LIMEGREEN,PALEGREEN,LIGHTGREEN,MEDIUMSPRINGGREEN,SPRINGGREEN,MEDIUMSEAGREEN,SEAGREEN,FORESTGREEN,GREEN,DARKGREEN,YELLOWGREEN,OLIVEDRAB,OLIVE,DARKOLIVEGREEN,MEDIUMAQUAMARINE,DARKSEAGREEN,LIGHTSEAGREEN,DARKCYAN,TEAL)
# BLUE
COLORS = COLORS + (AQUA,CYAN,LIGHTCYAN,PALETURQUOISE,AQUAMARINE,TURQUOISE,MEDIUMTURQUOISE,DARKTURQUOISE,CADETBLUE,STEELBLUE,LIGHTSTEELBLUE,POWDERBLUE,LIGHTBLUE,SKYBLUE,LIGHTSKYBLUE,DEEPSKYBLUE,DODGERBLUE,CORNFLOWERBLUE,MEDIUMSLATEBLUE,ROYALBLUE,BLUE,MEDIUMBLUE,DARKBLUE,NAVY,MIDNIGHTBLUE)
# BROWN
COLORS = COLORS + (CORNSILK,BLANCHEDALMOND,BISQUE,NAVAJOWHITE,WHEAT,BURLYWOOD,TAN,DRAB,ROSYBROWN,SANDYBROWN,GOLDENROD,DARKGOLDENROD,PERU,CHOCOLATE,SADDLEBROWN,SIENNA,BROWN,MAROON)
# WHITE
COLORS = COLORS + (WHITE,SNOW,HONEYDEW,MINTCREAM,AZURE,ALICEBLUE,GHOSTWHITE,WHITESMOKE,SEASHELL,BEIGE,OLDLACE,FLORALWHITE,IVORY,ANTIQUEWHITE,LINEN,LAVENDERBLUSH,MISTYROSE)
# GREY
COLORS = COLORS + (GAINSBORO,LIGHTGRAY,LIGHTGREY,SILVER,DARKGRAY,DARKGREY,GRAY,GREY,DIMGRAY,DIMGREY,LIGHTSLATEGRAY,LIGHTSLATEGREY,SLATEGRAY,SLATEGREY,DARKSLATEGRAY,DARKSLATEGREY,BLACK)
'''
COLORS = ['black', 'white', 'green', 'snow', 'aqua', 'ghostwhite', 'whitesmoke', 'gainsboro', 'floralwhite', 'oldlace',
    'lightgreen', 'lightpink', 'lightsalmon',
    'aliceblue', 'magenta', 'olive', 'firebrick', 'tan',
    'linen', 'antiquewhite', 'papayawhip', 'blanchedalmond', 'bisque', 'peachpuff',
    'navajowhite', 'lemonchiffon', 'mintcream', 'azure', 'aliceblue', 'lavender',
    'lavenderblush', 'mistyrose', 'darkslategray', 'dimgray', 'slategray',
    'lightslategray', 'gray', 'lightgrey', 'midnightblue', 'navy', 'cornflowerblue', 'darkslateblue',
    'slateblue', 'mediumslateblue', 'lightslateblue', 'mediumblue', 'royalblue', 'blue',
    'dodgerblue', 'deepskyblue', 'skyblue', 'lightskyblue', 'steelblue', 'lightsteelblue',
    'lightblue', 'powderblue', 'paleturquoise', 'darkturquoise', 'mediumturquoise', 'turquoise',
    'cyan', 'lightcyan', 'cadetblue', 'mediumaquamarine', 'aquamarine', 'darkgreen', 'darkolivegreen',
    'darkseagreen', 'seagreen', 'mediumseagreen', 'lightseagreen', 'palegreen', 'springgreen',
    'lawngreen', 'mediumspringgreen', 'greenyellow', 'limegreen', 'yellowgreen',
    'forestgreen', 'olivedrab', 'darkkhaki', 'khaki', 'palegoldenrod', 'lightgoldenrodyellow',
    'lightyellow', 'yellow', 'gold', 'lightgoldenrod', 'goldenrod', 'darkgoldenrod', 'rosybrown',
    'indianred', 'saddlebrown', 'sandybrown',
    'darksalmon', 'salmon', 'lightsalmon', 'orange', 'darkorange',
    'coral', 'lightcoral', 'tomato', 'orangered', 'red', 'hotpink', 'deeppink', 'pink', 'lightpink',
    'palevioletred', 'maroon', 'mediumvioletred', 'violetred',
    'mediumorchid', 'darkorchid', 'darkviolet', 'blueviolet', 'purple', 'mediumpurple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'antiquewhite1', 'antiquewhite2',
    'antiquewhite3', 'antiquewhite4', 'bisque2', 'bisque3', 'bisque4', 'peachpuff2',
    'peachpuff3', 'peachpuff4', 'navajowhite2', 'navajowhite3', 'navajowhite4',
    'lemonchiffon2', 'lemonchiffon3', 'lemonchiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'lavenderblush2', 'lavenderblush3', 'lavenderblush4', 'mistyrose2', 'mistyrose3',
    'mistyrose4', 'azure2', 'azure3', 'azure4', 'slateblue1', 'slateblue2', 'slateblue3',
    'slateblue4', 'royalblue1', 'royalblue2', 'royalblue3', 'royalblue4', 'blue2', 'blue4',
    'dodgerblue2', 'dodgerblue3', 'dodgerblue4', 'steelblue1', 'steelblue2',
    'steelblue3', 'steelblue4', 'deepskyblue2', 'deepskyblue3', 'deepskyblue4',
    'skyblue1', 'skyblue2', 'skyblue3', 'skyblue4', 'lightskyblue1', 'lightskyblue2',
    'lightskyblue3', 'lightskyblue4', 'slategray1', 'slategray2', 'slategray3',
    'slategray4', 'lightsteelblue1', 'lightsteelblue2', 'lightsteelblue3',
    'lightsteelblue4', 'lightblue1', 'lightblue2', 'lightblue3', 'lightblue4',
    'lightcyan2', 'lightcyan3', 'lightcyan4', 'paleturquoise1', 'paleturquoise2',
    'paleturquoise3', 'paleturquoise4', 'cadetblue1', 'cadetblue2', 'cadetblue3',
    'cadetblue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'darkslategray1', 'darkslategray2', 'darkslategray3', 'darkslategray4',
    'aquamarine2', 'aquamarine4', 'darkseagreen1', 'darkseagreen2', 'darkseagreen3',
    'darkseagreen4', 'seagreen1', 'seagreen2', 'seagreen3', 'palegreen1', 'palegreen2',
    'palegreen3', 'palegreen4', 'springgreen2', 'springgreen3', 'springgreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'olivedrab1', 'olivedrab2', 'olivedrab4', 'darkolivegreen1', 'darkolivegreen2',
    'darkolivegreen3', 'darkolivegreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'lightgoldenrod1', 'lightgoldenrod2', 'lightgoldenrod3', 'lightgoldenrod4',
    'lightyellow2', 'lightyellow3', 'lightyellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'darkgoldenrod1', 'darkgoldenrod2', 'darkgoldenrod3', 'darkgoldenrod4',
    'rosybrown1', 'rosybrown2', 'rosybrown3', 'rosybrown4', 'indianred1', 'indianred2',
    'indianred3', 'indianred4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'lightsalmon2', 'lightsalmon3', 'lightsalmon4', 'orange2',
    'orange3', 'orange4', 'darkorange1', 'darkorange2', 'darkorange3', 'darkorange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'orangered2',
    'orangered3', 'orangered4', 'red2', 'red3', 'red4', 'deeppink2', 'deeppink3', 'deeppink4',
    'hotpink1', 'hotpink2', 'hotpink3', 'hotpink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'lightpink1', 'lightpink2', 'lightpink3', 'lightpink4', 'palevioletred1',
    'palevioletred2', 'palevioletred3', 'palevioletred4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'violetred1', 'violetred2', 'violetred3', 'violetred4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'mediumorchid1', 'mediumorchid2', 'mediumorchid3',
    'mediumorchid4',  'darkorchid1',  'darkorchid2',  'darkorchid3',  'darkorchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'mediumpurple1', 'mediumpurple2',
    'mediumpurple3', 'mediumpurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

EQUALITY = 0.0001               #   magic constants
EPSILON = 0.000000000001
INFINITY = float('inf')
NEGATIVE_INFINITY = -INFINITY

def iscolor(*args):             #   check for color tuples or strings
    x = False
    if len(args)==1:
        o = args[0]
        if isinstance(o,str) and o.lower() in COLORS:
            x = True
        elif isinstance(o,str) and len(o)==7 and o[0]=='#':
            o = o.lower()
            c = 0
            for w in o[1:]:
                if not ( w in '0123456789' or w in 'abcdef'):
                    c+= 1
            x = ( c == 0 )
        else:
            x = isinstance(o, (list, tuple)) and len(o)>=3 and isnumeric(o[0]) and isnumeric(o[1]) and isnumeric(o[2]) and (0<=o[0]<=255) and (0<=o[1]<=255) and (0<=o[2]<=255)
    return x
def marioColor(c):
    if isinstance(c,str):
        return c.replace(' ','')
    else:
        return '#' + format(c[0],'02x') + format(c[1],'02x') + format(c[2],'02x') if iscolor(c) else '#000000'
def sign(a):
    v = float('nan')
    if isinstance(a,int) or isinstance(a,float):
        v=0
        if a>0:
            v=1
        elif a<0:
            v=-1
    return v
def rangeF(a=0,b=0,c=1):        #   simulation of a FLOAT RANGE
    if not ( isinstance(a,int) or isinstance(a,float) ): a=0
    if not ( isinstance(b,int) or isinstance(b,float) ): b=0
    if not ( isinstance(c,int) or isinstance(c,float) ): c=1
    while c>0 and a<=b or c<0 and a>=b:
        yield a
        a+= c
def zero_2PI(a):                #   reduce angles to one rotation
    _a= abs(a)
    _a= _a//(2.*pi)
    _a= _a*2.*pi
    if a>=0:
        a-= _a
    else:
        a+= _a
    if a<0: a+= 2.*pi;
    return a
def isnumeric(n):               #   check for numeric
    x = False
    if isinstance(n,int) or isinstance(n,float):
        if n==None or isnan(n) or isinf(n):
            pass
        else:
            x = True
    return x
def equal(a,b):                 #   approximation
    x = False
    if isnumeric(a) and isnumeric(b):
        x = ( abs(a-b) < EQUALITY )
    elif isinstance(a,Point) and isinstance(b,Point):
        x = a.equal(b)
    elif isinstance(a,Segment) and isinstance(b,Segment):
        x = a.equal(b)
    elif isinstance(a,Line) and isinstance(b,Line):
        x = a.equal(b)
    elif isinstance(a,Circle) and isinstance(b,Circle):
        x = a.equal(b)
    elif isinstance(a,Ray) and isinstance(b,Ray):
        x = a.equal(b)
    return x
def iszero(a):                  #   approximation
    if isnumeric(a):
        return equal(a,0)
    else:
        return False
def isnotzero(a):               #   approximation
    if isnumeric(a):
        return not iszero(a)
    else:
        return False
def swap(*args):                #   swap in a list-tuple: swap(list,p1,p2)
    if len(args)==3 and isinstance(args[0],list) and isinstance(args[1],int) and isinstance(args[2],int) and 0<=args[1]<len(args[0]) and 0<=args[2]<len(args[0]):
        i = args[1]
        j = args[2]
        args[0][i],args[0][j]=args[0][j],args[i]
    elif len(args)==5 and isinstance(args[0],list) and isinstance(args[0][0],list) and isinstance(args[1],int) and isinstance(args[2],int) and 0<=args[1]<len(args[0]) and 0<=args[2]<len(args[0][0]) and isinstance(args[3],int) and isinstance(args[4],int) and 0<=args[3]<len(args[0]) and 0<=args[4]<len(args[0][0]):
        i1 = args[1]
        j1 = args[2]
        i2 = args[3]
        j2 = args[4]
        args[0][i1][j1],args[0][i2][j2]=args[0][i2][j2],args[0][i1][j1]
def last(*args):                #   last index of a list-tuple
    x = -1
    if len(args)>=1 and isinstance(args[0],(list, tuple)):
        x = len(args[0])-1
    return x
def decimals(n):                #   number of decimals in a number
    r=0
    if isinstance(n,int) or isinstance(n,float):
        if abs(n) > EPSILON:
            z=str(abs(n))
            x=z.find('.')
            if x>=0:
                r= len(z)-1-x
    return r
def expand(tupl):               #   extracts only numeric items from a tuple
    x = ()
    for z in tupl:
        if isnumeric(z):
            x = x + (z,)
    return x

class Geometric(object):        # ---------------------------- ALL THE SHAPES
    outline = None
    fill = None
    thickness = None
    pointThickness = 3
    zIndex = ()
    z = None
    onTheScreen = False
    bbox = None
    def length(self):
        return float('inf')
    def onscreen(self):
        return self.onTheScreen
    def draw(self,*args):
        if len(args)>=1:
            if isinstance(args[0],Designer):            #   Designer must be first
                if (len(args)==1):
                    args[0].draw(self)                  #   Possible further arguments: outline-color, thickness [, fill-color]
                elif (len(args)==2):
                    args[0].draw(self,args[1])
                elif (len(args)==3):
                    args[0].draw(self,args[1],args[2])
                if (len(args)>=4):
                    args[0].draw(self,args[1],args[2],args[3])
    def near(self,*args):
        actual = None
        d = EQUALITY
        if len(args)>=1:
            if isinstance(args[0],Geometric):
                actual = self.distance(args[0])
                if len(args)>=2 and isnumeric(args[1]):
                    d = args[1]
            elif isnumeric(args[0]):
                d = args[0]
                if len(args)>=2 and isinstance(args[1],Geometric):
                    actual = self.distance(args[1])
        return actual<=d
    def on(self,*args):
        x = False
        if len(args)>=1:
            if isinstance(args[0],Geometric):
                if isinstance(args[0],Function):        #   "Function" contains 2 cases (Point-Segment)
                    x = args[0].on(self)
                elif iszero(self.distance(args[0])):    #   The case is determined by the "distance" methods
                    x = True
        return x
    def clicked(self,*args):
        x = False
        if isinstance(self.zIndex,tuple) and len(self.zIndex)>0 and isinstance(self.zIndex[0],Designer):
            if self.zIndex[0].click and self.onscreen():
                if isinstance(self,Image):
                    x = self.on(self.zIndex[0].mouse)   #   Special "on" for Image/Text
                elif isinstance(self,Point):
                    p = self.zIndex[0].mouse            #   
                    self.l = self.bbox[0]
                    self.t = self.bbox[1]
                    self.r = self.bbox[2]
                    self.b = self.bbox[3]
                    x = self.l <= p.x <= self.r and self.b <= p.y <= self.t
                elif isinstance(self,Rectangle):
                    x = self.inside(self.zIndex[0].mouse)
                elif isinstance(self,Ring):
                    x = abs( self.c.distance(self.zIndex[0].mouse) - self.r ) < self.zIndex[0].tolerance * self.zIndex[0].pixel
                else:
                    x = self.distance(self.zIndex[0].mouse) < self.zIndex[0].tolerance * self.zIndex[0].pixel
        return x
    def off(self,*args):
        x = False
        if len(args)>=1 and isinstance(args[0],Geometric):
            x = not self.on(args[0])
        return x
    def copy(self,other):
        if isinstance(self,Point) and isinstance(other,Point):
            self.x = other.x
            self.y = other.y
            if isinstance(self,Image) and isinstance(other,Image):
                self.label = other.label
        if isinstance(self,Segment) and isinstance(other,Segment):
            self.a.x = other.a.x
            self.a.y = other.a.y
            self.b.x = other.b.x
            self.b.y = other.b.y
        if isinstance(self,Line) and isinstance(other,Line):
            self.a = other.a
            self.b = other.b
            self.c = other.c
        if isinstance(self,Circle) and isinstance(other,Circle):
            self.c.x = other.c.x
            self.c.y = other.c.y
            self.r = other.r
        if isinstance(self,Ray) and isinstance(other,Ray):
            self.v.x = other.v.x
            self.v.y = other.v.y
            self.a = other.r
        if isinstance(self,Rectangle) and isinstance(other,Rectangle):
            self.l = other.l
            self.t = other.t
            self.r = other.r
            self.b = other.b
        if isinstance(self,Function) and isinstance(other,Function):
            self.f = other.f
        if isinstance(self,Polynomial) and isinstance(other,Polynomial):
            self.x = deepcopy(other.x)
        if isinstance(self,Rational) and isinstance(other,Rational):
            self.numerator = deepcopy(other.numerator)
            self.denominator = deepcopy(other.denominator)
    def clone(self,other):
        return deepcopy(self)
#        b = inspect.getmembers(self)
#        c = inspect.getmembers(self, predicate=inspect.ismethod)
#        for x in b:
#            if x[0][0]!= '_' and x not in c:
#                eval('new.'+x[0]+'=self.'+x[0])
#        return new

    '''
    def go_works(self,*args):                                 #   Move anything except "Function"
        if not isinstance(self,Function) and len(self.zIndex)>1:
            d = self.zIndex[0]                      #   This is the designer
            if isinstance(d,Designer):
                dx = dy = 0
                if len(args)>=1 and isinstance(args[0],Point):
                    #self.goThere(d,args[0].x,args[0].y)
                    xx,yy = args[0].x,args[0].y
                elif len(args)>=2 and isnumeric(args[0]) and isnumeric(args[1]):
                    #self.goThere(d,float(args[0]),float(args[1]))
                    xx,yy = float(args[0]),float(args[1])
                nx,ny = self.adjust(d,xx,yy,0)                     #   Change coordinates
                for z in self.zIndex[1:]:
                     d.screen.move(z,nx,ny)


    def goThere(self,d,xx,yy):
        nx,ny = self.adjust(d,xx,yy,0)                     #   Change coordinates
        for z in self.zIndex[1:]:
             d.screen.move(z,nx,ny)
    '''
    """
    def go(self,*args):                                 #   Move anything except "Function"
        if not isinstance(self,Function) and len(self.zIndex)>1:
            d = self.zIndex[0]
            if isinstance(d,Designer):
                if len(args)>=1:
                    dx = dy = 0
                    if isinstance(args[0],Point):
                        dx = args[0].x
                        dy = args[0].y
                    elif isnumeric(args[0]):
                        dx = float(args[0])
                        if len(args)>=2 and isnumeric(args[1]):
                                dy = float(args[1])
                dx,dy = self.adjust(d,dx,dy,0)          #   Change coordinates
                for o in self.zIndex[1:]:
                     d.screen.move(o,dx,dy)
    def move(self,*args):                               #   Move relatively
        if not isinstance(self,Function) and len(self.zIndex)>1:
            d = self.zIndex[0]
            if isinstance(d,Designer):
                if len(args)>=1:
                    dx = dy = 0
                    if isinstance(args[0],Point):
                        dx = args[0].x
                        dy = args[0].y
                    elif isnumeric(args[0]):
                        dx = float(args[0])
                        if len(args)>=2 and isnumeric(args[1]):
                                dy = float(args[1])
                    dx,dy = self.adjust(d,dx,dy,1)      #   Change coordinates
                    for o in self.zIndex[1:]:
                        d.screen.move(o,dx,dy)
    """
    def project(self,*args):                        #   Move anything except "Function"
        if len(self.zIndex)>=1 and len(args)>=2:
            if isnumeric(args[0]) and isnumeric(args[1]) and isnumeric(args[2]):
                self.project(Point(args[0],args[1]),args[2])
            if isinstance(args[0],Point) and isnumeric(args[1]) or isnumeric(args[0]) and isinstance(args[1],Point):
                p = Point(self)
                q = p.projection(args[0],args[1])
                self.go(q)
    def go(self,*args):                             #   Move anything except "Function"
        self.z = 0
        self.movement(*args)
        #self.redraw() # NO NEED 2017/12/18
    def move(self,*args):                           #   Move anything except "Function"
        self.z = 1
        self.movement(*args)
        #self.redraw() # NO NEED 2017/12/18
    def movement(self,*args):
        if self.onscreen() and len(self.zIndex)>=1:
            d = self.zIndex[0]                      #   "d" must be the designer
            if isinstance(d,Designer):
                if len(args)>=1:
                    dx = dy = 0
                    if isinstance(args[0],Point):
                        dx = args[0].x
                        dy = args[0].y
                    elif isnumeric(args[0]):
                        dx = float(args[0])
                        if len(args)>=2 and isnumeric(args[1]):
                            dy = float(args[1])
                    dx,dy,xx,yy = self.adjust(d,dx,dy,self.z)  #   Change coordinates
                    for o in self.zIndex[1:]:                  #   (also of other elements)
                        d.screen.move(o,dx,dy)
                    d.screen.update()
                    if isinstance(self,Point) and self.bbox:   #   adjust real estate
                        self.bbox[0]+= xx
                        self.bbox[2]+= xx
                        self.bbox[1]+= yy
                        self.bbox[3]+= yy
    def redraw(self,*args):
        self.z = 1
        self.drawing(*args)
        self.onTheScreen = True
    def delete(self,*args):
        self.z = 0
        self.drawing(*args)
        self.onTheScreen = False
        if self.bbox:
            self.bbox = None
    def erase(self,*args):
        self.delete(*args)
    def remove(self,*args):
        self.delete(*args)
    def drawing(self,*args):
        if len(self.zIndex)>0:
            d = self.zIndex[0]          #   Do we have a designer ?
            if isinstance(d,Designer):
                for o in self.zIndex[1:]:
                    d.screen.delete(o)
                if self.z:
                    d.draw(self)
                d.update()
    def checkNone(self,args):
        x = False
        if len(args)>=1:
            x = args[0]
            x = x is None or (type(x)==float or type(x)==int) and isnan(x) or issubclass(type(x),Geometric) and x.isnone()
        return x
    def projection(self,*args):
        n = type(self).__name__
        x = n.find('.')
        writeln('cannot project a',n[x+1:])
        return None

#------------------------ CLASS DESIGNER -----------------------#

class Designer():
    defaultviewport = (400,400)
    screen = None                       #   Defined with calibration
    bgcolor = "WHITE"
    fgcolor = "BLACK"
    l = 0; t = 0; r = 0; b = 0          #   world boundaries
    w = 0; h = 0                        #   world dimensions
    width = 0; height = 0               #   viewport dimensions
    xOr = 1; yOr = 1                    #   orientation of axes
    x1=0; y1=0                          #   pixels for one world unit
    px=0; py=0; pixel=0                 #   world dimensions of 1 pixel
    thickness = 1                       #   default line thickness
    fontname = 'Consolas'               #   font characteristics (?)
    fontsize = 0
    axisLabels = True                   #   only for axes
    axisFontSize = 10
    CONTINUE = False                    #   for animations
    forced = False                      #   check forced exit from event loop
    greeting = False                    #   final message
    tolerance = 5                       #   screen distance for clicking on a shape
    dt = 0.1                            #   default chronon value
    '''
        # of arguments passed to the constructor

        0 default viewport 400x400
        2 viewport only
        4 default + world: calibrate
        6 viewport + world: calibrate
    '''
    def __init__(self, *args, **kwargs):
        self.width = self.defaultviewport[0]
        self.height = self.defaultviewport[1]
        if len(args) < 1:               #   no arguments - default
            self.l = self.t = 0
            self.r = self.width - 1
            self.b = self.height - 1
            self.dimensions(self.width,self.height,self.l,self.t,self.r,self.b)
        elif len(args) == 1:            #   1 argument - square viewport
            try:
                n = int(args[0]);
                self.width = self.height = n
            except:
                pass
        elif len(args) == 2:            #   2 arguments - viewport only
            try:
                self.width = int(args[0])
                try:
                    self.height = int(args[1])
                except:
                    self.height = self.width
            except:
                self.height = int(args[1])
                try:
                    self.width = int(args[0])
                except:
                    self.width = self.height
                pass
        elif len(args) == 4:            #   4 arguments - world (default viewport)
            try:
                self.l = float(args[0])
                self.t = float(args[1])
                self.r = float(args[2])
                self.b = float(args[3])
            except:
                self.l = self.t = self.r = self.b = 0
            self.width = self.defaultviewport[0]
            self.height = self.defaultviewport[1]
            self.dimensions(self.width,self.height,self.l,self.t,self.r,self.b)
        elif len(args) == 6:            #   6 arguments - viewport + world
            try:
                self.width = int(args[0])
                self.height = int(args[1])
                self.l = float(args[2])
                self.t = float(args[3])
                self.r = float(args[4])
                self.b = float(args[5])
            except:
                self.width = self.defaultviewport[0]
                self.height = self.defaultviewport[1]
                self.l = self.t = self.r = self.b = 0
            self.dimensions(self.width,self.height,self.l,self.t,self.r,self.b)
        self.screen.focus_set()
    def dimensions(self,_w,_h,_l=0,_t=0,_r=0,_b=0):
        try:
            self.width = _w
            self.height = _h
        except:
            self.width = self.defaultviewport[0]
            self.height = self.defaultviewport[1]
        self.world(_l,_t,_r,_b)
        self.calibrate(self.l,self.t,self.r,self.b)
    def world(self,_l=0,_t=0,_r=0,_b=0):
        try:
            self.l=float(_l); self.t=float(_t); self.r=float(_r); self.b=float(_b);
        except:
            self.l = 0; self.t = 0; self.r = 0; self.b = 0
    def clear(self,c=None):             #   Clear viewport (with color)
        if not self.screen: return
        if c!= None and iscolor(c):
            self.bgcolor = c
            self.screen.config(bg=marioColor(self.bgcolor))
        self.screen.delete("all")
#       self.show()
    def calibrate(self,_l=0,_t=0,_r=0,_b=0):
        if self.screen == None:
            self.window = Tk()
            self.window.title('marioGraphics')   
            self.screen = Canvas(self.window,borderwidth=0,highlightthickness=0,relief="ridge",highlightcolor="yellow")
            self.screen.pack(expand=True,fill=BOTH)
            self.screen.bind('<ButtonRelease-1>', self.release1)
            self.screen.bind('<ButtonRelease-2>', self.release2)
            self.screen.bind('<ButtonRelease-3>', self.release3)
            self.screen.bind('<Button-1>', self.click1)
            self.screen.bind('<Button-2>', self.click2)
            self.screen.bind('<Button-3>', self.click3)
            self.screen.bind('<Key>', self.key)
            self.screen.bind('<Enter>', self.onfocus)
            self.screen.bind('<Leave>', self.onblur)
            self.screen.bind('<Motion>', self.motion)
            self.screen.bind('<Escape>', self.escape)
            self.screen.bind('<MouseWheel>', self.wheel_Windows)
            self.screen.bind('<Button-4>', self.wheel_Linux)
            self.screen.bind('<Button-5>', self.wheel_Linux)
#       writeln(list(self.screen.bind()))
        self.window.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.screen.config(bg=marioColor(self.bgcolor),width=self.width,height=self.height)
        self.show()

        self.xOr = self.yOr = 1
        if _l > _r:
            (_l,_r) = (_r,_l)
            self.xOr = -1                                                   #   orientation
        if _b > _t:
            (_b,_t) = (_t,_b)
            self.yOr = -1
        self.l=_l; self.t=_t; self.r=_r; self.b=_b;
        self.w = float(abs( self.r - self.l))                               #   world
        self.h = float(abs( self.t - self.b))
        if self.width != 0 and self.height != 0:                            #   w-h: world; width-height: screen
            self.px = self.w / (self.width-1)
            self.py = self.h / (self.height-1)                              #   All these quantities had SIGNS
            self.pixel = ( self.px ** 2 + self.py ** 2 ) ** 0.5
            self.pixel = ( self.px + self.py ) / 2
        else:
            self.px = self.py = self.pixel = float('nan')
        if not equal(self.px,0): self.x1 = 1. / float(self.px)
        if not equal(self.py,0): self.y1 = 1. / float(self.py)
        self.xMin = float(min(self.l,self.r))
        self.xMax = float(max(self.l,self.r))
        self.yMin = float(min(self.t,self.b))
        self.yMax = float(max(self.t,self.b))
        self.xMed = (self.xMin+self.xMax) / 2
        self.yMed = (self.yMin+self.yMax) / 2
        #self.tick(0.)
        self.start()    #   2018/01/17

#   how to set up user input
##        v = StringVar()
##        e = Entry(self.window, textvariable=v)
##        e.pack()
##        f = Button(self.window, text='schisa', command=test)
##        f.pack()
##
##        v.set("a default value")
##        s = v.get()
##        p_rint(s)
#   how to put the graphic window on top (not suggested)
##        w = self.window
##        w.iconify()
##        w.update()
##        w.deiconify()

    def text(self,*args):
        if self.screen:
            t = Text(*args)
            self.draw(t)
    def locateMouse(self):
        x = self.window.winfo_pointerx() - self.window.winfo_rootx()
        y = self.window.winfo_pointery() - self.window.winfo_rooty()
        self.mouse = Point( self.wx(x),self.wy(y))
    def on_closing(self):
        #if messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.CONTINUE = False
    def motion(self,event=None):
        self.move = event.x,event.y
        self.mouseMove = event.x,event.y
        self.mouse = Point( self.wx(event.x),self.wy(event.y))
    def wheel_Windows(self,event=None):
        self.updateWheel(event)
        if abs(event.delta)>100:
            self.delta = event.delta // 120     #   for Windows
    def wheel_Linux(self,event=None):
        self.updateWheel(event)
        self.delta = 1 if event.num == 5 else -1
    def updateWheel(self,event=None):
        self.wheel = event.x,event.y
        self.mouse = Point( self.wx(event.x),self.wy(event.y))
    def key(self,event=None):
        self.key = event.keysym
    def release1(self,event=None):
        self.release = event.x,event.y
        self.mouse = Point( self.wx(event.x),self.wy(event.y))
    def release2(self,event=None):
        self.releaseMiddle = event.x,event.y
        self.mouse = Point( self.wx(event.x),self.wy(event.y))
    def release3(self,event=None):
        self.releaseRight = event.x,event.y
        self.mouse = Point( self.wx(event.x),self.wy(event.y))
    def click1(self,event=None):
        self.click = event.x,event.y
        self.mouse = Point( self.wx(event.x),self.wy(event.y))
    def click2(self,event=None):
        self.middleClick = event.x,event.y
        self.mouse = Point( self.wx(event.x),self.wy(event.y))
    def click3(self,event=None):
        self.rightClick = event.x,event.y
        self.mouse = Point( self.wx(event.x),self.wy(event.y))
    def onfocus(self,event):
        self.enter = event.x,event.y
        self.mouse = Point( self.wx(event.x),self.wy(event.y))
    def onblur(self,event):
        self.leave = event.x,event.y
        self.mouse = Point( self.wx(event.x),self.wy(event.y))
    def tick(self,t=-87.87):
        if not self.dead():
            if t==-87.87:
                t = self.dt
            self.key = self.click = self.middleClick = self.rightClick = self.move = self.mouse = self.enter = self.leave = self.wheel = self.delta = self.release = self.releaseMiddle = self.releaseRight = self.mouseMove = None
            sleep(t)
            if self.screen:             #   2018/08/30
                self.screen.update()
            if t!=self.dt:
                self.dt=t
    def __del__(self):
        if not self.greeting:
            self.happyTrails()          #   2017/11/30
    def happyTrails(self):
        self.greeting = True
        write('ta-ra'); lf()
    def destroy(self):
        self.window.destroy()
        self.happyTrails()
    def alive(self):
        return self.CONTINUE
    def dead(self):
        return ( not self.alive() )
    def start(self,time=0.):
        self.screen.focus_force()
        self.screen.focus_set()
        self.CONTINUE = True
        self.tick(0.)
        if time>0:
            sleep(time)
    def escape(self,time=0.):             #   exit with esc or close
        self.CONTINUE = False
        self.forced = False
    def stop(self,t=0.):                #   forced exit
        self.CONTINUE = False
        self.forced = True
    def terminated(self,*args):
        return self.dead() and self.forced
    def closed(self,*args):
        return self.dead() and not self.forced
    def show(self):
        if self.screen:
            self.screen.update()
    def update(self):
        if self.screen:
            self.screen.update()
    def x(self,xx):                     #   screen coordinates (from world)
        if not self.screen or isnan(xx) or isnan(self.width) or equal(self.w,0.): return None
        if self.width<1: return None
        z1 = round( ( xx - self.l ) * (self.width-1) / self.w )
        z2 = int(z1)
        if self.xOr > 0:
            return z2
        else:
            return self.width - z2
    def y(self,yy):
        if not self.screen or isnan(yy) or isnan(self.height) or equal(self.h,0.): return None
        if self.height<1: return None
        z1 = round( ( self.t - yy ) * (self.height-1) / self.h )
        z2 = int(z1)
        if self.yOr > 0:
            return z2
        else:
            return self.height - z2
    def wx(self,xx):                    #   world coordinates (from screen)
        if not self.screen or isnan(xx) or isnan(self.width): return None
        if self.width<1: return None
        if self.xOr > 0:
            z2 = float(self.l + self.px * xx)
        else:
            z2 = float(self.r - self.px * xx)
        return z2
    def wy(self,yy):
        if not self.screen or isnan(yy) or isnan(self.height): return None
        if self.height<1: return None
        if self.yOr > 0:
            return float(self.t - self.py * yy)
        else:
            return float(self.b + self.py * yy)
    def dx(self,d):                     #   Distances in pixels: always POSITIVE
        if not self.screen or isnan(d) or equal(self.px,0.): return float('nan')
        return int(round(abs(d/self.px)))
    def dy(self,d):
        if not self.screen or isnan(d) or equal(self.py,0.): return float('nan')
        return int(round(abs(d/self.py)))
    def labels(self,x=True):
        if isinstance(x,bool):
            self.axisLabels = x
    def axes(self,scaleX=1,scaleY=-878787.878787):
        self.xAxis(scaleX)
        if scaleY==-878787.878787: scaleY = scaleX                          #   1 argument: same scale
        self.yAxis(scaleY)
    def xAxis(self,scale=1):                                                #   drawing the axes
        if not self.screen: return None
        xWall = 0
        zero = self.y(0)
        if self.t < 0 and self.yOr == 1 or self.b > 0 and self.yOr == -1:   #   On a wall?
            xWall = 1                                                       #   upper
        if self.b > 0 and self.yOr == 1 or self.t < 0 and self.yOr == -1:   #   On a wall?
            xWall = 2                                                       #   lower
        if not xWall:
            if equal(scale,0) or scale < 0 and 15 < zero < self.height - 5 or scale > 0 and 5 < zero < self.height - 15:
                if self.xOr > 0:
                    self.screen.create_line(5,zero,self.width-15,zero,width=1,fill=marioColor(self.fgcolor))
                    self.screen.create_polygon(self.width-15,zero-5,self.width-15,zero+5,self.width-5,zero,fill=marioColor(self.fgcolor))
                else:
                    self.screen.create_line(15,zero,self.width-5,zero,width=1,fill=marioColor(self.fgcolor))
                    self.screen.create_polygon(15,zero-5,15,zero+5,5,zero,fill=marioColor(self.fgcolor))
        if not iszero(scale): self.xNotches(scale,xWall)
    def yAxis(self,scale=1):
        if not self.screen: return None
        yWall = 0
        zero = self.x(0)
        if self.l > 0 and self.xOr == 1 or self.r < 0 and self.xOr == -1:
            yWall = 1                                                       #   left wall
        if self.r < 0 and self.xOr == 1 or self.l > 0 and self.xOr == -1:
            yWall = 2                                                       #   right wall
        if not yWall:
            if equal(scale,0) or scale < 0 and 15 < zero < self.width - 5 or scale > 0 and 5 < zero < self.width - 15:
                if self.yOr > 0:
                    self.screen.create_line(zero,15,zero,self.height-5,width=1,fill=marioColor(self.fgcolor))
                    self.screen.create_polygon(zero-5,15,zero,5,zero+5,15,fill=marioColor(self.fgcolor))
                else:
                    self.screen.create_line(zero,5,zero,self.height-15,width=1,fill=marioColor(self.fgcolor))
                    self.screen.create_polygon(zero-5,self.height-15,zero,self.height-5,zero+5,self.height-15,fill=marioColor(self.fgcolor))
        if not iszero(scale): self.yNotches(scale,yWall)
    def xNotches(self,scale,xWall):
        '''
            The axis starts at the 5th pixel, so the first feasible "x" is at the 6th pixel,
            with as many decimals as specified in the scale

            px (property): world width corresponding to 1 pixel, multiplied by 6
            aggiunta al margine sinistro, per ottenere la coordinata del 6. pixel

            Example: "x" of 6th pixel = -3.426; scale = 0.01
            ceil( x * 100 ) / 100 disposes of the decimals beyond the 2nd (starting from 3.42)
        '''
        if scale > 0:                       #   Position relative to x-axis
            under = True                    #   > 0: above (default)
        else:
            under = False                   #   < 0: below
            scale = - scale
        digits = decimals(scale);           #   Number of decimals for label
        if digits<1: digits = 0             #   By default, use units
        zero = self.y(0)                    #   vertical position of origin
        if xWall == 1:                      #   possible position on either wall
            zero = 0;
        elif xWall == 2:
            zero = self.height

        start = min( self.l,self.r)
        start = start + abs( self.px) * 6   #   first feasible point
        _x = ceil( start / scale ) * scale  #   (rounded to the scale decimals)
        '''
            Looking for a feasible distance between notches (at least 10 pixels);
            last possible scale: thousands
        '''
        while self.dx( scale) < 10 and scale < 1000:
            digits-=1
            scale*= 10
            _x = ceil( start / scale ) * scale
        if digits<0:
            digits=0
        '''
            Notches and corrisponding labels
        '''
        if self.dx( scale) >= 10:           #   "acceptable" scale
            if xWall==1:
                position = 6                #   upper wall
                a = 'n'
            elif xWall==2:
                position = self.height - 6  #   lower wall
                a = 's'
            elif under:
                a = 'n'
            else:
                a = 's'
            ff = "{0:."+str(digits)+"f}"    #   format string
            end = max( self.l,self.r)
            if (xWall):
                end = end - 6 * abs(self.px)
            else:
                end = end - 17 * abs(self.px)

            while _x < end:                 #   up to the arrow (if it exists)
                '''
                    The notch is skipped if the position corresponds to the y-axis
                    or if the y-axis is not visible
                '''
                if abs(_x) > 0.00001:
                    notch = self.x(_x)      #   Positione of notch
                    self.screen.create_line(notch,zero-4,notch,zero+4,width=1,fill=marioColor(self.fgcolor))
                    if self.axisLabels:
                        z = (ff.format(round(_x,digits)))
                        if not xWall:
                            if under:
                                position = zero + 4
                            else:
                                position = zero - 4
                        text = self.screen.create_text(notch,position,font=(self.fontname,self.axisFontSize),text=z,anchor=a,fill=marioColor(self.fgcolor))
                _x+= scale                  #   next notch (scale is positive anyway)
    def yNotches(self,scale,yWall):
        if ( scale > 0 ):                   #   Position with respect to the axis
            left = True                     #   > 0: to the left (default)
        else:
            left = False                    #   < 0: to the right
            scale = - scale
        digits = decimals(scale)
        if ( digits < 1 ): digits = 0
        zero = self.x(0)
        if ( yWall == 1):
            zero = 0
        elif ( yWall == 2):
            zero = self.width

        start = min( self.t,self.b)
        start = start + abs(self.py) * 6
        _y = ceil( start / scale ) * scale
        while ( self.dy( scale) < 10 and scale < 1000 ):
            digits-=1
            scale*= 10
            _y = ceil( start / scale ) * scale
        if digits<0:
            digits=0
        if ( self.dy( scale) >= 10 ):
            if (yWall==1):
                position = 10               #   Position of label
                a = 'w'
            elif (yWall==2):
                position = self.width - 7
                a = 'e'
            elif left:
                a = 'e'
            else:
                a = 'w'
            ff = "{0:."+str(digits)+"f}"
            end = max( self.t,self.b)
            if ( yWall ):
                end = end - 6 * self.py
            else:
                end = end - 17 * self.py
            while ( _y < end ):
                if ( abs(_y) > 0.00001 ):
                    notch = self.y(_y)                  #   Position of notch
                    self.screen.create_line(zero-4,notch,zero+4,notch,width=1,fill=marioColor(self.fgcolor))
                    if self.axisLabels:
                        z = (ff.format(round(_y,digits)))
                        if not yWall:
                            if left:
                                position = zero - 7
                            else:
                                position = zero + 7
                        text = self.screen.create_text(position,notch,font=(self.fontname,self.axisFontSize),text=z,anchor=a,fill=marioColor(self.fgcolor))
                _y+= scale;                             #   next notch (world)
    def wait(self,n=0):                                 #   wait (timed)
        if not self.screen:  return
        if not isnumeric(n): n=0.
        self.tick(n)
    def sleep(self,n=0.):                               #   wait (timed)
        self.wait(n)
    def rest(self,n=0.):                                #   wait (timed)
        self.wait(n)
    def freeze(self):                                   #   wait for Esc keypress
        if not self.screen: return
        writeln('freezing')
        self.start()
        while self.alive():
            self.show()
            self.tick(0.01)
    def thick(self,x):                                  #   check thickness
        if x <= 0:                                      #   2017/11/14
            t = 1
        else:
            t = x
        return t
    def background(self,*args):                         #   colors
        if len(args)==1 and iscolor(args[0]):
            self.bgcolor = args[0]
        elif len(args)>=3:
            c = (args[0],args[1],args[2])
            if iscolor(c):
                self.bgcolor = c
        self.screen.config(bg=marioColor(self.bgcolor))
    def foreground(self,*args):                         #   colors
        if len(args)==1 and iscolor(args[0]):
            self.fgcolor = args[0]
        elif len(args)>=3:
            c = (args[0],args[1],args[2])
            if iscolor(c):
                self.fgcolor = c
#       self.screen.config(highlightcolor=marioColor(self.fgcolor))
    def draw(self,*args):                               #   CONDITIONS FOR DRAWING
        if not self.screen: return                      #   screen must exist
        if len(args)==0: return                         #   argument must exist
        if not isinstance(args[0],Geometric): return    #   must be geometric
        o = args[0]
        if o.isnone(): return                           #   must have properties
        layer = ()
        newfontsize = -1
        newfontname = ''

        if len(args) >= 2:                              #   managing color and thickness (was ==2 and ==3)
            if isnumeric(args[1]):
                o.thickness = int(args[1])
                newfontsize = o.thickness
            elif iscolor(args[1]):
                if isinstance(o,Pixel):
                    o.fill = o.outline = args[1]        #   2017/11/28
                else:
                    o.outline = args[1]
        if len(args) >= 3:
            if iscolor(args[2]) and isnumeric(args[1]):
                o.outline = args[2]
                o.thickness = int(args[1])
                newfontsize = o.thickness
            elif iscolor(args[1]) and isnumeric(args[2]):
                o.outline = args[1]
                o.thickness = int(args[2])
                newfontsize = o.thickness
            elif iscolor(args[1]) and iscolor(args[2]):
                o.outline = args[1]
                o.fill = args[2]
            if isinstance(o,Text) and isnumeric(args[1]):
                newfontsize = o.thickness = int(args[1])
            if isinstance(o,Text) and isnumeric(args[2]):
                newfontsize = o.thickness = int(args[2])
            if isinstance(o,Text) and isinstance(args[1],str):
                newfontname = args[1]
            if isinstance(o,Text) and isinstance(args[2],str):
                newfontname = args[2]
        if len(args) >= 4:                              #   for full shapes (disk-rectangle)
            if isnumeric(args[1]) and iscolor(args[2]) and iscolor(args[3]):
                o.thickness = int(args[1])
                newfontsize = o.thickness
                o.outline = args[2]
                o.fill = args[3]
            elif iscolor(args[1]) and isnumeric(args[2]) and iscolor(args[3]):
                o.outline = args[1]
                o.thickness = int(args[2])
                newfontsize = o.thickness
                o.fill = args[3]
            elif iscolor(args[1]) and iscolor(args[2]) and isnumeric(args[3]):
                o.outline = args[1]
                o.fill = args[2]
                o.thickness = int(args[3])
                newfontsize = o.thickness
        if isinstance(o,Text):
            for i in range(1,len(args)):
                if isinstance(args[i],str):
                    newfontname = args[i]
                if isnumeric(args[i]):
                    newfontsize = args[i]
                if iscolor(args[i]):
                    o.outline = args[i]

        if newfontsize >= 0:                    #   2017/11/28 set point thickness for Segment/Circle/Ray
            o.pointThickness = newfontsize

        if isinstance(o,Point) or isinstance(o,Segment) or isinstance(o,Line) or isinstance(o,Ray) or isinstance(o,Function):
            if o.fill != None and o.outline == None:
                o.outline = o.fill
            elif o.fill == None and o.outline != None:
                o.fill = o.outline

        if o.thickness == None: o.thickness = self.thickness        #   from the Designer object
        if o.outline == None: o.outline = self.fgcolor
        if o.fill == None: o.fill = ( self.fgcolor if isinstance(o,Text) or isinstance(o,Segment) else self.bgcolor )
        if o.thickness < 0: o.thickness = 0
        if isinstance(o,Pixel):
            if o.thickness >= 1:                #   2017/11/14
                o.thickness = 1                 #   big pixel
            else:
                o.thickness = 0                 #   single pixel (thickness 1, actually)

        try:
            if isinstance(o,Image) or isinstance(o,Text):
                o.anchor = o.anchor.lower()
            if isinstance(o,Text):
                if newfontsize>0 and newfontsize != o.fontsize or newfontname!='' and newfontname != o.fontname:
                    o.newfont(newfontsize,newfontname)
                if o.fontsize != o.thickness:
                    o.thickness = o.fontsize
                if o.overwrite and len( o.zIndex)>1:
                    try:
                        self.screen.delete( o.zIndex[1])
                    except:
                        pass
                o.zIndex = (self, self.screen.create_text(self.x(o.x),self.y(o.y),text=o.label,font=(o.fontname,o.fontsize),fill=marioColor(o.fill),anchor=o.anchor) ,)
                '''
                    Determine the world region
                '''
                bbox = self.screen.bbox(o.zIndex[1])
                o.bbox = [self.wx(bbox[0]),self.wy(bbox[1]),self.wx(bbox[2]),self.wy(bbox[3])]
            elif isinstance(o,Image):           #   if: with image or empty
                if o.image:
                    o.zIndex = (self, self.screen.create_image(self.x(o.x),self.y(o.y),image=o.image,anchor=o.anchor) ,)
                else:
                    hw = o.width/2              #   no image: create gray rectangle
                    hh = o.height/2
                    if o.anchor in ('c','n','s'):
                        xLeft   = self.x(o.x) - hw
                        xRight  = self.x(o.x) + hw
                    elif o.anchor in ('e','ne','se'):
                        xLeft   = self.x(o.x) - o.width
                        xRight  = self.x(o.x)
                    else:
                        xLeft   = self.x(o.x)
                        xRight  = self.x(o.x) + o.width
                    if o.anchor in ('c','w','e'):
                        yTop    = self.y(o.y) - hh
                        yBottom = self.y(o.y) + hh
                    elif o.anchor in ('n','nw','ne'):
                        yTop    = self.y(o.y)
                        yBottom = self.y(o.y) + o.height
                    else:
                        yTop    = self.y(o.y) - o.height
                        yBottom = self.y(o.y)

                    o.zIndex = (self, self.screen.create_rectangle(xLeft,yTop,xRight,yBottom,outline=marioColor(LIGHTGREY),fill=marioColor(GREY),width=3) ,)
                '''
                    Determine the world region
                '''
                bbox = self.screen.bbox(o.zIndex[1])
                o.bbox = [self.wx(bbox[0]),self.wy(bbox[1]),self.wx(bbox[2]),self.wy(bbox[3])]
            elif isinstance(o,Point):
                if o.thickness < 1:             #   at least 1 pixel; this also works for regular PIXEL shapes
                    o.zIndex = (self, self.screen.create_line(self.x(o.x),self.y(o.y),self.x(o.x)+1,self.y(o.y)+1,fill=marioColor(o.outline),width=1) ,)
                else:
                    if isinstance(o,Pixel):     #   big pixel 2017/11/14
                        radius = 1
                    else:
                        radius = o.thickness    #   max(3,o.thickness) 2017/11/28
                    o.zIndex = (self, self.screen.create_oval(self.x(o.x)-radius,self.y(o.y)-radius,self.x(o.x)+radius,self.y(o.y)+radius,width=1,outline=marioColor(o.outline),fill=marioColor(o.outline)) ,)
                '''
                    Determine the world region
                '''
                bbox = self.screen.bbox(o.zIndex[1])
                o.bbox = [self.wx(bbox[0]),self.wy(bbox[1]),self.wx(bbox[2]),self.wy(bbox[3])]
            elif ( isinstance(o,Segment) or isinstance(o,Dash)):
                t = self.thick(o.thickness)
                o.zIndex = (self, self.screen.create_line(self.x(o.a.x),self.y(o.a.y),self.x(o.b.x),self.y(o.b.y),fill=marioColor(o.outline),width=t) ,)
                if not isinstance(o,Dash):
                    o.a.thickness = o.thickness
                    o.b.thickness = o.thickness
                    o.a.thickness = o.b.thickness = o.pointThickness    #   2017/11/28
                    o.zIndex+= (self.draw(o.a,o.outline)[1] ,)          #   DRAW POINT
                    o.zIndex+= (self.draw(o.b,o.outline)[1] ,)
            elif ( isinstance(o,Circle) or isinstance(o,Disk) or isinstance(o,Ring) ):
                c = Point(o.c)
                r = o.r
                t = self.thick(o.thickness)
                xLeft = self.x(o.c.x - self.xOr * r)
                yTop = self.y(o.c.y + self.yOr * r)
                xRight = self.x(o.c.x + self.xOr * r)
                yBottom = self.y(o.c.y - self.yOr * r)
                if isinstance(o,Disk):
                    o.zIndex = (self, self.screen.create_oval(xLeft,yTop,xRight,yBottom,width=t,outline=marioColor(o.outline),fill=marioColor(o.fill)) ,)
                else:
                    o.zIndex = (self, self.screen.create_oval(xLeft,yTop,xRight,yBottom,width=t,outline=marioColor(o.outline)) ,)
                    if not isinstance(o,Ring):
                        o.c.thickness = o.thickness                         #   2017/11/28
                        o.c.thickness = o.pointThickness                    #   DRAW POINT
                        if o.pointThickness > 0:                            #   only for Circles: draw the center
                            o.zIndex+= (self.draw(o.c,o.outline,o.c.thickness)[1],)
            elif isinstance(o,Line):
                t = self.thick(o.thickness)
                if ( o.vertical() ):
                    if ( abs(o.a) > EPSILON ):
                        o.zIndex = (self, self.screen.create_line(self.x(-o.c/o.a),self.y(self.t),self.x(-o.c/o.a),self.y(self.b),fill=marioColor(o.outline),width=t) ,)
                    else:
                        pass
                else:
                    if (o.slope()<1):
                        p1 = Point( self.l, o.ordinate(self.l))
                        p2 = Point( self.r, o.ordinate(self.r))
                    else:
                        p1 = Point( o.abscissa(self.b), self.b)
                        p2 = Point( o.abscissa(self.t), self.t)
                    o.zIndex = (self, self.screen.create_line(self.x(p1.x),self.y(p1.y),self.x(p2.x),self.y(p2.y),fill=marioColor(o.outline),width=t) ,)
            elif isinstance(o,Ray):
                if o.thickness<1:
                    t = 1
                else:
                    t = o.thickness
                p1 = o.v
                p2 = o.at(self.w * self.h)
                o.zIndex = (self, self.screen.create_line(self.x(p1.x),self.y(p1.y),self.x(p2.x),self.y(p2.y),fill=marioColor(o.outline),width=t) ,)
                if o.thickness>0:
                    o.v.thickness = o.thickness
                    o.v.thickness = o.pointThickness                        #   2017/11/28
                    o.zIndex+= (self.draw(o.v,o.outline)[1] ,)              #   DRAW POINT
            elif isinstance(o,Frame):
                t = self.thick(o.thickness)
                o.zIndex = (self.screen, self.screen.create_rectangle(self.x(o.l),self.y(o.t),self.x(o.l+o.w),self.y(o.t-o.h),outline=marioColor(o.outline),width=t) ,)
            elif isinstance(o,Rectangle):
                t = self.thick(o.thickness)
                o.zIndex = (self, self.screen.create_rectangle(self.x(o.l),self.y(o.t),self.x(o.l+o.w),self.y(o.t-o.h),outline=marioColor(o.outline),fill=marioColor(o.fill),width=t) ,)
            elif isinstance(o,Function):
                if o.thickness<1:
                    t = 1
                else:
                    t = o.thickness

                o.zIndex = (self.screen,)
                p1 = Point(self.l)
                dx = self.px
                while p1.x<=self.r:
                    p1.y = o.value(p1.x)
                    dx = self.px
                    p2 = Point(p1.x+dx)
                    p2.y = o.value(p2.x)
                    if isnumeric(p1.y) and isnumeric(p2.y) and ( self.b<p1.y<self.t or self.b<p2.y<self.t):
                        o.zIndex+= (self.screen.create_line(self.x(p1.x),self.y(p1.y),self.x(p2.x),self.y(p2.y),fill=marioColor(o.outline),width=t),)
                    p1.x+= dx
            layer = o.zIndex
            o.onTheScreen = True
            self.update()
        except Exception as e:
            write("cannot draW", e); lf()
            write(type(o)); lf()
            o.show()
            o.onTheScreen = False
        return layer

#------------------------ CLASS POINT -----------------------#

class Point(Geometric):
    x = 0.; y = 0.; thickness = 3
    def __init__(self, *args, **kwargs):
        empty = self.checkNone(args)
        if len(args)>=1:
            if empty:
                self.x = float('nan')
                self.y = float('nan')
            elif isinstance(args[0],Point):
                self.x = float(args[0].x)
                self.y = float(args[0].y)
            elif isinstance(args[0],Segment):
                self.x = float(args[0].a.x)
                self.y = float(args[0].a.y)
            elif isinstance(args[0],Circle):
                self.x = float(args[0].c.x)
                self.y = float(args[0].c.y)
            elif isinstance(args[0],Ray):
                self.x = float(args[0].v.x)
                self.y = float(args[0].v.y)
            elif len(args)>=2 and isnumeric(args[0]) and isnumeric(args[1]):
                self.x = float(args[0])
                self.y = float(args[1])
            elif isnumeric(args[0]):
                self.x = float(args[0])
            elif len(args)>=2 and isinstance(args[0],Line) and isinstance(args[1],Line):
                p = args[0].section(args[1])    
                self.x = float(p.x)
                self.y = float(p.y)
            else:
                self.x = float('nan')
                self.y = float('nan')
    def isnone(self):
        return not ( isnumeric(self.x) and isnumeric(self.y))
    def length(self):
        return 0.
    def isempty(self):
        return not ( isnumeric(self.x) and isnumeric(self.y))
    def angle(self,*args):
        a = float('nan')
        if len(args)==1 and isinstance(args[0],Point):
            p = Point(args[0])
            if not equal(self.x,p.x) or not equal(self.y,p.y):
                a = zero_2PI(atan2(p.y-self.y,p.x-self.x))
            else:
                a = 0.
        return a
    def midpoint(self, *args):
        x = Point(None)
        if len(args)>=1:
            if isinstance(args[0],Point):
                x.x = ( self.x + args[0].x ) / 2
                x.y = ( self.y + args[0].y ) / 2
            elif isinstance(args[0],Geometric):
                p = self.projection(args[0])
                if isinstance(p,Point):
                    s = Segment(self,p)
                elif isinstance(p,Segment):
                    p = self.projection(p)
                    s = Segment(self,p)
                else:
                    s = Segment(None)
                if not s.isnone():
                    x = s.midpoint()
        return x
    def ping(self, *args): 
        p = Point(self)
        return p.projection(*args)
    def projection(self, *args):    #   Project towards any shape AT A DISTANCE
        p = Point(self)
        d = 0
        thirdPoint = False
        if len(args)>=2 and isinstance(args[0],Point) and isnumeric(args[1]):
            p = args[0]
            d = args[1]
            thirdPoint = True
        elif len(args)>=2 and isinstance(args[1],Point) and isnumeric(args[0]):
            p = args[1]
            d = args[0]
            thirdPoint = True
        elif len(args)>=1 and isinstance(args[0],Point):
            p = args[0]
        elif len(args)>=2 and isinstance(args[0],Circle) and isnumeric(args[1]):
            p = Circle(args[0]).c
            d = args[1]
            thirdPoint = True
        elif len(args)>=2 and isinstance(args[1],Circle) and isnumeric(args[0]):
            p = Circle(args[1]).c
            d = args[0]
            thirdPoint = True
        elif len(args)>=1 and isinstance(args[0],Circle):
            c = Circle(args[0])
            p = Segment( c.c.projection(self,c.r), c.c.projection(self,-c.r)) 
        elif len(args)>=2 and isinstance(args[0],Line) and isnumeric(args[1]):
            p = self.projection(args[0])
            d = args[1]
            thirdPoint = True
        elif len(args)>=2 and isinstance(args[1],Line) and isnumeric(rgs[0]):
            p = self.projection(args[1])
            d = args[0]
            thirdPoint = True
        elif len(args)>=1 and isinstance(args[0],Line):
            r = self.perpendicular(args[0])
            p = r.section(args[0])       
        elif len(args)>=2 and isinstance(args[0],Ray) and isnumeric(args[1]):
            p = p.projection(args[0])
            d = args[1]
            thirdPoint = True
        elif len(args)>=2 and isinstance(args[1],Ray) and isnumeric(args[0]):
            p = p.projection(args[1])
            d = args[0]
            thirdPoint = True
        elif len(args)>=1 and isinstance(args[0],Ray):
            t = Line(args[0])
            r = self.perpendicular(t)
            p = r.section(t)
            if not p.on(args[0]):
                p = args[0].v
        elif len(args)>=2 and isinstance(args[0],Segment) and isnumeric(args[1]):
            p = p.projection(args[0])
            d = args[1]
            thirdPoint = True
        elif len(args)>=2 and isinstance(args[1],Segment) and isnumeric(args[0]):
            p = p.projection(args[1])
            d = args[0]
            thirdPoint = True
        elif len(args)>=1 and isinstance(args[0],Segment):
            s = Segment(args[0])
            t = Line(s)
            u = self.projection(t)
            if u.on(s):
                p = u
            elif self.distance(s.a) < self.distance(s.b): 
                p = s.a
            else:
                p = s.b
        if thirdPoint:
            if equal(self,p) or equal(d,0):
                _x = self.x
                _y = self.y
            else:
                a = self.angle(p)
                _x = self.x + d * cos(a)
                _y = self.y + d * sin(a)
            p = Point(_x,_y)
        if isinstance(self,Image):
            return Image(self.label,p.x,p.y,self.factor)
        return p
    def distance(self, *args):
        d = float('nan')
        if len(args)>=1 and isinstance(args[0],Point):
            d = pow( pow(self.x-args[0].x,2) + pow(self.y-args[0].y,2), 0.5)
        elif len(args)>=1 and ( isinstance(args[0],Segment) or isinstance(args[0],Line) or isinstance(args[0],Ray)):
            d = self.distance(self.projection(args[0]))
        elif len(args)>=1 and isinstance(args[0],Circle):
            d = self.distance(args[0].c)-args[0].r
        elif len(args)>=1 and isinstance(args[0],Rectangle):
            args[0].box()
            l = args[0].l; t = args[0].t; r = args[0].r; b = args[0].b
            s1 = Segment(l,t,r,t);  s2 = Segment(r,t,r,b);  s3 = Segment(r,b,l,b);  s4 = Segment(l,b,l,t)
            d1 = self.distance(s1); d2 = self.distance(s2); d3 = self.distance(s3); d4 = self.distance(s4)
            d = min( d1,d2,d3,d4)
            if self.internal(args[0])==-1:
                d = -d
        return d
    def section(self,*args):
        r = Line(None)
        if len(args)>=1 and isinstance(args[0],Point):
            r = Line(None)
            p = Point(args[0])
            if self.equal(p):
                r.a = 0
                r.b = 1
                r.c = -p.y
            else:
                r.a = p.y    - self.y
                r.b = self.x - p.x
                r.c = p.x * self.y - self.x * p.y
        elif len(args)>=1 and isinstance(args[0],Segment):
            r = self.section(self.projection(args[0]))
        elif len(args)>=1 and isinstance(args[0],Circle):
            r = self.section(args[0].c)                     
        elif len(args)>=1 and isinstance(args[0],Line):
            r = self.perpendicular(args[0])
        elif len(args)>=1 and isinstance(args[0],Ray):
            r = self.section(self.projection(args[0]))
        return r
    def parallel(self, *args):
        z = Line(None)
        if len(args)>=1 and isinstance(args[0],Point):
            r = self.section(args[0])
            z = self.perpendicular(r)
        elif len(args)>=1 and (isinstance(args[0],Line) or isinstance(args[0],Segment) or isinstance(args[0],Ray) ):
            r = Line(args[0])
            z.a = r.a
            z.b = r.b
            z.c = - r.a * self.x - r.b * self.y
        elif len(args)>=1 and isinstance(args[0],Circle):
            if self.outside(args[0]):
                r = self.section(args[0].c)                     
                z = self.perpendicular(r)
        return z
    def perpendicular(self, *args):
        z = Line(None)
        if len(args)>=1:
            if isinstance(args[0],Point):
                z = self.section(args[0])
            elif isinstance(args[0],Line) or isinstance(args[0],Segment) or isinstance(args[0],Ray):
                r = Line(args[0])
                z.a = -r.b
                z.b = r.a
                z.c = - z.a * self.x - z.b * self.y
            elif isinstance(args[0],Circle):
                z = self.section(args[0],self.c)                
        return z
    def on(self,*args):
        x = False
        if len(args)>=1:
            if isinstance(args[0],Image):
                x = args[0].on(self)
            elif isinstance(args[0],Point):
                x = equal(self.x,args[0].x) and equal(self.y,args[0].y)
            elif isinstance(args[0],Segment):
                x = equal( self.distance(args[0].a) + self.distance(args[0].b), args[0].length())
            elif isinstance(args[0],Circle):
                x = equal( self.distance(args[0].c), args[0].r)
            elif isinstance(args[0],Line):
                x = equal( self.x*args[0].a+self.y*args[0].b+args[0].c, 0)
            elif isinstance(args[0],Ray):
                z = Line(args[0])
                a1 = zero_2PI(args[0].v.angle(self))
                a2 = zero_2PI(args[0].a)
                x = self.on(z) and equal(a1,a2)
            elif isinstance(args[0],Polynomial) or isinstance(args[0],Rational) or isinstance(args[0],Function):
                x = self.x
                y = args[0].value(x)
                p = Point(x,y)
                x = self.equal(p)
        return x
    def inside(self,*args):
        x = float('nan')
        if len(args)==1 and ( isinstance(args[0],Circle) or isinstance(args[0],Rectangle)):
            x = self.internal(args[0]) == -1
        return x
    def outside(self,*args):
        x = float('nan')
        if len(args)==1 and ( isinstance(args[0],Circle) or isinstance(args[0],Rectangle)):
            x = self.internal(args[0]) == 1
        return x
    def internal(self,*args):
        x = float('nan')
        if len(args)==1 and isinstance(args[0],Circle):
            d = self.distance(args[0].c)
            if equal(d, args[0].r):
                x = 0
            elif d < args[0].r:
                x = -1
            else:
                x = 1
        elif len(args)==1 and isinstance(args[0],Rectangle):
            args[0].box()
            l = args[0].l; t = args[0].t; r = args[0].r; b = args[0].b
            if (equal(self.x,l) or equal(self.x,r)) and (b<=self.y<=t) or (equal(self.y,b) or equal(self.y,t)) and (l<=self.x<=r):
                x = 0
            elif l<self.x<r and b<self.y<t:
                x = -1
            else:
                x = 1
        return x
    def external(self,*args):
        x = float('nan')
        if len(args)>=1:
            x = - self.internal(args[0])
        return x
    def where(self,o):
        d = float('nan')
        if ( isinstance(o,Segment) or isinstance(o,Circle) or isinstance(o,Ray) ) and self.on(o):
            if isinstance(o,Segment):
                if self.equal(o.a):
                    d = 0
                elif self.equal(o.b):
                    d = 1
                else:
                    d = self.distance(o.a) / o.length()
            elif isinstance(o,Circle):
                #1 = Segment(o.c,o.c.x+1,o.c.y)
                s2 = Segment(o.c,self)
                d = s2.angle()
            else:
                d = o.v.distance(self)
        return d
    def equal(self, *args):
        x = False
        if len(args)>=1 and isinstance(args[0],Point):
            x = equal(self.x,args[0].x) and equal(self.y,args[0].y)
        return x
    def adjust(self,g,dx,dy,factor):            #   Adjust coordinates before a movement
        old = (g.x(self.x),g.y(self.y))
        old2 = (self.x,self.y)
        self.x = self.x * factor + dx
        self.y = self.y * factor + dy
        old3 = (self.x-old2[0],self.y-old2[1])
        return (g.x(self.x)-old[0],g.y(self.y)-old[1],old3[0],old3[1])
    def show(self):
        write("x,y (%.3f," % self.x, "%.3f)" % self.y); lf()
    def itIsOn(self,*args):
        if len(args)>=1 and isinstance(args[0],Image):
            return args[0].itIsOn(self)

#------------------------ SUBCLASS PIXEL -----------------------#

class Pixel(Point):
    thickness = 0           #   everything else is inherited

#------------------------ SUBCLASS IMAGE -----------------------#

class Image(Point):
    x = 0.
    y = 0.
    factor = 1
    label = ''
    originalLabel = ''
    secondary = ''
    anchor = 'c'             #   Tkinter settings (cardinal directions, plus "C"=center)
    image = None
    size = (41,41)
    def __init__(self, *args, **kwargs):        #   Customized constructor
        empty = self.checkNone(args)
        scale = 0
        if len(args)>=1:
            if empty: #args[0]==None or args[0]==float('nan'):
                self.x = float('nan')
                self.y = float('nan')
                self.label = ''
            elif isinstance(args[0],Image):
                self.x = args[0].x
                self.y = args[0].y
                self.label = args[0].label
            elif isinstance(args[0],str):
                self.label = args[0]
                if len(args)>=2 and isinstance(args[1],Point):
                    self.x = float(args[1].x)
                    self.y = float(args[1].y)
                if len(args)>=2 and isnumeric(args[1]):
                    self.x = float(args[1])
                if len(args)>=3 and isnumeric(args[2]):
                    self.y = float(args[2])
            elif len(args)>=2 and isinstance(args[0],Point) and isinstance(args[1],str):
                self.x = float(args[0].x)
                self.y = float(args[0].y)
                self.label = args[1]
            elif len(args)>=2 and isinstance(args[0],str) and isinstance(args[1],Point):
                self.x = float(args[1].x)
                self.y = float(args[1].y)
                self.label = args[0]
            elif len(args)==2 and isnumeric(args[0]) and isinstance(args[1],str):
                self.x = float(args[0])
                self.y = float(args[0])
                self.label = args[1]
            elif len(args)==2 and isnumeric(args[0]) and isnumeric(args[1]):
                self.x = float(args[0])
                self.y = float(args[1])
            elif len(args)>=3 and isnumeric(args[0]) and isnumeric(args[1]) and isinstance(args[2],str):
                self.x = float(args[0])
                self.y = float(args[1])
                self.label = args[2]
            elif len(args)>=3 and isnumeric(args[0]) and isinstance(args[1],str) and isnumeric(args[2]):
                self.x = float(args[0])
                self.y = float(args[2])
                self.label = args[1]
        if len(self.label)>0 and not isinstance(self,Text):
            if len(args)>=4 and isnumeric(args[3]):
                scale = args[3]
            self.originalLabel = self.label
            self.createTheImage(scale)
    def changeImage(self,*args):
        if len(args)>=0 and self.image and isinstance(args[0],str):
            scale = 0
            if len(args)>=2 and isnumeric(args[1]):
                scale = args[1]
            self.label = args[0]
            self.createTheImage(scale)
            self.redraw()
    def createTheImage(self,scaleFactor):
        try:
            self.image = PhotoImage(file=self.label)#, height=100, width=50)
            self.size = self.image.width(),self.image.height()
        except:
            pass
        if scaleFactor > 0:                         #   scale?
            self.scale(scaleFactor)
        self.width = self.size[0]                   #   real estate in pixels
        self.height = self.size[1]
    def align(self, *args):
        if len(args)==1 and isinstance(args[0],str):
            a = args[0].lower()
            if a in ('nw','n','ne','w','c','e','sw','s','se'):
                self.anchor=a
    def scale(self,factor=1):
        if isnumeric(factor):
            if factor!=1 and self.image:
                self.factor = abs(factor)
                a = float(round(self.factor,2))
                scaling = Fraction(a).limit_denominator(10)
                #scaling = a.as_integer_ratio()
                photo = self.image.zoom(scaling.numerator)
                self.image = photo.subsample(scaling.denominator)
                self.size = self.image.width(),self.image.height()
    def itIsOn(self,*args):
        z = False
        if len(args)>=1:
            if isinstance(args[0],Point):
                p = args[0]
                z = self.l<=p.x<=self.r and self.b<=p.y<=self.t
            elif isinstance(args[0],Segment):
                z = self.on(args[0].a) and self.on(args[0].b)
        return z
    def on(self,*args):                 #   only for Image and Text
        x = False
        if len(args)>=1:
            o = args[0]
            if isinstance(o,Point):
                if isinstance(self.zIndex,tuple) and isinstance(self.zIndex[0],Designer):
                    if self.bbox:
                        self.l = self.bbox[0]
                        self.t = self.bbox[1]
                        self.r = self.bbox[2]
                        self.b = self.bbox[3]
                        if isinstance(o,Point):
                            x = self.l <= o.x <= self.r and self.b <= o.y <= self.t
            else:
                x = Point(self).on(o)
        return x
    def click(self):
        if len(self.zIndex)>0:
            d = self.zIndex[0]          #   Do we have a designer ?
            if isinstance(d,Designer):
                self.checkClick(d)
                self.checkRelease(d)
    def checkClick(self,g):
        if isinstance(g,Designer) and self.secondary>'' and g.click:
            if self.itIsOn(g.mouse):
                self.changeImage(self.secondary)
    def checkRelease(self,g):
        if isinstance(g,Designer) and self.secondary>'' and g.release:
            if self.itIsOn(g.mouse):
                self.changeImage(self.originalLabel)

#    def rotate(self,angle=0):  #   2017/12/19
#        return
#     def isnone(self):         #   2017/11/07
#        return not ( isnumeric(self.x) and isnumeric(self.y)) # or self.image==None or self.size==(0,0)
    def show(self):
        write("x,y (%.3f," % self.x, "%.3f);" % self.y, 'string' if isinstance(self,Text) else 'image',":",self.label); lf()

#------------------------ SUBCLASS BUTTON -----------------------#

class Button(Image):
    def __init__(self, *args, **kwargs):
        where = None
        for i in range(len(args)):
            if isinstance(args[i],list):
                where = i
                x,self.secondary = self.checker(args[i])
        if isnumeric(where):
            newArgs = args[:where] + (x,) + args[where+1:]
        else:
            newArgs = args
        if sys.version_info.major==3:
            super().__init__(*newArgs, **kwargs)     #   where "super" is the parent class
        else:
            super(Image,self).__init__(*newArgs, **kwargs)
    def checker(self,z):
        if len(z)==0:
            z = z + ['',]
        if len(z)==1:
            z = z + ['',]
        if len(z)>2:
            z = z[0:2]
        for x in z:
            x = str(x)
        return z[0],z[1]
#    def click(self):
#    def checkClick(self,g):
#    def checkRelease(self,g):

#------------------------ SUBCLASS TEXT -----------------------#

class Text(Image):
    fontname = 'Consolas'
    fontsize = 12
    overwrite = True

    def __init__(self, *args, **kwargs):
        if sys.version_info.major==3:
            super().__init__(*args, **kwargs)     #   where "super" is the parent class
        else:
#           super(Image,self).__init__(*args, **kwargs)
            super(Text,self).__init__(*args, **kwargs)
        if len(args)>=4 and isnumeric(args[3]):
            self.fontsize = args[3]
            if len(args)>=5 and isinstance(args[4],str):
                self.fontname = args[4]
        if len(args)>=4 and isinstance(args[3],str):
            self.fontname = args[3]
            if len(args)>=4 and isnumeric(args[4]):
                self.fontsize = args[4]
        for x in args:
            if iscolor(x):
                self.outline = x
    def newfont(self, *args):
        change = False
        if len(args)>0:
            if isnumeric(args[0]):
                if args[0]>0:
                    self.fontsize = args[0]
                change = True
                if len(args)>1 and iscolor(args[1]):
                    self.outline = args[1]
#                    if len(args)>2 and isinstance(args[2],str) and self.fontname!='':
                    if len(args)>2 and isinstance(args[2],str) and args[2]!='':
                        self.fontname = args[2]
                elif len(args)>1 and isinstance(args[1],str) and args[1]!='':
                    self.fontname = args[1]
                    if len(args)>2 and iscolor(args[2]):
                        self.outline = args[2]
            elif isinstance(args[0],str) and not iscolor(args[0]):
                if self.fontname!='':
                    self.fontname = args[0]
                change = True
                if len(args)>1 and isnumeric(args[1]) and args[1]>0:
                    self.fontsize = args[1]
                    if len(args)>2 and iscolor(args[2]):
                        self.outline = args[2]
                elif len(args)>1 and iscolor(args[1]):
                    self.outline = args[1]
                    if len(args)>2 and isnumeric(args[2]) and args[2]>0:
                        self.fontsize = args[2]
            elif iscolor(args[0]):
                self.outline = args[0]
                change = True
                if len(args)>1 and isnumeric(args[1]) and args[1]>0:
                    self.fontsize = args[1]
                    if len(args)>2 and isinstance(args[2],str) and self.fontname!='':
                        self.fontname = args[2]
                elif len(args)>1 and isinstance(args[1],str):
                    self.fontname = args[1]
                    if len(args)>2 and isnumeric(args[2]) and args[2]>0:
                        self.fontsize = args[2]

#    def scale(self, *args):                    #   not supported
#        return
#    def rotate(self, *args):                   #   2017/12/19
#        return

##    def __init__(self, *args, **kwargs):
##        super().__init__(*args, **kwargs)     #   where "super" is the parent class
##        others = ()
##        if len(args)>=1 and isinstance(args[0],str):
##            self.text = args[0]
##            others = (1,2)
##        if len(args)>=2 and isinstance(args[1],str):
##            self.text = args[1]
##            others = (0,2)
##        if len(args)>=3 and isinstance(args[2],str):
##            self.text = args[2]
##            others = (0,1)
##        if len(args)>=1 and isinstance(args[0],Text):
##            self.x = args[0].x
##            self.y = args[0].y
##            self.text = args[0].text
##        n = 0
##        for x in others:
##            if x < len(args):
##                n+= 1
##                if n==1:
##                    self.x = float(args[x])
##                elif n==2:
##                    self.y = float(args[x])
##    def isnone(self):
##        return not ( isnumeric(self.x) and isnumeric(self.y)) or self.text == None
##    def show(self):
##        write("x,y (",self.x,",",self.y,"); text (",self.text,')'); lf()

#------------------------ CLASS SEGMENT -----------------------#

class Segment(Geometric):
    a = Point()
    b = Point()
    def __init__(self, *args, **kwargs):
        self.a = Point()
        self.b = Point()
        empty = self.checkNone(args)
        if empty: #( args[0]==None or isnan(args[0]) ):
            self.a.x = float('nan'); self.a.y= float('nan')
            self.b.x = float('nan'); self.b.y= float('nan')
        elif len(args)==1 and isinstance(args[0],Segment):
            self.a.x = float(args[0].a.x); self.a.y = float(args[0].a.y)
            self.b.x = float(args[0].b.x); self.b.y = float(args[0].b.y)
        elif len(args)==1 and isinstance(args[0],Point):
            self.a.x = float(args[0].x); self.a.y = float(args[0].y)
            self.b.x = float(args[0].x); self.b.y = float(args[0].y)
        elif len(args)==2 and isinstance(args[0],Point) and isinstance(args[1],Point):
            self.a.x = float(args[0].x); self.a.y = float(args[0].y)
            self.b.x = float(args[1].x); self.b.y = float(args[1].y)
        elif len(args)==1 and isnumeric(args[0]):
            self.a.x = float(args[0])
        elif len(args)==2 and isnumeric(args[0]) and isnumeric(args[1]):
            self.a.x = float(args[0])
            self.a.y = float(args[1])
        elif len(args)>=3 and isinstance(args[0],Point) and isnumeric(args[1]) and isnumeric(args[2]):
            self.a.x = float(args[0].x)
            self.a.y = float(args[0].y)
            self.b.x = float(args[1])
            self.b.y = float(args[2])
        elif len(args)>=3 and isnumeric(args[0]) and isinstance(args[1],Point) and isnumeric(args[2]):
            self.b.x = float(args[1].x)
            self.b.y = float(args[1].y)
            self.a.x = float(args[0])
            self.a.y = float(args[2])
        elif len(args)>=3 and isnumeric(args[0]) and isnumeric(args[1]) and isinstance(args[2],Point):
            self.b.x = float(args[2].x)
            self.b.y = float(args[2].y)
            self.a.x = float(args[0])
            self.a.y = float(args[1])
        elif len(args)==3 and isnumeric(args[0]) and isnumeric(args[1]) and isnumeric(args[2]):
            self.a.x = float(args[0])
            self.a.y = float(args[1])
            self.b.x = float(args[2])
        elif len(args)>=4 and isnumeric(args[0]) and isnumeric(args[1]) and isnumeric(args[2]) and isnumeric(args[3]):
            self.a.x = float(args[0])
            self.a.y = float(args[1])
            self.b.x = float(args[2])
            self.b.y = float(args[3])
        elif len(args)==1 and isinstance(args[0],Circle):
            self.a.x = float(args[0].c.x-args[0].r); self.a.y = float(args[0].c.y)
            self.b.x = float(args[0].c.x+args[0].r); self.b.y = float(args[0].c.y)
    def isnone(self):
        return self.a.isnone() or self.b.isnone()
    def length(self):
        return self.a.distance(self.b)
    def angle(self):
        return zero_2PI(self.a.angle(self.b))
    def slope(self):
        return tan(self.angle())
    def spin(self,_a,reverse=0):
        self.rotate(_a,reverse)
        if self.zIndex:
            self.redraw()
    def rotate(self,_a,reverse=0):
        if reverse:
            s = Segment(self.b,self.a)
            s.rotate(_a)
            self.a.x = float(s.b.x); self.a.y = float(s.b.y)
            self.b.x = float(s.a.x); self.b.y = float(s.a.y)
        else:
            lng = self.length()
            ang = self.a.angle(self.b)
            ang+=_a
            self.b.x = self.a.x + lng * cos(ang)
            self.b.y = self.a.y + lng * sin(ang)
        return self
    def stretch(self,_length,reverse=0):
        if reverse:
            ang = self.b.angle(self.a)
            self.a.x = self.b.x + _length * cos(ang)
            self.a.y = self.b.y + _length * sin(ang)
        else:
            ang = self.a.angle(self.b)
            self.b.x = self.a.x + _length * cos(ang)
            self.b.y = self.a.y + _length * sin(ang)
        return self
    def midpoint(self):
        return self.a.midpoint(self.b)
    def at(self,d):
        p = Point()
        if isnumeric(d):
            if d<0: d=0.
            if d>1: d=1.
            a = self.angle()
            p.x = self.a.x + d * self.length() * cos(a)
            p.y = self.a.y + d * self.length() * sin(a)
        else:
            p.x = float('nan'); p.y = float('nan')
        return p
    def where(self,p):
        if isinstance(p,Point) and p.on(self):
            return p.where(self)
    def sub(self,n):
        if isnumeric(n):
            if n<=0: n=1
        else:
            n = 1
        return max(.0001,self.length() / n),n+1
    def flip(self):
        self.a, self.b = self.b, self.a
    def verify_on(self,*args):                              #   Check if both end points lie on a shape
        if len(args)>=1 and isinstance(args[0],Geometric):
            x = args[0]
            if self.isnone():
                pass
            elif self.a.on(x) and self.b.on(x):
                pass
            elif not self.a.on(x) and not self.b.on(x):
                self.a = self.b = Point(None)
            elif self.a.on(x) and not self.b.on(x):
                self.b = Point(self.a)
            elif not self.a.on(x) and self.b.on(x):
                self.a = Point(self.b)
    def section(self,*args):
        x = None
        if len(args)==0:
            x = self.a.section(self.b)
        elif len(args)>=1 and isinstance(args[0],Point):
            x = args[0].section(self)
        elif len(args)>=1 and ( isinstance(args[0],Segment) or isinstance(args[0],Line)  or isinstance(args[0],Ray) ):
            r = Line(self)
            s = Line(args[0])
            x = r.section(s)
            if x.isnone() or not x.on(self) or not x.on(args[0]):
                x = Point(None)
        elif len(args)>=1 and ( isinstance(args[0],Circle) ):
            if self.inside(args[0]):
                x = Segment(float('nan'))
            else:
                r = Line(self)
                x = args[0].section(r)
                x.verify_on(self)
#                if not x.isnone():
#                    if x.a.on(self) and not x.b.on(self):
#                        x.b = Point(x.a)
#                    elif x.b.on(self) and not x.a.on(self):
#                        x.a = Point(x.b)
#                    elif not x.a.on(self) and not x.b.on(self):
#                        x = Segment(None)
        return x
    def inside(self,*args):
        x = None
        if len(args)==1 and (isinstance(args[0],Circle) or isinstance(args[0],Rectangle)):
            x = self.a.internal(args[0])<1 and self.b.internal(args[0])<1
        return x
    def distance(self, *args):
        d = float('nan')
        if len(args)>=1 and isinstance(args[0],Point):
            d = args[0].distance(self)
        elif len(args)>=1 and ( isinstance(args[0],Segment) or isinstance(args[0],Line) or isinstance(args[0],Circle) or isinstance(args[0],Ray) or isinstance(args[0],Rectangle)):
            s = self.section(args[0])
            if isinstance(s,Segment) and not s.isnone():
                d = 0.
            elif isinstance(s,Point) and not s.isnone():
                d = 0.
            else:
                d1 = self.a.distance(args[0])
                d2 = self.b.distance(args[0])
                if ( isinstance(args[0],Circle) or isinstance(args[0],Rectangle)) and d1<0 and d2<0:
                    d = max(d1,d2)
                else:
                    d = min(d1,d2)
        return d
    def equal(self, *args):
        x = False
        if len(args)>=1 and isinstance(args[0],Segment):
            x = equal(self.a,args[0].a) and equal(self.b,args[0].b) or equal(self.b,args[0].a) and equal(self.a,args[0].b)
        return x
    def parallel(self,*args):
        x = Line(None)
        if len(args)>=1 and isinstance(args[0],Point):
            x = args[0].parallel(self)
        elif len(args)>=1 and ( isinstance(args[0],Line) or isinstance(args[0],Segment) or isinstance(args[0],Ray) ):
            r = Line(args[0])
            s = Line(self)
            x = equal( s.slope(), r.slope())
        elif len(args)>=1 and isinstance(args[0],Circle):
            c = Circle(args[0])
            x = not self.on(c) and equal( self.a.distance(c.c),self.b.distance(c.c) ) 
        elif len(args)>=1 and isinstance(args[0],Geometric):
            x = None
        return x
    def perpendicular(self,*args):
        x = Line(None)
        if len(args)>=1 and isinstance(args[0],Point):
            x = args[0].perpendicular(self)
        elif len(args)==1 and ( isinstance(args[0],Segment) or isinstance(args[0],Line) or isinstance(args[0],Ray)):
            r = Line(args[0])
            s = Line(self)
            x = s.perpendicular(r)
        elif len(args)>=1 and isinstance(args[0],Circle):
            s = Line(self)
            x = s.on(args[0].c)
        elif len(args)>=1 and isinstance(args[0],Geometric):
            x = None
        return x
    def adjust(self,g,dx,dy,factor):
        old = g.x(self.a.x),g.y(self.a.y)
        for z in (self.a,self.b):
            z.x = z.x * factor + dx
            z.y = z.y * factor + dy
        return g.x(self.a.x)-old[0], g.y(self.a.y)-old[1]
    def ordinate(self,x):
        return Line(self).ordinate(x)
    def abscissa(self,y):
        return Line(self).abscissa(y)
    def show(self):
        write("a(x,y) (%.3f," % self.a.x, "%.3f);" % self.a.y, "b(x,y) (%.3f," % self.b.x, "%.3f" % self.b.y, ")"); lf()
    def itIsOn(self,*args):
        if len(args)>=1 and isinstance(args[0],Image):
            return args[0].itIsOn(self)

#------------------------ SUBCLASS DASH -----------------------#

class Dash(Segment):
    pass                    #   everything else is inherited; only change: end points not shown

#------------------------ CLASS CIRCLE -----------------------#

class Circle(Geometric):
    def __init__(self, *args, **kwargs):
        self.c = Point()
        self.r = 1.
        empty = self.checkNone(args)
        if empty: #len(args)>=1 and ( args[0]==None or isnan(args[0]) ):
            self.c.x = float('nan')
            self.c.y = float('nan')
            self.r   = float('nan')
        elif len(args)==1 and isinstance(args[0],Point):
            self.c.x = float(args[0].x)
            self.c.y = float(args[0].y)
        elif len(args)>=1 and isinstance(args[0],Point) and isnumeric(args[1]):
            self.c.x = float(args[0].x)
            self.c.y = float(args[0].y)
            self.r = float(args[1])
        elif len(args)>=1 and isnumeric(args[0]) and isinstance(args[1],Point):
            self.c.x = float(args[1].x)
            self.c.y = float(args[1].y)
            self.r = float(args[0])
        elif len(args)==2 and isnumeric(args[0]) and isnumeric(args[1]):
            self.c.x = float(args[0])
            self.c.y = float(args[1])
        elif len(args)==3 and isnumeric(args[0]) and isnumeric(args[1]) and isnumeric(args[2]):
            self.c.x = float(args[0])
            self.c.y = float(args[1])
            self.r = float(args[2])
        elif len(args)==2 and isinstance(args[0],Point) and isinstance(args[1],Point):
            d = args[0].distance(args[1])/2.
            self.c = args[0].projection(args[1],d)      
            self.r = float(d)
        elif len(args)==1 and isinstance(args[0],Segment):
            self.c = args[0].a.midpoint(args[0].b)
            self.r = args[0].length()/2.
        elif len(args)==1 and isinstance(args[0],Circle):
            self.c.x = float(args[0].c.x)
            self.c.y = float(args[0].c.y)
            self.r = float(args[0].r)
        elif len(args)>=4 and isnumeric(args[0]) and isnumeric(args[1]) and isnumeric(args[2]) and isnumeric(args[3]):
            s = Segment(args[0],args[1],args[2],args[3])
            self.c = s.midpoint()
            self.r = s.length()/2.
    def isnone(self):
        return self.c.isnone() or not isnumeric(self.r)
    def length(self):
        return 2. * pi * self.r
    def area(self):
        return pi * pow(self.r,2)
    def at(self,d):
        p = Point()
        if isnumeric(d):
            p.x = self.c.x + self.r * cos(d)
            p.y = self.c.y + self.r * sin(d)
        else:
            p.x = None; p.y = None
        return p
    def where(self,p):
        if isinstance(p,Point) and p.on(self):
            return p.where(self)
    def stretch(self,d):
        if isnumeric(d):
            self.r = abs(d)
    def section(self,*args):
        s = Segment(None)
        if len(args)>=1 and ( isinstance(args[0],Point) or isinstance(args[0],Segment)):
            s = args[0].section(self)
        elif len(args)>=1 and isinstance(args[0],Circle):
            s = Segment(None)
            c1 = Circle(self)
            c2 = Circle(args[0])
            if c1.c.distance(c2.c) <= c1.r + c2.r:
                z = (c1.c).projection(c2.c, c1.r)   #   point on the circle
                r = Segment( c1.c, z)               #   the radius
                a = c2.r                            #   the triangle
                b = c1.c.distance(c2.c)
                c = c1.r
                angle = acos( ( pow(b,2) + pow(c,2) - pow(a,2) ) / ( 2 * b * c ) )
                r.rotate(angle)
                s.a = Point(r.b)                    #   first end point
                r.rotate(-2*angle)
                s.b = Point(r.b)                    #   second end point
        elif len(args)>=1 and isinstance(args[0],Line):
            s = Segment(float('nan'))
            t = Line(args[0])
            p = self.c.projection(t)
            d = self.c.distance(p)
            if equal(d,0):
                if t.vertical():
                    s.a.x = self.c.x
                    s.a.y = self.c.y - self.r
                    s.b.x = self.c.x
                    s.b.y = self.c.y + self.r
                else:
                    p = Point(self.c.x+1,t.ordinate(self.c.x+1))
                    s.a = self.c.projection(p,-self.r)
                    s.b = self.c.projection(p,+self.r)
            elif d <= self.r:
                a = acos(d/self.r)
                q = self.c.projection(p,self.r)
                t = Segment(self.c,q)
                t.rotate(a)
                s.a = Point(t.b)
                t.rotate(-2*a)
                s.b = Point(t.b)
        elif len(args)>=1 and isinstance(args[0],Ray):
            r = Line(args[0])
            s = self.section(r)
            s.verify_on(args[0])
        return s
    def inside(self,*args):
        x = None
        if len(args)>=1 and ( isinstance(args[0],Point) or isinstance(args[0],Segment)):
            x = args[0].inside(self)
        elif len(args)>=1 and ( isinstance(args[0],Circle) or isinstance(args[0],Rectangle )):
            x = self.c.inside(args[0]) and self.r <= abs(self.c.distance(args[0]))
        return x
    def distance(self, *args):
        d = None
        if len(args)>=1 and ( isinstance(args[0],Point) or isinstance(args[0],Segment) ):
            d = args[0].distance(self)
        elif len(args)>=1 and ( isinstance(args[0],Line) or isinstance(args[0],Ray)):
            s = self.section(args[0])
            if isinstance(s,Segment):
                if not s.isnone():
                    d = 0
                else:
                    d = self.c.distance(self.c.projection(args[0])) - self.r
        elif len(args)>=1 and isinstance(args[0],Circle):
            c2 = Circle(args[0])
            radii = self.r + c2.r
            d2 = self.c.distance(c2.c)
            if d2 >= radii:
                d = d2 - radii
            else:
                if self.inside(c2):
                    d = self.c.distance(c2) + self.r
                elif c2.inside(self):
                    d = c2.c.distance(self) + c2.r
                else:
                    d=0
        return d
    def equal(self, *args):
        x = False
        if len(args)>=1 and isinstance(args[0],Circle):
            x = equal(self.c,args[0].c) and equal(self.r,args[0].r)
        return x
    def parallel(self,*args):
        x = None
        if len(args)>=1 and ( isinstance(args[0],Point) or isinstance(args[0],Line) or isinstance(args[0],Segment) or isinstance(args[0],Ray) ):
            args[0].parallel(self)
        elif len(args)>=1 and isinstance(args[0],Circle):
            x = self.c.distance(args[0].c) > self.r + args[0].r
        elif len(args)>=1 and isinstance(args[0],Geometric):
            x = None
        return x
    def perpendicular(self,*args):
        x = None
        if len(args)>=1 and isinstance(args[0],Point):
            x = args[0].perpendicular(self)
        elif len(args)==1 and ( isinstance(args[0],Segment) or isinstance(args[0],Line) or isinstance(args[0],Ray)):
            s = Line(args[0])
            x = s.perpendicular(self)
        elif len(args)>=1 and isinstance(args[0],Geometric):
            x = None
        return x
    def adjust(self,g,dx,dy,factor):
        old = g.x(self.c.x),g.y(self.c.y)
        self.c.x = self.c.x * factor + dx
        self.c.y = self.c.y * factor + dy
        return g.x(self.c.x)-old[0], g.y(self.c.y)-old[1]
    def show(self):
        write("c(x,y) (%.3f," % self.c.x, "%.3f" % self.c.y, "); r :",self.r); lf()

#------------------------ SUBCLASS RING -----------------------#

class Ring(Circle):
    pass                    #   everything else is inherited; only change: center not shown

#------------------------ SUBCLASS DISK -----------------------#

class Disk(Circle):
    pass                    #   everything else is inherited; only change: interior color

#------------------------ CLASS LINE -----------------------#

class Line(Geometric):
    a = 0.; b = 0.; c = 0.
    def __init__(self, *args, **kwargs):
        empty = self.checkNone(args)
        if len(args)==0:
            self.b = 1.
        elif empty: # len(args)>=1 and ( args[0]==None or isnumeric(args[0]) and isnan(args[0]) ):
            self.a = float('nan')
            self.b = float('nan')
            self.c = float('nan')
        elif len(args)==1 and isinstance(args[0],Line):
            self.a = float(args[0].a)
            self.b = float(args[0].b)
            self.c = float(args[0].c)
        elif len(args)==1 and isinstance(args[0],Segment):
            x = args[0].section()
            self.a = float(x.a)
            self.b = float(x.b)
            self.c = float(x.c)
        elif len(args)==1 and isinstance(args[0],Circle):
            self.a = 0.
            self.b = 1.
            self.c = -float(args[0].c.y)
        elif len(args)==1 and isinstance(args[0],Ray):
            p = args[0].at(1)
            x = Line(args[0].v,p)
            self.a = float(x.a)
            self.b = float(x.b)
            self.c = float(x.c)
        elif len(args)==1 and isnumeric(args[0]):
            self.b = 1.
            self.c = -float(args[0])
        elif len(args)==2 and isnumeric(args[0]) and isnumeric(args[1]):
            self.a = float(args[0])
            self.b = -1.
            self.c = float(args[1])
        elif len(args)==3 and isnumeric(args[0]) and isnumeric(args[1]) and isnumeric(args[2]):
            self.a = float(args[0])
            self.b = float(args[1])
            self.c = float(args[2])
            if iszero(self.a) and iszero(self.b) and iszero(self.c):
                self.b = 1.
        elif len(args)==1 and isinstance(args[0],Point):
            self.a = 0.
            self.b = 1.
            self.c = -float(args[0].y)
        elif len(args)==2 and isinstance(args[0],Point) and isinstance(args[1],Point):
            x = args[0].section(args[1])        
            self.a = float(x.a)
            self.b = float(x.b)
            self.c = float(x.c)
        elif len(args)==4 and isnumeric(args[0]) and isnumeric(args[1]) and isnumeric(args[2]) and isnumeric(args[3]):
            p = Point(args[0],args[1])
            q = Point(args[2],args[3])
            if p.equal(q):
                q.x = p.x+1.
            x = p.section(q)                    
            self.a = float(x.a)
            self.b = float(x.b)
            self.c = float(x.c)
    def isnone(self):
        return not ( isnumeric(self.a) and isnumeric(self.b) and isnumeric(self.c)) or (equal(self.a,0) and equal(self.b,0))
    def vertical(self):
        return ( abs(self.b) < EQUALITY )
    def horizontal(self):
        return ( abs(self.a) < EQUALITY )
    def slope(self):
        if self.vertical():
            return float('inf')
        else:
            return -self.a/self.b
    def angle(self):
        _a = None
        if self.a != 0 or self.b != 0:
            _a = atan2(self.a,-self.b)
        return zero_2PI(_a)
    def intercept(self):
        if self.vertical():
            return None
        else:
            return -self.c/self.b
    def ordinate(self,x):
        if self.vertical() or not isnumeric(x):
            return None
        else:
            return -self.a/self.b*x-self.c/self.b
    def y(self,x):
        return self.ordinate(x)
    def value(self,x):
        return self.ordinate(x)
    def abscissa(self,y):
        if self.horizontal() or not isnumeric(y):
            return None
        else:
            return -self.b/self.a*y-self.c/self.a
    def x(self,y):
        return self.abscissa(y)
    def section(self,*args):                                    
        x = Point(float('nan'))
        if len(args)>=1 and ( isinstance(args[0],Point) or isinstance(args[0],Segment) or isinstance(args[0],Circle)):
            x = args[0].section(self)
        elif len(args)>=1 and isinstance(args[0],Line):
            r = Line(args[0])
            delta = self.a * r.b - self.b * r.a
            if ( delta ):
                x.x = ( self.b * r.c - r.b * self.c ) / delta
                x.y = ( r.a * self.c - self.a * r.c ) / delta
        elif len(args)>=1 and isinstance(args[0],Ray):
            r = Line(args[0])
            x = self.section(r)
            if ( not x.on(args[0]) ):
                x = Point(None)
        return x
    def parallel(self,*args):
        x = None
        if len(args)>=1 and isinstance(args[0],Point):
            x = args[0].parallel(self)
        elif len(args)>=1 and ( isinstance(args[0],Line) or isinstance(args[0],Segment) or isinstance(args[0],Ray) ):
            r = Line(args[0])
            x = equal( self.slope(), r.slope())
        elif len(args)>=1 and isinstance(args[0],Circle):
            x = not self.on(args[0])
        elif len(args)>=1 and isinstance(args[0],Geometric):
            x = None
        return x
    def perpendicular(self,*args):
        x = None
        if len(args)>=1 and isinstance(args[0],Point):
            x = args[0].perpendicular(self)
        elif len(args)==1 and isinstance(args[0],Line):
            x = False
            if iszero(self.a) and not iszero(args[0].b):
                x = True
            elif iszero(self.b) and not iszero(args[0].a):
                x = True
            elif not iszero(self.a) and not iszero(self.b) and not iszero(args[0].a) and not iszero(args[0].b):
                x = equal( self.b / self.a, - args[0].a / args[0],b)
        elif len(args)==1 and ( isinstance(args[0],Segment) or isinstance(args[0],Ray) ):
            r = Line(args[0])
            x = self.perpendicular(r)
        elif len(args)==1 and isinstance(args[0],Circle):
            x = self.on(args[0].c)
        elif len(args)>=1 and isinstance(args[0],Geometric):
            x = None
        return x
    def distance(self, *args):
        d = None
        if len(args)>=1 and ( isinstance(args[0],Point) or isinstance(args[0],Segment) or isinstance(args[0],Circle)):
            d = args[0].distance(self)
        elif len(args)>=1 and isinstance(args[0],Line):
            if self.parallel(args[0]):
                r = O.perpendicular(self)
                p = r.section(self)
                q = r.section(args[0])
                d = p.distance(q)
            else:
                d=0
        elif len(args)>=1 and isinstance(args[0],Ray):
            r = Line(args[0])
            p = self.section(r)
            if p.on(args[0]):
                d = 0
            else:
                d = self.distance(args[0].v)
        return d
    def equal(self, *args):
        x = False
        if len(args)>=1 and isinstance(args[0],Line):
            w = Line(args[0])
            if w.vertical() and self.vertical():
                x = equal(self.x/self.a, w.x/w.a)
            elif self.vertical() and not w.vertical() or w.vertical() and not self.vertical():
                x = False
            else:
                x = equal(self.slope(),args[0].slope()) and equal(self.intercept(),args[0].intercept())
        return x
    def at(self,x):
        if self.vertical():
            p = Point(-self.c/self.a,x)
        else:
            p = Point(x,self.ordinate(x))
        return p
    def spin(self,_a,where):
        p = None
        if isinstance(where,Point):
            p = Point(where)
            if self.vertical():
                q = Point(-self.c/self.a,p.x+1)
            else:
                q = Point(p.x+1,self.ordinate(p.x+1))
        if isnumeric(where):
            if self.vertical():
                p = Point(-self.c/self.a,where)
                q = Point(-self.c/self.a,where+1)
            else:
                p = Point(where,self.ordinate(where))
                q = Point(where+1,self.ordinate(where+1))
        if self.on(p) and self.on(q):
            s = Segment(p,q)
            s.rotate(_a)
            z = Line(s)
            self.a = z.a
            self.b = z.b
            self.c = z.c
            if self.zIndex:
                self.redraw()
    def show(self):
        write("a,b,c (%.3f" % self.a,",%.3f" % self.b,",%.3f" % self.c)
        if self.vertical():
            write("); vertical, x = %.3f" % (-self.c / self.a)); lf()
        else:
            write("); m,q (%.3f" % self.slope(),",%.3f)" % self.intercept()); lf()

    def adjust(self,g,dx,dy,factor):
        if self.vertical():
            y = 0
            x = self.abscissa(y)
        else:
            x = 0
            y = self.ordinate(x)
        p = Point(x,y)
        old = (g.x(p.x),g.y(p.y))
        p.adjust(g,dx,dy,factor)
        q = p.parallel(self)
        self.a = q.a
        self.b = q.b
        self.c = q.c
        return (g.x(p.x)-old[0],g.y(p.y)-old[1])

#------------------------ CLASS RAY -----------------------#

class Ray(Geometric):
    def __init__(self, *args, **kwargs):
        self.v = Point()
        self.a = 0.
        empty = self.checkNone(args)
        if empty: #len(args)>=1 and ( args[0]==None or isnan(args[0]) ):
            self.v.x = float('nan')
            self.v.y = float('nan')
            self.a = float('nan')
        elif len(args)==1 and isinstance(args[0],Segment):
            self.v.x = float(args[0].a.x)
            self.a = args[0].a.angle(args[0].b)
        elif len(args)>=1 and isinstance(args[0],Circle):
            self.v.x = float(args[0].c.x)
            self.v.y = float(args[0].c.y)
        elif len(args)==1 and isnumeric(args[0]):
            self.v.x = float(args[0])
        elif len(args)==2 and isnumeric(args[0]) and isnumeric(args[1]):
            self.v.x = float(args[0])
            self.v.y = float(args[1])
        elif len(args)==3 and isnumeric(args[0]) and isnumeric(args[1]) and isnumeric(args[2]):
            self.v.x = float(args[0])
            self.v.y = float(args[1])
            self.a = float(args[2])
        elif len(args)==1 and isinstance(args[0],Point):
            self.v.x = float(args[0].x)
            self.v.y = float(args[0].y)
        elif len(args)==2 and isinstance(args[0],Point) and isinstance(args[1],Point):
            self.v.x = float(args[0].x)
            self.v.y = float(args[0].y)
            self.a = args[0].angle(args[1])
        elif len(args)==4 and isnumeric(args[0]) and isnumeric(args[1]) and isnumeric(args[2]) and isnumeric(args[3]):
            p = Point(args[0],args[1])
            q = Point(args[2],args[3])
            self.v.x = float(p.x)
            self.v.y = float(p.y)
            self.a = p.angle(q)
        self.reduction()
    def isnone(self):
        return self.v.isnone() or not isnumeric(self.a)
    def reduction(self):
        self.a = zero_2PI(self.a)
    def vertical(self):
        return equal(self.a,pi/2) or equal(self.a,3*pi/2)
    def horizontal(self):
        return equal(self.a,0) or equal(self.a,pi)
    def slope(self):
        return tan(self.a)
    def angle(self):
        return self.a
    def equal(self, *args):
        x = False
        if len(args)==1 and isinstance(args[0],Ray):
            x = equal(self.v,args[0].v) and equal(self.a,args[0].a)
        return x
    def rotate(self, *args):
        if len(args)>=1 and isnumeric(args[0]):
            self.a+= args[0]
            self.reduction()
        return self
    def at(self, *args):
        p = Point(None)
        if len(args)>=1 and isnumeric(args[0]):
            d = abs(args[0])
            p.x = self.v.x + d * cos(self.a)
            p.y = self.v.y + d * sin(self.a)
        return p
    def where(self,p):
        if isinstance(p,Point) and p.on(self):
            return p.where(self)
    def distance(self, *args):
        d = None
        if len(args)>=1 and ( isinstance(args[0],Point) or isinstance(args[0],Segment) or isinstance(args[0],Circle) or isinstance(args[0],Line)):
            d = args[0].distance(self)
        elif len(args)>=1 and isinstance(args[0],Ray):
            r1 = Line(self)
            r2 = Line(args[0])
            p = r1.section(r2)
            if not p.isnone() and p.on(self) and p.on(args[0]):
                d = 0
            else:
                d = min(self.v.distance(args[0]),args[0].v.distance(self)) 
        return d
    def section(self,*args):
        x = Point(None)
        if len(args)>=1 and ( isinstance(args[0],Point) or isinstance(args[0],Segment) or isinstance(args[0],Circle) or isinstance(args[0],Line)):
            x = args[0].section(self)
        elif len(args)>=1 and isinstance(args[0],Ray):
            r = Line(args[0])
            s = Line(self)
            x = r,section(s)
            if ( not x.on(args[0]) or not x.on(self) ):
                x = Point(None)
        return x
    def parallel(self,*args):
        x = None
        if len(args)>=1 and isinstance(args[0],Point):
            x = args[0].parallel(self)
        elif len(args)>=1 and ( isinstance(args[0],Line) or isinstance(args[0],Segment) or isinstance(args[0],Ray) ):
            r = Line(args[0])
            s = Line(self)
            x = equal( s.slope(), r.slope())
        elif len(args)>=1 and isinstance(args[0],Circle):
            x = not self.on(args[0])
        elif len(args)>=1 and isinstance(args[0],Geometric):
            x = None
        return x
    def perpendicular(self,*args):
        x = None
        if len(args)>=1:
            if isinstance(args[0],Point) or isinstance(args[0],Segment) or isinstance(args[0],Line) or isinstance(args[0],Circle):
                x = args[0].perpendicular(self)
            elif isinstance(args[0],Ray):
                x = args[0].perpendicular(self)
                s = Line(args[0])
                x = s.perpendicular(self)
                x = None
            elif len(args)>=1 and isinstance(args[0],Geometric):
                x = None
        return x
    def adjust(self,g,dx,dy,factor):
        old = g.x(self.v.x),g.y(self.v.y)
        self.v.x = self.v.x * factor + dx
        self.v.y = self.v.y * factor + dy
        return g.x(self.v.x)-old[0], g.y(self.v.y)-old[1]
    def show(self):
        write("v: (%.3f" % self.v.x,",%.3f"  % self.v.y,"); a :",self.a); lf()

#------------------------ CLASS RECTANGLE -----------------------#

class Rectangle(Geometric):
    l = 0.
    t = 0.
    w = 0.
    h = 0.
    def __init__(self, *args, **kwargs):
        empty = self.checkNone(args)
        if empty: #len(args)>=1 and ( args[0]==None or isnan(args[0]) ):
            self.l = float('nan')
            self.t = float('nan')
            self.w = float('nan')
            self.h = float('nan')
        elif len(args)==1 and isinstance(args[0],Segment):
            s = args[0]
            self.l = float(s.a.x)
            self.t = float(s.a.y)
            self.w = float(s.b.x - s.a.x)
            self.h = float(s.b.y - s.a.y)
        elif len(args)==1 and isinstance(args[0],Circle):
            c = args[0]
            self.l = float(c.c.x - c.r)
            self.b = float(c.c.y - c.r)
            self.w = c.r * 2.
            self.h = c.r * 2.
        elif len(args)==1 and isnumeric(args[0]):
            self.l = 1.
        elif len(args)==2 and isnumeric(args[0]) and isnumeric(args[1]):
            self.l = float(args[0])
            self.t = float(args[1])
        elif len(args)==3 and isnumeric(args[0]) and isnumeric(args[1]) and isnumeric(args[2]):
            self.l = float(args[0])
            self.t = float(args[1])
            self.w = float(args[2])
        elif len(args)==1 and isinstance(args[0],Point):
            self.l = float(args[0].x)
            self.t = float(args[0].y)
            self.w = 0.
            self.h = 0.
        elif len(args)==2 and isinstance(args[0],Point) and isinstance(args[1],Point):
            self.l = float(args[0].x)
            self.t = float(args[0].y)
            self.w = float(abs(args[1].x - args[0].x))
            self.h = float(abs(args[1].y - args[0].y))
        elif len(args)==4 and isnumeric(args[0]) and isnumeric(args[1]) and isnumeric(args[2]) and isnumeric(args[3]):
            self.l = float(args[0])
            self.t = float(args[1])
            self.w = float(abs(args[2]))
            self.h = float(abs(args[3]))
    def isnone(self):
        return not ( isnumeric(self.l) and isnumeric(self.t) and isnumeric(self.w) and isnumeric(self.h))
    def length(self):
        return 2 * ( self.w + self.h )
    def inside(self,*args):
        x = None
        if len(args)>=1 and ( isinstance(args[0],Point) or isinstance(args[0],Segment)):
            x = args[0].inside(self)
        elif len(args)>=1 and ( isinstance(args[0],Circle) or isinstance(args[0],Rectangle)):
            self.box()
            p1 = Point(self.l,self.t)
            p2 = Point(self.r,self.b)
            x = p1.inside(args[0]) and p2.inside(args[0])
        return x
    def box(self):
        self.r = self.l+self.w; self.b = self.t-self.h
    def equal(self, *args):
        x = False
        if len(args)==1 and isinstance(args[0],Rectangle):
            x = equal(self.l,args[0].l) and equal(self.t,args[0].t) and equal(self.w,args[0].w) and equal(self.h,args[0].h)
        return x
    def center(self):
        return Point(self.l+self.w/2,self.t-self.h/2)
    def adjust(self,g,dx,dy,factor):
        old = g.x(self.l),g.y(self.t)
        self.l = self.l * factor + dx
        self.t = self.t * factor + dy
        return g.x(self.l)-old[0], g.y(self.t)-old[1]
    def show(self):
        write("l,t: (%.3f" % self.l,",%.3f" % self.t,"); w,h: (%.3f" % self.w,",%.3f" % self.h,"); r,b: (%.3f" % (self.l+self.w),",%.3f" % (self.t-self.h),")"); lf()

class Frame(Rectangle):
    pass                    #   everything else is inherited; only change: interior not shown

#------------------------ CLASS FUNCTION -----------------------#

class Function(Geometric):
    f = float('nan')
    def __init__(self, *args, **kwargs):
        empty = self.checkNone(args)
        if empty: #len(args)>=1 and ( args[0]==None or isnan(args[0]) ):
            pass
        elif len(args)==1 and isinstance(args[0],str):
            self.f = args[0]
        elif len(args)==1 and isinstance(args[0],Point):
            self.f = str(args[0].y)
        elif len(args)==1 and isinstance(args[0],Segment):
            r = Line(args[0])
            self.f = str(r.intercept())+'+'+str(r.slope())+'*x'
        elif len(args)==1 and isinstance(args[0],Line):
            self.f = str(args[0].intercept())+'+'+str(args[0].slope())+'*x'
        elif len(args)==2 and isinstance(args[0],Point) and isinstance(args[1],Point):
            r = args[0].section(args[1])
            self.f = str(r.intercept())+'+'+str(r.slope())+'*x'
    def value(self,*args):
        y = float('nan')
        if len(args)>=1 and isnumeric(args[0]):
            x = float(args[0])
            try:
                y = eval(self.f)
            except:
                pass
        return y
    def ordinate(self,*args):
        return self.value(*args)
    def y(self,*args):
        return self.value(*args)
    def at(self,*args):
        z = None
        if len(args)>0:
            a = args[0]
            if isnumeric(a):
                x = a
            elif isinstance(a,Point):
                x = a.x
            if isnumeric(x):
                z = Point(x,self.value(x))
        return z
    def isnone(self):
        return self.f==None
    def show(self):
        write(self.f); lf()
    def on(self,*args):
        z = False
        if len(args)>=1:
            if isinstance(args[0],Point):
                z = args[0].on(self)
            elif isinstance(args[0],Segment):
                z = self.on(args[0].a) and self.on(args[0].b)
        return z

#------------------------ SUBCLASS POLYNOMIAL -----------------------#

class Polynomial(Function):
    def __init__(self, *args, **kwargs):
        self.x = ()
        empty = self.checkNone(args)
        if len(args)>=1:
            if empty:
                self.x = (float('nan'),)
            elif isinstance(args[0],Polynomial):
                for z in args[0].x:
                    self.x = self.x + (float(z),)
            elif( isinstance(args[0],(list, tuple))):
                self.x = expand(args[0])
            else:
                self.x = expand(args)
        self.normalize()
        if len(self.x)==0:
            self.x = (0.,)
    def degree(self):
        return len(self.x)-1
    def pop(self):
        z = ()
        for i in range(0,len(self.x)-1):
            z = z + (float(self.x[i]),)
        self.x = expand(z)
    def push(self,*args):
        if len(args)>=1:
            if( isinstance(args[0],(list, tuple))):
                z = expand(args[0])
            else:
                z = expand(args)
        self.x = self.x + (float(z),)
    def show(self,*args):
        first = True
        i = len(self.x)-1
        while i>=0:
            if (self.x[i]):
                if (self.x[i]<0):
                    write("-")
                elif self.x[i]>0 and not first:
                    write("+")
               #
                if not equal(abs(self.x[i]),1) or i==0:
                    if self.x[i]:
                        write("%.3f" % abs(self.x[i]))
                    else:
                        pass
               #
                if i > 0:
                    write("x")
                    if i > 1:
                        write("**",i)
                first = False
            i-=1
        if first:
            write(0)
            first = False
        if not first:
            if len(args)>=1 and isinstance(args[0],bool) and not args[0]:
                pass
            else:
                lf()
    def value(self,x):
        z = 0.
        i = len(self.x)-1
        while i>=0:
            z = self.x[i] + x * z
            i-=1
        return z
    def y(self,*args):
        return self.value(*args)
    def showlist(self):
        write(self.x); lf()
    def derivative(self):
        n = ()
        for i in range(0,len(self.x)-1):
            n = n + (self.x[i+1]*(i+1),)
        return Polynomial(n)
    def integral(self):
        n = (1,)
        for i in range(1,len(self.x)+1):
            n = n + (self.x[i-1] / i,)
        return Polynomial(n)
    def opposite(self):
        n = ()
        for i in range(0,len(self.x)):
            n = n + (-self.x[i],)
        return Polynomial(n)
    def isnone(self):
        return False
    def normalize(self):        #   deletes unnecessary zeroes
        n = NEGATIVE_INFINITY
        i = last(self.x)
        while i>=0 and equal(self.x[i],0):
            self.pop()
            i-=1
    def add(self,*args):
        p = Polynomial()
        if len(args)>=1 and isinstance(args[0],Polynomial):
            p = []
            q = []
            s = Polynomial(args[0])
            mx = max(len(self.x),len(s.x))
            mn = min(len(self.x),len(s.x))
            for i in range(0,mx): p = p + [0]; q = q + [0]
            for i in range(0,len(self.x)): p[i] = self.x[i]
            for i in range(0,len(s.x)): q[i] = s.x[i]
            for i in range(0,mx): p[i]+=q[i];
            q = ()
            for x in p: q = q + (x,)
            p = Polynomial(p)
        return p
    def subtract(self,*args):
        if len(args)>=1 and isinstance(args[0],Polynomial):
            return self.add(args[0].opposite())
    def multiply(self,*args):
        if len(args)>=1 and isinstance(args[0],Polynomial):
            p = []
            s = Polynomial(args[0])
            for i in range(0,len(self.x)+len(s.x)): p = p + [0]
            for i in range(0,len(self.x)):
                for j in range(0,len(s.x)):
                    p[i+j]+= self.x[i] * s.x[j]
            q = ()
            for x in p: q = q + (x,)
            p = Polynomial(p)
        return p

#------------------------ SUBCLASS RATIONAL -----------------------#

class Rational(Function):                   #   2 Polynomials: numerator and denominator
    def __init__(self, *args, **kwargs):    #   may look like a superclass, but it is not
        self.numerator = Polynomial()
        self.denominator = Polynomial(1)
        empty = self.checkNone(args)
        if len(args)>=1:
            if empty:
                self.numerator.x = (float('nan'),)
            elif isinstance(args[0],Rational):
                self.numerator.x = ()
                for z in args[0].numerator.x:
                    self.numerator.x = self.numerator.x + (z,)
                self.denominator.x = ()
                for z in args[0].denominator.x:
                    self.denominator.x = self.denominator.x + (z,)
            elif isinstance(args[0],Polynomial):
                self.numerator.x = ()
                for z in args[0].x:
                    self.numerator.x = self.numerator.x + (z,)
                if len(args)>=2:
                    build = False
                    if isnumeric(args[0]):
                        build = True
                    elif isinstance(args[1],Rational):
                        poly = args[1].n.x
                    elif isinstance(args[1],Polynomial):
                        poly = args[1].x
                    if build:
                        self.denominator.x = expand(args)
                    else:
                        self.denominator.x = ()
                        for z in poly:
                            self.denominator.x = self.denominator.x + (z,)
            elif isinstance(args[0],(list, tuple)):
                self.numerator.x = expand(args[0])
                if len(args)>=2:
                    if isinstance(args[1],(list, tuple)):
                        self.denominator.x = expand(args[1])
                    else:
                        self.denominator.x = expand(args)
                else:
                    pass
            elif isnumeric(args[0]):
                if isinstance(args[len(args)-1],(list, tuple)):
                    self.denominator.x = expand(args[len(args)-1])
                self.numerator.x = expand(args)
        if iszero(self.denominator.y(0)) and iszero(self.denominator.y(1)):
            self.denominator = Polynomial(1)
        d1 = self.numerator.degree()
        d2 = self.denominator.degree()
    def isnone(self):
        return False
    def show(self):
        self.numerator.show(False)
        write('/')
        self.denominator.show()
    def showlist(self):
        self.numerator.showlist()
        self.denominator.showlist()
    def value(self,x):
        n = self.numerator.value(x)
        d = self.denominator.value(x)
        if not equal(d,0.):
            v = n / d
        else:
            if n > 0:
                v = INFINITY
            elif n < 0:
                v = NEGATIVE_INFINITY
            else:
                v = None
        return v
    def y(self,*args):
        return self.value(*args)
    def derivative(self):
        n = self.numerator.derivative().multiply(self.denominator).subtract(self.numerator.multiply(self.denominator.derivative()))
        d = self.denominator.multiply(self.denominator)
        n.normalize()
        d.normalize()
        return Rational(n,d)

#------------------------ USEFUL SHAPES (MAGIC CONSTANTS) -----------------------#

xAxis = Line()              #   x axis (what else)
yAxis = Line(1.,0.,0.)      #   y axis (what else)
O = Point()                 #   The origin
C = Circle()                #   The goniometric circle
R = Ray()                   #   positive x axis
bi13 = Line(0,0,1,1)        #   bisectors (1st-3rd quadrant)
bi24 = Line(0,0,1,-1)       #   (2nd-4th quadrant)

#---------------------------- SAMPLE --------------------------#

"""
#d.foreground(RED)
d.text('testo',2,2,25,'Annone',BLUE)
t = Text('testo')
#z = [Point(1,2), Point(2,-2), Point(-2,1)]
pol = Polynomial(-1,2,0,-1,1)
#d.newfont(30,'Annone')
#ok d.draw(t,'Annone',RED,30)
d.draw(t,RED,'Annone',30)
d.draw(pol,RED,4)
#d.draw(t,RED,30,'Annone')
#for x in z:
#    d.draw(x,BLUE)
#d.draw(Segment(-1,-2,-3,-1),RED)
#d.draw(Circle(2,.5,1.2),GREEN)
d.freeze()
d.destroy()
del d
"""
'''
w=3
g = Designer(200,200,-w,w,w,-w)
g.axes()

i = Point()
i = Segment(0,0,1,1)
#i = Function('sin(x)')
#i = Image('mario1.GIF')
#i = Line(1,1)
#i = Rectangle(0,0,2,1)
i.draw(g,BLUE,4)
while g.alive():
    if i.clicked():
        print('there was a click near the shape')
        print(g.px,g.py,g.pixel)
    g.tick(.05)

g.destroy()
del g
'''
"""
w = 200
n = -3.6
n = +3.6
d = Designer(w,w,-n,n,n,-n)
print(d.w,d.h,d.width,d.height)
d.axes()
l = Line(-3,1,-3,2)
l.draw(d,RED)
a = 0
da = 0.01
x = 1
p = l.at(x)
p.draw(d,BLUE)
while a<=pi:
    l.spin(da/2,p)
    d.tick(.01)
    a+= da

d.freeze()
d.destroy()
del d
"""
'''
w = 200
n = -3.6
n = +3.6
g = Designer(w,w,-n,n,n,-n)
sushi = Image('sushi.GIF',-3,-2)
sushi.draw(g)
elvis = Image('elvis.GIF')
elvis.draw(g)
pos = [Point(2,2),Point(2,-2),Point(-2,-2),Point(-2,2)]
p = 0
elvis.go(pos[p])
a = 0
da = 0.1
c = Circle()
c.draw(g)
t = Text(-3,3)
t.draw(g)
then = mktime(gmtime())

while g.alive():
    time = int(mktime(gmtime())-then)
    t.label = time
    t.redraw()
    sushi.go(c.at(a))
    if elvis.clicked():
        p = (p+1) % len(pos)
        elvis.go(pos[p])
    if sushi.clicked():
        print('click 2')
    if c.c.clicked():
        print('click 2')
    g.tick(0.1)
    a+= da

g.destroy()
del g

'''
