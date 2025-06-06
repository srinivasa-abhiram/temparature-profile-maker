import matplotlib.pyplot as plt
import numpy as np
import re

degree = "\u00B0" #defined the degree symbol use: {degree} for the symbol, when ever needed

font_size = 17

#==========================================================
def build_profile(sentences):
    steps = []
    total_time = 0
    current_temp = 25  # default start temp

    ramp_pattern = r"Ramp from (\d+(?:\.\d+)?)(?:C)? to (\d+(?:\.\d+)?)(?:C)? in (\d+(?:\.\d+)?) hours"
    hold_pattern = r"Hold at (\d+(?:\.\d+)?)(?:C)? for (\d+(?:\.\d+)?) hours"
    cool_pattern = r"Cool to (\d+(?:\.\d+)?)(?:C)? in (\d+(?:\.\d+)?) hours"

    for sentence in sentences:
        ramp_match = re.match(ramp_pattern, sentence)
        hold_match = re.match(hold_pattern, sentence)
        cool_match = re.match(cool_pattern, sentence)

        if ramp_match:
            start, end, duration = map(float, ramp_match.groups())
            steps.append({"type": "ramp", "start": start, "end": end, "duration": duration})
            current_temp = end
            total_time += duration
        elif hold_match:
            temp, duration = map(float, hold_match.groups())
            steps.append({"type": "hold", "temp": temp, "duration": duration})
            current_temp = temp
            total_time += duration
        elif cool_match:
            end, duration = map(float, cool_match.groups())
            steps.append({"type": "cool", "start": current_temp, "end": end, "duration": duration})
            current_temp = end
            total_time += duration
        else:
            print(f"Could not parse: '{sentence}'")

    return steps, total_time

# =============================================
def plot_profile(steps, total_duration, sample_code="", start_label="Start", end_label="End"):
    fig, ax = plt.subplots(figsize=(12, 6))
    x, y = 0, 25
    x_vals = [x]
    y_vals = [y]

    for step in steps:
        if step['type'] == 'ramp':
            x_len = step['duration']
            y_len = step['end'] - step['start']
            x_new = x + x_len
            y_new = y + y_len
            ax.plot([x, x_new], [y, y_new], color='red', linewidth=2)

            rate = y_len / x_len
            ax.text((x + x_new) / 2, (y + y_new) / 2 + 30,
                    f"{rate:.1f} °C/hr", fontsize=font_size, ha='center')
            ax.text((x + x_new) / 2, (y + y_new) / 2 - 40,
                    f"{x_len} h", fontsize=font_size, ha='center')

            x, y = x_new, y_new
            x_vals.append(x)
            y_vals.append(y)

        elif step['type'] == 'hold':
            x_len = step['duration']
            x_new = x + x_len
            ax.plot([x, x_new], [y, y], color='black', linewidth=2)

            ax.text((x + x_new) / 2, y + 25,
                    f"{step['temp']} °C", fontsize=font_size, ha='center')
            ax.text((x + x_new) / 2, y - 60,
                    f"{x_len} h", fontsize=font_size, ha='center')

            x = x_new
            x_vals.append(x)
            y_vals.append(y)

        elif step['type'] == 'cool':
            x_len = step['duration']
            y_len = step['end'] - step['start']
            x_new = x + x_len
            y_new = y + y_len
            ax.plot([x, x_new], [y, y_new], color='blue', linewidth=2)

            rate = y_len / x_len
            ax.text((x + x_new) / 2, (y + y_new) / 2 + 30,
                    f"{rate:.1f} °C/hr", fontsize=font_size, ha='center')
            ax.text((x + x_new) / 2, (y + y_new) / 2 - 40,
                    f"{x_len} h", fontsize=font_size, ha='center')

            x, y = x_new, y_new
            x_vals.append(x)
            y_vals.append(y)

    # Set axis range
    all_temps = []
    for step in steps:
        if step['type'] in ['ramp', 'cool']:
            all_temps.extend([step['start'], step['end']])
        elif step['type'] == 'hold':
            all_temps.append(step['temp'])

    max_temp = max(all_temps)
    ax.set_xlim(0, max(x_vals) + 2)
    ax.set_ylim(0, max_temp + 100)
    ax.set_xticks(np.arange(0, max(x_vals) + 10, 5))
    ax.set_yticks(np.arange(0, max_temp + 150, 100))

    ax.set_xlabel("Time (hours)", fontsize=font_size)
    ax.set_ylabel("Temperature (°C)", fontsize=font_size)
    ax.grid(True, linestyle="--", alpha=0.5)

    # ====================

    # Set the plot title
    ax.set_title("Temperature-Time Profile", fontsize=font_size + 2)

    # Start and end labels (you can change the text easily here)
    ax.text(x_vals[0], y_vals[0] + 20,
            f"{start_label}", fontsize=font_size,
            ha='left', va='bottom', color='green')

    ax.text(x_vals[-1] + 3.5, y_vals[-1] + 10,
            f"{end_label}", fontsize=font_size,
            ha='right', va='bottom', color='purple')

    # Sample code and total duration box (top-right)
    info = f"Sample: {sample_code}\nTotal Time: {total_duration:.1f} h"
    ax.text(0.98, 0.96, info,
            transform=ax.transAxes,
            fontsize=font_size,
            verticalalignment='top',
            horizontalalignment='right',
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    # ========================================================

    plt.tight_layout()
    plt.show()

sentences = [
    "Ramp from 25 to 990.2C in 5 hours",
    "Hold at 990.2 for 12 hours",
    "Cool to 320.4 in 6 hours",
    "Hold at 320.4C for 10 hours",
    "Cool to 25 in 5 hours"
]
#One can use any time line, for increasing redline will come for hold black will come and for cooling blue shall come:)

steps, total_duration = build_profile(sentences)
plot_profile(
    steps,
    total_duration,
    sample_code="MT01",
    start_label=f" 24 {degree}C",
    end_label=f"24{degree}C"
)
