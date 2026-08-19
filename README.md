# 🧮 Python Calculator with Firebase

A simple **Python calculator application** that performs basic arithmetic operations and stores the calculated result in **Firebase Realtime Database**.

## 📌 Project Overview

This project combines **Python programming** with **Firebase Realtime Database**. The user enters two numbers and an arithmetic operator. The program performs the calculation and uploads the result to Firebase.

### Supported Operations

* Addition `+`
* Subtraction `-`
* Multiplication `*`
* Division `/`

## 🛠️ Technologies Used

* **Python**
* **Firebase Realtime Database**
* **Firebase Admin SDK**
* **Python `firebase_admin` library**

## 📂 Project Structure

```text
Python-Firebase-Calculator/
│
├── calculator.py
├── firebase-service-account.json
└── README.md
```

## ⚙️ Requirements

Before running the project, install the Firebase Admin SDK:

```bash
pip install firebase-admin
```

You also need:

1. A Firebase project
2. Firebase Realtime Database
3. Firebase Admin SDK service-account JSON file
4. Python installed on your system

## 🔥 Firebase Configuration

The program connects to Firebase using a service-account credential:

```python
cred = credentials.Certificate("path/to/service-account.json")

firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://your-project-default-rtdb.firebaseio.com/"
    }
)
```

> **Security Note:** Never upload your Firebase service-account JSON file to GitHub. Add it to `.gitignore`.

Example:

```text
firebase-service-account.json
*.json
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Python-Firebase-Calculator.git
```

### 2. Install the required library

```bash
pip install firebase-admin
```

### 3. Configure Firebase

Replace the Firebase credential path and database URL with your own Firebase project details.

### 4. Run the program

```bash
python calculator.py
```

## 💻 Example

```text
Enter the first number: 20
Enter the Operator: +
Enter the second number: 10

data sent
```

The result stored in Firebase will be:

```text
Calsi
   └── calculate the number: 30
```

## 🔄 How It Works

```text
User Input
    ↓
First Number
    ↓
Operator
    ↓
Second Number
    ↓
Python Calculator
    ↓
Calculation Result
    ↓
Firebase Realtime Database
```

## 🧠 Important Code Concepts

### Taking User Input

```python
a = float(input("Enter the first number"))
b = input("Enter the Operator")
c = float(input("Enter the second number"))
```

The program accepts two numbers and an arithmetic operator from the user.

### Performing Calculation

```python
if b == "+":
    d = a + c
elif b == "*":
    d = a * c
elif b == "/":
    if c != 0:
        d = a / c
elif b == "-":
    d = a - c
```

The `if-elif` statements determine which mathematical operation should be performed.

### Connecting to Firebase

```python
ref = db.reference('Calsi')
```

This creates a reference to the `Calsi` node in Firebase Realtime Database.

### Uploading Data

```python
ref.push({"calculate the number": d})
```

The calculated result is uploaded to Firebase using `push()`.

## ⚠️ Error Handling

The program prevents division by zero:

```python
if c != 0:
    d = a / c
else:
    print("cannot divide by zero")
```

It also displays `"Fail"` when an unsupported operator is entered.

## 🚀 Future Improvements

* Add modulus `%` operation
* Add power `**` operation
* Store the complete calculation, such as `20 + 10 = 30`
* Retrieve previous calculations from Firebase
* Create a GUI using Tkinter or CustomTkinter
* Add calculation history
* Add better exception handling
* Deploy the application

## 👨‍💻 Author

**Pranay Vishwanath Jadhao**

* 📧 Email: [pranayvjadhao@gmail.com](mailto:pranayvjadhao@gmail.com)
* 💼 LinkedIn: [www.linkedin.com/in/pranayjadhao](http://www.linkedin.com/in/pranayjadhao)
* 💻 GitHub: https://github.com/

## 📄 License

This project is created for **learning and educational purposes**.
