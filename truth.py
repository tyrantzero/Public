
import stddraw
import color

t=str(input("Wählen Sie einen Text: "))

stddraw.setCanvasSize(1000,500)
stddraw.setYscale(0,10)
stddraw.setXscale(0,10)

AlleNonnenSindLesben = True

r=0
g=0
b=0

rup=True
gub=True
bup=True

while AlleNonnenSindLesben == True:
    stddraw.setPenColor(color.Color(0,0,0))
    stddraw.filledRectangle(0,0,10,10)
    stddraw.setFontSize(90)

    stddraw.setPenColor(color.Color(r,g,b))

    if r==255: rup=False
    if rup==True and gub==True and bup==True:r+=5

    if g==255: gub=False
    if rup==False and gub==True and bup==True:g+=5

    if b==255: bup=False
    if rup==False and gub==False and bup==True:b+=5

    if r == 0: rup = True
    if rup == False and gub == False and bup == False: r -= 5

    if g == 0: gub = True
    if rup == True and gub == False and bup == False: g -= 5

    if b == 0: bup = True
    if rup == True and gub == True and bup == False: b -= 5


    stddraw.rectangle(0.7,3,8.6,4)
    stddraw.text(5,5,t)
    stddraw.show(4)
