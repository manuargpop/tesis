from PyQt6.QtWidgets import * 
import sys
import pyqtgraph as pg
 
 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("grafica nojodaaaaaaa!!!")
 
        # setting geometry
        self.setGeometry(100, 100, 600, 500)
 
        # calling method
        self.UiComponents()
 
        # showing all the widgets
        self.show()
 
    # method for components
    def UiComponents(self):
 
        # creating a widget object
        widget = QWidget()
 
        # creating a plot window
        plot = pg.plot()
 
        # datos de entrada para hacer grafica
        y1 = [76,0]
        y2 = [0,64]
        xlab = ['CITA 1', 'CITA 2']
        xval = list(range(1,len(xlab)+1))
        print(xval)

        ticks=[]
        for i, item in enumerate(xlab):
            ticks.append( (xval[i], item) )
        ticks = [ticks]

        bargraph = pg.BarGraphItem(x=xval, height=y1, width=0.5, brush ='#1f78b4')
        plot.addItem(bargraph)
        bargraph2 = pg.BarGraphItem(x=xval, height=y2, width=0.5, brush ="#fe7f0e") 
        plot.addItem(bargraph2)

        plot.setBackground("w")
        ax = plot.getAxis('bottom')
        ax.setTicks(ticks)
 
        # Creating a grid layout
        layout = QGridLayout()
 
        # setting this layout to the widget
        widget.setLayout(layout)

 
        # plot window goes on right side, spanning 3 rows
        layout.addWidget(plot, 0, 1, 1)
 
        # setting this widget as central widget of the main window
        self.setCentralWidget(widget)
 
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())