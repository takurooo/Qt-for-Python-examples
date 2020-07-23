# ---------------------------
# Treeを表示する
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QTreeWidget

app = QApplication(sys.argv)

qw_tree = QTreeWidget()
qw_tree.show()

sys.exit(app.exec_())