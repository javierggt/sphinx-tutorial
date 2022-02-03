#!/usr/bin/env python
"""
Plot the star field at a given time and around a given attitude
"""

import sys
import argparse

from PyQt5 import QtWidgets as QtW

from star_plot import StarPlot


def parser():
    """
    Returns an argparse.ArgumentParser instance.
    """
    parse = argparse.ArgumentParser(description=__doc__)
    parse.add_argument('--obsid', help='OBSID')
    parse.add_argument('--date', help='Date in any CxcTime-compatible format')
    return parse


def main():
    """
    Run the script
    """
    args = parser().parse_args()

    app = QtW.QApplication(sys.argv)
    w = StarPlot()
    w.resize(800, 600)
    w.show()
    app.exec()


if __name__ == '__main__':
    main()
