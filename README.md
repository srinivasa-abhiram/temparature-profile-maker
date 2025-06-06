🔥 Temperature-Time Profile Plotter
This Python script allows you to generate temperature-time plots from simple, human-readable text instructions. It’s especially useful for visualizing furnace heating/cooling protocols in materials science, ceramics, or thermal treatment experiments. 

✨ Features:
- Easy natural-language input like: `Ramp from 25 to 900C in 10 hours`
- Supports decimals and temperature units like `25C`, `350.4`, etc.
- Automatically calculates and annotates ramp rates, hold durations, total time
- Shows customizable start/end labels and sample code
- Clean matplotlib visuals for scientific reports or lab records


MIT License
Copyright (c) 2025 [Srinivasa Abhiram Kurapati]

📌 Example Input:
```python
sentences = [
    "Ramp from 25 to 990.2C in 10 hours",
    "Hold at 990.2 for 12 hours",
    "Cool to 320.4 in 6 hours",
    "Hold at 320.4C for 10 hours",
    "Cool to 25 in 5 hours"
]

