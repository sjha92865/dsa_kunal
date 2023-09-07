# #include <bits/stdc++.h>
# using namespace std;
# void insertion(vector<int>&v,int temp)
# {
#   if(v.size()==0 || v[v.size()-1]<=temp)
#   {
#   v.push_back(temp);
#   return;
#   }
#   int x=v[v.size()-1];
#   v.pop_back();
#   insertion(v,temp);
#   v.push_back(x);
# }
# void sorting(vector<int>&v)
# {
#   if(v.size()<=1)
#   return;
#   int temp=v[v.size()-1];
#   v.pop_back();
#   sorting(v);
#   insertion(v,temp);
# }
# int main()
# {
#     vector<int>v={5,3,2,4,1};
#     sorting(v);
#   for(auto it:v)
#   cout<<it<<" ";
#     return 0;
# }
def insertion(arr,temp):
    if len(arr)==0 or arr[-1]<=temp:
       print("aa",arr)
       arr.append(temp)
       return
    x=arr.pop()
    insertion(arr,temp)
    arr.append(x)
    # print(arr)
def sorting(arr):
    if len(arr)<=1:
        return
    temp=arr.pop()
    sorting(arr)
    print(arr,temp)
    insertion(arr,temp)

if __name__=='__main__':
    v=[5,3,2,4,1]
    sorting(v)
    print(v)

# 100 baat ki ek baat, parameter me pass kroge to, it is passed as reference variable meaning,
# many ref variables pointing to same object, hence the original array will be sorted and returned.
# https://www.geeksforgeeks.org/is-python-call-by-reference-or-call-by-value/
# bubble sort compare adjacent elements do swapping according to condition and at the end of inner loop,
# one element goes to its correct position
