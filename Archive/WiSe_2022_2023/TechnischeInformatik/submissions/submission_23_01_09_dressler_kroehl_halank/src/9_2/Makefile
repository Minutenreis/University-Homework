BUILD_DIR = ./build

gemm_asm: driver.cpp kernels/gemm_ref.cpp kernels/gemm_asm_fp_4_4_4.s kernels/gemm_asm_asimd_4_4_4.s
		g++ -pedantic -Wall -Wextra -Werror -O2 -c kernels/gemm_ref.cpp -o ${BUILD_DIR}/gemm_ref.o
		gcc -pedantic -Wall -Wextra -Werror -c kernels/gemm_asm_fp_4_4_4.s -o ${BUILD_DIR}/gemm_asm_fp_4_4_4.o
		gcc -pedantic -Wall -Wextra -Werror -c kernels/gemm_asm_asimd_4_4_4_optimized.s -o ${BUILD_DIR}/gemm_asm_asimd_4_4_4_optimized.o
		g++ -pedantic -Wall -Wextra -Werror driver.cpp ${BUILD_DIR}/gemm_ref.o ${BUILD_DIR}/gemm_asm_fp_4_4_4.o ${BUILD_DIR}/gemm_asm_asimd_4_4_4_optimized.o -o ${BUILD_DIR}/gemm_asm

$(shell mkdir -p build)