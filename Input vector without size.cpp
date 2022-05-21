#include <string>
#include <vector>
#include <sstream>
#include <string>
using namespace std;

int main()
{
    vector<int> vec;
    string buffer;
    int data;
    getline(cin, buffer);
    istringstream iss(buffer);
    while (iss >> data)
          vec.push_back(data);
    //foo(vec);   
}
