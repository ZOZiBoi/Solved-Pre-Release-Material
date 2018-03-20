maxVotes = 30
while True:
    candidates = int(input("How many candidates?"))
    print(candidates)
    if (candidates>=2 and candidates<=4):
        break
    else:
        print("Invalid candidate number. Enter a valid number b/w 2 and 4")
vote = [0] * candidates
candidateName = vote[:]
for i in range(0,candidates):
    candidateName[i] = input("Name of candidate?")
for i in range(0,maxVotes):
    for i in range(0,candidates):
        print("Options: " + candidateName[i] + "    " + str(i+1))
    while True:
        option = int(input("Select one"))
        if (option<=candidates and option>0):
            vote[option-1] += 1
            print("You voted for " + candidateName[option-1] )
            break
        else:
            print("Enter a valid vote")
for i in range(0,candidates):
    for j in range(0,candidates):
        if (vote[j]<vote[i]):
            tmp = vote[i]
            tmp1 = candidateName[i]
            vote[i] = vote [j]
            candidateName[i] = candidateName[j]
            vote[j] = tmp
            candidateName[j] = tmp1
print(list(vote))
print(list(candidateName))
if (vote[0]>vote[1]):
    print("NEW CLASS CAPTAIN: " + candidateName[0])
else:
    print("NO OVERALL WINNER")
