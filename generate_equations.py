#!/usr/bin/env python3
"""
Equation Generator - Creates 10,000 progressively challenging math equations
Generates two stylish PDFs: one with equations, one with answers
"""

import random
import math
from fractions import Fraction
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas


class EquationGenerator:
    """Generates progressively challenging equations based on pre-algebra syllabus"""

    def __init__(self, seed=None):
        """Initialize with optional seed for reproducibility"""
        if seed is None:
            seed = random.randint(0, 1000000)
        random.seed(seed)
        self.seed = seed
        self.equations = []
        self.answers = []

    def gcd(self, a, b):
        """Greatest common divisor"""
        while b:
            a, b = b, a % b
        return a

    def simplify_fraction(self, num, den):
        """Simplify a fraction"""
        if den == 0:
            return num, 1
        g = self.gcd(abs(num), abs(den))
        return num // g, den // g

    def format_fraction(self, num, den):
        """Format fraction as string"""
        num, den = self.simplify_fraction(num, den)
        if den == 1:
            return str(num)
        if den == -1:
            return str(-num)
        if den < 0:
            num, den = -num, -den
        return f"{num}/{den}"

    def eval_equation(self, expr, x_val):
        """Safely evaluate equation with given x value"""
        return eval(expr.replace('x', str(x_val)))

    # ===== UNIT 1: FUNDAMENTALS OF REAL NUMBERS =====

    def generate_addition_subtraction(self, difficulty):
        """Basic addition and subtraction of integers"""
        if difficulty <= 1:
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            eq = f"{a} + {b}"
            ans = a + b
        elif difficulty == 2:
            a = random.randint(-20, 20)
            b = random.randint(1, 20)
            eq = f"{a} + {b}"
            ans = a + b
        else:
            a = random.randint(-50, 50)
            b = random.randint(-50, 50)
            c = random.randint(-50, 50)
            eq = f"{a} + {b} - {c}"
            ans = a + b - c

        return eq, str(ans)

    def generate_multiplication_division(self, difficulty):
        """Basic multiplication and division of integers"""
        if difficulty <= 1:
            a = random.randint(2, 12)
            b = random.randint(2, 12)
            eq = f"{a} × {b}"
            ans = a * b
        elif difficulty == 2:
            a = random.randint(2, 12)
            b = random.randint(2, 12)
            result = a * b
            eq = f"{result} ÷ {a}"
            ans = b
        else:
            a = random.randint(-12, 12)
            b = random.randint(-12, 12)
            if b == 0:
                b = random.randint(1, 12)
            eq = f"{a} × {b}"
            ans = a * b

        return eq, str(ans)

    def generate_pemdas(self, difficulty):
        """Order of operations problems"""
        if difficulty <= 1:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            eq = f"{a} + {b} × {c}"
            ans = a + b * c
        elif difficulty == 2:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            eq = f"({a} + {b}) × {c}"
            ans = (a + b) * c
        else:
            a = random.randint(2, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 5)
            d = random.randint(1, 10)
            eq = f"{a}² + {b} × {c} - {d}"
            ans = a**2 + b * c - d

        return eq, str(ans)

    def generate_absolute_value(self, difficulty):
        """Absolute value problems"""
        if difficulty <= 1:
            a = random.randint(-20, 20)
            eq = f"|{a}|"
            ans = abs(a)
        elif difficulty == 2:
            a = random.randint(-20, 20)
            b = random.randint(-20, 20)
            eq = f"|{a}| + |{b}|"
            ans = abs(a) + abs(b)
        else:
            a = random.randint(-20, 20)
            b = random.randint(-20, 20)
            eq = f"|{a} - {b}|"
            ans = abs(a - b)

        return eq, str(ans)

    def generate_square_roots(self, difficulty):
        """Square root problems"""
        perfect_squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]

        if difficulty <= 1:
            sq = random.choice(perfect_squares[:9])
            eq = f"√{sq}"
            ans = int(math.sqrt(sq))
        elif difficulty == 2:
            sq = random.choice(perfect_squares)
            eq = f"√{sq}"
            ans = int(math.sqrt(sq))
        else:
            sq1 = random.choice(perfect_squares[:9])
            sq2 = random.choice(perfect_squares[:9])
            eq = f"√{sq1} + √{sq2}"
            ans = int(math.sqrt(sq1) + math.sqrt(sq2))

        return eq, str(ans)

    # ===== UNIT 2: FRACTIONS AND DECIMALS =====

    def generate_fraction_addition(self, difficulty):
        """Adding fractions"""
        if difficulty <= 1:
            # Like denominators
            den = random.randint(2, 12)
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            eq = f"{num1}/{den} + {num2}/{den}"
            ans = self.format_fraction(num1 + num2, den)
        elif difficulty == 2:
            # Unlike denominators (one is multiple of other)
            den1 = random.choice([2, 3, 4, 5])
            den2 = den1 * random.randint(2, 3)
            num1 = random.randint(1, 5)
            num2 = random.randint(1, 8)
            eq = f"{num1}/{den1} + {num2}/{den2}"
            # Find common denominator
            lcm = (den1 * den2) // self.gcd(den1, den2)
            result_num = num1 * (lcm // den1) + num2 * (lcm // den2)
            ans = self.format_fraction(result_num, lcm)
        else:
            # Any unlike denominators
            den1 = random.randint(2, 8)
            den2 = random.randint(2, 8)
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            eq = f"{num1}/{den1} + {num2}/{den2}"
            lcm = (den1 * den2) // self.gcd(den1, den2)
            result_num = num1 * (lcm // den1) + num2 * (lcm // den2)
            ans = self.format_fraction(result_num, lcm)

        return eq, ans

    def generate_fraction_multiplication(self, difficulty):
        """Multiplying fractions"""
        if difficulty <= 1:
            num1 = random.randint(1, 6)
            den1 = random.randint(2, 8)
            num2 = random.randint(1, 6)
            den2 = random.randint(2, 8)
            eq = f"{num1}/{den1} × {num2}/{den2}"
            ans = self.format_fraction(num1 * num2, den1 * den2)
        elif difficulty == 2:
            num1 = random.randint(1, 12)
            den1 = random.randint(2, 12)
            num2 = random.randint(-12, 12)
            den2 = random.randint(2, 12)
            eq = f"{num1}/{den1} × {num2}/{den2}"
            ans = self.format_fraction(num1 * num2, den1 * den2)
        else:
            # Division
            num1 = random.randint(1, 10)
            den1 = random.randint(2, 10)
            num2 = random.randint(1, 10)
            den2 = random.randint(2, 10)
            eq = f"{num1}/{den1} ÷ {num2}/{den2}"
            ans = self.format_fraction(num1 * den2, den1 * num2)

        return eq, ans

    def generate_decimal_operations(self, difficulty):
        """Decimal operations"""
        if difficulty <= 1:
            a = round(random.uniform(0.1, 10), 2)
            b = round(random.uniform(0.1, 10), 2)
            eq = f"{a} + {b}"
            ans = round(a + b, 2)
        elif difficulty == 2:
            a = round(random.uniform(0.1, 100), 2)
            b = round(random.uniform(0.1, 100), 2)
            eq = f"{a} - {b}"
            ans = round(a - b, 2)
        else:
            a = round(random.uniform(0.1, 10), 2)
            b = round(random.uniform(0.1, 10), 2)
            eq = f"{a} × {b}"
            ans = round(a * b, 2)

        return eq, str(ans)

    # ===== UNIT 3: EXPRESSIONS AND PROPERTIES =====

    def generate_evaluate_expression(self, difficulty):
        """Evaluate algebraic expressions"""
        x_val = random.randint(1, 10)

        if difficulty <= 1:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            eq = f"Evaluate: {a}x + {b} when x = {x_val}"
            ans = a * x_val + b
        elif difficulty == 2:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            eq = f"Evaluate: {a}x² + {b}x + {c} when x = {x_val}"
            ans = a * x_val**2 + b * x_val + c
        else:
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            eq = f"Evaluate: {a}x² - {b}x when x = {x_val}"
            ans = a * x_val**2 - b * x_val

        return eq, str(ans)

    def generate_distributive_property(self, difficulty):
        """Distributive property simplification"""
        if difficulty <= 1:
            a = random.randint(2, 8)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            eq = f"Simplify: {a}(x + {b})"
            ans = f"{a}x + {a * b}"
        elif difficulty == 2:
            a = random.randint(2, 8)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            eq = f"Simplify: {a}(x - {b})"
            ans = f"{a}x - {a * b}"
        else:
            a = random.randint(-8, 8)
            if a == 0:
                a = random.randint(2, 8)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            eq = f"Simplify: {a}({b}x + {c})"
            ans = f"{a * b}x + {a * c}"

        return eq, ans

    def generate_combine_like_terms(self, difficulty):
        """Combining like terms"""
        if difficulty <= 1:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            eq = f"Simplify: {a}x + {b}x + {c}"
            ans = f"{a + b}x + {c}"
        elif difficulty == 2:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            d = random.randint(1, 10)
            eq = f"Simplify: {a}x + {b} + {c}x - {d}"
            ans = f"{a + c}x + {b - d}"
        else:
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            c = random.randint(-10, 10)
            d = random.randint(-10, 10)
            eq = f"Simplify: {a}x² + {b}x + {c}x² - {d}x"
            ans = f"{a + c}x² + {b - d}x"

        return eq, ans

    # ===== UNIT 4: SOLVING EQUATIONS =====

    def generate_one_step_addition(self, difficulty):
        """One-step equations with addition/subtraction"""
        if difficulty <= 1:
            solution = random.randint(1, 20)
            b = random.randint(1, 20)
            eq = f"x + {b} = {solution + b}"
            ans = solution
        elif difficulty == 2:
            solution = random.randint(-20, 20)
            b = random.randint(1, 20)
            eq = f"x - {b} = {solution - b}"
            ans = solution
        else:
            solution = random.randint(-30, 30)
            b = random.randint(-30, 30)
            eq = f"x + {b} = {solution + b}"
            ans = solution

        return eq, f"x = {ans}"

    def generate_one_step_multiplication(self, difficulty):
        """One-step equations with multiplication/division"""
        if difficulty <= 1:
            solution = random.randint(1, 15)
            a = random.randint(2, 10)
            eq = f"{a}x = {a * solution}"
            ans = solution
        elif difficulty == 2:
            solution = random.randint(-15, 15)
            a = random.randint(2, 10)
            eq = f"{a}x = {a * solution}"
            ans = solution
        else:
            solution = random.randint(-20, 20)
            a = random.randint(-10, 10)
            if a == 0:
                a = random.randint(2, 10)
            eq = f"{a}x = {a * solution}"
            ans = solution

        return eq, f"x = {ans}"

    def generate_two_step_equation(self, difficulty):
        """Two-step equations"""
        if difficulty <= 1:
            solution = random.randint(1, 15)
            a = random.randint(2, 8)
            b = random.randint(1, 15)
            eq = f"{a}x + {b} = {a * solution + b}"
            ans = solution
        elif difficulty == 2:
            solution = random.randint(-15, 15)
            a = random.randint(2, 8)
            b = random.randint(-15, 15)
            eq = f"{a}x - {b} = {a * solution - b}"
            ans = solution
        else:
            solution = random.randint(-20, 20)
            a = random.randint(-10, 10)
            if a == 0:
                a = random.randint(2, 8)
            b = random.randint(-20, 20)
            eq = f"{a}x + {b} = {a * solution + b}"
            ans = solution

        return eq, f"x = {ans}"

    def generate_variables_both_sides(self, difficulty):
        """Equations with variables on both sides"""
        if difficulty <= 1:
            solution = random.randint(1, 15)
            a = random.randint(2, 8)
            b = random.randint(1, 8)
            c = random.randint(1, 15)
            # ax + c = bx + d, where a > b
            if a <= b:
                a, b = b + 1, a
            d = b * solution + c - a * solution
            eq = f"{a}x + {c} = {b}x + {d}"
            ans = solution
        elif difficulty == 2:
            solution = random.randint(-15, 15)
            a = random.randint(3, 10)
            b = random.randint(1, 5)
            c = random.randint(-15, 15)
            d = b * solution + c - a * solution
            eq = f"{a}x + {c} = {b}x + {d}"
            ans = solution
        else:
            solution = random.randint(-20, 20)
            a = random.randint(2, 12)
            b = random.randint(1, 8)
            c = random.randint(-25, 25)
            d = b * solution + c - a * solution
            eq = f"{a}x - {c} = {b}x - {d}"
            ans = solution

        return eq, f"x = {ans}"

    def generate_distributive_equation(self, difficulty):
        """Equations requiring distribution"""
        if difficulty <= 1:
            solution = random.randint(1, 12)
            a = random.randint(2, 6)
            b = random.randint(1, 10)
            result = a * solution - a * b
            eq = f"{a}(x - {b}) = {result}"
            ans = solution
        elif difficulty == 2:
            solution = random.randint(-12, 12)
            a = random.randint(2, 6)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            result = a * solution + a * b + c
            eq = f"{a}(x + {b}) + {c} = {result}"
            ans = solution
        else:
            solution = random.randint(-15, 15)
            a = random.randint(2, 6)
            b = random.randint(1, 10)
            c = random.randint(2, 6)
            d = random.randint(1, 10)
            # a(x + b) = c(x - d)
            result = c * solution - c * d
            left_result = a * solution + a * b
            if left_result == result:
                eq = f"{a}(x + {b}) = {c}x - {c * d}"
            else:
                eq = f"{a}(x - {b}) = {a * solution - a * b}"
            ans = solution

        return eq, f"x = {ans}"

    def generate_fraction_equation(self, difficulty):
        """Equations with fractions"""
        if difficulty <= 1:
            solution = random.randint(2, 20)
            den = random.choice([2, 3, 4, 5])
            # Make sure solution * den works nicely
            b = random.randint(1, 15)
            eq = f"x/{den} + {b} = {solution // den + b}"
            ans = solution
        elif difficulty == 2:
            solution = random.randint(-20, 20)
            num = random.randint(2, 8)
            den = random.choice([2, 3, 4, 5])
            b = random.randint(1, 15)
            result = (num * solution) // den + b
            eq = f"{num}x/{den} + {b} = {result}"
            ans = solution
        else:
            solution = random.randint(-15, 15)
            num = random.randint(2, 6)
            den = random.choice([2, 3, 4])
            b = random.randint(-10, 10)
            result = (num * solution) // den - b
            eq = f"{num}x/{den} - {b} = {result}"
            ans = solution

        return eq, f"x = {ans}"

    # ===== UNIT 5: RATIOS, PROPORTIONS, AND PERCENTAGES =====

    def generate_ratio(self, difficulty):
        """Ratio problems"""
        if difficulty <= 1:
            a = random.randint(1, 12)
            b = random.randint(1, 12)
            eq = f"Simplify ratio {a * 2}:{b * 2}"
            g = self.gcd(a * 2, b * 2)
            ans = f"{(a * 2) // g}:{(b * 2) // g}"
        elif difficulty == 2:
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            c = random.randint(1, 20)
            eq = f"Simplify ratio {a}:{b}:{c}"
            g = self.gcd(self.gcd(a, b), c)
            ans = f"{a // g}:{b // g}:{c // g}"
        else:
            # Unit rate
            distance = random.randint(100, 500)
            time = random.choice([2, 4, 5, 10])
            eq = f"Find unit rate: {distance} miles in {time} hours"
            ans = f"{distance // time} mph"

        return eq, ans

    def generate_proportion(self, difficulty):
        """Solve proportions"""
        if difficulty <= 1:
            a = random.randint(2, 12)
            b = random.randint(2, 12)
            solution = random.randint(2, 20)
            c = a * solution // b
            eq = f"{a}/{b} = x/{c}"
            ans = solution
        elif difficulty == 2:
            a = random.randint(2, 15)
            b = random.randint(2, 15)
            solution = random.randint(3, 25)
            c = (a * solution) // b
            eq = f"x/{a} = {c}/{b}"
            ans = solution
        else:
            a = random.randint(2, 20)
            b = random.randint(2, 20)
            c = random.randint(2, 20)
            solution = (b * c) // a
            eq = f"{a}/{b} = {c}/x"
            ans = solution

        return eq, f"x = {ans}"

    def generate_percent(self, difficulty):
        """Percentage problems"""
        if difficulty <= 1:
            percent = random.choice([10, 20, 25, 50, 75])
            of_value = random.randint(20, 200)
            eq = f"Find {percent}% of {of_value}"
            ans = (percent * of_value) // 100
        elif difficulty == 2:
            percent = random.randint(5, 95)
            of_value = random.randint(50, 500)
            eq = f"What is {percent}% of {of_value}?"
            ans = round((percent * of_value) / 100, 2)
        else:
            # Percent of change
            original = random.randint(50, 200)
            change = random.randint(10, 50)
            new_value = original + change
            eq = f"Find percent increase from {original} to {new_value}"
            ans = f"{round((change / original) * 100, 1)}%"

        return eq, str(ans)

    def generate_simple_interest(self, difficulty):
        """Simple interest problems"""
        principal = random.randint(100, 5000)
        rate = random.choice([2, 3, 4, 5, 6, 7, 8])
        time = random.randint(1, 10)

        if difficulty <= 1:
            eq = f"I = Prt. Find I when P = ${principal}, r = {rate}%, t = {time} years"
            interest = (principal * rate * time) // 100
            ans = f"${interest}"
        elif difficulty == 2:
            interest = (principal * rate * time) // 100
            total = principal + interest
            eq = f"Find total amount: P = ${principal}, r = {rate}%, t = {time} years"
            ans = f"${total}"
        else:
            interest = (principal * rate * time) // 100
            eq = f"Find rate: P = ${principal}, I = ${interest}, t = {time} years"
            ans = f"{rate}%"

        return eq, ans

    # ===== UNIT 6: EXPONENTS =====

    def generate_exponent_basic(self, difficulty):
        """Basic exponent evaluation"""
        if difficulty <= 1:
            base = random.randint(2, 10)
            exp = random.randint(2, 4)
            eq = f"{base}^{exp}"
            ans = base ** exp
        elif difficulty == 2:
            base = random.randint(-5, 5)
            if base == 0:
                base = random.randint(2, 8)
            exp = random.randint(2, 3)
            eq = f"({base})^{exp}"
            ans = base ** exp
        else:
            base = random.randint(2, 8)
            exp1 = random.randint(2, 3)
            exp2 = random.randint(2, 3)
            eq = f"{base}^{exp1} × {base}^{exp2}"
            ans = base ** (exp1 + exp2)

        return eq, str(ans)

    def generate_exponent_properties(self, difficulty):
        """Exponent properties"""
        base = random.randint(2, 10)

        if difficulty <= 1:
            exp1 = random.randint(3, 8)
            exp2 = random.randint(2, 5)
            if exp1 <= exp2:
                exp1, exp2 = exp2 + 1, exp1
            eq = f"Simplify: x^{exp1} ÷ x^{exp2}"
            ans = f"x^{exp1 - exp2}"
        elif difficulty == 2:
            exp1 = random.randint(2, 5)
            exp2 = random.randint(2, 4)
            eq = f"Simplify: (x^{exp1})^{exp2}"
            ans = f"x^{exp1 * exp2}"
        else:
            exp = random.randint(2, 6)
            eq = f"Simplify: (xy)^{exp}"
            ans = f"x^{exp}y^{exp}"

        return eq, ans

    def generate_negative_exponents(self, difficulty):
        """Negative and zero exponents"""
        base = random.randint(2, 10)

        if difficulty <= 1:
            eq = f"{base}^0"
            ans = "1"
        elif difficulty == 2:
            exp = random.randint(1, 4)
            eq = f"{base}^(-{exp})"
            ans = f"1/{base**exp}"
        else:
            exp = random.randint(2, 4)
            eq = f"Simplify: x^(-{exp})"
            ans = f"1/x^{exp}"

        return eq, ans

    def generate_scientific_notation(self, difficulty):
        """Scientific notation"""
        if difficulty <= 1:
            coef = round(random.uniform(1, 9.9), 1)
            exp = random.randint(1, 6)
            eq = f"Write in standard form: {coef} × 10^{exp}"
            ans = str(int(coef * (10 ** exp)))
        elif difficulty == 2:
            num = random.randint(1000, 999999)
            eq = f"Write in scientific notation: {num}"
            # Count digits
            digits = len(str(num))
            coef = num / (10 ** (digits - 1))
            ans = f"{coef} × 10^{digits - 1}"
        else:
            coef1 = round(random.uniform(1, 9), 1)
            coef2 = round(random.uniform(1, 9), 1)
            exp1 = random.randint(2, 5)
            exp2 = random.randint(2, 5)
            eq = f"Multiply: ({coef1} × 10^{exp1})({coef2} × 10^{exp2})"
            result_coef = coef1 * coef2
            result_exp = exp1 + exp2
            if result_coef >= 10:
                result_coef /= 10
                result_exp += 1
            ans = f"{result_coef} × 10^{result_exp}"

        return eq, ans

    # ===== UNIT 7: LINEAR FUNCTIONS =====

    def generate_coordinate_plane(self, difficulty):
        """Coordinate plane problems"""
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)

        if difficulty <= 1:
            eq = f"What quadrant contains ({x}, {y})?"
            if x > 0 and y > 0:
                ans = "Quadrant I"
            elif x < 0 and y > 0:
                ans = "Quadrant II"
            elif x < 0 and y < 0:
                ans = "Quadrant III"
            elif x > 0 and y < 0:
                ans = "Quadrant IV"
            else:
                ans = "On an axis"
        elif difficulty == 2:
            x2 = random.randint(-10, 10)
            eq = f"Find distance between ({x}, 0) and ({x2}, 0)"
            ans = abs(x - x2)
        else:
            y2 = random.randint(-10, 10)
            eq = f"Find midpoint of ({x}, {y}) and ({x}, {y2})"
            ans = f"({x}, {(y + y2) / 2})"

        return eq, str(ans)

    def generate_slope(self, difficulty):
        """Slope calculations"""
        if difficulty <= 1:
            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            m = random.randint(1, 5)
            run = random.randint(1, 4)
            x2 = x1 + run
            y2 = y1 + m * run
            eq = f"Find slope between ({x1}, {y1}) and ({x2}, {y2})"
            ans = m
        elif difficulty == 2:
            x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
            x2, y2 = random.randint(-10, 10), random.randint(-10, 10)
            if x2 == x1:
                x2 += random.randint(1, 5)
            eq = f"Find slope: ({x1}, {y1}) and ({x2}, {y2})"
            slope = (y2 - y1) / (x2 - x1)
            if slope == int(slope):
                ans = int(slope)
            else:
                ans = f"{y2 - y1}/{x2 - x1}"
        else:
            m = random.randint(-5, 5)
            b = random.randint(-10, 10)
            eq = f"Find slope of y = {m}x + {b}"
            ans = m

        return eq, str(ans)

    def generate_linear_equation(self, difficulty):
        """Linear equations in slope-intercept form"""
        m = random.randint(-5, 5)
        b = random.randint(-10, 10)

        if difficulty <= 1:
            x = random.randint(1, 10)
            eq = f"Find y when x = {x} in y = {m}x + {b}"
            ans = m * x + b
        elif difficulty == 2:
            y = random.randint(-20, 20)
            # mx + b = y, solve for x
            if m == 0:
                m = random.randint(1, 5)
            x = (y - b) // m
            actual_y = m * x + b
            eq = f"Find x when y = {actual_y} in y = {m}x + {b}"
            ans = x
        else:
            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            m = random.randint(1, 5)
            b = y1 - m * x1
            eq = f"Write equation: slope = {m}, passes through ({x1}, {y1})"
            ans = f"y = {m}x + {b}"

        return eq, str(ans)

    # ===== UNIT 8: GEOMETRY =====

    def generate_angle_relationships(self, difficulty):
        """Angle relationships"""
        if difficulty <= 1:
            angle = random.randint(10, 80)
            eq = f"Find complement of {angle}°"
            ans = f"{90 - angle}°"
        elif difficulty == 2:
            angle = random.randint(10, 170)
            eq = f"Find supplement of {angle}°"
            ans = f"{180 - angle}°"
        else:
            # Vertical angles
            angle = random.randint(30, 150)
            eq = f"If two vertical angles are equal and one is {angle}°, find the other"
            ans = f"{angle}°"

        return eq, ans

    def generate_perimeter_area(self, difficulty):
        """Perimeter and area"""
        if difficulty <= 1:
            length = random.randint(5, 20)
            width = random.randint(3, 15)
            eq = f"Find area of rectangle: length = {length}, width = {width}"
            ans = length * width
        elif difficulty == 2:
            side = random.randint(5, 20)
            eq = f"Find perimeter of square with side {side}"
            ans = 4 * side
        else:
            base = random.randint(5, 20)
            height = random.randint(4, 15)
            eq = f"Find area of triangle: base = {base}, height = {height}"
            ans = (base * height) / 2

        return eq, str(ans)

    def generate_circle_problems(self, difficulty):
        """Circle circumference and area"""
        radius = random.randint(3, 15)

        if difficulty <= 1:
            eq = f"Find circumference: radius = {radius} (use π ≈ 3.14)"
            ans = round(2 * 3.14 * radius, 2)
        elif difficulty == 2:
            eq = f"Find area of circle: radius = {radius} (use π ≈ 3.14)"
            ans = round(3.14 * radius ** 2, 2)
        else:
            diameter = radius * 2
            eq = f"Find area: diameter = {diameter} (use π ≈ 3.14)"
            ans = round(3.14 * radius ** 2, 2)

        return eq, str(ans)

    def generate_pythagorean(self, difficulty):
        """Pythagorean theorem"""
        # Use Pythagorean triples for cleaner answers
        triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]

        if difficulty <= 1:
            a, b, c = random.choice(triples[:2])
            eq = f"Find c: a = {a}, b = {b} (a² + b² = c²)"
            ans = c
        elif difficulty == 2:
            a, b, c = random.choice(triples)
            eq = f"Find hypotenuse: legs are {a} and {b}"
            ans = c
        else:
            a, b, c = random.choice(triples)
            eq = f"Find leg: hypotenuse = {c}, other leg = {a}"
            ans = b

        return eq, str(ans)

    def generate_volume(self, difficulty):
        """Volume problems"""
        if difficulty <= 1:
            l = random.randint(3, 10)
            w = random.randint(3, 10)
            h = random.randint(3, 10)
            eq = f"Find volume of rectangular prism: l={l}, w={w}, h={h}"
            ans = l * w * h
        elif difficulty == 2:
            r = random.randint(2, 8)
            h = random.randint(5, 15)
            eq = f"Find volume of cylinder: r={r}, h={h} (V=πr²h, π≈3.14)"
            ans = round(3.14 * r**2 * h, 2)
        else:
            s = random.randint(3, 12)
            eq = f"Find volume of cube: side = {s}"
            ans = s ** 3

        return eq, str(ans)

    # ===== UNIT 9: DATA AND PROBABILITY =====

    def generate_mean_median(self, difficulty):
        """Mean, median, mode"""
        if difficulty <= 1:
            data = [random.randint(1, 20) for _ in range(5)]
            eq = f"Find mean: {data}"
            ans = sum(data) / len(data)
        elif difficulty == 2:
            data = sorted([random.randint(1, 30) for _ in range(7)])
            eq = f"Find median: {data}"
            ans = data[len(data) // 2]
        else:
            data = [random.randint(1, 50) for _ in range(10)]
            eq = f"Find range: {data}"
            ans = max(data) - min(data)

        return eq, str(ans)

    def generate_probability(self, difficulty):
        """Probability problems"""
        if difficulty <= 1:
            favorable = random.randint(1, 5)
            total = random.randint(favorable + 1, 12)
            eq = f"Probability: {favorable} favorable outcomes out of {total} total"
            ans = self.format_fraction(favorable, total)
        elif difficulty == 2:
            # Coin flip
            eq = "Probability of getting heads on a fair coin"
            ans = "1/2"
        else:
            # Dice
            outcomes = random.randint(1, 6)
            eq = f"Probability of rolling ≤ {outcomes} on standard die"
            ans = self.format_fraction(outcomes, 6)

        return eq, ans

    # ===== MAIN GENERATION LOGIC =====

    def generate_equation_set(self, count=10000):
        """Generate a complete set of progressively challenging equations"""

        # Define progression stages
        stages = [
            # Stage 1: Basic arithmetic (equations 1-1000)
            {
                'range': (0, 500),
                'generators': [
                    (self.generate_addition_subtraction, [1, 1, 2]),
                    (self.generate_multiplication_division, [1, 1, 2]),
                    (self.generate_pemdas, [1, 1, 1]),
                    (self.generate_absolute_value, [1, 1, 1]),
                ]
            },
            # Stage 2: More arithmetic + square roots (equations 501-1200)
            {
                'range': (500, 1200),
                'generators': [
                    (self.generate_addition_subtraction, [2, 3, 3]),
                    (self.generate_multiplication_division, [2, 3, 3]),
                    (self.generate_pemdas, [2, 2, 2]),
                    (self.generate_square_roots, [1, 1, 2]),
                ]
            },
            # Stage 3: Fractions introduction (equations 1201-2000)
            {
                'range': (1200, 2000),
                'generators': [
                    (self.generate_pemdas, [3, 3, 3]),
                    (self.generate_square_roots, [2, 2, 3]),
                    (self.generate_fraction_addition, [1, 1, 1]),
                    (self.generate_fraction_multiplication, [1, 1, 1]),
                    (self.generate_decimal_operations, [1, 1, 2]),
                ]
            },
            # Stage 4: Advanced fractions + decimals (equations 2001-3000)
            {
                'range': (2000, 3000),
                'generators': [
                    (self.generate_fraction_addition, [2, 2, 3]),
                    (self.generate_fraction_multiplication, [2, 2, 3]),
                    (self.generate_decimal_operations, [2, 3, 3]),
                ]
            },
            # Stage 5: Expressions and evaluation (equations 3001-4000)
            {
                'range': (3000, 4000),
                'generators': [
                    (self.generate_evaluate_expression, [1, 1, 2]),
                    (self.generate_distributive_property, [1, 1, 2]),
                    (self.generate_combine_like_terms, [1, 1, 2]),
                ]
            },
            # Stage 6: Advanced expressions (equations 4001-4800)
            {
                'range': (4000, 4800),
                'generators': [
                    (self.generate_evaluate_expression, [2, 2, 3]),
                    (self.generate_distributive_property, [2, 2, 3]),
                    (self.generate_combine_like_terms, [2, 2, 3]),
                ]
            },
            # Stage 7: One-step equations (equations 4801-5600)
            {
                'range': (4800, 5600),
                'generators': [
                    (self.generate_one_step_addition, [1, 2, 2]),
                    (self.generate_one_step_multiplication, [1, 2, 2]),
                ]
            },
            # Stage 8: Two-step equations (equations 5601-6500)
            {
                'range': (5600, 6500),
                'generators': [
                    (self.generate_one_step_addition, [3, 3, 3]),
                    (self.generate_one_step_multiplication, [3, 3, 3]),
                    (self.generate_two_step_equation, [1, 1, 2]),
                ]
            },
            # Stage 9: Variables on both sides (equations 6501-7200)
            {
                'range': (6500, 7200),
                'generators': [
                    (self.generate_two_step_equation, [2, 3, 3]),
                    (self.generate_variables_both_sides, [1, 1, 2]),
                ]
            },
            # Stage 10: Distribution in equations (equations 7201-7800)
            {
                'range': (7200, 7800),
                'generators': [
                    (self.generate_variables_both_sides, [2, 2, 3]),
                    (self.generate_distributive_equation, [1, 2, 2]),
                    (self.generate_fraction_equation, [1, 1, 1]),
                ]
            },
            # Stage 11: Ratios and proportions (equations 7801-8400)
            {
                'range': (7800, 8400),
                'generators': [
                    (self.generate_distributive_equation, [3, 3, 3]),
                    (self.generate_fraction_equation, [2, 2, 3]),
                    (self.generate_ratio, [1, 2, 2]),
                    (self.generate_proportion, [1, 2, 2]),
                    (self.generate_percent, [1, 2, 2]),
                ]
            },
            # Stage 12: Exponents (equations 8401-9000)
            {
                'range': (8400, 9000),
                'generators': [
                    (self.generate_simple_interest, [1, 2, 3]),
                    (self.generate_exponent_basic, [1, 2, 3]),
                    (self.generate_exponent_properties, [1, 2, 2]),
                    (self.generate_negative_exponents, [1, 2, 3]),
                    (self.generate_scientific_notation, [1, 1, 2]),
                ]
            },
            # Stage 13: Linear functions (equations 9001-9500)
            {
                'range': (9000, 9500),
                'generators': [
                    (self.generate_scientific_notation, [2, 3, 3]),
                    (self.generate_coordinate_plane, [1, 2, 3]),
                    (self.generate_slope, [1, 2, 3]),
                    (self.generate_linear_equation, [1, 2, 3]),
                ]
            },
            # Stage 14: Geometry (equations 9501-9800)
            {
                'range': (9500, 9800),
                'generators': [
                    (self.generate_angle_relationships, [1, 2, 3]),
                    (self.generate_perimeter_area, [1, 2, 3]),
                    (self.generate_circle_problems, [1, 2, 3]),
                    (self.generate_pythagorean, [1, 2, 3]),
                    (self.generate_volume, [1, 2, 3]),
                ]
            },
            # Stage 15: Final mixed review (equations 9801-10000)
            {
                'range': (9800, 10000),
                'generators': [
                    (self.generate_mean_median, [1, 2, 3]),
                    (self.generate_probability, [1, 2, 3]),
                    (self.generate_variables_both_sides, [3, 3, 3]),
                    (self.generate_distributive_equation, [3, 3, 3]),
                    (self.generate_linear_equation, [3, 3, 3]),
                    (self.generate_pythagorean, [3, 3, 3]),
                ]
            },
        ]

        equation_num = 1

        for stage in stages:
            start, end = stage['range']
            generators = stage['generators']

            while equation_num <= end and equation_num <= count:
                # Randomly select a generator
                generator, difficulties = random.choice(generators)
                difficulty = random.choice(difficulties)

                try:
                    eq, ans = generator(difficulty)
                    self.equations.append(f"{equation_num}. {eq}")
                    self.answers.append(f"{equation_num}. {ans}")
                    equation_num += 1
                except Exception as e:
                    # If generation fails, try again
                    continue

        return self.equations, self.answers


def create_pdf(filename, title, content_list, is_answers=False):
    """Create a stylish PDF with equations or answers"""
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=1*inch,
        bottomMargin=0.75*inch
    )

    # Container for the 'Flowable' objects
    elements = []

    # Define styles
    styles = getSampleStyleSheet()

    # Custom title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1a5490'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    # Custom subtitle style
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#666666'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    )

    # Custom equation style
    equation_style = ParagraphStyle(
        'EquationStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.black,
        leftIndent=0,
        fontName='Helvetica',
        leading=16
    )

    # Answer style (slightly different color)
    answer_style = ParagraphStyle(
        'AnswerStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#2c5282') if is_answers else colors.black,
        leftIndent=0,
        fontName='Helvetica-Bold' if is_answers else 'Helvetica',
        leading=16
    )

    # Add title
    elements.append(Paragraph(title, title_style))

    # Add generation date
    date_str = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    elements.append(Paragraph(f"Generated on {date_str}", subtitle_style))

    # Add horizontal line
    elements.append(Spacer(1, 0.2*inch))

    # Add content in organized sections
    items_per_page = 50

    for i in range(0, len(content_list), items_per_page):
        section = content_list[i:i+items_per_page]

        # Create table data
        table_data = []
        for item in section:
            # Use answer style for answer PDFs
            style = answer_style if is_answers else equation_style
            table_data.append([Paragraph(item, style)])

        # Create table
        t = Table(table_data, colWidths=[6.5*inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
        ]))

        elements.append(t)

        # Add page break if not last section
        if i + items_per_page < len(content_list):
            elements.append(PageBreak())

    # Build PDF
    doc.build(elements)


def main():
    """Main function to generate equations and create PDFs"""
    print("=" * 70)
    print("EQUATION GENERATOR - Pre-Algebra Practice")
    print("=" * 70)
    print()

    # Generate equations
    print("Generating 10,000 progressively challenging equations...")
    generator = EquationGenerator()
    equations, answers = generator.generate_equation_set(10000)

    print(f"✓ Generated {len(equations)} equations")
    print(f"  Seed used: {generator.seed}")
    print()

    # Create PDFs
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    equations_filename = f"equations_{timestamp}.pdf"
    answers_filename = f"answers_{timestamp}.pdf"

    print("Creating stylish PDF files...")

    # Create equations PDF
    create_pdf(
        equations_filename,
        "10,000 Pre-Algebra Practice Equations",
        equations,
        is_answers=False
    )
    print(f"✓ Created: {equations_filename}")

    # Create answers PDF
    create_pdf(
        answers_filename,
        "Answer Key - 10,000 Pre-Algebra Equations",
        answers,
        is_answers=True
    )
    print(f"✓ Created: {answers_filename}")

    print()
    print("=" * 70)
    print("COMPLETE!")
    print("=" * 70)
    print()
    print(f"Equations PDF: {equations_filename}")
    print(f"Answers PDF:   {answers_filename}")
    print()
    print("Each time you run this script, new random equations will be generated")
    print("following the same progressive difficulty curve based on the syllabus.")
    print()


if __name__ == "__main__":
    main()
