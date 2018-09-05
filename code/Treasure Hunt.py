from ctypes import *
import pygame, sys
from pygame.locals import *
from random import *
import os
print("--------------------------Treasure Hunt----------------------------")
windll.user32.SetProcessDPIAware()
true_res = (windll.user32.GetSystemMetrics(0),windll.user32.GetSystemMetrics(1))
SCREENWIDTH=true_res[0]
SCREENHEIGHT=true_res[1]
i=1
imgB=pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"jjj.jpg")),True,False),(SCREENWIDTH,SCREENHEIGHT))
imgB.set_alpha(80)
imgc1=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"jjj.jpg")),(SCREENWIDTH,SCREENHEIGHT))
imgb1=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"jjj.jpg")),(SCREENWIDTH,SCREENHEIGHT))
imgb1.set_alpha(180)
imgd1=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"tre1.jpg")),(SCREENWIDTH,SCREENHEIGHT))
imgd1.set_alpha(80)
img6=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"pl.png")),(int(SCREENWIDTH/9.6),int(SCREENHEIGHT/7.2)))
img7=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"pn1.png")),(int(SCREENWIDTH/9.6),int(SCREENHEIGHT/7.2)))
img8=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"tip.png")),(int(SCREENWIDTH/12.8),int(SCREENHEIGHT/10.8)))
img9=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"th.png")),(int(SCREENWIDTH/2),int(SCREENHEIGHT)))
img10=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"home.png")),(int(SCREENWIDTH/12.8),int(SCREENHEIGHT/10.8)))
img11=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"NEXT.png")),(int(SCREENWIDTH/9.6),int(SCREENHEIGHT/10.8)))
img12=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"round1.png")),(int(SCREENWIDTH/7.68),int(SCREENHEIGHT/14.3)))
img13=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"r.png")),(int(SCREENWIDTH/9),int(SCREENHEIGHT/14.3)))
img131=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"21.gif")),(int(SCREENWIDTH/20),int(SCREENHEIGHT/9)))
img14=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"round3.png")),(int(SCREENWIDTH/7.68),int(SCREENHEIGHT/14.3)))
img1=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"spritesheet (1).png"))
numImages1=4
imggold=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"go.png")),(int(SCREENWIDTH/15),int(SCREENHEIGHT/8.5)))
imgsilver=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"sl.png")),(int(SCREENWIDTH/15),int(SCREENHEIGHT/8.5)))
imgbronze=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"br.png")),(int(SCREENWIDTH/15),int(SCREENHEIGHT/8.5)))
img2=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"123.png"))
numImages2=29
img3=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"download (2).png"))
numImages3=41
img5=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"spritesheet.png")),(int(SCREENWIDTH/11.75),int(SCREENHEIGHT/9.9)))
numImages5=2
WINDOWMULTIPLIER =5
WINDOWSIZE =int(SCREENWIDTH/10.97)
WINDOWWIDTH =WINDOWSIZE * WINDOWMULTIPLIER
WINDOWHEIGHT =WINDOWSIZE * WINDOWMULTIPLIER
SQUARESIZE = int((WINDOWSIZE * WINDOWMULTIPLIER) / 5)
img0=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"1.jpg"))
img0=pygame.transform.scale(img0, (SQUARESIZE, SQUARESIZE))
img01=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"1.jpg")),(SCREENWIDTH,SCREENHEIGHT))
BLACK =    (0,  0,  0)
WHITE =    (255,255,255)#white color in RGB format
pygame.mixer.pre_init(44100, 16, 2,4096)
pygame.mixer.init()
pygame.mixer.set_num_channels(2) 
s1=pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"startmusic.wav"))
s2=pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"mainmusic.wav"))
s3=pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"topen.wav"))
s5=pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"tclose.wav"))
s4=pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"click.wav"))
img4=pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"coins.png")),(SQUARESIZE,SQUARESIZE))
pygame.display.set_caption('TREASURE HUNT') 
DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT),pygame.RESIZABLE) 
shiftx=int(SCREENWIDTH/12)
shifty=int(SCREENHEIGHT/30)
def random_row():
    return randint(0,4)
def random_col():
    return randint(0,4)
def box(i):
 l=[]
 while len(l)!=1+2*i:  
    ship_row = random_row()
    ship_col = random_col()
    
    if (ship_row,ship_col) in l:
        continue
    l.append((ship_row,ship_col))
 return l
def equal(l,k):
 c=0
 for i in l:
    for j in k:
        if i==j:
            c+=1
            break
 return c
def drawGrid():
   for x in range(0+shiftx, WINDOWWIDTH+shiftx+SQUARESIZE, SQUARESIZE): # draw vertical lines
      pygame.draw.line(DISPLAYSURF, BLACK, (x,0+shifty),(x,WINDOWHEIGHT+shifty))
   for y in range (0+shifty, WINDOWHEIGHT+shifty+SQUARESIZE, SQUARESIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLACK, (0+shiftx,y), (WINDOWWIDTH+shiftx, y))
def initiateCells():
    currentGrid = {}
    for xCoord in range(0,5):
        for yCoord in range(0,5):
            currentGrid[xCoord,yCoord] = 'X' # Copies List
    return currentGrid
def displaycells(currentGrid):
      for item in currentGrid: # item is x,y co-ordinate from 0 - 8
         # isolates the numbers still available for that cell
        celldata=currentGrid[item] 
        populateCells(celldata,((item[0])*SQUARESIZE+shiftx+(WINDOWSIZE/2)),((item[1])*SQUARESIZE+(WINDOWSIZE/2)+shifty))
      return None
def populateCells(cellData,x,y):
    cellSurf = myfont.render('%s' %(cellData), True, BLACK)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = (x, y)
    DISPLAYSURF.blit(cellSurf, cellRect)
    DISPLAYSURF.blit(img0,(x-(SQUARESIZE/2),y-(SQUARESIZE/2)))
def drawBox(mousex, mousey):
    boxx =((mousex*5) / WINDOWWIDTH) * (SQUARESIZE ) # 27 number of squares
    boxy =((mousey*5) / WINDOWHEIGHT) * (SQUARESIZE ) # 27 number of squares
    pygame.draw.rect(DISPLAYSURF, BLUE, (boxx,boxy,SQUARESIZE,SQUARESIZE), 1)    
def end(i,mouseClicked,mousex,mousey):
                              if i <3:
                               print("\nResults:-")   
                               print("\nRound %s:-\n"%(i))
                               print("Total Treasures this round:\t",a)
                               print("Collected Treasures:\t",o)  
                               if i==1:  
                                
                                if r<=1000:   
                                 print("Come on!! You can Guess much Better!!")
                                elif r==2000:
                                    print("Well done! Keep Going")
                                else:
                                    print("Congrats!!!! You Collected All the Treasures")
                               if i==2:
                                 if r<=3000:   
                                  print("Come on!! You can Guess much Better!!")
                                 elif r>3000 and r<=5000:
                                    print("Well done! Keep Going")
                                 else:
                                    print("Congrats!!!! You Collected All the Treasures")
                               print("NET SCORE:\t",r)   
                               main(i+1)
                              else:
                                  print("\nResults:-")   
                                  print("\nRound %s:-\n"%(i))
                                  print("Total Treasures this round:\t",a)
                                  print("Collected Treasures:\t",o)
                                  print("You Got %s coins out of 15000"%(r)) 
                                  final=myfont.render("FINAL SCORE",True,WHITE)
                                  final1=myfont.render("YOU WON:",True,WHITE)
                                  print("\nFINAL SCORE:")
                                  print(r,"\n")
                                  
                                  if r==0:
                                      print("You Lose:-\n")
                                      print("HARD LUCK!!!!")
                                      print("KEEP GUESSING!!!!")
                                      DISPLAYSURF.blit(myfont.render("Hard Luck :p",True,WHITE),(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/3.3)))    
                                      DISPLAYSURF.blit(myfont.render("Keep Guessing!!!",True,WHITE),(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/2.075)))    
                                  elif r>1000 and r<5000:
                                      print("Congrats!!!! You WON:-\n")
                                      print("A BRONZE TROPHY!!!!")
                                      DISPLAYSURF.blit(imgbronze,(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/3.3)))
                                      DISPLAYSURF.blit(myfont.render("A BRONZE Trophy!!!",True,WHITE),(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/2.075)))
                                  elif r>4000 and r<9000:
                                      print("Congrats!!!! You WON:-\n")
                                      print("A SILVER TROPHY!!!!")
                                      DISPLAYSURF.blit(imgsilver,(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/3.3)))
                                      DISPLAYSURF.blit(myfont.render("A SILVER Trophy!!!",True,WHITE),(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/2.075)))
                                  else:    
                                      print("Bulls Eye!!!!! You WON:-\n")
                                      print("A GOLD TROPHY!!!!") 
                                      DISPLAYSURF.blit(imggold,(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/3.3)))
                                      DISPLAYSURF.blit(myfont.render("A Gold Trophy!!!",True,WHITE),(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/2.075)))
                                  DISPLAYSURF.blit(final1,(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/4)))    
                                  score=myfont.render('%s' %(r),True,WHITE)
                                  DISPLAYSURF.blit(img9,(int(SCREENWIDTH/3.9),-int(SCREENHEIGHT/6)))
                                  DISPLAYSURF.blit(final,(int(SCREENWIDTH/7),int(SCREENHEIGHT/4)))
                                  DISPLAYSURF.blit(score,(int(SCREENWIDTH/5.9),int(SCREENHEIGHT/2.6)))
                                  DISPLAYSURF.blit(img6,(int(SCREENWIDTH/2),int(SCREENHEIGHT/1.6))) 
                                  pygame.display.update() 
                                  print("\nThanks for Playing")
                                  while True:
                                   chest1.update()
                                   chest1.render(DISPLAYSURF)  
                                   DISPLAYSURF.blit(imgb1,(0,0))
                                   DISPLAYSURF.blit(img9,(int(SCREENWIDTH/3.9),-int(SCREENHEIGHT/6)))
                                   DISPLAYSURF.blit(final,(int(SCREENWIDTH/7),int(SCREENHEIGHT/4)))
                                   final1=myfont.render("YOU WON:",True,WHITE)
                                   if r==0:
                                      DISPLAYSURF.blit(myfont.render("Hard Luck :p",True,WHITE),(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/3.8)))    
                                      DISPLAYSURF.blit(myfont.render("Keep Guessing!!!",True,WHITE),(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/2.075)))    
                                   elif r>1000 and r<5000:
                                      DISPLAYSURF.blit(imgbronze,(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/3.3)))
                                      DISPLAYSURF.blit(myfont.render("A Bronze Trophy!!!",True,WHITE),(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/2.075)))
                                   elif r>4000 and r<9000:
                                      DISPLAYSURF.blit(imgsilver,(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/3.3)))
                                      DISPLAYSURF.blit(myfont.render("A Silver Trophy!!!",True,WHITE),(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/2.075)))
                                   else:  
                                      DISPLAYSURF.blit(imggold,(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/3.3)))
                                      DISPLAYSURF.blit(myfont.render("A Gold Trophy!!!",True,WHITE),(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/2.075)))
                                   DISPLAYSURF.blit(final1,(int(SCREENWIDTH/1.47),int(SCREENHEIGHT/4)))    
                                   DISPLAYSURF.blit(score,(int(SCREENWIDTH/5.9),int(SCREENHEIGHT/2.6)))
                                   DISPLAYSURF.blit(img6,(int(SCREENWIDTH/2),int(SCREENHEIGHT/1.6)))
                                   pygame.display.update()
                                   
                                   for event in pygame.event.get():  
                                    if event.type == QUIT:
                                     pygame.quit()
                                     sys.exit()
                                    if (event.type is KEYDOWN and event.key == K_f):
                                      if DISPLAYSURF.get_flags() & FULLSCREEN:
                                        pygame.display.set_mode(true_res,pygame.RESIZABLE)
                                      else:
                                       pygame.display.set_mode(true_res, FULLSCREEN)
                                    elif event.type == MOUSEBUTTONUP:
                                       mousex, mousey = event.pos
                                       mouseClicked = True
                                   if mouseClicked == True:
                                       if Rect(SCREENWIDTH/2,SCREENHEIGHT/1.6,int(SCREENWIDTH/9.6),int(SCREENHEIGHT/7.2)).collidepoint(mousex,mousey):  
                                           print("\n------------------PLAYING AGAIN-----------------------------------")
                                           pygame.mixer.Channel(1).stop() 
                                           s4.play()
                                           pygame.time.wait(200)
                                           starting()
                                           main(1)
                                               


class player():
    def __init__(self,x,y,images,numImages,resol,width,height,crop):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.images=images
        self.resol=resol
        self.numImages=numImages
        self.cImage=0
        self.crop=crop
    def update(self):
        if(self.cImage>=self.numImages-1):
          self.cImage=0
        else:
            self.cImage+=1
    def render(self,DISPLAYSURF):
        if self.cImage=='a':
            self.rect=(0,6*self.height,(self.width),(self.height))
            self.cropped =self.images.subsurface(self.rect)
            self.cropped=pygame.transform.scale(self.cropped,self.resol)
            DISPLAYSURF.blit(self.cropped,(self.x,self.y))
            self.cImage=self.numImages
            return
        self.rect=(0,self.cImage*self.height,(self.width),(self.height-self.crop))
        self.cropped =self.images.subsurface(self.rect)
        self.cropped=pygame.transform.scale(self.cropped,self.resol)
        DISPLAYSURF.blit(self.cropped,(self.x,self.y))
    def move(self,DISPLAYSURF):
                                   self.y-=20
                                   DISPLAYSURF.blit(self.images,(int(self.x), int(self.y)))
    def rendermiss(self,DISPLAYSURF):
        if self.cImage=='a':
            self.rect=(0,3*self.height,(self.width),(self.height))
            self.cropped =self.images.subsurface(self.rect)
            self.cropped=pygame.transform.scale(self.cropped,self.resol)
            DISPLAYSURF.blit(self.cropped,(self.x,self.y))
            self.cImage=self.numImages
            return
        self.rect=(0,self.cImage*self.height,(self.width),(self.height))
        self.cropped =self.images.subsurface(self.rect)
        self.cropped=pygame.transform.scale(self.cropped,self.resol)
        DISPLAYSURF.blit(self.cropped,(self.x,self.y))
    def updateimg2(self):
        if(self.cImage>=self.numImages-15):
          self.cImage='a'
        else:
            self.cImage+=1    
    def updatemainimg2(self):
        if(self.cImage>=self.numImages-1):
          self.cImage='a'
        else:
            self.cImage+=1        
    def renderstart(self,DISPLAYSURF):
       DISPLAYSURF.blit(self.images,(self.x,self.y),(0,self.cImage*self.height,(self.width),(self.height)))   
    def renderbanner(self,DISPLAYSURF):
      if self.y>=-int(SCREENHEIGHT/6):
        DISPLAYSURF.blit(self.images,(self.x,self.y))
        self.y-=20
      else:
          DISPLAYSURF.blit(self.images,(self.x,self.y))
    def removebanner(self,DISPLAYSURF):
       pygame.draw.rect(DISPLAYSURF,(0,0,0,0),[self.x,self.y,self.x+self.width+500,self.y+self.height+500],0)    
def starting():
    s1.set_volume(1)
    pygame.mixer.Channel(0).play(s1,loops=-1)
    global FPSCLOCK, DISPLAYSURF,myimage,r,banner1,player1,player2,chest1,FPS
    FPS=15
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('TREASURE HUNT') 
    player1=player(0,0,img1,numImages1,(SCREENWIDTH,SCREENHEIGHT),1280,720,0)
    player2=player(0,0,img2,numImages2,(SCREENWIDTH,SCREENHEIGHT),1280,720,100)
    chest1=player(0,0,img3,numImages3,(SCREENWIDTH,SCREENHEIGHT),1280,720,120)
    banner1=player(SCREENWIDTH/3.9,(int(SCREENHEIGHT/1.3)+9)//10*10,img9,0,0,int(SCREENWIDTH/2),int(SCREENHEIGHT),0)
    x=0
    while x>=-int(SCREENHEIGHT/6): #main window loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type is KEYDOWN and event.key == K_f):
                     if DISPLAYSURF.get_flags() & FULLSCREEN:
                       pygame.display.set_mode(true_res,pygame.RESIZABLE)
                     else:
                       pygame.display.set_mode(true_res, FULLSCREEN)
        chest1.update()
        chest1.render(DISPLAYSURF)   
        DISPLAYSURF.blit(imgd1,(0,0))
        banner1.renderbanner(DISPLAYSURF)
        x=getattr(banner1,'y')
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    start1=player(SCREENWIDTH/2.1,SCREENHEIGHT/1.7,img5,numImages5,0,int(SCREENWIDTH/11.75),int(SCREENHEIGHT/20),0)
    q=True
    while q: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type is KEYDOWN and event.key == K_f):
                     if DISPLAYSURF.get_flags() & FULLSCREEN:
                       pygame.display.set_mode(true_res,pygame.RESIZABLE)
                     else:
                       pygame.display.set_mode(true_res, FULLSCREEN)

            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True  
                if mouseClicked == True :
                     if Rect(SCREENWIDTH/2.1,SCREENHEIGHT/1.7,int(SCREENWIDTH/11.75),int(SCREENHEIGHT/9.9)).collidepoint(mousex,mousey):
                         x=0
                         s4.play()
                         pygame.time.wait(200)
                         imgd1.set_alpha(30)
                         while x!=28:
                          if x==5:
                             pygame.mixer.fadeout(3000)
                          player2.updatemainimg2()
                          player2.render(DISPLAYSURF)
                          DISPLAYSURF.blit(imgd1,(0,0))
                          x=getattr(player2,'cImage')
                          pygame.display.update()
                          FPSCLOCK.tick(FPS)
                          if x==16:
                              s2.play(-1,0,1000)
                         main(1)
                         q=False
        chest1.update()
        chest1.render(DISPLAYSURF) 
        DISPLAYSURF.blit(imgd1,(0,0)) 
        banner1.renderbanner(DISPLAYSURF)    
        start1.update()        
        start1.renderstart(DISPLAYSURF) 
        x=getattr(banner1,'y')
        pygame.display.update()
        FPSCLOCK.tick(FPS)
def main(i): 
    s2.set_volume(1)
    global myfont,mouseClicked,a,o
    pygame.font.init()
    myfont=pygame.font.SysFont('Comic Sans MS',int(SCREENWIDTH/60))
    textsurface=myfont.render('ROUND %s'%i,True,WHITE)
    FPSCLOCK = pygame.time.Clock()
    mouseClicked = False
    mousex = 0
    mousey = 0
    global r,mc
    mc=0
    
    currentGrid = initiateCells()
    o=[]
    a=box(i)
    if i==1:
     r=0   
     DISPLAYSURF.fill(BLACK)  
     chest1.update()
     chest1.render(DISPLAYSURF)  
     DISPLAYSURF.blit(imgb1,(0,0))
     DISPLAYSURF.blit(img9,(int(SCREENWIDTH/3.9),-int(SCREENHEIGHT/6)))
     DISPLAYSURF.blit(img7,(int(SCREENWIDTH/5.65),int(SCREENHEIGHT/2.45)))
     DISPLAYSURF.blit(img8,(int(SCREENWIDTH/1.4),int(SCREENHEIGHT/2.45)))
    else:
     DISPLAYSURF.fill(BLACK)  
     chest1.update()
     chest1.render(DISPLAYSURF)  
     DISPLAYSURF.blit(imgb1,(0,0))
     NETSCORE= myfont.render("NET SCORE: %s"%r,True,WHITE)
     DISPLAYSURF.blit(NETSCORE,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/9)))
     DISPLAYSURF.blit(img11,(int(SCREENWIDTH/5.64),int(SCREENHEIGHT/2.45)))
    while True: #main game loop
        if i==1:
         DISPLAYSURF.fill(BLACK)   
         chest1.update()
         chest1.render(DISPLAYSURF)  
         DISPLAYSURF.blit(imgb1,(0,0))
         DISPLAYSURF.blit(img9,(int(SCREENWIDTH/3.9),-int(SCREENHEIGHT/6)))
         DISPLAYSURF.blit(img7,(int(SCREENWIDTH/5.65),int(SCREENHEIGHT/2.45)))
         DISPLAYSURF.blit(img8,(int(SCREENWIDTH/1.4),int(SCREENHEIGHT/2.45)))
        else:
            DISPLAYSURF.fill(BLACK)
            chest1.update()
            chest1.render(DISPLAYSURF)  
            DISPLAYSURF.blit(imgb1,(0,0))
            DISPLAYSURF.blit(img9,(int(SCREENWIDTH/3.9),-int(SCREENHEIGHT/6)))
            NETSCORE= myfont.render("NET SCORE: %s"%r,True,WHITE)
            DISPLAYSURF.blit(NETSCORE,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/9)))
            DISPLAYSURF.blit(img11,(int(SCREENWIDTH/5.64),int(SCREENHEIGHT/2.45)))
        for event in pygame.event.get():
            if i==1:
              DISPLAYSURF.blit(img9,(int(SCREENWIDTH/3.9),-int(SCREENHEIGHT/6)))
              DISPLAYSURF.blit(img7,(int(SCREENWIDTH/5.65),int(SCREENHEIGHT/2.45)))
              DISPLAYSURF.blit(img8,(int(SCREENWIDTH/1.4),int(SCREENHEIGHT/2.45)))
            else:
              
              DISPLAYSURF.blit(img9,(int(SCREENWIDTH/3.9),-int(SCREENHEIGHT/6)))
              NETSCORE= myfont.render("NET SCORE: %s"%r,True,WHITE)
              DISPLAYSURF.blit(NETSCORE,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/9)))
              DISPLAYSURF.blit(img11,(int(SCREENWIDTH/5.64),int(SCREENHEIGHT/2.45)))
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type is KEYDOWN and event.key == K_f):
                     if DISPLAYSURF.get_flags() & FULLSCREEN:
                       pygame.display.set_mode(true_res,pygame.RESIZABLE)
                     else:
                       pygame.display.set_mode(true_res, FULLSCREEN)
            elif event.type==pygame.KEYDOWN:
                if event.key==K_4:
                        print("\n------------------PLAYING AGAIN-----------------------------------")
                        pygame.mixer.Channel(1).stop()  
                        starting()
                        main(1) 
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        if mouseClicked == True:
            if Rect(int(SCREENWIDTH/5.64),int(SCREENHEIGHT/2.45),int(SCREENWIDTH/9.6),int(SCREENHEIGHT/10.8)).collidepoint(mousex,mousey):
             s3.stop()
             s4.stop()
             s5.stop()
             s4.play()
             DISPLAYSURF.fill(BLACK) 
             DISPLAYSURF.blit(imgc1,(0,0))
             if i==1:
               DISPLAYSURF.blit(img12,(int(SCREENWIDTH/5),int(SCREENHEIGHT/6)))
             if i==2:
               DISPLAYSURF.blit(img13,(int(SCREENWIDTH/5),int(SCREENHEIGHT/6)))
               DISPLAYSURF.blit(img131,(int(SCREENWIDTH/3.3),int(SCREENHEIGHT/6.8)))
             if i==3:
                 DISPLAYSURF.blit(img14,(int(SCREENWIDTH/5),int(SCREENHEIGHT/6)))
             pygame.display.update()
             pygame.time.delay(2000)
             player1.update()
             player1.render(DISPLAYSURF) 
             DISPLAYSURF.blit(imgB,(0,0))
             displaycells(currentGrid)
             drawGrid()
             chance= myfont.render("You have %s Chances left"%(1+2*i+5-mc),True,WHITE)
             DISPLAYSURF.blit(chance,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/60)))
             treasure= myfont.render("You have %s Treasures left"%(len(a)-len(o)),True,WHITE)
             DISPLAYSURF.blit(treasure,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/1.85)))
             NETSCORE= myfont.render("NET SCORE: %s"%r,True,WHITE)
             DISPLAYSURF.blit(NETSCORE,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/9)))
             while True: #main game loop
                  player1.update()
                  player1.render(DISPLAYSURF)
                  DISPLAYSURF.blit(imgB,(0,0))
                  displaycells(currentGrid)
                  drawGrid()
                  chance= myfont.render("You have %s Chances left"%(1+2*i+5-mc),True,WHITE)
                  DISPLAYSURF.blit(chance,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/60)))
                  treasure= myfont.render("You have %s Treasures left"%(len(a)-len(o)),True,WHITE)
                  DISPLAYSURF.blit(treasure,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/1.85)))
                  NETSCORE= myfont.render("NET SCORE: %s"%r,True,WHITE)
                  DISPLAYSURF.blit(NETSCORE,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/9)))
                  for event in pygame.event.get():
                    if event.type == QUIT:
                      pygame.quit()
                      sys.exit()
                    if (event.type is KEYDOWN and event.key == K_f):
                     if DISPLAYSURF.get_flags() & FULLSCREEN:
                       pygame.display.set_mode(true_res,pygame.RESIZABLE)
                     else:
                       pygame.display.set_mode(true_res, FULLSCREEN)
                    elif event.type==pygame.KEYDOWN:
                     if event.key==K_2:
                        print("\n------------------Returning To Round 1-----------------------------------")
                        main(1) 
                     elif event.key==K_3:
                        print("\n------------------Starting Round Again-----------------------------------") 
                        r=r-1000*len(o) 
                        main(i)   
                     elif event.key==K_4:
                        print("\n------------------PLAYING AGAIN-----------------------------------")
                        pygame.mixer.Channel(1).stop()    
                        starting()
                        main(1)    
                    elif event.type==MOUSEBUTTONUP: 
                     mousex, mousey = event.pos
                     mouseClicked = True   
                     if mouseClicked == True:
                      if Rect(shiftx,shifty,WINDOWWIDTH,WINDOWHEIGHT).collidepoint(mousex,mousey):
                        for dtem in o:
                           if Rect((dtem[1])*SQUARESIZE+shiftx,(dtem[0])*SQUARESIZE+shifty,SQUARESIZE,SQUARESIZE).collidepoint(mousex,mousey):
                               s3.stop()
                               s4.stop()
                               s5.stop()
                               s5.play()
                               player5=player((dtem[1])*SQUARESIZE+shiftx,(dtem[0])*SQUARESIZE+shifty,img2,3,(SQUARESIZE,SQUARESIZE),1280,720,0)
                               while True:
                                  displaycells(currentGrid)
                                  drawGrid()   
                                  player5.updatemainimg2()
                                  player5.rendermiss(DISPLAYSURF)
                                  pygame.display.update()
                                  if getattr(player5,'cImage')==2:
                                   DISPLAYSURF.blit(img0,((dtem[1])*SQUARESIZE+shiftx,(dtem[0])*SQUARESIZE+shifty))
                                   break
                               mc-=1
                               done= myfont.render("ALREADY COLLECTED!!!!",True,WHITE)
                               DISPLAYSURF.blit(imgB,(0,0))
                               displaycells(currentGrid)
                               drawGrid()
                               DISPLAYSURF.blit(done,(SCREENWIDTH/1.5,SCREENHEIGHT/4))
                               pygame.display.update()
                               pygame.time.wait(200)
                               break
                        mc+=1 
                        chance= myfont.render("You have %s Chances left"%(1+2*i+5-mc),True,WHITE)
                        DISPLAYSURF.blit(chance,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/60)))
                        treasure= myfont.render("You have %s Treasures left"%(len(a)-len(o)),True,WHITE)
                        DISPLAYSURF.blit(treasure,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/1.85)))
                        NETSCORE= myfont.render("NET SCORE: %s"%r,True,WHITE)
                        DISPLAYSURF.blit(NETSCORE,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/9)))
                      for item in currentGrid:
                       if item not in a:
                            if Rect((item[1])*SQUARESIZE+shiftx,(item[0])*SQUARESIZE+shifty,SQUARESIZE,SQUARESIZE).collidepoint(mousex,mousey):
                               s3.stop()
                               s4.stop()
                               s5.stop()
                               s5.play()
                               player4=player((item[1])*SQUARESIZE+shiftx,(item[0])*SQUARESIZE+shifty,img2,3,(SQUARESIZE,SQUARESIZE),1280,720,0)
                               while True:
                                  displaycells(currentGrid)
                                  drawGrid()   
                                  player4.updatemainimg2()
                                  player4.rendermiss(DISPLAYSURF)
                                  pygame.display.update()
                                  if getattr(player4,'cImage')==2:
                                   DISPLAYSURF.blit(img0,((item[1])*SQUARESIZE+shiftx,(item[0])*SQUARESIZE+shifty))
                                   break
                               done= myfont.render("YOU MISSED IT!!!!",True,WHITE)
                               DISPLAYSURF.blit(imgB,(0,0))
                               displaycells(currentGrid)
                               drawGrid()
                               DISPLAYSURF.blit(done,(SCREENWIDTH/1.5,SCREENHEIGHT/4))
                               pygame.display.update()
                               pygame.time.wait(200)
                               DISPLAYSURF.blit(imgB,(0,0))
                               displaycells(currentGrid)
                               drawGrid()
                               chance= myfont.render("You have %s Chances left"%(1+2*i+5-mc),True,WHITE)
                               DISPLAYSURF.blit(chance,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/60)))
                               treasure= myfont.render("You have %s Treasures left"%(len(a)-len(o)),True,WHITE)
                               DISPLAYSURF.blit(treasure,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/1.85)))
                               NETSCORE= myfont.render("NET SCORE: %s"%r,True,WHITE)
                               DISPLAYSURF.blit(NETSCORE,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/9)))
                               if 1+2*i+5-mc==0:
                                 end(i,mouseClicked,mousex,mousey)
                       for p in a:
                        if p==item: 
                         if Rect((item[1])*SQUARESIZE+shiftx,(item[0])*SQUARESIZE+shifty,SQUARESIZE,SQUARESIZE).collidepoint(mousex,mousey) and (item[0],item[1]) not in o:
                          s3.stop()
                          s4.stop()
                          s5.stop()
                          s3.play()
                          player3=player((item[1])*SQUARESIZE+shiftx,(item[0])*SQUARESIZE+shifty,img2,numImages2,(SQUARESIZE,SQUARESIZE),1280,720,0)
                          player6=player((item[1])*SQUARESIZE+shiftx,(item[0])*SQUARESIZE+shifty,img4,0,(SQUARESIZE,SQUARESIZE),1875,2000,0)
                          while True:
                           displaycells(currentGrid)
                           drawGrid()   
                           player3.updateimg2()
                           player3.render(DISPLAYSURF)
                           pygame.time.wait(100)
                           pygame.display.update()
                           if getattr(player3,'cImage')==12:
                               while (int(getattr(player6,'x')),int(getattr(player6,'y')))>=(int(getattr(player6,'x')),-20):
                                  
                                  displaycells(currentGrid)
                                  drawGrid()   
                                  player3.updateimg2()
                                  player3.render(DISPLAYSURF)
                                  player6.move(DISPLAYSURF)
                                  pygame.display.update()
                               break   
                          displaycells(currentGrid)
                          drawGrid() 
                          o.append((item[0],item[1]))
                          r=r+1000
                          pygame.display.update()
                          DISPLAYSURF.blit(imgB,(0,0)) 
                          displaycells(currentGrid)
                          drawGrid()
                          chance= myfont.render("You have %s Chances left"%(1+2*i+5-mc),True,WHITE)
                          DISPLAYSURF.blit(chance,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/60)))
                          treasure= myfont.render("You have %s Treasures left"%(len(a)-len(o)),True,WHITE)
                          DISPLAYSURF.blit(treasure,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/1.85)))
                          NETSCORE= myfont.render("NET SCORE: %s"%r,True,WHITE)
                          DISPLAYSURF.blit(NETSCORE,(int(SCREENWIDTH/1.5),int(SCREENHEIGHT/9)))
                          pygame.display.update()
                          c=equal(o,a)
                          if c==len(a) or 1+2*i+5-mc==0:
                             end(i,mouseClicked,mousex,mousey)
                  pygame.display.update()
                  FPSCLOCK.tick(FPS) 
            elif Rect(int(SCREENWIDTH/1.4),int(SCREENHEIGHT/2.45),int(SCREENWIDTH/12.8),int(SCREENHEIGHT/10.8)).collidepoint(mousex,mousey) and i==1:
                s4.stop()
                s3.stop()
                s5.stop()
                s4.play()
                DISPLAYSURF.fill(BLACK)
                DISPLAYSURF.blit(img01,(0,0))
                while True:
                  DISPLAYSURF.fill(BLACK)
                  DISPLAYSURF.blit(img01,(0,0))
                  INST=myfont.render("INSTRUCTIONS",True,WHITE)
                  INST0=myfont.render("1.Treasure Hunt Game",True,WHITE)
                  INST1=myfont.render("2.Total 3 Rounds",True,WHITE)
                  INST2=myfont.render("3.Collect treasure by guessing randomly over the Board",True,WHITE)      
                  INST3=myfont.render("4.Press 2 to get to Round 1 during a game",True,WHITE)
                  INST4=myfont.render("5.Press 3 to get to Previous Round during a game",True,WHITE)
                  INST5=myfont.render("6.Press 4 to get to Starting Screen during a game",True,WHITE)
                  INST6=myfont.render("7.FINAL SCORE is given on the basis of NET SCORE calculated after each round",True,WHITE)
                  INST7=myfont.render("8.Press F to toggle Fullscreen",True,WHITE)
                  DISPLAYSURF.blit(INST,(int(SCREENWIDTH/3),int(SCREENHEIGHT/20)))    
                  DISPLAYSURF.blit(INST0,(int(SCREENWIDTH/8),int(SCREENHEIGHT/6)))                   
                  DISPLAYSURF.blit(INST1,(int(SCREENWIDTH/8),int(SCREENHEIGHT/4.9))) 
                  DISPLAYSURF.blit(INST2,(int(SCREENWIDTH/8),int(SCREENHEIGHT/4.15))) 
                  DISPLAYSURF.blit(INST3,(int(SCREENWIDTH/8),int(SCREENHEIGHT/3.6)))
                  DISPLAYSURF.blit(INST4,(int(SCREENWIDTH/8),int(SCREENHEIGHT/3.17)))  
                  DISPLAYSURF.blit(INST5,(int(SCREENWIDTH/8),int(SCREENHEIGHT/2.84)))
                  DISPLAYSURF.blit(INST6,(int(SCREENWIDTH/8),int(SCREENHEIGHT/2.57))) 
                  DISPLAYSURF.blit(INST7,(int(SCREENWIDTH/8),int(SCREENHEIGHT/2.346)))    
                  DISPLAYSURF.blit(img10,(int(SCREENWIDTH/8),int(SCREENHEIGHT/2)))
                  for event in pygame.event.get():
                    if event.type == QUIT:
                      pygame.quit()
                      sys.exit()
                    if (event.type is KEYDOWN and event.key == K_f):
                     if DISPLAYSURF.get_flags() & FULLSCREEN:
                       pygame.display.set_mode(true_res,pygame.RESIZABLE)
                     else:
                       pygame.display.set_mode(true_res, FULLSCREEN)
                    elif event.type == MOUSEBUTTONUP:
                      mousex, mousey = event.pos
                      mouseClicked = True
                    elif event.type== pygame.KEYDOWN:
                        main(1)
                        break
                  if mouseClicked == True:
                       if Rect(int(SCREENWIDTH/8),int(SCREENHEIGHT/2),int(SCREENWIDTH/12.8),int(SCREENHEIGHT/10.8)).collidepoint(mousex,mousey):
                        s4.stop()
                        s3.stop()
                        s5.stop()
                        s4.play()
                        main(1)  
                  pygame.display.update()
                  FPSCLOCK.tick(FPS)  
        pygame.display.update()
        FPSCLOCK.tick(FPS)
if __name__=='__main__':
    starting()        
if __name__=='__main__':
    main(i)        

