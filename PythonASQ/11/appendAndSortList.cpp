#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sys/resource.h>

bool compare(const std::string &a, const std::string &b)
{
    std::string delimiter = "\t";
    size_t posA1 = a.find(delimiter);
    size_t posB1 = b.find(delimiter);
    int aChr = std::stoi(a.substr(3, posA1));
    int bChr = std::stoi(b.substr(3, posB1));
    if (aChr != bChr)
    {
        return aChr < bChr;
    }
    size_t posA2 = a.find(delimiter, posA1 + 1);
    size_t posB2 = b.find(delimiter, posB1 + 1);
    std::string aPos = a.substr(posA1 + 1, posA2);
    std::string bPos = b.substr(posB1 + 1, posB2);
    return aPos.length() == bPos.length() && aPos < bPos || aPos.length() < bPos.length();
}

int main(int argc, char const *argv[])
{
    if (argc != 3)
    {
        std::cerr << "Usage: " << argv[0] << " <file1> <file2>" << std::endl;
        return 1;
    }
    std::string file1 = argv[1];
    std::string file2 = argv[2];

    std::ifstream file1Stream(file1);
    std::ifstream file2Stream(file2);

    if (!file1Stream.is_open())
    {
        std::cerr << "Error: Could not open file " << file1 << std::endl;
        return 1;
    }
    if (!file2Stream.is_open())
    {
        std::cerr << "Error: Could not open file " << file2 << std::endl;
        return 1;
    }

    std::vector<std::string> shared_list;
    std::string line;
    getline(file1Stream, line);
    while (getline(file1Stream, line))
    {
        shared_list.push_back(line);
    }
    getline(file2Stream, line);
    while (getline(file2Stream, line))
    {
        shared_list.push_back(line);
    }

    std::sort(shared_list.begin(), shared_list.end(), compare);

    std::ofstream out("bin/sorted.bed");
    for (auto &line : shared_list)
    {
        out << line << std::endl;
    }

    struct rusage usage;
    getrusage(RUSAGE_SELF, &usage);
    auto statPeakMemoryMB = usage.ru_maxrss / 1024;

    std::cout << "Peak Memory CPP:    " << statPeakMemoryMB << " MB" << std::endl;

    /* code */
    return 0;
}
