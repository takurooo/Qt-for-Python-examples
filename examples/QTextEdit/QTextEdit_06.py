# ---------------------------
# TextEditの文字のフォントを変える
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QTextEdit
from PySide2.QtGui import QFont

app = QApplication(sys.argv)

qw_text_edit = QTextEdit()
qt_font = QFont("Monaco")  # monaco fontを生成
qt_font.setStyleHint(QFont.Helvetica)  # monacoが使用できない場合はHelveticaにする
qw_text_edit.setFont(qt_font)  # fontを設定
qw_text_edit.append('This is a text edit widget.')
qw_text_edit.show()

sys.exit(app.exec_())