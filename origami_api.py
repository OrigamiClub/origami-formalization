import json
from pathlib import Path
from typing import Any, Dict, List, Union


class OrigamiAPI:
    """
    Manages the state of Huzita axioms and generates Lean code.
    """

    def __init__(self):
        self.axioms: List[Dict[str, Any]] = []

    def add_axiom(self, axiom_type: int, params: Dict[str, Any]) -> None:
        """
        Validates and adds a Huzita axiom to the stack.
        """
        self._validate_axiom(axiom_type, params)
        self.axioms.append({"type": axiom_type, "params": params})

    def _validate_axiom(self, axiom_type: int, params: Dict[str, Any]) -> None:
        """
        Validates the parameters for a given axiom type.
        """
        if axiom_type == 1:
            if not ("p1" in params and "p2" in params):
                raise ValueError("Axiom 1 requires two points (p1, p2)")
        elif axiom_type == 2:
            if not ("p1" in params and "p2" in params):
                raise ValueError("Axiom 2 requires two points (p1, p2)")
        elif axiom_type == 3:
            if not ("l1" in params and "l2" in params):
                raise ValueError("Axiom 3 requires two lines (l1, l2)")
        elif axiom_type == 4:
            if not ("p1" in params and "l1" in params):
                raise ValueError("Axiom 4 requires a point (p1) and a line (l1)")
        elif axiom_type == 5:
            if not ("p1" in params and "p2" in params and "l1" in params):
                raise ValueError("Axiom 5 requires two points (p1, p2) and a line (l1)")
        elif axiom_type == 6:
            if not ("p1" in params and "p2" in params and "l1" in params and "l2" in params):
                raise ValueError("Axiom 6 requires two points (p1, p2) and two lines (l1, l2)")
        elif axiom_type == 7:
            if not ("p1" in params and "l1" in params and "l2" in params):
                raise ValueError("Axiom 7 requires a point (p1) and two lines (l1, l2)")
        else:
            raise ValueError(f"Unknown axiom type: {axiom_type}")

    def generate_lean_code(self) -> str:
        """
        Generates a Lean script from the axiom stack.
        """
        if not self.axioms:
            return "import Origami.V1\\n\\nopen Origami V1\\n\\ndef construction : Construction :=\\nby {\\n  -- No axioms in the stack.\\n}"

        lean_code = "import Origami.V1\n\n"
        lean_code += "open Origami V1\n\n"
        lean_code += "def construction : Construction :=\n"
        lean_code += "by {\n"

        for i, axiom in enumerate(self.axioms):
            axiom_type = axiom["type"]
            params = axiom["params"]
            param_string = " ".join(params.values())
            lean_code += f"  h{i+1}: apply axiom{axiom_type} {param_string}\n"

        lean_code += "}\n"
        return lean_code

    def write_lean_file(self, output_path: Union[str, Path]) -> None:
        """
        Writes the generated Lean code to a file.
        """
        lean_code = self.generate_lean_code()
        Path(output_path).write_text(lean_code, encoding="utf-8")

    def clear(self) -> None:
        """
        Clears the axiom stack.
        """
        self.axioms = []
