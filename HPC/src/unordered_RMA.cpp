#include "../mpi.h"
#include <string>

int main(int argc, char *argv[])
{
    MPI_Init(&argc, &argv);
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    float buffer[100];

    MPI_Info info;
    MPI_Info_create(&info);
    std::string key = "accumulate_ordering";
    std::string value = "none";
    MPI_Info_set(info, key.data(), value.data());

    MPI_Win win;
    MPI_Win_create(buffer, 100 * sizeof(float), sizeof(float), info, MPI_COMM_WORLD, &win);

    return 0;
}
