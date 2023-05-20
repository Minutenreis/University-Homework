#include <cstdint>
#include <cmath>
#include <chrono>
#include <tuple>
#include <iostream>
#include <unistd.h>

extern "C" {
  uint64_t micro_aarch64_madd_w_independent( uint64_t i_n_repetitions );
  uint64_t micro_aarch64_madd_w_raw_rn( uint64_t i_n_repetitions );
}

/**
 * Measures the performance (time) of the given kernel.
 *
 * @param i_kernel benchmarked kernel.
 * @param i_n_repetitions number of performed repetitions.
 * @return duration required for the performed repetitions.
 **/
double timeKernel( uint64_t (*i_kernel)(uint64_t),
                   uint64_t   i_n_repetitions ) {
  std::chrono::steady_clock::time_point l_tp0, l_tp1;
  std::chrono::duration< double > l_dur;

  l_tp0 = std::chrono::steady_clock::now();
  (*i_kernel)( i_n_repetitions );
  l_tp1 = std::chrono::steady_clock::now();

  l_dur = std::chrono::duration_cast< std::chrono::duration< double> >( l_tp1 - l_tp0 );

  return l_dur.count();
}

/**
 * Benchmarks the performance (repetitions, time, giga instructions) of the given microkernel.
 *
 * @param i_kernel benchmarked kernel.
 * @param i_time_target targeted total execution time; the number of actual repetitions is adjusted accordingly.
 * @param i_n_repetitions_initial initial number of performed repetitions.
 * @return (repetitions, time, gints).
 **/
std::tuple< uint64_t,
            double,
            double > benchKernel( uint64_t (*i_kernel)(uint64_t),
                                  double     i_time_target = 10.0,
                                  uint64_t   i_n_repetitions_initial = 1000000 ) {
  // get number of flops per iter
  uint64_t l_n_insts = i_kernel(1);

  // get time required for initial number of reps
  double l_dur = timeKernel( i_kernel,
                             i_n_repetitions_initial );

  // derive number of reps for targeted duration
  double l_scaling_time = i_time_target / l_dur;
  uint64_t l_n_repetitions_adj = i_n_repetitions_initial * l_scaling_time;
  if( l_n_repetitions_adj == 0 ) {
    l_n_repetitions_adj = 1;
  }

  // benchmark kernel
  l_dur = timeKernel( i_kernel,
                      l_n_repetitions_adj );

  // derive ginsts
  double l_ginsts = l_n_repetitions_adj;
  l_ginsts *= l_n_insts / l_dur;
  l_ginsts *= 1.0E-9;

  return std::make_tuple( l_n_repetitions_adj,
                          l_dur,
                          l_ginsts );
}

int main() {
  std::cout << "running aarch64 microbenchmarks" << std::endl;

  // common benchmark data
  uint64_t l_n_repetitions = 0;
  double l_time = 0;
  double l_ginsts = 0;

  // benchmark micro_aarch64_madd_w_independent
  std::cout << "micro_aarch64_madd_w_independent" << std::endl;

  std::tie( l_n_repetitions,
            l_time,
            l_ginsts ) = benchKernel( micro_aarch64_madd_w_independent );

  std::cout << "  repetitions: " << l_n_repetitions << std::endl;
  std::cout << "  duration: " << l_time << " seconds" << std::endl;
  std::cout << "  GInstructions: " << l_ginsts << std::endl;

    // benchmark micro_aarch64_madd_w_raw_rn
  std::cout << "micro_aarch64_madd_w_raw_rn" << std::endl;

  std::tie( l_n_repetitions,
            l_time,
            l_ginsts ) = benchKernel( micro_aarch64_madd_w_raw_rn );

  std::cout << "  repetitions: " << l_n_repetitions << std::endl;
  std::cout << "  duration: " << l_time << " seconds" << std::endl;
  std::cout << "  GInstructions: " << l_ginsts << std::endl;

  std::cout << "finished aarch64 microbenchmarks" << std::endl;

  return EXIT_SUCCESS;
}
