


class Solution {
public:
    int maximumSwap(int num) {
        string a = to_string(num);
        int res = num;
        for(int i=0; i<a.size(); i++){
            for(int j=i+1; j<a.size(); j++){
                swap(a[i], a[j]);
                res = max(res, stoi(a));
                swap(a[i], a[j]);
            }
        }
        return res;
    }
};


int main(int argc, char* argv[]) {
    int num = 2732;
    Solution s;
    cout<<s.maximumSwap(num)<<endl;
    return 0;
}