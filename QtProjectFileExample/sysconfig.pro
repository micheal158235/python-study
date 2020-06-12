#----------------------------------------------------
#
# Project created by QtCreator 2016-10-29T11:09:33
#
#----------------------------------------------------
QT        += core gui script sql network
#QT       -= gui
CONFIG    += plugin
#CONFIG   += console
#CONFIG   -= aqq_bundle
#CONFIG   += c++11
#CONFIG   += precompile_header
TARGET     = sysconfig
TEMPLATE   = lib
#TEMPLATE  = app
#TEMPLATE  = staticlib
win32{
CONFIG    += qaxcontainer
}
DESTDIR   += ../../target/lib

# The following define makes your compiler emit warnings if you use
# any feature of Qt which as been marked deprecated(the exact warnings depend on your compiler).
# Please consult the documentation of the deprecated API in order to know how to port your code away from it.
DEFINES   += QT_DEPRECATED_WARNINGS
# You can also make your code fail to compile if you use deprecated APIS.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIS only up to a certain version of Qt.
#DEFINES   += QT_DISABLE_DEPRECATED_BEFORE=0x060000    #disables all the APIS deprecated before Qt 6.0.0

INCLUDEPATH += ../commonlib/Notify
INCLUDEPATH += "../../parkingBox/commonlib/comFunction"

LIBS        += -L../../target/lib
LIBS        += -lcomFunction -ldbsql -lscreenshot -ljsnotify

win32{
LIBS        += -ljsonwin
}

unix{
LIBS        += -ljsonwin
LIBS        += -L../../tools/log/bin -ljslog
}

unix{
QMAKE_LFLAGS   += -fprofile-arcs -ftest-coverage
QMAKE_CXXFLAGS += -fprofile-arcs -ftest-coverage
}

include(sync/sync.pri)

SOURCES +=\
    $$PWD/menu/uiConfig.cpp \
	menu/systemmenu.cpp \
	comView/JS3StateTreeView.cpp \
	comView/JSLabel.cpp \
	main.cpp
	
HEADERS += \
	$$PWD/menu/uiConfig.h \
	menu/systemmenu.h \
	comView/JS3StateTreeView.h \
	comView/JSLabel.h \
	main.h

FORMS += \
    menu/uiConfig.ui \
	menu/systemmenu.ui \
	comView/JS3StateTreeView.ui \
	comView/JSLabel.ui \
	
OTER_FILES += \
    other/SysConfigStyle.css
	
RESOURCES += \
    menuStyle.qrc
	
QMAKE_CXXFLAGS += -Wno-unused-parameter

DISTFILES += \
    img/gate_middle.png
	