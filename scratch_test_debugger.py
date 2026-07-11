import numpy as np
import pandas as pd
from stp.config.settings import AnalysisParams
from stp.core.pipeline import run_analysis
from stp.visualization.series_plots import plot_manifold_3d
from stp.reports.pdf_report import generate_pdf_report

print("1. Creating dummy data...")
X = np.random.randn(1000)

print("2. Running analysis with auto_tune=True...")
params = AnalysisParams(auto_tune=True)
result = run_analysis(X, params)

print(f"Auto-tuned params: window={result.params.window}, stride={result.params.stride}, m={result.params.m}")

print("3. Testing 3D manifold plot...")
fig = plot_manifold_3d(result)
if fig:
    print("3D plot generated.")

print("4. Testing PDF generation...")
pdf_bytes = generate_pdf_report(result)
if pdf_bytes:
    print(f"PDF generated, size: {len(pdf_bytes)} bytes.")
    
print("5. Checking division by zero edge case in auto_tau...")
from stp.core.auto_tau import estimate_optimal_delay
X_const = np.zeros(100)
try:
    delay = estimate_optimal_delay(X_const)
    print(f"Constant delay returned: {delay}")
except Exception as e:
    print(f"Constant delay FAILED: {e}")

print("6. Checking UI imports...")
try:
    import importlib
    importlib.import_module("app.pages.5_Laboratorio")
    print("5_Laboratorio imported successfully (though Streamlit might complain about being run directly, this checks syntax and top-level imports).")
except Exception as e:
    print(f"5_Laboratorio top-level failed: {e}")

print("All debugger tests finished.")
