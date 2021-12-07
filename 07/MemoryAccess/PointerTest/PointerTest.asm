// push constant 3030
//інструкція 0
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0
//інструкція 7
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@3
D=A
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// push constant 3040
//інструкція 23
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1
//інструкція 30
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

// push constant 32
//інструкція 46
@32
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop this 2
//інструкція 53
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@2
D=A
@THIS
D=M+D
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// push constant 46
//інструкція 71
@46
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop that 6
//інструкція 78
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@6
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

// push pointer 0
//інструкція 96
@3
D=M
@SP
A=M
M=D
@SP
M=M+1

// push pointer 1
//інструкція 103
@4
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
//інструкція 110
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

// push this 2
//інструкція 120
@2
D=A
@THIS
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// sub
//інструкція 130
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

// push that 6
//інструкція 140
@6
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
//інструкція 150
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

