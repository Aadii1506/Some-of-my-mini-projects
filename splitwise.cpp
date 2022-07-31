// suppose we wanna solve a problem in which a pays some amnt to b and b pays some amnt to c AND c pays some amnt to a. so in order to solve this in least transaction we use this algorithm

#include<bits/stdc++.h>
using namespace std;

class person_compare{
    public:
    bool operator()(pair<string,int>p1,pair<string,int>p2){
        return p1.second<p2.second;
    }
};

int main(){
    int no_of_transaction,friends;
    cout<<"Enter the number of transactions and number of friends\n";
    cin>>no_of_transaction>>friends;
    int amount;
    string x,y;

    map<string,int> net;    //to store amnt against name
    while(no_of_transaction--){
        cout<<"Enter the person names and amount given by first person to second\n";
        cin>>x>>y>>amount;
        if(net.count(x)==0)net[x]=0;
        if(net.count(y)==0)net[y]=0;
        net[x]-=amount;
        net[y]+=amount;
    }

    
    //iterate over the persons and add those person in multiset who have non zero net
    multiset<pair<string,int>,person_compare> m;
    for(auto p:net){
        string person=p.first;
        int amount=p.second;
        if(net[person]!=0){
            m.insert(make_pair(person,amount));
        }
    }

    //ready to make settlement through   start and end
    int cnt=0;
    while(!m.empty()){
        auto low=m.begin();
        auto high=prev(m.end());
        int debit=low->second;
        string debit_person=low->first;
        
        string credit_person=high->first;
        int credit=high->second;
        //pop them out from set
        m.erase(low);
        m.erase(high);

        int settled_amnt=min(-debit,credit);
        debit+=settled_amnt;
        credit+=settled_amnt;

        //print the transaction btw ppl
        cout<<debit_person<<" will pay "<<settled_amnt<<" to "<<credit_person<<endl;
        if(debit!=0){
            m.insert(make_pair(debit_person,debit));
        }
        if(credit!=0){
            m.insert(make_pair(credit_person,credit));
        }
        cnt++;
    }
    cout<<cnt<<endl;

    return 0;
}