from turtle import  *
tracer(0)
screensize(5000,5000)
k = 20
left(90)

for i in range(14):
    for j in range(3):
        forward(3*k)
        right(90)
    left(180)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k,y*k)
        dot(3)
goto(0,0)
dot(5,'red')
done()
