import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QDirIterator, qDebug, QUrl
import resources


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.addImportPath(":/styles")

    created_obj = False
    url = QUrl("./main.qml");
    def object_created_slot(obj, url):
        global created_obj
        created_obj = (obj is not None)
        if obj is None and url == objUrl:
            QGuiApplication.exit(-1)
    engine.objectCreated.connect(object_created_slot)

    engine.load(url)

    dir_iter = QDirIterator(":/", QDirIterator.Subdirectories)
    while dir_iter.hasNext():
        qDebug(dir_iter.next())

    sys.exit(app.exec())
