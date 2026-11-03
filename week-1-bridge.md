---
title: 'Week 1 Concepts Bridge: How Code Runs'
teaching: 20
exercises: 10
---

:::::::::::::::::::::::::::::::::::::: questions

- How does the code I type become something a computer can run?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Explain the difference between machine code, assembly, compilers and interpreters.
- Compare Hello World in Python with other languages.

::::::::::::::::::::::::::::::::::::::::::::::::

**Time:** about 30 minutes (15 min reading, 5 min trying the code, 10 min activity).

## Why this matters

Before you write much code, it helps to know how the code you type becomes something a computer can run: machine code, assembly language, compilers and interpreters. Comparing "Hello World" in several languages helps you analyse a problem and its solution (LO 1). It also sets you up for LO 4, where you judge which language or paradigm suits a problem. It builds on video **T#67**, which you have already watched in the Watch block. You do not need to watch it again.

## The big idea: a computer only understands machine code

A computer chip can only follow very simple instructions, such as "add these two numbers" or "move this value". Each instruction is a pattern of 1s and 0s. This is called **machine code**.

Nobody wants to write patterns of 1s and 0s. So people invented layers that make code easier to write.

| Layer | What it looks like | Who writes it |
|---|---|---|
| Machine code | `10110000 01100001` | Almost nobody |
| **Assembly language** | `mov al, 97` | Specialists, for very small or very fast code |
| **High-level language** (C, Java, Python) | `print("Hello")` | Almost everyone |

**Assembly language** is machine code with short names instead of numbers. One assembly line is about one machine instruction. A program called an **assembler** turns it into machine code.

A **high-level language** reads more like English. One line can become many machine instructions. Something must translate it. There are two main ways.

## Compilers and interpreters

A **compiler** translates the whole program into machine code *before* it runs. You get a separate file that the computer runs directly. C works this way. Compiled programs usually run fast. A mistake in the code is often caught before the program starts.

An **interpreter** reads your program and carries it out *while it runs*, one step at a time. You do not make a separate machine-code file first. This makes testing quick, because you change a line and run it again.

Think of a speech in another language. A compiler is like translating the whole speech into a written copy first. An interpreter is like a person translating live, sentence by sentence.

## Where Python sits

Python is usually called an interpreted language, but the real story has two steps:

1. Python first **compiles** your code into **bytecode**. Bytecode is a simple set of instructions for Python itself, not for your computer chip.
2. The **Python virtual machine** (PVM), which is part of the interpreter, then runs the bytecode one instruction at a time.

Java is similar. It compiles to bytecode, and the Java Virtual Machine runs it. Python does the compile step for you, automatically, each time you run a file. That is why T#67 says the answer is "both".

You can see Python's bytecode with the built-in `dis` module (short for "disassemble"). Save this as a file and run it.

> **Just copy and run this.** You have not learned `def` or `import` yet. You will learn `def` (making your own functions) in Week 3 and `import` (using other code) in Week 6. For now, only look at the output.

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

The exact lines depend on your Python version. You will see names such as `LOAD_FAST` (fetch a value) and `BINARY_OP` (do the maths) and `RETURN_VALUE`. Those are bytecode instructions. You wrote one short line. Python turned it into several steps.

Here is a second small check. Python's `compile()` function does the compile step by hand. Again, just copy and run it. `compile()` and `exec()` are not part of this week's lessons.

```python
code = compile("print('Hello, World!')", "<example>", "exec")
print(type(code))
exec(code)
```

`compile()` returns a **code object** (the bytecode and its details). `exec()` then runs it. This is what Python does for every file you run.

## Hello World in four languages

The same job, printing one line, looks very different in each language.

**C** (compiled to machine code, then run):

```c
#include <stdio.h>

int main(void) {
    printf("Hello, World!\n");
    return 0;
}
```

**Java** (compiled to bytecode, run by the Java Virtual Machine):

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

**Assembly** (x86-64 for Linux, NASM assembler). You do not need to understand it. Notice how many instructions it takes:

```nasm
section .data
    msg db "Hello, World!", 10
    len equ $ - msg

section .text
    global _start

_start:
    mov rax, 1        ; system call number for "write"
    mov rdi, 1        ; 1 means "standard output" (the screen)
    mov rsi, msg      ; the address of the text
    mov rdx, len      ; how many characters to write
    syscall           ; ask the operating system to do it
    mov rax, 60       ; system call number for "exit"
    xor rdi, rdi      ; exit code 0
    syscall
```

**Python** (compiled to bytecode, run by the interpreter):

```python
print("Hello, World!")
```

One line. No `main`, no semicolons, no types, no set-up. That is why Python suits beginners. The trade-off is speed: Python is usually slower than C, because of the extra interpreting step.

## Video

You have already watched this in the Watch block. Rewatch it only if the ideas above feel new.

- **T#67** Is Python Compiled or Interpreted? (6:48): https://www.youtube.com/watch?v=0BhSWyDEDC4&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3

## Activity (10 minutes)

1. Run the three Python code blocks above in PyCharm. Use a new file for each.
2. Fill in this table in your own notes. Count lines of code for "Hello World" (blank lines do not count) and say how each language is run.

| Language | Lines | Compiled, interpreted or both? |
|---|---|---|
| C | | |
| Java | | |
| Assembly | | |
| Python | | |

3. In two or three sentences, answer: *why would someone still choose C or assembly when Python is so short?*

Keep your answers. You will use them in the practice task.

### Model answer

| Language | Lines | Compiled, interpreted or both? |
|---|---|---|
| C | 5 | Compiled to machine code |
| Java | 5 | Compiled to bytecode, then run by the JVM |
| Assembly | 14 (with the data and text sections) | Assembled to machine code |
| Python | 1 | Both: compiled to bytecode, then interpreted |

Exact counts change a little with how you write each program. A fair answer is: C and assembly give you close control of the hardware and run very fast, and their programs are small and need no interpreter. That matters for operating systems, device software and games. Python trades that speed for being quick to write and easy to read.

## Further reading

- Driscoll, M. (2017) *Python 101*. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (Introduction).
- Romano, F. (2018) *Learn Python Programming*, 2nd edn. Birmingham: Packt. Chapter 1, on how Python code is run.
- Python Software Foundation (2024) *dis: Disassembler for Python bytecode*. Available at: https://docs.python.org/3/library/dis.html (Accessed: 2 November 2026).

:::::::::::::::::::::::::::::::::::::: keypoints

- Computers only run machine code.
- Compilers translate a whole program first; interpreters run it step by step.
- Python compiles to bytecode, then the interpreter runs it.

::::::::::::::::::::::::::::::::::::::::::::::::
