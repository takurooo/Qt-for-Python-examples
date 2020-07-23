# ---------------------------
# SplitterでTextEditを垂直に2つ表示する
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QSplitter, QTextEdit
from PySide2.QtCore import Qt

app = QApplication(sys.argv)

qw_text_edit_top = QTextEdit()
qw_text_edit_top.append('top')

qw_text_edit_bottom = QTextEdit()
qw_text_edit_bottom.append('bottom')

qw_splitter = QSplitter()
qw_splitter.setOrientation(Qt.Orientation.Vertical)  # Splitterを垂直に設定
print(qw_splitter.orientation())
qw_splitter.addWidget(qw_text_edit_top)
qw_splitter.addWidget(qw_text_edit_bottom)

qw_splitter.show()

sys.exit(app.exec_())