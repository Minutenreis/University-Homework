#include "mpi.h"
#include "omp.h"

int main(int argc, char *argv[])
{
    int dataLen = 100;
    float dataLeft[dataLen], dataRight[dataLen];
    bool done = false;
    MPI_Init(&argc, &argv);
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm comm_0[3], comm_1[3];
    for (int i = 0; i < 3; i++)
    {
        MPI_Comm_dup(MPI_COMM_WORLD, &comm_0[i]);
        MPI_Comm_dup(MPI_COMM_WORLD, &comm_1[i]);
    }

#pragma omp parallel num_threads(9)
    {
        while (!done)
        {
            // halo exchange
            int tid = omp_get_thread_num();
            int tid_x = tid % 3;
            int tid_y = tid / 3;
            if (tid_x == 0)
            {
                MPI_Comm left_comm = rank % 2 ? comm_1[tid_y] : comm_0[tid_y];
                MPI_Sendrecv_replace(&dataLeft, dataLen, MPI_FLOAT, rank - 1, 0, rank - 1, 0, left_comm, MPI_STATUS_IGNORE);
            }
            else if (tid_x == 2)
            {
                MPI_Comm right_comm = rank % 2 ? comm_0[tid_y] : comm_1[tid_y];
                MPI_Sendrecv_replace(&dataRight, dataLen, MPI_FLOAT, rank + 1, 0, rank + 1, 0, right_comm, MPI_STATUS_IGNORE);
            }
            // update boundaries  with new data
            // calculate next step
        }
    }

    for (int i = 0; i < 3; i++)
    {
        MPI_Comm_free(&comm_0[i]);
        MPI_Comm_free(&comm_1[i]);
    }

    MPI_Finalize();
    return 0;
}