class Solution {
public:
    vector<string> findHighAccessEmployees(vector<vector<string>>& access_times) {
     // name -> access_times
        unordered_map<string,vector<int>>mp;
        for(auto &it:access_times){
            int time = stoi(it[1]); // convert to int
            mp[it[0]].push_back(time); // store in map
        }
        
         // sort each employee access times
          for(auto &it: mp)
              sort(it.second.begin(),it.second.end());
        
        // scan sorted access times to check if access times>=3
        vector<string>ans;  // to store required employees
        for(auto &it :mp){
                   vector <int> &time= it.second;
                   for(int i=2;i<time.size();i++){
                      if(time[i] - time[i-2]<100){
                          // store employee in ans and move to other employee
                          ans.push_back(it.first);
                          break;
                      }
            }
        }
            return ans;
    }
};   // here tc is o(nlogn) and sc is o(n)