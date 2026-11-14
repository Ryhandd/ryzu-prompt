#!/usr/bin/env python3
"""ryzu-prompt design-intelligence search. Python 3 stdlib only."""
import argparse, csv, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
DOMAINS = {
    "ux": "ux-guidelines.csv", "style": "styles.csv", "color": "colors.csv",
    "typography": "typography.csv", "landing": "landing.csv", "chart": "charts.csv",
    "react": "react-perf.csv", "web": "web-interface.csv", "icons": "icons.csv",
    "google-fonts": "google-fonts.csv", "gsap": "gsap.csv", "product": "products.csv",
}
STACKS = ["react", "nextjs", "vue", "svelte", "astro", "html-tailwind", "shadcn",
          "react-native", "flutter", "swiftui", "jetpack-compose", "threejs"]


def load(path):
    if not os.path.isfile(path):
        sys.exit(f"[missing] {path}")
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def tok(s):
    return [t for t in re.findall(r"[a-z0-9]+", s.lower()) if len(t) > 1]


def score(row, qt):
    kw = set(tok(row.get("keywords", "")))
    name = set(tok(row.get("name", "")))
    body = set(tok(" ".join(v for k, v in row.items() if k not in ("keywords", "name") and v)))
    s = 0.0
    for t in qt:
        if t in kw:
            s += 3
        if t in name:
            s += 2
        if t in body:
            s += 1
    return s


def search(rows, query, n=3):
    qt = tok(query)
    ranked = sorted(((score(r, qt), r) for r in rows), key=lambda x: -x[0])
    return [r for s, r in ranked if s > 0][:n]


def fmt(row):
    return "\n".join(f"- {k}: {v}" for k, v in row.items() if v and k != "keywords")


def find(rows, name):
    name = (name or "").lower()
    for r in rows:
        if r.get("name", "").lower() == name:
            return r
    hit = search(rows, name, 1)
    return hit[0] if hit else None


def design_system(query, project, var, mot, den):
    products = load(os.path.join(DATA, "products.csv"))
    hit = search(products, query, 1)
    p = hit[0] if hit else products[0]
    style = find(load(os.path.join(DATA, "styles.csv")), p["style"])
    color = find(load(os.path.join(DATA, "colors.csv")), p["palette"])
    typo = find(load(os.path.join(DATA, "typography.csv")), p["typography"])
    land = find(load(os.path.join(DATA, "landing.csv")), p["landing"])
    out = [f"# Design System: {project or p['name']}",
           f"Query: {query}", f"Matched product: {p['name']}",
           f"Dials -> variance {var}/10 | motion {mot}/10 | density {den}/10", ""]
    for title, r in (("STYLE", style), ("COLOR", color), ("TYPOGRAPHY", typo), ("LANDING PATTERN", land)):
        out += [f"## {title}", fmt(r) if r else "- (no match)", ""]
    out += [
        "## DIAL GUIDE",
        f"- Variance {var}: " + ("asymmetric, overlapping, off-grid hero" if var >= 7 else "balanced, symmetric grid" if var >= 4 else "strict, conventional layout"),
        f"- Motion {mot}: " + ("scroll-reveal + stagger + parallax (GSAP ok)" if mot >= 7 else "tasteful reveals + micro-interactions" if mot >= 4 else "minimal transitions only"),
        f"- Density {den}: " + ("compact, data-rich, small gaps" if den >= 7 else "moderate spacing" if den >= 4 else "airy, large whitespace"),
        "",
        "## ANTI-PATTERNS",
        "- Emoji icons, purple-gradient cliches, lorem ipsum, gray-on-gray text, hardcoded hex, hover-only actions.",
    ]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="ryzu-prompt design search")
    ap.add_argument("query")
    ap.add_argument("--design-system", action="store_true")
    ap.add_argument("-p", "--project", default="")
    ap.add_argument("--domain", choices=sorted(DOMAINS))
    ap.add_argument("--stack", choices=STACKS)
    ap.add_argument("-n", "--max-results", type=int, default=3)
    ap.add_argument("--variance", type=int, default=7)
    ap.add_argument("--motion", type=int, default=6)
    ap.add_argument("--density", type=int, default=4)
    ap.add_argument("--persist", action="store_true")
    ap.add_argument("--output-dir", default=".")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    if a.design_system:
        text = design_system(a.query, a.project, a.variance, a.motion, a.density)
        print(text)
        if a.persist:
            d = os.path.join(a.output_dir, "design-system")
            os.makedirs(d, exist_ok=True)
            f = os.path.join(d, "MASTER.md")
            if os.path.exists(f) and not a.force:
                sys.exit(f"\n[skip] {f} exists. Use --force to overwrite.")
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(text + "\n")
            print(f"\n[saved] {f}")
        return

    if a.stack:
        rows = load(os.path.join(DATA, "stacks", f"{a.stack}.csv"))
    else:
        rows = load(os.path.join(DATA, DOMAINS[a.domain or "ux"]))
    res = search(rows, a.query, a.max_results)
    if not res:
        print("[no match] gunakan general guidance.")
        return
    for i, r in enumerate(res, 1):
        print(f"### Result {i}\n{fmt(r)}\n")


if __name__ == "__main__":
    main()
