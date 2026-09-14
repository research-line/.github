# -*- coding: utf-8 -*-
"""Contract tests for research-line organization profile parity and integrity."""

import os
import re
import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

PUBLIC_REPOS = [
    ".github",
    "abc-hct",
    "ai-elite-swr",
    "crm-cosmology",
    "fst-nash",
    "functional-stability-theory",
    "rfep-framework",
    "rh-even-dominance",
]

SISTER_ORGS = [
    "open-bricks",
    "ellmos-ai",
    "file-bricks",
    "doc-bricks",
    "dev-bricks",
    "biotec-line",
    "entertain-and-more",
    "assistassets-ai",
    "um-bruch",
    "lukisch",
]

PRIVATE_LEAK_PATTERNS = [
    r"https://github\.com/research-line/[^)\s]+.*PRIVATE",
    r"visibility[\"': ]+PRIVATE",
    r"internal draft repository\s*:",
]


def get_file_content(relative_path: str) -> str:
    path = os.path.join(REPO_ROOT, relative_path)
    assert os.path.exists(path), f"File not found: {path}"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def test_markdown_fence_balance():
    """Verify all markdown files have balanced code fences."""
    md_files = [
        "README.md",
        "profile/README.md",
        "profile/README_de.md",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
    ]
    for rel_path in md_files:
        content = get_file_content(rel_path)
        fence_count = len(re.findall(r"^```", content, flags=re.MULTILINE))
        assert fence_count % 2 == 0, f"Unbalanced code fences in {rel_path} (found {fence_count})"


def test_public_repo_inventory():
    """Verify all 8 public repos are cataloged in core profile documents."""
    target_files = [
        "profile/README.md",
        "profile/README_de.md",
        "README.md",
        "llms.txt",
    ]
    for rel_path in target_files:
        content = get_file_content(rel_path)
        for repo in PUBLIC_REPOS:
            assert repo in content, f'Public repo "{repo}" missing from {rel_path}'


def test_private_repo_leak_guard():
    """Verify private/internal repo details are not exposed in public profile documents."""
    target_files = [
        "profile/README.md",
        "profile/README_de.md",
        "README.md",
        "llms.txt",
        "CHANGELOG.md",
        "SECURITY.md",
        "CONTRIBUTING.md",
    ]
    for rel_path in target_files:
        content = get_file_content(rel_path)
        for pattern in PRIVATE_LEAK_PATTERNS:
            assert not re.search(pattern, content, flags=re.IGNORECASE), (
                f'Leak-pattern violation: "{pattern}" found in {rel_path}'
            )


def test_check_timestamp_parity():
    """Verify verification date 2026-09-14 across profile files."""
    expected_iso = "2026-09-14"
    expected_de = "14. September 2026"

    en_content = get_file_content("profile/README.md")
    assert expected_iso in en_content

    de_content = get_file_content("profile/README_de.md")
    assert expected_iso in de_content or expected_de in de_content

    root_content = get_file_content("README.md")
    assert expected_iso in root_content

    llms_content = get_file_content("llms.txt")
    assert expected_iso in llms_content


def test_activity_snapshot_integrity():
    """Verify recent push activity entries in profile READMEs."""
    en_content = get_file_content("profile/README.md")
    de_content = get_file_content("profile/README_de.md")

    for push_repo in ["rh-even-dominance", "functional-stability-theory", "abc-hct", "crm-cosmology", "fst-nash", ".github"]:
        assert push_repo in en_content
        assert push_repo in de_content


def test_ecosystem_cross_linking():
    """Verify sister organization references are complete across profile docs."""
    target_files = ["profile/README.md", "profile/README_de.md", "llms.txt"]
    for rel_path in target_files:
        content = get_file_content(rel_path)
        for org in SISTER_ORGS:
            assert org in content, f'Sister org "{org}" missing from {rel_path}'


def test_mermaid_diagram_syntax():
    """Verify Mermaid flowchart blocks exist and have matching subgraph boundaries."""
    for rel_path in ["profile/README.md", "profile/README_de.md"]:
        content = get_file_content(rel_path)
        assert "```mermaid" in content
        assert "flowchart TD" in content
        subgraph_opens = len(re.findall(r"\bsubgraph\b", content))
        subgraph_ends = len(re.findall(r"\bend\b", content))
        assert subgraph_opens > 0
        assert subgraph_opens == subgraph_ends, f"Mismatched subgraph blocks in {rel_path}"


def test_utf8_encoding_and_umlauts():
    """Verify clean UTF-8 encoding and genuine German umlauts."""
    de_content = get_file_content("profile/README_de.md")
    assert "\ufffd" not in de_content, "Unicode replacement character (mojibake) in profile/README_de.md"
    assert "Öffentliche Repos" in de_content
    assert "Zahlentheorie" in de_content
    assert "übergreifenden" in de_content or "Dachstruktur" in de_content


def test_security_policy_integrity():
    """Verify security contacts and advisory links in SECURITY.md."""
    sec_content = get_file_content("SECURITY.md")
    for contact in ["security@open-bricks.org", "security@ellmos.ai", "lukas@open-bricks.org", "support@lukasgeiger.com"]:
        assert contact in sec_content, f'Missing contact "{contact}" in SECURITY.md'
    assert "GitHub Security Advisories" in sec_content
