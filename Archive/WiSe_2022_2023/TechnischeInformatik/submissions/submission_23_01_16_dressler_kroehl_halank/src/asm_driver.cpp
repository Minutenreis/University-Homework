#include <cstdint>
#include <cstdlib>
#include <iostream>

extern "C" {
  uint64_t machine_code_c();
  uint64_t machine_code_asm_0();
  uint64_t machine_code_asm_1();
}

int main() {
  uint64_t l_result_c = 0;
  uint64_t l_result_asm_0 = 0;
  uint64_t l_result_asm_1 = 0;

  // machine_code_c
  std::cout << "### calling machine_code_c ###" << std::endl;
  l_result_c = machine_code_c();
  std::cout << l_result_c << std::endl;

  // machine_code_asm_0
  std::cout << "### calling machine_code_asm_0 ###" << std::endl;
  l_result_asm_0 = machine_code_asm_0();
  std::cout << l_result_asm_0 << std::endl;

  // machine_code_asm_1
  std::cout << "### calling machine_code_asm_1 ###" << std::endl;
  l_result_asm_1 = machine_code_asm_1();
  std::cout << l_result_asm_1 << std::endl;

  return EXIT_SUCCESS;
}