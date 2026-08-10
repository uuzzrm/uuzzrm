#!/usr/bin/env python3
"""Update the account-level repository star history used by the profile README."""

from __future__ import annotations

import html
import json
import math
import os
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
OWNER = "uuzzrm"
HISTORY_PATH = ROOT / "data" / "account-stars.json"
LIGHT_SVG_PATH = ROOT / "assets" / "account-stars-light.svg"
DARK_SVG_PATH = ROOT / "assets" / "account-stars-dark.svg"


def github_json(url: str) -> object:
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "uuzzrm-profile-star-history",
        },
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")

    with urlopen(request, timeout=30) as response:
        return json.load(response)


def fetch_repositories() -> list[dict[str, object]]:
    repositories: list[dict[str, object]] = []
    page = 1

    while True:
        payload = github_json(
            f"https://api.github.com/users/{OWNER}/repos?per_page=100&page={page}&sort=full_name"
        )
        if not isinstance(payload, list):
            raise RuntimeError("GitHub returned an unexpected repository payload")

        repositories.extend(item for item in payload if isinstance(item, dict))
        if len(payload) < 100:
            break
        page += 1

    return repositories


def build_snapshot(repositories: list[dict[str, object]], today: str) -> dict[str, object]:
    tracked: list[dict[str, object]] = []

    for repository in repositories:
        full_name = str(repository.get("full_name", ""))
        if not full_name:
            continue
        if bool(repository.get("private")):
            continue

        tracked.append(
            {
                "full_name": full_name,
                "stars": int(repository.get("stargazers_count", 0)),
                "fork": bool(repository.get("fork")),
            }
        )

    tracked.sort(key=lambda item: str(item["full_name"]).lower())
    return {
        "date": today,
        "total_stars": sum(int(item["stars"]) for item in tracked),
        "repository_count": len(tracked),
        "repositories": tracked,
    }


def load_existing() -> dict[str, object]:
    if not HISTORY_PATH.exists():
        return {"history": []}

    with HISTORY_PATH.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise RuntimeError("Existing account star history is not an object")
    return payload


def update_history(snapshot: dict[str, object]) -> dict[str, object]:
    existing = load_existing()
    history = existing.get("history", [])
    if not isinstance(history, list):
        history = []

    history = [item for item in history if isinstance(item, dict)]
    if history and history[-1].get("date") == snapshot["date"]:
        history[-1] = {
            "date": snapshot["date"],
            "total_stars": snapshot["total_stars"],
            "repository_count": snapshot["repository_count"],
        }
    else:
        history.append(
            {
                "date": snapshot["date"],
                "total_stars": snapshot["total_stars"],
                "repository_count": snapshot["repository_count"],
            }
        )

    return {
        "owner": OWNER,
        "metric": "total stars received by tracked public repositories",
        "history": history,
        "latest": snapshot,
    }


def format_count(value: int) -> str:
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if value >= 1_000:
        return f"{value / 1_000:.1f}K"
    return f"{value:,}"


def nice_top(value: int) -> int:
    if value <= 0:
        return 0
    magnitude = 10 ** math.floor(math.log10(value))
    normalized = value / magnitude
    step = 1 if normalized <= 1 else 2 if normalized <= 2 else 5 if normalized <= 5 else 10
    return int(step * magnitude)


def svg_text(value: object) -> str:
    return html.escape(str(value), quote=True)


def make_svg(payload: dict[str, object], *, dark: bool) -> str:
    history = payload.get("history", [])
    if not isinstance(history, list):
        history = []

    points = [item for item in history if isinstance(item, dict)]
    latest = payload.get("latest", {})
    if not isinstance(latest, dict):
        latest = {}

    total_stars = int(latest.get("total_stars", points[-1].get("total_stars", 0) if points else 0))
    repository_count = int(latest.get("repository_count", 0))
    first_date = str(points[0].get("date", "—")) if points else "—"
    latest_date = str(latest.get("date", points[-1].get("date", "—") if points else "—"))
    max_value = max((int(item.get("total_stars", 0)) for item in points), default=0)
    top_value = nice_top(max_value)

    colors = {
        "background": "#0d1117" if dark else "#ffffff",
        "panel": "#111827" if dark else "#f8fafc",
        "text": "#f0f6fc" if dark else "#111827",
        "muted": "#8b949e" if dark else "#64748b",
        "grid": "#273244" if dark else "#e2e8f0",
        "border": "#253047" if dark else "#dbeafe",
        "line": "#7dd3fc" if dark else "#2563eb",
        "dot": "#f0f6fc" if dark else "#0f172a",
        "halo": "#172554" if dark else "#eff6ff",
    }

    width, height = 1000, 560
    left, right, chart_top, chart_bottom = 92, 948, 170, 420
    chart_width = right - left
    chart_height = chart_bottom - chart_top

    def parse_day(raw: object) -> date | None:
        try:
            return date.fromisoformat(str(raw))
        except ValueError:
            return None

    dates = [parse_day(item.get("date")) for item in points]
    valid_dates = [item for item in dates if item is not None]
    first_day = min(valid_dates) if valid_dates else None
    last_day = max(valid_dates) if valid_dates else None
    span = (last_day - first_day).days if first_day and last_day else 0

    def x_position(index: int) -> float:
        if not points:
            return float(left)
        if span > 0 and dates[index] is not None and first_day is not None:
            return left + ((dates[index] - first_day).days / span) * chart_width
        if len(points) == 1:
            return float(right)
        return left + (index / (len(points) - 1)) * chart_width

    def y_position(value: int) -> float:
        if top_value <= 0:
            return float(chart_bottom)
        return chart_bottom - (value / top_value) * chart_height

    line_points = [(x_position(index), y_position(int(item.get("total_stars", 0)))) for index, item in enumerate(points)]
    if line_points:
        if len(line_points) == 1:
            path = f"M {left} {line_points[0][1]:.2f} L {right} {line_points[0][1]:.2f}"
        else:
            path = "M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in line_points)
    else:
        path = f"M {left} {chart_bottom} L {right} {chart_bottom}"

    grid_markup: list[str] = []
    tick_values = [0] if top_value <= 0 else [round(top_value * index / 4) for index in range(5)]
    for tick in tick_values:
        y = y_position(tick)
        grid_markup.append(
            f'<line x1="{left}" y1="{y:.2f}" x2="{right}" y2="{y:.2f}" stroke="{colors["grid"]}" stroke-width="1" />'
        )
        grid_markup.append(
            f'<text x="{left - 18}" y="{y + 5:.2f}" text-anchor="end" fill="{colors["muted"]}" font-size="14">{svg_text(format_count(tick))}</text>'
        )

    date_markup = ""
    if points:
        first_x = x_position(0)
        last_x = x_position(len(points) - 1)
        if len(points) == 1:
            date_markup = f'<text x="{right}" y="{chart_bottom + 34}" text-anchor="end" fill="{colors["muted"]}" font-size="14">{svg_text(latest_date)}</text>'
        else:
            date_markup = (
                f'<text x="{first_x:.2f}" y="{chart_bottom + 34}" text-anchor="start" fill="{colors["muted"]}" font-size="14">{svg_text(first_date)}</text>'
                f'<text x="{last_x:.2f}" y="{chart_bottom + 34}" text-anchor="end" fill="{colors["muted"]}" font-size="14">{svg_text(latest_date)}</text>'
            )

    dots_markup = "".join(
        f'<circle cx="{x:.2f}" cy="{y:.2f}" r="4" fill="{colors["dot"]}" stroke="{colors["line"]}" stroke-width="3" />'
        for x, y in line_points[-1:]
    )

    description = (
        f"{OWNER} account repository star history. {total_stars} total stars across "
        f"{repository_count} public repositories."
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">{svg_text(OWNER)} account repository star history</title>
  <desc id="desc">{svg_text(description)}</desc>
  <rect width="{width}" height="{height}" rx="28" fill="{colors["background"]}" />
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="27" fill="none" stroke="{colors["border"]}" />
  <circle cx="865" cy="66" r="110" fill="{colors["halo"]}" opacity="0.7" />
  <text x="56" y="62" fill="{colors["text"]}" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" font-size="26" font-weight="650">{svg_text(OWNER)} / repository stars</text>
  <text x="56" y="91" fill="{colors["muted"]}" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" font-size="15">Total stars received by tracked public repositories</text>
  <text x="944" y="60" text-anchor="end" fill="{colors["text"]}" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" font-size="34" font-weight="650">{svg_text(format_count(total_stars))}</text>
  <text x="944" y="88" text-anchor="end" fill="{colors["muted"]}" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" font-size="14">stars · updated {svg_text(latest_date)}</text>
  <g font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
    {''.join(grid_markup)}
    <path d="{path}" fill="none" stroke="{colors["line"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
    {dots_markup}
    {date_markup}
  </g>
  <line x1="56" y1="484" x2="944" y2="484" stroke="{colors["grid"]}" stroke-width="1" />
  <text x="56" y="516" fill="{colors["muted"]}" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" font-size="13">{svg_text(repository_count)} public repositories · forks count only their own stars</text>
  <text x="944" y="516" text-anchor="end" fill="{colors["muted"]}" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" font-size="13">history from {svg_text(first_date)}</text>
</svg>
'''


def write_outputs(payload: dict[str, object]) -> None:
    HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LIGHT_SVG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with HISTORY_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    LIGHT_SVG_PATH.write_text(make_svg(payload, dark=False), encoding="utf-8", newline="\n")
    DARK_SVG_PATH.write_text(make_svg(payload, dark=True), encoding="utf-8", newline="\n")


def main() -> None:
    today = datetime.now(timezone.utc).date().isoformat()
    snapshot = build_snapshot(fetch_repositories(), today)
    payload = update_history(snapshot)
    write_outputs(payload)
    print(
        f"Tracked {snapshot['repository_count']} public repositories; "
        f"total stars: {snapshot['total_stars']} ({today})"
    )


if __name__ == "__main__":
    main()
