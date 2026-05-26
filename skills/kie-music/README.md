# kie-music

Generate background music using Suno AI via the [kie.ai](https://kie.ai) API from inside Claude Code.

## Install

```bash
cp kie-music ~/.claude/skills/kie-music
```

## Requirements

```bash
export KIE_API_KEY=your_key_here
```

## Usage

```
/kie-music <description> [flags]
```

### Flags

| Flag | Default | Description |
|---|---|---|
| `--model <version>` | `V4_5` | Suno model version (see below) |
| `--style <tags>` | — | Genre/style tags — activates custom mode |
| `--title <title>` | — | Track title (recommended in custom mode) |
| `--vocals` | off | Include vocals (default is instrumental) |
| `--avoid <tags>` | — | Styles to exclude |

### Available Models

| Model ID | Description |
|---|---|
| `V4` | Suno v4 |
| `V4_5` | Suno v4.5 (default) |
| `V4_5PLUS` | Suno v4.5 Plus |
| `V4_5ALL` | Suno v4.5 All |
| `V5` | Suno v5 |
| `V5_5` | Suno v5.5 — latest |

## Modes

### Simple Mode (default)
Describe the music in plain language. Suno interprets it.

```
/kie-music slow dark ambient music with distant drums and eerie tones
```

### Custom Mode (`--style` activates it)
Provide explicit genre/style tags for precise control.

```
/kie-music ancient mystery exploration --style "dark ambient, cinematic, tribal drums" --title "Lost Civilization"
```

## Examples

```
/kie-music epic orchestral theme for an ancient ruins reveal
```

```
/kie-music mysterious atmospheric background, slow build --model V5_5
```

```
/kie-music upbeat adventure theme --style "orchestral, adventure, heroic" --title "Into the Unknown"
```

```
/kie-music dark ceremonial chanting --style "tribal, ceremonial, ominous" --avoid "electronic, modern"
```

```
/kie-music dramatic narrative underscore --vocals
```

## How It Works

1. Submits to `POST https://api.kie.ai/api/v1/generate`
2. Polls `GET https://api.kie.ai/api/v1/generate/record-info?taskId=` every 10 seconds
3. Generation takes 30–120 seconds; Suno often returns 2 track variations
4. Returns all audio URLs; optionally downloads to `~/Downloads/`

## Status Values

`PENDING` → `TEXT_SUCCESS` → `FIRST_SUCCESS` → `SUCCESS`

## API Reference

- [kie.ai Suno music docs](https://docs.kie.ai/suno-api/generate-music.md)
