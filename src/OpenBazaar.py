# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpenBazaar.ui'
#
# Created: Fri Nov 13 14:18:05 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_OpenBazaar(object):
    def setupUi(self, OpenBazaar):
        OpenBazaar.setObjectName(_fromUtf8("OpenBazaar"))
        OpenBazaar.resize(1163, 867)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/small_logo.jpeg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OpenBazaar.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(OpenBazaar)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabMenu = QtGui.QTabWidget(self.centralwidget)
        self.tabMenu.setTabsClosable(True)
        self.tabMenu.setObjectName(_fromUtf8("tabMenu"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.textBrowser = QtGui.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(-5, 1, 531, 441))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tabMenu.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(117, 50, 111, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 50, 98, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 50, 98, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.tabMenu.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 70, 98, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 70, 98, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.tabMenu.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_4)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 80, 98, 27))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(self.tab_4)
        self.pushButton_9.setGeometry(QtCore.QRect(250, 80, 98, 27))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.tabMenu.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.pushButton = QtGui.QPushButton(self.tab_5)
        self.pushButton.setGeometry(QtCore.QRect(127, 60, 111, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_5)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 60, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabMenu.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.pushButton_10 = QtGui.QPushButton(self.tab_6)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 60, 98, 27))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(self.tab_6)
        self.pushButton_11.setGeometry(QtCore.QRect(140, 60, 98, 27))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12 = QtGui.QPushButton(self.tab_6)
        self.pushButton_12.setGeometry(QtCore.QRect(247, 60, 111, 27))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_13 = QtGui.QPushButton(self.tab_6)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 120, 98, 27))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_14 = QtGui.QPushButton(self.tab_6)
        self.pushButton_14.setGeometry(QtCore.QRect(140, 120, 98, 27))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_15 = QtGui.QPushButton(self.tab_6)
        self.pushButton_15.setGeometry(QtCore.QRect(260, 120, 98, 27))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.tabMenu.addTab(self.tab_6, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabMenu, 7, 2, 1, 1)
        self.currencySelector = QtGui.QComboBox(self.centralwidget)
        self.currencySelector.setObjectName(_fromUtf8("currencySelector"))
        self.currencySelector.addItem(_fromUtf8(""))
        self.currencySelector.addItem(_fromUtf8(""))
        self.currencySelector.addItem(_fromUtf8(""))
        self.currencySelector.addItem(_fromUtf8(""))
        self.currencySelector.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.currencySelector, 2, 1, 1, 1)
        self.displayPicture = QtGui.QLabel(self.centralwidget)
        self.displayPicture.setText(_fromUtf8(""))
        self.displayPicture.setPixmap(QtGui.QPixmap(_fromUtf8("images/default-avatar.png")))
        self.displayPicture.setObjectName(_fromUtf8("displayPicture"))
        self.gridLayout.addWidget(self.displayPicture, 0, 0, 2, 2)
        self.merchantsList = QtGui.QListWidget(self.centralwidget)
        self.merchantsList.setObjectName(_fromUtf8("merchantsList"))
        item = QtGui.QListWidgetItem()
        self.merchantsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.merchantsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.merchantsList.addItem(item)
        self.gridLayout.addWidget(self.merchantsList, 1, 4, 4, 3)
        self.myMerchantsLabel = QtGui.QLabel(self.centralwidget)
        self.myMerchantsLabel.setObjectName(_fromUtf8("myMerchantsLabel"))
        self.gridLayout.addWidget(self.myMerchantsLabel, 0, 5, 1, 2)
        self.recentTransactionsLabel = QtGui.QLabel(self.centralwidget)
        self.recentTransactionsLabel.setObjectName(_fromUtf8("recentTransactionsLabel"))
        self.gridLayout.addWidget(self.recentTransactionsLabel, 4, 0, 1, 2)
        self.recentTransactionsTable = QtGui.QTableWidget(self.centralwidget)
        self.recentTransactionsTable.setObjectName(_fromUtf8("recentTransactionsTable"))
        self.recentTransactionsTable.setColumnCount(2)
        self.recentTransactionsTable.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.recentTransactionsTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.recentTransactionsTable.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.recentTransactionsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.recentTransactionsTable.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.recentTransactionsTable, 5, 0, 3, 2)
        self.addStoreText = QtGui.QLineEdit(self.centralwidget)
        self.addStoreText.setObjectName(_fromUtf8("addStoreText"))
        self.gridLayout.addWidget(self.addStoreText, 5, 4, 1, 2)
        self.addStoreButton = QtGui.QPushButton(self.centralwidget)
        self.addStoreButton.setObjectName(_fromUtf8("addStoreButton"))
        self.gridLayout.addWidget(self.addStoreButton, 5, 6, 1, 1)
        self.myNotariesLabel = QtGui.QLabel(self.centralwidget)
        self.myNotariesLabel.setObjectName(_fromUtf8("myNotariesLabel"))
        self.gridLayout.addWidget(self.myNotariesLabel, 6, 5, 1, 2)
        self.myNotariesList = QtGui.QListWidget(self.centralwidget)
        self.myNotariesList.setObjectName(_fromUtf8("myNotariesList"))
        item = QtGui.QListWidgetItem()
        self.myNotariesList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.myNotariesList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.myNotariesList.addItem(item)
        self.gridLayout.addWidget(self.myNotariesList, 7, 4, 1, 3)
        self.addNotaryText = QtGui.QLineEdit(self.centralwidget)
        self.addNotaryText.setObjectName(_fromUtf8("addNotaryText"))
        self.gridLayout.addWidget(self.addNotaryText, 8, 4, 1, 2)
        self.addNotaryButton = QtGui.QPushButton(self.centralwidget)
        self.addNotaryButton.setObjectName(_fromUtf8("addNotaryButton"))
        self.gridLayout.addWidget(self.addNotaryButton, 8, 6, 1, 1)
        self.searchBarText = QtGui.QLineEdit(self.centralwidget)
        self.searchBarText.setObjectName(_fromUtf8("searchBarText"))
        self.gridLayout.addWidget(self.searchBarText, 2, 2, 1, 1)
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.gridLayout.addWidget(self.searchButton, 2, 3, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.openBazaarBanner = QtGui.QLabel(self.centralwidget)
        self.openBazaarBanner.setText(_fromUtf8(""))
        self.openBazaarBanner.setPixmap(QtGui.QPixmap(_fromUtf8("images/logo.png")))
        self.openBazaarBanner.setObjectName(_fromUtf8("openBazaarBanner"))
        self.gridLayout.addWidget(self.openBazaarBanner, 1, 2, 1, 1)
        OpenBazaar.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(OpenBazaar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1163, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHome = QtGui.QMenu(self.menubar)
        self.menuHome.setObjectName(_fromUtf8("menuHome"))
        self.menuMessages = QtGui.QMenu(self.menubar)
        self.menuMessages.setObjectName(_fromUtf8("menuMessages"))
        self.menuContracts = QtGui.QMenu(self.menubar)
        self.menuContracts.setObjectName(_fromUtf8("menuContracts"))
        self.menuStore = QtGui.QMenu(self.menubar)
        self.menuStore.setObjectName(_fromUtf8("menuStore"))
        self.menuNotaries = QtGui.QMenu(self.menubar)
        self.menuNotaries.setObjectName(_fromUtf8("menuNotaries"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        OpenBazaar.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(OpenBazaar)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        OpenBazaar.setStatusBar(self.statusbar)
        self.actionMy_Listings = QtGui.QAction(OpenBazaar)
        self.actionMy_Listings.setObjectName(_fromUtf8("actionMy_Listings"))
        self.actionMy_Orders = QtGui.QAction(OpenBazaar)
        self.actionMy_Orders.setObjectName(_fromUtf8("actionMy_Orders"))
        self.actionMy_Settings = QtGui.QAction(OpenBazaar)
        self.actionMy_Settings.setObjectName(_fromUtf8("actionMy_Settings"))
        self.actionSend_a_Message = QtGui.QAction(OpenBazaar)
        self.actionSend_a_Message.setObjectName(_fromUtf8("actionSend_a_Message"))
        self.actionInbo = QtGui.QAction(OpenBazaar)
        self.actionInbo.setObjectName(_fromUtf8("actionInbo"))
        self.actionOutbox = QtGui.QAction(OpenBazaar)
        self.actionOutbox.setObjectName(_fromUtf8("actionOutbox"))
        self.actionPurchased = QtGui.QAction(OpenBazaar)
        self.actionPurchased.setObjectName(_fromUtf8("actionPurchased"))
        self.actionSold = QtGui.QAction(OpenBazaar)
        self.actionSold.setObjectName(_fromUtf8("actionSold"))
        self.actionActive = QtGui.QAction(OpenBazaar)
        self.actionActive.setObjectName(_fromUtf8("actionActive"))
        self.actionCreate_a_Store = QtGui.QAction(OpenBazaar)
        self.actionCreate_a_Store.setObjectName(_fromUtf8("actionCreate_a_Store"))
        self.actionView_a_Store = QtGui.QAction(OpenBazaar)
        self.actionView_a_Store.setObjectName(_fromUtf8("actionView_a_Store"))
        self.actionFind = QtGui.QAction(OpenBazaar)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.actionBecome_a_Notary = QtGui.QAction(OpenBazaar)
        self.actionBecome_a_Notary.setObjectName(_fromUtf8("actionBecome_a_Notary"))
        self.actionFind_a_Notary = QtGui.QAction(OpenBazaar)
        self.actionFind_a_Notary.setObjectName(_fromUtf8("actionFind_a_Notary"))
        self.actionHelp_with_Notaries = QtGui.QAction(OpenBazaar)
        self.actionHelp_with_Notaries.setObjectName(_fromUtf8("actionHelp_with_Notaries"))
        self.actionGet_Help_Online = QtGui.QAction(OpenBazaar)
        self.actionGet_Help_Online.setObjectName(_fromUtf8("actionGet_Help_Online"))
        self.actionUser_Guide = QtGui.QAction(OpenBazaar)
        self.actionUser_Guide.setObjectName(_fromUtf8("actionUser_Guide"))
        self.menuHome.addAction(self.actionMy_Listings)
        self.menuHome.addAction(self.actionMy_Orders)
        self.menuHome.addAction(self.actionMy_Settings)
        self.menuHome.addSeparator()
        self.menuMessages.addAction(self.actionSend_a_Message)
        self.menuMessages.addAction(self.actionInbo)
        self.menuMessages.addAction(self.actionOutbox)
        self.menuContracts.addAction(self.actionPurchased)
        self.menuContracts.addAction(self.actionSold)
        self.menuContracts.addAction(self.actionActive)
        self.menuStore.addAction(self.actionCreate_a_Store)
        self.menuStore.addAction(self.actionView_a_Store)
        self.menuStore.addAction(self.actionFind)
        self.menuNotaries.addAction(self.actionBecome_a_Notary)
        self.menuNotaries.addAction(self.actionFind_a_Notary)
        self.menuNotaries.addAction(self.actionHelp_with_Notaries)
        self.menuHelp.addAction(self.actionGet_Help_Online)
        self.menuHelp.addAction(self.actionUser_Guide)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuMessages.menuAction())
        self.menubar.addAction(self.menuContracts.menuAction())
        self.menubar.addAction(self.menuStore.menuAction())
        self.menubar.addAction(self.menuNotaries.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(OpenBazaar)
        self.tabMenu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OpenBazaar)

    def retranslateUi(self, OpenBazaar):
        OpenBazaar.setWindowTitle(_translate("OpenBazaar", "OpenBazaar", None))
        self.tabMenu.setTabText(self.tabMenu.indexOf(self.tab), _translate("OpenBazaar", "Home", None))
        self.pushButton_3.setText(_translate("OpenBazaar", "Send a Message", None))
        self.pushButton_4.setText(_translate("OpenBazaar", "Inbox", None))
        self.pushButton_5.setText(_translate("OpenBazaar", "Outbox", None))
        self.tabMenu.setTabText(self.tabMenu.indexOf(self.tab_2), _translate("OpenBazaar", "Messages", None))
        self.pushButton_6.setText(_translate("OpenBazaar", "My Sales", None))
        self.pushButton_7.setText(_translate("OpenBazaar", "My Purchases", None))
        self.tabMenu.setTabText(self.tabMenu.indexOf(self.tab_3), _translate("OpenBazaar", "Orders", None))
        self.pushButton_8.setText(_translate("OpenBazaar", "Notarized", None))
        self.pushButton_9.setText(_translate("OpenBazaar", "Pending", None))
        self.tabMenu.setTabText(self.tabMenu.indexOf(self.tab_4), _translate("OpenBazaar", "Notarizations", None))
        self.pushButton.setText(_translate("OpenBazaar", "Add a Contract", None))
        self.pushButton_2.setText(_translate("OpenBazaar", "Republish", None))
        self.tabMenu.setTabText(self.tabMenu.indexOf(self.tab_5), _translate("OpenBazaar", "Contracts", None))
        self.pushButton_10.setText(_translate("OpenBazaar", "Store Info", None))
        self.pushButton_11.setText(_translate("OpenBazaar", "Keys", None))
        self.pushButton_12.setText(_translate("OpenBazaar", "Communication", None))
        self.pushButton_13.setText(_translate("OpenBazaar", "Notary", None))
        self.pushButton_14.setText(_translate("OpenBazaar", "Advanced", None))
        self.pushButton_15.setText(_translate("OpenBazaar", "Backup", None))
        self.tabMenu.setTabText(self.tabMenu.indexOf(self.tab_6), _translate("OpenBazaar", "Settings", None))
        self.currencySelector.setItemText(0, _translate("OpenBazaar", "CAD", None))
        self.currencySelector.setItemText(1, _translate("OpenBazaar", "MBTC", None))
        self.currencySelector.setItemText(2, _translate("OpenBazaar", "BTC", None))
        self.currencySelector.setItemText(3, _translate("OpenBazaar", "USD", None))
        self.currencySelector.setItemText(4, _translate("OpenBazaar", "EUR", None))
        __sortingEnabled = self.merchantsList.isSortingEnabled()
        self.merchantsList.setSortingEnabled(False)
        item = self.merchantsList.item(0)
        item.setText(_translate("OpenBazaar", "Merchant 1", None))
        item = self.merchantsList.item(1)
        item.setText(_translate("OpenBazaar", "Merchant 2", None))
        item = self.merchantsList.item(2)
        item.setText(_translate("OpenBazaar", "Merchant 3", None))
        self.merchantsList.setSortingEnabled(__sortingEnabled)
        self.myMerchantsLabel.setText(_translate("OpenBazaar", "My Merchants", None))
        self.recentTransactionsLabel.setText(_translate("OpenBazaar", "Recent Transactions", None))
        item = self.recentTransactionsTable.verticalHeaderItem(0)
        item.setText(_translate("OpenBazaar", "Fake Transaction 1", None))
        item = self.recentTransactionsTable.verticalHeaderItem(1)
        item.setText(_translate("OpenBazaar", "Fake Transaction 2", None))
        item = self.recentTransactionsTable.horizontalHeaderItem(0)
        item.setText(_translate("OpenBazaar", "Date", None))
        item = self.recentTransactionsTable.horizontalHeaderItem(1)
        item.setText(_translate("OpenBazaar", "Price", None))
        self.addStoreText.setText(_translate("OpenBazaar", "Enter Store GUID", None))
        self.addStoreButton.setText(_translate("OpenBazaar", "Add Store", None))
        self.myNotariesLabel.setText(_translate("OpenBazaar", "My Notaries", None))
        __sortingEnabled = self.myNotariesList.isSortingEnabled()
        self.myNotariesList.setSortingEnabled(False)
        item = self.myNotariesList.item(0)
        item.setText(_translate("OpenBazaar", "Notary 1", None))
        item = self.myNotariesList.item(1)
        item.setText(_translate("OpenBazaar", "Notary 2", None))
        item = self.myNotariesList.item(2)
        item.setText(_translate("OpenBazaar", "Notary 3", None))
        self.myNotariesList.setSortingEnabled(__sortingEnabled)
        self.addNotaryText.setText(_translate("OpenBazaar", "Enter Notary GUID", None))
        self.addNotaryButton.setText(_translate("OpenBazaar", "Add Notary", None))
        self.searchBarText.setText(_translate("OpenBazaar", "Search the OpenBazaar!", None))
        self.searchButton.setText(_translate("OpenBazaar", "Search", None))
        self.label.setText(_translate("OpenBazaar", "$14,092", None))
        self.menuHome.setTitle(_translate("OpenBazaar", "Home", None))
        self.menuMessages.setTitle(_translate("OpenBazaar", "Messages", None))
        self.menuContracts.setTitle(_translate("OpenBazaar", "Contracts", None))
        self.menuStore.setTitle(_translate("OpenBazaar", "Stores", None))
        self.menuNotaries.setTitle(_translate("OpenBazaar", "Notaries", None))
        self.menuHelp.setTitle(_translate("OpenBazaar", "Help", None))
        self.actionMy_Listings.setText(_translate("OpenBazaar", "My Listings", None))
        self.actionMy_Orders.setText(_translate("OpenBazaar", "My Orders", None))
        self.actionMy_Settings.setText(_translate("OpenBazaar", "My Settings", None))
        self.actionSend_a_Message.setText(_translate("OpenBazaar", "Send a Message", None))
        self.actionInbo.setText(_translate("OpenBazaar", "Inbox", None))
        self.actionOutbox.setText(_translate("OpenBazaar", "Outbox", None))
        self.actionPurchased.setText(_translate("OpenBazaar", "Purchased", None))
        self.actionSold.setText(_translate("OpenBazaar", "Sold", None))
        self.actionActive.setText(_translate("OpenBazaar", "Active", None))
        self.actionCreate_a_Store.setText(_translate("OpenBazaar", "Create a Store", None))
        self.actionView_a_Store.setText(_translate("OpenBazaar", "View a Store", None))
        self.actionFind.setText(_translate("OpenBazaar", "Find a Store", None))
        self.actionBecome_a_Notary.setText(_translate("OpenBazaar", "Become a Notary", None))
        self.actionFind_a_Notary.setText(_translate("OpenBazaar", "Find a Notary", None))
        self.actionHelp_with_Notaries.setText(_translate("OpenBazaar", "Help with Notaries", None))
        self.actionGet_Help_Online.setText(_translate("OpenBazaar", "Get Help Online", None))
        self.actionUser_Guide.setText(_translate("OpenBazaar", "User Guide", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    OpenBazaar = QtGui.QMainWindow()
    ui = Ui_OpenBazaar()
    ui.setupUi(OpenBazaar)
    OpenBazaar.show()
    sys.exit(app.exec_())

