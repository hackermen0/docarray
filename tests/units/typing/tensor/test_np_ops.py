// Licensed to the LF AI & Data foundation under one
// or more contributor license agreements. See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership. The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
                                                 // "License"); you may not use this file except in compliance
// with the License. You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
import numpy as np

from docarray import BaseDoc
from docarray.typing import NdArray


def test_tensor_ops():
    class A(BaseDoc):
        tensor: NdArray[3, 224, 224]

    class B(BaseDoc):
        tensor: NdArray[3, 112, 224]

    tensor = A(tensor=np.ones((3, 224, 224))).tensor
    tensord = A(tensor=np.ones((3, 224, 224))).tensor
    tensorn = np.zeros((3, 224, 224))
    tensorhalf = B(tensor=np.ones((3, 112, 224))).tensor
    tensorfull = np.concatenate([tensorhalf, tensorhalf], axis=1)

    assert type(tensor) == NdArray
    assert type(tensor + tensord) == NdArray
    assert type(tensor + tensorn) == NdArray
    assert type(tensor + tensorfull) == NdArray
