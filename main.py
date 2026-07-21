import sys
from renderlab.ui.builders import MainWindowBuilder
from renderlab.ui.factories import UIFactory
from renderlab.scene.builders import SceneBuilder
from renderlab.camera.builders import CameraBuilder
from renderlab.geometry.factories import GeometryFactory
from renderlab.materials.factories import MaterialFactory
from renderlab.renderer.builders import RendererBuilder
from renderlab.math.models import Vector3

def main():
    print("Initializing RenderLab Engine...")

    # 1. Build the Main Window (This safely initializes the PySide6 Application)
    window = (MainWindowBuilder()
              .set_title("RenderLab Engine - First Render")
              .set_resolution(800, 600)
              .build())

    # 2. Build the Camera
    camera = (CameraBuilder()
              .set_position(0.0, 0.0, 1.0)
              .look_at(0.0, 0.0, -1.0)
              .set_fov(90.0)
              .set_aspect_ratio(800.0 / 600.0)
              .build())

    # 3. Create Geometry and Materials
    geo_factory = GeometryFactory()
    mat_factory = MaterialFactory()

    # Create a red sphere
    sphere_geo = geo_factory.create(type="sphere", center=Vector3(0.0, 0.0, -1.0), radius=0.5)
    sphere_mat = mat_factory.create(type="lambertian", albedo=Vector3(0.8, 0.2, 0.2)) 

    # Create a ground sphere
    ground_geo = geo_factory.create(type="sphere", center=Vector3(0.0, -100.5, -1.0), radius=100.0)
    ground_mat = mat_factory.create(type="lambertian", albedo=Vector3(0.8, 0.8, 0.0))

    # 4. Build the Scene Aggregate
    scene = (SceneBuilder()
             .with_name("Hello RenderLab")
             .with_camera(camera)
             .with_background(0.5, 0.7, 1.0) # Sky blue gradient
             .add_object(sphere_geo, sphere_mat, name="Red Sphere")
             .add_object(ground_geo, ground_mat, name="Ground Sphere")
             .build())

    # 5. Configure the Renderer
    # Note: 5 samples per pixel is low quality but renders fast for testing
    renderer_builder = (RendererBuilder()
                        .set_resolution(800, 600)
                        .set_samples(5)
                        .set_max_depth(3))
    
    renderer = renderer_builder.build()
    settings = renderer_builder.get_settings()

    # 6. Start the Engine asynchronously
    print("Launching UI and starting background render...")
    window.start_engine(scene, renderer, settings)
    window.show()

    # 8. Start the Qt GUI Event Loop
    print("Launching UI...")
    sys.exit(UIFactory.get_qapplication().exec())

if __name__ == "__main__":
    main()