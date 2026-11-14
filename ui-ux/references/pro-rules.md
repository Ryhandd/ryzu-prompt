# Pro Rules: Mobile/Native Polish + Canonical Checklist (load on demand)

## Mobile / Native
- Respect safe areas (notch, home indicator, status bar).
- Native conventions: back gesture, large titles (iOS), Material 3 patterns (Android).
- Touch targets 44-48px; thumb-zone primary actions.
- Virtualize lists; memoize rows; avoid re-render storms.
- Keyboard: avoid covering inputs; correct keyboard type; dismiss on scroll.
- Handle offline, slow network, permission denied, and empty data.
- Haptics/sound only as feedback, and optional.
- Store-ready: icons, splash, permissions strings, versioning.

## Canonical Pre-Delivery Checklist
- [ ] Contrast ok
- [ ] Focus visible
- [ ] Responsive at 375/768/1280
- [ ] No horizontal scroll
- [ ] No emoji icons (SVG only)
- [ ] Tokens used, no scattered hex
- [ ] Reduced-motion respected
- [ ] Images sized, lazy-loaded
- [ ] No console errors
- [ ] All links/buttons work
- [ ] No placeholders / lorem ipsum
