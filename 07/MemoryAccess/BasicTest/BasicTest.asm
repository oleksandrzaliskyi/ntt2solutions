// push constant 10
//інструкція 0
@10
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

// push constant 21
//інструкція 25
@21
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 22
//інструкція 32
@22
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop argument 2
//інструкція 39
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@2
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

// pop argument 1
//інструкція 57
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@1
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

// push constant 36
//інструкція 75
@36
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop this 6
//інструкція 82
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@6
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

// push constant 42
//інструкція 100
@42
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 45
//інструкція 107
@45
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop that 5
//інструкція 114
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@5
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

// pop that 2
//інструкція 132
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

// push constant 510
//інструкція 150
@510
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop temp 6
//інструкція 157
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@11
D=A
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// push local 0
//інструкція 173
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

// push that 5
//інструкція 183
@5
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
//інструкція 193
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

// push argument 1
//інструкція 203
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

// sub
//інструкція 213
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

// push this 6
//інструкція 223
@6
D=A
@THIS
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push this 6
//інструкція 233
@6
D=A
@THIS
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
//інструкція 243
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

// sub
//інструкція 253
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

// push temp 6
//інструкція 263
@11
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
//інструкція 270
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

