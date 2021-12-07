// push constant 17
//інструкція 0
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17
//інструкція 7
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
//інструкція 14
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SETTRUE.0
D;JEQ
(SETFALSE.0)
@SP
A=M
M=0
@ENDBRANCH.0
0;JMP
(SETTRUE.0)
@SP
A=M
M=-1
@ENDBRANCH.0
0;JMP
(ENDBRANCH.0)
@SP
M=M+1

// push constant 17
//інструкція 39
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 16
//інструкція 46
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
//інструкція 53
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SETTRUE.1
D;JEQ
(SETFALSE.1)
@SP
A=M
M=0
@ENDBRANCH.1
0;JMP
(SETTRUE.1)
@SP
A=M
M=-1
@ENDBRANCH.1
0;JMP
(ENDBRANCH.1)
@SP
M=M+1

// push constant 16
//інструкція 78
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17
//інструкція 85
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
//інструкція 92
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SETTRUE.2
D;JEQ
(SETFALSE.2)
@SP
A=M
M=0
@ENDBRANCH.2
0;JMP
(SETTRUE.2)
@SP
A=M
M=-1
@ENDBRANCH.2
0;JMP
(ENDBRANCH.2)
@SP
M=M+1

// push constant 892
//інструкція 117
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891
//інструкція 124
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
//інструкція 131
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SETTRUE.3
D;JLT
(SETFALSE.3)
@SP
A=M
M=0
@ENDBRANCH.3
0;JMP
(SETTRUE.3)
@SP
A=M
M=-1
@ENDBRANCH.3
0;JMP
(ENDBRANCH.3)
@SP
M=M+1

// push constant 891
//інструкція 156
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 892
//інструкція 163
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
//інструкція 170
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SETTRUE.4
D;JLT
(SETFALSE.4)
@SP
A=M
M=0
@ENDBRANCH.4
0;JMP
(SETTRUE.4)
@SP
A=M
M=-1
@ENDBRANCH.4
0;JMP
(ENDBRANCH.4)
@SP
M=M+1

// push constant 891
//інструкція 195
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891
//інструкція 202
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
//інструкція 209
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SETTRUE.5
D;JLT
(SETFALSE.5)
@SP
A=M
M=0
@ENDBRANCH.5
0;JMP
(SETTRUE.5)
@SP
A=M
M=-1
@ENDBRANCH.5
0;JMP
(ENDBRANCH.5)
@SP
M=M+1

// push constant 32767
//інструкція 234
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766
//інструкція 241
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
//інструкція 248
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SETTRUE.6
D;JGT
(SETFALSE.6)
@SP
A=M
M=0
@ENDBRANCH.6
0;JMP
(SETTRUE.6)
@SP
A=M
M=-1
@ENDBRANCH.6
0;JMP
(ENDBRANCH.6)
@SP
M=M+1

// push constant 32766
//інструкція 273
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32767
//інструкція 280
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
//інструкція 287
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SETTRUE.7
D;JGT
(SETFALSE.7)
@SP
A=M
M=0
@ENDBRANCH.7
0;JMP
(SETTRUE.7)
@SP
A=M
M=-1
@ENDBRANCH.7
0;JMP
(ENDBRANCH.7)
@SP
M=M+1

// push constant 32766
//інструкція 312
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766
//інструкція 319
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
//інструкція 326
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SETTRUE.8
D;JGT
(SETFALSE.8)
@SP
A=M
M=0
@ENDBRANCH.8
0;JMP
(SETTRUE.8)
@SP
A=M
M=-1
@ENDBRANCH.8
0;JMP
(ENDBRANCH.8)
@SP
M=M+1

// push constant 57
//інструкція 351
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 31
//інструкція 358
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 53
//інструкція 365
@53
D=A
@SP
A=M
M=D
@SP
M=M+1

// add
//інструкція 372
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M+D
@SP
M=M+1

// push constant 112
//інструкція 382
@112
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub
//інструкція 389
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1

// neg
//інструкція 399
@SP
A=M-1
M=-M

// and
//інструкція 402
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M&D
@SP
M=M+1

// push constant 82
//інструкція 412
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

// or
//інструкція 419
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M|D
@SP
M=M+1

// not
//інструкція 429
@SP
A=M-1
M=!M

