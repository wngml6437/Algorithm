#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    unsigned int S = 0;
    int m, inputN;
    string inputS;
    cin >> m;
     
    for (int i = 0; i < m; i++) {
        cin >> inputS;

        if (inputS == "add") {
            cin >> inputN;
            S |= (1 << --inputN);
        }
        else if (inputS == "remove") {
            cin >> inputN;
            S &= ~(1 << --inputN);
        }
        else if (inputS == "check") {
            cin >> inputN;
            if (S & (1 << --inputN))
                cout << 1 << "\n";
            else
                cout << 0 << "\n";
        }
        else if (inputS == "toggle") {
            cin >> inputN;
            S ^= (1 << --inputN);
        }
        else if (inputS == "all") {
            S = (2 << 21) - 1;
        }
        else {
            S = 0;
        }
   }    
      
   return 0;
}