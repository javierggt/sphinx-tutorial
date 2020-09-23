#!/usr/bin/env python

import sys

from PyQt5 import QtWidgets as QtW

from star_plot import StarPlot


def main():
    app = QtW.QApplication(sys.argv)
    w = StarPlot()
    w.resize(800, 600)
    w.show()
    app.exec()


if __name__ == '__main__':
    main()
