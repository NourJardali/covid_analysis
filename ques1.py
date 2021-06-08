candidates = []
votes = []
totalVotes = []
total = 0
for i in range(5):
    name = input("Enter the last name of candidate: ")
    vote = int(input("Enter number of votes received: "))
    candidates.append(name)
    votes.append(vote)
    total = total + vote

for i in range(5):
    percentage = (votes[i] / total) * 100
    percentage = round(percentage, 2)
    totalVotes.append(percentage)
    print("Candidate :")
    print("Last name: ",candidates[i])
    print("Votes Received: ",votes[i])
    print("\"%\" of Total votes: ",percentage)

max = totalVotes[0]
index = 0
for i in range(5):
    if max < totalVotes[i]:
        max = totalVotes[i]
        index = i

print("The winner of the election is ",candidates[index])