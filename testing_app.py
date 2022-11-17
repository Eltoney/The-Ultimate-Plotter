import pytest

import plotterApp
from PySide2.QtWidgets import (
    QMainWindow, QApplication, QWidget, QGridLayout, QPushButton,
    QLineEdit, QLabel, QMessageBox)
from PySide2.QtCore import Qt, QSize

import sys


@pytest.fixture
def app(qtbot):
    test_plotter_app = plotterApp.MainWindow()
    qtbot.addWidget(test_plotter_app)
    return test_plotter_app

def test_func_label(app):
    assert app.func_label.text() == 'Function: '


def test_min_label(app):
    assert app.min_label.text() == 'Min x value: '


def test_max_label(app):
    assert app.max_label.text() == 'Max x value: '


def test_func_input(app):
    assert app.func_input.placeholderText() == 'Enter Your f(x) here'


def test_min_input(app):
    assert app.min_input.placeholderText() == 'lowest x'


def test_max_input(app):
    assert app.max_input.placeholderText() == 'highest x'
