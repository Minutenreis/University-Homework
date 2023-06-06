#include <cstdint>

extern "C"
{
    int32_t low_lvl_0(int32_t i_value);

    uint64_t low_lvl_1(uint64_t);

    int32_t low_lvl_2(int32_t i_option);

    void low_lvl_3(int32_t *i_option,

                   int32_t *o_result);

    uint32_t low_lvl_4(uint32_t i_x,

                       uint32_t i_y,

                       uint32_t i_z);

    void low_lvl_5(uint32_t i_nIters,

                   int32_t *io_value);

    void low_lvl_6(uint64_t i_nIters,

                   int64_t i_inc,

                   int64_t *io_value);

    void low_lvl_7(uint64_t i_nValues,

                   int64_t *i_valuesIn,

                   int64_t *i_valuesOut);
}