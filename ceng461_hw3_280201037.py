import numpy as np

R = {1:0.2, 1.25:0.3, 1.5:0.3, 1.75:0.2}
M = 100
discount = 0.9
utilites = np.zeros(M+1) #initial utilities are zero 
states = np.arange(start=0, stop=M+1, step=1)


def value_iteration(states, utilites, R, discount,M):
    updated_utilities = np.zeros(len(utilites))
    optimal_policy = np.zeros(len(utilites))
    for state in states:
        policy_utilities = []
        for policy in range(0,state+1):
            expected_utility = 0
            for r, prob in R.items():
                remaining = state-policy
                next_population = min(M, np.floor(remaining*r+0.5))
                expected_utility += prob*utilites[int(next_population)]
            utility = policy + discount*expected_utility
            policy_utilities.append(utility)
        updated_utilities[state] = max(policy_utilities)
        optimal_policy[state] = np.argmax(policy_utilities)

    return updated_utilities,optimal_policy


for i in range (0,2):
    utilites, optimal_policies = value_iteration(states,utilites,R,0.9,M)
    print("Utilities and optimal policies after",i+1,"Iteration")
    print()
    for u in range (0,len(utilites)):
        print("U"+str(i+1)+"(s = "+str(u)+"):", utilites[u])
        print("Optimal policy is to catch",optimal_policies[u],"fish for s="+str(u))
        print()

