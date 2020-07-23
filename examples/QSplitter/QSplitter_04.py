# ---------------------------
# Splitterの子widgetのサイズ調整をしたときに調整完了後にサイズを変更する
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

qw_splitter.setOpaqueResize(False) # 子widgetのサイズ調整を操作完了後に行う
print(qw_splitter.opaqueResize())

qw_splitter.show()

sys.exit(app.exec_())