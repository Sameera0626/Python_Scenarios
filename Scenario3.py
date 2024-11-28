Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n . The second line contains an array A[]  of n integers each separated by a space.

n=int(input())

#input scores convert in to a list of integers
scores=list(map(int,input().split())

#remove duplicates
unique_scores=list(set(scores))

#sorted by descing order
unique_scores.sort(reverse=True)

#second runner up score
runner_up=unique_scores[1]
print(runner_up)
            

