BUILD_DIR = ./build
CXX_BASE_FLAGS ?= -Wall -Wextra -Werror -O2

sum: sum.cpp
		${CXX} ${CXX_BASE_FLAGS} sum.cpp -o ${BUILD_DIR}/sum

all: sum

$(shell mkdir -p build)
