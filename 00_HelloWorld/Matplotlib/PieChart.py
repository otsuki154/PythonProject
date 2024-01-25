import matplotlib.pyplot as pyplot

mobileBranches = ["Apple", "Samsung", "Xiaomi", "LG"]
slice = [30,30,25,15]
color = ["brown", "gray","green","yellow"]
explode = [0.1, 0, 0, 0] #tach phan pie muon roi ra
pyplot.pie(slice,
    labels=mobileBranches,
    colors=color,
    explode=explode,
    startangle=0,
    autopct="%1.1f%%"
)
pyplot.title("Pie char example \nHope you enjoy!")
pyplot.show()
