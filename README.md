Here is a `README.md` file for your GitHub repository. It is structured to be a comprehensive learning journal for the FTL Syria Programme, incorporating all the details from the provided files and your specific requests.

You can copy and paste this directly into a `README.md` file in your new repository.

---

# My FTL Syria Programme Journey: AI for Climate

Welcome to my learning journal for the **Frontier Tech Leaders (FTL) Syria Programme – AI for Climate**!

This repository documents my progress, key takeaways, and projects throughout this 3.5-month intensive program running from September to December 2026. The program is a unique collaboration between the UNDP, the UNDP Istanbul International Center for Private Sector in Development (ICPSD), and Damascus University, supported by the German Federal Ministry for Economic Cooperation and Development (BMZ) through KfW.

The goal is to build a new generation of tech leaders by connecting technical skills in AI, Python, and data science to real-world challenges in climate, energy, and the environment.

---

## 👨‍💻 About Me

I'm Ahmad Deeb, a passionate learner on a mission to leverage technology for sustainable development.

- **GitHub:** [@AhmedGDeeb](https://github.com/AhmedGDeeb)
- **LinkedIn:** [Ahmad Deeb](https://www.linkedin.com/in/ahmad-deeb-13699b39a/)

---

## 🗓️ Programme Schedule & Progress

The program is structured into several key phases. I will update this section as we progress.

| Phase / Module | Status | Key Topics |
| :--- | :---: | :--- |
| **Python Bootcamp** | 🔄 **In Progress** | Python syntax, Data Types, Variables, Operators, Control Flow, Functions |
| **Python Hackathon** | ⏳ Not Started | Group-based problem solving and presentation |
| **Data Analysis & SDG** | ⏳ Not Started | Data manipulation, analysis techniques, peer coding |
| **Applied Machine Learning** | ⏳ Not Started | Regression, Classification, Clustering, Model Development |
| **Applied Dev & Deployment** | ⏳ Not Started | Git, GitHub, Command Line, Docker, APIs, Model Integration |
| **Specialized Sessions** | ⏳ Not Started | Cybersecurity, AI Security, AI for Climate, Smart Grids |
| **Capstone Project** | ⏳ Not Started | Literature review, Problem statement, Model development, Final Presentation |
| **Professional Certifications**| ⏳ Not Started | Power Systems, Wireless Networking, IoT, Climate Monitoring |

**Key Programme Timelines:**
- **Program Duration:** September - December 2026
- **Python Hackathon:** September 28 - October 2, 2026
- **Capstone Final Presentation:** December 22-23, 2026

---

## 📚 Session Notes & Key Learnings

This section is my personal knowledge base. I'll add key takeaways from each session here. All code and exercises will be in my main [Colab Notebook](https://colab.research.google.com/drive/1Tu9UNohVNN8d0dFyCV62qMhIZZi32Xyy?usp=sharing).

---

### Day 1: Welcome & Python Intro (Sep 14, 2026)

**Key Takeaways:**

- **Welcome & Program Overview:** The session introduced the FTL Syria Programme, its mission to apply frontier technologies like AI to climate challenges, and its structure over the next three months.
- **Program Logistics:** We learned about the timeline, the 70% minimum attendance requirement, access to a Coursera license, and the importance of the final Capstone project.
- **Python Bootcamp Launch:** The Python bootcamp will consist of eight sessions over two weeks, designed to build a foundation for the more advanced machine learning modules.
- **Tools Introduction:** The primary tools for the program are **Google Colab** for coding and **GitHub** for version control and sharing projects.
- **Python Fundamentals:** We kicked off the technical part by learning the absolute basics of Python:
    - **Variables:** Names that refer to objects in memory.
    - **Data Types:** Introduction to `int`, `float`, `string`, `list`, `dict`, and `boolean`.
    - **Dynamic Typing:** Python automatically determines the type of a variable at runtime.
    - **Expressions and Operators:** Combining values and variables with arithmetic (`+`, `-`, `*`, `/`) and assignment (`=`) operators.

- **My Code & Exercises:** [Link to my Day 1 Notebook](https://colab.research.google.com/drive/1Tu9UNohVNN8d0dFyCV62qMhIZZi32Xyy?usp=sharing)

---

### Day 2: Session 1 — Functions, Lambda & Control Flow (Sep 15, 2026)

**Key Takeaways:**

- **Review of Day 1:** We quickly recapped variables, data types, and basic operators.
- **Control Flow:** The main topic was controlling the flow of a program.
    - **Conditional Statements:** Using `if`, `elif`, and `else` to execute code based on certain conditions.
    - **Comparison Operators:** Using `==`, `!=`, `>`, `<`, `>=`, `<=` to compare values.
    - **Logical Operators:** Using `and`, `or`, and `not` to combine multiple conditions.
- **Functions — Basics:**
    - **Definition:** A function is a reusable block of code that performs a specific task.
    - **Syntax:** Defined using `def function_name(parameters):` followed by an indented block.
    - **Return Values:** Functions can return values using the `return` keyword; if no `return` is used, the function returns `None`.
    - **Parameters vs. Arguments:** Parameters are the placeholders in the function definition; arguments are the actual values passed when calling the function.
    - **Scope:** Variables defined inside a function are local to that function and cannot be accessed outside it.
- **Lambda Functions:**
    - **Definition:** A lambda function is a small, anonymous function defined with the `lambda` keyword.
    - **Syntax:** `lambda arguments: expression`
    - **When to Use:** Best for short, one-line operations where a full `def` function would be overkill.
    - **Example:** `square = lambda x: x ** 2`
    - **Common Use Cases:** Passing a function as an argument (e.g., to `map()`, `filter()`, `sorted()`), inline calculations.
- **Practice:** We wrote small functions and lambda expressions to solve simple problems (e.g., unit conversions, basic calculations).
- **My Code & Exercises:** [Link to my Day 2 Notebook](https://colab.research.google.com/drive/1Tu9UNohVNN8d0dFyCV62qMhIZZi32Xyy?usp=sharing)

---

### Day 3: Session 2 — Strings & Files (Sep 16, 2026)

**Key Takeaways:**

- **Exercise Review & Peer Feedback:** We reviewed our previous exercise (the BMI calculator and treasure-hunt game). I presented my **function-oriented BMI calculator** (with unit conversions, health categories, and CLI interaction) and a **randomly generated treasure-and-trap grid game** (with boundary checks and user attempts). The facilitator asked me to share my solution with the group for peer review and comments. The key lesson: combine the best elements from different approaches.

- **Python Strings — Representation & Core Operations:**
    - **Definition:** A string is a **sequence of characters** enclosed in single, double, or triple quotes.
    - **No Separate Character Type:** In Python, there is no `char` type — a single character is just a string of length 1.
    - **Immutability:** Strings cannot be changed in place; operations create new strings. Demonstrated with `id()` — the memory address changes after concatenation.
    - **Indexing:** Each character has an index starting from `0` (zero-based); negative indices count from the end (`-1` = last character).
    - **Concatenation:** Combine strings with `+`.
    - **Repetition:** Repeat strings with `*`.
    - **Length:** Use `len()` to count characters.

- **String Indexing & Slicing:**
    - **Indexing:** Access individual characters with `string[index]`.
    - **Slicing:** Extract a range with `string[start:stop:step]`. The **stop index is exclusive** (not included). Defaults: start=`0`, stop=end, step=`1`.
    - **Negative Indexing:** Access from the end (`-1` = last character).
    - **Example:** `"Monty Python"[0:4]` returns `"Mont"`; `"frontier"[0:4]` returns `"fron"`.

- **String Methods & Object Inspection:**
    - **Common Methods:** `.upper()`, `.lower()`, `.replace()`, `.split()`, `.find()`, `.startswith()`, `.endswith()`, `.join()`.
    - **`dir()`:** Lists all available methods for an object — a great way to explore (e.g., `dir('Lamacun')`).
    - **`type()`:** Confirms the data type (e.g., `type(s)` returns `str`).
    - **Parsing Example:** Extracting the username from an email using `.find("@")` and slicing: `email[0:findex]` returns `"john.doe"`.

- **String Comparisons & Boolean Checks:**
    - **Equality:** `==` and `!=` compare strings (e.g., `'Helo' == 'Hello'` returns `False`).
    - **Prefix/Suffix:** `.startswith()` and `.endswith()` return `True`/`False`.
    - **Use Case:** Filtering or validating text data.

- **Loop-Based Vowel Counting:**
    - **Approach:** Normalize to lowercase, iterate through each character, increment a counter when a vowel is found.
    - **Two Implementations:** One with a `while` loop (`count_vowels_while`), one with a `for` loop (`count_vowels_for`) — same logic, different syntax.

- **Type Annotations (Optional but Good Practice):**
    - Python is **dynamically typed**, so annotations are not required.
    - **Why Use Them:** Document expected types, support error handling, improve readability.
    - **Example:** `def count_vowels(text: str) -> int:`

- **Palindrome Exercise:**
    - **Definition:** A word, phrase, or number that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
    - **Approach:** Clean the input with `''.join(c for c in input_string if c.isalnum()).lower()`, then use `left` and `right` indices to compare characters from opposite ends, moving inward.
    - **Two Versions:** One using a `while` loop (`is_palindrome_while`), one using a `for` loop (`is_palindrome_for`).
    - **Example:** `"A man, a plan, a canal, Panama"` is a palindrome.

- **Python File Concepts & Opening Files:**
    - **Why Files Matter:** Data comes from different sources — we need to read, write, and append. Console input uses primary memory (RAM); files use secondary memory.
    - **Built-in `open()` Function:** `open(filepath, mode)` returns a **file handle** (`_io.TextIOWrapper`) providing methods to interact with the file.
    - **File Modes:**
        - `"r"` — Read (default)
        - `"w"` — Write (creates file, **replaces** existing content)
        - `"a"` — Append (adds to the end, **preserves** existing content)
        - `"b"` — Binary mode (for images, executables)
    - **Colab Note:** Mount Google Drive with `from google.colab import drive; drive.mount('/content/drive')` to access files.

- **Reading Files:**
    - **`.read()`** — Reads the entire file as a single string.
    - **`.readline()`** — Reads one line (the first line).
    - **`.readlines()`** — Reads all lines into a list.
    - **Looping:** Use a `for` loop with `enumerate()` to read specific lines or process line-by-line with numbering.

- **Writing & Appending Files:**
    - **Write Mode (`"w"`):** Replaces existing content; creates a new empty file if it doesn't exist.
    - **Append Mode (`"a"`):** Adds new content at the end without erasing; creates a new file if it doesn't exist.
    - **Best Practice:** Use the `with` statement — it automatically closes the file when the block completes, so no explicit `.close()` is needed.

- **Listing Files in a Directory:**
    - Use `os.listdir(basepath)` to iterate over every item (files, directories).
    - Use `os.path.isfile(os.path.join(basepath, entry))` to check if a path points to a regular file.

- **Error Handling for File Operations:**
    - **Problem:** `FileNotFoundError` when the path or filename is incorrect.
    - **Solution:** Use `try`/`except` to catch errors and provide a helpful message.
    - **Example:**
      ```python
      try:
          fhand = open(filept, "r")
          content = fhand.read()
          print(content)
      except:
          print('File Not found check again: ', filept)
          quit()
      ```

- **My Code & Exercises:** [Link to my Day 3 Notebook](https://colab.research.google.com/drive/1Tu9UNohVNN8d0dFyCV62qMhIZZi32Xyy?usp=sharing)

---

### Day 4: Session 3 — Data Structures (Sep 17, 2026)

*(This section will be filled out after the session)*

- **Key Takeaways:**
    - ...

---


## 🎓 Capstone Project: [Project Title Placeholder]

This section is dedicated to my final Capstone project, a requirement for graduation. The project must connect AI and climate and follow a structured development process.

- **Project Idea:** _To be decided._
- **Literature Review:** _To be completed._
- **Problem Statement:** _To be defined._
- **Methodology & Models:** _To be developed._
- **Final Deliverable:** _A working prototype/analysis and a final presentation scheduled for December 22-23, 2026._

---

## 🙏 Acknowledgements

A huge thank you to the entire team and all the organizers for making this incredible learning opportunity possible.

- **[Cristóvăo Cacombe]()** (UNDP Course Guide) for his excellent instruction and guidance.
- The **UNDP**, the **SDG AI Lab**, and **Damascus University** for creating and delivering this comprehensive program.
- The **German Federal Ministry for Economic Cooperation and Development (BMZ)** and **KfW** for their generous support.
- My fellow participants for the collaboration and shared learning journey.

Special thanks to the **FTL Team** for their continuous support and coordination. This program is a life-changing opportunity, and I am committed to making the most of it.