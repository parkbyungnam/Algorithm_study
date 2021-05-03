def solution(participant, completion):
    temp = participant
    for man in participant:
        if man in completion:
            participant.remove(man)
        elif man not in completion:
            print(man)
    #answer = participant[0]
    for p in participant:
        print(p)
    #return answer

solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])