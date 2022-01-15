#include<vector>
#include<string>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // solを求める．
        int res = 0;
        int n = s.size();
        
        for(int i = 0; i < n; i++){
            for(int j = i; j < n; j ++){
                if(allUnique(s, i, j)) {
                    res = max(res, j - i + 1);
                }
            }
        }
        return res;
    }
    
    bool allUnique(string& s, int start, int end){
        vector<int> chars(128);
        
        for(int i = start; i <= end; i++){
            char c = s[i];
            chars[c]++;
            if(chars[c] > 1){
                return false;
            }
        }
        
        return true;
    }
};