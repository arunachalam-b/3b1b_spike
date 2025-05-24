# Pythagorean Theorem Animation

This project contains a simple 30-second mathematical animation created using the 3Blue1Brown manim library. The animation visually explains the Pythagorean Theorem using a right triangle and squares on each side.

## What the Animation Shows

The animation demonstrates:
- A right triangle with sides of length 3, 4, and 5
- Squares constructed on each side of the triangle
- The areas of each square (9, 16, and 25)
- The mathematical relationship: a² + b² = c²
- Numerical verification: 3² + 4² = 5² → 9 + 16 = 25

## Requirements

- Python 3.7 or higher
- manim library (version 0.19.0)

## Installation

1. Install manim:
```bash
pip3 install manim
```

Or use the requirements file:
```bash
pip3 install -r requirements.txt
```

## Running the Animation

To generate the video, run:
```bash
manim -pqh pythagorean_theorem.py PythagoreanTheorem
```

This will create a high-quality video file in the `media/videos/pythagorean_theorem/1080p60/` directory.

## Options

- `-p`: Preview the video after rendering
- `-q`: Quality (l=low, m=medium, h=high, k=4k)
- `-h`: High quality (1080p60)

For a quick preview in lower quality:
```bash
manim -pql pythagorean_theorem.py PythagoreanTheorem
```

## Output

The animation will be approximately 30 seconds long and will be saved as an MP4 file. 