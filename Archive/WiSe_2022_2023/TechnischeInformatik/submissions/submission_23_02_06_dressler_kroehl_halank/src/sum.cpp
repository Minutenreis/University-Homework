#include <iostream>
#include <chrono>
#include <fstream>
#include <iostream>
using namespace std;

int main()
{
  std::cout << "running benchmark" << std::endl;

  ofstream myfile;
  myfile.open ("output.txt");
  myfile << "size\tbandwidth\n";

  for (uint64_t l_size = 512; l_size <= 1024 * 1024 * 1024 / 4; l_size *= 2)
  {

    // derive size in bytes and gigabytes
    uint64_t l_size_b = l_size * sizeof(uint64_t);
    double l_size_gib = l_size_b / (1024.0 * 1024.0 * 1024.0);
    uint64_t l_n_repetitions = (uint64_t)10 * 1024 * 1024 * 1024 / l_size_b;

    // share config
    std::cout << "config:\n"
              << "  number of repetitions:        " << l_n_repetitions << "\n"
              << "  number of entries per vector: " << l_size << "\n"
              << "  size per vector (B):          " << l_size_b << "\n"
              << "  size per vector (GB):         " << l_size_gib << "\n"
              << "  total size (GB):              " << l_n_repetitions * l_size_gib
              << std::endl;

    // instrumentation vars
    std::chrono::steady_clock::time_point l_tp0, l_tp1;
    std::chrono::duration<double> l_dur;

    // alloc memory and init
    uint64_t *l_a = (uint64_t *)aligned_alloc(4096,
                                              l_size_b);

    for (uint64_t l_en = 0; l_en < l_size; l_en++)
    {
      l_a[l_en] = 1;
    }

    // benchmark
    std::cout << "benchmarking" << std::endl;
    uint64_t l_sum = 0;
    l_tp0 = std::chrono::steady_clock::now();
    for (uint64_t l_re = 0; l_re < l_n_repetitions; l_re++)
    {
      for (uint64_t l_en = 0; l_en < l_size; l_en++)
      {
        l_sum += l_a[l_en];
      }
    }
    l_tp1 = std::chrono::steady_clock::now();

    // share results
    l_dur = std::chrono::duration_cast<std::chrono::duration<double>>(l_tp1 - l_tp0);
    double l_bandwidth = l_n_repetitions * l_size_gib / l_dur.count();
    std::cout << "  error:            " << l_sum - (l_n_repetitions * l_size) << "\n"
              << "  time:             " << l_dur.count() << "\n"
              << "  bandwidth (GiB/s): " << l_bandwidth
              << std::endl;

    myfile << l_size_b << "\t" << l_bandwidth << "\n";
    

    // free memory
    free(l_a);
  }
  myfile.close();

  return EXIT_SUCCESS;
}