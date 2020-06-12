TEMPLATE    = subdirs

SUBDIRS += \
#    ocreSource \
     commonlib \
	 sysconfig \
	 
win32{
SUBDIRS += \ 
     centerTollgate
}

win32{
#QMAKE_CXXFLAGS += /MP
}

CONFIG    += ordered