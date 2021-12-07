@256
D=A
@SP
M=D
@Sys.init
0;JMP
// function Sys.init 0
//інструкція 6
(Sys.init)

// push constant 4
//інструкція 7
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Main.fibonacci 1
//інструкція 14
@Main.fibonacci.0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@Main.fibonacci
0; JMP
(Main.fibonacci.0)

// label WHILE
//інструкція 52
(WHILE)

// goto WHILE
//інструкція 53
@WHILE
0;JMP

// function Main.fibonacci 0
//інструкція 55
(Main.fibonacci)

// push argument 0
//інструкція 56
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 2
//інструкція 66
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
//інструкція 73
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SETTRUE.0
D;JLT
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

// if-goto IF_TRUE
//інструкція 98
@SP
M=M-1
A=M
D=M
@IF_TRUE
D;JNE

// goto IF_FALSE
//інструкція 104
@IF_FALSE
0;JMP

// label IF_TRUE
//інструкція 106
(IF_TRUE)

// push argument 0
//інструкція 107
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// return
//інструкція 117
@LCL
A=M
D=A
@FRAME
M=D
@FRAME
A=M
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@RET
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@FRAME
A=M
A=A-1
D=M
@THAT
M=D
@FRAME
A=M
A=A-1
A=A-1
D=M
@THIS
M=D
@FRAME
A=M
A=A-1
A=A-1
A=A-1
D=M
@ARG
M=D
@FRAME
A=M
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@LCL
M=D
@RET
A=M
0; JMP

// label IF_FALSE
//інструкція 175
(IF_FALSE)

// push argument 0
//інструкція 176
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 2
//інструкція 186
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub
//інструкція 193
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

// call Main.fibonacci 1
//інструкція 203
@Main.fibonacci.0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@Main.fibonacci
0; JMP
(Main.fibonacci.0)

// push argument 0
//інструкція 241
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 1
//інструкція 251
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub
//інструкція 258
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

// call Main.fibonacci 1
//інструкція 268
@Main.fibonacci.0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@Main.fibonacci
0; JMP
(Main.fibonacci.0)

// add
//інструкція 306
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

// return
//інструкція 316
@LCL
A=M
D=A
@FRAME
M=D
@FRAME
A=M
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@RET
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@FRAME
A=M
A=A-1
D=M
@THAT
M=D
@FRAME
A=M
A=A-1
A=A-1
D=M
@THIS
M=D
@FRAME
A=M
A=A-1
A=A-1
A=A-1
D=M
@ARG
M=D
@FRAME
A=M
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@LCL
M=D
@RET
A=M
0; JMP

