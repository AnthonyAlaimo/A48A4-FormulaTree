"""
# Copyright Anthony, Alaimo, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file. If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

# Do not change any of the class declarations above this comment.

# Add your functions here.
# PEP8 is impossible to fix :(
def build_tree(formula):
    '''(str) -> FormulaTree
    Takes a formula as a string and returns the formula tree of it, if
    the string is valid. If not, then returns None.
    REQ: formula must be a str
    >>> ('(x*-y)')
    AndTree(NotTree(Leaf('y')), Leaf('x')))
    '''
    try:
        # The formula is a leaf
        if len(formula) == 1:
            result = Leaf(formula)
        # The formula is a NotTree of 1 variable
        elif len(formula) == 2:
            result = NotTree(Leaf(formula[1]))
        # The formula is a NotTree of more then 1 variable
        elif formula[0] == '-':
            result = NotTree(build_tree(formula[1:]))
        elif formula[0] == '(':
            # the tree must have more then 2 variables, therefore there must be
            # at least one '*' or '+' inside the formula, if not the formula is
            # invalid
            if '*' not in formula and '+' not in formula:
                result = None
            # checking if there are multiple '(' brackets inside the given
            # formula, which will indicated, the number of sets of variables
            # the formula is made up of.
            elif '(' in formula[1:]:
                if formula[1] == '(':
                    # this count is used to keep track of the current position
                    # in formula we are at in the loop
                    count = 0
                    result = ''
                    while result == '':
                        count += 1
                        # if there is a '(' bracket after an '*' or '+', then
                        # that '*' or '+', represents the main type of tree the
                        # formula is.
                        if formula[count] == '*' or formula[count] == '+':
                            if formula[count - 1] == ')' and (formula[count + 1] == '(' or formula[count + 2] == '('):
                                if formula[count] == '*':
                                    result = AndTree(build_tree(formula[1:count]), build_tree(formula[count + 1:len(formula)-1]))
                                else:
                                    result = OrTree(build_tree(formula[1:count]), build_tree(formula[count + 1:len(formula)-1]))
                            # reasonings is the same, if the next character in
                            # formula is a '-' and the one following that is
                            # '('
                            elif formula[count + 1] == '-':
                                # if the count plus 4 is the length of
                                # the formula, this means we are at the end of
                                # the formula, and the last variable is a leaf
                                if (count + 4) == len(formula):
                                    if formula[count] == '*':
                                        result = AndTree(build_tree(formula[1:count]), NotTree(Leaf(formula[count + 2])))
                                    else:
                                        result = OrTree(build_tree(formula[1:count]), NotTree(Leaf(formula[count + 2])))
                                elif '(' in formula[count + 2:]:
                                    if formula[count + 3] == ')':
                                        pass
                                    elif formula[count] == '*':
                                        result = AndTree(build_tree(formula[1:count]), NotTree(build_tree(formula[count + 2:len(formula)-1])))
                                    else:
                                        result = OrTree(build_tree(formula[1:count]), NotTree(build_tree(formula[count + 2:len(formula)-1])))
                                else:
                                    if formula[count] == '*':
                                        result = AndTree(build_tree(formula[1:count]), NotTree(Leaf(formula[count + 2])))
                                    else:
                                        result = OrTree(build_tree(formula[1:count]), NotTree(Leaf(formula[count + 2])))
                            # if the count plus 3 is the length of
                            # the formula, this means we are at the end of
                            # the formula, and the last variable is a leaf
                            else:
                                if (count + 3) == len(formula):
                                    if formula[count] == '*':
                                        result = AndTree(build_tree(formula[1:count]), Leaf(formula[count + 1]))
                                    else:
                                        result = OrTree(build_tree(formula[1:count]), Leaf(formula[count + 1]))
                # if formula[1] is not a '(', it must be a single variable with
                # or without a '-' or there are '-' in front of '('
                elif formula[1] == '-':
                    neg_count = 0
                    while formula[neg_count + 1] == '-':
                        neg_count += 1
                    if formula[neg_count + 1] != '(':
                        if formula[neg_count + 2] == '*':
                            result = AndTree(build_tree(formula[1:neg_count+2]), build_tree(formula[neg_count+3:len(formula)-1]))
                        else:
                            result = OrTree(build_tree(formula[1:neg_count+2]), build_tree(formula[neg_count+3:len(formula)-1]))
                    else:
                        # this count is used to keep track of the current
                        # position in formula we are at in the loop
                        count = 0
                        result = ''
                        while result == '':
                            count += 1
                            # if there is a '(' bracket after a '*' or '+',
                            # then that '*' or '+', represents the main type of
                            # tree the formula is.
                            if formula[count] == '*' or formula[count] == '+':
                                if formula[count - 1] == ')' and (formula[count + 1] == '(' or formula[count + 2] == '('):
                                    if formula[count] == '*':
                                        result = AndTree(build_tree(formula[1:count]), build_tree(formula[count + 1:len(formula)-1]))
                                    else:
                                        result = OrTree(build_tree(formula[1:count]), build_tree(formula[count + 1:len(formula)-1]))
                                # reasonings is the same, if the next character
                                # in formula is a '-' and the one following
                                # that is '('
                                elif formula[count + 1] == '-':
                                    # if the count plus 4 is the length of the
                                    # formula, this means we are at the end of
                                    # the formula, and the last variable is a
                                    # leaf
                                    if (count + 4) == len(formula):
                                        if formula[count] == '*':
                                            result = AndTree(build_tree(formula[1:count]), NotTree(Leaf(formula[count + 2])))
                                        else:
                                            result = OrTree(build_tree(formula[1:count]), NotTree(Leaf(formula[count + 2])))
                                    elif '(' in formula[count + 2:]:
                                        if formula[count + 3] == ')':
                                            pass
                                        elif formula[count] == '*':
                                            result = AndTree(build_tree(formula[1:count]), NotTree(build_tree(formula[count + 2:len(formula)-1])))
                                        else:
                                            result = OrTree(build_tree(formula[1:count]), NotTree(build_tree(formula[count + 2:len(formula)-1])))
                                    else:
                                        if formula[count] == '*':
                                            result = AndTree(build_tree(formula[1:count]), NotTree(Leaf(formula[count + 2])))
                                        else:
                                            result = OrTree(build_tree(formula[1:count]), NotTree(Leaf(formula[count + 2])))
                                # if the count plus 3 is the length of
                                # the formula, this means we are at the end of
                                # the formula, and the last variable is a leaf
                                else:
                                    if (count + 3) == len(formula):
                                        if formula[count] == '*':
                                            result = AndTree(build_tree(formula[1:count]), Leaf(formula[count + 1]))
                                        else:
                                            result = OrTree(build_tree(formula[1:count]), Leaf(formula[count + 1]))
                # formula[1] must be a variable (leaf)
                else:
                    if formula[2] == '*':
                        result = AndTree(Leaf(formula[1]), build_tree(formula[3:len(formula)-1]))
                    else:
                        result = OrTree(Leaf(formula[1]), build_tree(formula[3:len(formula)-1]))
            # the formula in this case can't have a second ')' otherwise its
            # invalid
            elif formula[-2] == ')':
                result = None
            # There must only be 2 variables in the Tree, so all we need to
            # compare are if these variables are not trees(and how many '-'
            # are in front of the variable) or leafs and if they are being
            # compared using an AndTree or an OrTree
            elif formula[1] == '-':
                neg_count = 0
                while formula[neg_count + 1] == '-':
                    neg_count += 1
                if formula[neg_count + 2] == '*':
                    result = AndTree(build_tree(formula[1:neg_count+2]), build_tree(formula[neg_count+3:len(formula)-1]))
                else:
                    result = OrTree(build_tree(formula[1:neg_count+2]), build_tree(formula[neg_count+3:len(formula)-1]))
            else:
                if formula[2] == '*':
                    result = AndTree(Leaf(formula[1]), build_tree(formula[3:len(formula)-1]))
                else:
                    result = OrTree(Leaf(formula[1]), build_tree(formula[3:len(formula)-1]))
    except:
        # if the tree is not valid, we return none
        result = None
    # this is used just in case the result is invalid but wasn't caught by
    # the try and except
    value = ''
    if result != None:
        for children in result.get_children():
            if children == None:
                value = None
        if value == None:
            result = None
    return result


def draw_formula_tree(root):
    '''(FormulaTree) -> str
    Takes a root to the head of a FormulaTree and returns a str represents the
    Tree of the root
    >>> x = build_tree('(x*-y)')
    >>> draw_formula_tree(x)
    * - y
      x
    '''
    # we know the tree is drawn from the right to left, meaning the first
    # variable of the root will be the variable furthest to the right
    # Need to keep track of the layerer we are on and the current node.
    # use a helper function to create variables for all these things
    formula_tree =  ''
    result = draw_helper(root, formula_tree, tree_layer = 0)
    # resubmit with this one line change, draw tree has one extra blank line at the end
    result = result.strip('\n')
    return result


def draw_helper(cur_root, formula_tree, tree_layer):
    '''(FormulaTree, str, int) -> str
    helper function to help draw formula tree
    '''
    # SelfNote: there should also be a space inbetween symbols of the same
    # layer. ex. - + + x , NOT: -++x
    # the tree layer will define how many spaces are need at any given position
    # of cur_root and it's children
    formula_tree_length = len(formula_tree) - 1
    if len(formula_tree) == 0:
        pass
    elif formula_tree[formula_tree_length] == '\n':
        # if the layer we are on -1 != then we need to subtract a layer to set
        # it back to the correct one, otherwise the for loop will have one
        # extra step and the spacing of variables will be wrong
        if (tree_layer - 1) == 0:
            pass
        else:
            tree_layer = tree_layer - 1
        layer_count = 0
        while layer_count < tree_layer:
            layer_count += 1
            # each layer deep must be indented 2 spaces ahead of the previous
            formula_tree += '  '            
    if cur_root.get_symbol() != '-' and cur_root.get_symbol() != '+' and cur_root.get_symbol() != '*':
        # the cur_root must be a variable, so the formula_tree should move
        # to the next layer
        formula_tree += cur_root.get_symbol()
        formula_tree += '\n'
    else:
        # otherwise just keep adding symbols to the current layer, until it's
        # variable is found
        formula_tree += cur_root.get_symbol()
        # add a space inbetween symbols
        formula_tree += ' '
    # each child of the root, will add another layer on to our string
    # tree in their respective path
    # The root of the tree is connected to the last variable in the formula
    # meaning we must look at the children nodes from right to left
    for children in cur_root.get_children()[::-1]:
        tree_layer += 1
        # recursively, evaluate each child at their specific layer in the tree
        formula_tree = draw_helper(children, formula_tree, tree_layer)
    return formula_tree


def evaluate(root, variables, values):
    '''(FormulaTree, str, str) -> int
    This function takes the root of a formula tree, a string of its variables
    and their corresponding values, and returns a boolean of 0 or 1 depending
    on the outcome
    >>> x = build_tree('(x*-y)')
    >>> evaluate(x, 'xy', '10')
    1
    '''
    # we need a way to refer to variables and their individual values,
    # therefore we need to create a empty dictionary and add these values to it
    variable_values = {}
    count = 0
    while count < len(variables):
        variable_values[variables[count]] = values[count]
        count += 1
    # uses our new dictionary and root and send them to a helper function
    result = evaluate_helper(root, variable_values)
    return result


def evaluate_helper(root, variable_values):
    '''(FormulaTree, dict) -> int
    helps to evaluate Formulas
    '''
    # Divide the types of trees into different cases and evaluate accordingly
    if type(root) == Leaf:
        if variable_values[root.get_symbol()] == '1':
            result = 1
        else:
            result = 0
    # result will be the opposite of whatever it's equal too
    elif type(root) == NotTree:
        for children in root.get_children():
            result = evaluate_helper(children, variable_values)
        if result == 1:
            result = 0
        else:
            result = 1
    # Use two unique variables, to each evaluate a variable of the Andtree
    # then compare their values
    elif type(root) == AndTree:
        child1 = evaluate_helper(root._children[0], variable_values)
        child2 = evaluate_helper(root._children[1], variable_values)
        # if both the values are the same, statement is true(1), otherwise
        # if they are not the same the statement msut be false(0)
        if child1 == child2 and child1 == 1:
            result = 1
        else:
            result = 0
    # Similar to the AndTree except then requirements for result to be 1 or 0
    # are different. Also long as both child don't evaluate to 0, result
    # will be True (1)
    elif type(root) == OrTree:
        child1 = evaluate_helper(root._children[0], variable_values)
        child2 = evaluate_helper(root._children[1], variable_values)
        if child1 == child2 and child1 == 0:
            result = 0
        else:
            result = 1
    return result


def play2win(roots, turns, variables, values):
    '''(FormulaTree, str, str, str) -> int
    This function is given the root to a formula tree, a turn order, the
    variables in the formula and a string for the values which the players
    have chose thus far. With this information the user will be given an output
    indicating what move is the best for them to make. Player E wants an output
    of 1 and player A wants an output of 0
    REQ: len(turns) > len(values)
    >>> x = build_tree('(x*-y)')
    >>> play2win(x, 'EA', 'xy', '1')
    1
    '''
    # Used to figure out who's turn it is
    player_turn = turns[len(values)]
    if player_turn == 'E':
        goal_value = 1
    else:
        goal_value = 0
    # The next move will decide the outcome of the game
    if (len(values) + 1) == len(turns):
        if goal_value == 1:
            # if Player E picked '1' or '0'
            outcome_1 = evaluate(roots, variables, values + '1')
            outcome_0 = evaluate(roots, variables, values + '0')
            # Winning move or player can't win
            if outcome_1 == 1:
                result = 1
            elif outcome_0 == 1:
                result = 0
            else:
                result = 1
        else:
            # Same as above but for Player A
            outcome_1 = evaluate(roots, variables, values + '1')
            outcome_0 = evaluate(roots, variables, values + '0')
            if outcome_1 == 0:
                result = 1
            elif outcome_0 == 0:
                result = 0
            else:
                result = 0
    # Gives the best possible option
    else:
        result = (1 if goal_value == 1 else 0)
    return result

#testing formulas
formula = '---(-(x*(y*x))+---(x+-y))'
formula2 = '---x'
formula3 = '(--x*(x+y))'
formula4 = '((x*y)+-z)'
formula5 = '((x*b)+-(y+d))'
formula6 = '(x*y*z)'
formula7 ='--(--(x+(--y+d))*--(--(u*-x)+--(-d*-q)))'
#testing formula7
print(build_tree(formula7))
x = build_tree(formula7)
print(draw_formula_tree(NotTree(AndTree(NotTree(OrTree(Leaf('a'), Leaf('b'))), NotTree(Leaf('c'))))))
print(evaluate(x, 'xyduq', '10111'))
print(play2win(x, 'EAAAA', 'xyduq', '0100'))
