# Equation Generator - Pre-Algebra Practice

A Python program that generates 10,000 progressively challenging pre-algebra math equations and creates two beautifully formatted PDF files: one with equations for practice and one with complete answers.

## Features

- **10,000 Unique Equations**: Generates a comprehensive set of math problems covering the entire pre-algebra syllabus
- **Progressive Difficulty**: Questions are organized in 15 stages, starting from basic arithmetic and progressing to complex geometry and probability
- **Two Styled PDFs**: Creates separate, professionally formatted PDFs for equations and answers
- **Reproducible Results**: Uses random seed generation for reproducibility
- **Comprehensive Coverage**: Covers 9 major mathematical units

## Topics Covered

### Unit 1: Fundamentals of Real Numbers
- Addition and subtraction of integers
- Multiplication and division
- Order of operations (PEMDAS)
- Absolute value
- Square roots

### Unit 2: Fractions and Decimals
- Adding and multiplying fractions
- Decimal operations
- Simplifying fractions

### Unit 3: Expressions and Properties
- Evaluating algebraic expressions
- Distributive property
- Combining like terms

### Unit 4: Solving Equations
- One-step equations (addition/subtraction and multiplication/division)
- Two-step equations
- Variables on both sides
- Equations with distribution
- Equations with fractions

### Unit 5: Ratios, Proportions, and Percentages
- Simplifying ratios
- Solving proportions
- Percentage calculations
- Simple interest problems

### Unit 6: Exponents
- Basic exponent evaluation
- Exponent properties
- Negative and zero exponents
- Scientific notation

### Unit 7: Linear Functions
- Coordinate plane
- Slope calculations
- Linear equations in slope-intercept form

### Unit 8: Geometry
- Angle relationships (complementary, supplementary, vertical angles)
- Perimeter and area (rectangles, squares, triangles)
- Circle circumference and area
- Pythagorean theorem
- Volume (rectangular prisms, cylinders, cubes)

### Unit 9: Data and Probability
- Mean, median, mode, and range
- Basic probability

## Requirements

- Python 3.x
- ReportLab library

## Installation

1. Clone or download this repository

2. Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install reportlab
```

## Usage

Run the program from the command line:

```bash
python3 generate_equations.py
```

The program will:
1. Generate 10,000 progressively challenging equations
2. Display progress in the terminal
3. Create two timestamped PDF files:
   - `equations_YYYYMMDD_HHMMSS.pdf` - Practice equations
   - `answers_YYYYMMDD_HHMMSS.pdf` - Complete answer key

## Example Output

```
======================================================================
EQUATION GENERATOR - Pre-Algebra Practice
======================================================================

Generating 10,000 progressively challenging equations...
✓ Generated 10000 equations
  Seed used: 427851

Creating stylish PDF files...
✓ Created: equations_20231220_143052.pdf
✓ Created: answers_20231220_143052.pdf

======================================================================
COMPLETE!
======================================================================

Equations PDF: equations_20231220_143052.pdf
Answers PDF:   answers_20231220_143052.pdf

Each time you run this script, new random equations will be generated
following the same progressive difficulty curve based on the syllabus.
```

## How It Works

### Progression System

The program divides the 10,000 equations into 15 stages, with difficulty increasing gradually:

- **Stage 1 (Equations 1-500)**: Basic arithmetic
- **Stage 2 (501-1200)**: Advanced arithmetic and square roots
- **Stage 3 (1201-2000)**: Introduction to fractions
- **Stage 4 (2001-3000)**: Advanced fractions and decimals
- **Stage 5 (3001-4000)**: Basic algebraic expressions
- **Stage 6 (4001-4800)**: Advanced expressions
- **Stage 7 (4801-5600)**: One-step equations
- **Stage 8 (5601-6500)**: Two-step equations
- **Stage 9 (6501-7200)**: Variables on both sides
- **Stage 10 (7201-7800)**: Distribution in equations
- **Stage 11 (7801-8400)**: Ratios and proportions
- **Stage 12 (8401-9000)**: Exponents
- **Stage 13 (9001-9500)**: Linear functions
- **Stage 14 (9501-9800)**: Geometry
- **Stage 15 (9801-10000)**: Mixed final review

### PDF Formatting

- Professional layout with color-coded headers
- 50 equations per page in organized tables
- Alternating row colors for easy reading
- Timestamp on each document
- Different styling for equations vs. answers

### Randomization

Each run generates new random equations while maintaining the same difficulty progression. The seed value is displayed so you can regenerate the same set if needed.

## Customization

You can modify the program to:
- Change the total number of equations (modify the `count` parameter in `generate_equation_set()`)
- Adjust difficulty ranges for specific topics
- Modify the progression stages
- Customize PDF styling (colors, fonts, layout)

## Use Cases

- **Teachers**: Generate unique practice worksheets for students
- **Students**: Create custom practice sets for exam preparation
- **Tutors**: Provide varied homework assignments
- **Homeschooling**: Generate comprehensive math practice materials

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to submit issues or pull requests to improve the equation generator or add new problem types.
