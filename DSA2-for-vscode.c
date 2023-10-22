// Credits: Christian Villanueva, Jaero Octaviano

#include <stdio.h>
#include <windows.h>
#define p printf

void d(float x)
{
    Sleep(x);
}

void g(int x, int y)
{
    COORD c;
    c.X = x;
    c.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), c);
}

void main()
{
    int i;
    int j;
    int k;
    int t = 5; // adjust animation speed
    
    system("cls");
    
    // forward
    for (i = 4; i <= 8; i++) {
        if (i == 4) { // top: left to right (first layer)
            for (j = i; j <= 72 - 4 * i; j++) {
                g(j + 10, 2 * i - 3);d(t);p("%c", 219);
            }
            
        } else { // top: left to right (layers...)
            for (j = 4 * i - 6; j <= 84 - 4 * i; j++) {
                g(j, 2 * i - 3);d(t);p("%c", 219);
            }
        }
        
        if (i < 8) { 
            for (k = 2 * i - 3; k <= 29 - 2 * i; k++) { // after first layer, rightmost
                g(80 - 4 * i + 3, k);d(t);p("%c%c", 219, 219);
            } 
            for (j = 4 * i - 11; j <= 74 - 4 * i; j++) { // bottom: right to left
                g(72 - j, 29 - 2 * i);d(t);p("%c", 219);
            }
            for (k = 2 * i - 3; k <= 26 - 2 * i; k++) { // after bottom, leftmost
                g(4 * i - 2, 25 - k);d(t);p("%c%c", 219, 219);
            }
        }
    }
    
    // reverse
    for (i = 8; i >= 4 ; i--) {
        if (i == 8) { // starts at 5th middle layer
            for (j = 84 - 4 * i; j >= 4 * i - 6; j--) {
                g(j, 2 * i - 3);d(t);p(" ");
            } 
        } else {
            for (k = 26 - 2 * i; k >= 2 * i - 3; k--) {
                g(4 * i - 2, 25 - k);d(t);p("  ");
            }
            for (j = 74 - 4 * i; j >= 4 * i - 11; j--) {
                g(72 - j, 29 - 2 * i);d(t);p(" ");
            }
            for (k = 29 - 2 * i; k >= 2 * i - 3; k--) {
                g(80 - 4 * i + 3, k);d(t);p("  ");
            }

            if (i > 4) { 
                for (j = 84 - 4 * i; j >= 4 * i - 6; j--) {
                g(j, 2 * i - 3);d(t);p(" ");
                }

            } else {
                for (j = 84 - 4 * i; j >= 4 * i - 5; j--) {
                g(j, 2 * i - 3);d(t);p(" ");
                }
            }
        }
    }
    getch();
}