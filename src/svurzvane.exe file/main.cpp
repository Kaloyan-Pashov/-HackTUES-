#include <iostream>
#include <iomanip>
#include <fstream>
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
unsigned long long is_noting_DONE()
{
    system("test.exe");
    FILE *fp;
    unsigned long long temp;
    fp=fopen("test.txt","r");
    fscanf(fp,"%llu", &temp);
    fclose(fp);
    fopen("test.txt","w");
    fclose(fp);
    return temp;
}
int main()
{
    // system("python settings.py");
    //    cout << result;
    //if start clicked:
    int x1,x2,x3,x4,x5,x6,x7,x8;
    ifstream inFile;

    inFile.open("settings.txt");
    inFile >> x1 >> x2 >> x3 >> x4 >> x5 >> x6 >> x7 >> x8;
    if(true)
    {
        cout<<x1<<endl;
        cout<<x2<<endl;
        cout<<x3<<endl;
        cout<<x4<<endl;
        cout<<x5<<endl;
        cout<<x6<<endl;
        cout<<x7<<endl;
        cout<<x8<<endl;

    }

    inFile.close();

        int result = system("python pop-up.py \"”пражнение с очи\" мигайте icon.ico 30");
        cout << result;


    /*unsigned long long timecomp=0, a=is_noting_DONE();
    while(1)
    {
        Sleep(15000);
        if(a>20000)
        {
            timecomp++;
        }
        else
        {
            continue;
        }

    }*/

    return 0;
}
