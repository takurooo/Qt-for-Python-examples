# Qt-for-Python-examples

Examples for [Qt for Python(PySide2)](https://www.qt.io/qt-for-python)

# インストール
```
pip install pyside2
```

# 基本

![sample](https://user-images.githubusercontent.com/35373553/88448941-e8c9e200-ce7d-11ea-86a8-a691f1fdbd0d.png)

```python
import sys
from PySide2.QtWidgets import QApplication, QTreeWidget

app = QApplication(sys.argv)

qw_tree = QTreeWidget()
qw_tree.show()

sys.exit(app.exec_())
```

- QtではWidgetと呼ばれる部品を使うことで色々なGUIを作ることができる。  
- ``QApplication()``はWidget関連の初期化をするので、Widgetを使う前に実行しなければならない。  
- ``QTreeWidget()``はツリー形式のGUIを作るためのWidget。  
- Widgetを表示するためには、show()を実行する。show()は全てのWidgetが持つメソッド。  
- ``sys.exit(app.exec_())``でQtのメインループに入る。

ということで、GUIを作るためには``QApplication()``と``sys.exit(app.exec_())``の間で
  1. **必要なWidgetを定義**
  2. **Widgetのメソッドであるshow()を実行**  

が必要になる。


### see also
- [QTreeWidgetの基本的なこと](https://takuroooooo.hatenablog.com/entry/2020/01/12/QTreeWidget%E3%81%AE%E5%9F%BA%E6%9C%AC%E7%9A%84%E3%81%AA%E3%81%93%E3%81%A8)
- [QTextEditの基本的なこと](https://takuroooooo.hatenablog.com/entry/2020/01/26/QTextEdit%E3%81%AE%E5%9F%BA%E6%9C%AC%E7%9A%84%E3%81%AA%E3%81%93%E3%81%A8)
- [QSplitterの基本的なこと](https://takuroooooo.hatenablog.com/entry/2020/07/23/QSplitter%E3%81%AE%E5%9F%BA%E6%9C%AC%E7%9A%84%E3%81%AA%E3%81%93%E3%81%A8)
- [QStackedWidgetの基本的なこと](https://takuroooooo.hatenablog.com/entry/2020/07/23/QStackedWidget%E3%81%AE%E5%9F%BA%E6%9C%AC%E7%9A%84%E3%81%AA%E3%81%93%E3%81%A8)	
