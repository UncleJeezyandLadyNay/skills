# ru-thumbnail

**Skill for:** The Ruins Untold YouTube Channel  
**Type:** Thumbnail Prompt Generation  
**Output:** Nano Banana 2 JSON prompt + text overlay suggestion + ready-to-run `/kie-image` command

---

## What It Does

Generates structured **Nano Banana 2 JSON thumbnail prompts** for The Ruins Untold — an ancient mysteries / alternative history YouTube channel.

Invoke it, pick a template, enter an episode title. It outputs a complete 12-field NB2 JSON prompt tuned for:

- Maximum CTR at 168×94px thumbnail scale
- The channel's cinematic dark-archaeological visual identity
- The genre-native color palette: near-black, ochre/gold, crimson accent
- Real tactile textures over AI-smoothed surfaces ("Proof of Human" signal)
- `text_space` always reserved lower-right for 2–3 word post-production overlay

---

## Install

```bash
cp -r ru-thumbnail ~/.claude/skills/ru-thumbnail
```

---

## Usage

```
/ru-thumbnail
```

The skill asks two questions:

1. **Which template?** — pick from the 5 types below
2. **Episode title** — type it in the "Other" field

Then outputs the full JSON prompt, a text overlay suggestion, and the `/kie-image` command.

---

## The 5 Templates

### 1. Revelation Shot
*Best for: discovery episodes, cover-up reveals, document/record evidence*

The hero artifact or object occupies left-center. If the episode involves institutional suppression, a worn aged document with a bold red **DESTROYED** or **CLASSIFIED** ink stamp anchors the upper-right. Hard spotlight from lower-left rakes across surface texture. Deep absolute shadows everywhere else.

**Fires on:** "The Smithsonian Destroyed Giants", "Their Own Records Prove It", "What NASA Found and Never Told You"

```
Palette:    near-black | aged ochre/bone-yellow | deep crimson-red | off-white parchment
Lighting:   single hard spotlight, lower-left, vault lantern quality
Mood:       forbidden knowledge surfacing
```

---

### 2. Explorer Face
*Best for: on-location episodes, field content, host reaction moments*

Host face left-third of frame, expression of genuine awe or disbelief — not a smile. Eyes directed right toward the location behind them. The environment provides the lighting — no studio flash, no fill. Real skin texture is the signal.

**Fires on:** "I Went Inside the Sealed Chamber", "What I Found Beneath Giza", "Standing Inside Puma Punku"

```
Palette:    follows the real location — do not override with color grade
Lighting:   practical only — golden hour, torch, deep shadow
Mood:       standing at the edge of discovery
```

---

### 3. Split Reveal
*Best for: "official story vs truth" episodes, mainstream vs evidence comparisons*

Hard 50/50 vertical cut. Left side: the accepted version — textbook illustration, institutional photo, desaturated and cool. Right side: the suppressed version — dramatically lit, warm, more viscerally compelling. The tension between the two halves is the click trigger.

**Fires on:** "What History Books Say vs What the Stones Show", "Egypt: Official Version vs What Geologists Found"

```
Palette:    LEFT cool grey-blue | RIGHT warm ochre-red | divider white or deep crimson
Lighting:   LEFT flat institutional | RIGHT dramatic warm side-light
Mood:       cognitive dissonance — the truth is more compelling
```

---

### 4. Mystery Object
*Best for: artifact episodes, out-of-place technology, "this shouldn't exist" content*

Pure black background. Single artifact centered, occupying 40–60% of frame height. One hard light source — crisp highlight edge, pure shadow on the other side. No environment, no context, no other figure. Maximum readability at tiny thumbnail size.

**Fires on:** "Antikythera: The Device That Shouldn't Exist", "The Baghdad Battery", "Crystal Skulls: The Truth"

```
Palette:    pure black | object's natural material color | single gold/white highlight edge
Lighting:   one hard overhead or angled source only
Mood:       this object should not exist
```

---

### 5. Location Atmosphere
*Best for: site deep-dives, place-focused episodes, no face required*

Full-bleed environment shot. One natural focal anchor — an artifact, doorway, light beam, or water reflection — draws the eye. Cinematic grade: shadows darker, highlights warm, local contrast increased. Blue/orange split for surface locations; ochre-gold on near-black for underground.

**Fires on:** "The Hidden Rooms Beneath the Sphinx", "Nan Madol: Who Built This?", "Göbekli Tepe: The Site They Tried to Bury"

```
Palette:    blue/orange cinematic split (surface) OR near-black + ochre-gold (underground)
Lighting:   natural or practical only — golden hour, storm, deep shadow
Mood:       ancient, forgotten, the place has been waiting to be found
```

---

## Output Format

The skill emits three things and nothing else:

```json
{
  "goal": "...",
  "subject": ["...", "..."],
  "context": "...",
  "style": "cinematic photorealism, documentary photography, dark archaeological aesthetic",
  "composition": "...",
  "lighting": "...",
  "color_palette": ["...", "...", "..."],
  "background": "...",
  "camera_or_lens": {
    "type": "...",
    "lens": "...",
    "aperture": "...",
    "shutter_speed": "...",
    "ISO": "...",
    "flash": "none"
  },
  "mood": "...",
  "text_space": "lower-right quadrant reserved for text overlay",
  "negative_constraints": ["...", "...", "...", "...", "...", "..."]
}
```

> Text overlay suggestion: `[2–3 WORDS IN ALL CAPS]`

> To generate: `/kie-image [paste JSON] --model nano-banana-2 --ratio 16:9 --resolution 2K`

---

## JSON Field Reference

| Field | Type | Rules |
|---|---|---|
| `goal` | string | Episode title + channel context anchor |
| `subject` | array | Physical traits of main subject — always an array, never a single string |
| `context` | string | Environment/location description |
| `style` | string | Always `"cinematic photorealism, documentary photography, dark archaeological aesthetic"` |
| `composition` | string | Framing, focal placement, text-safe zone |
| `lighting` | string | Source + direction + quality — all three required |
| `color_palette` | array | 2–4 entries, always includes near-black background and ochre/gold subject |
| `background` | string | Detailed environment — no modern surfaces unless the episode requires it |
| `camera_or_lens` | object | `flash` always `"none"` — practical lighting only |
| `mood` | string | Emotional register of the image |
| `text_space` | string | Always `"lower-right quadrant reserved for text overlay"` |
| `negative_constraints` | array | Minimum 6 entries — always includes no AI textures, no lens flare, no in-image text |

---

## Why JSON Prompting?

Natural language prompts bleed. Change one word and the lighting, composition, and mood all shift together. JSON isolates each element into its own field — changing `lighting` doesn't touch `subject` or `color_palette`.

| Metric | Natural language | JSON |
|---|---|---|
| Color/lighting/composition precision | 68% | 92% |
| Character variation between generations | ~20% | <3% |
| Pose/style retention | baseline | +40% |
| Complex scene accuracy | baseline | +60–80% |

*Source: Nano Banana 2 community benchmarks, May 2026*

---

## Research Behind the Templates

These templates were built from a `/last30days` research pass on YouTube thumbnail performance (May 2026):

- **Faces** increase CTR 20–30% — requires genuine expression, not a posed smile
- **High contrast** improves CTR 20–40% — red/white, yellow/black, blue/orange outperform
- **Text: 2–3 words max** — longer text drops CTR even when the copy is strong
- **"Proof of Human" trend** — real skin textures outperform AI-polished faces by 22% in long-term click satisfaction as AI thumbnail saturation increases
- **One dominant focal point** — thumbnails trying to show two things test lower than thumbnails committed to one
- **Left-weighted composition** — critical elements on left side; eyes land there first on horizontal scroll
- **Dark mode optimization** — dark backgrounds with warm/neon accents rising with dark mode adoption

The genre-native palette for ancient history and mysteries: **near-black shadows + ochre/gold highlights + one high-saturation accent**. This maps naturally to vault lighting, torch light, and archaeological site photography while passing the thumbnail-wall legibility test at small sizes.

---

## Example Output

**Episode:** *Antikythera — The Device That Shouldn't Exist*  
**Template:** Revelation Shot

```json
{
  "goal": "YouTube thumbnail for 'Antikythera — The Device That Shouldn't Exist' — cinematic revelation shot of the Antikythera mechanism for an ancient mysteries channel, optimized for CTR at 168x94px",
  "subject": [
    "the Antikythera mechanism — corroded bronze gear assembly, heavily encrusted with verdigris and mineral deposits",
    "interlocking gear teeth and inscribed astronomical dials visible under raking light, surface texture showing centuries of corrosion and calcification",
    "fragment angled to reveal maximum mechanical complexity — gears overlapping, depth of the device fully apparent",
    "no human figures — the object itself is the revelation"
  ],
  "context": "deep archaeological vault or maritime excavation chamber, stone and sediment surfaces barely visible in deep shadow, atmosphere of a discovery that rewrites history",
  "style": "cinematic photorealism, documentary photography, dark archaeological aesthetic — real tactile surface textures throughout, no AI smoothing",
  "composition": "rule of thirds, mechanism dominant left-center occupying 55-60% of frame width, deep void filling upper-right, strong diagonal from lower-left light source across mechanism face, lower-right quadrant kept fully clear for text overlay, all critical detail within center-safe zone",
  "lighting": "single hard spotlight from lower-left raking across gear surfaces and inscribed dials to reveal maximum texture depth, deep absolute shadows filling right side and background, warm amber-ochre practical light suggesting a dim vault lantern, no fill light — shadow edges are hard and uncompromising",
  "color_palette": [
    "near-black background — #080806",
    "aged verdigris green and corroded bronze — #4a6741 and #7a5c2e",
    "warm amber-gold highlight edge from key light — #c8922a"
  ],
  "background": "rough stone and sediment barely visible at frame edges, deep shadow throughout, no modern surfaces or materials, atmosphere of a sealed chamber undisturbed for two thousand years",
  "camera_or_lens": {
    "type": "DSLR documentary",
    "lens": "85mm",
    "aperture": "f/2.8",
    "shutter_speed": "1/125",
    "ISO": "400",
    "flash": "none"
  },
  "mood": "revelatory, impossible — this object should not exist, the weight of a lost civilization made physical",
  "text_space": "lower-right quadrant reserved for text overlay",
  "negative_constraints": [
    "no text generated in image",
    "no AI-smoothed textures — surface must show real corrosion pits, mineral encrustation, and gear wear",
    "no lens flare",
    "no extra limbs or figures",
    "no museum display lighting or white background",
    "no clean or pristine metal — full corrosion and patina required throughout",
    "no modern tools, labels, or display cases visible",
    "no bright or saturated colors outside the defined palette"
  ]
}
```

> Text overlay suggestion: `SHOULDN'T EXIST`

> To generate: `/kie-image [paste JSON] --model nano-banana-2 --ratio 16:9 --resolution 2K`

---

## Related Skills

| Skill | What it does |
|---|---|
| [`RU_ideas`](../RU_ideas/) | Generates structured video ideas with evidence, researchers, and hook style |
| [`kie-image`](../../skills/kie-image/) | Generates the actual thumbnail image via kie.ai nano-banana-2 |
