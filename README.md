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

This section is my personal knowledge base. I'll add key takeaways from each session here. All code and exercises will be in my main [Colab Notebook](https://colab.research.google.com/github/AhmedGDeeb/FTL/blob/main/tasks/FTL_Tasks_ahmad_deeb.ipynb).

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

- **My Code & Exercises:** [Link to my Day 1 Notebook](https://colab.research.google.com/github/AhmedGDeeb/FTL/blob/main/tasks/FTL_Tasks_ahmad_deeb.ipynb)

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
- **My Code & Exercises:** [Link to my Day 2 Notebook](https://colab.research.google.com/github/AhmedGDeeb/FTL/blob/main/tasks/FTL_Tasks_ahmad_deeb.ipynb)

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

- **My Code & Exercises:** [Link to my Day 3 Notebook](https://colab.research.google.com/github/AhmedGDeeb/FTL/blob/main/tasks/FTL_Tasks_ahmad_deeb.ipynb)

---

### Day 4: Session 3 — Data Structures (Sep 17, 2026)

**Key Takeaways:**

- **Data Structures Overview:**
    - A data structure is a way of storing and organizing data so it can be accessed and updated efficiently.
    - Classified into **Linear** (lists, tuples) and **Non-linear** (dictionaries).

- **Python Lists:**
    - **Definition:** Ordered collections that can contain mixed data types. They are similar to arrays in other languages but with more capabilities.
    - **Properties:**
        - **Ordered:** Maintain the order of data insertion (e.g., `ordered_list[0]` returns the first item).
        - **Changeable (Mutable):** Items can be modified after creation (e.g., `ordered_list[0] = 'mango'`).
        - **Heterogeneous:** Can contain data of different types (e.g., `['apple', 100, 3.14, True, ['sub-list', 'elements']]`).
        - **Allows Duplicates:** Duplicate data is permitted (e.g., `['apple', 'apple', 'banana', 'cherry', 'banana']`).

- **List Methods:**
    - **`.append(item)`** — Adds a single item to the end of the list. If the item is a list, it is added as a nested list.
    - **`.extend(iterable)`** — Adds multiple items from an iterable to the end, flattening them into the list.
    - **`.sort(reverse=True/False)`** — Sorts the list in place. `reverse=True` sorts in descending order.
    - **`len(list)`** — Returns the number of items in the list.

- **List Operations:**
    - **`+` (Concatenation):** Combines two lists into a new list (e.g., `[1, 3, 3] + [4, 4, 6]` = `[1, 3, 3, 4, 4, 6]`).
    - **`*` (Repetition):** Repeats a list a given number of times (e.g., `[1, 3, 3] * 3` = `[1, 3, 3, 1, 3, 3, 1, 3, 3]`).

- **List Slicing:**
    - Format: `list[start:end]` — starts at `start` and goes up to, but does **not** include, `end`.
    - **Negative Slicing:** `numbers[-3:]` returns the last three items.
    - **Example:** `numbers[2:4]` on `[0, 1, 2, 3, 4, 5]` returns `[2, 3]`.

- **Accessing List Elements:**
    - Items are identified by their position, starting with `0`.
    - **Negative Indexing:** `dogs[-1]` returns the last element; `dogs[-2]` returns the second-to-last.

- **Lists and Loops:**
    - **`for` Loop:** Iterates over each item in the list (e.g., `for dish in dishes: print('I love ' + dish + ' very much')`).
    - **`enumerate()`:** Tracks the index of each item during iteration (e.g., `for index, dish in enumerate(dishes): print('Dish Number: ' + str(index) + ' ' + dish)`).

- **Lists and Strings:**
    - **`.split()`** — Breaks a string into a list of words (e.g., `"Python for Everybody".split()` returns `['Python', 'for', 'Everybody']`).
    - **`.join()`** — Combines a list into a string (e.g., `' '.join(words)` returns `"Python for Everybody"`).

- **Dictionaries:**
    - **Definition:** Store data values in **key:value** pairs. General syntax: `{key_1: value_1, key_2: value_2}`.
    - **Characteristics:**
        - **Keys are unique** — no duplicates allowed.
        - **No index** — not ordered by position; the key is the default iterator used to retrieve values.
        - **Mutable (changeable)** — values can be modified (e.g., `fruits_dict['apple'] = 4`).
        - Accessing a non-existent key raises a **`KeyError`** (e.g., `fruits_dict[0]`).

- **Dictionary Methods:**
    - **`.keys()`** — Returns all keys (e.g., `dict_keys(['apple', 'oranges', 'mangos'])`).
    - **`.values()`** — Returns all values (e.g., `dict_values([4, 2, 3])`).
    - **`.items()`** — Returns all key:value pairs as tuples (e.g., `dict_items([('apple', 4), ('oranges', 2), ('mangos', 3)])`).

- **Common Dictionary Operations:**
    - **Adding new key-value pairs:** `african_countries['Nigeria'] = 'Abuja'`.
    - **Modifying values:** `african_countries['Cameroon'] = 'Yaounde'`.
    - **Removing key-value pairs:** `del african_countries['Cameroon']`.
    - **Modifying keys:** Two steps — create a new key with the old value, then delete the old key (e.g., `african_countries['Niger'] = african_countries['Nigeria']; del african_countries['Nigeria']`).

- **Dictionaries and Loops:**
    - **Loop through all key-value pairs:** `for country, capital in african_countries.items():`.
    - **Loop through all keys:** `for key in my_dict.keys():` (or simply `for key in my_dict:`).
    - **Loop through all values:** `for value in my_dict.values():`.

- **Tuples:**
    - **Definition:** Ordered, **immutable** collections — like lists that can never be changed after creation. Can contain mixed data types.
    - **Creating Tuples:** `sample_tuple = (1, 2, "Python", 3.5)`; convert from a list with `tuple(['Veery', 'Eastern Meadowlark', 10, 25, True])`; blank tuple with `tuple()`.
    - **Accessing Elements:** Same indexing as lists (e.g., `c_tup[2]` returns `'South Africa'`).
    - **Slicing:** Same syntax as lists (e.g., `c_tup[1:4]` returns `('Egypt', 'South Africa', 'Ghana')`).
    - **Converting between Lists and Tuples:** `tuple(sample_list)` and `list(converted_tuple)`.
    - **Tuples as Return Values:** Functions can return multiple values as a tuple (e.g., `def min_max(numbers): return (min(numbers), max(numbers))`).

- **Dictionaries and Tuples (Advanced):**
    - **Sorting by key:** `sorted(word_freq.items())`.
    - **Sorting by value:** `sorted(word_freq.items(), key=lambda item: item[1], reverse=True)` — uses a lambda to select the value for sorting.

- **Assignments:**
    - **List Assignment (Party):** Maintain a guest list using Python lists — add guests, remove guests, and check who's on the list.
    - **Advanced Party Guest Manager:** Build a guest management system using dictionaries and tuples:
        1. Initialize an empty `guests` dictionary where each guest has a name, age, and email.
        2. Add guests using tuples: `"Alice", 28, "alice@email.com"`, `"Bob", 35, "bob@email.com"`, `"Charlie", 30, "charlie@email.com"`. Use the name as the key and `(age, email)` as the value.
        3. Update the list: add `"David", 22, "david@email.com"` and remove `"Bob"`.
        4. Create `get_guest_info(guest_name)` — returns a formatted string if the guest is on the list, otherwise a "not on the guest list" message.
        5. Display the total number of guests.
        - **Extensions:** Allow user input for new guests, display guests in order of age, and handle duplicate guest names by prompting to update or skip.

- **My Code & Exercises:** [Link to my Day 4 Notebook](https://colab.research.google.com/github/AhmedGDeeb/FTL/blob/main/tasks/FTL_Tasks_ahmad_deeb.ipynb)

# Day 5: Session 4 — Working with Scientific Data in Python / Intro to OOP (Sep 21, 2026)

## Key Takeaways

### 1. Course Plan & Capstone Projects
- The week includes: continued Python material, a coding session, a ninth session, and a **Wednesday coding challenge**.
- **Capstone projects**: Participants can choose their own topics. The instructor will provide optional problem suggestions and guidelines for documenting the problem and proposed solution.
- Submission options:
  - **No GitHub**: Submit a Python notebook or script via email.
  - **With GitHub**: Upload work and send the link to the instructor.

### 2. Review of Lists, Loops, Dictionaries, Strings & Tuples
- **Lists + Loops**: `for` loops iterate over each item in a list.
- **`enumerate()`**: Exposes the index of each item during iteration.
- **String ↔ List conversion**:
  - `.split()` — breaks a string into a list of words
  - `.join()` — combines a list into a string
- **Dictionaries**: Key-value collections with unique keys; demonstrated reading, changing, adding, and removing entries.
- **Looping through dictionaries**: Process keys, values, or complete key-value pairs.
- **Tuples**: Ordered, immutable collections; demonstrated creation, conversion from lists, indexing, slicing, and use for preserving unchangeable values.

### 3. Guest-List Application Demonstration (Abdulrahman Abdulkader)
- Presented a guest-list app that:
  - Separated data operations from command-line display and control logic
  - Handled empty lists and errors gracefully
  - Used a **dictionary to map menu choices to functions**
- **Function references**: George Al Issa asked how the dictionary referenced functions. Abdulrahman explained that functions are objects whose references can be stored and later invoked through dictionary keys.

### 4. Transition to Object-Oriented Programming (OOP)
- OOP helps organize larger programs and prevents code repetition.
- **Core terminology**:
  - **Class**: A template/blueprint defining attributes and behavior
  - **Attribute**: A variable within a class
  - **Method**: A function within a class
  - **Object**: A particular instance of a class
  - **Constructor**: Runs when an object is created
  - **Inheritance**: Extending a class to make a new class
  - **Encapsulation & Abstraction**: Deferred to later sessions

### 5. Python Objects & Built-In Classes
- In Python, **everything is an object**.
- Examples:
  - `type("a")` → `str` class
  - `type(2.2)` → `float` class
  - `type(5)` → `int` class
  - Lists belong to the `list` class
- Built-in objects (strings, integers, floats, lists) expose methods defined by their classes.

### 6. Creating a Custom Dog Class
- Started with an **empty class** using `pass` as a placeholder (Python doesn't allow empty class bodies).
- Created an **instance** and checked its type.
- Progressed from an empty class to one with attributes and methods.

### 7. Instance Attributes & Methods
- **`__init__`**: Constructor method to initialize attributes when a new instance is created.
- **`self`**: Represents the individual object/instance.
- **Instance attributes**: Belong to each individual object (e.g., a dog's name and age).
- **Methods**: Define behavior (e.g., eating, sleeping, barking).
- Example: A dog's `tired` state controlled whether it would sleep or play.

### 8. Class Attributes & Inheritance
- **Class attributes**: Defined outside the constructor; shared by all instances of the class (e.g., `species = "canine"`).
- Useful for storing constants and values common to all instances.
- **Inheritance**: Introduced as a future topic — allows a new class to reuse attributes and behaviors from an existing class.
- **Encapsulation and abstraction**: Deferred.

### 9. Practice Exercises & Submission Process
- Instructor shared **class exercises** for participants to complete independently.
- Exercises will be reviewed at the beginning of the next session.
- **Submission options** (clarified for Amjad Shekhani):
  - Email a Python notebook or script
  - Submit a GitHub link
- Instructor planned to share materials earlier before future sessions.


# Day 6: Session 5 – ... (Sep 22, 2026)

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