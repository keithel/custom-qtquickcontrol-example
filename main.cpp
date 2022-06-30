#include <QGuiApplication>
#include <QQmlApplicationEngine>

#include <QDirIterator>
#include <QDebug>


int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    QQmlApplicationEngine engine;
    engine.addImportPath(":/styles");
    const QUrl url(u"qrc:/custom-qtquickcontrol/main.qml"_qs);
    QObject::connect(&engine, &QQmlApplicationEngine::objectCreated,
                     &app, [url](QObject *obj, const QUrl &objUrl) {
        if (!obj && url == objUrl)
            QCoreApplication::exit(-1);
    }, Qt::QueuedConnection);
    engine.load(url);

    QDirIterator dirIter(":/", QDirIterator::Subdirectories);
    while (dirIter.hasNext()) {
        qDebug() << dirIter.next();
    }

    return app.exec();
}
