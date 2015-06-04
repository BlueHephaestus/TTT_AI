#this will not add duplicate states to the main array, resulting in a smaller tree and also hopefully the end of the pattern problem
import sys, math, copy, os#, davy

			
def game_over(state):
	for i in range(3):
		if state[i] == state[i+3] == state[i+6]:
			if state[i] == 'x':
				return '1'
			elif state[i] == 'o':
				return '2'
			#vertical
		elif state[i*3] == state[i*3+1] == state[i*3+2]:
			if state[i*3] == 'x':
				return '1'
			elif state[i*3] == 'o':
				return '2'
	#horizontal
	if state[0] == state[4] == state[8]:
		if state[0] == 'x':
			return '1'
		elif state[0] == 'o':
			return '2'
	if state[2] == state[4] == state[6]:	
		if state[2] == 'x':
			return '1'
		elif state[2] == 'o':
			return '2'
	#diagonal
	if '0' in state:
		return False
	return '3'
		
def opp_piece(piece):
	if piece == 'x':
		opp_piece = 'o'
	elif piece == 'o':
		opp_piece = 'x'
	return opp_piece	
	
def state_print(state):
	for i in range(3):
		print "%s|%s|%s" % (state[i*2+i], state[i*2+i+1], state[i*2+i+2])

def main_print(main):
	count = 1
	for state in main:
		print count, state, count
		count += 1
		
def get_full_prev_states(main_arr, prev_state):
	#this may not be fully accurate, compare with more steps if this problem arises
	full_prev_state = []
	for state in main_arr:
		for step in range(len(state)):
			if prev_state in state[step]:
				step_depth = step -1
				while step_depth >= 0:
					full_prev_state.append(state[step_depth])
					step_depth -= 1
				return full_prev_state

def main_write(main_arr):
	log_path = "C:\\Users\\Steve\\Desktop\\Programming\\Challenges\\shiro\\main_log.log"
	log = open(log_path, 'a')
	for state in main_arr:
		state_str = ''
		for step in state:
			state_str += step
		state_str += '\n'
		log.write(state_str)
def clear_logs():
	os.remove("main_log.log")
			
state = '000000000'
piece = 'x'
main_arr = [['000000000']]
depth = 0

while True:
	full_prev_state_arr = []
	#the rest of the states before the prev_state_arr
	prev_state_arr = []
	state_arr = []
	####
	#need to do something special for the initial, perhaps just set if depth = 1 then prev_state_arr = ['000000000']
	#also need to check if the one that follows them is a victory type, or a victory type is in it, ie xoxoxoxox3, so as not to follow/worry about that one any further
	#need to figure out piece situation
		#alternate pieces
		#start over again with a different first move, unless x always goes first
	#not getting past depth 2, only of len 3
	for state in main_arr:
		#print prev_state_arr
		if len(state) == depth + 1:
			state_arr.append(state[depth])
			#determine if there are nodes that can be made from the previous state
		elif len(state) == depth:
			#if game_over(state[depth-1]) != False:
			prev_state_arr.append(state[depth-1])
	#print 'prev:', prev_state_arr
	#print 'curr:', state_arr
	#for state in prev_state_arr:
		#if state.count('0') > len(state_arr):
			#if there should be more nodes at the current depth according to the number of 0s in a previous state,<---- BAKA!
			#go through each previous state and generate a new state from all the zeroes present, and then compare the ones created with the ones in the depth
	new_state_arr = []
	#print prev_state_arr
	for prev_state in prev_state_arr:
		for cell in range(len(prev_state)):
			if prev_state[cell] == '0':
				backup_prev_state = copy.deepcopy(prev_state)
				prev_state = list(prev_state)
				prev_state[cell] = piece 
				prev_state_str = ''
				for cell in prev_state:
					prev_state_str += cell
				new_state_arr.append(prev_state_str)
				prev_state = backup_prev_state
		#at this point add the elements from new state arr to the previous state to make a new array
		#perhaps find a way to do this without being in a loop b/c this causes there to be so many?
		for new_state in new_state_arr:
			full_state_arr = []
			full_prev_states = get_full_prev_states(main_arr, prev_state)
			#need to add the full sequence of previous states to this before doing the new one, however is having trouble getting past level 3
			if len(full_prev_states) > 0:
				for full_prev_state in full_prev_states:
					full_state_arr.append(full_prev_state)
			full_state_arr.append(prev_state)
			if game_over(new_state) != False:
				new_state += game_over(new_state)
			full_state_arr.append(new_state)
			main_arr.append(full_state_arr)
	main_print(main_arr)
	piece = opp_piece(piece)
	depth+=1			
	






















	
	
	
	