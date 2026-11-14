# UX Quick Reference (load on demand)

## Accessibility
- Contrast >=4.5:1 body, >=3:1 large text/UI; never color-only meaning.
- Visible `:focus-visible`; logical tab order; skip link on long pages.
- Alt text on informative images; labels on every input; ARIA only when native HTML can't.
- Honor `prefers-reduced-motion`.

## Touch & Interaction
- Targets >=44x44px (iOS) / 48dp (Android), >=8px gap.
- Feedback on every action (pressed, loading, success, error).
- No hover-only features; gestures need visible alternatives.

## Performance
- WebP/AVIF, `loading=lazy`, explicit width/height, CLS < 0.1.
- `font-display: swap`, <=2 families, subset.
- Animate `transform`/`opacity` only; avoid layout thrash.
- Code-split routes; defer non-critical JS.

## Layout & Type
- Mobile-first; test 375 / 768 / 1280; no horizontal scroll.
- 4/8px spacing scale; body >=16px, line-height ~1.5; line length 45-75ch.
- Semantic color tokens (CSS vars), not raw hex.

## Forms
- Visible labels, inline errors beside field, helper text, correct input types/autocomplete.
- Preserve input on error; disable submit only while submitting.

## States
- Always design: loading (skeleton), empty (next action), error (recovery), offline.

## Navigation
- Predictable placement; <=5 bottom-nav items; sticky header with offset anchors; deep-linkable.

## Conversion (marketing sites)
- Hero: value prop + one primary CTA + proof. Repeat CTA ~3x. Pricing clarity, FAQ for objections.
- Specific human copy; no lorem ipsum; SEO meta + OG + favicon.
