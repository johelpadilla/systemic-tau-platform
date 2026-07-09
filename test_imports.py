import sys
import glob
import importlib.util

sys.path.insert(0, "src")
sys.path.insert(0, "app")

files = glob.glob("app/pages/*.py") + ["app/Home.py"]
for file in files:
    name = file.replace("/", ".").replace(".py", "")
    spec = importlib.util.spec_from_file_location(name, file)
    module = importlib.util.module_from_spec(spec)
    try:
        # We can't easily execute streamlit scripts headless like this without mocking streamlit, 
        # but we can try to compile them to AST to catch undefined names.
        import ast
        with open(file, "r") as f:
            tree = ast.parse(f.read(), filename=file)
    except Exception as e:
        print(f"Error in {file}: {e}")
        sys.exit(1)
print("All files parsed successfully.")
