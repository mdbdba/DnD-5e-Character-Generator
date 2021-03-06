from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

def setupDescription(self):
    # create tab
    self.page0 = QtGui.QWizardPage()
    self.page0.setObjectName(_fromUtf8("page0"))
    self.horizontalLayout_19 = QtGui.QHBoxLayout(self.page0)
    self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))

    # create left side
    self.page0_character_layout = QtGui.QGroupBox("Character", self.page0)
    self.page0_character_layout.setObjectName(_fromUtf8("page0_character_layout"))
    self.verticalLayout_22 = QtGui.QVBoxLayout(self.page0_character_layout)
    self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
    
    # create character's form
    self.page0_character_form = QtGui.QFormLayout()
    self.page0_character_form.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
    self.page0_character_form.setObjectName(_fromUtf8("page0_character_form"))
    self.page0_characterNameLabel = QtGui.QLabel("Character Name", self.page0_character_layout)
    self.page0_characterNameLabel.setObjectName(_fromUtf8("page0_characterNameLabel"))
    self.page0_character_form.setWidget(0, QtGui.QFormLayout.LabelRole, self.page0_characterNameLabel)
    self.page0_characterNameLineEdit = QtGui.QLineEdit(self.page0_character_layout)
    self.page0_characterNameLineEdit.textChanged.connect(self.wizard.character.setName)
    self.page0_characterNameLineEdit.setObjectName(_fromUtf8("page0_characterNameLineEdit"))
    self.page0_character_form.setWidget(0, QtGui.QFormLayout.FieldRole, self.page0_characterNameLineEdit)
    self.page0_playerNameLabel = QtGui.QLabel("Player Name", self.page0_character_layout)
    self.page0_playerNameLabel.setObjectName(_fromUtf8("page0_playerNameLabel"))
    self.page0_character_form.setWidget(1, QtGui.QFormLayout.LabelRole, self.page0_playerNameLabel)
    self.page0_playerNameLineEdit = QtGui.QLineEdit(self.page0_character_layout)
    self.page0_playerNameLineEdit.textChanged.connect(self.wizard.character.setPlayer)
    self.page0_playerNameLineEdit.setObjectName(_fromUtf8("page0_playerNameLineEdit"))
    self.page0_character_form.setWidget(1, QtGui.QFormLayout.FieldRole, self.page0_playerNameLineEdit)
    self.page0_campaignLabel = QtGui.QLabel("Campaign", self.page0_character_layout)
    self.page0_campaignLabel.setObjectName(_fromUtf8("page0_campaignLabel"))
    self.page0_character_form.setWidget(2, QtGui.QFormLayout.LabelRole, self.page0_campaignLabel)
    self.page0_campaignComboBox = QtGui.QComboBox(self.page0_character_layout)
    self.page0_campaignComboBox.activated[str].connect(self.wizard.character.setCampaign)
    self.page0_campaignComboBox.setEditable(True)
    self.page0_campaignComboBox.setObjectName(_fromUtf8("page0_campaignComboBox"))
    self.page0_character_form.setWidget(2, QtGui.QFormLayout.FieldRole, self.page0_campaignComboBox)
    self.page0_genderLabel = QtGui.QLabel("Gender", self.page0_character_layout)
    self.page0_genderLabel.setObjectName(_fromUtf8("page0_genderLabel"))
    self.page0_character_form.setWidget(3, QtGui.QFormLayout.LabelRole, self.page0_genderLabel)
    self.page0_genderComboBox = QtGui.QComboBox(self.page0_character_layout)
    self.page0_genderComboBox.activated.connect(self.wizard.character.setGender)
    self.page0_genderComboBox.setObjectName(_fromUtf8("page0_genderComboBox"))
    self.page0_genderComboBox.addItem("Male")
    self.page0_genderComboBox.addItem("Female")
    self.page0_character_form.setWidget(3, QtGui.QFormLayout.FieldRole, self.page0_genderComboBox)
    self.page0_ageLabel = QtGui.QLabel("Age", self.page0_character_layout)
    self.page0_ageLabel.setObjectName(_fromUtf8("page0_ageLabel"))
    self.page0_character_form.setWidget(4, QtGui.QFormLayout.LabelRole, self.page0_ageLabel)
    self.page0_ageLineEdit = QtGui.QLineEdit(self.page0_character_layout)
    self.page0_ageLineEdit.textChanged.connect(self.wizard.character.setAge)
    self.page0_ageLineEdit.setObjectName(_fromUtf8("page0_ageLineEdit"))
    self.page0_character_form.setWidget(4, QtGui.QFormLayout.FieldRole, self.page0_ageLineEdit)
    self.page0_heightLabel = QtGui.QLabel("Height", self.page0_character_layout)
    self.page0_heightLabel.setObjectName(_fromUtf8("page0_heightLabel"))
    self.page0_character_form.setWidget(5, QtGui.QFormLayout.LabelRole, self.page0_heightLabel)
    self.page0_heightLineEdit = QtGui.QLineEdit(self.page0_character_layout)
    self.page0_heightLineEdit.textChanged.connect(self.wizard.character.setHeight)
    self.page0_heightLineEdit.setObjectName(_fromUtf8("page0_heightLineEdit"))
    self.page0_character_form.setWidget(5, QtGui.QFormLayout.FieldRole, self.page0_heightLineEdit)
    self.page0_weightLabel = QtGui.QLabel("Weight", self.page0_character_layout)
    self.page0_weightLabel.setObjectName(_fromUtf8("page0_weightLabel"))
    self.page0_character_form.setWidget(6, QtGui.QFormLayout.LabelRole, self.page0_weightLabel)
    self.page0_weightLineEdit = QtGui.QLineEdit(self.page0_character_layout)
    self.page0_weightLineEdit.textChanged.connect(self.wizard.character.setWeight)
    self.page0_weightLineEdit.setObjectName(_fromUtf8("page0_weightLineEdit"))
    self.page0_character_form.setWidget(6, QtGui.QFormLayout.FieldRole, self.page0_weightLineEdit)
    self.page0_hairLabel = QtGui.QLabel("Hair", self.page0_character_layout)
    self.page0_hairLabel.setObjectName(_fromUtf8("page0_hairLabel"))
    self.page0_character_form.setWidget(7, QtGui.QFormLayout.LabelRole, self.page0_hairLabel)
    self.page0_hairLineEdit = QtGui.QLineEdit(self.page0_character_layout)
    self.page0_hairLineEdit.textChanged.connect(self.wizard.character.setHair)
    self.page0_hairLineEdit.setObjectName(_fromUtf8("page0_hairLineEdit"))
    self.page0_character_form.setWidget(7, QtGui.QFormLayout.FieldRole, self.page0_hairLineEdit)
    self.page0_eyeslabel = QtGui.QLabel("Eyes", self.page0_character_layout)
    self.page0_eyeslabel.setObjectName(_fromUtf8("page0_eyeslabel"))
    self.page0_character_form.setWidget(8, QtGui.QFormLayout.LabelRole, self.page0_eyeslabel)
    self.page0_eyesLineEdit = QtGui.QLineEdit(self.page0_character_layout)
    self.page0_eyesLineEdit.textChanged.connect(self.wizard.character.setEyes)
    self.page0_eyesLineEdit.setObjectName(_fromUtf8("page0_eyesLineEdit"))
    self.page0_character_form.setWidget(8, QtGui.QFormLayout.FieldRole, self.page0_eyesLineEdit)
    self.verticalLayout_22.addLayout(self.page0_character_form)
        
    # Notable features
    self.page0_features_layout = QtGui.QGroupBox("Notable Features", self.page0_character_layout)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.page0_features_layout.sizePolicy().hasHeightForWidth())
    self.page0_features_layout.setSizePolicy(sizePolicy)
    self.page0_features_layout.setObjectName(_fromUtf8("page0_features_layout"))
    self.verticalLayout_21 = QtGui.QVBoxLayout(self.page0_features_layout)
    self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
    self.page0_features = QtGui.QTextEdit(self.page0_features_layout)
    self.page0_features.textChanged.connect(self.notableFeaturesChanged)
    self.page0_features.setObjectName(_fromUtf8("page0_features"))

    self.verticalLayout_21.addWidget(self.page0_features)
    self.verticalLayout_22.addWidget(self.page0_features_layout)
    self.horizontalLayout_19.addWidget(self.page0_character_layout)

    # image
    self.page0_img_abilities_layout = QtGui.QVBoxLayout()
    self.page0_img_abilities_layout.setContentsMargins(0, -1, -1, -1)
    self.page0_img_abilities_layout.setObjectName(_fromUtf8("page0_img_abilities_layout"))
    self.page0_img_layout = QtGui.QHBoxLayout()
    self.page0_img_layout.setObjectName(_fromUtf8("page0_img_layout"))
    spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.page0_img_layout.addItem(spacerItem)
    self.page0_img = QtGui.QLabel(self.page0)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.page0_img.sizePolicy().hasHeightForWidth())
    self.page0_img.setSizePolicy(sizePolicy)
    self.page0_img.setMaximumSize(QtCore.QSize(400, 400))
    self.page0_img.setMinimumHeight(400)
    self.page0_img.setScaledContents(True)
    self.page0_img.setAlignment(QtCore.Qt.AlignCenter)
    self.page0_img.setObjectName(_fromUtf8("page0_img"))
    self.page0_img_layout.addWidget(self.page0_img)
    spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.page0_img_layout.addItem(spacerItem1)
    self.page0_img_button_layout = QtGui.QVBoxLayout()
    self.page0_img_button_layout.setObjectName(_fromUtf8("page0_img_button_layout"))
    self.page0_import_button = QtGui.QPushButton("Import Image", self.page0)
    self.page0_import_button.setObjectName(_fromUtf8("page0_import_button"))
    self.page0_import_button.clicked.connect(self.importImage)
    self.page0_img_button_layout.addWidget(self.page0_import_button)
    self.page0_remove_button = QtGui.QPushButton("Remove Image", self.page0)
    self.page0_remove_button.setObjectName(_fromUtf8("page0_remove_button"))
    self.page0_remove_button.clicked.connect(self.removeImage)
    self.page0_img_button_layout.addWidget(self.page0_remove_button)
    self.page0_img_layout.addLayout(self.page0_img_button_layout)
    self.page0_img_abilities_layout.addLayout(self.page0_img_layout)
    
    # abilities
    self.page0_abilities_layout = QtGui.QGroupBox("Abilities", self.page0)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.page0_abilities_layout.sizePolicy().hasHeightForWidth())
    self.page0_abilities_layout.setSizePolicy(sizePolicy)
    self.page0_abilities_layout.setObjectName(_fromUtf8("page0_abilities_layout"))
    self.verticalLayout_19 = QtGui.QVBoxLayout(self.page0_abilities_layout)
    self.verticalLayout_19.setSpacing(25)
    self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        
    # Choose Value
    self.page0_ability_style_layout = QtGui.QHBoxLayout()
    self.page0_ability_style_layout.setObjectName(_fromUtf8("page0_ability_style_layout"))
    self.page0_ability_style_combo = QtGui.QComboBox(self.page0_abilities_layout)
    self.page0_ability_style_combo.activated[str].connect(self.changeRollStyle)
    self.page0_ability_style_combo.setMinimumSize(QtCore.QSize(120, 0))
    self.page0_ability_style_combo.setObjectName(_fromUtf8("page0_ability_style_combo"))
    self.page0_ability_style_combo.addItem("Random")
    self.page0_ability_style_combo.addItem("Free")
    self.page0_ability_style_combo.addItem("Pregenerated")
    self.page0_ability_style_combo.addItem("Points")
    self.page0_ability_style_layout.addWidget(self.page0_ability_style_combo)
    self.page0_roll_button = QtGui.QPushButton("Roll", self.page0_abilities_layout)
    self.page0_roll_button.setObjectName(_fromUtf8("page0_roll_button"))
    self.page0_roll_button.clicked.connect(self.rollAbilities)
    self.page0_ability_style_layout.addWidget(self.page0_roll_button)
    self.page0_ability_point_score = QtGui.QLabel("", self.page0_abilities_layout)
    self.page0_ability_style_layout.addWidget(self.page0_ability_point_score)
    spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.page0_ability_style_layout.addItem(spacerItem2)
    self.verticalLayout_19.addLayout(self.page0_ability_style_layout)

    # Show Value
    self.page0_abilities_value_layout = QtGui.QHBoxLayout()
    self.page0_abilities_value_layout.setObjectName(_fromUtf8("page0_abilities_value_layout"))
    self.page0_ability_value_1 = QtGui.QLineEdit(self.page0_abilities_layout)
    self.page0_ability_value_1.textChanged.connect(self.changeAbilityRoll)
    self.page0_ability_value_1.setReadOnly(False)
    self.page0_ability_value_1.setObjectName(_fromUtf8("page0_ability_value_1"))
    self.page0_abilities_value_layout.addWidget(self.page0_ability_value_1)
    self.page0_ability_value_2 = QtGui.QLineEdit(self.page0_abilities_layout)
    self.page0_ability_value_2.textChanged.connect(self.changeAbilityRoll)
    self.page0_ability_value_2.setObjectName(_fromUtf8("page0_ability_value_2"))
    self.page0_abilities_value_layout.addWidget(self.page0_ability_value_2)
    self.page0_ability_value_3 = QtGui.QLineEdit(self.page0_abilities_layout)
    self.page0_ability_value_3.textChanged.connect(self.changeAbilityRoll)
    self.page0_ability_value_3.setObjectName(_fromUtf8("page0_ability_value_3"))
    self.page0_abilities_value_layout.addWidget(self.page0_ability_value_3)
    self.page0_ability_value_4 = QtGui.QLineEdit(self.page0_abilities_layout)
    self.page0_ability_value_4.textChanged.connect(self.changeAbilityRoll)
    self.page0_ability_value_4.setObjectName(_fromUtf8("page0_ability_value_4"))
    self.page0_abilities_value_layout.addWidget(self.page0_ability_value_4)
    self.page0_ability_value_5 = QtGui.QLineEdit(self.page0_abilities_layout)
    self.page0_ability_value_5.textChanged.connect(self.changeAbilityRoll)
    self.page0_ability_value_5.setObjectName(_fromUtf8("page0_ability_value_5"))
    self.page0_abilities_value_layout.addWidget(self.page0_ability_value_5)
    self.page0_ability_value_6 = QtGui.QLineEdit(self.page0_abilities_layout)
    self.page0_ability_value_6.textChanged.connect(self.changeAbilityRoll)
    self.page0_ability_value_6.setObjectName(_fromUtf8("page0_ability_value_6"))
    self.page0_abilities_value_layout.addWidget(self.page0_ability_value_6)
    self.verticalLayout_19.addLayout(self.page0_abilities_value_layout)

    # Score attribution
    self.page0_abilities_choice_layout = QtGui.QGridLayout()
    self.page0_abilities_choice_layout.setObjectName(_fromUtf8("page0_abilities_choice_layout"))
    self.page0_cha_combo = QtGui.QComboBox(self.page0_abilities_layout)
    self.page0_cha_combo.setObjectName(_fromUtf8("page0_cha_combo"))
    self.page0_cha_combo.activated[str].connect(self.wizard.character.setCharisma)
    self.page0_cha_combo.activated.connect(self.changeAttributionAbility)
    self.page0_abilities_choice_layout.addWidget(self.page0_cha_combo, 1, 5, 1, 1)
    self.page0_wis_combo = QtGui.QComboBox(self.page0_abilities_layout)
    self.page0_wis_combo.activated[str].connect(self.wizard.character.setWisdom)
    self.page0_wis_combo.activated.connect(self.changeAttributionAbility)
    self.page0_wis_combo.setObjectName(_fromUtf8("page0_wis_combo"))
    self.page0_abilities_choice_layout.addWidget(self.page0_wis_combo, 1, 4, 1, 1)
    self.page0_int_combo = QtGui.QComboBox(self.page0_abilities_layout)
    self.page0_int_combo.activated[str].connect(self.wizard.character.setIntelligence)
    self.page0_int_combo.activated.connect(self.changeAttributionAbility)
    self.page0_int_combo.setObjectName(_fromUtf8("page0_int_combo"))
    self.page0_abilities_choice_layout.addWidget(self.page0_int_combo, 1, 3, 1, 1)
    self.page0_con_combo = QtGui.QComboBox(self.page0_abilities_layout)
    self.page0_con_combo.activated[str].connect(self.wizard.character.setConstitution)
    self.page0_con_combo.activated.connect(self.changeAttributionAbility)
    self.page0_con_combo.setObjectName(_fromUtf8("page0_con_combo"))
    self.page0_abilities_choice_layout.addWidget(self.page0_con_combo, 1, 2, 1, 1)
    self.page0_dex_combo = QtGui.QComboBox(self.page0_abilities_layout)
    self.page0_dex_combo.activated[str].connect(self.wizard.character.setDexterity)
    self.page0_dex_combo.activated.connect(self.changeAttributionAbility)
    self.page0_dex_combo.setObjectName(_fromUtf8("page0_dex_combo"))
    self.page0_abilities_choice_layout.addWidget(self.page0_dex_combo, 1, 1, 1, 1)
    self.page0_str_combo = QtGui.QComboBox(self.page0_abilities_layout)
    self.page0_str_combo.activated[str].connect(self.wizard.character.setStrength)
    self.page0_str_combo.activated.connect(self.changeAttributionAbility)
    self.page0_str_combo.setObjectName(_fromUtf8("page0_str_combo"))
    self.page0_abilities_choice_layout.addWidget(self.page0_str_combo, 1, 0, 1, 1)
    # labels
    self.page0_cha_label = QtGui.QLabel("Charisma", self.page0_abilities_layout)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.page0_cha_label.sizePolicy().hasHeightForWidth())
    self.page0_cha_label.setSizePolicy(sizePolicy)
    self.page0_cha_label.setAlignment(QtCore.Qt.AlignCenter)
    self.page0_cha_label.setObjectName(_fromUtf8("page0_cha_label"))
    self.page0_abilities_choice_layout.addWidget(self.page0_cha_label, 0, 5, 1, 1)
    self.page0_wis_label = QtGui.QLabel("Wisdom", self.page0_abilities_layout)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.page0_wis_label.sizePolicy().hasHeightForWidth())
    self.page0_wis_label.setSizePolicy(sizePolicy)
    self.page0_wis_label.setAlignment(QtCore.Qt.AlignCenter)
    self.page0_wis_label.setObjectName(_fromUtf8("page0_wis_label"))
    self.page0_abilities_choice_layout.addWidget(self.page0_wis_label, 0, 4, 1, 1)
    self.page0_str_label = QtGui.QLabel("Strength", self.page0_abilities_layout)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.page0_str_label.sizePolicy().hasHeightForWidth())
    self.page0_str_label.setSizePolicy(sizePolicy)
    self.page0_str_label.setAlignment(QtCore.Qt.AlignCenter)
    self.page0_str_label.setObjectName(_fromUtf8("page0_str_label"))
    self.page0_abilities_choice_layout.addWidget(self.page0_str_label, 0, 0, 1, 1)
    self.page0_dex_label = QtGui.QLabel("Dexterity", self.page0_abilities_layout)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.page0_dex_label.sizePolicy().hasHeightForWidth())
    self.page0_dex_label.setSizePolicy(sizePolicy)
    self.page0_dex_label.setAlignment(QtCore.Qt.AlignCenter)
    self.page0_dex_label.setObjectName(_fromUtf8("page0_dex_label"))
    self.page0_abilities_choice_layout.addWidget(self.page0_dex_label, 0, 1, 1, 1)
    self.page0_con_label = QtGui.QLabel("Constitution", self.page0_abilities_layout)
    self.page0_con_label.setAlignment(QtCore.Qt.AlignCenter)
    self.page0_con_label.setObjectName(_fromUtf8("page0_con_label"))
    self.page0_abilities_choice_layout.addWidget(self.page0_con_label, 0, 2, 1, 1)
    self.page0_int_label = QtGui.QLabel("Intelligence", self.page0_abilities_layout)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.page0_int_label.sizePolicy().hasHeightForWidth())
    self.page0_int_label.setSizePolicy(sizePolicy)
    self.page0_int_label.setAlignment(QtCore.Qt.AlignCenter)
    self.page0_int_label.setObjectName(_fromUtf8("page0_int_label"))
    self.page0_abilities_choice_layout.addWidget(self.page0_int_label, 0, 3, 1, 1)
    self.verticalLayout_19.addLayout(self.page0_abilities_choice_layout)
    spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.verticalLayout_19.addItem(spacerItem3)
    self.page0_img_abilities_layout.addWidget(self.page0_abilities_layout)
    self.horizontalLayout_19.addLayout(self.page0_img_abilities_layout)

    return self.page0
