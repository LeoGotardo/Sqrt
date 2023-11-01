# ✓ Quadratic Equation Solver - Documentation

## Introduction

This Python program serves as a quadratic equation solver. It calculates the roots (also known as solutions or zeroes) of a quadratic equation in the form of `ax^2 + bx + c = 0`, where `a`, `b`, and `c` are coefficients provided by the user.

## How to Use

1. Run the program in your preferred Python environment.
2. The program will prompt you to enter the coefficients `a`, `b`, and `c` of the quadratic equation.

## Program Logic

- The program consists of several functions to perform the necessary mathematical operations:

  1. **`inverte_sinal(pri)`**: This function takes a single argument `pri` and returns its negation (inverted sign).

  2. **`soma(pri, sec)`**: This function takes two arguments `pri` and `sec` and returns their sum.

  3. **`subtracao(pri, sec)`**: This function takes two arguments `pri` and `sec` and returns the result of subtracting `sec` from `pri`.

  4. **`multiplicacao(pri, sec)`**: This function takes two arguments `pri` and `sec` and returns their product.

  5. **`divisao(pri, sec)`**: This function takes two arguments `pri` and `sec` and returns the result of dividing `pri` by `sec`.

  6. **`quadrado(pri)`**: This function takes a single argument `pri` and returns its square (the value of `pri` raised to the power of 2).

  7. **`raiz(pri)`**: This function takes a single argument `pri` and returns the square root of `pri`.

  8. **`delta(a, b, c)`**: This function calculates the discriminant (`delta`) of the quadratic equation using the formula `b^2 - 4ac`.

  9. **`bhaskara()`**: This function is the main function that takes user inputs for coefficients `a`, `b`, and `c` of the quadratic equation. It then calculates the roots of the equation using the quadratic formula and prints the results.

## Example Usage

```
a: 1
b: -3
c: 2
Para a equação:  1.0 x^2 +  -3.0 x +  2.0  = 0
As raizes são:  2.0  e  1.0
```

## Note

- The program calculates the roots using the quadratic formula. In some cases, the roots may be complex numbers, but the current implementation handles only real roots.
- For educational purposes, the program assumes valid inputs from the user. In a real-world application, data validation and error handling should be included to ensure that the user provides appropriate coefficients for a quadratic equation.
