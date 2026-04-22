# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
from dataclasses import MISSING

from isaaclab.utils import configclass

from agile.rl_env.assets.robots.unitree_g1 import G1_REF_PARITY_ACTION_SCALE, G1_REF_PARITY_CFG
from agile.rl_env.tasks.tracking.tracking_env_ref_parity_cfg import TrackingEnvRefParityCfg


@configclass
class G1FlatRefParityEnvCfg(TrackingEnvRefParityCfg):
    """No-USD G1 tracking task surface aligned with whole_body_tracking_clean."""

    def __post_init__(self):
        super().__post_init__()

        self.scene.robot = G1_REF_PARITY_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
        self.actions.joint_pos.scale = G1_REF_PARITY_ACTION_SCALE
        self.commands.motion.anchor_body_name = "torso_link"
        self.commands.motion.motion_file = os.getenv("MOTION_FILE", MISSING)
        self.commands.motion.body_names = [
            "pelvis",
            "left_hip_roll_link",
            "left_knee_link",
            "left_ankle_roll_link",
            "right_hip_roll_link",
            "right_knee_link",
            "right_ankle_roll_link",
            "torso_link",
            "left_shoulder_roll_link",
            "left_elbow_link",
            "left_wrist_yaw_link",
            "right_shoulder_roll_link",
            "right_elbow_link",
            "right_wrist_yaw_link",
        ]
