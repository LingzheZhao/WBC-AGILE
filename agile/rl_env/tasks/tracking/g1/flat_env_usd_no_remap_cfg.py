# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from isaaclab.utils import configclass

from agile.rl_env.tasks.tracking.g1.flat_env_cfg import G1FlatEnvCfg


@configclass
class G1FlatUsdNoRemapEnvCfg(G1FlatEnvCfg):
    """USD tracking task with source body and joint remaps disabled."""

    def __post_init__(self):
        super().__post_init__()
        self.commands.motion.motion_body_names = None
        self.commands.motion.motion_joint_names = None
