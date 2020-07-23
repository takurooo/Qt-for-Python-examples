# ---------------------------
# Splitterの左右の比率を変える
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QSplitter, QTextEdit

app = QApplication(sys.argv)

qw_text_edit_left = QTextEdit()
qw_text_edit_left.append('left')

qw_text_edit_right = QTextEdit()
qw_text_edit_right.append('right')

qw_splitter = QSplitter() # Orientationの初期値は水平
qw_splitter.addWidget(qw_text_edit_left)
qw_splitter.addWidget(qw_text_edit_right)

qw_splitter_size = qw_splitter.size() # Splitterのサイズを取得する
qw_splitter_size_width = qw_splitter_size.width() # Splitterの横サイズを取得する
qw_splitter.setSizes([qw_splitter_size_width*0.1, qw_splitter_size_width*0.9]) # Splitterの横の比率を1:9に変更する
print(qw_splitter.size()) # Splitter全体のサイズ
print(qw_splitter.sizes()) # Splitterの子widgetごとのサイズ

qw_splitter.show()

sys.exit(app.exec_())