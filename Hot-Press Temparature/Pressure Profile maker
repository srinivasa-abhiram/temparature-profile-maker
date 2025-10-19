import matplotlib.pyplot as plt
import numpy as np
import re

# Degree symbol for temperature annotations
degree = "\u00B0" 

# --- CHANGED ---
# Font size reduced by 2 points
font_size = 12 
# --- END CHANGE ---

#==========================================================
def build_pressure_profile(sentences):
    """
    Parses a list of string commands to create a hot-press pressure profile.
    Time unit is now in MINUTES.
    """
    steps = []
    total_time = 0
    current_pressure = 0  # Start at 0 MPa (gauge pressure)

    # Regex patterns updated from 'hours' to 'minutes'
    ramp_pattern = r"Ramp pressure from (\d+(?:\.\d+)?) ?(?:MPa)? to (\d+(?:\.\d+)?) ?(?:MPa)? in (\d+(?:\.\d+)?) minutes"
    dwell_pattern = r"Dwell at (\d+(?:\.\d+)?) ?(?:MPa)? for (\d+(?:\.\d+)?) minutes at (\d+(?:\.\d+)?) ?(?:C)?"
    release_pattern = r"Release pressure to (\d+(?:\.\d+)?) ?(?:MPa)? in (\d+(?:\.\d+)?) minutes"

    for sentence in sentences:
        ramp_match = re.match(ramp_pattern, sentence)
        dwell_match = re.match(dwell_pattern, sentence)
        release_match = re.match(release_pattern, sentence)

        if ramp_match:
            start, end, duration = map(float, ramp_match.groups())
            steps.append({"type": "ramp_pressure", "start": start, "end": end, "duration": duration})
            current_pressure = end
            total_time += duration
            
        elif dwell_match:
            pressure, duration, temp = map(float, dwell_match.groups())
            steps.append({"type": "dwell", "pressure": pressure, "duration": duration, "temp": temp})
            current_pressure = pressure
            total_time += duration
            
        elif release_match:
            end, duration = map(float, release_match.groups())
            steps.append({"type": "release_pressure", "start": current_pressure, "end": end, "duration": duration})
            current_pressure = end
            total_time += duration
            
        else:
            print(f"Could not parse: '{sentence}'")

    return steps, total_time

# =============================================
def plot_pressure_profile(steps, total_duration, sample_code="", start_label="Start", end_label="End"):
    """
    Plots the pressure-time profile from the parsed steps.
    Time unit is now in MINUTES.
    """
    fig, ax = plt.subplots(figsize=(10, 5)) 
    x, y = 0, 0  # Start at time 0, pressure 0
    x_vals = [x]
    y_vals = [y]

    for step in steps:
        if step['type'] == 'ramp_pressure':
            x_len = step['duration']
            y_len = step['end'] - step['start']
            x_new = x + x_len
            y_new = y + y_len
            ax.plot([x, x_new], [y, y_new], color='red', linewidth=2.5) # Ramping

            rate = y_len / x_len
            
            # --- CHANGED ---
            # Increased vertical offsets from +3/-4 to +4/-5 for better spacing
            ax.text((x + x_new) / 2, (y + y_new) / 2 + 4,
                    f"{rate:.1f} MPa/min", fontsize=font_size, ha='center')
            ax.text((x + x_new) / 2, (y + y_new) / 2 - 5,
                    f"{x_len} min", fontsize=font_size, ha='center')
            # --- END CHANGE ---

            x, y = x_new, y_new
            x_vals.append(x)
            y_vals.append(y)

        elif step['type'] == 'dwell':
            x_len = step['duration']
            x_new = x + x_len
            ax.plot([x, x_new], [y, y], color='green', linewidth=2.5) # Dwell/Hold
            
            # --- CHANGED ---
            # Combined Pressure/Temp text and adjusted logic for low-pressure dwells
            x_mid = (x + x_new) / 2
            info_text = f"{step['pressure']} MPa @ {step['temp']}{degree}C"
            duration_text = f"{x_len} min"

            # Check if pressure is low (e.g. 0) to avoid text going below axis
            if y < 5: # Use 5 MPa as a buffer
                # Stack all text *above* the line
                ax.text(x_mid, y + 5, info_text, fontsize=font_size, ha='center', color='black')
                ax.text(x_mid, y + 2.5, duration_text, fontsize=font_size, ha='center')
            else: 
                # Standard placement: info above, duration below
                ax.text(x_mid, y + 3, info_text, fontsize=font_size, ha='center', color='black')
                ax.text(x_mid, y - 4, duration_text, fontsize=font_size, ha='center')
            # --- END CHANGE ---

            x = x_new
            x_vals.append(x)
            y_vals.append(y)

        elif step['type'] == 'release_pressure':
            x_len = step['duration']
            y_len = step['end'] - step['start']
            x_new = x + x_len
            y_new = y + y_len
            ax.plot([x, x_new], [y, y_new], color='blue', linewidth=2.5) # Releasing

            rate = y_len / x_len
            
            # --- CHANGED ---
            # Increased vertical offsets from +3/-4 to +4/-5 for better spacing
            ax.text((x + x_new) / 2, (y + y_new) / 2 + 4,
                    f"{rate:.1f} MPa/min", fontsize=font_size, ha='center')
            ax.text((x + x_new) / 2, (y + y_new) / 2 - 5,
                    f"{x_len} min", fontsize=font_size, ha='center')
            # --- END CHANGE ---

            x, y = x_new, y_new
            x_vals.append(x)
            y_vals.append(y)

    # --- Set axis range based on pressure ---
    all_pressures = [0] 
    for step in steps:
        if step['type'] in ['ramp_pressure', 'release_pressure']:
            all_pressures.extend([step['start'], step['end']])
        elif step['type'] == 'dwell':
            all_pressures.append(step['pressure'])

    max_pressure = max(all_pressures)
    
    # Adjust limits and ticks for the minute-based scale
    ax.set_xlim(0, max(x_vals) * 1.1)
    ax.set_ylim(-max_pressure * 0.1, max_pressure * 1.25) # Give a little space at bottom
    ax.set_xticks(np.arange(0, max(x_vals) + 5, 2)) 
    ax.set_yticks(np.arange(0, max_pressure + 20, 10))

    # --- Update Labels and Title ---
    # Updated x-axis label
    ax.set_xlabel("Time (minutes)", fontsize=font_size)
    ax.set_ylabel("Pressure (MPa)", fontsize=font_size)
    ax.grid(True, linestyle="--", alpha=0.5)

    ax.set_title("Hot-Press Pressure-Time Profile", fontsize=font_size + 2)

    # --- Start and end labels ---
    ax.text(x_vals[0], y_vals[0] + 2,
            f"{start_label}", fontsize=font_size,
            ha='left', va='bottom', color='green')

    ax.text(x_vals[-1] * 1.02, y_vals[-1] + 2,
            f"{end_label}", fontsize=font_size,
            ha='left', va='bottom', color='purple')

    # --- Sample code and total duration box ---
    # Updated info box to show minutes
    info = f"Sample: {sample_code}\nTotal Time: {total_duration:.1f} min"
    ax.text(0.98, 0.96, info,
            transform=ax.transAxes,
            fontsize=font_size,
            verticalalignment='top',
            horizontalalignment='right',
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    # ========================================================
    plt.tight_layout()
    plt.show()

# ========================================================
# --- Example Usage based on your request ---
# ========================================================

# This list is based on your outline, with the assumptions I mentioned above.
# You can change the durations (e.g., "2 minutes") to fit your needs.
hp_sentences = [
    "Ramp pressure from 0 to 30 MPa in 4 minutes",
    "Dwell at 30 MPa for 2 minutes at 250C",      # Assumed 2 min duration
    "Ramp pressure from 30 to 50 MPa in 2 minutes", # Assumed 2 min duration
    "Dwell at 50 MPa for 7 minutes at 390C",
    "Release pressure to 0 MPa in 1 minutes",
    "Dwell at 0 MPa for 1 minutes at 390C" # Your new step
]

# Build and plot the profile
steps, total_duration = build_pressure_profile(hp_sentences)
plot_pressure_profile(
    steps,
    total_duration,
    sample_code="CuSbSe$_2$",
    start_label=f"Start", # Changed from RT
    end_label=f"End"   # Changed from RT
)
