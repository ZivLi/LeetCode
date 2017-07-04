#include <iostream>
using namespace std;

class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 and !(n&(n-1));
    }
};
