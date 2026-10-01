import matplotlib.pyplot as mp
x=["Tuesday", "Wednesday","Thursday" ]
y=[3,5,3]
y1=[1,2,3]
#mp.plot(x,y)
mp.title("class details")
mp.plot(x,y1)
mp.xlabel("weekdays")
mp.ylabel("classes")
mp.plot(x,y,marker='o',linestyle='-',label="data points")
mp.legend()
mp.grid(True)
mp.show()