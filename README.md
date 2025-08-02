# Variables-control-structure-capstone
Interactive Python financial calculator with loan payment, compound interest, and investment return calculations. Demonstrates mastery of variables, control structures, and input validation.
financial-calculator-capstone/
# Variables-Control-Structure-Capstone

## 📊 Financial Calculator Project

A comprehensive Python financial calculator that demonstrates mastery of fundamental programming concepts including variables, control structures, and user input validation. This capstone project provides essential financial calculations for investment planning and loan management.

## 🎯 Project Overview

This interactive console application allows users to calculate:
- **Simple Interest** - Linear growth on investments
- **Compound Interest** - Exponential growth with compounding
- **Bond Repayments** - Monthly mortgage/loan payment calculations

## ✨ Features

- **Investment Calculator**
  - Simple interest calculations using A = P(1 + rt)
  - Compound interest calculations using A = P(1 + r)^t
  - User choice between calculation methods

- **Bond Calculator**
  - Monthly repayment calculations for home loans
  - Uses standard bond repayment formula
  - Handles various loan terms and interest rates

- **User Experience**
  - Clear menu system with detailed descriptions
  - Input validation and error handling
  - Formatted output for easy reading
  - Case-insensitive input processing

## 🛠️ Technologies Used

- **Python 3.x**
- **Math Library** - For exponential calculations
- **Built-in Functions** - Input validation and string manipulation

## 🚀 How to Run

1. **Prerequisites**: Ensure Python 3.x is installed on your system
2. **Download**: Clone or download the `financial_calculator.py` file
3. **Execute**: Run the program from your terminal/command prompt:
   ```bash
   python financial_calculator.py
   ```
4. **Follow Prompts**: Select your calculation type and enter the required values

## 📝 Usage Examples

### Investment Calculation (Simple Interest)
```
Enter either "investment" or "bond": investment
Select "simple" or "compound" interest: simple
Enter the amount of money you deposit: 1000
Enter the interest rate (in percentage): 5
Enter the number of years you plan on investing: 3
Total amount of money after 3 years with simple interest is 1150.0
```

### Investment Calculation (Compound Interest)
```
Enter either "investment" or "bond": investment
Select "simple" or "compound" interest: compound
Enter the amount of money you deposit: 1000
Enter the interest rate (in percentage): 5
Enter the number of years you plan on investing: 3
Total amount of money after 3 years with compound interest is 1157.63
```

### Bond Calculation
```
Enter either "investment" or "bond": bond
Enter the value of the house: 200000
Enter your monthly interest rate (in percentage): 0.5
Enter the number of months over which the bond will be repaid: 240
You have to repay the amount of money monthly is 1319.91
```

## 📚 Programming Concepts Demonstrated

### Variables & Data Types
- **Float variables** for monetary calculations and percentages
- **Integer variables** for time periods
- **String variables** for user input and menu options
- **Type conversion** between strings and numeric types

### Control Structures
- **Conditional statements** (if, elif, else) for menu navigation
- **Nested conditions** for investment type selection
- **Input validation** logic flow

### User Input & Validation
- **Input sanitization** using `.lower().strip()`
- **Error handling** for invalid menu selections
- **Type conversion** with proper validation

### Mathematical Operations
- **Arithmetic operations** for financial formulas
- **Exponential calculations** using `math.pow()`
- **Percentage conversions** and rate calculations

## 🧮 Mathematical Formulas

### Simple Interest
```
A = P(1 + rt)
Where: A = Final amount, P = Principal, r = Interest rate, t = Time
```

### Compound Interest
```
A = P(1 + r)^t
Where: A = Final amount, P = Principal, r = Interest rate, t = Time
```

### Bond Repayment
```
M = (i × P) / (1 - (1 + i)^(-n))
Where: M = Monthly payment, i = Monthly interest rate, P = Principal, n = Number of payments
```

## 🎓 Learning Outcomes

This project successfully demonstrates:
- **Problem decomposition** - Breaking complex financial calculations into manageable steps
- **User interface design** - Creating intuitive menu systems and clear prompts
- **Data validation** - Ensuring user input is clean and appropriate
- **Mathematical implementation** - Translating financial formulas into working code
- **Code organization** - Structuring logic flow for maintainability

## 🔧 Future Enhancements

Potential improvements for this project:
- Add input validation for negative numbers
- Implement error handling for non-numeric inputs
- Create graphical user interface (GUI)
- Add more financial calculation options (savings goals, loan comparisons)
- Include data persistence to save calculation history

## 📄 File Structure

```
Variables-control-structure-capstone/
├── README.md
├── financial_calculator.py
└── examples/
    └── sample_outputs.txt
```

## 👨‍💻 Author

**Arturs Kaufmanis**
- Transitioning from law enforcement to cybersecurity
- Applying analytical and problem-solving skills to programming
- Building foundational programming knowledge through practical projects

## 📝 License

This project is created for educational purposes as part of a cybersecurity learning journey.

---

*This project represents a foundational understanding of Python programming concepts and demonstrates the ability to create practical, user-friendly applications.*
