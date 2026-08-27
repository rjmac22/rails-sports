#!/usr/bin/env python3
"""Validate story_map.json and render story_map.md.

Uses only the Python standard library.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "story_map.json"
OUTPUT_PATH = ROOT / "story_map.md"

VALID_DECISIONS = {"keep", "keep_short", "likely", "bridge_only", "optional", "drop"}
VALID_REPORTING = {
    "to_report",
    "partial",
    "reported",
    "reported_enough",
    "enough_for_bridge",
}


def load_data() -> dict:
    with DATA_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def validate(data: dict) -> None:
    evidence = {item["id"]: item for item in data["evidence"]}
    if len(evidence) != len(data["evidence"]):
        raise ValueError("Duplicate evidence id")

    question_ids = [q["id"] for q in data["questions"]]
    if len(set(question_ids)) != len(question_ids):
        raise ValueError("Duplicate question id")

    for question in data["questions"]:
        missing = [eid for eid in question["evidence_ids"] if eid not in evidence]
        if missing:
            raise ValueError(
                f"{question['id']} references missing evidence ids: {', '.join(missing)}"
            )
        if question["decision"] not in VALID_DECISIONS:
            raise ValueError(
                f"{question['id']} has invalid decision: {question['decision']}"
            )
        if question["reporting_status"] not in VALID_REPORTING:
            raise ValueError(
                f"{question['id']} has invalid reporting status: "
                f"{question['reporting_status']}"
            )


def label(value: str) -> str:
    return value.replace("_", " ")


def render(data: dict) -> str:
    evidence = {item["id"]: item for item in data["evidence"]}

    lines = [
        f"# {data['title']}",
        "",
        f"Source study: `{data['source_study']}`",
        "",
        data["purpose"],
        "",
        "This file is generated from `story_map.json`. Edit the JSON, then run:",
        "",
        "```bash",
        "python reporting/cricket_winning_the_game/build_story_map.py",
        "```",
        "",
        "## Question-to-evidence map",
        "",
        "| Study question | Analytical point | Evidence | Article role | Decision | Reporting |",
        "|---|---|---|---|---|---|",
    ]

    for q in data["questions"]:
        evidence_labels = "<br>".join(evidence[eid]["label"] for eid in q["evidence_ids"])
        lines.append(
            "| {question} | {point} | {evidence} | {role} | {decision} | {status} |".format(
                question=q["study_question"],
                point=q["analytical_point"],
                evidence=evidence_labels,
                role=label(q["article_role"]),
                decision=label(q["decision"]),
                status=label(q["reporting_status"]),
            )
        )

    lines += ["", "## Evidence jobs", ""]

    for item in data["evidence"]:
        lines += [
            f"### {item['label']}",
            "",
            f"- Type: {label(item['type'])}",
            f"- Reporting file: `{item['reporting_file']}`",
            f"- Status: {label(item['status'])}",
            f"- Job: {item['job']}",
            "",
        ]

    lines += ["## Guardrails", ""]
    lines += [f"- {guardrail}" for guardrail in data["guardrails"]]
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    data = load_data()
    validate(data)
    OUTPUT_PATH.write_text(render(data), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH.relative_to(ROOT.parent.parent)}")


if __name__ == "__main__":
    main()
