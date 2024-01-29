import matplotlib.pyplot as pyplot
import matplotlib.animation as animation

fig = pyplot.figure()
ax1 = fig.add_subplot(1,1,1)

def refreshInputData(i):
    print('Refreshing data...')
    X = []
    Y = []
    grapData = open("../../FileSamples/dynamic.txt", "r").read()
    datas = grapData.split('\n')

    for data in datas:
        if len(data) > 1:
            x, y = data.split(",")
            X.append(x)
            Y.append(y)
    ax1.clear()
    ax1.plot(X,Y)

ani = animation.FuncAnimation(fig, refreshInputData,interval=1000)
pyplot.show()
