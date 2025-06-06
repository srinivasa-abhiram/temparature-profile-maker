🔥 Temperature-Time Profile Plotter
This Python script allows you to generate temperature-time plots from simple, human-readable text instructions. It’s especially useful for visualizing furnace heating/cooling protocols in materials science, ceramics, or thermal treatment experiments. 

✨ Features:
- Easy natural-language input like: `Ramp from 25 to 900C in 10 hours`
- Supports decimals and temperature units like `25C`, `350.4`, etc.
- Automatically calculates and annotates ramp rates, hold durations, total time
- Shows customizable start/end labels and sample code
- Clean matplotlib visuals for scientific reports or lab records

📌 Example Input:
```python
sentences = [
    "Ramp from 25 to 990.2C in 10 hours",
    "Hold at 990.2 for 12 hours",
    "Cool to 320.4 in 6 hours",
    "Hold at 320.4C for 10 hours",
    "Cool to 25 in 5 hours"
]

MIT License

Copyright (c) 2025 [Srinivasa Abhiram Kurapati]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.
