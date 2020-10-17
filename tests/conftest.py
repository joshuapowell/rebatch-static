#!/usr/bin/env python

"""rStatic (Rebatch Static Site Generator).

Create by Joshua Powell on 2020-OCT-16.

Copyright (c) 2020 Joshua Powell. All rights reserved.

For license and copyright information please see the LICENSE.md (the "License")
document packaged with this software. This file and all other files included in
this packaged software may not be used in any manner except in compliance with
the License. Software distributed under this License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTY, OR CONDITIONS OF ANY KIND, either express or
implied.

See the License for the specific language governing permission and limitations
under the License.
"""

import pytest

from rstatic import application

@pytest.fixture
def app():

    app = application.Application(
        name=__name__,
        environment="testing",
    )

    """A stub for when case app_context is required."""
    with app.app_context():
        pass

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()