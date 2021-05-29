#Importing the turtle module 
import turtle 
x = turtle.Turtle()
x.speed(4)
#Defining Variables
factor = 3
terms = 13

#Pen thickness
x.pensize(factor-1)

#Function that returns a list containing the fibbonachi sequence
def fibonachi_generator(num):

    mylist = []
    a = 1
    b = 1
        
    for num in range(num):
        mylist.extend([a])
        new_sum = a + b
        a = int(b)
        b = new_sum
    return mylist

#Saving the function result
mylist = fibonachi_generator(terms)
print(mylist)
print(len(mylist))

#Changing Sate of turtle and defining position
x.penup()
x.setposition(-200,-350)

#Printing the Fibonachi Sequence 
x.write(f"Fibonachi Sequence: {mylist}")

#Function that draws a sqaure
def draw_square(length):
    for i in range(4):
        x.forward(length)
        x.right(90)
        

#Redifining starting point of turtle
x.setposition(50,-100)
x.pendown()

#iterating through the fibbonachi sequence while drawing corresponding squares.
for i in range(len(mylist)):
    draw_square(factor*mylist[i])
    x.penup()
    x.forward(factor*mylist[i])
    x.right(90)
    x.forward(factor*mylist[i])
    x.pendown()

#Setting Tutrle up for drawing the Spiral    
x.penup()
x.setposition(50,-100)
#Face the turtle to the right
x.setheading(0)
x.pendown()
x.pencolor("#ed0c22")
x.pensize(factor)

#Drawing the spiral by iterating through list
for j in range(len(mylist)):
    x.circle(-1*factor*mylist[j],90)

#Keeps screen open until user closes window
x.getscreen()._root.mainloop()

