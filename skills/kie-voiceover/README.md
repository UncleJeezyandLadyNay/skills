# kie-voiceover

Generate voiceovers from scripts using ElevenLabs via the [kie.ai](https://kie.ai) API from inside Claude Code.

## Install

```bash
cp kie-voiceover ~/.claude/skills/kie-voiceover
```

## Requirements

```bash
export KIE_API_KEY=your_key_here
```

## Usage

```
/kie-voiceover <script text> [flags]
```

### Flags

| Flag | Default | Description |
|---|---|---|
| `--voice <id>` | `Lp2NZJAfG4zDynNcYPSz` | ElevenLabs voice ID |
| `--model <id>` | `elevenlabs/text-to-speech-turbo-2-5` | TTS model |
| `--speed <n>` | `1` | Playback rate (0.7–1.2) |
| `--stability <n>` | `0.5` | Voice consistency (0–1). Lower = more expressive |
| `--lang <code>` | auto | ISO 639-1 language code (e.g. `en`, `es`) |
| `--prev-text <text>` | — | Preceding script segment for voice continuity |
| `--next-text <text>` | — | Following script segment for voice continuity |

### Available Models

| Model ID | Description |
|---|---|
| `elevenlabs/text-to-speech-turbo-2-5` | Turbo 2.5 — fast, high quality (default) |
| `elevenlabs/text-to-speech-multilingual-v2` | Multilingual v2 — best for non-English |

## Examples

```
/kie-voiceover "In the shadow of forgotten empires, a story waits to be told."
```

```
/kie-voiceover "Chapter one. The temple had stood for three thousand years." --stability 0.3
```

```
/kie-voiceover "...and that is why historians remain baffled to this day." --speed 0.9
```

## Multi-Part Voiceovers (Voice Continuity)

For long scripts split into multiple generations, pass surrounding context to keep the delivery consistent:

```
/kie-voiceover "This is segment two of the narration." \
  --prev-text "This is segment one of the narration." \
  --next-text "This is segment three of the narration."
```

The `previous_text` and `next_text` parameters tell ElevenLabs the surrounding context so pacing and tone stay consistent across segments.

## How It Works

1. Submits to `POST https://api.kie.ai/api/v1/jobs/createTask` with model `elevenlabs/text-to-speech-turbo-2-5`
2. Polls `GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=` every 8 seconds
3. Returns the MP3 URL; optionally downloads to `~/Downloads/`

## API Reference

- [kie.ai ElevenLabs TTS docs](https://docs.kie.ai/market/elevenlabs/text-to-speech-turbo-2-5.md)
