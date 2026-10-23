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
| **Python Bootcamp** | ✅ **Done** | Python syntax, Data Types, Variables, Operators, Control Flow, Functions |
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

Of course. Here is the revised summary of your FTL Syria Programme journey, based on the information you provided.

I have condensed the existing daily entries into more concise key takeaways and added summaries for the coding session files, which I've assumed are from the `1 - Applied Python for Engineering & Climate Systems` module. The daily entries are now titled by topic rather than a specific date to create a more unified learning log.

***

## 📚 Session Notes & Key Learnings

This section is my personal knowledge base, summarizing the key takeaways from each session. All code and exercises are available in my main [Colab Notebook](https://colab.research.google.com/github/AhmedGDeeb/FTL/blob/main/tasks/FTL_Tasks_ahmad_deeb.ipynb).

---

### Python Bootcamp

#### Day 1: Welcome & Python Fundamentals
*Session: "Welcome & Python Intro"*

- **Program Overview:** The FTL Syria Programme, a collaboration between UNDP, Damascus University, and BMZ/KfW, aims to build tech leaders skilled in applying AI to climate challenges. Key logistics include a 70% attendance requirement, a Coursera license, and a final Capstone project.
- **Core Tools:** The program introduced **Google Colab** for coding and **GitHub** for version control and project sharing.
- **Python Basics:** We covered the absolute fundamentals: **Variables** (names for objects in memory), basic **Data Types** (`int`, `float`, `string`, `list`, `dict`, `boolean`), and **Dynamic Typing** (Python determines a variable's type at runtime). We also practiced using arithmetic and assignment **operators**.

---

#### Day 2: Control Flow, Functions & Lambda
*Session: "Functions, Lambda & Control Flow"*

- **Control Flow:** Learned to direct program execution using conditional statements (`if`, `elif`, `else`), comparison operators (`==`, `!=`, `>`), and logical operators (`and`, `or`, `not`).
- **Functions:** Explored reusable code blocks defined with `def`. Key concepts included the difference between **parameters** (placeholders) and **arguments** (actual values), using `return` to output values, and variable **scope** (local vs. global).
- **Lambda Functions:** Introduced small, anonymous functions (`lambda arguments: expression`) for concise, one-line operations, especially useful when passing a function as an argument to another function like `map()` or `filter()`.

---

#### Day 3: Strings & File I/O
*Session: "Strings & Files"*

- **String Manipulation:** We analyzed strings as immutable **sequences of characters**. Key operations included **indexing** (accessing a single character) and **slicing** (`[start:stop:step]`), along with common methods like `.upper()`, `.split()`, and `.join()`.
- **File Operations:** Learned to read from and write to files using the built-in `open()` function. We covered different **file modes** (`'r'` for read, `'w'` for write, `'a'` for append) and practiced the best practice of using the `with` statement for automatic file closing.
- **Error Handling:** Implemented `try`/`except` blocks to gracefully handle common file errors, such as `FileNotFoundError`.

---

#### Day 4: Core Data Structures
*Session: "Data Structures"*

- **Lists:** Explored ordered, mutable, and heterogeneous collections. Learned to use key methods like `.append()` and `.sort()`, as well as list operations like concatenation (`+`) and slicing.
- **Dictionaries:** Covered collections of **key:value** pairs with unique keys. We practiced adding, modifying, and deleting items, as well as iterating through keys, values, and items (`.items()`, `.keys()`, `.values()`).
- **Tuples:** Introduced ordered, **immutable** collections, highlighting their use for storing data that shouldn't change and their efficiency. We also noted their common use as return values for functions.

---

#### Day 5: Intro to Object-Oriented Programming (OOP)
*Session: "Scientific Data / Intro to OOP"*

- **OOP Principles:** Introduced OOP as a paradigm to organize code and prevent repetition. Key terminology: **Class** (a blueprint), **Object** (an instance of a class), **Attribute** (a variable in a class), and **Method** (a function in a class).
- **Creating Classes:** Learned to define a custom class with a constructor (`__init__`) and the **`self`** parameter, which refers to the instance being created. We learned how to define instance attributes and methods.
- **Class Attributes vs. Instance Attributes:** Distinguished between attributes that belong to each individual object (e.g., a dog's name) and attributes that are shared across all objects of a class (e.g., `species = "canine"`).

---

#### Day 6: OOP Continued, Regex & Web Scraping
*Session: "OOP, Regex & Web Scraping"*

- **Advanced OOP:** We covered **Inheritance** (a child class extending a parent class), **Encapsulation** (restricting direct access to data using `_` or `__` conventions), and **Abstraction** (hiding complexity via abstract base classes using the `abc` module).
- **Regular Expressions (Regex):** Used the `re` module for advanced pattern matching. Learned key functions like `re.search()` (finds the first match) and `re.findall()` (finds all matches) and common pattern symbols (`^`, `$`, `*`, `+`, `\d`, `\w`).
- **Web Scraping:** Introduced the fundamentals of making HTTP requests with the `requests` library (e.g., `GET`) and parsing HTML content with **Beautiful Soup** to extract data from websites.

---

#### Day 7: Databases & SQL
*Session: "Intro to Databases, SQL & SQLite"*

- **Database Concepts:** Learned the purpose of **databases** (structured data storage) and **relational databases**, which use tables of rows (records) and columns (fields). The language for interacting with these is **SQL (Structured Query Language)**.
- **Basic SQL Commands:** We practiced fundamental operations: `SELECT` (retrieve data), `INSERT` (add data), `UPDATE` (modify data), and `DELETE` (remove data).
- **Practical Application:** Used **SQLite**, a lightweight serverless database, and the **SQLite Browser** as a GUI tool to create tables and run SQL queries.

---

#### Day 8: Python Bootcamp – Hands-On Coding
*Session: "Applied Python for Engineering & Climate Systems"*

The sessions from the `1 - Applied Python for Engineering & Climate Systems` module provided extensive hands-on practice. A summary of the practical coding tasks from the provided notebooks is below.

- **`Day_1.1.ipynb` Summary:** This session focused on the fundamental building blocks of Python. The exercises involved creating variables of different data types (strings, integers, floats) and using the `type()` function to inspect them. We practiced using arithmetic operators, creating simple expressions, and assigning results to new variables. The notebooks also served as an introduction to Colab's environment.

- **`Day_1.2.ipynb` Summary:** This session moved beyond simple variables to more complex data structures and control flow. The exercises focused on writing functions with parameters, returning values, and understanding variable scope. We implemented logic using `if/elif/else` statements to make decisions and used `for` and `while` loops to iterate over data, performing calculations and counting operations. The practice included creating a simple calculator function and a vowel counting utility.

- **`Day_1.3.ipynb` Summary:** The focus of this notebook was on working with text data (strings) and data collections (lists, tuples, dictionaries). Exercises involved string slicing, cleaning, and parsing, such as extracting usernames from email addresses and checking for palindromes. We also practiced using list methods like `.append()` and `.sort()`, and explored dictionary operations for storing and retrieving key-value data, such as creating a simple word frequency counter.

- **`Day_1.4.ipynb` Summary:** This session bridged data manipulation with the program's climate theme. The coding exercises involved using lists and dictionaries to model and analyze simple climate-related datasets. For example, we calculated averages from a list of temperatures, processed a list of dictionaries containing city climate data, and used loops to filter datasets based on conditions. This practical work reinforced the application of core Python skills to engineering and environmental problems.


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

- **[Cristóvăo Cacombe](https://www.linkedin.com/in/cristov%C3%A3o-cacombe-0b4514a3/)** (UNDP Course Guide) for his excellent instruction and guidance.
- The **UNDP**, the **SDG AI Lab**, and **Damascus University** for creating and delivering this comprehensive program.
- The **German Federal Ministry for Economic Cooperation and Development (BMZ)** and **KfW** for their generous support.
- My fellow participants for the collaboration and shared learning journey.

Special thanks to the **FTL Team** for their continuous support and coordination. This program is a life-changing opportunity, and I am committed to making the most of it.