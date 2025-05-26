# How to Run Manim Animation Files

## Prerequisites

1. **Check if Manim is installed:**
   ```bash
   python3 -c "import manim; print('Manim version:', manim.__version__)"
   ```

2. **If not installed, install Manim:**
   ```bash
   pip install manim
   ```

## Basic Command Structure

```bash
manim [OPTIONS] FILE_NAME SCENE_CLASS_NAME
```

- `FILE_NAME`: Your Python file (e.g., `bouncing_balls.py`)
- `SCENE_CLASS_NAME`: The class name of your scene (e.g., `BouncingBalls`)

## Quality Options

### 1. **Low Quality (fastest rendering)**
```bash
manim bouncing_balls.py BouncingBalls -ql
```
- Resolution: 480p
- Frame rate: 15fps
- Best for: Quick testing and development

### 2. **Medium Quality (default)**
```bash
manim bouncing_balls.py BouncingBalls
```
- Resolution: 1080p
- Frame rate: 60fps
- Best for: Final output

### 3. **High Quality**
```bash
manim bouncing_balls.py BouncingBalls -qh
```
- Resolution: 1440p
- Frame rate: 60fps

### 4. **4K Quality**
```bash
manim bouncing_balls.py BouncingBalls -qk
```
- Resolution: 2160p (4K)
- Frame rate: 60fps
- Best for: Professional/presentation quality

## Preview Options

### 1. **Preview Quality (with auto-open)**
```bash
manim bouncing_balls.py BouncingBalls -p
```
- Renders in preview quality (480p, 15fps)
- Automatically opens the video when rendering is complete

### 2. **Live Preview**
```bash
manim bouncing_balls.py BouncingBalls --preview
```
- Interactive preview mode
- Shows real-time rendering

## Output Options

### 1. **Save as GIF**
```bash
manim bouncing_balls.py BouncingBalls --format gif
```

### 2. **Save Last Frame as PNG**
```bash
manim bouncing_balls.py BouncingBalls -s
```

### 3. **Transparent Background**
```bash
manim bouncing_balls.py BouncingBalls -t
```

## Useful Flags

### 1. **Verbose Output**
```bash
manim bouncing_balls.py BouncingBalls -v DEBUG
```

### 2. **Disable Caching**
```bash
manim bouncing_balls.py BouncingBalls --disable_caching
```

### 3. **Custom Output Directory**
```bash
manim bouncing_balls.py BouncingBalls -o /path/to/output
```

### 4. **Custom Resolution**
```bash
manim bouncing_balls.py BouncingBalls -r 1920,1080
```

### 5. **Custom Frame Rate**
```bash
manim bouncing_balls.py BouncingBalls --frame_rate 30
```

## Common Combinations

### For Development/Testing:
```bash
manim bouncing_balls.py BouncingBalls -pql
```
- Preview quality + auto-open

### For Final Output:
```bash
manim bouncing_balls.py BouncingBalls -qh
```
- High quality rendering

### For Quick Check:
```bash
manim bouncing_balls.py BouncingBalls -s
```
- Just save the last frame as image

## Output Locations

By default, rendered files are saved to:
```
media/
├── videos/
│   └── [filename]/
│       └── [quality]/
│           └── [SceneName].mp4
├── images/
│   └── [filename]/
│       └── [SceneName].png
└── Tex/  (for LaTeX renders)
```

For example:
- Video: `media/videos/bouncing_balls/1080p60/BouncingBalls.mp4`
- Image: `media/images/bouncing_balls/BouncingBalls.png`

## Troubleshooting

### 1. **"Command 'python' not found"**
Use `python3` instead of `python`:
```bash
python3 -m manim bouncing_balls.py BouncingBalls
```

### 2. **"No module named 'manim'"**
Install Manim:
```bash
pip install manim
# or
pip3 install manim
```

### 3. **Scene not found**
Make sure:
- The class name matches exactly (case-sensitive)
- The class inherits from `Scene`
- The file syntax is correct

### 4. **Rendering errors**
- Check your code for syntax errors
- Ensure all imports are correct
- Use `-v DEBUG` for detailed error messages

## Example Usage

```bash
# Quick test
manim my_animation.py MyScene -pql

# Final render
manim my_animation.py MyScene -qh

# Create GIF
manim my_animation.py MyScene --format gif -ql

# Just get the last frame
manim my_animation.py MyScene -s
```

## Additional Resources

- **Manim Documentation**: https://docs.manim.community/
- **Manim Examples**: https://docs.manim.community/en/stable/examples.html
- **Community Forum**: https://www.reddit.com/r/manim/ 