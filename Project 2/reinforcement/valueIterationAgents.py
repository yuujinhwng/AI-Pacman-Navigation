# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        
        # for i in range(self.iterations):
        #     value = util.Counter()
        #     states = self.mdp.getStates()
        #     for state in states:
        #         max = float("-inf")
        #         for action in self.mdp.getPossibleActions(state):
        #             q_value = self.computeQValueFromValues(state, action)
        #             value_opt += q_value
        #             if q_value > max:
        #                 max = q_value
        #             value[state] = max
        #         self.values = value

        #for value = 0
        # for iteration t....
        # for each state
        # value(t) = qvalue(t-1)
        states = self.mdp.getStates()

        for iteration in range(self.iterations):
            value = util.Counter()
            for state in states:
                actions = self.mdp.getPossibleActions(state)
                if self.mdp.isTerminal(state):
                    value[state] = 0
                else:
                    value[state] = max(self.computeQValueFromValues(state, action) for action in actions)
            self.values = value    

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        q_value = 0.0
        transition_state = self.mdp.getTransitionStatesAndProbs(state, action)
        for transition in transition_state:
            q_value += transition[1] * (self.mdp.getReward(state, action, transition[0])+(self.discount * self.getValue(transition[0])))
        return q_value
        util.raiseNotDefined()
  
    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        actions = self.mdp.getPossibleActions(state)
        best_action = None
        best_action_val = float("-inf")
        for action in actions:
            q_value = self.computeQValueFromValues(state, action)
            if q_value > best_action_val:
                best_action_val = q_value
                best_action = action
        return best_action
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
