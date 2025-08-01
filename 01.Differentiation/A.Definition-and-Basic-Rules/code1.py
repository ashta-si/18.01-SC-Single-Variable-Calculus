import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Define function and derivative
def f(x):
    return x**3 - 2*x**2 + x + 2

def f_prime(x):
    return 3*x**2 - 4*x + 1

# Fixed point x0
x0 = 1.5
y0 = f(x0)
m_tangent = f_prime(x0)

# Generate function plot data
x_vals = np.linspace(-1, 3, 500)
y_vals = f(x_vals)

# Set up plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-1, 3)
ax.set_ylim(-2, 8)
ax.set_title("Derivative as Limit of Secant Lines")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True, linestyle='--', alpha=0.6)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Plot function
ax.plot(x_vals, y_vals, 'b-', label="$f(x) = x^3 - 2x^2 + x + 2$", linewidth=2)

# Point P
ax.plot([x0], [y0], 'ro', label=f"Point P at $x_0 = {x0}$")

# Tangent line
tangent_x = np.array([x0 - 1.5, x0 + 1.5])
tangent_y = y0 + m_tangent * (tangent_x - x0)
tangent_line, = ax.plot(tangent_x, tangent_y, 'r-', linewidth=2, label="Tangent Line")

# Secant line & point Q
secant_line, = ax.plot([], [], 'g--', linewidth=2, label="Secant Line")
point_Q, = ax.plot([], [], 'go', markersize=6)

# Text annotations
delta_x_text = ax.text(0.05, 0.9, "", transform=ax.transAxes, fontsize=10)
delta_f_text = ax.text(0.05, 0.85, "", transform=ax.transAxes, fontsize=10)
slope_text = ax.text(0.05, 0.8, "", transform=ax.transAxes, fontsize=10)
final_text = ax.text(1.0, 7.5, "", fontsize=12, color='purple')

# Animation function
def animate(dx):
    xQ = x0 + dx
    yQ = f(xQ)

    secant_line.set_data([x0, xQ], [y0, yQ])
    point_Q.set_data([xQ], [yQ])

    delta_x = dx
    delta_f = yQ - y0
    slope = delta_f / delta_x if delta_x != 0 else np.nan

    delta_x_text.set_text(f"$\\Delta x = {delta_x:.4f}$")
    delta_f_text.set_text(f"$\\Delta f = {delta_f:.4f}$")
    slope_text.set_text(f"Slope of PQ = $\\frac{{\\Delta f}}{{\\Delta x}} = {slope:.4f}$")

    final_text.set_text("As $\\Delta x \\to 0$, the secant becomes the tangent." if dx < 0.002 else "")

    return secant_line, point_Q, delta_x_text, delta_f_text, slope_text, final_text

# Δx values
deltas = np.concatenate([
    np.linspace(1.0, 0.1, 15),
    np.linspace(0.1, 0.01, 15),
    np.linspace(0.01, 0.001, 10)
])

# Add legend
ax.legend(loc="upper left")

# Create animation
ani = FuncAnimation(fig, animate, frames=deltas, interval=250, blit=False)

# Show animation in a window
plt.show()

# Optional: save as GIF
ani.save("derivative_secant_to_tangent.gif", writer=PillowWriter(fps=10))
