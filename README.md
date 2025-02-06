# 3D Car Battle Arena Game

## Overview
A dynamic 3D multiplayer car battle game built with Python, OpenGL, and Pygame. Players control different colored cars while avoiding obstacles and battling for survival in an enclosed arena environment.

## Features

### Gameplay Elements
- **Multiple Player Support**: Up to 5 players can play simultaneously
- **Unique Car Controls**: Each car has dedicated keyboard controls
- **Health System**: Cars have individual health bars that deplete upon taking damage
- **Dynamic Obstacles**: 
  - Moving and static cubes that damage cars on contact
  - Bouncing spheres creating additional challenge
  - Rotating orange rectangle as a centerpiece obstacle
- **Interactive Environment**:
  - Checkered floor pattern
  - Boundary walls with dynamic patterns
  - Grid-based movement system

### Technical Features
- Real-time 3D rendering using OpenGL
- Physics-based movement and collisions
- Dynamic lighting and color effects
- Smooth animations and transitions
- Health bar UI system

## Controls

### Car Controls
- **Car 1 (Black/Red)**:
  - Arrow keys for movement
  - Up/Down: Forward/Backward
  - Left/Right: Lateral movement

- **Car 2 (Green/Purple)**:
  - W/S: Forward/Backward
  - A/D: Lateral movement

- **Car 3 (Pink/Cyan)**:
  - AI-controlled, automatically avoids obstacles

- **Car 4 (Yellow/Black)**:
  - I/K: Forward/Backward
  - J/L: Lateral movement

- **Car 5 (Brown/Black)**:
  - T/G: Forward/Backward
  - F/H: Lateral movement

## System Requirements
- Python 3.x
- PyGame
- PyOpenGL
- NumPy
- Operating System: Windows/Linux/MacOS

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
```

2. Install required dependencies:
```bash
pip install pygame
pip install pyopengl
pip install numpy
```

3. Run the game:
```bash
python main.py
```

## Project Structure
```
├── src/
│   ├── main.py          # Main game loop and initialization
│   ├── car.py           # Car rendering and mechanics
│   ├── control.py       # Input handling and movement controls
│   ├── cube.py          # Obstacle generation and behavior
│   ├── health_bar.py    # Health system UI
│   ├── init.py          # Display and background initialization
│   └── sphere.py        # Sphere obstacle mechanics
├── assets/
│   └── images/         # Game textures and images
└── README.md
```

## Technical Details

### Graphics
- OpenGL-based 3D rendering
- Custom shaders for car models
- Dynamic lighting effects
- Particle effects for collisions
- Real-time shadow rendering

### Physics
- Collision detection system
- Boundary checking
- Velocity-based movement
- Dynamic obstacle behavior

### AI
- Autonomous car with obstacle avoidance
- Path finding algorithm
- Dynamic response to environment

## Game Mechanics

### Health System
- Each car starts with 300 health points
- Damage taken from:
  - Collision with moving cubes
  - Contact with static obstacles
  - Impact with other cars
- Health bars display current status
- Cars disappear when health reaches zero

### Obstacles
- **Moving Cubes**: Track and follow nearest car
- **Static Cubes**: Deal heavy damage on contact
- **Bouncing Spheres**: Create dynamic environment
- **Orange Rectangle**: Rotating central obstacle

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Version History
- v1.0: Initial release
  - Basic car mechanics
  - Multiplayer support
  - Obstacle system
  - Health tracking


## Future Enhancements
- Add power-ups and special abilities
- Implement multiplayer networking
- Add sound effects and background music
- Create additional game modes
- Enhance graphics and particle effects
