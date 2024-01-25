import matplotlib.pyplot as pyplot

x1Values = [1,3,5,7,9]
y1Values = [4,5,6,7,12]
pyplot.bar(x1Values,y1Values,label="This is bar1", width=0.4, color="green")

x2Values = [2,4,6,8,10]
y2Values = [2,3,4,5,10]
pyplot.bar(x2Values,y2Values,label="This is bar2",width=0.4,color="violet")

pyplot.xlabel("X Axis")
pyplot.ylabel("Y Axis")
pyplot.title("Bar char example \nHope you enjoy!")
pyplot.legend()
pyplot.show()