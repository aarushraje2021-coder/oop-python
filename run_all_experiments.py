"""
Master Runner: Executes all OOP Python Experiments in sequence.
"""

import os
import subprocess
import sys

EXPERIMENTS = [
    ("01_default_constructor.py", "Experiment 1: Default Constructor & Initializer"),
    ("02_class_and_instance_variables.py", "Experiment 2: Class vs Instance Variables"),
    ("03_parameterized_constructor.py", "Experiment 3: Parameterized Constructor"),
    ("04_constructor_default_arguments.py", "Experiment 4: Constructor with Default Arguments"),
    ("05_bank_account.py", "Experiment 5: Encapsulation & Real-world OOP (BankAccount)"),
    ("06_single_inheritance.py", "Experiment 6: Single Inheritance"),
    ("07_multiple_inheritance.py", "Experiment 7: Multiple Inheritance & MRO"),
    ("08_super_function.py", "Experiment 8: Super Function in Multiple Inheritance"),
    ("09_multilevel_inheritance.py", "Experiment 9: Multilevel Inheritance"),
    ("10_hierarchical_inheritance.py", "Experiment 10: Hierarchical Inheritance"),
    ("11_hybrid_inheritance.py", "Experiment 11: Hybrid Inheritance"),
    ("12_polymorphism_overloading_overriding.py", "Experiment 12: Method Overloading & Overriding"),
]

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    python_exec = sys.executable

    print("=" * 70)
    print("        RUNNING ALL EXPERIMENTS: OBJECT ORIENTED PROGRAMMING IN PYTHON")
    print("=" * 70)

    total = len(EXPERIMENTS)
    passed = 0

    for idx, (filename, description) in enumerate(EXPERIMENTS, start=1):
        filepath = os.path.join(base_dir, filename)
        print(f"\n[{idx}/{total}] RUNNING: {description} ({filename})")
        print("-" * 70)

        if not os.path.exists(filepath):
            print(f"ERROR: File {filename} not found!")
            continue

        result = subprocess.run([python_exec, filepath], capture_output=True, text=True)
        print(result.stdout.strip())
        if result.stderr:
            print("STDERR:")
            print(result.stderr.strip())

        if result.returncode == 0:
            print("-" * 70)
            print(f"[OK] {filename} completed successfully.")
            passed += 1
        else:
            print("-" * 70)
            print(f"[FAILED] {filename} exited with code {result.returncode}")

    print("\n" + "=" * 70)
    print(f"Summary: {passed}/{total} experiments executed successfully.")
    print("=" * 70)

if __name__ == "__main__":
    main()
