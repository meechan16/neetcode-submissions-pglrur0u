class MinStack {
private:
    long min;
    stack<long> st;
public:
    MinStack() {
        
    }
    
    void push(int val) {
        if(st.empty()){
            st.push(0);
            min = val;
        }else{
            st.push((long)val-min);
            if(val < min) min = val;
        }
    }
    
    void pop() {
        if(st.empty()) return ;
        long pop = st.top();
        st.pop();

        if(pop<0) min = min - pop;
    }
    
    int top() {
        long top = st.top();
        if(top>0){
            return (int)(top+min);
        }
        return (int)min;
        
    }
    
    int getMin() {
        return (int)min;
    }
};