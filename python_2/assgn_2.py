import math

# Relative roughness
epsilon_relative = 0.000166

# Function to calculate friction factor (f) using Colebrook equation
def colebrook_equation(NRe, d):
    epsilon = epsilon_relative * d
    
    return (1.74 - math.log10((epsilon / 3.7) + (2.51 / (NRe * math.sqrt(f)))))**2

# Function to calculate friction factor (f) iteratively
def calculate_friction_factor(NRe, d, epsilon):
    f_initial = 0.001  # Initial guess
    iteration = 0
    max_iterations = 100

    while iteration < max_iterations:
        f = colebrook_equation(NRe, d)
        iteration += 1

        if abs(f - f_initial) < 0.0001:
            break
        f_initial = f

    return f

# Reynolds numbers
Reynolds_numbers = [300, 600, 900, 3000, 6000, 9000]

# Diameter
d = 18.7  # Assumed diameter since it's not given in the problem statement

# Calculate friction factors (f) for the given Reynolds numbers
friction_factors = [calculate_friction_factor(NRe, d, epsilon_relative * d) for NRe in Reynolds_numbers]

# Print results
for NRe, f in zip(Reynolds_numbers, friction_factors):
    print(f"Reynolds number: {NRe:6.0f}, Friction factor: {f:.4f}")

    #One comment with regards to Reynolds number and Friction factor:The Reynolds number is a dimensionless 
    # quantity that characterizes the flow regime (laminar or turbulent) in a fluid 
    # flowing through a pipe. The friction factor (f) is a dimensionless coefficient that quantifies the resistance
    #  to flow due to pipe roughness and fluid viscosity. The Colebrook equation is used to estimate the friction factor 
    # for both laminar and turbulent flow regimes. The friction factor is essential for calculating
    #  pressure loss and head loss in pipe flow systems.