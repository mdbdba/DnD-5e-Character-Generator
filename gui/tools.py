from PyQt4 import QtGui, QtCore
import random
from string import replace, lower
import math

import core.proficiency as pfy


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

def totalMoney(money):
    """ Transform all the money in cp
    """
    value = money['cp'] + 10*money['sp']
    return value + 100*money['gp']    

def formatMoney(money):
    ret_dict = {'gp': 0, 'sp': 0, 'cp': 0}
    ret_dict['gp'] = int(money)/100
    money -= ret_dict['gp']*100
    ret_dict['sp'] = int(money)/10
    money -= ret_dict['sp']*10
    ret_dict['cp'] = int(money)
    return ret_dict

def getMoneyFromString(money):
    temp = money.split(',')
    money = 0
    for i in temp:
        if 'gp' in i:
            money += 100*int(i.split(' ')[0])
        elif 'sp' in i:
            money += 10*int(i.split(' ')[0])
        elif 'cp' in i:
            money += int(i.split(' ')[0])
    return money

def generateMoneyString(money):
    if isinstance(money, int):
        money = formatMoney(money)
    text = str(money['gp']) + " gp, "
    text += str(money['sp']) + " sp, "
    text += str(money['cp']) + " cp"
    return text
    
def rollDice(number_dice, type_dice):
    """ roll (number_dice)d(type_dice)
    :param int number_dice: Number of dice to roll
    :param int type_dice: Type of dice (d4, d6, ...)
    :returns: Value
    """
    value = 0
    for i in range(number_dice):
        value += random.randint(1,type_dice)
    return value

def rollAbility():
    """ Roll 4d6 and remove the lowest one.
    :return: Value of the rolls
    """
    rolls = [rollDice(1,6), rollDice(1,6), rollDice(1,6), rollDice(1,6)]
    min_ind = rolls.index(min(rolls))
    value = 0
    for i in range(len(rolls)):
        if i != min_ind:
            value += rolls[i]
    return value

def choiceLabel(title):
    """ Make the title nice
    :param str title: String to process
    :returns: str with a nice presentation
    """
    title = title.title()
    return replace(title, '_', ' ')

def getWeapons(weapon_type):
    weapons = []
    if weapon_type == 'simple':
        for i in range(15):
            weapons.append(choiceLabel(pfy.WeaponProficiency(i).name))
    elif weapon_type == 'martial':
        for i in range(15, 38):
            weapons.append(choiceLabel(pfy.WeaponProficiency(i).name))

    return weapons
            
def getLanguages(allow_exotic=False):
    """ Return the list of available languages
    :param bool allow_exotic: Add the exotic languages to the list
    :returns: [str] List of all the available languages
    """
    languages = ['Common', 'Dwarvish', 'Elvish', 'Giant', 'Gnomish',
                 'Goblin', 'Halfling', 'Orc']
    if allow_exotic:
        languages.extend(['Abyssal', 'Celestial', 'Draconic', 'Deep Speech',
                          'Infernal', 'Primordial', 'Sylvan', 'Undercommon'])
    return languages


def createObjectProficiencyLabel(
        self, list_prof, enum_prof, current_index=0, parent='loader',
        column=2):
    """
    :param list list_prof: Proficiency list from the class Proficiency
    :param Enum enum_prof: Enum proficiency class
    """
    if parent == 'loader':
        grid = self.gridLayout_16
        object_layout = self.object_proficiency_layout
        list_object = self.list_object
    elif parent == 'play':
        grid = self.object_gridLayout
        object_layout = self.tab0_object_layout
        list_object = self.tab0_list_object
        
    for i in range(len(list_prof)):
        if list_prof[i]:
            label = QtGui.QLabel(
                choiceLabel(enum_prof(i).name),
                object_layout)
            label.setAlignment(QtCore.Qt.AlignCenter)
            grid.addWidget(
                label, int(current_index/column),
                current_index%column)
            list_object.append(label)
            current_index += 1
    return current_index

