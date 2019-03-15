#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
    system("test.exe");
    ifstream inFile;
    inFile.open("test.txt");
    int a=0;
    inFile >>a ;
    inFile.close();
    cout<<a;
    system("del test.txt");

    return 0;
}
