# Copyright 2018 Xiaomi, Inc.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from enum import Enum

from mace.proto import mace_pb2


class DeviceType(Enum):
    CPU = 0
    GPU = 2
    HEXAGON = 3


class DataFormat(Enum):
    NHWC = 0
    NCHW = 1


class FilterFormat(Enum):
    HWIO = 0
    OIHW = 1
    HWOI = 2
    OHWI = 3


class PaddingMode(Enum):
    VALID = 0
    SAME = 1
    FULL = 2


class PoolingType(Enum):
    AVG = 1
    MAX = 2


class ActivationType(Enum):
    NOOP = 0
    RELU = 1
    RELUX = 2
    PRELU = 3
    TANH = 4
    SIGMOID = 5


class EltwiseType(Enum):
    SUM = 0
    SUB = 1
    PROD = 2
    DIV = 3
    MIN = 4
    MAX = 5
    NEG = 6
    ABS = 7
    SQR_DIFF = 8
    POW = 9
    EQUAL = 10


class FrameworkType(Enum):
    TENSORFLOW = 0
    CAFFE = 1


MaceSupportedOps = [
    'Activation',
    'AddN',
    'ArgMax',
    'BatchNorm',
    'BatchToSpaceND',
    'BiasAdd',
    'Cast',
    'ChannelShuffle',
    'Concat',
    'Conv2D',
    'Crop',
    'Deconv2D',
    'DepthToSpace',
    'DepthwiseConv2d',
    'Dequantize',
    'Eltwise',
    'ExpandDims',
    'FoldedBatchNorm',
    'Fill',
    'FullyConnected',
    'Gather',
    'Identity',
    'InferConv2dShape',
    'LocalResponseNorm',
    'LSTMCell',
    'MatMul',
    'Pad',
    'Pooling',
    'Proposal',
    'Quantize',
    'ReduceMean',
    'Reshape',
    'ResizeBicubic',
    'ResizeBilinear',
    'Reverse',
    'ScalarMath',
    'Slice',
    'Split',
    'Shape',
    'Squeeze',
    'Stack',
    'Unstack',
    'StridedSlice',
    'Softmax',
    'SpaceToBatchND',
    'SpaceToDepth',
    'Transpose',
    'WinogradInverseTransform',
    'WinogradTransform',
]

MaceOp = Enum('MaceOp', [(op, op) for op in MaceSupportedOps], type=str)


class MaceKeyword(object):
    # node related str
    mace_input_node_name = 'mace_input_node'
    mace_output_node_name = 'mace_output_node'
    mace_buffer_type = 'buffer_type'
    mace_mode = 'mode'
    mace_buffer_transform = 'BufferTransform'
    mace_buffer_inverse_transform = 'BufferInverseTransform'
    # arg related str
    mace_padding_str = 'padding'
    mace_padding_values_str = 'padding_values'
    mace_strides_str = 'strides'
    mace_dilations_str = 'dilations'
    mace_pooling_type_str = 'pooling_type'
    mace_global_pooling_str = 'global_pooling'
    mace_kernel_str = 'kernels'
    mace_data_format_str = 'data_format'
    mace_filter_format_str = 'filter_format'
    mace_element_type_str = 'type'
    mace_activation_type_str = 'activation'
    mace_activation_max_limit_str = 'max_limit'
    mace_resize_size_str = 'size'
    mace_batch_to_space_crops_str = 'crops'
    mace_paddings_str = 'paddings'
    mace_align_corners_str = 'align_corners'
    mace_space_batch_block_shape_str = 'block_shape'
    mace_space_depth_block_size_str = 'block_size'
    mace_constant_value_str = 'constant_value'
    mace_dims_str = 'dims'
    mace_axis_str = 'axis'
    mace_num_split_str = 'num_split'
    mace_keepdims_str = 'keepdims'
    mace_shape_str = 'shape'
    mace_winograd_filter_transformed = 'is_filter_transformed'
    mace_device = 'device'
    mace_scalar_input_str = 'scalar_input'
    mace_wino_block_size = 'wino_block_size'
    mace_output_shape_str = 'output_shape'
    mace_begin_mask_str = 'begin_mask'
    mace_end_mask_str = 'end_mask'
    mace_ellipsis_mask_str = 'ellipsis_mask'
    mace_new_axis_mask_str = 'new_axis_mask'
    mace_shrink_axis_mask_str = 'shrink_axis_mask'
    mace_transpose_a_str = 'transpose_a'
    mace_transpose_b_str = 'transpose_b'
    mace_op_data_type_str = 'T'
    mace_offset_str = 'offset'
    mace_opencl_max_image_size = "opencl_max_image_size"
    mace_seperate_buffer_str = 'seperate_buffer'
    mace_scalar_input_index_str = 'scalar_input_index'
    mace_opencl_mem_type = "opencl_mem_type"
    mace_framework_type_str = "framework_type"


class TransformerRule(Enum):
    REMOVE_IDENTITY_OP = 1
    TRANSFORM_GLOBAL_POOLING = 2
    FOLD_RESHAPE = 3
    TRANSFORM_MATMUL_TO_FC = 4
    FOLD_BATCHNORM = 5
    FOLD_CONV_AND_BN = 6
    FOLD_DEPTHWISE_CONV_AND_BN = 7
    TRANSFORM_GPU_WINOGRAD = 8
    TRANSFORM_ADD_TO_BIASADD = 9
    FOLD_BIASADD = 10
    FLATTEN_ATROUS_CONV = 11
    FOLD_ACTIVATION = 12
    TRANSPOSE_FILTERS = 13
    RESHAPE_FC_WEIGHT = 14
    TRANSPOSE_DATA_FORMAT = 15
    TRANSFORM_GLOBAL_CONV_TO_FC = 16
    ADD_BUFFER_TRANSFORM = 17
    ADD_DEVICE = 18
    SORT_BY_EXECUTION = 19
    ADD_IN_OUT_TENSOR_INFO = 20
    ADD_MACE_INPUT_AND_OUTPUT_NODES = 21
    UPDATE_FLOAT_OP_DATA_TYPE = 22
    QUANTIZE_NODES = 23
    ADD_QUANTIZE_TENSOR_RANGE = 24
    QUANTIZE_WEIGHTS = 25
    TRANSFORM_LSTMCELL_ZEROSTATE = 26
    TRANSFORM_BASIC_LSTMCELL = 27
    TRANSFORM_FAKE_QUANTIZE = 28
    CHECK_QUANTIZE_INFO = 29
    REARRANGE_BATCH_TO_SPACE = 30
    ADD_OPENCL_INFORMATIONS = 31


class ConverterInterface(object):
    """Base class for converting external models to mace models."""

    def run(self):
        raise NotImplementedError('run')


class NodeInfo(object):
    """A class for describing node information"""

    def __init__(self):
        self._name = None
        self._shape = []
        self._range = [-1.0, 1.0]

    @property
    def name(self):
        return self._name

    @property
    def shape(self):
        return self._shape

    @property
    def range(self):
        return self._range

    @name.setter
    def name(self, name):
        self._name = name

    @shape.setter
    def shape(self, shape):
        self._shape = shape

    @range.setter
    def range(self, range):
        self._range = range

    def __str__(self):
        return '%s %s' % (self._name, str(self._shape))


class ConverterOption(object):
    """A class for specifying options passed to converter tool"""

    def __init__(self):
        self._input_nodes = {}
        self._output_nodes = {}
        self._data_type = mace_pb2.DT_FLOAT
        self._device = DeviceType.CPU.value
        self._winograd = 0
        self._quantize = False
        self._quantize_range_file = ""
        self._change_concat_ranges = False
        self._transformer_option = None
        self._cl_mem_type = ""

    @property
    def input_nodes(self):
        return self._input_nodes

    @property
    def output_nodes(self):
        return self._output_nodes

    @property
    def data_type(self):
        return self._data_type

    @property
    def device(self):
        return self._device

    @property
    def winograd(self):
        return self._winograd

    @property
    def quantize(self):
        return self._quantize

    @property
    def change_concat_ranges(self):
        return self._change_concat_ranges

    @property
    def quantize_range_file(self):
        return self._quantize_range_file

    @property
    def transformer_option(self):
        return self._transformer_option

    @property
    def cl_mem_type(self):
        return self._cl_mem_type

    @input_nodes.setter
    def input_nodes(self, input_nodes):
        for node in input_nodes:
            self._input_nodes[node.name] = node

    def add_input_node(self, input_node):
        self._input_nodes[input_node.name] = input_node

    @output_nodes.setter
    def output_nodes(self, output_nodes):
        for node in output_nodes:
            self.output_nodes[node.name] = node

    def add_output_node(self, output_node):
        self._output_nodes[output_node.name] = output_node

    @data_type.setter
    def data_type(self, data_type):
        self._data_type = data_type

    @device.setter
    def device(self, device):
        self._device = device

    @winograd.setter
    def winograd(self, winograd):
        self._winograd = winograd

    @quantize.setter
    def quantize(self, quantize):
        self._quantize = quantize

    @quantize_range_file.setter
    def quantize_range_file(self, quantize_range_file):
        self._quantize_range_file = quantize_range_file

    @change_concat_ranges.setter
    def change_concat_ranges(self, change_concat_ranges):
        self._change_concat_ranges = change_concat_ranges

    @transformer_option.setter
    def transformer_option(self, transformer_option):
        self._transformer_option = transformer_option

    @cl_mem_type.setter
    def cl_mem_type(self, cl_mem_type):
        self._cl_mem_type = cl_mem_type

    def disable_transpose_filters(self):
        if TransformerRule.TRANSPOSE_FILTERS in self._transformer_option:
            self._transformer_option.remove(TransformerRule.TRANSPOSE_FILTERS)

    def enable_transpose_filters(self):
        if TransformerRule.TRANSPOSE_FILTERS not in self._transformer_option:
            self._transformer_option.append(TransformerRule.TRANSPOSE_FILTERS)

    def build(self):
        if self._transformer_option:
            self._transformer_option = [TransformerRule[transformer]
                                        for transformer in self._transformer_option]  # noqa
        else:
            self._transformer_option = [
                # Model structure related transformation
                TransformerRule.TRANSFORM_FAKE_QUANTIZE,
                TransformerRule.REMOVE_IDENTITY_OP,
                TransformerRule.TRANSFORM_GLOBAL_POOLING,
                TransformerRule.TRANSFORM_LSTMCELL_ZEROSTATE,
                TransformerRule.TRANSFORM_BASIC_LSTMCELL,
                TransformerRule.FOLD_RESHAPE,
                TransformerRule.TRANSFORM_MATMUL_TO_FC,
                TransformerRule.FOLD_BATCHNORM,
                TransformerRule.FOLD_CONV_AND_BN,
                TransformerRule.FOLD_DEPTHWISE_CONV_AND_BN,
                TransformerRule.TRANSFORM_GPU_WINOGRAD,
                TransformerRule.TRANSFORM_ADD_TO_BIASADD,
                TransformerRule.REARRANGE_BATCH_TO_SPACE,
                TransformerRule.FOLD_BIASADD,
                TransformerRule.FLATTEN_ATROUS_CONV,
                TransformerRule.FOLD_ACTIVATION,
                TransformerRule.TRANSFORM_GLOBAL_CONV_TO_FC,
                TransformerRule.RESHAPE_FC_WEIGHT,
                # Model data format related transformation
                TransformerRule.TRANSPOSE_FILTERS,
                TransformerRule.TRANSPOSE_DATA_FORMAT,
                # Mace model structure related transformation
                TransformerRule.ADD_IN_OUT_TENSOR_INFO,
                # Device related transformation
                TransformerRule.ADD_BUFFER_TRANSFORM,
                TransformerRule.ADD_DEVICE,
                # Data type related transformation
                TransformerRule.UPDATE_FLOAT_OP_DATA_TYPE,
                # Transform finalization
                TransformerRule.ADD_OPENCL_INFORMATIONS,
                TransformerRule.ADD_MACE_INPUT_AND_OUTPUT_NODES,
                # for quantization entropy calibration use
                TransformerRule.SORT_BY_EXECUTION,
                # Need to be put after SORT_BY_EXECUTION
                TransformerRule.ADD_QUANTIZE_TENSOR_RANGE,
            ]
            if self._quantize:
                self._transformer_option = self._transformer_option + [
                    # need to be put after ADD_QUANTIZE_TENSOR_RANGE
                    TransformerRule.QUANTIZE_NODES,
                    TransformerRule.QUANTIZE_WEIGHTS,
                    TransformerRule.SORT_BY_EXECUTION,
                    TransformerRule.CHECK_QUANTIZE_INFO,
                ]


class ConverterUtil(object):
    @staticmethod
    def get_arg(op, arg_name):
        for arg in op.arg:
            if arg.name == arg_name:
                return arg
        return None

    @staticmethod
    def add_data_format_arg(op, data_format):
        data_format_arg = op.arg.add()
        data_format_arg.name = MaceKeyword.mace_data_format_str
        data_format_arg.i = data_format.value

    @staticmethod
    def add_data_type_arg(op, data_type):
        data_type_arg = op.arg.add()
        data_type_arg.name = MaceKeyword.mace_op_data_type_str
        data_type_arg.i = data_type

    @staticmethod
    def data_format(op):
        arg = ConverterUtil.get_arg(op, MaceKeyword.mace_data_format_str)
        if arg is None:
            return None
        elif arg.i == DataFormat.NHWC.value:
            return DataFormat.NHWC
        elif arg.i == DataFormat.NCHW.value:
            return DataFormat.NCHW
        else:
            return None

    @staticmethod
    def set_filter_format(net, filter_format):
        arg = net.arg.add()
        arg.name = MaceKeyword.mace_filter_format_str
        arg.i = filter_format.value

    @staticmethod
    def filter_format(net):
        arg = ConverterUtil.get_arg(net, MaceKeyword.mace_filter_format_str)
        if arg is None:
            return None
        elif arg.i == FilterFormat.HWIO.value:
            return FilterFormat.HWIO
        elif arg.i == FilterFormat.HWOI.value:
            return FilterFormat.HWOI
        elif arg.i == FilterFormat.OIHW.value:
            return FilterFormat.OIHW
        else:
            return None
