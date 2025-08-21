from typing import Any
from openai import OpenAI
import openai.resources.evals.evals as evals_mod

# Fix missing forward reference
evals_mod.Input = Any

client = OpenAI()

eval_cfg = client.evals.create(
    name="visio_json_exact_match",
    data_source_config={
        "type": "custom",
        "item_schema": {
            "type": "object",
            "properties": {
                "prompt": {"type": "string"},
                "expected": {"type": "string"}
            },
            "required": ["prompt", "expected"]
        },
        "include_sample_schema": True
    },
    testing_criteria=[
        {
            "type": "string_check",
            "name": "Exact JSON match",
            "operation": "eq",
            "input": "{{sample.output_text}}",
            "reference": "{{item.expected}}"
        }
    ]
)

print("Eval created successfully:", eval_cfg)
