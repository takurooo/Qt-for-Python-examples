# ---------------------------
# TextEditのカーソルの位置を変える
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QTextEdit
from PySide2.QtGui import QTextCursor

app = QApplication(sys.argv)

qw_text_edit = QTextEdit()
for i in range(20):
    qw_text_edit.append(str(i))

first_row_block = qw_text_edit.document().findBlockByLineNumber(0)  # 1行目のblockを取得
text_cursor = QTextCursor(first_row_block)  # カーソルを取得
qw_text_edit.setTextCursor(text_cursor)  # cursorを1行目に設定

qw_text_edit.show()

sys.exit(app.exec_())