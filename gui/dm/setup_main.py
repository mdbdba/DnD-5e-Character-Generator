from PyQt4 import QtGui, QtCore

import gui.tools as tools


def setupDMMain(self):

    self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
    self.verticalLayout.setObjectName(tools._fromUtf8("verticalLayout"))
    # Tree
    self.tree_widget = QtGui.QTreeWidget(self.centralwidget)
    self.tree_widget.setObjectName(tools._fromUtf8("tree_widget"))
    self.tree_widget.headerItem().setText(0, "Name")
    self.tree_widget.headerItem().setText(1, "Player")
    self.tree_widget.headerItem().setText(2, "Class")
    self.tree_widget.headerItem().setText(3, "HP")
    self.tree_widget.headerItem().setText(4, "Take Damage")
    self.tree_widget.headerItem().setText(5, "Gold")
    self.tree_widget.headerItem().setText(6, "Group")
    __sortingEnabled = self.tree_widget.isSortingEnabled()
    self.tree_widget.setSortingEnabled(__sortingEnabled)
    self.tree_widget.itemDoubleClicked.connect(self.openCharacter)
    self.verticalLayout.addWidget(self.tree_widget)

    # menu
    self.menu_bar = QtGui.QMenuBar(self.main_window)
    self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1009, 19))
    self.menu_bar.setObjectName(tools._fromUtf8("menu_bar"))
    self.menu_server = QtGui.QMenu("&Server", self.menu_bar)
    self.menu_server.setObjectName(tools._fromUtf8("menu_server"))    
    self.menu_encounters = QtGui.QMenu("&Encounters", self.menu_bar)
    self.menu_encounters.setObjectName(tools._fromUtf8("menu_encounters"))
    self.menu_dungeon = QtGui.QMenu("&Dungeon", self.menu_bar)
    self.menu_dungeon.setObjectName(tools._fromUtf8("menu_dungeon"))
    self.menu_npc = QtGui.QMenu("&NPC", self.menu_bar)
    self.menu_npc.setObjectName(tools._fromUtf8("menu_npc"))
    self.menu_event = QtGui.QMenu("E&vent", self.menu_bar)
    self.menu_event.setObjectName(tools._fromUtf8("menu_event"))
    self.menu_treasure = QtGui.QMenu("&Treasure", self.menu_bar)
    self.menu_treasure.setObjectName(tools._fromUtf8("menu_treasure"))
    self.menu_survival = QtGui.QMenu("S&urvival", self.menu_bar)
    self.menu_survival.setObjectName(tools._fromUtf8("menu_survival"))
    self.menu_settlements = QtGui.QMenu("Se&ttlements", self.menu_bar)
    self.menu_settlements.setObjectName(tools._fromUtf8("menu_settlements"))
    self.menu_modify_character = QtGui.QMenu("&Modify Character", self.menu_bar)
    self.menu_modify_character.setObjectName(tools._fromUtf8("menu_modify_character"))
    self.main_window.setMenuBar(self.menu_bar)
    self.statusbar = QtGui.QStatusBar(self.main_window)
    self.statusbar.showMessage("You have 0 player")
    self.statusbar.setObjectName(tools._fromUtf8("statusbar"))
    self.main_window.setStatusBar(self.statusbar)

    # action
    self.action_get_ip = QtGui.QAction("&Get IP", self.main_window)
    self.action_get_ip.setObjectName(tools._fromUtf8("action_get_ip"))
    self.action_kick_player = QtGui.QAction("&Kick Player", self.main_window)
    self.action_kick_player.setObjectName(tools._fromUtf8("action_kick_player"))
    self.action_new = QtGui.QAction("&New", self.main_window)
    self.action_new.setObjectName(tools._fromUtf8("action_new"))
    self.action_load = QtGui.QAction("&Load", self.main_window)
    self.action_load.setObjectName(tools._fromUtf8("action_load"))
    self.menu_server.addAction(self.action_get_ip)
    self.menu_server.addAction(self.action_kick_player)
    self.menu_encounters.addAction(self.action_new)
    self.menu_encounters.addAction(self.action_load)
    self.menu_bar.addAction(self.menu_server.menuAction())
    self.menu_bar.addAction(self.menu_encounters.menuAction())
    self.menu_bar.addAction(self.menu_dungeon.menuAction())
    self.menu_bar.addAction(self.menu_npc.menuAction())
    self.menu_bar.addAction(self.menu_event.menuAction())
    self.menu_bar.addAction(self.menu_treasure.menuAction())
    self.menu_bar.addAction(self.menu_survival.menuAction())
    self.menu_bar.addAction(self.menu_settlements.menuAction())
    self.menu_bar.addAction(self.menu_modify_character.menuAction())
    
    QtCore.QMetaObject.connectSlotsByName(self.main_window)