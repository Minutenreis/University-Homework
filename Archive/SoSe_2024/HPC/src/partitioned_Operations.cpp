// example from MPI 4.0 standard https://www.mpi-forum.org/docs/mpi-4.0/mpi40-report.pdf
#include "../mpi.h"
int main()
{
    // initialize MPI and get own rank as rank
    float *buffer = new float[numThreads * arrLengthPerThread];
    bool done = false;
    MPI_Request request;
    if (rank == 0)
    {
        MPI_Psend_init(buffer, numThreads, arrLengthPerThread, MPI_FLOAT, 0, 0, MPI_COMM_WORLD, info, &request);
#pragma omp parallel shared(request) num_threads(numThreads)
        while (!done)
        {
#pragma omp single
            MPI_Start(&request);
#pragma omp for
            for (int i = 0; i < numThreads; i++)
            {
                /* compute and fill partition #i, then mark ready: */
                MPI_Pready(i, request);
            }
#pragma omp single
            MPI_Wait(&request, &flag, MPI_STATUS_IGNORE);
        }
    }
    else if (rank == 1)
    {
        MPI_Precv_init(buffer, numThreads, arrLengthPerThread, MPI_FLOAT, 0, 0, info, MPI_COMM_WORLD, &request);
#pragma omp parallel shared(request) num_threads(numThreads)
        while (!done)
        {
            int arrived = 0;
#pragma omp single
            MPI_Start(&request);
#pragma omp for
            for (int i = 0; i < numThreads; i++)
            {
                while (arrived == 0)
                {
                    MPI_Parrived(i, request, &arrived);
                }
                // process partition #i
            }
            MPI_Wait(&request, &flag, MPI_STATUS_IGNORE);
        }
    }
    MPI_Request_free(&request);
    MPI_Finalize();
    return 0;
}