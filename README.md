# Recruitment Task

## Project setup

### Requirements
- **Python 3.10+** 
- **Git**

### 1. Clone the repository
```bash
git clone https://github.com/HyeroDrimm/Cloudefide-Recruitment-Task.git
cd Cloudefide-Recruitment-Task
```

### 2. Create a virtual environment
```bash
python -m venv .venv
```

### 3. Activate it
- Windows (PowerShell): `.venv\Scripts\Activate.ps1`
- Windows (cmd): `.venv\Scripts\activate.bat`
- Linux / macOS: `source .venv/bin/activate`

### 4. Install the requirements
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Run the tests
```bash
python -m unittest -v
```

### 6. Run pipeline
```bash
python pipeline.py
```

## Equation parser
I assumed the best possible scenario that anyone with access to function "add_virtual_column" is not malicious because eval can be used for code injection. If there was a need for something safer I could implement expression tree.

## Cleaning decisions
- I didn't drop rows with negative Quantity, there were 6 of them. I concluded that they may be returns of orders. In actual job I would inquire what that would mean from where the data came.
- I filled the unit costs for 4 missing values for "Keyboard" and "Printing paper" based on their prices in other rows (89 and 21 respectively), only after checking if every keyboard and printing paper had the same price.
- There was a suspicious outliers that were larger than 1000, when rest values are lower than 100. I decided to leave them since they had the same, consistent formating with space seperating thousnds.

### Renaming columns
- Quantity column was named "Quantity " with a space at the end of it. I renamed it to Quantity for the easier usage.
- Replaced all spaces in column names for floors for ease of use (for example in eval)

### Removing Rows 
- There was an additional header row. I removed it.
- There was a row with total sum of Quantity and Discount. It was removed

### Cleaning up values
- Regions values had varying upper and lower cases of letters and white symbols. I used strip and capitalize to make them uniform.
- In Quantity there were numbers that used spaces as thousands separators, which prevented converting them to numbers from string. I removed all spaces from Quantity values.
- Unit price values had values that had commas as decimal separators instead of dot. Replaced all commas for dots.
- Discount values that were NAN were replaced with 0 for easier calculations.

### Parsing to correct types
- Quantity, Unit Price and Discount were parsed to numeric types
- Order date was parsed for datetime type.

## Calculating revenue
I decided to round values in revenue to avoid floating point errors. Is pretty important when it comes to money to keep very accurate account.

## AI usage
As form of exercise generative AI was used only in capacity of search engine. AI didn't write any code, all code was written by me.