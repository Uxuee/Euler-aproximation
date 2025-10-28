# Euler Method — Forward Euler Approximation for ODEs

https://en.wikipedia.org/wiki/Euler_method

![Euler Method Illustration](https://raw.githubusercontent.com/Uxuee/Euler-aproximation/master/800px-Euler_method.svg.png)

A minimal, well-documented implementation of the **Forward Euler** method to numerically solve **first-order ordinary differential equations (ODEs)**:
\[
\frac{dy}{dt} = f(t, y), \quad y(t_0) = y_0
\]
Includes examples, error analysis, and guidance on **step-size** and **stability**.

> If you’re learning numerical methods, this repo shows the full path: definition → code → plots → error vs. step size → caveats.

---

## ✨ Features
- **Forward Euler** integrator for \( y' = f(t,y) \)
- Works with scalar ODEs and simple vector ODEs
- **Examples**: exponential decay, harmonic oscillator (vector form)
- **Plots** of numerical vs. analytical solutions (when available)
- **Error analysis** (local/global truncation error) and **stability notes**
- Clean API you can extend to **Heun**, **RK2/RK4**, or adaptive methods

---

## 🧠 Method (in one minute)

Forward Euler updates the solution with a first-order Taylor step:
\[
y_{n+1} = y_n + h \, f(t_n, y_n), \qquad t_{n+1} = t_n + h
\]
- **Local truncation error:** \( \mathcal{O}(h^2) \)
- **Global error:** \( \mathcal{O}(h) \)
- **Stability caveat:** small \( h \) needed, especially for stiff problems or negative real eigenvalues.

---

## 📦 Installation

This project is intentionally lightweight. If it’s pure Python:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # if provided
# Or just ensure numpy/matplotlib are installed:
pip install numpy matplotlib
