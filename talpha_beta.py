def alpha_beta_search(node):
		"""
		:param node: current node
		:return: best state (child node)

		min max tree search with alpha-beta pruning assuming the player is maximizing player

		"""
		infinity = float('inf')
		best_val = -infinity
		beta = infinity

		successors = self.getSuccessors(node)
		best_state = None
		for state in successors:
			value = self.min_value(state, best_val, beta)
			if value > best_val:
				best_val = value
				best_state = state
		return best_state

def max_value(node, alpha, beta):
		if self.isTerminal(node):
			return self.getUtility(node)
		infinity = float('inf')
		value = -infinity

		successors = self.getSuccessors(node)
		for state in successors:
			value = max(value, self.min_value(state, alpha, beta))
			if value >= beta:
				return value
			alpha = max(alpha, value)
		return value

	def min_value(self, node, alpha, beta):
		if self.isTerminal(node):
			return self.getUtility(node)
		infinity = float('inf')
		value = infinity

		successors = self.getSuccessors(node)
		for state in successors:
			value = min(value, self.max_value(state, alpha, beta))
			if value <= alpha:
				return value
			beta = min(beta, value)

		return value