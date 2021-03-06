from collections import OrderedDict
import random

from axelrod import Actions, Player, random_choice

C, D = Actions.C, Actions.D


class RiskyQLearner(Player):
    """A player who learns the best strategies through the q-learning
    algorithm.

    This Q learner is quick to come to conclusions and doesn't care about the
    future.

    Names:

    - Risky Q Learner: Original strategy by Geraint Palmer
    """

    name = 'Risky QLearner'
    classifier = {
        'memory_depth': float('inf'),  # Long memory
        'stochastic': True,
        'makes_use_of': set(["game"]),
        'long_run_time': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }
    learning_rate = 0.9
    discount_rate = 0.9
    action_selection_parameter = 0.1
    memory_length = 12

    def __init__(self):
        """Initialises the player by picking a random strategy."""

        super().__init__()

        # Set this explicitely, since the constructor of super will not pick it up
        # for any subclasses that do not override methods using random calls.
        self.classifier['stochastic'] = True

        self.prev_action = random_choice()
        self.history = []
        self.score = 0
        self.Qs = OrderedDict({'':  OrderedDict(zip([C, D], [0, 0]))})
        self.Vs = OrderedDict({'': 0})
        self.prev_state = ''

    def receive_match_attributes(self):
        (R, P, S, T) = self.match_attributes["game"].RPST()
        self.payoff_matrix = {C: {C: R, D: S}, D: {C: T, D: P}}

    def strategy(self, opponent):
        """Runs a qlearn algorithm while the tournament is running."""
        state = self.find_state(opponent)
        reward = self.find_reward(opponent)
        if state not in self.Qs:
            self.Qs[state] = OrderedDict(zip([C, D], [0, 0]))
            self.Vs[state] = 0
        self.perform_q_learning(self.prev_state, state, self.prev_action, reward)
        action = self.select_action(state)
        self.prev_state = state
        self.prev_action = action
        return action

    def select_action(self, state):
        """
        Selects the action based on the epsilon-soft policy
        """
        rnd_num = random.random()
        p = 1. - self.action_selection_parameter
        if rnd_num < p:
            return max(self.Qs[state], key=lambda x: self.Qs[state][x])
        return random_choice()

    def find_state(self, opponent):
        """
        Finds the my_state (the opponents last n moves +
        its previous proportion of playing C) as a hashable state
        """
        prob = '{:.1f}'.format(opponent.cooperations)
        return ''.join(opponent.history[-self.memory_length:]) + prob

    def perform_q_learning(self, prev_state, state, action, reward):
        """
        Performs the qlearning algorithm
        """
        self.Qs[prev_state][action] = (1.-self.learning_rate)*self.Qs[prev_state][action] + self.learning_rate*(reward + self.discount_rate*self.Vs[state])
        self.Vs[prev_state] = max(self.Qs[prev_state].values())

    def find_reward(self, opponent):
        """
        Finds the reward gained on the last iteration
        """

        if len(opponent.history) == 0:
            opp_prev_action = random_choice()
        else:
            opp_prev_action = opponent.history[-1]
        return self.payoff_matrix[self.prev_action][opp_prev_action]

    def reset(self):
        """
        Resets scores and history
        """
        super().reset()

        self.Qs = {'': {C: 0, D: 0}}
        self.Vs = {'': 0}
        self.prev_state = ''
        self.prev_action = random_choice()


class ArrogantQLearner(RiskyQLearner):
    """A player who learns the best strategies through the q-learning
    algorithm.

    This Q learner jumps to quick conclusions and cares about the future.

    Names:

    - Arrogant Q Learner: Original strategy by Geraint Palmer
    """

    name = 'Arrogant QLearner'
    learning_rate = 0.9
    discount_rate = 0.1


class HesitantQLearner(RiskyQLearner):
    """A player who learns the best strategies through the q-learning algorithm.

    This Q learner is slower to come to conclusions and does not look ahead much.

    Names:

    - Hesitant Q Learner: Original strategy by Geraint Palmer
    """

    name = 'Hesitant QLearner'
    learning_rate = 0.1
    discount_rate = 0.9


class CautiousQLearner(RiskyQLearner):
    """A player who learns the best strategies through the q-learning algorithm.

    This Q learner is slower to come to conclusions and wants to look ahead
    more.

    Names:

    - Cautious Q Learner: Original strategy by Geraint Palmer
    """

    name = 'Cautious QLearner'
    learning_rate = 0.1
    discount_rate = 0.1
