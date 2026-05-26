# kie-image

Generate images using the [kie.ai](https://kie.ai) API from inside Claude Code.

## Install

Copy `kie-image` to your Claude Code skills folder:

```bash
cp kie-image ~/.claude/skills/kie-image
```

## Requirements

Set your kie.ai API key:

```bash
export KIE_API_KEY=your_key_here
```

Add to `~/.zshrc` or `~/.bashrc` to persist across sessions.

## Usage

```
/kie-image <prompt> [flags]
```

### Flags

| Flag | Default | Description |
|---|---|---|
| `--model <id>` | `nano-banana-2` | Model to use (see below) |
| `--ratio <ratio>` | `16:9` | Aspect ratio |
| `--resolution <res>` | `1K` | Output resolution: `1K`, `2K`, `4K` |
| `--format <fmt>` | `jpg` | Output format: `jpg`, `png` |
| `--ref <url>` | — | Reference image URL (repeat up to 14×) |

### Available Models

| Model ID | Description |
|---|---|
| `nano-banana-2` | Google Nano Banana 2 (default) |
| `seedream-v4` | ByteDance Seedream v4 |
| `flux-2/pro` | Black Forest Labs Flux 2 Pro |
| `gpt-image-2` | OpenAI GPT Image 2 |

### Aspect Ratios

`1:1` · `2:3` · `3:2` · `3:4` · `4:3` · `4:5` · `5:4` · `9:16` · `16:9` · `21:9`

## Examples

```
/kie-image ancient Egyptian temple at golden hour, cinematic lighting
```

```
/kie-image crumbling stone archway covered in vines --ratio 9:16 --resolution 2K
```

```
/kie-image aerial view of Machu Picchu --model flux-2/pro --format png
```

```
/kie-image character portrait --ref https://example.com/reference.jpg
```

## How It Works

1. Submits the task to `POST https://api.kie.ai/api/v1/jobs/createTask`
2. Polls `GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=` every 8 seconds
3. Returns the image URL when complete; optionally downloads to `~/Downloads/`

## API Reference

- [kie.ai docs](https://docs.kie.ai)
- [Nano Banana 2 model](https://docs.kie.ai/market/google/nanobanana2.md)
