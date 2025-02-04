# ByteMorph
📌 FBX to GLB Conversion Guide
Convert FBX Files to GLB Using Blender’s Headless Mode
🚀 This guide walks you through downloading, setting up, and running a script that converts FBX files to GLB using Blender’s Python API.

📥 Download & Install Requirements
1️⃣ Install Blender
Download Blender from Blender.org
Install Blender and ensure it's added to your system PATH (so you can run blender in the terminal).
2️⃣ Clone This Repository
Run the following command in your terminal:

  git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
  cd YOUR_REPO_NAME

3️⃣ Place Your FBX File
Move your .fbx file into the repository folder (or use an absolute path when running the script).

⚡ How to Run the Script
Run the following command in Command Prompt (Windows) or Terminal (Mac/Linux):

  blender --background --python convert_fbx_to_glb.py -- path/to/your/file.fbx

  Example:
  blender --background --python convert_fbx_to_glb.py -- D:\Models\character.fbx

✅ This will generate a .glb file in the same directory as the .fbx file.

🛠 Troubleshooting
1. Blender is Not Recognized as a Command
If you see:

  'blender' is not recognized as an internal or external command

You need to add Blender to your system PATH:

 - Windows: Add C:\Program Files\Blender Foundation\Blender 3.x\ to the Path environment variable.
 - Mac: Blender is usually located in /Applications/Blender.app/Contents/MacOS/Blender.
 - Linux: Install Blender via package manager (sudo apt install blender).
 - 
2. FBX Import Fails
   
 - Ensure your FBX file is valid and exported correctly.
 - Try opening it in Blender manually to confirm it's not corrupted.
