@256
D=A
@SP
M=D
// call Sys.init 0
//інструкція 4
@Sys.init.0
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
@Sys.init
0; JMP
(Sys.init.0)

// function Sys.init 0
//інструкція 42
(Sys.init)

// push constant 4000
//інструкція 43
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0
//інструкція 50
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

// push constant 5000
//інструкція 66
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1
//інструкція 73
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

// call Sys.main 0
//інструкція 89
@Sys.main.0
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
@Sys.main
0; JMP
(Sys.main.0)

// pop temp 1
//інструкція 127
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@6
D=A
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// label LOOP
//інструкція 143
(LOOP)

// goto LOOP
//інструкція 144
@LOOP
0;JMP

// function Sys.main 5
//інструкція 146
(Sys.main)
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1

// push constant 4001
//інструкція 172
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0
//інструкція 179
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

// push constant 5001
//інструкція 195
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1
//інструкція 202
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

// push constant 200
//інструкція 218
@200
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 1
//інструкція 225
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@1
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

// push constant 40
//інструкція 243
@40
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 2
//інструкція 250
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@2
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

// push constant 6
//інструкція 268
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 3
//інструкція 275
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@3
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

// push constant 123
//інструкція 293
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Sys.add12 1
//інструкція 300
@Sys.add12.0
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
@Sys.add12
0; JMP
(Sys.add12.0)

// pop temp 0
//інструкція 338
@SP
M=M-1
@SP
A=M
D=M
@R15
M=D
@5
D=A
@R14
M=D
@R15
D=M
@R14
A=M
M=D

// push local 0
//інструкція 354
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

// push local 1
//інструкція 364
@1
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 2
//інструкція 374
@2
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 3
//інструкція 384
@3
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 4
//інструкція 394
@4
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
//інструкція 404
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

// add
//інструкція 414
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

// add
//інструкція 424
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

// add
//інструкція 434
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
//інструкція 444
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
A=M
A=A-1
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

// function Sys.add12 0
//інструкція 503
(Sys.add12)

// push constant 4002
//інструкція 504
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0
//інструкція 511
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

// push constant 5002
//інструкція 527
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1
//інструкція 534
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
//інструкція 550
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

// push constant 12
//інструкція 560
@12
D=A
@SP
A=M
M=D
@SP
M=M+1

// add
//інструкція 567
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
//інструкція 577
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
A=M
A=A-1
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

