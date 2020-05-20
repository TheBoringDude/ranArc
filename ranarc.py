import sys, threading
import webview
from PySide2.QtWidgets import QApplication, QMainWindow
from base import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.btnFindArticle.clicked.connect(self.Initialize)
        
    def Initialize(self):
        t = threading.Thread(target=self.FIND_ARTICLE)
        t.daemon = True
        t.start()

    def FIND_ARTICLE(self):
        # To pass custom settings to CEF, import and update settings dict
        from webview.platforms.cef import settings
        settings.update({
            'persist_session_cookies': True,
        })
        webview.create_window('CEF Example', 'https://en.wikipedia.org/wiki/Special:Random')
        webview.start(gui='cef')

if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())