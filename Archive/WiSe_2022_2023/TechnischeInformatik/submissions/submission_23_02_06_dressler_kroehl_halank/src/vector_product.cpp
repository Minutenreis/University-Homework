#include <cstdint>
#include <cmath>
#include <chrono>
#include <tuple>
#include <iostream>
#include <unistd.h>

uint64_t read(const uint64_t *a, const uint64_t *b, const uint64_t size, uint64_t distance)
{
    uint64_t result = 0;
    for (uint64_t l = 0; l < distance; l++)
    {
        for (uint64_t k = 0; k < size / distance; k++)
        {
            result += a[distance * k + l] * b[distance * k + l];
        }
    }
    return result;
}

int main()
{
    uint64_t l_size = 134217728;

    // derive size in bytes and gigabytes
    uint64_t l_size_b = l_size * sizeof(uint64_t);
    double l_size_gib = l_size_b / (1024.0 * 1024.0 * 1024.0);

    uint64_t *a = (uint64_t *)aligned_alloc(4096, l_size_b);
    uint64_t *b = (uint64_t *)aligned_alloc(4096, l_size_b);

    for (uint64_t l_en = 0; l_en < l_size; l_en++)
    {
        a[l_en] = 1;
        b[l_en] = 2;
    }

    std::chrono::steady_clock::time_point start, end;
    std::chrono::duration<double> l_dur;

    for (int distance = 1; distance <= 16; distance *= 2)
    {
        // benchmark
        start = std::chrono::steady_clock::now();
        uint64_t result = read(a, b, l_size, distance);
        end = std::chrono::steady_clock::now();

        // share results
        l_dur = std::chrono::duration_cast<std::chrono::duration<double>>(end - start);
        std::cout << "Dot product Distance " << distance << ": \n"
                  << "  error:             " << result - 2 * l_size << "\n"
                  << "  time:              " << l_dur.count() << "\n"
                  << "  bandwidth (GiB/s): " << l_size_gib / l_dur.count()
                  << std::endl;
    }

    // free memory
    free(a);
    free(b);

    return EXIT_SUCCESS;
}