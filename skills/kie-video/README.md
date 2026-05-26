# kie-video

Generate videos using Google Veo 3.1 via the [kie.ai](https://kie.ai) API from inside Claude Code.

## Install

```bash
cp kie-video ~/.claude/skills/kie-video
```

## Requirements

```bash
export KIE_API_KEY=your_key_here
```

## Usage

```
/kie-video <prompt> [flags]
```

### Flags

| Flag | Default | Description |
|---|---|---|
| `--model <id>` | `veo3_fast` | Model to use (see below) |
| `--ratio <ratio>` | `16:9` | Aspect ratio: `16:9` or `9:16` |
| `--duration <sec>` | `6` | Duration in seconds: `4`, `6`, or `8` |
| `--resolution <res>` | `720p` | Output resolution: `720p`, `1080p`, `4k` |
| `--image <url>` | — | Reference image for image-to-video (repeat up to 3×) |

### Available Models

| Model ID | Description |
|---|---|
| `veo3_fast` | Veo 3.1 Fast — best speed/quality balance (default) |
| `veo3` | Veo 3.1 — highest quality, slower |
| `veo3_lite` | Veo 3.1 Lite — fastest, lower cost |

## Examples

```
/kie-video slow cinematic pan across an ancient stone temple, golden hour lighting
```

```
/kie-video dramatic flyover of jungle ruins --duration 8 --resolution 1080p
```

```
/kie-video camera pushes through a dark cave entrance --model veo3 --ratio 9:16
```

```
/kie-video animate this scene --image https://example.com/scene.jpg
```

## How It Works

1. Submits to `POST https://api.kie.ai/api/v1/veo/generate`
2. Polls `GET https://api.kie.ai/api/v1/veo/record-info?taskId=` every 15 seconds
3. Video generation typically takes 1–5 minutes
4. Returns the MP4 URL; optionally downloads to `~/Downloads/`

## Status Codes

| `successFlag` | Meaning |
|---|---|
| `0` | Generating |
| `1` | Success |
| `2` | Failed |
| `3` | Generation failed |

## API Reference

- [kie.ai Veo 3.1 docs](https://docs.kie.ai/veo3-api/generate-veo-3-video.md)
