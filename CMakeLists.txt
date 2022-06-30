cmake_minimum_required(VERSION 3.16)

project(custom-qtquickcontrol-test VERSION 0.1 LANGUAGES CXX)

set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 6.2 COMPONENTS Quick REQUIRED)

qt_add_executable(appcustom-qtquickcontrol-test
    main.cpp
)

qt_add_resources(appcustom-qtquickcontrol-test "base_resources"
    PREFIX "/"
    BASE "resources"
    FILES
        resources/qtquickcontrols2.conf
)

qt_add_resources(appcustom-qtquickcontrol-test "qtquickcontrols2_style_mystyle"
    PREFIX "/"
    BASE "resources"
    FILES
        resources/styles/MyStyle/qmldir
        resources/styles/MyStyle/Button.qml
        resources/styles/MyStyle/ComboBox.qml
        resources/styles/MyStyle/Label.qml
        resources/styles/MyStyle/RoundButton.qml
        resources/styles/MyStyle/TabBar.qml
        resources/styles/MyStyle/TabButton.qml
)

qt_add_qml_module(appcustom-qtquickcontrol-test
    URI custom-qtquickcontrol-test
    VERSION 1.0
    QML_FILES main.qml 
)

set_target_properties(appcustom-qtquickcontrol-test PROPERTIES
    MACOSX_BUNDLE_GUI_IDENTIFIER my.example.com
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

target_compile_definitions(appcustom-qtquickcontrol-test
    PRIVATE $<$<OR:$<CONFIG:Debug>,$<CONFIG:RelWithDebInfo>>:QT_QML_DEBUG>)
target_link_libraries(appcustom-qtquickcontrol-test
    PRIVATE Qt6::Quick)
