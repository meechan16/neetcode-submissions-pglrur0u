class Solution {
public:
    bool isValid(string s) {
        stack<int> st;
        unordered_map<char, char> brack = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        for(auto et: s){
            if(brack.count(et)){
                if(!st.empty() && st.top() == brack[et]) st.pop();
             else{
                return false;
            }
            }
            else{
                st.push(et);
            }
        }
        return st.empty();
    }
};
