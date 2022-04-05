"""
AnkiMaker v0.0.1 by RealEmeralds - Easily make Anki cards to learn a new language

Note: Still have to improve + add quite a bit of functionality
Also really shit code

I spent too much time on this - I have a Chinese test tmr (lol)
"""

import sys
sys.path.insert(1, "assets")
import googletrans
from googletrans import Translator  # idfk why I need this
from sinopy import pinyin
import codecs
from betaui1 import Ui_AnkiMaker
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
import pickle


class AppWindow(qtw.QMainWindow):
    # defining class Variables
    translator = Translator(service_urls=['translate.googleapis.com'])
    toTranslate = ""
    currentDefinition = ""
    originalPronunciation = ""
    newPronunciation = ""
    tags = []
    appearance = 0
    waitingIndex = 0
    translatorInstance = ""
    spaget = False
    holding = []
    holdingIndex = []
    removed = []
    removedIndex = []

    def __init__(self, *args, **kwargs):
        # Inherit the MainWindow properties
        super().__init__(*args, **kwargs)

        # Instantiate UI
        self.ui = Ui_AnkiMaker()
        self.ui.setupUi(self)
        self.ui.timer = qtc.QTimer()

        # Set attributes for UI
        self.ui.tags.lineEdit().setPlaceholderText("<Enter> to save tag")
        self.ui.tags.lineEdit().setFont(qtg.QFont("Google Sans", 10))
        self.ui.tags.addItems(self.__class__.tags)
        self.ui.statusbar.showMessage("Waiting...")

        # Set application name and icon
        self.setWindowIcon(qtg.QIcon('assets/AnkiMakerLogo.png'))
        self.setWindowTitle("AnkiMaker")

        # Set signals
        self.ui.totranslate.textChanged.connect(self.updateResults)
        self.ui.comboBox.currentIndexChanged.connect(self.updateResults)
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.ui.newpronounce.setText(""))
        self.ui.tags.currentIndexChanged.connect(self.storeSettings)
        self.ui.timer.timeout.connect(self.timeoutEvent)
        self.ui.actionMultiple_2.triggered.connect(lambda: self.changeCards(0))
        self.ui.actionCloseDefinition.triggered.connect(lambda: self.changeCards(1))
        self.ui.actionCloseTranslated.triggered.connect(lambda: self.changeCards(2))
        self.ui.actionUndo.triggered.connect(self.removeFromHold)
        self.ui.actionRedo.triggered.connect(self.restoreFromRemoved)
        self.ui.translated.textEdited.connect(self.resultsUpdated)
        self.ui.totranslate.returnPressed.connect(lambda: self.holdBeforeCSV(self.__class__.toTranslate,
                                                                            self.__class__.currentDefinition,
                                                                            self.__class__.originalPronunciation,
                                                                            self.__class__.newPronunciation,
                                                                            self.ui.tags.currentText()))
        self.ui.translated.returnPressed.connect(lambda: self.holdBeforeCSV(self.__class__.toTranslate,
                                                                            self.__class__.currentDefinition,
                                                                            self.__class__.originalPronunciation,
                                                                            self.__class__.newPronunciation,
                                                                            self.ui.tags.currentText()))
        self.ui.submitButton.clicked.connect(lambda: self.holdBeforeCSV(self.__class__.toTranslate,
                                                                        self.__class__.currentDefinition,
                                                                        self.__class__.originalPronunciation,
                                                                        self.__class__.newPronunciation,
                                                                        self.ui.tags.currentText()))

        # Load settings
        self.loadSettings()

        # Load StatusBar
        self.ui.timer.start(0)

    def closeEvent(self, a0: qtg.QCloseEvent) -> None:  # Runs as application closes
        self.writeIntoCSV()  # Write everything in holding into CSV file
        with open('assets/config.pickle', 'wb') as f:  # Save settings in pickle file
            pickle.dump([self.__class__.tags, self.__class__.appearance, self.__class__.cardType], f)

    def loadSettings(self):
        try:
            with open("assets/config.pickle", "rb") as f:
                stuff = pickle.load(f)
                self.__class__.tags = stuff[0]
                self.__class__.appearance = stuff[1]
                self.changeCards(stuff[2])
        except Exception:
            with open("assets/config.pickle", "wb") as f:  # Creates file if it doesn't exist
                pass
            self.changeCards(0)

        self.ui.tags.addItems(self.__class__.tags)

    def storeSettings(self):
        # append tag to class variable tags
        if self.ui.tags.currentText() not in self.__class__.tags:
            self.__class__.tags.append(self.ui.tags.currentText())

    def timeoutEvent(self):  # Event that runs every time QTimer expires, used to update status
        if self.ui.totranslate.text() == "":
            waitingList = ["Waiting...", "Waiting..", "Waiting."]
            self.ui.statusbar.showMessage(waitingList[self.__class__.waitingIndex % 3], 1000)
            self.__class__.waitingIndex += 1
            self.ui.timer.start(250)

    def changeCards(self, number):
        # Triggered when a checkbox is clicked to change how cards are saved
        self.__class__.cardType = number
        self.ui.actionCloseDefinition.setChecked(False)
        self.ui.actionMultiple_2.setChecked(False)
        self.ui.actionCloseTranslated.setChecked(False)
        actions = [self.ui.actionMultiple_2.setChecked,
                   self.ui.actionCloseDefinition.setChecked,
                   self.ui.actionCloseTranslated.setChecked]
        actions[number](True)

    def updateResults(self):
        # Does a translation when top box is modified, and bottom box hasn't been modified since last clear
        self.__class__.toTranslate = self.ui.totranslate.text()  # Put text from search box into
                                                                 # toTranslate class variable
        destChoice = self.ui.comboBox.currentText()
        destChoiceDict = googletrans.LANGUAGES  # Translate combobox option to language code
        destChoiceCode = ""
        for k, v in destChoiceDict.items():  # Find language code for translation
            if v == destChoice.lower():
                destChoiceCode = k
                break
        assert destChoiceCode != "", "No language to translate to found!"

        if not self.__class__.spaget:
            # Translate the text using GoogleTrans
            self.__class__.translatorInstance = self.translator.translate(self.__class__.toTranslate,
                                                                          dest=destChoiceCode)
            self.__class__.currentDefinition = self.__class__.translatorInstance.text  # Grab translated text

        if self.__class__.toTranslate == "":  # Clear pronunciation fields if the toTranslate box is empty
            self.ui.hanyu.setText("")
            self.ui.newpronounce.setText("")
            self.__class__.newPronunciation = ""
            self.__class__.originalPronunciation = ""
            self.__class__.spaget = False

        elif self.__class__.translatorInstance.src == "zh-CN" or self.__class__.translatorInstance.src == "zh-TW":
            # Show pinyin if translating from chinese
            self.__class__.originalPronunciation = pinyin(self.__class__.toTranslate, variant='mandarin')
            self.ui.hanyu.setText(self.__class__.originalPronunciation)
        # Show destination language pronunciation if not translating to english
        if self.__class__.translatorInstance.dest != "en":
            self.__class__.newPronunciation = self.__class__.translatorInstance.pronunciation
            self.ui.newpronounce.setText(self.__class__.newPronunciation)

        if not self.__class__.spaget:
            self.ui.translated.setText(self.__class__.currentDefinition)

    def resultsUpdated(self):
        # Locks the translate text edit from editing by updateResults
        if self.__class__.toTranslate == "":
            return
        self.__class__.spaget = True
        self.ui.newpronounce.setText("")
        self.__class__.newPronunciation = ""
        self.__class__.currentDefinition = self.ui.translated.text()

    def holdBeforeCSV(self, definition: str, character: str, oldpronunciation="", newpronunciation="", tags=""):
        if not definition or not character:
            # function does not run if fields are not filled up
            self.ui.statusbar.showMessage("Error: Fill up fields before submitting", 2000)
            self.ui.timer.start(2000)
            return None

        # Add brackets to pronunciation if they exist
        if oldpronunciation:
            oldpronunciation = f"({oldpronunciation})"
        if newpronunciation:
            newpronunciation = f"({newpronunciation})"

        # Append arguments to a class variable based on the class variable CardType
        if self.__class__.cardType == 0:
            AppWindow.holding.append(f"{definition}<br><br>{{{{c1::{character} {oldpronunciation}{newpronunciation}}}}},{tags}")
            AppWindow.holding.append(f"{character}<br><br>{{{{c1::{definition}}}}}, {oldpronunciation} {newpronunciation},{tags}")
            AppWindow.holdingIndex.append(2)
        elif self.__class__.cardType == 1:
            AppWindow.holding.append(f"{character}<br><br>{{{{c1::{definition}{oldpronunciation} {newpronunciation}}}}},{tags}")
            AppWindow.holdingIndex.append(1)
        elif self.__class__.cardType == 2:
            AppWindow.holding.append(f"{definition}<br><br>{{{{c1::{character}{oldpronunciation} {newpronunciation}}}}}, {tags}")
            AppWindow.holdingIndex.append(1)

        # Refresh status, clear terminal
        if tags:
            self.ui.statusbar.showMessage(f"Added \"{character}\" to CSV with tag \"{tags}\"", 2000)
            self.ui.timer.start(2000)
        else:
            self.ui.statusbar.showMessage(f"Added \"{character}\" to CSV with NO tag", 2000)
            self.ui.timer.start(2000)
        self.ui.totranslate.setText("")
        self.ui.translated.setText("")

    def removeFromHold(self):
        if not AppWindow.holding:
            self.ui.statusbar.showMessage("Nothing to undo...", 2000)
            self.ui.timer.start(2000)
            return
        length = AppWindow.holdingIndex.pop()
        for i in range(length):
            AppWindow.removed.append(AppWindow.holding.pop())
        AppWindow.removedIndex.append(length)
        self.ui.statusbar.showMessage(f"Removed card(s) with \"{AppWindow.removed[-1].partition('<br><br>')[0]}\" and \"{AppWindow.removed[-1].partition('<br><br>')[2].partition(',')[0].strip('{}c1:')}\"", 2000)
        self.ui.timer.start(2000)

    def restoreFromRemoved(self):
        print(AppWindow.removed)
        print(len(AppWindow.removed))
        if not AppWindow.removed:
            self.ui.statusbar.showMessage("Nothing to redo...", 2000)
            self.ui.timer.start(2000)
            return
        length = AppWindow.removedIndex.pop()
        for i in range(length):
            AppWindow.holding.append(AppWindow.removed.pop())
        self.__class__.holdingIndex.append(length)
        self.ui.statusbar.showMessage(
            f"Restored card(s) with \"{AppWindow.holding[-1].partition('<br><br>')[0]}\" and \"{AppWindow.holding[-1].partition('<br><br>')[2].partition(',')[0].strip('{}c1:')}\"",
            2000)
        self.ui.timer.start(2000)

    def writeIntoCSV(self):
        with codecs.open('assets/Import_Me.csv', 'a+', encoding='utf-8') as f:
            f.seek(0)
            f.write('\n'.join(AppWindow.holding))
            f.seek(0)

        self.ui.totranslate.clear()


def main():
    app = qtw.QApplication([])
    window = AppWindow()
    window.show()
    # Execute the app
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
