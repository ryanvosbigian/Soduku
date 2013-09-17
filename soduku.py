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
	X,Y = 0,0
	
	for repeat in range(81):
		exec "P"+ str(X) + str(Y)+ "= Position()"
		if Y == 8: Y = 0
		else: Y+=1
		X+=1
	"""P00= Position()
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
	P88= Position()"""
	##########################RUNING IT PART STARTS############################################################################
	x,y = 0,0
	for repeats in range(81):
		exec "p" + x + y + "= P" + x + y + ".init(board,[" + x + "," + y + "])"
		if y = 8: y = 0
		else: y+=1
		x += 1
	"""p00= P00.init(board,[0,0])
	p01= P01.init(board,[0,1])
	p02= P02.init(board,[0,2])
	p03= P03.init(board,[0,3])
	p04= P04.init(board,[0,4])
	p05= P05.init(board,[0,5])
	p06= P06.init(board,[0,6])
	p07= P07.init(board,[0,7])
	p08= P08.init(board,[0,8])
	p10= P10.init(board,[1,0])
	p11= P11.init(board,[1,1])
	p12= P12.init(board,[1,2])
	p13= P13.init(board,[1,3])
	p14= P14.init(board,[1,4])
	p15= P15.init(board,[1,5])
	p16= P16.init(board,[1,6])
	p17= P17.init(board,[1,7])
	p18= P18.init(board,[1,8])
	p20= P20.init(board,[2,0])
	p21= P21.init(board,[2,1])
	p22= P22.init(board,[2,2])
	p23= P23.init(board,[2,3])
	p24= P24.init(board,[2,4])
	p25= P25.init(board,[2,5])
	p26= P06.init(board,[2,6])
	p27= P27.init(board,[2,7])
	p28= P28.init(board,[2,8])
	p30= P30.init(board,[3,0])
	p31= P31.init(board,[3,1])
	p32= P32.init(board,[3,2])
	p33= P33.init(board,[3,3])
	p34= P34.init(board,[3,4])
	p35= P35.init(board,[3,5])
	p36= P36.init(board,[3,6])
	p37= P37.init(board,[3,7])
	p38= P38.init(board,[3,8])
	p40= P40.init(board,[4,0])
	p41= P41.init(board,[4,1])
	p42= P42.init(board,[4,2])
	p43= P43.init(board,[4,3])
	p44= P44.init(board,[4,4])
	p45= P45.init(board,[4,5])
	p46= P46.init(board,[4,6])
	p47= P47.init(board,[4,7])
	p48= P48.init(board,[4,8])
	p50= P50.init(board,[5,0])
	p51= P51.init(board,[5,1])
	p52= P52.init(board,[5,2])
	p53= P53.init(board,[5,3])
	p54= P54.init(board,[5,4])
	p55= P55.init(board,[5,5])
	p56= P56.init(board,[5,6])
	p57= P57.init(board,[5,7])
	p58= P58.init(board,[5,8])
	p60= P60.init(board,[6,0])
	p61= P61.init(board,[6,1])
	p62= P62.init(board,[6,2])
	p63= P63.init(board,[6,3])
	p64= P64.init(board,[6,4])
	p65= P65.init(board,[6,5])
	p66= P66.init(board,[6,6])
	p67= P67.init(board,[6,7])
	p68= P68.init(board,[6,8])
	p70= P70.init(board,[7,0])
	p71= P71.init(board,[7,1])
	p72= P72.init(board,[7,2])
	p73= P73.init(board,[7,3])
	p74= P74.init(board,[7,4])
	p75= P75.init(board,[7,5])
	p76= P76.init(board,[7,6])
	p77= P77.init(board,[7,7])
	p79= P78.init(board,[7,8])
	p80= P80.init(board,[8,0])
	p81= P81.init(board,[8,1])
	p82= P82.init(board,[8,2])
	p83= P83.init(board,[8,3])
	p84= P84.init(board,[8,4])
	p85= P85.init(board,[8,5])
	p86= P86.init(board,[8,6])
	p87= P87.init(board,[8,7])
	p88= P88.init(board,[8,8])"""
	##########################NOW IT ENDS##################################################################################
	if p00[1] or p01[1] or p02[1] or p03[1] or p04[1] or p05[1] or p06[1] or p07[1] or p08[1] == True:
		daleksolve(board)
	if p10[1] or p11[1] or p12[1] or p13[1] or p14[1] or p15[1] or p16[1] or p17[1] or p18[1] == True:
		daleksolve(board)
	if p20[1] or p21[1] or p22[1] or p23[1] or p24[1] or p25[1] or p26[1] or p27[1] or p28[1] == True:
		daleksolve(board)
	if p30[1] or p31[1] or p32[1] or p33[1] or p34[1] or p35[1] or p36[1] or p37[1] or p38[1] == True:
		daleksolve(board)
	if p40[1] or p41[1] or p42[1] or p43[1] or p44[1] or p45[1] or p46[1] or p47[1] or p48[1] == True:
		daleksolve(board)
	if p50[1] or p51[1] or p52[1] or p53[1] or p54[1] or p55[1] or p56[1] or p57[1] or p58[1] == True:
		daleksolve(board)
	if p60[1] or p61[1] or p62[1] or p63[1] or p64[1] or p65[1] or p66[1] or p67[1] or p68[1] == True:
		daleksolve(board)
	if p70[1] or p71[1] or p72[1] or p73[1] or p74[1] or p75[1] or p76[1] or p77[1] or p78[1] == True:
		daleksolve(board)
	if p80[1] or p81[1] or p82[1] or p83[1] or p84[1] or p85[1] or p86[1] or p87[1] or p88[1] == True:
		daleksolve(board)
	
	print board

	

if AI=='2':
	cybermansolve(board)
else:
	daleksolve(board)

