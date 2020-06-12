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
	