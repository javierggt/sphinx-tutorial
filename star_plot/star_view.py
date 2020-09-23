from PyQt5 import QtCore as QtC, QtWidgets as QtW, QtGui as QtG

from .utils import get_stars


class StarView(QtW.QGraphicsView):
    def __init__(self, scene=None):
        super().__init__(scene)

        self._start = None
        self._moving = False
        b1hw = 512.
        self.fov = self.scene().addRect(-b1hw, -b1hw, 2 * b1hw, 2 * b1hw)

    def mouseMoveEvent(self, event):
        pos = event.pos()
        if self._start is None:
            return

        if pos != self._start:
            self._moving = True

        if self._moving:
            end_pos = self.mapToScene(pos)
            start_pos = self.mapToScene(self._start)
            dx, dy = end_pos.x() - start_pos.x(), end_pos.y() - start_pos.y()

            scene_rect = self.scene().sceneRect()
            new_scene_rect = QtC.QRectF(scene_rect.x() - dx, scene_rect.y() - dy,
                                        scene_rect.width(), scene_rect.height())
            self.scene().setSceneRect(new_scene_rect)
            self._start = pos

    def mouseReleaseEvent(self, event):
        self._start = None

    def mousePressEvent(self, event):
        self._moving = False
        self._start = event.pos()

    def wheelEvent(self, event):
        scale = 1 + 0.5 * event.angleDelta().y() / 360
        self.scale(scale, scale)

    def drawForeground(self, painter, rect):
        black_pen = QtG.QPen()
        black_pen.setWidth(2)
        b1hw = 512.
        center = QtC.QPoint(self.viewport().width() / 2, self.viewport().height() / 2)
        center = self.mapToScene(center)
        painter.drawRect(center.x() - b1hw, center.y() - b1hw, 2 * b1hw, 2 * b1hw)
        b2w = 520
        painter.drawRect(center.x() - b2w, center.y() - b1hw, 2 * b2w, 2 * b1hw)
        painter.setPen(QtG.QPen(QtG.QColor('magenta')))
        painter.drawLine(center.x() - 511, center.y(), center.x() + 511, center.y())
        painter.drawLine(center.x(), center.y() - 511, center.x(), center.y() + 511)

