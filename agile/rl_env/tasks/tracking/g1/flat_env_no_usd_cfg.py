# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from isaaclab.utils import configclass

from agile.rl_env.assets.robots.unitree_g1 import G1_29DOF_NO_USD
from agile.rl_env.tasks.tracking.g1.flat_env_cfg import G1FlatEnvCfg


@configclass
class G1FlatNoUsdEnvCfg(G1FlatEnvCfg):
    """Tracking-Flat-G1-v0 with only the robot asset changed from USD to URDF."""

    def __post_init__(self):
        super().__post_init__()
        self.scene.robot = G1_29DOF_NO_USD.replace(prim_path="{ENV_REGEX_NS}/Robot")
        self.commands.motion.motion_body_names = None
        self.commands.motion.motion_joint_names = None
