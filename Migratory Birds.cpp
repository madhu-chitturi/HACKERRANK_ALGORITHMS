/*                                                                  Migratory Birds
                                                                  
Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

Example

There are two each of types  and , and one sighting of type . Pick the lower of the two types seen twice: type .

Function Description

Complete the migratoryBirds function in the editor below.

migratoryBirds has the following parameter(s):

int arr[n]: the types of birds sighted
Returns

int: the lowest type id of the most frequently sighted birds
Input Format

The first line contains an integer, , the size of .
The second line describes  as  space-separated integers, each a type number of the bird sighted.

Constraints

It is guaranteed that each type is , , , , or .
Sample Input 0

6
1 4 4 4 5 3
Sample Output 0

4                    */



<=========== C++ SOLUTION===============>

#include <bits/stdc++.h>

using namespace std;
void countsort(int arr[],int n){
    int cnt[n+1];
    for(int i=0;i<n;i++){
        cnt[i]=0;
    }
    for(int i=0;i<n;i++){
        cnt[arr[i]]++;
    }
    for(int i=0;i<n;i++){
        arr[i]=cnt[i];
    }
}
int main(){
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    countsort(arr,n);
    int max=0,min=0;
    for(int i=0;i<n;i++){
        if(arr[i]>max){
            max=arr[i];
            if(min!=i){
                min=i;
            }
        }
    }
    printf("%d",min);
}
