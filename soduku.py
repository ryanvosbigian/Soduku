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
	P00= Position()
	P01= Position()
	P02= Position()
	P03= Position()
	P04= Position()
	P05= Position()
	P06= Position()
	P07= Position()
	P08= Position()
	P10= Position()
	P11= Position()
	P12= Position()
	P13= Position()
	P14= Position()
	P15= Position()
	P16= Position()
	P17= Position()
	P18= Position()
	P20= Position()
	P21= Position()
	P22= Position()
	P23= Position()
	P24= Position()
	P25= Position()
	P06= Position()
	P27= Position()
	P28= Position()
	P30= Position()
	P31= Position()
	P32= Position()
	P33= Position()
	P34= Position()
	P35= Position()
	P36= Position()
	P37= Position()
	P38= Position()
	P40= Position()
	P41= Position()
	P42= Position()
	P43= Position()
	P44= Position()
	P45= Position()
	P46= Position()
	P47= Position()
	P48= Position()
	P50= Position()
	P51= Position()
	P52= Position()
	P53= Position()
	P54= Position()
	P55= Position()
	P56= Position()
	P57= Position()
	P58= Position()
	P60= Position()
	P61= Position()
	P62= Position()
	P63= Position()
	P64= Position()
	P65= Position()
	P66= Position()
	P67= Position()
	P68= Position()
	P70= Position()
	P71= Position()
	P72= Position()
	P73= Position()
	P74= Position()
	P75= Position()
	P76= Position()
	P77= Position()
	P78= Position()
	P80= Position()
	P81= Position()
	P82= Position()
	P83= Position()
	P84= Position()
	P85= Position()
	P86= Position()
	P87= Position()
	P88= Position()
	
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

