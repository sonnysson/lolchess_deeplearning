import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtTest import *  
from PyQt5 import uic 

class QLabelCustom(QLabel):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedHeight(80)
        self.setFixedWidth(80)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QFont("Helvetia", 13)
        font.setBold(True)

class QPushButtonUpload(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setFixedHeight(80)
        self.setFixedWidth(80)
        self.setIconSize(QSize(72, 72))

class QPushButtonIcon(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedHeight(60)
        self.setFixedWidth(60)
        self.setIconSize(QSize(60,60))
        
class QGridLayoutChampion(QGridLayout):
    def __init__(self, parent = None):

        super().__init__(parent)
        
class QPushButtonItem(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedHeight(24)
        self.setFixedWidth(24)
        self.setIconSize(QSize(24,24))
    
class QPushButtonReset(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedHeight(50)
        font = QFont("Helvetica", 12)
        font.setBold(True)
        self.setFont(font)

class QItemLabel(QLabel):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedHeight(25)
        self.setFixedWidth(23)

class Main(QDialog):
    
    def __init__(self):
        super().__init__()
        self.set_champions()
        self.init_ui()
        self.set_style()
        self.set_items()

    def set_items(self):
        self.item_name = ["ArcaneGauntlet.png","Archangelembrace.png","Backhand.png","Bloodthirster.png","BlueBuff.png","BrambleVest.png","Chalice.png",
                      "Curtainofsilence.png","DragonsClaw.png","FrozenHeart.png","GiantSlayer.png","GuardianAngel.png","GuinsoosRageblade.png",
                      "HandofJustice.png","HextechGunblade.png","InfinityEdge.png","IonicSpark.png","IronWill.png","LastWhisper.png","LocketoftheIronSolari.png",
                      "LordsEdge.png","Morellonomicon.png","Quicksilver.png","RabadonsDeathcap.png","RapidFirecannon.png","Redemption.png","RunaansHurricane.png",
                     "SpearofShojin.png","StatikkShiv.png","SunfireCape.png","ThiefsGloves.png","TitansResolve.png","Warmog'sArmor.png","ZekesHerald.png",
                     "Zephyr.png","ZzRotPortal.png"]
        
        self.items ={}
        
        for index,filename in enumerate(self.item_name):
            pixmap=QPixmap(f"image\items\{filename}")     
            pixmap = pixmap.scaled(45,45,Qt.IgnoreAspectRatio)      
            item = QIcon()
            item.addPixmap(pixmap)
            
            self.items[index] = item      
    def set_champions(self):
        self.suggest_list=[]
        self.item_list=[]
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
        with open("style.css", 'r') as f:
            self.setStyleSheet(f.read())
    def init_ui(self):
        self.setWindowTitle('lolchess')
        
        main_layout = QVBoxLayout()
        middle_layout=QHBoxLayout()
        champion_layout = QGridLayout()
        select_layout = QHBoxLayout()
        suggest_layout = QHBoxLayout()
        button_layout = QGridLayout()        
        item_layout=QHBoxLayout()
        
        self.pbuttons = {}
        self.sbuttons = {}
        self.item_labels={}
        
        for index in range(10):
            button = QPushButtonUpload()
            self.pbuttons[index] = button
            button.clicked.connect(lambda state ,index = index : self.pbutton_clicked(self,index))
            select_layout.addWidget(button,index)
           
        
        for index in range(10):
            button = QPushButtonUpload()
            self.sbuttons[index] = button
            suggest_layout.addWidget(button,index)
            
        for index in range(30):
            button = QPushButtonItem()
            self.item_labels[index]=button
            item_layout.addWidget(button,index)
            
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
                
        middle_layout.addLayout(champion_layout,0)
        
        expected_rank = QLabelCustom()
        
        middle_right_layout = QHBoxLayout()
        middle_right_layout.addWidget(expected_rank,2)
        middle_layout.addLayout(middle_right_layout,1)
        
        self.button_reset = QPushButtonReset("Reset")
        self.button_reset.clicked.connect(self.action_reset)

        self.button_solution = QPushButtonReset("Solution")
        self.button_solution.clicked.connect(self.action_solution)

        button_layout.addWidget(self.button_reset,0,0)
        button_layout.addWidget(self.button_solution,0,1)
        
        main_layout.addLayout(select_layout)   
        main_layout.addLayout(suggest_layout)  
        main_layout.addLayout(item_layout)
        main_layout.addLayout(middle_layout)
        main_layout.addStretch(1)
        main_layout.addLayout(button_layout)
        
        self.setLayout(main_layout)
        self.setGeometry(400,100,600,600)
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
    def set_suggest_index(self):
        for idx in range(len(self.suggest_list)):
            sbuttons = self.sbuttons[idx]
            champnum = self.suggest_list[idx]
            icon = self.icons_for_index[champnum]
            sbuttons.setIcon(icon) 
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
        if idx>=len(self.selection_list):
            pass
        elif self.selection_list[idx] != None:
            del self.selection_list[idx]
            self.delete_button_index()
    def action_reset(self):
        self.champion_btn_able()
        self.suggest_list=[]
        self.selection_list = []
        
        for button in self.pbuttons.values():
            button.setIcon(QIcon())
            
        for button in self.sbuttons.values():
            button.setIcon(QIcon())
            
        for button in self.item_labels.values():
            button.setIcon(QIcon())
    def solution(self):
        self.suggest_list = [12,26,35,12,26,35,12,26,35,7]
        self.item_list =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29] 
    def action_solution(self):
        self.champion_btn_disable()
        self.solution()
        self.set_suggest_index()   
        self.set_suggest_item() 
    def set_suggest_item(self):
        for idx in range(len(self.item_list)):
            itemname = self.item_labels[idx]
            num = self.item_list[idx]
            item = self.items[num]
            itemname.setIcon(item)
    def champion_btn_able(self):
        for index,button in self.push_buttons.items():
            button.setEnabled(True)            
    def champion_btn_disable(self):
        for index,button in self.push_buttons.items():
            button.setDisabled(True)         
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
        