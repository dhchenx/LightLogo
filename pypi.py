# Copyright © 2022, Donghua Chen
# All Rights Reserved
# Software Name: LightLogo
# By: Donghua Chen (https://github.com/dhchenx)
# License: BSD-3 - https://github.com/dhchenx/LightLogo/blob/main/LICENSE

#                         BSD 3-Clause License
#
# Copyright (c) 2022, Donghua Chen
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from quick_pypi.deploy import *

auto_deploy(
    cwd=os.path.dirname(os.path.realpath(__file__)),
    name="LightLogo",
    long_name="Lightweight Logo 3D",
    description="A simple, lightweight and powerful 3D agent-based simulation toolkit with Logo",
    long_description="A simple, lightweight and powerful 3D agent-based simulation toolkit with Logo",
    src_root="src",
    dists_root=f"dists",
    pypi_token='../pypi_upload_token.txt',
    test=False,
    version="0.0.1a0",
    project_url="http://github.com/dhchenx/LightLogo",
    author_name="Donghua Chen",
    author_email="douglaschan@126.com",
    requires="matplotlib", # use ; for multiple requires
    license='BSD-3',
    license_filename='LICENSE',
    keywords="logo, lightlogo, agent-based modeling, simulation, turtle in 3D",
    github_username="dhchenx",
    readme_path="README.md",
   # console_scripts=""
)

