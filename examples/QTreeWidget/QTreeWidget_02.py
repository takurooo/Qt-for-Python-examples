import sys
from PySide2.QtWidgets import QApplication, QTreeWidget

app = QApplication(sys.argv)

qw_tree = QTreeWidget()
qw_tree.setHeaderLabels(["name", "tel", "mail"])  # Headerをつける
qw_tree.show()

sys.exit(app.exec_())