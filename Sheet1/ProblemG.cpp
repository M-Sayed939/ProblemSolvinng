#include <iostream>
using namespace std;
 
int main() {
    string str;
    cin >> str;
    int i = 0;
    int j = str.size() - 1;
    while (i < j) {
        swap(str[i], str[j]);
        i++;
        j--;
    }
    i = 0;
    while (str[i] == '0') {
        i++;
    }
    str = str.substr(i);
    cout << str << endl;
    return 0;
}