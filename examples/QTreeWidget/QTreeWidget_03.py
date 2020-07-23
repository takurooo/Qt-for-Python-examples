# ---------------------------
# Treeにitemを追加する
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

app = QApplication(sys.argv)

qw_tree = QTreeWidget()
qw_tree.setHeaderLabels(["name", "tel", "mail"])
qw_tree_parent_item = QTreeWidgetItem(['family'])  # Treeに追加するItemを生成
qw_tree.addTopLevelItem(qw_tree_parent_item)  # TreeにItemを追加する
qw_tree.show()

sys.exit(app.exec_())