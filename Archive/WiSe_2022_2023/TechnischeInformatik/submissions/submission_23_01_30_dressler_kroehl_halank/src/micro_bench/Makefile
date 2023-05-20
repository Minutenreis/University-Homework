BUILD_DIR = ./build
CC_BASE_FLAGS ?= -Wall -Wextra -Werror ${CC_ASIMD_EXTRA_FLAGS}
CXX_BASE_FLAGS ?= -Wall -Wextra -Werror -O2 ${CXX_ASIMD_EXTRA_FLAGS}

micro_aarch64: driver_aarch64.cpp kernels/micro_aarch64_madd_w.s
		${CC} ${CC_BASE_FLAGS} -c kernels/micro_aarch64_madd_w.s -o ${BUILD_DIR}/micro_aarch64_madd_w.o
		${CXX} ${CXX_BASE_FLAGS} driver_aarch64.cpp ${BUILD_DIR}/micro_aarch64_madd_w.o -o ${BUILD_DIR}/micro_aarch64_madd_w

$(shell mkdir -p build)
