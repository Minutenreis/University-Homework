#include <iostream>

#include "high_level.h"
#include "low_level.h"

int main()
{

    std::cout << "running driver" << std::endl;

    std::cout << "high_lvl_0(10): "

              << high_lvl_0(10)

              << std::endl;

    std::cout << "high_lvl_1(10): "

              << high_lvl_1(10) << std::endl;

    std::cout << "high_lvl_2(32): "

              << high_lvl_2(32) << std::endl;

    std::cout << "high_lvl_2( 5): "

              << high_lvl_2(5) << std::endl;

    int32_t l_highLvlOpt3 = 17;

    int32_t l_highLvlRes3 = -1;

    high_lvl_3(&l_highLvlOpt3,

               &l_highLvlRes3);

    std::cout << "high_lvl_3 #1: "

              << l_highLvlRes3 << std::endl;

    l_highLvlOpt3 = 43;

    high_lvl_3(&l_highLvlOpt3,

               &l_highLvlRes3);

    std::cout << "high_lvl_3 #2: "

              << l_highLvlRes3 << std::endl;

    std::cout << "high_lvl_4(1,2,3): "

              << high_lvl_4(1, 2, 3) << std::endl;

    std::cout << "high_lvl_4(4,2,3): "

              << high_lvl_4(4, 2, 3) << std::endl;

    std::cout << "high_lvl_4(4,3,3): "

              << high_lvl_4(4, 3, 3) << std::endl;

    int32_t l_highLvlValue5 = 500;

    high_lvl_5(17,

               &l_highLvlValue5);

    std::cout << "high_lvl_5: " << l_highLvlValue5 << std::endl;

    int64_t l_highLvlValue6 = 23;

    high_lvl_6(5,

               13,

               &l_highLvlValue6);

    std::cout << "high_lvl_6: "

              << l_highLvlValue6 << std::endl;

    int64_t l_highLvlVasIn7[10] = {0, 7, 7, 4, 3,

                                   -10, -50, 40, 2, 3};

    int64_t l_highLvlVasOut7[10] = {0};

    high_lvl_7(10,

               l_highLvlVasIn7,

               l_highLvlVasOut7);

    std::cout << "high_lvl_7: "

              << l_highLvlVasOut7[0] << " / "

              << l_highLvlVasOut7[1] << " / "

              << l_highLvlVasOut7[2] << " / "

              << l_highLvlVasOut7[3] << " / "

              << l_highLvlVasOut7[4] << " / "

              << l_highLvlVasOut7[5] << " / "

              << l_highLvlVasOut7[6] << " / "

              << l_highLvlVasOut7[7] << " / "

              << l_highLvlVasOut7[8] << " / "

              << l_highLvlVasOut7[9] << std::endl;

    // low-level part goes here

    std::cout << "running driver" << std::endl;

    std::cout << "low_lvl_0(10): "

              << low_lvl_0(10)

              << std::endl;

    std::cout << "low_lvl_1(10): "

              << low_lvl_1(10) << std::endl;

    std::cout << "low_lvl_2(32): "

              << low_lvl_2(32) << std::endl;

    std::cout << "low_lvl_2( 5): "

              << low_lvl_2(5) << std::endl;

    int32_t l_lowLvlOpt3 = 17;

    int32_t l_lowLvlRes3 = -1;

    low_lvl_3(&l_lowLvlOpt3,

               &l_lowLvlRes3);

    std::cout << "low_lvl_3 #1: "

              << l_lowLvlRes3 << std::endl;

    l_lowLvlOpt3 = 43;

    high_lvl_3(&l_lowLvlOpt3,

               &l_lowLvlRes3);

    std::cout << "low_lvl_3 #2: "

              << l_lowLvlRes3 << std::endl;

    std::cout << "low_lvl_4(1,2,3): "

              << low_lvl_4(1, 2, 3) << std::endl;

    std::cout << "low_lvl_4(4,2,3): "

              << low_lvl_4(4, 2, 3) << std::endl;

    std::cout << "low_lvl_4(4,3,3): "

              << low_lvl_4(4, 3, 3) << std::endl;

    int32_t l_lowLvlValue5 = 500;

    low_lvl_5(17,

               &l_lowLvlValue5);

    std::cout << "low_lvl_5: " << l_lowLvlValue5 << std::endl;

    int64_t l_lowLvlValue6 = 23;

    low_lvl_6(5,

               13,

               &l_lowLvlValue6);

    std::cout << "low_lvl_6: "

              << l_lowLvlValue6 << std::endl;

    int64_t l_lowLvlVasIn7[10] = {0, 7, 7, 4, 3,

                                   -10, -50, 40, 2, 3};

    int64_t l_lowLvlVasOut7[10] = {0};

    high_lvl_7(10,

               l_lowLvlVasIn7,

               l_lowLvlVasOut7);

    std::cout << "low_lvl_7: "

              << l_lowLvlVasOut7[0] << " / "

              << l_lowLvlVasOut7[1] << " / "

              << l_lowLvlVasOut7[2] << " / "

              << l_lowLvlVasOut7[3] << " / "

              << l_lowLvlVasOut7[4] << " / "

              << l_lowLvlVasOut7[5] << " / "

              << l_lowLvlVasOut7[6] << " / "

              << l_lowLvlVasOut7[7] << " / "

              << l_lowLvlVasOut7[8] << " / "

              << l_lowLvlVasOut7[9] << std::endl;

    std::cout << "finished, exiting" << std::endl;

    return EXIT_SUCCESS;
}