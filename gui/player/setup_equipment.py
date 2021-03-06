from PyQt4 import QtCore, QtGui
import gui.tools as tools

        
def setupEquipment(self):
    self.tab3 = QtGui.QWidget()
    self.tab3.setObjectName(tools._fromUtf8("tab3"))
    self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab3)
    self.verticalLayout_6.setObjectName(tools._fromUtf8("verticalLayout_6"))
    self.tab3_tabwidget = QtGui.QTabWidget(self.tab3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tab3_tabwidget.sizePolicy().hasHeightForWidth())
    self.tab3_tabwidget.setSizePolicy(sizePolicy)
    self.tab3_tabwidget.setObjectName(tools._fromUtf8("tab3_tabwidget"))

    # weapons
    self.tab3_tab0 = QtGui.QWidget()
    self.tab3_tab0.setObjectName(tools._fromUtf8("tab3_tab0"))
    self.horizontalLayout_11 = QtGui.QHBoxLayout(self.tab3_tab0)
    self.horizontalLayout_11.setObjectName(tools._fromUtf8("horizontalLayout_11"))
    # list
    self.tab3_tab0_list_layout = QtGui.QGroupBox("List", self.tab3_tab0)
    self.tab3_tab0_list_layout.setObjectName(tools._fromUtf8("tab3_tab0_list_layout"))
    self.horizontalLayout_31 = QtGui.QHBoxLayout(self.tab3_tab0_list_layout)
    self.horizontalLayout_31.setObjectName(tools._fromUtf8("horizontalLayout_31"))
    self.tab3_tab0_list_tree = QtGui.QTreeWidget(self.tab3_tab0_list_layout)
    self.tab3_tab0_list_tree.currentItemChanged.connect(
        self.updateEquipmentDescription)
    self.tab3_tab0_list_tree.setRootIsDecorated(True)
    self.tab3_tab0_list_tree.setObjectName(tools._fromUtf8("tab3_tab0_list_tree"))
    self.horizontalLayout_31.addWidget(self.tab3_tab0_list_tree)
    self.horizontalLayout_11.addWidget(self.tab3_tab0_list_layout)
    self.tab3_tab0_list_tree.setSortingEnabled(True)
    self.tab3_tab0_list_tree.headerItem().setText(0, "Name")
    self.tab3_tab0_list_tree.headerItem().setText(1, "Cost")
    self.tab3_tab0_list_tree.headerItem().setText(2, "Damage")
    self.tab3_tab0_list_tree.headerItem().setText(3, "Weight")
    self.tab3_tab0_list_tree.headerItem().setText(4, "Properties")
    self.tab3_tab0_list_tree.headerItem().setText(5, "Type")
    # owned
    self.tab3_tab0_owned_layout = QtGui.QGroupBox("Owned", self.tab3_tab0)
    self.tab3_tab0_owned_layout.setObjectName(tools._fromUtf8("tab3_tab0_owned_layout"))
    self.horizontalLayout_32 = QtGui.QHBoxLayout(self.tab3_tab0_owned_layout)
    self.horizontalLayout_32.setObjectName(tools._fromUtf8("horizontalLayout_32"))
    self.tab3_tab0_owned_tree = QtGui.QTreeWidget(self.tab3_tab0_owned_layout)
    self.tab3_tab0_owned_tree.currentItemChanged.connect(
        self.updateEquipmentDescription)
    self.tab3_tab0_owned_tree.setSortingEnabled(True)
    self.tab3_tab0_owned_tree.setObjectName(tools._fromUtf8("tab3_tab0_owned_tree"))
    self.horizontalLayout_32.addWidget(self.tab3_tab0_owned_tree)
    self.horizontalLayout_11.addWidget(self.tab3_tab0_owned_layout)
    self.tab3_tab0_owned_layout.setTitle("Weapon Owned")
    self.tab3_tab0_owned_tree.headerItem().setText(0, "Name")
    self.tab3_tab0_owned_tree.headerItem().setText(1, "Cost")
    self.tab3_tab0_owned_tree.headerItem().setText(2, "Damage")
    self.tab3_tab0_owned_tree.headerItem().setText(3, "Weight")
    self.tab3_tab0_owned_tree.headerItem().setText(4, "Properties")
    self.tab3_tab0_owned_tree.headerItem().setText(5, "Type")
    self.tab3_tabwidget.addTab(self.tab3_tab0, "Weapons")
    
    # armor
    self.tab3_tab1 = QtGui.QWidget()
    self.tab3_tab1.setObjectName(tools._fromUtf8("tab3_tab1"))
    self.horizontalLayout_23 = QtGui.QHBoxLayout(self.tab3_tab1)
    self.horizontalLayout_23.setObjectName(tools._fromUtf8("horizontalLayout_23"))
    # list
    self.tab3_tab1_list_layout = QtGui.QGroupBox("List", self.tab3_tab1)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tab3_tab1_list_layout.sizePolicy().hasHeightForWidth())
    self.tab3_tab1_list_layout.setSizePolicy(sizePolicy)
    self.tab3_tab1_list_layout.setObjectName(tools._fromUtf8("tab3_tab1_list_layout"))
    self.horizontalLayout_29 = QtGui.QHBoxLayout(self.tab3_tab1_list_layout)
    self.horizontalLayout_29.setObjectName(tools._fromUtf8("horizontalLayout_29"))
    self.tab3_tab1_list_tree = QtGui.QTreeWidget(self.tab3_tab1_list_layout)
    self.tab3_tab1_list_tree.currentItemChanged.connect(
        self.updateEquipmentDescription)
    self.tab3_tab1_list_tree.setSortingEnabled(True)
    self.tab3_tab1_list_tree.setRootIsDecorated(True)
    self.tab3_tab1_list_tree.setObjectName(tools._fromUtf8("tab3_tab1_list_tree"))
    self.tab3_tab1_list_tree.headerItem().setText(0, "Name")
    self.tab3_tab1_list_tree.headerItem().setText(1, "Cost")
    self.tab3_tab1_list_tree.headerItem().setText(2, "Armor")
    self.tab3_tab1_list_tree.headerItem().setText(3, "Strength")
    self.tab3_tab1_list_tree.headerItem().setText(4, "Stealth")
    self.tab3_tab1_list_tree.headerItem().setText(5, "Weight")
    self.tab3_tab1_list_tree.headerItem().setText(6, "Type")
    self.horizontalLayout_29.addWidget(self.tab3_tab1_list_tree)
    self.horizontalLayout_23.addWidget(self.tab3_tab1_list_layout)
    # owned
    self.tab3_tab1_owned_layout = QtGui.QGroupBox("Owned", self.tab3_tab1)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tab3_tab1_owned_layout.sizePolicy().hasHeightForWidth())
    self.tab3_tab1_owned_layout.setSizePolicy(sizePolicy)
    self.tab3_tab1_owned_layout.setObjectName(tools._fromUtf8("tab3_tab1_owned_layout"))
    self.horizontalLayout_30 = QtGui.QHBoxLayout(self.tab3_tab1_owned_layout)
    self.horizontalLayout_30.setObjectName(tools._fromUtf8("horizontalLayout_30"))
    self.tab3_tab1_owned_tree = QtGui.QTreeWidget(self.tab3_tab1_owned_layout)
    self.tab3_tab1_owned_tree.currentItemChanged.connect(
        self.updateEquipmentDescription)
    self.tab3_tab1_owned_tree.setSortingEnabled(True)
    self.tab3_tab1_owned_tree.setObjectName(tools._fromUtf8("tab3_tab1_owned_tree"))
    self.tab3_tab1_owned_tree.headerItem().setText(0, "Name")
    self.tab3_tab1_owned_tree.headerItem().setText(1, "Cost")
    self.tab3_tab1_owned_tree.headerItem().setText(2, "Armor")
    self.tab3_tab1_owned_tree.headerItem().setText(3, "Strength")
    self.tab3_tab1_owned_tree.headerItem().setText(4, "Stealth")
    self.tab3_tab1_owned_tree.headerItem().setText(5, "Weight")
    self.tab3_tab1_owned_tree.headerItem().setText(6, "Type")
    self.horizontalLayout_30.addWidget(self.tab3_tab1_owned_tree)
    self.horizontalLayout_23.addWidget(self.tab3_tab1_owned_layout)
    self.tab3_tabwidget.addTab(self.tab3_tab1, "Armor")

    # Gear
    self.tab3_tab2 = QtGui.QWidget()
    self.tab3_tab2.setObjectName(tools._fromUtf8("tab3_tab2"))
    self.horizontalLayout_24 = QtGui.QHBoxLayout(self.tab3_tab2)
    self.horizontalLayout_24.setObjectName(tools._fromUtf8("horizontalLayout_24"))
    # list
    self.tab3_tab2_list_layout = QtGui.QGroupBox("List", self.tab3_tab2)
    self.tab3_tab2_list_layout.setObjectName(tools._fromUtf8("tab3_tab2_list_layout"))
    self.horizontalLayout_28 = QtGui.QHBoxLayout(self.tab3_tab2_list_layout)
    self.horizontalLayout_28.setObjectName(tools._fromUtf8("horizontalLayout_28"))
    self.tab3_tab2_list_tree = QtGui.QTreeWidget(self.tab3_tab2_list_layout)
    self.tab3_tab2_list_tree.currentItemChanged.connect(
        self.updateEquipmentDescription)
    self.tab3_tab2_list_tree.setSortingEnabled(True)
    self.tab3_tab2_list_tree.setObjectName(tools._fromUtf8("tab3_tab2_list_tree"))
    self.tab3_tab2_list_tree.headerItem().setText(0, "Name")
    self.tab3_tab2_list_tree.headerItem().setText(1, "Cost")
    self.tab3_tab2_list_tree.headerItem().setText(2, "Weight")
    self.tab3_tab2_list_tree.headerItem().setText(3, "Quantity")
    self.horizontalLayout_28.addWidget(self.tab3_tab2_list_tree)
    self.horizontalLayout_24.addWidget(self.tab3_tab2_list_layout)
    # owned
    self.tab3_tab2_owned_layout = QtGui.QGroupBox("Owned", self.tab3_tab2)
    self.tab3_tab2_owned_layout.setObjectName(tools._fromUtf8("tab3_tab2_owned_layout"))
    self.verticalLayout_23 = QtGui.QVBoxLayout(self.tab3_tab2_owned_layout)
    self.verticalLayout_23.setObjectName(tools._fromUtf8("verticalLayout_23"))
    self.tab3_tab2_owned_tree = QtGui.QTreeWidget(self.tab3_tab2_owned_layout)
    self.tab3_tab2_owned_tree.currentItemChanged.connect(
        self.updateEquipmentDescription)
    self.tab3_tab2_owned_tree.setSortingEnabled(True)
    self.tab3_tab2_owned_tree.setObjectName(tools._fromUtf8("tab3_tab2_owned_tree"))
    self.tab3_tab2_owned_tree.headerItem().setText(0, "Name")
    self.tab3_tab2_owned_tree.headerItem().setText(1, "Cost")
    self.tab3_tab2_owned_tree.headerItem().setText(2, "Weight")
    self.tab3_tab2_owned_tree.headerItem().setText(3, "Quantity")
    self.verticalLayout_23.addWidget(self.tab3_tab2_owned_tree)
    self.horizontalLayout_24.addWidget(self.tab3_tab2_owned_layout)
    self.tab3_tabwidget.addTab(self.tab3_tab2, "Gear")

    # lower part
    self.verticalLayout_6.addWidget(self.tab3_tabwidget)
    self.tab3_gold_layout = QtGui.QHBoxLayout()
    self.tab3_gold_layout.setContentsMargins(0, 0, -1, -1)
    # money
    self.tab3_gold_layout.setObjectName(tools._fromUtf8("tab3_gold_layout"))
    self.tab3_carry_label = QtGui.QLabel("", self.tab3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
    self.tab3_carry_label.setSizePolicy(sizePolicy)
    self.tab3_carry_label.setAlignment(QtCore.Qt.AlignCenter)
    self.tab3_carry_label.setObjectName(tools._fromUtf8("tab3_carry_label"))
    self.tab3_gold_layout.addWidget(self.tab3_carry_label)
    carry_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
    self.tab3_gold_layout.addItem(carry_spacer)

    self.tab3_gold_label = QtGui.QLabel("", self.tab3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tab3_gold_label.sizePolicy().hasHeightForWidth())
    self.tab3_gold_label.setSizePolicy(sizePolicy)
    self.tab3_gold_label.setAlignment(QtCore.Qt.AlignCenter)
    self.tab3_gold_label.setObjectName(tools._fromUtf8("tab3_gold_label"))
    self.tab3_gold_layout.addWidget(self.tab3_gold_label)
    spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
    self.tab3_gold_layout.addItem(spacerItem10)
    self.tab3_gold_button = QtGui.QPushButton("Earn/Loose Money", self.tab3)
    self.tab3_gold_button.clicked.connect(self.earnMoney)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tab3_gold_button.sizePolicy().hasHeightForWidth())
    self.tab3_gold_button.setSizePolicy(sizePolicy)
    self.tab3_gold_button.setObjectName(tools._fromUtf8("tab3_gold_button"))
    self.tab3_gold_layout.addWidget(self.tab3_gold_button)
    self.verticalLayout_6.addLayout(self.tab3_gold_layout)

    # description
    self.tab3_description_layout = QtGui.QGroupBox("Description", self.tab3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tab3_description_layout.sizePolicy().hasHeightForWidth())
    self.tab3_description_layout.setSizePolicy(sizePolicy)
    self.tab3_description_layout.setObjectName(tools._fromUtf8("tab3_description_layout"))
    self.horizontalLayout_25 = QtGui.QHBoxLayout(self.tab3_description_layout)
    self.horizontalLayout_25.setObjectName(tools._fromUtf8("horizontalLayout_25"))
    self.tab3_buy_layout = QtGui.QVBoxLayout()
    self.tab3_buy_layout.setObjectName(tools._fromUtf8("tab3_buy_layout"))
    self.tab3_buy_button = QtGui.QPushButton("Buy", self.tab3_description_layout)
    self.tab3_buy_button.clicked.connect(self.buyEquipment)
    self.tab3_buy_button.setObjectName(tools._fromUtf8("tab3_buy_button"))
    self.tab3_buy_layout.addWidget(self.tab3_buy_button)
    self.tab3_add_button = QtGui.QPushButton("Add", self.tab3_description_layout)
    self.tab3_add_button.setObjectName(tools._fromUtf8("tab3_add_button"))
    self.tab3_add_button.clicked.connect(self.addEquipment)
    self.tab3_buy_layout.addWidget(self.tab3_add_button)
    self.horizontalLayout_25.addLayout(self.tab3_buy_layout)
    self.tab3_description = QtGui.QTextBrowser(self.tab3_description_layout)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tab3_description.sizePolicy().hasHeightForWidth())
    self.tab3_description.setSizePolicy(sizePolicy)
    self.tab3_description.setObjectName(tools._fromUtf8("tab3_description"))
    self.horizontalLayout_25.addWidget(self.tab3_description)
    self.tab3_sell_layout = QtGui.QVBoxLayout()
    self.tab3_sell_layout.setObjectName(tools._fromUtf8("tab3_sell_layout"))
    self.tab3_sell_button = QtGui.QPushButton("Sell", self.tab3_description_layout)
    self.tab3_sell_button.clicked.connect(self.sellEquipment)
    self.tab3_sell_button.setObjectName(tools._fromUtf8("tab3_sell_button"))
    self.tab3_sell_layout.addWidget(self.tab3_sell_button)
    self.tab3_remove_button = QtGui.QPushButton("Remove", self.tab3_description_layout)
    self.tab3_remove_button.setObjectName(tools._fromUtf8("tab3_remove_button"))
    self.tab3_remove_button.clicked.connect(self.removeEquipment)
    self.tab3_sell_layout.addWidget(self.tab3_remove_button)
    self.horizontalLayout_25.addLayout(self.tab3_sell_layout)
    self.verticalLayout_6.addWidget(self.tab3_description_layout)

    generateEquipmentList(self)
    generateInitialEquipment(self)
    self.main_tab.addTab(self.tab3, "Equipment")

def generateEquipmentList(self):
    weapon = self.equipment_parser.getListWeapon()
    for i in weapon:
        item = QtGui.QTreeWidgetItem(self.tab3_tab0_list_tree, i)

    armor = self.equipment_parser.getListArmor()
    for i in armor:
        item = QtGui.QTreeWidgetItem(self.tab3_tab1_list_tree, i)

    gear = self.equipment_parser.getListGear()
    for i in gear:
        item = QtGui.QTreeWidgetItem(self.tab3_tab2_list_tree, i)

def generateInitialEquipment(self):
    for item in self.character.equipment:
        item_parser = self.equipment_parser.getEquipment(item)
        if item_parser.tag == 'gear':
            list_string = [item_parser.get('name'),
                           item_parser.get('cost'),
                           item_parser.get('weight'),
                           item_parser.get('quantity')]
            item = QtGui.QTreeWidgetItem(
                self.tab3_tab2_owned_tree, list_string)
        elif item_parser.tag == 'armor':
            list_string = [item_parser.get('name'),
                           item_parser.get('cost'),
                           item_parser.get('ac'),
                           item_parser.get('strength'),
                           item_parser.get('stealth'),
                           item_parser.get('weight'),
                           item_parser.get('type')]
            item = QtGui.QTreeWidgetItem(
                self.tab3_tab1_owned_tree, list_string)
        elif item_parser.tag == 'weapon':
            list_string = [item_parser.get('name'),
                           item_parser.get('cost'),
                           item_parser.get('damage'),
                           item_parser.get('weight'),
                           item_parser.get('properties'),
                           item_parser.get('type')]
            item = QtGui.QTreeWidgetItem(
                self.tab3_tab0_owned_tree, list_string)

        self.updateCarryCapacity()
