import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtTest import *
from PyQt5 import uic

class QPushButtonUpload(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setFixedHeight(80)
        self.setFixedWidth(80)
        self.setIconSize(QSize(72, 72))

class QPushButtonIcon(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedHeight(45)
        self.setFixedWidth(45)
        self.setIconSize(QSize(41,41))
        
class champion_layout(QGridLayout):
    def __init__(self, parent = None):

        super().__init__(parent)
        self.setFixedHeight(45)
        self.setFixedWidth(45)
        self.setIconSize(QSize(80,80))
        

class QPushButtonReset(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedHeight(50)
        font = QFont("Helvetica", 12)
        font.setBold(True)
        self.setFont(font)


class Main(QDialog):
    
    def __init__(self):
        super().__init__()
        self.set_champions()
        self.init_ui()
        self.set_style()
        

    
    def set_champions(self):
        self.selection_list = []
        
        self.figures = ["Aatrox.png","Anivia.png","AoShin.png","Ashe.png","AurelionSol.png","Bard.png",
                     "Braum.png","Corki.png","Daeja.png","Diana.png","Elise.png","Ezreal.png","Gnar.png",
                     "Hecarim.png","Heimerdinger.png","Idas.png","Illaoi.png","Jinx.png","Karma.png",
                     "Kayn.png","Leesin.png","Leona.png","Lillia.png","Lulu.png","Nami.png","Neeko.png",
                     "Nidalee.png","Nunu.png","Olaf.png","Ornn.png","Pyke.png","Qiyana.png","Ryze.png",
                     "Sejuani.png","Senna.png","Sett.png","Shen.png","ShiOhYu.png","Shyvana.png",
                     "Skarner.png","Sona.png","Soraka.png","Swain.png","Syfen.png","Sylas.png",
                     "TahmKench.png","Talon.png","Taric.png","Thresh.png","Tristana.png",
                     "Twitch.png","Varus.png","Vladimir.png","Volibear.png","Xayah.png",
                     "Yasuo.png","Yone.png","Zoe.png"]
        self.icons = {}
        self.icons_for_index = {}
        
        for index, filename in enumerate(self.figures):
            pixmap = QPixmap(f"image\champions\select\{filename}")
            pixmap = pixmap.scaled(45, 45, Qt.IgnoreAspectRatio)
            pixmap_for_index = pixmap.scaled(80, 80, Qt.IgnoreAspectRatio)            
            icon = QIcon()
            icon_for_index=QIcon()
            icon.addPixmap(pixmap)
            icon_for_index.addPixmap(pixmap_for_index)
            
            self.icons[index] = icon
            self.icons_for_index[index] = icon_for_index
            



 
            
    def set_style(self):
        with open("style", 'r') as f:
            self.setStyleSheet(f.read())


    def init_ui(self):
        self.setWindowTitle('lolchess')
        
        main_layout = QVBoxLayout()
        
        champion_layout = QGridLayout()
        select_layout = QHBoxLayout()
        suggest_layout = QHBoxLayout()
        
        self.pbuttons = {}
        
        for index in range(10):
            button = QPushButtonUpload()
            self.pbuttons[index] = button
            button.clicked.connect(lambda state ,index = index : self.pbutton_clicked(self,index))
            select_layout.addWidget(button,index)
           
        
        for index in range(10):
            button = QPushButtonUpload()
            button.clicked.connect(lambda state, button = button, idx = index:
                                   self.sbutton_clicked(state, idx, button))
            suggest_layout.addWidget(button,index)

        
        rows = 0
        columns = 0
        
        self.push_buttons = {}     
        for idx, icon in self.icons.items():
            button = QPushButtonIcon()
            button.setIcon(icon)
            self.push_buttons[idx]=button
            button.clicked.connect(lambda state, button = button, idx = idx :
                                self.champion_clicked(state, idx, button))
            
            champion_layout.addWidget(button,rows,columns)
            
            columns+=1
            
            if columns % 7 == 0:
                columns = 0
                rows += 1

        main_layout.addLayout(select_layout)   
        main_layout.addLayout(suggest_layout)  
        main_layout.addLayout(champion_layout)
        

        self.setLayout(main_layout)
        self.setFixedSize(main_layout.sizeHint())
        self.setWindowTitle("LoL Chess")
        self.show()

    def champion_clicked(self, state, idx, button):
        if len(self.selection_list) < len(self.pbuttons):
            self.selection_list.append(idx)
        self.set_button_index()

            
    def set_button_index(self):
        for idx in range(len(self.selection_list)):
            pbuttons = self.pbuttons[idx]
            champnum = self.selection_list[idx]
            icon = self.icons_for_index[champnum]
            pbuttons.setIcon(icon)
    
    def delete_button_index(self):  
        list_len = len(self.selection_list)
        
        
        for idx in range(list_len):        
            pbuttons = self.pbuttons[idx]
            champnum = self.selection_list[idx]
            icon = self.icons_for_index[champnum]
            pbuttons.setIcon(icon)
            
        for idx_last in range(int(10-list_len)):
            index = idx_last + list_len
            pbuttons = self.pbuttons[index]
            pbuttons.setIcon(QIcon())
   
    def pbutton_clicked(self,state,idx):
        if idx>len(self.selection_list):
            pass
        elif self.selection_list[idx] != None:
            del self.selection_list[idx]
            self.delete_button_index()
            


    def action_reset(self):
        
        self.selection_list = []
        
        for button in self.qbuttons.values():
            button.setDisabled(False)
        for button in self.sbuttons.values():
            button.setIcon(QIcon())        
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
        