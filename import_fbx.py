import bpy
import sys
import os

def convert_fbx_to_glb(input_fbx):
    # Clear the existing scene
    bpy.ops.wm.read_factory_settings(use_empty=True)

    # Import the FBX file
    bpy.ops.import_scene.fbx(filepath=input_fbx)
    print(f"Successfully imported: {input_fbx}")

    # Generate output path (same directory, but with .glb extension)
    output_glb = os.path.splitext(input_fbx)[0] + ".glb"

    # Export as GLB
    bpy.ops.export_scene.gltf(filepath=output_glb, export_format='GLB')
    print(f"Converted to GLB: {output_glb}")

if __name__ == "__main__":
    # Get the FBX file path from command-line arguments
    input_fbx = sys.argv[-1]

    # Run the conversion
    convert_fbx_to_glb(input_fbx)