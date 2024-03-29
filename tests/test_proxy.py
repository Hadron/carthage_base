# Copyright (C) 2023, Hadron Industries, Inc.
# Carthage is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation. It is distributed
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the file
# LICENSE for details.

import pytest
from carthage import *
from carthage.modeling import *
from carthage.pytest import *
from carthage.podman import *
from carthage.oci import *
from carthage_base.proxy import *
from layout import test_layout as layout


@async_test
async def test_proxy_config_generate(ainjector):
    l = await ainjector(layout)
    await l.generate()
    

@async_test
async def test_proxy_works(ainjector):
    l = await ainjector(layout)
    ainjector = l.ainjector
    try:
        await l.microservice.machine.async_become_ready()
        await l.webserver.machine.async_become_ready()
        async with l.microservice.machine.machine_running(), \
                   l.webserver.machine.machine_running():
            breakpoint()
    finally:
        try: await l.webserver.machine.delete()
        except Exception: pass
        try: await l.microservice.machine.delete()
        except Exception: pass
    
    
