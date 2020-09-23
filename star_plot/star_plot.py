import numpy as np
from PyQt5 import QtCore as QtC, QtWidgets as QtW, QtGui as QtG

from Quaternion import Quat
from Chandra.Time import DateTime

from .utils import get_stars
from .star_view import StarView


GLOBAL_VARIABLE = None


def _symsize(mag):
    # map mags to figsizes, defining
    # mag 6 as 40 and mag 11 as 3
    # interp should leave it at the bounding value outside
    # the range
    return np.interp(mag, [6.0, 11.0], [40.0, 3.0])


class StarPlot(QtW.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QtW.QVBoxLayout(self)
        self.setLayout(layout)

        self.scene = QtW.QGraphicsScene(self)
        self.scene.setSceneRect(-100, -100, 200, 200)
        self.view = StarView(self.scene)
        self.layout().addWidget(self.view)

        self.view.scale(0.5, 0.5)
        quaternion = Quat(q=[-0.474674, -0.473931, 0.262471, 0.693674])
        starcat_time = DateTime('2020:001:19:18:21.914')
        self.show_stars(starcat_time, quaternion)

    def show_stars(self, starcat_time, quaternion):
        self.scene.clear()
        self.stars = get_stars(starcat_time, quaternion)
        black_pen = QtG.QPen()
        black_pen.setWidth(2)
        black_brush = QtG.QBrush(QtG.QColor("black"))
        red_pen = QtG.QPen(QtG.QColor("red"))
        red_brush = QtG.QBrush(QtG.QColor("red"))
        for star in self.stars:
            s = _symsize(star['MAG'])
            rect = QtC.QRectF(star['row'] - s/2, -star['col'] - s/2, s, s)
            # this hardcoded list would come from the commanded star catalog. Cheating...
            if star['AGASC_ID'] in [237774392, 237776560, 237899472, 237899816, 237900784,
                                    238420640, 238421128, 238300048, 237897848]:
                self.scene.addEllipse(rect, red_pen, red_brush)
            else:
                self.scene.addEllipse(rect, black_pen, black_brush)

