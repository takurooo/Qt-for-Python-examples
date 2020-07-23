# ---------------------------
# SplitterでTextEditを水平に2つ表示する
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QSplitter, QTextEdit
from PySide2.QtCore import Qt

app = QApplication(sys.argv)

qw_text_edit_left = QTextEdit()
qw_text_edit_left.append('left')

qw_text_edit_right = QTextEdit()
qw_text_edit_right.append('right')

qw_splitter = QSplitter()
qw_splitter.addWidget(qw_text_edit_left) # Splitterにwidgetを追加
qw_splitter.addWidget(qw_text_edit_right) # Splitterにwidgetを追加

qw_splitter.show()

sys.exit(app.exec_())