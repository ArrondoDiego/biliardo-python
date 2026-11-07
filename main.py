from marioGraphics import*
from marioConsole import*

d = Designer()
d.dimensions(900,900,-100,100,100,-100)

d.show()

#variabili di gioco
direzione = 0
intens = 1
ready = False
angolo = 0

#immagini necessarie
sfondo = Image("./imgs/sfondo.png",0,0,2)
ball = Image("./imgs/ball.png",-45,0,0.15)
asta = Image("./imgs/asta.png",-120,-8,1)
ball2 = Image("./imgs/ball2.png",0,0,0.05)

#oggetti necessari
linea = Segment(-95,0,-55,0)
radius = Circle(ball2,10)
p = Point(-45,0)
p1 = Point(-77,50)
p2 = Point(-77,-50)
p3 = Point(77,50)
p4 = Point(77,-50)
p5 = Point(0,-50)
p6 = Point(0,50)
l1 = Segment(p1,p2)
l2 = Segment(p2,p4)
l3 = Segment(p3,p4)
l4 = Segment(p3,p1)
buca1 = Circle(p1,7)
buca2 = Circle(p2,7)
buca3 = Circle(p3,7)
buca4 = Circle(p4,7)
buca5 = Circle(p5,7)
buca6 = Circle(p6,7)
tavolo = Rectangle(-77,50,154,100)


def setup():
    #disegna lo sfondo
    disegna()

    preparazione()


def disegna():
    global d
    d.draw(sfondo)
    d.draw(ball)
    d.draw(ball2)
    d.draw(asta)
    d.draw(linea)
    #d.draw(tavolo,RED,10)

def forza():
    #disegna la tabella d'intensità
    global d
    global tabella
    global intens

    if(intens==1):
        tabella = Image("./imgs/1.png",-50,80,0.25)
        tabella.draw(d)


    if(intens==2):
        tabella = Image("./imgs/2.png",-50,80,0.25)
        tabella.draw(d)


    if(intens==3):
        tabella = Image("./imgs/3.png",-50,80,0.25)
        tabella.draw(d)


    if(intens==4):
        tabella = Image("./imgs/4.png",-50,80,0.25)
        tabella.draw(d)

def preparazione():
     global ready
     global intens
     global direzione
     
     while(not ready):
         if d.key:
            if d.key=="Return":
                #siamo pronti!!!
                ready = True
            if d.key=="Right":
                #aumenta angolo
                direzione=0.02
            if d.key=="Left":
                #diminuisci angolo
                direzione=-0.02
            if d.key=="Up":
                #aumenta intensità
                if(intens<4):
                    intens+=1
            if d.key=="Down":
                #diminuisci intensità
                if(intens>1):
                    intens-=1
         update()
         direzione=0
         
     lancio()

def update():
    global angolo

    d.tick(0.00000001)
    linea.rotate(direzione,1)
    angolo = angolo + direzione
    linea.redraw(d)
    forza()

def lancio():
    global linea
    global ball
    global ball2
    global intens
    global direzione
    global p
    
    traiettoria = Line(linea)
    estremo = Point(55,traiettoria.ordinate(55))
    
    #d.draw(traiettoria)
    #d.draw(estremo,RED,10)

    while(not checkschianto()):
        ball = ball.projection(estremo,intens)
        p = p.projection(estremo,intens)
        d.tick(0.05)
        #p.draw(d,BLUE,5)
        ball.draw(d)

    traiettoria = Line(p,radius.c)
    estremo = Point(radius.c.x+100,traiettoria.ordinate(radius.c.x+100))
    #d.draw(estremo,RED,10)
    #traiettoria.draw(d,RED)
    
    q = Point(radius.c.x,radius.c.y+(angolo*100))
    poverino = Line(p,q)
    estremo2 = Point(q.x+100,poverino.ordinate(q.x+100))
    #d.draw(estremo2,BLUE,5)
    #poverino.draw(d,BLUE)
    o = Point(radius.c.x,radius.c.y)
    #d.draw(o,RED,5)

    movimento(estremo, estremo2, intens, o)

def checkschianto():
    global ball
    global ball2
    global d
    global radius

    #controllo se si scontrano
    if(ball.distance(radius.c)>=radius.r+2):
        return False
    else:
        return True

def movimento(estremo, estremo2, intens, o):
    global angolo
    global p
    global l1
    global l2
    global l3
    global l4
    global ball
    global ball2

    attrito = 0.001
    
    mball = 0.80
    mball2 = 1

    vfball = -(((mball - mball2)/(mball + mball2))*intens)*1.2
    vfball2 = (((2*mball)/(mball + mball2))*intens)/2

    print(vfball, " ", vfball2)
    ''' MANCANO LE BUCHE LATERALI e le sponde'''
    while(True):
        if(p.distance(p1)<6 or p.distance(p2)<10 or p.distance(p3)<10 or p.distance(p4)<10):
            perso()
            vfball = 0
            vfball2 = 0
        if(vfball>0):
            if(p.distance(l1)<1 or p.distance(l2)<1 or p.distance(l3)<1 or p.distance(l4)<1):
                vfball = 0
            else:
                vfball = vfball - attrito

            p = p.projection(estremo2,vfball)
            ball = ball.projection(estremo2,vfball)
            #d.draw(p,BLUE,5)
            d.draw(ball)
            
        if(o.distance(p1)<6 or o.distance(p2)<10 or o.distance(p3)<10 or o.distance(p4)<10):
            vinto()
            vfball2 = 0
            vfball = 0
        if(vfball>0):
            if(o.distance(l1)<1 or o.distance(l2)<1 or o.distance(l3)<1 or o.distance(l4)<1):
                vfball2 = 0
            else:
                vfball2 = vfball2 - attrito

            o = o.projection(estremo,vfball2)
            ball2 = ball2.projection(estremo,vfball2) 
            #d.draw(o,RED,5)
            d.draw(ball2)

def perso():
    #print("perso")
    lose = Image("./imgs/lose.png",0,0)
    d.draw(lose)
    d.freeze()

def vinto():
    print("vinto")
    win = Image("./imgs/win.png",0,0,0.5)
    d.draw(win)
    d.freeze()
        

setup()
