# CMakeList.txt: 顶级CMake项目文件，执行全局配置和此处的包含子项目

cmake_minimum_required (VERSION 3.8)

PROJECT ("pcs")

#包含子项目
ADD_SUBDIRECTORY ("pcs")
ADD_SUBDIRECTORY ("jsst.pcs.network_manager")

#设置安装目录
IF (WIN32)
    SET (CMAKE_INSTALL_FREFIX /usr/local)
ELSEIF (UNIX)
    SET (CMAKE_INSTALL_FREFIX ./bin)
ELSEIF (APPLE)
    SET (CMAKE_INSTALL_FREFIX ./bin)
ENDIF (WIN32)

#设置对c++11 支持
SET (CMAKE_CXX_FLAGS "$CMAKE_CXX_FLAGS" -std=c++11) #-std=c++0x

#设置编译目录
#SET (CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/pcsoutput)
#SET (CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/pcsoutput)
#SET (CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/pcsoutput)

#设置安装目录
#SET (EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/pcsoutput)
#SET (LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/pcsoutput})












