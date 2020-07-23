# ---------------------------
# Splitterにwidgetをインデックスで指定した位置に追加する
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QSplitter, QTextEdit

app = QApplication(sys.argv)

qw_text_edit_left = QTextEdit()
qw_text_edit_left.append('left')

qw_text_edit_right = QTextEdit()
qw_text_edit_right.append('right')

qw_splitter = QSplitter()
qw_splitter.addWidget(qw_text_edit_left)
qw_splitter.addWidget(qw_text_edit_right)

qw_text_edit_center = QTextEdit()
qw_text_edit_center.append('center')
qw_splitter.insertWidget(1, qw_text_edit_center) # index 1 の位置にwidgetを追加

print(qw_splitter.indexOf(qw_text_edit_left))
print(qw_splitter.indexOf(qw_text_edit_center))
print(qw_splitter.indexOf(qw_text_edit_right))

qw_splitter.show()

sys.exit(app.exec_())