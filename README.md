# Lab Programs

A collection of programming lab exercises, assignments, and notes. The repository is primarily focused on C, with additional practice in Python, SQL/PL-SQL, Go, R, and data structures.

## Contents

- [C Programs](#c-programs)
- [Data Structures in C](#data-structures-in-c)
- [C++](#c)
- [DBMS and SQL](#dbms-and-sql)
- [Python](#python)
- [Go](#go)
- [R](#r)
- [Repository layout](#repository-layout)
- [Running the programs](#running-the-programs)

## C Programs

The [`C-Programs`](./C-Programs) directory contains introductory programs, lab questions, process scheduling, functions, and queue/stack implementations.

- [`Info.md`](./C-Programs/Info.md) contains array problem solutions and notes.
- [`LabQues.txt`](./C-Programs/LabQues.txt), [`lab5.md`](./C-Programs/lab5.md), and [`lab6.md`](./C-Programs/lab6.md) contain lab questions and exercises.
- [`DSA`](./C-Programs/DSA) contains linked lists, stacks, queues, and the array assignment.

The standalone [`DecimalToBinary.c`](./DecimalToBinary.c) program converts a decimal integer to binary.

## Data Structures in C

The [`DS`](./DS) directory contains separate implementations and notes for:

- Stack operations: [`StackOps.c`](./DS/StackOps.c)
- Graphs, including adjacency-list operations and traversal notes: [`DS/Graph`](./DS/Graph)
- Trees, including binary tree and binary search tree programs: [`DS/Trees`](./DS/Trees)

## C++

The [`CPP`](./CPP) directory is reserved for C++ work. It currently contains [`Info.md`](./CPP/Info.md), which is empty and available for future notes or programs.

## DBMS and SQL

The [`DBMS`](./DBMS) directory contains Oracle SQL and PL/SQL lab work, query notes, and database setup material.

- Query scripts: [`BasicQueries.sql`](./DBMS/BasicQueries.sql), [`LabQueries.sql`](./DBMS/LabQueries.sql), [`Subqueries.sql`](./DBMS/Subqueries.sql), and [`Termwork3.sql`](./DBMS/Termwork3.sql)
- Topic notes: [`Joins.md`](./DBMS/Joins.md), [`Subqueries.md`](./DBMS/Subqueries.md), [`UNION.md`](./DBMS/UNION.md), and [`PL/SQL.md`](./DBMS/PL/SQL.md)
- Supporting material: [`Queries.txt`](./DBMS/Queries.txt), [`Termwork3.txt`](./DBMS/Termwork3.txt), [`Info.md`](./DBMS/Info.md), and [`Dockerfile`](./DBMS/Dockerfile)

See [`DBMS/Info.md`](./DBMS/Info.md) for the Oracle Database and SQL*Plus/SQL Developer prerequisites.

## Python

The [`Python`](./Python) directory contains general lab solutions, notebooks, file handling, object-oriented programming, and introductory AI/problem-solving exercises.

- General exercises: [`AllProgram.py`](./Python/AllProgram.py), [`Sol1.py`](./Python/Sol1.py) through [`Sol4.py`](./Python/Sol4.py), and [`Qlab3.md`](./Python/Qlab3.md)
- OOP practice: [`Python/OOPs`](./Python/OOPs)
- AI and algorithms: [`Python/AI-Lab(Noob)`](./Python/AI-Lab%28Noob%29)
- File handling and lab notebooks: [`Python/File-Handling`](./Python/File-Handling) and [`lab3.ipynb`](./Python/lab3.ipynb)

## Go

The [`GO-Lang`](./GO-Lang) directory contains Go syntax examples, a hello-world program, and a stack implementation:
[`All-syntax.go`](./GO-Lang/All-syntax.go), [`hello.go`](./GO-Lang/hello.go), and [`Stack.go`](./GO-Lang/Stack.go).

## R

The [`R`](./R) directory contains syntax and examples for vectors, lists, and basic R operations:
[`AllSyntaxStuff.r`](./R/AllSyntaxStuff.r), [`Vectors.r`](./R/Vectors.r), and [`list.r`](./R/list.r).

## Repository layout

```text
.
├── C-Programs/       C labs, assignments, and basic DSA
├── CPP/              C++ notes and future programs
├── DBMS/             Oracle SQL and PL/SQL queries and notes
├── DS/               Graph, tree, and stack implementations in C
├── GO-Lang/          Go examples
├── Python/           Python labs, notebooks, OOP, and AI exercises
├── R/                R examples
├── DecimalToBinary.c Standalone C program
├── LICENSE
└── notes.txt
```

## Running the programs

Clone the repository:

```bash
git clone https://github.com/Ayush41/Lab-Pograms.git
cd Lab-Pograms
```

Compile and run a C program with GCC:

```bash
gcc DecimalToBinary.c -o decimal-to-binary
./decimal-to-binary
```

Run a Python script with Python 3:

```bash
python3 Python/Sol1.py
```

Open `.ipynb` files with Jupyter Notebook or JupyterLab. Execute `.sql` files with an Oracle SQL client after configuring an Oracle database.

## License

This project is distributed under the [GNU General Public License v3.0](./LICENSE).
