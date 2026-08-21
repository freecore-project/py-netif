#-
# Copyright (c) 2014 iXsystems, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#

import os
import re
import subprocess
import sys

import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True

from setuptools import setup
from Cython.Distutils.extension import Extension
from Cython.Distutils import build_ext


HERE = os.path.dirname(os.path.abspath(__file__))
PLACEHOLDER = re.compile(r'@[A-Za-z_][A-Za-z0-9_]*@')


def generate_config():
    """Derive config.pxi/config.h from the pinned headers via autoconf.

    TrueNAS CORE 13.3 generated both at build time; they are gitignored
    build artifacts, not sources. netif.pyx and defs.pxd `include "config.pxi"`,
    so a stale copy silently adds or omits public API members with nothing to
    detect the disagreement (freecore/the internal development record).

    The committed configure is fully expanded, so this needs only /bin/sh and a
    C compiler -- no autoconf build dependency. Every failure mode is fatal:
    a silent skip is what put frozen values in the tree in the first place.
    """
    configure = os.path.join(HERE, 'configure')
    if not os.path.isfile(configure):
        sys.exit('py-netif: configure is missing; cannot derive config.pxi')

    try:
        subprocess.run(['/bin/sh', configure], cwd=HERE, check=True)
    except subprocess.CalledProcessError as exc:
        sys.exit('py-netif: configure failed with exit status %d' % exc.returncode)

    config_pxi = os.path.join(HERE, 'config.pxi')
    if not os.path.isfile(config_pxi):
        sys.exit('py-netif: configure did not produce config.pxi')

    with open(config_pxi) as f:
        body = f.read()

    leftover = PLACEHOLDER.search(body)
    if leftover:
        sys.exit(
            'py-netif: config.pxi still contains the unsubstituted placeholder %s'
            % leftover.group(0)
        )


generate_config()


extensions = [
    Extension(
        "netif",
        ["netif.pyx", "ifmedia.c"],
        extra_compile_args=["-g"],
    )
]

setup(
    name='netif',
    version='1.0',
    packages=[''],
    package_data={'': ['*.html', '*.c']},
    cmdclass={'build_ext': build_ext},
    ext_modules=extensions
)
