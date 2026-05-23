def car_crash_simulator(m1, v1, m2, v2, collision_type):
    if collision_type == "elastic":
        v1_final = ((m1 - m2) / (m1 + m2)) * v1 + ((2 * m2) / (m1 + m2)) * v2
        v2_final = ((2 * m1) / (m1 + m2)) * v1 + ((m2 - m1) / (m1 + m2)) * v2
    elif collision_type == "inelastic":
        v_final = (m1 * v1 + m2 * v2) / (m1 + m2)
        v1_final = v_final
        v2_final = v_final
    else:
        raise ValueError("Invalid collision type. Use 'elastic' or 'inelastic'.")
    ke_initial = 0.5 * m1 * v1 ** 2 + 0.5 * m2 * v2 ** 2
    ke_final = 0.5 * m1 * v1_final ** 2 + 0.5 * m2 * v2_final ** 2
    energy_lost = ke_initial - ke_final
    return v1_final, v2_final, energy_lost

# Test cases
result1 = car_crash_simulator(1000, 10, 1000, -5, "elastic")
print(result1)

result2 = car_crash_simulator(800, 20, 1200, 0, "inelastic")
print(result2)

result3 = car_crash_simulator(1500, 15, 1500, -10, "inelastic")
print(result3)