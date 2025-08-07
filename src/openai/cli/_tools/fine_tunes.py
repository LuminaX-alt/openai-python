import click
from openai import OpenAI, AsyncOpenAI

@click.group()
def chat_fine_tunes():
    """CLI tools for chat fine‑tuning (e.g., gpt-3.5‑turbo style)."""
    pass

@chat_fine_tunes.command("prepare-data")
@click.option("--input", "-i", required=True, help="Path to JSONL with chat messages rows.")
@click.option("--output", "-o", default="prepared_chat.jsonl", help="Output file path.")
def prepare_data(input: str, output: str):
    """
    Prepare chat‑formatted data for fine‑tuning.
    Converts structured 'messages' JSONL into prompt-completion pairs or validates format.
    """
    import json
    valid = []
    with open(input, 'r') as f:
        for line in f:
            obj = json.loads(line)
            if "messages" not in obj:
                click.echo(f"Skipping invalid line (no messages): {obj}", err=True)
                continue
            valid.append(line)
    with open(output, 'w') as fo:
        fo.writelines(valid)
    click.echo(f"Saved validated chat‑formatted entries to {output}")

@chat_fine_tunes.command("create")
@click.option("--training_file", "-t", required=True, help="ID or path of uploaded training file.")
@click.option("--validation_file", "-v", help="ID or path of uploaded validation file.")
@click.option("--model", "-m", default="gpt-3.5‑turbo", help="Base model to fine‑tune.")
def create(training_file: str, validation_file: str, model: str):
    """
    Create a chat fine‑tuning job.
    """
    client = OpenAI()
    response = client.fine_tunes.create(
        training_file=training_file,
        validation_file=validation_file,
        model=model
    )
    click.echo(f"Chat fine‑tune job created: {response['id']}")

@chat_fine_tunes.command("list")
def list_jobs():
    """List chat fine‑tuning jobs."""
    client = OpenAI()
    jobs = client.fine_tunes.list()
    click.echo(jobs)

@chat_fine_tunes.command("events")
@click.argument("job_id")
def events(job_id: str):
    """Stream events for a chat fine‑tune job."""
    client = OpenAI()
    for e in client.fine_tunes.list_events(id=job_id, stream=True):
        click.echo(e)

@chat_fine_tunes.command("delete")
@click.argument("job_id")
def delete(job_id: str):
    """Delete a chat fine‑tune job."""
    client = OpenAI()
    client.fine_tunes.cancel(id=job_id)
    click.echo(f"Canceled chat fine‑tune job {job_id}")
from openai.cli.fine_tunes import chat_fine_tunes

cli.add_command(chat_fine_tunes, name="chat_fine_tunes")

from __future__ import annotations

import sys
from typing import TYPE_CHECKING
from argparse import ArgumentParser

from .._models import BaseModel
from ...lib._validators import (
    get_validators,
    write_out_file,
    read_any_format,
    apply_validators,
    apply_necessary_remediation,
)

if TYPE_CHECKING:
    from argparse import _SubParsersAction


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser("fine_tunes.prepare_data")
    sub.add_argument(
        "-f",
        "--file",
        required=True,
        help="JSONL, JSON, CSV, TSV, TXT or XLSX file containing prompt-completion examples to be analyzed."
        "This should be the local file path.",
    )
    sub.add_argument(
        "-q",
        "--quiet",
        required=False,
        action="store_true",
        help="Auto accepts all suggestions, without asking for user input. To be used within scripts.",
    )
    sub.set_defaults(func=prepare_data, args_model=PrepareDataArgs)


class PrepareDataArgs(BaseModel):
    file: str

    quiet: bool


def prepare_data(args: PrepareDataArgs) -> None:
    sys.stdout.write("Analyzing...\n")
    fname = args.file
    auto_accept = args.quiet
    df, remediation = read_any_format(fname)
    apply_necessary_remediation(None, remediation)

    validators = get_validators()

    assert df is not None

    apply_validators(
        df,
        fname,
        remediation,
        validators,
        auto_accept,
        write_out_file_func=write_out_file,
    )
