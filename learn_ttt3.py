import sys, math, copy


def get_next(current_step, piece,count,level):
	#it's not game over when this is called
	#returns the new state that hasnt been explored
	current_step_count = current_step.count("0") *2
	while True:
		explored_nexts = []
		for state in main_arr:
			for step in range(len(state)):
				if current_step in state[step]:
					if ((len(state[int(math.pow(step, level))]) > 1) and (explored_nexts.count(state[int(math.pow(step, level))]) < 1) and (state[int(math.pow(step, level))] != '000000000') and (len(explored_nexts) != current_step_count/2)):
						#if the next state is not the "game over type" state 
						#and it is not already in the state 
						#and it is not the initial state
						#and the length of explored_nexts is not the max it can possibly be
						#there are only so many moves that can be made from any given position
						print state[step+level]
						explored_nexts.append(state[step+level])
		explored_nexts = list(set(explored_nexts))
		#remove dupes
		if len(explored_nexts) > 1:
			explored_nexts_len = int(math.pow(len(explored_nexts), level) * 2)
			#should this be *2 for this instance and power for the previous ones?
		else:
			explored_nexts_len = len(explored_nexts)
		print 'piece:', piece
		print 'level:',level
		print 'len:',explored_nexts_len
		print 'step count:', current_step_count
		print 'state:', current_step
		print 'exp_nexts', explored_nexts
		
		if explored_nexts_len == current_step_count:
			#make the next 0 the piece and go up a level
			current_step = list(current_step)
			for cell in range(len(current_step)):
				if current_step[cell]== "0":
					current_step[cell] = piece
					break
			current_step_str = ''
			for cell in current_step:
				current_step_str += cell
			return current_step_str
		elif explored_nexts_len < current_step_count:
			current_step = list(current_step)
			current_step_str = ''
			for cell in range(len(current_step)):
				if current_step[cell] == "0" and explored_nexts_len == 0:
					current_step[cell] = piece
					for cell in current_step:
						current_step_str += cell
					return current_step_str
				elif current_step[cell] == "0":
					for next_cell in range(9):
						explored_count = 0
						for explored_next in explored_nexts:

							if ((explored_next[next_cell] == "0") or (explored_next[next_cell] == opp_piece(piece))):#and (next_cell == cell) # or (explored_next[next_cell] == opp_piece(piece))):
								#if the cell that is the same index as the current one is also the same value as the next one, then set it to the piece
								#(explore it if it's unexplored)
								for explored_next in explored_nexts:
									if ((explored_next[next_cell] == '0') or (explored_next[next_cell] == opp_piece(piece))):
										explored_count += 1
								if ((explored_count == explored_nexts_len) and (current_step[next_cell] != opp_piece(piece))):
									current_step[next_cell] = piece
									for cell in current_step:
										current_step_str += cell
									return current_step_str									
			else:
				#current_step[cell] = piece
				#needs to go to the previous iteration where a move can be made, since none can be made at this level in tree
				for cell in current_step:
					current_step_str += cell
				return current_step_str	
		else:
			sys.exit("ayy")
		#current_step[next_cell] = piece

		#print explored_count
		'''if explored_count < len(explored_nexts) and (explored_count != 0 or len(explored_nexts) == 0):
			current_step[cell] = piece
			for cell in current_step:
				current_step_str += cell
			return current_step_str
		elif explored_count == len(explored_nexts):
			sys.exit('lmao')'''
		#if level > 9:
			#go to the next secondary state, or go to initial and increase the count
			#count += 1
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
		
state = '000000000'
piece = 'x'
main_arr = []
step_arr = []
count = 0
level = 1
#append array of arrays to this array

#main_arr = [[[]]]
#main array -> states -> step array(with game over type at end of this)
while True:
	if game_over(state) == False:
		step_arr.append(state)
		backup = copy.deepcopy(state)
		state = get_next(state, piece, count, level)
		if state == backup:
			#level += 1
			while True:
				backup = copy.deepcopy(state)
				#backup is just being 'run again'
				state = get_next(state, piece, count, level)
				if level >= 2:
					sys.exit()
					#this would subsequently not be needed
				if state == backup:
					#end of branch reached...what should be done here so that this path is not followed, go back and go to next step?
					level += 1
					#need something different here, shouldnt actually increase level...perhaps this only occurs when a dead end is encountered
				elif state != backup:
					break
				else:
					sys.exit("lmao")
				#else:
					#sys.exit()
					#state = '000000000'
					#level = 1
					#print 'running again'		
		#new state and switch to other piece
		state_print(state)
		
		piece = opp_piece(piece)
		
	else:
		step_arr.append(state)
		step_arr.append(game_over(state))
		state_print(state)
		print game_over(state)
		
		main_arr.append(step_arr)
		step_arr = []
		state = '000000000'
		#reset to initial
	level = 1
	#print main_arr
	print len(main_arr)
	
	
	