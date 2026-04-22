# No-USD G1 Tracking

`Tracking-Flat-G1-RefParity-v0` is a lightweight G1 whole-body tracking task for
training and rendering with a URDF/capsule-friendly robot asset instead of the default
USD robot asset.

This task is intended for comparison against the open whole-body-tracking setup. It keeps
the WBC command and reward implementations, but aligns the task surface where practical:

- robot asset: URDF G1 with `replace_cylinders_with_capsules=True`
- actuators: implicit actuator groups instead of delayed wrappers
- observations: reference-style motion anchor, base velocity, joints, and previous actions
- events and rewards: reference-style reduced event and penalty surface
- runner: empirical normalization enabled, no WBC-only reward normalization or L2C2 config

## Required environment variables

The repository does not vendor the reference G1 URDF or motion clips. Set both paths before
training or rendering:

```bash
export G1_REF_PARITY_URDF_PATH=/path/to/unitree_description/urdf/g1/main.urdf
export MOTION_FILE=/path/to/motion.npz
```

For parity runs, disable AGILE runtime monkey patches:

```bash
export AGILE_MONKEY_PATCHES=none
```

If `AGILE_MONKEY_PATCHES` is unset, `scripts/train.py` and `scripts/eval.py` keep the
existing default behavior and load all AGILE monkey patches.

## Train

```bash
python scripts/train.py \
    --task Tracking-Flat-G1-RefParity-v0 \
    --num_envs 4096 \
    --max_iterations 30000 \
    --headless \
    --logger tensorboard
```

The task uses `MOTION_FILE` as the motion source. Use a motion file that matches the G1
tracking body order expected by the tracking command.

## Render a trained policy

Use `scripts/eval.py` for policy rendering. `scripts/play.py` is only for environment
validation with generated sinusoidal actions and does not load PPO checkpoints.

```bash
python scripts/eval.py \
    --task Tracking-Flat-G1-RefParity-v0 \
    --checkpoint /path/to/model_29999.pt \
    --num_envs 1 \
    --video \
    --video_length 400 \
    --headless
```

The rendered policy should be trained on `Tracking-Flat-G1-RefParity-v0`. A checkpoint
trained on the default USD task is not a clean no-USD render comparison.

## Monkey patch behavior

The monkey patch modules remain in `agile/isaaclab_extras/monkey_patches/` and are not
duplicated by this task. This branch only changes how `scripts/train.py` and `scripts/eval.py`
load them:

- `AGILE_MONKEY_PATCHES=all` or unset: load all existing patches.
- `AGILE_MONKEY_PATCHES=none`: load no patches.
- `AGILE_MONKEY_PATCHES=contact_sensor,manager_based_rl_env`: load only named patches.

This keeps existing tasks backward-compatible while allowing no-USD parity runs to use the
same unpatched runtime surface used in the reference comparison experiments.
