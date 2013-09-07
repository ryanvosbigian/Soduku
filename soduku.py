#!/usr/bin/python2.7 -tt
import sys, pygame,time
from pygame.locals import *

print "Welcome to Soduku. Watch, interact, and admire."

AI= raw_input("What level of intelligence do you want? A fly's brain (1), cyberman (2), or dalek (3). 1, 2, or 3?: ")

Commit summary: Extended description: (optional)
ryanvosbigian ryanvosbigian@gmail.com



def flyexplode():
	
	print '''

		   * 
		 *****
	     *************
	   *****************
	  *******************
	 *********************
	***********************
	 *********************
          *******************
	    ***************
	     *************
	         *****
		   *
'''
  	




if AI== '1':
	print "Can not comprehend numbers. Self destruct in 5..."
	time.sleep(4)
	flyexplode()
	sys.exit()

board= [[0,0,0,8,0,0,0,1,4],[1,0,6,4,0,0,7,5],[0,4,7,5,3,0,0,0,0],[9,0,0,0,5,0,0,6,2],[0,0,0,7,0,9,0,0,0],[6,3,0,0,4,0,0,0,5],[0,0,0,0,8,7,3,4,0],[0,1,4,0,0,5,6,0,9],[8,9,0,0,0,4,0,0,0]]


def solvecyberman(board,pos0):
	def addx(x):
		print "is this even running?"
		if x== 1:
			x=0
			return x
		x=1
		return x


	row1= board[0]
	row2= board[1]
	line2= [board[0][1],board[1][1]]
	line1= [board[0][0],board[1][0]]
	posnum=[2,1]
	whatrotation= 0
	x=0
	while True:
		print x
		print posnum[x]
		posant=(pos0[1])
		pospost=(pos0[4])
		if int(posant)==0:
			if pospost==0:
				board[0][0]= posnum[x]
			else:
				exec 'board[0][1]='+str(posnum[x])
			
		else:		
			exec 'board'+pos0+'='+str(posnum[x])
		print board
		if whatrotation == 1:
			break
		whatrotation+=1
		
		if 0 not in row1:
			if row1[0]==row1[1]:
				print "test test"
				x= addx(x)
		elif row1[0]==0:
			exec 'board[0][0]='+str(posnum[x])	
			
		elif 0 not in row2:
			if row2[0]==row2[1]:
				print "Test"
				x= addx(x)
		elif 0 not in line1:
			if line1[0]==line1[1]:
				print "TEST"
				x= addx(x)
		elif 0 not in line2:
			if line2[0]==line2[1]:
				print "Test test"
				x= addx(x)
		else:
			break


		
		if row1[0]==row1[1]:
			print "test test"
			x= addx(x)
		if row2[0]==row2[1]:
			print "Test"
			x= addx(x)
		if line1[0]==line1[1]:
			print "TEST"
			x= addx(x)
		if line2[0]==line2[1]:
			print "Test test"
			x= addx(x)
		else:
			break
		
		
	return board



def cybermansolve(board):
	row1= board[0]
	row2= board[1]
	line2= [board[0][1],board[1][1]]
	line1= [board[0][0],board[1][0]]
	while True:
		if 0 in row1:
			if 0 in line1:
				print "TESTS"
				board=solvecyberman(board,'[0][0]')
			else:
				print "tests"
				board=solvecyberman(board,'[0][1]')
		else:
			if 0 in line1:
				print "and more tests"
				board=solvecyberman(board,'[1][0]')
			else:
				print "I like tests"
				board=solvecyberman(board,'[1][1]')
		row1= board[0]
		row2= board[1]
		line2= [board[0][1],board[1][1]]
		line1= [board[0][0],board[1][0]]
		if 0 not in row1:
			if row1[0]==row1[1]:
				print "_test test"
		elif 0 not in row2:	
			if row2[0]==row2[1]:
				print "_Test"
		elif 0 not in line1:	
			if line1[0]==line1[1]:
				print "_TEST"
		elif 0 not in line2:		
			if line2[0]==line2[1]:
				print "_Test test"
			
		else:
			break
	
class Position():
	def init(self,board,position): #position like (x,y)
		possibles= [1,2,3,4,5,6,7,8,9]
		self.board = board
		self.pos = position
		self.row= board[position[0]]
		self.box=[]
		for liness in self.board:
			if position[0] in [0,1,2]:
				if position[1] in [0,1,2]:
					self.box = [board[0][:3],board[1][:3],board[2][:3]]	
				elif position[1] in [3,4,5]:
					self.box = [board[0][3:6],board[1][3:6],board[2][3:6]]
				elif position[1] in [6,7,8]:
					self.box = [board[0][6:],board[1][6:],board[2][6:]]
				else:
					raise SystemExit
			elif position[0] in [3,4,5]:
				if position[1] in [0,1,2]:
					self.box = [board[3][:3],board[4][:3],board[5][:3]]	
				elif position[1] in [3,4,5]:
					self.box = [board[3][3:6],board[4][3:6],board[5][3:6]]
				elif position[1] in [6,7,8]:
					self.box = [board[3][6:],board[4][6:],board[5][6:]]
				else:
					raise SystemExit
			elif  position[0] in [6,7,8]:
				if position[1] in [0,1,2]:
					self.box = [board[6][:3],board[7][:3],board[8][:3]]
				elif position[1] in [3,4,5]:
					self.box = [board[6][3:6],board[7][3:6],board[8][3:6]]
				elif position[1] in [6,7,8]:
					self.box = [board[6][6:],board[7][6:],board[8][6:]]
				else:
					raise SystemExit
			else:
				print "There was an error"
				raise SystemExit 
		self.line= []
		for lines in self.board:
			(self.line).append(lines[position[1]])
		for numbers in possibles:
			if numbers in self.line or self.row or self.box:
				possibles.remove(numbers)
		if len(possibles) == 1:
			return [self.board[position[0]][position[1]], True]
		else:
			return [possibles, False]
		
		


	
def daleksolve(board):
	P00= Position(board,[0,0])
	P01= Position(board,[0,1])
	P02= Position(board,[0,2])
	P03= Position(board,[0,3])
	P04= Position(board,[0,4])
	P05= Position(board,[0,5])
	P06= Position(board,[0,6])
	P07= Position(board,[0,7])
	P08= Position(board,[0,8])
	P10= Position(board,[1,0])
	P11= Position(board,[1,1])
	P12= Position(board,[1,2])
	P13= Position(board,[1,3])
	P14= Position(board,[1,4])
	P15= Position(board,[1,5])
	P16= Position(board,[1,6])
	P17= Position(board,[1,7])
	P18= Position(board,[1,8])
	P20= Position(board,[2,0])
	P21= Position(board,[2,1])
	P22= Position(board,[2,2])
	P23= Position(board,[2,3])
	P24= Position(board,[2,4])
	P25= Position(board,[2,5])
	P06= Position(board,[2,6])
	P27= Position(board,[2,7])
	P28= Position(board,[2,8])
	P30= Position(board,[3,0])
	P31= Position(board,[3,1])
	P32= Position(board,[3,2])
	P33= Position(board,[3,3])
	P34= Position(board,[3,4])
	P35= Position(board,[3,5])
	P36= Position(board,[3,6])
	P37= Position(board,[3,7])
	P38= Position(board,[3,8])
	P40= Position(board,[4,0])
	P41= Position(board,[4,1])
	P42= Position(board,[4,2])
	P43= Position(board,[4,3])
	P44= Position(board,[4,4])
	P45= Position(board,[4,5])
	P46= Position(board,[4,6])
	P47= Position(board,[4,7])
	P48= Position(board,[4,8])
	P50= Position(board,[5,0])
	P51= Position(board,[5,1])
	P52= Position(board,[5,2])
	P53= Position(board,[5,3])
	P54= Position(board,[5,4])
	P55= Position(board,[5,5])
	P56= Position(board,[5,6])
	P57= Position(board,[5,7])
	P58= Position(board,[5,8])
	P60= Position(board,[6,0])
	P61= Position(board,[6,1])
	P62= Position(board,[6,2])
	P63= Position(board,[6,3])
	P64= Position(board,[6,4])
	P65= Position(board,[6,5])
	P66= Position(board,[6,6])
	P67= Position(board,[6,7])
	P68= Position(board,[6,8])
	P70= Position(board,[7,0])
	P71= Position(board,[7,1])
	P72= Position(board,[7,2])
	P73= Position(board,[7,3])
	P74= Position(board,[7,4])
	P75= Position(board,[7,5])
	P76= Position(board,[7,6])
	P77= Position(board,[7,7])
	P78= Position(board,[7,8])
	P80= Position(board,[8,0])
	P81= Position(board,[8,1])
	P82= Position(board,[8,2])
	P83= Position(board,[8,3])
	P84= Position(board,[8,4])
	P85= Position(board,[8,5])
	P86= Position(board,[8,6])
	P87= Position(board,[8,7])
	P88= Position(board,[8,8])
	
	if P00[1] or P01[1] or P02[1] or P03[1] or P04[1] or P05[1] or P06[1] or P07[1] or P08[1] == True:
		daleksolve(board)
	if P10[1] or P11[1] or P12[1] or P13[1] or P14[1] or P15[1] or P16[1] or P17[1] or P18[1] == True:
		daleksolve(board)
	if P20[1] or P21[1] or P22[1] or P23[1] or P24[1] or P25[1] or P26[1] or P27[1] or P28[1] == True:
		daleksolve(board)
	if P30[1] or P31[1] or P32[1] or P33[1] or P34[1] or P35[1] or P36[1] or P37[1] or P38[1] == True:
		daleksolve(board)
	if P40[1] or P41[1] or P42[1] or P43[1] or P44[1] or P45[1] or P46[1] or P47[1] or P48[1] == True:
		daleksolve(board)
	if P50[1] or P51[1] or P52[1] or P53[1] or P54[1] or P55[1] or P56[1] or P57[1] or P58[1] == True:
		daleksolve(board)
	if P60[1] or P61[1] or P62[1] or P63[1] or P64[1] or P65[1] or P66[1] or P67[1] or P68[1] == True:
		daleksolve(board)
	if P70[1] or P71[1] or P72[1] or P73[1] or P74[1] or P75[1] or P76[1] or P77[1] or P78[1] == True:
		daleksolve(board)
	if P80[1] or P81[1] or P82[1] or P83[1] or P84[1] or P85[1] or P86[1] or P87[1] or P88[1] == True:
		daleksolve(board)
	
	print board

	

if AI=='2':
	cybermansolve(board)
else:
	daleksolve(board)

