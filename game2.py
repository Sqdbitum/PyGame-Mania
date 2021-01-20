def menu():
    import sys
    from PyQt5 import uic
    from PyQt5.QtWidgets import QApplication, QMainWindow
    music = ["Philip Glass - Candyman.wav", "Portal - Still Alive.wav", "Smash Mouth - All Star.wav",
             "Smash Mouth - I'm A Believer.wav"]
    # a = False
    lvls = ['Too easy', 'Easy', 'Hard', 'Insane', 'Extra']

    fi = open('fal.txt', 'w+')
    u = False
    class MyWidget(QMainWindow):
        def __init__(self):
            self.a = False
            self.b = False
            super().__init__()

            uic.loadUi('proektmenu.ui', self)
            self.pushButton.clicked.connect(self.music)
            self.comboBox.addItems(lvls)
            self.comboBox_2.addItems(music)
            self.comboBox.activated[str].connect(self.lvl)
            self.comboBox_2.activated[str].connect(self.song)

        def song(self, sn):
            self.b = True
            self.sn = sn

        def lvl(self, lv):
            self.a = True
            self.lv = lv

        def music(self):
            if self.b != True:
                self.sn = "Philip Glass - Candyman.wav"
            fi.write('music\\' + self.sn + '\n')
            if self.a != True:
                self.lv = 'Too easy'
            fi.write(self.lv + '\n')
            fi.close()
            print(5676)
            exit()



    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

menu()