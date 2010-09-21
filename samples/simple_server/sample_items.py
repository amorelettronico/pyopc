# This file is part of pyopc.
#
# pyopc is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# pyopc is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General
# Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with pyopc.  If not, see
# <http://www.gnu.org/licenses/>.
#
# $Id$
#
''' Sample OPC Items for testing purposes '''

import datetime
from PyOPC.OPCContainers import *

# Initial timestamp for all ItemValues
def_ts = datetime.datetime(2006, 2, 15, 12, 15, 18)

TestOPCItems = ((ItemContainer(ItemName='sample_integer',
                               Value=14,
                               Timestamp=def_ts,
                               QualityField='good',
                               LimitField='none',
                               VendorField=0),
                 (OPCProperty(Name='accessRights',
                              Value='readWriteable'),
                  OPCProperty(Name='description',
                              Value='Integer Item'),
                  OPCProperty(Name='MyProperty',
                              Value = 'foobar',
                              ItemPath='MyPath',
                              ItemName='MyName'))),
                (ItemContainer(ItemName='sample_float',
                               Value=96.43,
                               Timestamp=def_ts,
                               QualityField='good',
                               LimitField='none',
                               VendorField=0),
                 (OPCProperty(Name='accessRights',
                              Value='readWriteable'),)))
