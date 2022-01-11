#include<iostream>
using namespace std;
/*
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

*/
int main(void){
    int N;
    cin >> N;
    string out = "";

    int M = N / 1000;  // 4800 -> 4になる．C++では小数点以下は切り捨てられる
    for(int i = 0; i < M; i++){
        out += "M";
    }

    N = (N % 1000);
    // N　が１００の位いかの数字になる．
    if(N >= 900){
        // 900 ~ 
        // CMを足す
        out += "CM";
    } else if(N >= 500){
        // 500 ~ 899
        // Dを入れる
        out += "D";
        N -= 500; // 800 -> 300になる
        int C = N / 100;
        for(int i = 0; i < C; i++){
            out += "C";
        }
    }
    else if(N < 500 && N >= 400){
        // 400 ~ 499
        // CDを入れる．
        out += "CD";
    } else if(N >= 100) {
        // 100 ~ 399
        int C = N / 100;
        for(int i = 0; i < C; i++){
            out += "C";
        }
    }

    int tmp = (N % 100);
    if(tmp < 0) tmp += 100; // 598 -> 98になるはず LXVIを処理すれば良い
    cout << tmp << endl;

    N %= 100; 

    if(N >= 90){
        // 90 ~ 
        // XCを足す
        out += "XC";
    } else if(N >= 50){
        // 50 ~ 89
        // Lを入れる
        out += "L";
        N -= 50; // 80 -> 30になる
        int X = N / 10;
        for(int i = 0; i < X; i++){
            out += "X";
        }
    }
    else if(N < 50 && N >= 40){
        // 400 ~ 499
        // XLを入れる．
        out += "XL";
    } else if(N >= 10) {
        // 10 ~ 39
        int X = N / 10;
        for(int i = 0; i < X; i++){
            out += "X";
        }
    }

    N %= 10; 

    if(N >= 9){
        // 9 ~ 
        // IXを足す
        out += "IX";
    } else if(N >= 5){
        // 5 ~ 8
        // Vを入れる
        out += "V";
        N -= 5; // 8 -> 3になる
        for(int i = 0; i < N; i++){
            out += "I";
        }
    }
    else if(N == 4){
        // 4
        // XLを入れる．
        out += "IV";
    } else if(N >= 1) {
        // 1 ~ 3
        // int I = N / 10;
        for(int i = 0; i < N; i++){
            out += "I";
        }
    }



    cout << out <<endl;
    return 0;
}