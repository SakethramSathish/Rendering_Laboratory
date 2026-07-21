<div align="center">
  
# Rendering Laboratory

**A Python-based Interactive Path Tracing Engine**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Ray Tracing](https://img.shields.io/badge/Graphics-Ray%20Tracing-FF6F00?style=for-the-badge)

</div>

---

## 🌟 Overview

**Rendering Laboratory** is a completely modular, CPU-based path-tracing engine written entirely in Python. It provides a highly extensible object-oriented architecture designed for experimenting with advanced computer graphics, geometric intersections, physically-based materials, and dynamic ray tracing.

## ✨ Features

- **Physically-Based Path Tracing**: Accurate light bouncing, diffuse scattering (Lambertian), and metallic reflections.
- **Interactive Camera System**: Navigate the 3D scene in real-time using asynchronous rendering.
- **Dynamic Quality Scaling**: Automatically drops to a fast 1-sample preview during movement and seamlessly resolves to a high-quality multi-sampled image when idle.
- **Modular Architecture**: Built with robust Factory and Builder design patterns, making it trivial to add new geometries, materials, and engine components.
- **Multi-threaded GUI**: A responsive PySide6 UI that leverages `QThread` to prevent UI freezing during intensive mathematical computations.

## 🏗️ Engine Architecture

Rendering Laboratory strictly separates the User Interface, Scene Construction, and the Rendering Engine to maintain clean dependencies. The interactive event flow and data pipeline are visualized below:

```mermaid
flowchart TD
    %% Define styles
    classDef ui fill:#1E88E5,stroke:#fff,stroke-width:2px,color:#fff
    classDef worker fill:#8E24AA,stroke:#fff,stroke-width:2px,color:#fff
    classDef engine fill:#43A047,stroke:#fff,stroke-width:2px,color:#fff
    classDef data fill:#FB8C00,stroke:#fff,stroke-width:2px,color:#fff

    User([👤 User]) -->|Keyboard & Mouse Events| UI(PySide6 Main Window):::ui
    
    subgraph Frontend [UI & Event Loop]
        UI -->|Updates Origin & FOV| CamData[(Camera State)]:::data
        UI -->|Spawns & Manages| Worker{RenderWorker QThread}:::worker
    end
    
    subgraph Backend [Ray Tracing Engine]
        Worker -->|Executes| Renderer(CPU Path Tracer):::engine
        Renderer -->|Generates Rays from| CamData
        Renderer -->|Computes Intersections| Scene[Scene Graph Aggregate]:::engine
        Scene -->|Evaluates| Geom(Geometry Models):::data
        Scene -->|Evaluates| Mat(Material Shaders):::data
    end

    Renderer -->|Returns Pixel Buffer| Worker
    Worker -.->|Emits QImage Cross-Thread Signal| UI
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- [NumPy](https://numpy.org/) (for accelerated matrix and vector math)
- [PySide6](https://doc.qt.io/qtforpython-6/) (for the GUI and threading)

### Running the Engine
Simply launch the engine by running the main module:
```bash
python main.py
```

### Controls
Once the engine has booted, you can explore the scene:
- `W` - Move Camera Forward
- `S` - Move Camera Backward
- `A` - Strafe Camera Left
- `D` - Strafe Camera Right
- `Mouse Scroll Wheel` - Dynamically adjust the Field of View (Zoom)

## 🛠️ Extending the Engine

Because of the Factory-based architecture, extending the engine is straightforward.

**To add a new shape:**
1. Create a new class inheriting from `Intersectable` in `renderlab.geometry.services`.
2. Implement the mathematical ray-intersection logic in the `intersect()` method.
3. Register your new shape in the `GeometryFactory` (`renderlab.geometry.factories`).
4. Apply any existing `Material` to your new shape and render!
