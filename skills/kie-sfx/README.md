# kie-sfx

Generate sound effects using Suno AI via the [kie.ai](https://kie.ai) API from inside Claude Code.

## Install

```bash
cp kie-sfx ~/.claude/skills/kie-sfx
```

## Requirements

```bash
export KIE_API_KEY=your_key_here
```

## Usage

```
/kie-sfx <sound description> [flags]
```

### Flags

| Flag | Default | Description |
|---|---|---|
| `--model <version>` | `V5_5` | Suno model: `V5` or `V5_5` |
| `--loop` | off | Make the audio loop seamlessly |
| `--tempo <bpm>` | — | Tempo in BPM (1–300) |
| `--key <key>` | `Any` | Musical key (e.g. `C`, `C#m`, `Dm`, `Em`) |

## Examples

```
/kie-sfx ancient stone door grinding open slowly
```

```
/kie-sfx thunder crack with deep rumbling echo
```

```
/kie-sfx distant tribal drums in a stone chamber --loop
```

```
/kie-sfx wind howling through ruins at night --model V5_5
```

```
/kie-sfx mysterious cave ambience with dripping water --loop --tempo 60
```

## Tips for Great SFX

- Be specific and descriptive: *"heavy iron chain dragging across stone floor"* beats *"chain sound"*
- Add acoustic context: *"in a large stone chamber"*, *"from a distance"*, *"echoing"*
- Use `--loop` for ambient backgrounds meant to play continuously
- Use `--tempo` when the SFX needs to sync with music

## How It Works

1. Submits to `POST https://api.kie.ai/api/v1/generate/sounds`
2. Polls `GET https://api.kie.ai/api/v1/generate/record-info?taskId=` every 10 seconds
3. Returns the audio URL; optionally downloads to `~/Downloads/`

## Status Values

`PENDING` → `FIRST_SUCCESS` → `SUCCESS`

## API Reference

- [kie.ai Suno sounds docs](https://docs.kie.ai/suno-api/generate-sounds.md)
