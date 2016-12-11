# Copyright 2016 Zara Zaimeche

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


WINDOWWIDTH = 500
WINDOWHEIGHT = 500

COLUMNS = 30
ROWS = 30

COLUMNWIDTH = WINDOWWIDTH / COLUMNS
ROWHEIGHT = WINDOWHEIGHT /ROWS

PLAYERSPEED = 1 # 1 column a frame
SHOOTSPEED = 5
PLAYERSIZE = 1 # 1 column
ALIENSIZE = 1 #also 1 column. should separate width and height since
              # they are 2 columns wide via a hack at the moment.

LAZERRATE = 15 #lower is faster

FPS = 40
