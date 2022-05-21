// TwoSum
#include<iostream>
#include<vector>
#include<sstream>
#include<map>
using namespace std;

int main(){
	vector<int>nums;
	string buffer;
	int input;
	getline(cin,buffer);
	istringstream iss(buffer);
	while(iss>>input) nums.push_back(input);
	int target;cin>>target;
	map<int,int>TwoSum;
	for(int i=0;i<nums.size();++i){
		if(TwoSum.find(target-nums[i])!=TwoSum.end()) cout<<TwoSum.find(target-nums[i])->second<<' '<<i;
		TwoSum.emplace(nums[i],i);
	}
}
