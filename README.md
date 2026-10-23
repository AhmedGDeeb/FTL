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
| **Python Hackathon** | ✅ **Done** | Group-based problem solving and presentation |
| **Data Analysis & SDG** | 🔄 **In Progress** | Data manipulation, analysis techniques, peer coding |
| **Applied Machine Learning** | 🔄 **In Progress** | Regression, Classification, Clustering, Model Development |
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

Of course. Here is the updated version of your learning journal. I have added a new section detailing your experience and project from the Python Hackathon, as requested. This new section is inserted after the "Session Notes & Key Learnings" and before the "Capstone Project" section.


---

### Day 8: Python Bootcamp – Hands-On Coding
*Session: "Applied Python for Engineering & Climate Systems"*

The sessions from the `1 - Applied Python for Engineering & Climate Systems` module provided extensive hands-on practice. A summary of the practical coding tasks from the provided notebooks is below.

- **`Day_1.1.ipynb` Summary:** This session focused on the fundamental building blocks of Python. The exercises involved creating variables of different data types (strings, integers, floats) and using the `type()` function to inspect them. We practiced using arithmetic operators, creating simple expressions, and assigning results to new variables. The notebooks also served as an introduction to Colab's environment.

- **`Day_1.2.ipynb` Summary:** This session moved beyond simple variables to more complex data structures and control flow. The exercises focused on writing functions with parameters, returning values, and understanding variable scope. We implemented logic using `if/elif/else` statements to make decisions and used `for` and `while` loops to iterate over data, performing calculations and counting operations. The practice included creating a simple calculator function and a vowel counting utility.

- **`Day_1.3.ipynb` Summary:** The focus of this notebook was on working with text data (strings) and data collections (lists, tuples, dictionaries). Exercises involved string slicing, cleaning, and parsing, such as extracting usernames from email addresses and checking for palindromes. We also practiced using list methods like `.append()` and `.sort()`, and explored dictionary operations for storing and retrieving key-value data, such as creating a simple word frequency counter.

- **`Day_1.4.ipynb` Summary:** This session bridged data manipulation with the program's climate theme. The coding exercises involved using lists and dictionaries to model and analyze simple climate-related datasets. For example, we calculated averages from a list of temperatures, processed a list of dictionaries containing city climate data, and used loops to filter datasets based on conditions. This practical work reinforced the application of core Python skills to engineering and environmental problems.

---

## 🚀 Python Hackathon: FTL Syria AI4Climate

[Full details](hackathon\idea.md)

The Python Hackathon was a four-day intensive challenge where teams used Python and climate-related data to investigate a real-world environmental problem. Our project, **Syria WheatWatch**, was developed for this event.

### The Challenge: Syria WheatWatch

The 2024–2025 drought was Syria's worst in nearly four decades, causing rainfall to drop over 50% below average and wheat production to collapse to 900,000 tonnes. This created a 3 million tonne deficit and pushed millions into food insecurity. Our team set out to build an open, reproducible early-warning tool to analyze how rainfall and solar variability have affected Syrian wheat production between 1991 and 2025.

**Our Team (Team 4):** Haya Sukkar, Nimra Afzaal, Sular Albalkhi, Abdulrahman Abdulkader, Ahmad Deeb, and Aous Azzam.

### What We Built

Our project, **Syria WheatWatch**, is a full data pipeline and predictive tool:

- **📊 Data Pipeline:** A Python pipeline that merges 34 years of data from **NASA POWER** (solar irradiance), **HDX** (rainfall), and **FAOSTAT** (crop production).
- **📈 Analysis & Modeling:** We performed correlation and regression analysis. Our key finding was that **climate variability drives crop yield, not planted area**. A linear regression model we developed can predict wheat yield from rainfall and solar inputs (cross-validated R² ≈ 0.35).
- **🚀 Public API & Web Service:** We deployed our model as a public **FastAPI** web service with a JSON API, allowing anyone to get yield predictions for given climate conditions.
- **📉 Interactive Dashboard:** We created a **Power BI dashboard** for exploring historical drought severity and production trends.

### Key Findings

The project's core insight is that climate variability impacts wheat production through the **yield channel**, not the **area channel**:

- **Climate-driven:** Wheat **yield** (per-hectare output) is strongly correlated with rainfall (r = +0.54) and solar irradiance (r = -0.65).
- **Not climate-driven:** Planted **area** has no significant correlation with rainfall (r = 0.13) or solar (r = -0.11). It is primarily influenced by conflict, policy, and economic factors.

This distinction is critical for early warning: it tells us to monitor weather to predict yield, and to monitor policy and conflict to predict planting decisions.

### Project Deliverables

- **🐍 Python Notebook:** The full analysis from data cleaning to modeling is documented in our notebooks.
- **📂 Dataset:** The raw and cleaned datasets are available in the repository.
- **📄 Presentation:** Our final 7-slide presentation is included.
- **📝 Project Summary:** A detailed README file explains the project.
- **🔗 Public Links:**
    - **Live API & Web Interface:** [https://syria-wheat-api.onrender.com/](https://syria-wheat-api.onrender.com/)
    - **Full Code Repository:** [Link to the GitHub Repo](https://lnkd.in/e36a6yda)

This project was a fantastic opportunity to apply our Python skills to a pressing humanitarian challenge. We are grateful to the FTL team, our instructor Cristóvão Cacombe, and the open data providers (NASA, HDX, FAO) for making this work possible. A summary of our journey and impact was also shared on [LinkedIn](https://lnkd.in/p/eyWnace7).

---

## Data Analysis & SDG

### Day 9: Introduction to Data in Data Science
*Session: "Data and Data Collection"*

- **What is Data?:** We explored the definition of data as raw, unprocessed facts and observations. The session emphasized that data's true value emerges only when it is processed, interpreted, and applied effectively to generate insights and support decision-making.
- **The Role of Data:** We discussed how data is used across different domains—businesses optimize operations, researchers address societal challenges, and policymakers develop evidence-based strategies. This reinforced the program's goal of using data to tackle climate and environmental issues.

---

### Day 10: Data Quality Characteristics
*Session: "Data and Data Collection"*

- **Key Quality Dimensions:** We learned that high-quality data must be **accurate**, **complete**, **consistent**, **timely**, and **relevant**. Poor data quality can lead to biased or incorrect conclusions, making validation a critical step.
- **Impact on Analysis:** The session highlighted that understanding data quality is essential before any modeling or analysis. Identifying issues early prevents compounding errors and ensures that insights are reliable and actionable.

---

### Day 11: Common Data Formats
*Session: "Data and Data Collection"*

- **CSV (Comma-Separated Values):** A simple, tabular format ideal for spreadsheets and many data analysis tools. Best for structured, flat data.
- **JSON (JavaScript Object Notation):** A hierarchical, nested format commonly used in web APIs and for semi-structured data.
- **XML (eXtensible Markup Language):** A structured format for data exchange, useful when data requires a strict schema.
- **Pickle:** A Python-specific format for serializing and de-serializing Python objects, ideal for saving models or complex data structures.
- **Choosing the Right Format:** We discussed how the choice of format depends on the data's structure, the tools being used, and the need for compatibility with other systems.

---

### Day 12: Web Scraping, Data Privacy & Ethics
*Session: "Data and Data Collection"*

- **HTTP Requests & Parsing:** We learned to use the **`requests`** library to fetch web pages and **BeautifulSoup** to parse HTML content, navigate the document tree, and extract specific data elements like tables, links, and text.
- **Ethical and Legal Considerations:** The session emphasized the importance of respecting `robots.txt`, website terms of service, and copyright laws. We discussed the responsibility of scraping only public data and avoiding excessive requests that could disrupt services.
- **GDPR and Data Protection:** We covered the General Data Protection Regulation (GDPR) and its principles, including lawful processing, data minimization, and user consent. The session highlighted the importance of protecting personal data and ensuring transparency.
- **Ethical Data Handling:** Beyond legal compliance, we discussed the ethical responsibilities of data scientists—avoiding bias, ensuring fairness, and being transparent about data sources and methods.

---

Here is the revised section, with a clearer focus on the problem, simpler explanations, and a dedicated team section:

---

## Pair Coding Session

### Day 13: Water Access Analysis

*Session: "Group/Pair Coding Challenge"*

---

#### 👥 Our Team

- Diana
- Nimra
- Albert
- Ahmad

---

#### 🎯 The Problem

A humanitarian program needed to know: **Which community should we visit first to address water shortages?**

We were given a survey dataset (`survey.csv`) containing records from four communities (A, B, C, D). Each record included:
- `survey_id` — unique identifier for each survey
- `community` — the community name
- `households` — number of households represented
- `days_without_water` — how many days that household went without water
- `latitude` / `longitude` — location coordinates

The data was messy. It had duplicates, missing values, and invalid entries (like "unknown" for households and "8" for days without water). Our job was to clean it, apply validation rules, and calculate which community had the highest percentage of households facing at least 3 days without water.

---

#### 🧹 How We Cleaned the Data

We applied these rules step by step:

| Rule | What We Did |
|------|-------------|
| **One record per survey** | Removed duplicate rows using `drop_duplicates()` |
| **Households must be positive whole numbers** | Converted to numeric with `pd.to_numeric(errors='coerce')`, filled missing values with the median, and rounded to whole numbers |
| **Days without water must be 0–7** | Clipped values below 0 to 0 and above 7 to 7 |
| **Exclude invalid records** | Kept only complete records in `df_clean`, but saved the original data for review |

After cleaning, we had **10 valid records** across the four communities.

---

#### 📊 What We Calculated

For each community, we calculated:

1. **Total households represented** — sum of households per community
2. **Households with ≥3 days without water** — counted only those where `days_without_water >= 3`
3. **Percentage affected** — (affected households ÷ total households) × 100

**Results:**

| Community | Total Households | Affected Households | % Affected | Avg. Days Without Water |
|-----------|-----------------|---------------------|------------|-------------------------|
| Community B | 40 | 40 | **100%** | 5.0 |
| Community D | 30 | 30 | **100%** | 5.5 |
| Community A | 30 | 20 | 66.7% | 3.0 |
| Community C | 30 | 10 | 33.3% | 1.67 |

We visualized this with a bar chart comparing the percentages side by side.

---

#### 🏆 Our Recommendation

**Visit Community D first, then Community B.**

**Why?**
- Both communities had **100% of households** reporting at least 3 days without water.
- They were tied, so we used **severity** as a tie-breaker: Community D averaged **5.5 days** without water, while Community B averaged **5.0 days**.
- Community A (66.7%) is a secondary concern.
- Community C (33.3%) needs no urgent follow-up.

---

#### 📝 Data Collection Lesson

We proposed two simple validation rules for future survey forms to prevent these errors:

1. **Households field:** Only allow positive whole numbers (no text like "unknown").
2. **Days without water field:** Only allow whole numbers from 0 to 7 (no 8 or higher).

These rules would catch bad data at the source and save hours of cleaning later.

---

#### 🛠️ Tools We Used

`pd.read_csv()`, `pd.to_numeric()`, `duplicated()`, `drop_duplicates()`, `groupby()`, `agg()`, and `matplotlib` for the bar chart.

---

This session showed us how messy real-world data can be—and how a structured cleaning process and clear visualization can turn chaos into a clear, actionable recommendation.

---

## Applied Machine Learning

## Applied Machine Learning

### Day 14: Linear Regression

- **The model:** `f(x) = w*x + b` — `w` (weight/slope) measures how much the prediction changes as the input changes; `b` (bias/intercept) is the predicted value when `x = 0`. `ŷ` is the model's prediction.
- **Univariate linear regression:** Linear regression with one variable — fitting a line through data (e.g., house size vs. price). The model is written `f_{w,b}(x) = wx + b`.
- **Notation:** `x` = input feature, `y` = output target, `m` = number of training examples, `(x, y)` = single training example, `(x⁽ⁱ⁾, y⁽ⁱ⁾)` = i-th training example.
- **Prediction errors:** For each example, error = prediction − actual (`ŷ⁽ⁱ⁾ − y⁽ⁱ⁾`). Squaring prevents positive and negative errors from cancelling out and gives larger errors more influence.
- **Cost function (MSE):** `J(w,b) = (1/2m) Σᵢ₌₁ᵐ (wx⁽ⁱ⁾ + b − y⁽ⁱ⁾)²`. The factor `1/2` makes derivatives simpler and does not change which parameters minimise the cost.
- **Worked example:** With three points and a line `f(x) = 0.5x` (or similar), the cost is computed as `J(w,b) = (1/(2×3)) × ((1.5−1)² + (4−2)² + (2−2.5)²) = 0.75`.
- **Comparing candidate lines:** Different `(w, b)` pairs produce different lines; each line has its own cost. The cost function gives one number to summarise how well each line fits all the examples and to objectively compare them.
- **Visualising the cost function:** The cost surface over `(w, b)` is bowl-shaped (convex for linear regression), with a unique global minimum. Cross-sections show the cost as a function of one parameter while holding the other fixed.
- **How to represent f:** The hypothesis is the linear function `f_{w,b}(x) = wx + b`; fitting means finding the `w, b` that minimise the cost.
- **From slides:** Examples of lines with different `w, b` — `w = 0, b = 1.5` (horizontal), `w = 0.5, b = 0` (through origin), `w = 0.5, b = 1` (shifted up) — showing how slope and intercept change the fit.

---

### Day 15: Regression Evaluation

- **Cost function recap:** `J(w,b) = (1/2m) Σ(prediction − actual)²`. It averages squared errors across all examples and penalises large errors more heavily.
- **Gradient descent outline:** (1) Initialise parameters; (2) calculate the gradient of the loss with respect to each parameter (points in the direction of steepest increase); (3) update parameters by a small amount opposite the gradient; (4) repeat, each time moving closer to the minimum.
- **Gradients for linear regression:**
  - `∂J/∂w = (1/m) Σᵢ₌₁ᵐ (wx⁽ⁱ⁾ + b − y⁽ⁱ⁾) x⁽ⁱ⁾`
  - `∂J/∂b = (1/m) Σᵢ₌₁ᵐ (wx⁽ⁱ⁾ + b − y⁽ⁱ⁾)`
  - The slope gradient includes `x` because changing `w` affects predictions in proportion to `x`; the intercept gradient is the average prediction error.
- **Update rule:** `w := w − α·∂J/∂w`, `b := b − α·∂J/∂b`, where `α` is the learning rate.
- **Simultaneous update:** Calculate both gradients from the same old values of `w` and `b`, then update both parameters together. Updating one first and using the new value to compute the other gradient is incorrect.
- **Learning rate (`α`):** Controls step size. Too small → cost decreases very slowly; reasonable → cost decreases steadily; too large → cost may oscillate or diverge. Near a local minimum, the derivative becomes smaller, so update steps naturally become smaller — a fixed learning rate can reach the minimum.
- **Positive vs. negative slope:** On the right of the minimum the slope is positive, so subtracting `α·gradient` moves `w` left (downhill); on the left the slope is negative, so subtracting moves `w` right (downhill).
- **Local vs. global minima:** Non-convex cost surfaces can have local minima, maxima and a global minimum. Techniques to escape local minima include adding noise, momentum, and learning-rate adjustment. For linear regression, MSE is convex, so gradient descent converges to the global minimum.
- **Batch gradient descent:** Each step uses all training examples. Cost decreases smoothly. One update = one iteration.
- **Stochastic gradient descent (SGD):** Each update uses a single observation; cost shows many variations but can be faster per step.
- **Mini-batch gradient descent:** Each update uses a subset of the data; cost is smoother than SGD and can be more efficient than batch.
- **Comparison:** Batch = entire dataset per update, smooth cost curve; SGD = single observation per update, noisy cost curve; mini-batch = subset per update, smoother than SGD.
- **Feature scaling for numerical stability:** Raw feature magnitudes (e.g., house sizes in square feet ~2000) make gradients very large. Rescaling (e.g., thousands of square feet) keeps steps reasonable. This changes the units of the slope, not the underlying relationship.
- **One update step-by-step:** From `w=0, b=0`, `α=0.1`: compute `∂J/∂w`, `∂J/∂b` from old values, compute new `w`, `b`, then compare cost before and after — the cost should decrease.
- **Cost during training:** A falling cost curve indicates the cost is getting smaller; a plateau indicates convergence.
- **Evaluating the fitted line:** Compare the learned line with observations; inspect the cost curve; examine the gradient descent path on cost contours.
- **Evaluation metrics:** MAE (average absolute error, in target units), RMSE (square root of average squared error; penalises large errors more), R² (compares model against predicting the mean; can be negative on test data). Lower MAE and RMSE are generally better; interpret all metrics in the context of the intended decision.
- **Baseline comparison:** Always compare a trained model against a simple reference (e.g., predicting the training mean) to judge whether the model is useful.
- **Prediction for new inputs:** Apply the learned `w, b` to a new `x`; report in original units (e.g., house size × 1000, price × 1000 USD).

---

### Day 16: Classification Fundamentals

- **Regression vs. classification:** Regression predicts a numerical quantity (`ŷ ∈ ℝ`, e.g., daily energy generation = 145.7 kWh). Classification predicts membership in a category (binary `y ∈ {0,1}`, multiclass `y ∈ {1…K}`, e.g., land-cover class = cropland).
- **Evaluation measures:** Regression uses MAE, RMSE; classification uses precision, recall, F1, accuracy.
- **Classification examples:** Cancer detection (tumour size → malignant/benign); land-cover classification from satellite imagery. A classifier may output class scores or probabilities before applying a decision rule.
- **Binary classification:** Two classes (e.g., 0 = benign, 1 = malignant). The model learns a decision boundary.
- **Multiclass classification:** More than two classes (`y ∈ {1, 2, …, K}`), e.g., multiple land-cover types.
- **Two or more inputs:** With two features (`x₁`, `x₂`), the decision boundary is a line in 2D space; with more features it becomes a plane or hyperplane. Example: tumour size and age → malignant/benign.
- **Supervised learning with labelled data:** The model is trained on labelled examples (shapes with class labels) and predicts labels for test data (e.g., circle, triangle, square classification).
- **Classification workflow:** Provide labelled examples → generate predictions → measure disagreement → adjust the model → evaluate on separate examples (same as supervised training process).
- **Important consideration:** A classifier's output may be a probability; a decision threshold converts it to a class. Threshold choice trades off precision and recall.
- **Connection to climate:** Classification supports land-cover mapping, event detection, and risk categorisation (e.g., high-rainfall day vs. normal day).


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