// push constant 111
//інструкція 0
@111
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 333
//інструкція 7
@333
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 888
//інструкція 14
@888
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop static 8
//інструкція 21
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@24
D=A
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// pop static 3
//інструкція 37
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@19
D=A
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// pop static 1
//інструкція 53
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@17
D=A
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// push static 3
//інструкція 69
@19
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1
//інструкція 76
@17
D=M
@SP
A=M
M=D
@SP
M=M+1

// sub
//інструкція 83
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

// push static 8
//інструкція 93
@24
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
//інструкція 100
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

