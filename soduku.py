#!/usr/bin/python2.7 -tt
import sys, pygame,time
from pygame.locals import *

print "Welcome to Soduku. Watch, interact, and admire."

AI= raw_input("What level of intelligence do you want? A fly's brain (1), cyberman (2), or dalek (3). 1, 2, or 3?: ")



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

board= [["2","0",],["0","0"]]


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
		

	
def daleksolve(board):
	def composs(board,pos): #compute possibilities. (board, position (string... "xy" example 10))
		print board
		possnum = ["2","1"]
		currentline= board[int(pos[0])]
		if pos[1]=='0':
			currentrow= [board[0][0],board[1][0]]
		else:
			currentrow= [board[0][1],board[1][1]]
		for numbers in possnum:
			print numbers
			if numbers in currentline:
				possnum.remove(numbers)
			if numbers in str(currentrow):
				try:
					possnum.remove(numbers)
				except:
					pass
		if len(possnum)==1:
			return (possnum, True)
		else:
			return (possnum, False)

		print board

	if board[0][0]=='0':
		l0r0= composs(board,"00")
		if l0r0[1] == True:
			board[0]=(l0r0[0],board[0][1:]) 
			print board
			daleksolve(board)
	else:
		l0r0 = int
	if board[0][1]=='0':
		l0r1 =composs(board,"01")
		if l0r1[1] == True:
			board[0]=(board[0][0],l0r1[0],board[0][2:]) 
			print board
			daleksolve(board)
	else:
		l0r1 = int

	if board[0][2]=='0':
		l0r2= composs(board,"02")
		if l0r2[1] == True:
			board[0]=(board[0][:1],l0r2[0],board[0][3:]) 
			print board
			daleksolve(board)
	else:
		l0r2 = int

	if board[0][3]=='0':
		l0r3= composs(board,"03")
		if l0r3[1] == True:
			board[0]=(board[0][:2],l0r3[0],board[0][4:]) 
			print board
			daleksolve(board)
	else:
		l0r3 = int

	if board[0][4]=='0':
		l0r4= composs(board,"04")
		if l0r4[1] == True:
			board[0]=(board[0][:3],l0r4[0],board[0][5:]) 
			print board
			daleksolve(board)
	else:
		l0r4 = int

	if board[0][5]=='0':
		l0r5= composs(board,"05")
		if l0r5[1] == True:
			board[0]=(board[0][:4],l0r5[0],board[6:]) 
			print board
			daleksolve(board)
	else:
		l0r5 = int

	if board[0][6]=='0':
		l0r6= composs(board,"06")
		if l0r6[1] == True:
			board[0]=(board[0][:5],l0r6[0],board[0][7:]) 
			print board
			daleksolve(board)
	else:
		l0r6 = int

	if board[0][7]=='0':
		l0r7= composs(board,"07")
		if l0r7[1] == True:
			board[0]=(board[0][:6],l0r7[0],board[0][8:]) 
			print board
			daleksolve(board)
	else:
		l0r7 = int

	if board[0][8]=='0':
		l0r8= composs(board,"08")
		if l0r8[1] == True:
			board[0]=(board[0][:7],l0r8[0]) 
			print board
			daleksolve(board)
	else:
		l0r8 = int

	if board[1][0]=='0':
		l1r0= composs(board,"10")
		if l1r0[1] == True:
			board[1]=(l1r0[0],board[1][1:]) 
			print board
			daleksolve(board)
	else:
		l1r0 = int
	if board[1][1]=='0':
		l1r1 =composs(board,"11")
		if l1r1[1] == True:
			board[1]=(board[1][0],l1r1[0],board[1][2:]) 
			print board
			daleksolve(board)
	else:
		l1r1 = int

	if board[1][2]=='0':
		l1r2= composs(board,"12")
		if l1r2[1] == True:
			board[1]=(board[1][:1],l1r2[0],board[1][3:]) 
			print board
			daleksolve(board)
	else:
		l1r2 = int

	if board[1][3]=='0':
		l1r3= composs(board,"13")
		if l1r3[1] == True:
			board[1]=(board[1][:2],l1r3[0],board[1][4:]) 
			print board
			daleksolve(board)
	else:
		l1r3 = int

	if board[1][4]=='0':
		l1r4= composs(board,"14")
		if l1r4[1] == True:
			board[1]=(board[1][:3],l1r4[0],board[1][5:]) 
			print board
			daleksolve(board)
	else:
		l1r4 = int

	if board[1][5]=='0':
		l1r5= composs(board,"15")
		if l1r5[1] == True:
			board[1]=(board[1][:4],l1r5[0],board[1][6:]) 
			print board
			daleksolve(board)
	else:
		l1r5 = int

	if board[1][6]=='0':
		l1r6= composs(board,"16")
		if l1r6[1] == True:
			board[1]=(board[1][:5],l1r6[0],board[1][7:]) 
			print board
			daleksolve(board)
	else:
		l1r6 = int

	if board[1][7]=='0':
		l1r7= composs(board,"17")
		if l1r7[1] == True:
			board[1]=(board[1][:6],l1r7[0],board[1][8:]) 
			print board
			daleksolve(board)
	else:
		l1r7 = int

	if board[1][8]=='0':
		l1r8= composs(board,"18")
		if l1r8[1] == True:
			board[1]=(board[1][:7],l1r8[0]) 
			print board
			daleksolve(board)
	else:
		l1r8 = int

	if board[2][0]=='0':
		l2r0= composs(board,"20")
		if l2r0[1] == True:
			board[2]=(l2r0[0],board[2][1:]) 
			print board
			daleksolve(board)
	else:
		l2r0 = int

	if board[2][1]=='0':
		l2r1 =composs(board,"21")
		if l2r1[1] == True:
			board[2]=(board[2][0],l2r1[0],board[2][2:]) 
			print board
			daleksolve(board)
	else:
		l2r1 = int

	if board[2][2]=='0':
		l2r2= composs(board,"22")
		if l2r2[1] == True:
			board[2]=(board[2][:1],l2r2[0],board[2][3:]) 
			print board
			daleksolve(board)
	else:
		l2r2 = int

	if board[2][3]=='0':
		l2r3= composs(board,"23")
		if l2r3[1] == True:
			board[2]=(board[2][:2],l2r3[0],board[2][4:]) 
			print board
			daleksolve(board)
	else:
		l2r3 = int

	if board[2][4]=='0':
		l2r4= composs(board,"24")
		if l2r4[1] == True:
			board[2]=(board[2][:3],l2r4[0],board[2][5:]) 
			print board
			daleksolve(board)
	else:
		l2r4 = int

	if board[2][5]=='0':
		l2r5= composs(board,"25")
		if l2r5[1] == True:
			board[2]=(board[2][:4],l2r5[0],board[2][6:]) 
			print board
			daleksolve(board)
	else:
		l2r5 = int

	if board[2][6]=='0':
		l2r6= composs(board,"26")
		if l2r6[1] == True:
			board[2]=(board[2][:5],l2r6[0],board[2][7:]) 
			print board
			daleksolve(board)
	else:
		l2r6 = int

	if board[2][7]=='0':
		l2r7= composs(board,"27")
		if l2r7[1] == True:
			board[2]=(board[2][:6],l2r7[0],board[2][8:]) 
			print board
			daleksolve(board)
	else:
		l2r7 = int

	if board[2][8]=='0':
		l2r8= composs(board,"28")
		if l2r8[1] == True:
			board[2]=(board[2][:7],l2r8[2][0]) 
			print board
			daleksolve(board)
	else:
		l2r8 = int

	if board[3][0]=='0':
		l3r0= composs(board,"30")
		if l0r0[1] == True:
			board[3]=(l3r0[0],board[3][1:]) 
			print board
			daleksolve(board)
	else:
		l3r0 = int

	if board[3][1]=='0':
		l3r1 =composs(board,"31")
		if l3r1[1] == True:
			board[3]=(board[3][0],l3r1[0],board[3][2:]) 
			print board
			daleksolve(board)
	else:
		l3r1 = int

	if board[3][2]=='0':
		l3r2= composs(board,"32")
		if l0r2[1] == True:
			board[3]=(board[3][:1],l3r2[0],board[3][3:]) 
			print board
			daleksolve(board)
	else:
		l3r2 = int

	if board[3][3]=='0':
		l3r3= composs(board,"33")
		if l3r3[1] == True:
			board[3]=(board[3][:2],l3r3[0],board[3][4:]) 
			print board
			daleksolve(board)
	else:
		l3r3 = int

	if board[3][4]=='0':
		l3r4= composs(board,"34")
		if l3r4[1] == True:
			board[3]=(board[3][:3],l3r4[0],board[3][5:]) 
			print board
			daleksolve(board)
	else:
		l3r4 = int

	if board[3][5]=='0':
		l3r5= composs(board,"35")
		if l3r5[1] == True:
			board[3]=(board[3][:4],l3r5[0],board[3][6:]) 
			print board
			daleksolve(board)
	else:
		l3r5 = int

	if board[3][6]=='0':
		l3r6= composs(board,"36")
		if l3r6[1] == True:
			board[3]=(board[3][:5],l3r6[0],board[3][7:]) 
			print board
			daleksolve(board)
	else:
		l3r6 = int

	if board[3][7]=='0':
		l3r7= composs(board,"37")
		if l3r7[1] == True:
			board[0]=(board[3][:6],l3r7[0],board[3][8:]) 
			print board
			daleksolve(board)
	else:
		l3r7 = int

	if board[3][8]=='0':
		l3r8= composs(board,"38")
		if l3r8[1] == True:
			board[3]=(board[3][:7],l3r8[0]) 
			print board
			daleksolve(board)
	else:
		l3r8 = int


	if board[1][0]=='0':
		l1r0 =composs(board,"10")
		if l1r0[1] == True:
			print l1r0[1]
			board[1]= (l1r0[0],board[1][0]) 
			print board
			daleksolve(board)
	else:
		l1r0 = int
	if board[1][1]=='0':
		l1r1 =composs(board,"11")
		if l1r1[1] == True:
			board[1]= (board[1][0],l1r1[0])
			print board
			daleksolve(board)
	else:
		l1r1 = int

if AI=='2':
	cybermansolve(board)
else:
	daleksolve(board)

