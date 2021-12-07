// push argument 1
//інструкція 0
@1
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1
//інструкція 10
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@4
D=A
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// push constant 0
//інструкція 26
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop that 0
//інструкція 33
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@0
D=A
@THAT
D=M+D
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// push constant 1
//інструкція 51
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop that 1
//інструкція 58
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@1
D=A
@THAT
D=M+D
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// push argument 0
//інструкція 76
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
//інструкція 86
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub
//інструкція 93
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

// pop argument 0
//інструкція 103
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@0
D=A
@ARG
D=M+D
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// label MAIN_LOOP_START
//інструкція 121
(MAIN_LOOP_START)

// push argument 0
//інструкція 122
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

// if-goto COMPUTE_ELEMENT
//інструкція 132
@SP
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JNE

// goto END_PROGRAM
//інструкція 138
@END_PROGRAM
0;JMP

// label COMPUTE_ELEMENT
//інструкція 140
(COMPUTE_ELEMENT)

// push that 0
//інструкція 141
@0
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push that 1
//інструкція 151
@1
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
//інструкція 161
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

// pop that 2
//інструкція 171
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@2
D=A
@THAT
D=M+D
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// push pointer 1
//інструкція 189
@4
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 1
//інструкція 196
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// add
//інструкція 203
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

// pop pointer 1
//інструкція 213
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@4
D=A
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// push argument 0
//інструкція 229
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
//інструкція 239
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub
//інструкція 246
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

// pop argument 0
//інструкція 256
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@0
D=A
@ARG
D=M+D
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// goto MAIN_LOOP_START
//інструкція 274
@MAIN_LOOP_START
0;JMP

// label END_PROGRAM
//інструкція 276
(END_PROGRAM)

