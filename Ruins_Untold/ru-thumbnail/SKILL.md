---
name: ru-thumbnail
description: >
  Generate a Nano Banana 2 JSON thumbnail prompt for The Ruins Untold YouTube channel.
  Use when the user asks to create a thumbnail prompt, generate a thumbnail prompt,
  design a thumbnail, or invokes /ru-thumbnail. Also use when the user says things like
  "make a thumbnail for [episode title]" or "thumbnail prompt for [topic]".
---

# ru-thumbnail

Generates structured Nano Banana 2 JSON thumbnail prompts for **The Ruins Untold** — an ancient mysteries / alternative history YouTube channel. Every prompt follows the 12-field NB2 schema and is tuned for high CTR at thumbnail scale (168×94px).

---

## Step 1: Gather inputs

Use the **AskUserQuestion** tool with TWO questions in a single call:

**Question 1 — Template** (header: "Template", single select):

| Option | Label | Description |
|---|---|---|
| 1 | Revelation Shot | Single artifact or object — dramatic vault/dig-site lighting, document element if relevant |
| 2 | Explorer Face | Host face + location background — reaction expression drives the click |
| 3 | Split Reveal | Left/right split — official story (muted) vs suppressed truth (dramatic) |
| 4 | Mystery Object | Single artifact centered on pure black — no environment, maximum impact at small size |
| 5 | Location Atmosphere | Full-bleed environment — cinematic grade, no face required |

**Question 2 — Title** (header: "Episode title", single select with Other as the expected path):
- Options: `"Type it below (use Other)"`, `"Same as last episode"`, `"I'll paste it"`, `"Still deciding"`
- The user will almost always click **Other** and type the episode title. That typed value is the title.

---

## Step 2: Generate the JSON prompt

Once you have the template choice and the episode title, generate the full 12-field Nano Banana 2 JSON prompt using the rules below.

### Universal rules (apply to every template)

- `color_palette`: always 2–4 entries; always include near-black background, ochre/gold for the primary subject, and one accent color tied to the episode's emotional register
- `negative_constraints`: always at least 6 entries; always include `"no text generated in image"`, `"no AI-smoothed textures"`, `"no lens flare"`, `"no extra limbs or figures"`
- `text_space`: always `"lower-right quadrant reserved for text overlay"` — this is where the 2–3 word text goes in post
- `style`: always `"cinematic photorealism, documentary photography, dark archaeological aesthetic"`
- `camera_or_lens.flash`: always `"none"` — practical lighting only

### Template 1 — Revelation Shot

```
subject:     The central artifact, discovery, or object tied to the episode title.
             If the episode involves documents or records, include a worn aged document
             with a visible bold-ink stamp (CLASSIFIED / DESTROYED / SUPPRESSED)
             as a secondary subject element, upper-right of frame.
context:     Sealed underground vault or deep archaeological excavation chamber.
             Atmosphere of forbidden institutional secrecy.
composition: Rule of thirds. Hero object dominant left-center.
             Document/stamp element anchored upper-right.
             Strong diagonal tension between the two focal points.
lighting:    Single hard spotlight from lower-left raking across surface texture.
             Deep absolute shadows right side and background.
             Warm amber-ochre practical light (vault lantern or dig-site work light).
palette:     near-black background, aged ochre/bone-yellow for subject,
             deep crimson-red for stamp accent, off-white parchment for document.
mood:        Revelatory, conspiratorial — forbidden knowledge surfacing.
```

### Template 2 — Explorer Face

```
subject:     Host face, left side of frame. Expression: genuine awe, disbelief, or
             intensity — not a smile. Eyes directed right toward the location or object.
             Practical environment lighting on face — no studio flash.
context:     The episode location — ruin, dig site, cave, jungle, underground chamber.
             Visible in background behind and to the right of host.
composition: Host occupies left third. Location fills right two-thirds with atmospheric
             depth. Host eye-line creates diagonal toward background focal point.
lighting:    Natural or practical only. Golden hour, torch light, or deep shadow.
             Hard-side light on face from the environment itself (not fill).
palette:     Palette follows the real environment. Do not override with color grade.
             Preserve raw skin texture — "Proof of Human" signal is critical here.
mood:        Awe, disbelief, urgency — the feeling of standing at the edge of discovery.
```

### Template 3 — Split Reveal

```
subject:     LEFT HALF: the official / mainstream version — textbook illustration,
             institutional photo, accepted theory visual. Slightly desaturated.
             RIGHT HALF: the suppressed / real version — dramatic, higher contrast,
             warmer tones. More viscerally compelling than the left.
context:     The split itself IS the context. Hard vertical cut or diagonal slash divider.
composition: Strict 50/50 horizontal split. One large spanning text optional across both
             halves (upper-center) OR small label text top of each half.
lighting:    LEFT: flat, cool, institutional. RIGHT: dramatic, warm, side-lit.
palette:     LEFT: cool grey-blue desaturated. RIGHT: warm ochre-red high contrast.
             Dividing line: white or deep crimson.
mood:        Tension, cognitive dissonance — the truth is more compelling than the story.
```

### Template 4 — Mystery Object

```
subject:     Single artifact or object from the episode. Center frame.
             Lit from above or dramatic angle. Sharp surface detail visible.
             If scale is meaningful, include a single hand holding it — no other figure.
context:     Pure black — no environment, no background detail whatsoever.
composition: Object centered, occupying 40–60% of frame height.
             All negative space is pure black.
lighting:    Single overhead or dramatic angle hard light. One-source only.
             Crisp highlight edge on one side. Pure shadow on the other.
palette:     Pure black background, object's natural material color,
             one accent highlight (gold or white) from the light edge.
mood:        Mystery, weight, significance — this object should not exist.
```

### Template 5 — Location Atmosphere

```
subject:     The location itself is the subject. No human figure required.
             One natural focal anchor (artifact, doorway, light beam, water reflection)
             as the eye-entry point.
context:     The episode's primary location — wide or medium establishing shot.
             Golden hour, storm light, deep shadow, or underground practical lighting.
composition: Full-bleed. Focal anchor positioned left-center or lower-center.
             Text space kept clear in lower-right. Horizon line if present: upper third.
lighting:    Natural or practical only. Push shadows darker in post feel.
             Pull highlights warm. Increase local contrast — do not flatten.
palette:     Blue/orange cinematic split (cool shadows, warm highlights) OR
             near-black with ochre-gold single light source for underground locations.
mood:        Ancient, forgotten, vast — the place has been waiting to be found.
```

---

## Step 3: Output format

Emit the prompt as a single clean JSON code block. No preamble, no explanation before the block.

After the block, add one line:

```
> Text overlay suggestion: [2–3 words in ALL CAPS that complete the visual question]
```

Then add one line:

```
> To generate: /kie-image [paste JSON] --model nano-banana-2 --ratio 16:9 --resolution 2K
```

Nothing else.
