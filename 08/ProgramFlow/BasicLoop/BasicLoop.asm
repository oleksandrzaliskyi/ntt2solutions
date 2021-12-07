// push constant 0
//інструкція 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 0
//інструкція 7
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@0
D=A
@LCL
D=M+D
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// label LOOP_START
//інструкція 25
(LOOP_START)

// push argument 0
//інструкція 26
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

// push local 0
//інструкція 36
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
//інструкція 46
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

// pop local 0
//інструкція 56
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@0
D=A
@LCL
D=M+D
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// push argument 0
//інструкція 74
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
//інструкція 84
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub
//інструкція 91
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
//інструкція 101
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

// push argument 0
//інструкція 119
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

// if-goto LOOP_START
//інструкція 129
@SP
M=M-1
A=M
D=M
@LOOP_START
D;JNE

// push local 0
//інструкція 135
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

