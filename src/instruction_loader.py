
import os
import json

base_dir = os.path.dirname(os.path.abspath(__file__))


class Loader:

    template_path = os.path.join(base_dir, 'prompts_template')
    params_path = os.path.join(base_dir, 'params.json')

    def __init__(self):
        self.template = self.load_templates()
        self.params = self.load_params()

    def load_templates(self) -> str:
        if not os.path.exists(self.template_path):
            print(f"Template file not found: {self.template_path}")
            return ""
        with open(self.template_path, 'r') as f:
            return f.read().strip()

    def load_params(self) -> dict:
        if not os.path.exists(self.params_path):
            print(f"Params file not found: {self.params_path}")
            return {}
        with open(self.params_path, 'r') as f:
            return json.load(f)
    
    def get_instruction(self, phone: str) -> str:
        if phone not in self.params:
            return ""
        return self.template.format(**self.params[phone])



loader = Loader()


if __name__ == "__main__":
    print(loader.get_instruction("0188615651766158"))
