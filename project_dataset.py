import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

# -----------------------------
# CONFIG
# -----------------------------
NUM_ROWS = 20000
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)

# Plants, Units, Zones, Machines
plants = ["Plant-1", "Plant-2", "Plant-3"]
zones = ["Zone-A", "Zone-B", "Zone-C"]
units = {
    "Plant-1": ["Unit-1A", "Unit-1B", "Unit-1C"],
    "Plant-2": ["Unit-2A", "Unit-2B"],
    "Plant-3": ["Unit-3A", "Unit-3B", "Unit-3C", "Unit-3D"],
}
machines = [
    "Mixer-1", "Mixer-2",
    "Extruder-1", "Extruder-2",
    "Packaging-1", "Packaging-2",
    "Utility-Chiller", "Utility-Compressor"
]
machine_rated_power = {
    "Mixer-1": 75,
    "Mixer-2": 75,
    "Extruder-1": 120,
    "Extruder-2": 150,
    "Packaging-1": 40,
    "Packaging-2": 40,
    "Utility-Chiller": 90,
    "Utility-Compressor": 110
}

# Tariff info
tariff_slabs = ["Peak", "Off-Peak", "Normal"]
base_rate = {
    "Peak": 9.0,      # Rs/kWh
    "Normal": 7.0,
    "Off-Peak": 5.5
}

# -----------------------------
# TIME RANGE
# -----------------------------
# Let's create timestamps over ~90 days, hourly data, then sample 20k rows
start_datetime = datetime(2025, 1, 1, 0, 0, 0)
end_datetime = start_datetime + timedelta(days=90)
all_hours = pd.date_range(start=start_datetime, end=end_datetime, freq="H")
# We'll sample from this list for each row
total_hours = len(all_hours)

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def get_shift(hour):
    """Return Shift based on hour of day."""
    if 6 <= hour < 14:
        return "Shift-1"  # Morning
    elif 14 <= hour < 22:
        return "Shift-2"  # Evening
    else:
        return "Shift-3"  # Night

def get_time_of_use(hour):
    """Classify hour for tariff."""
    if 18 <= hour < 22:
        return "Peak"
    elif 22 <= hour or hour < 6:
        return "Off-Peak"
    else:
        return "Normal"

def get_zone():
    return random.choice(zones)

def generate_row():
    # Choose random timestamp
    ts = all_hours[np.random.randint(0, total_hours)]
    hour = ts.hour

    plant = random.choice(plants)
    unit = random.choice(units[plant])
    zone = get_zone()
    machine = random.choice(machines)
    rated_power = machine_rated_power[machine]

    shift = get_shift(hour)
    time_of_use = get_time_of_use(hour)

    # Tariff slab = time_of_use for simplicity
    tariff_slab = time_of_use
    rate_per_kwh = base_rate[tariff_slab] + np.random.normal(0, 0.3)  # small fluctuation
    rate_per_kwh = max(rate_per_kwh, 4.0)  # floor

    # Utilization depends on shift & machine type
    if shift == "Shift-1":
        base_util = np.random.uniform(0.6, 0.9)
    elif shift == "Shift-2":
        base_util = np.random.uniform(0.5, 0.85)
    else:
        base_util = np.random.uniform(0.2, 0.6)

    # Utilities (chiller, compressor) may run more consistently
    if "Utility" in machine:
        base_util += 0.1
        base_util = min(base_util, 1.0)

    # Runtime in this hour (0–1 hour realistically)
    runtime_hours = np.clip(np.random.normal(base_util, 0.15), 0, 1.0)

    # Energy and power
    # basic: Energy_kWh = RatedPower * utilization * runtime
    load_factor = np.clip(np.random.normal(base_util, 0.1), 0.2, 1.0)
    energy_kwh = rated_power * load_factor * runtime_hours
    # Add some random noise
    energy_kwh += np.random.normal(0, rated_power * 0.05)
    energy_kwh = max(energy_kwh, 0.0)

    power_kw = energy_kwh  # since this is 1 hour interval, approx kW ~ kWh/h

    # Production quantity roughly proportional to runtime & machine type
    if "Extruder" in machine:
        base_output_rate = np.random.uniform(80, 120)   # units/hour
    elif "Mixer" in machine:
        base_output_rate = np.random.uniform(50, 90)
    elif "Packaging" in machine:
        base_output_rate = np.random.uniform(100, 200)
    else:
        # Utilities - no direct production, but we can set low or zero
        base_output_rate = np.random.uniform(0, 10)

    quantity_produced = base_output_rate * runtime_hours
    # rounding & noise
    quantity_produced += np.random.normal(0, base_output_rate * 0.05)
    quantity_produced = max(quantity_produced, 0.0)

    # Electrical parameters (typical industrial values)
    voltage = np.random.normal(415, 10)   # 3-phase ~ 415V
    voltage = np.clip(voltage, 380, 450)

    # I = P / (sqrt(3)*V*PF)
    power_factor = np.clip(np.random.normal(0.9, 0.05), 0.7, 1.0)
    apparent_power_kva = power_kw / power_factor if power_factor > 0 else 0
    current = 0.0
    if voltage > 0:
        current = (apparent_power_kva * 1000) / (np.sqrt(3) * voltage)
    current += np.random.normal(0, 5)
    current = max(current, 0.0)

    # Demand charge: only significant in peak hours
    if time_of_use == "Peak":
        demand_charge = np.random.uniform(200, 600)
    else:
        demand_charge = np.random.uniform(50, 150)

    # Random meter ID
    meter_id = f"M-{np.random.randint(1001, 1100)}"

    # Compose row
    row = {
        "Timestamp": ts,
        "Plant": plant,
        "Zone": zone,
        "Unit": unit,
        "Machine": machine,
        "MeterID": meter_id,
        "RatedPower_kW": rated_power,
        "Energy_kWh": round(energy_kwh, 2),
        "Power_kW": round(power_kw, 2),
        "Voltage": round(voltage, 1),
        "Current": round(current, 2),
        "PowerFactor": round(power_factor, 2),
        "QuantityProduced": int(quantity_produced),
        "MachineRuntimeHours": round(runtime_hours, 2),
        "Shift": shift,
        "TariffSlab": tariff_slab,
        "RatePerKWh": round(rate_per_kwh, 2),
        "DemandCharge": round(demand_charge, 2),
        "TimeOfUse": time_of_use
    }
    return row

# -----------------------------
# GENERATE DATA
# -----------------------------
rows = [generate_row() for _ in range(NUM_ROWS)]
df = pd.DataFrame(rows)

# Sort by timestamp for realism
df = df.sort_values("Timestamp").reset_index(drop=True)

# -----------------------------
# SAVE TO CSV
# -----------------------------
output_file = "industrial_energy_efficiency_20000.csv"
df.to_csv(output_file, index=False)

print(f"Dataset generated and saved to: {output_file}")
print(df.head())
