from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QScreen
#from controllers.main_window import MainWindow
from controllers.main import MainWindow
        
def center_window( window):
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = window.frameGeometry()
        geo.moveCenter(center)
        window.move(geo.topLeft())

if __name__ == "__main__":
    app = QApplication()
    #app.setWindowIcon(QtGui.QIcon(os.path.join(ruta_principal(), "resources", "app_icon" ,"app-logo-hotel.ico")))
    window = MainWindow()
    window.show()
    #center_window(window)
    app.exec()
