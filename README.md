<h1 align="center">⚡ YAPL — Yet Another Programming Language ⚡</h1>

<p align="center">
  <em>Design. Parse. Interpret. Create your own programming language.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/PLY-SLY-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/status-Stable-green?style=for-the-badge" />
</p>

---

<h2>🚀 Overview</h2>

<p>
<strong>YAPL (Yet Another Programming Language)</strong> is a fully functional toy programming language built from scratch using Python’s <code>PLY</code> / <code>SLY</code> libraries.  
It includes a custom <strong>lexer</strong>, <strong>parser</strong>, and <strong>interpreter</strong>, giving you full control over syntax and execution.
</p>

<p>
YAPL supports variables, expressions, control flow, loops, data structures, functions, and recursion — everything needed to write expressive programs from scratch.
</p>

---

<h2>🧠 Features</h2>

<ul>
  <li>📦 <strong>Core Fundamentals</strong>: Static typing, declarations, assignments, expressions, type checking, standard output</li>
  <li>🌀 <strong>Control Flow</strong>: Nested <code>if-elseif-else</code> statements</li>
  <li>🔁 <strong>Loops</strong>: <code>for</code> loops or <code>do-while</code> loops with full nesting support</li>
  <li>📋 <strong>Data Structures</strong>: Lists (push/pop/index/slice) or Structs (custom objects with fields)</li>
  <li>🧩 <strong>Functions & Recursion</strong>: Multi-parameter functions, local scope, return values, recursion</li>
  <li>⚡ <strong>Error Handling</strong>: Redeclaration errors, type errors, division by zero, attribute/index out of bounds, and more</li>
</ul>

---

<h2>📁 Project Structure</h2>

<pre>
├── yapl_lexer.py
├── yapl_parser.py
├── yapl_interpreter.py
├── test_cases/
│   ├── standard_output.txt
│   ├── variables.txt
│   ├── expressions.txt
│   ├── if_else.txt
│   ├── do_while_loops.txt / for_loops.txt
│   ├── lists.txt / structs.txt
│   └── functions_recursion.txt
└── README.md
</pre>

---

<h2>⚙️ How It Works</h2>

<ol>
  <li><strong>Lexer (<code>yapl_lexer.py</code>):</strong> Tokenizes raw source code into meaningful symbols using regex rules.</li>
  <li><strong>Parser (<code>yapl_parser.py</code>):</strong> Converts tokens into a parse tree based on grammar rules.</li>
  <li><strong>Interpreter (<code>yapl_interpreter.py</code>):</strong> Traverses the parse tree and executes your code.</li>
</ol>

---

<h2>🧪 Running Test Programs</h2>

<p>
Add your program to the <code>test_cases</code> folder (for example, <code>variables.txt</code>), then run:
</p>

```bash
python yapl_interpreter.py variables.txt
