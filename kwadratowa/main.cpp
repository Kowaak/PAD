#include <iostream>
#include <stdlib.h>
#include <math.h>
using namespace std;

int main()
{
    system("color 0a");
    double a,b,c,delta,x,x1,x2;
    cout<<"Podaj a: ";
    cin>>a;
    cout<<"Podaj b: ";
    cin>>b;
    cout<<"Podaj c: ";
    cin>>c;
    if (a==0){
        cout<<"To nie jest rownanie kwadratowe"<<endl;
        return 0;
    }else delta = (b*b)-(4*a*c);
    cout<<"Delta wynosi: "<<delta<<endl;
    if (delta<0){
        cout<<"Rownanie nie ma pierwiastków"<<endl;
        return 0;
    }else if(delta==0){
        b=b*-1;
        x=b/(2*a);
        cout<<"x wynosi: "<<x;
        return 0;
    }else{
        b=b*-1;
        x1=(b-sqrt(delta))/(2*a);
        x2=(b+sqrt(delta))/(2*a);
        cout<<"x1 wynosi: "<<x1<<endl;
        cout<<"x2 wynosi: "<<x2<<endl;
    }
    return 0;
}
