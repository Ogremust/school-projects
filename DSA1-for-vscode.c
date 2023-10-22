#include <stdio.h>
#include <windows.h>
#define p printf
#define g gotoxy

void g(int x, int y)
{
    COORD c;
    c.X = x;
    c.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), c);
}

void main() {
    int x;
    system("cls");
    g(2,2); p("NUMBER");
    g(12, 2); p("SQUARE");
    g(22, 2); p("CUBE");

    // Loop from 0 to 10 to compute and display the square and cube
    for(x = 0; x <= 10; x++) 
    {
        g(2, x+4); p("%d", x);
        g(12, x+4); p("%d", x*x);        // display square
        g(22, x+4); p("%d", x*x*x);      // display cube
    }

}