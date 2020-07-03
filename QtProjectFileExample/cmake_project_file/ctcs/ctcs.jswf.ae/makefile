## 源代码文件路径
SRC_PATH = .
INC = -I/usr/local/include/

## 默认编译debug版本
version = debug
## 默认编译32位程序
platform = arm400

ifeq ($(platform), x64)
    CPP = g++ -m64 -std=c++11
else ifeq ($(platform), x86)
    CPP = g++ -m32 -std=c++11
else
    CPP = arm-hisiv400-linux-g++ -std=c++11 -march=armv7-a
endif

OUTPUT_DIR = ../../linuxoutput/$(platform)/$(version)
OBJ_DIR = ./obj/$(platform)/$(version)

## 目标文件
TARGET = libCtcsJswfAe.so
BIN_TARGET = $(OUTPUT_DIR)/$(TARGET)

## 提取所有源文件（即：*.cpp文件）和所有中间文件（即：*.o）
SRCS = $(wildcard $(SRC_PATH)/*.cpp)
OBJS = $(patsubst %.cpp, $(OBJ_DIR)/%.o, $(notdir $(SRCS)))

ifeq ($(version), release)
CFLAGS = -O3 -DNDEBUG -Wall -fPIC $(INC)
else
CFLAGS = -g -DDEBUG -Wall -fPIC $(INC)
endif

## 宏定义
## DEFS = -DDEBUG

## 依赖库
DEP_LIBS = -L /usr/local/lib -L $(OUTPUT_DIR) -Wl,-Bdynamic -lpthread -lpss -llog4cpp

##用所有中间文件生成目的文件，规则中可以用$^替换掉$(OBJS)
$(BIN_TARGET):$(OBJS)
    @if test ! -d $(OUTPUT_DIR); \
	then \
	mkdir -p $(OUTPUT_DIR); \
	fi
	rm -rf $(BIN_TARGET)
	$(CPP) -Wl,-rpath,$$ORIGIN -shared -o $@ $^ $(DEP_LIBS)
	@echo buid $(BIN_TARGET)
	
## 生成各中间文件
$(OBJ_DIR)/%.o:./%.cpp
    @echo $< $@ $^
    @if test ! -d $(OBJ_DIR); \
    then \
    mkdir -p $(OBJ_DIR); \
	fi
	$(CPP) $(CFLAGS) -c $< -o $@

.PHONY: clean
clean:
    rm -f $(OBJ_DIR)/*.o
	rm -rf $(BIN_TARGET)
	
.PHONY: dir
dir:
    @if test ! -d $(OBJ_DIR); \
	then \
	mkdir -p $(OBJ_DIR); \
	fi
	@if test ! -d $(OUTPUT_DIR); \
	then \
	mkdir -p $(OUTPUT_DIR); \
	fi
	
.PHONY: print
print:
    @echo SOURCE = $(SRCS)
	@echo OBJECT = $(OBJS)








