#include<iostream>
#include<stack>
#include<vector>
using namespace std;
int pres(string ch)
{
    if(ch=="/" || ch=="*") return 2;
    else if(ch=="+" || ch=="-") return 1;
    return 0;
}
bool isOperator(string ch)
{
    if(ch=="+" or ch=="-" or ch=="/" or ch=="*") return true;
    return false;
}
vector<string> infixToPostfix(vector<string> s)
{
    vector<string> ans;
    stack<string> st;
    for(int i=0;i<s.size();i++)
    {
        string ch=s[i];
        if(ch>="0" && ch<="9999999")
        {
            ans.push_back(ch);
        }
        else if(ch=="(") st.push(ch);
        else if(ch==")")
        {
            while(!st.empty() && st.top()!="(")
            {
                ans.push_back(st.top());
                st.pop();
            }
            st.pop();
        }
        else
        {
            if(st.empty() || pres(ch)>pres(st.top()))
            {
                st.push(ch);
            }
            else
            {
                while(!st.empty() && pres(ch)<=pres(st.top()))
                {
                    ans.push_back(st.top());
                    st.pop();
                }
                st.push(ch);
            }
        }
    }
    while(!st.empty())
    {
        ans.push_back(st.top());
        st.pop();
    }
    return ans;
}
int solve(vector<string> a)
{
    stack<int> st;
    for(auto x: a)
    {
        if(isOperator(x))
        {
            int two=st.top();
            st.pop();
            int one=st.top();
            st.pop();
            if(x=="+")
                st.push(one+two);
            else if(x=="-")
                st.push(one-two);
            else if(x=="*")
                st.push(one*two);
            else if(x=="/")
            {
                try{
                    if(two==0)
                        throw runtime_error("Division by 0 Detected!!");
                    st.push(one/two);
                }catch(runtime_error& e){
                    throw e;
                }
            }
        }
        else
        {
            st.push(stoi(x));
        }
    }
    return st.top();
}
int main()
{
    string s;
    cout<<"Enter Equation to solve: "; cin>>s;
    vector<string> an;
    for(int i=0;i<s.length();)
    {
        string tmp="";
        if(s[i]>='0' && s[i]<='9')
        {
            while(s[i]>='0' && s[i]<='9')
            {
                tmp+=s[i++];
            }
        }
        else
        {
            tmp+=s[i++];
        }
        an.push_back(tmp);
    }
    vector<string> a=infixToPostfix(an);
    try{
        cout<<solve(a);
    }
    catch(runtime_error& e){
        cout<<e.what();
    }
    return 0;
}
