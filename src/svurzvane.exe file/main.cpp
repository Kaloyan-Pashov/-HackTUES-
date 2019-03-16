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
    int result=system("python settings.py");
    cout << result;
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
    while(true)
    {
        while(x1>0)
        {
        Sleep(x1);
        int result1 = system("python pop-up.py \"Упражнение с очи\" мигайте icon.ico 30");
        cout << result1;
        break;
        }
        while(x2>0)
        {
        Sleep(x2);
        int result2 = system("python pop-up.py \"Безопасно разстояние от монитора\" \"Стойте поне на 2 педии разстояние\" icon.ico 30");
        cout << result2;
        break;
        }
        while(x3>0)
        {
        Sleep(x3);
        int result3 = system("python pop-up.py \"Безопасно разстояние от монитора\" \"Стойте поне на 2 педии разстояние\" icon.ico 30");
        cout << result3;
        break;
        }
        while(x4>0)
        {
        Sleep(x4);
        int result4 = system("python pop-up.py \"Упражнение с очи\" мигайте icon.ico 30");
        cout << result4;
        break;
        }
        while(x5>0)
        {
        Sleep(x5);
        int result5 = system("python pop-up.py \"Упражнение с очи\" мигайте icon.ico 30");
        cout << result5;
        break;
        }
        while(x6>0)
        {
        Sleep(x6);
        int result6 = system("python pop-up.py \"Упражнение с очи\" мигайте icon.ico 30");
        cout << result6;
        break;
        }
        while(x7>0)
        {
        Sleep(x7);
        int result7 = system("python pop-up.py \"Упражнение с очи\" мигайте icon.ico 30");
        cout << result7;
        break;
        }
        while(x8>0)
        {
        Sleep(x8);
        int result8 = system("python pop-up.py \"Упражнение с очи\" мигайте icon.ico 30");
        cout << result8;
        break;
        }
        //while(x2>0)
    }
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
