import os

class OutputWriter:
    """
    Responsible for exporting the finalized architecture and code to the filesystem.
    """
    def __init__(self, base_path="./entropia_out"):
        self.base_path = base_path

    def write(self, project_name: str, content: dict):
        output_dir = os.path.join(self.base_path, project_name)
        os.makedirs(output_dir, exist_ok=True)
        print(f"[Writer] Project exported to {output_dir}")
        # Logic to write files
