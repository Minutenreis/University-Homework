#include <cstdint>
#include <cstdlib>
#include <iostream>

extern "C" {
    void showcase_fmla_element( float const * i_a,
                            float const * i_b,
                            float       * o_c);
}

int main(){
    std::cout << "Running 9.1.2 Code" << std::endl;

    float l_a_fp32[4] = {1,2,3,4};
    float l_b_fp32[4] = {5,6,7,8};
    float l_c_fp32[4] = {10,11,12,13};

    showcase_fmla_element(l_a_fp32, l_b_fp32, l_c_fp32);

    std::cout << "C:" << l_c_fp32[0] << " " << l_c_fp32[1] << " " << l_c_fp32[2] << " " << l_c_fp32[3] << std::endl;
    std::cout << "Finished 9.1.2 Code" << std::endl;
    return EXIT_SUCCESS;
}
    