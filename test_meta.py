from PySide6.QtWidgets import QWidget, QMainWindow
from abc import ABC, ABCMeta

class QABCMeta(type(QWidget), ABCMeta):
    pass

class MyABC(ABC):
    pass

class MyWindow(QMainWindow, MyABC, metaclass=QABCMeta):
    pass

print("Success Window")
