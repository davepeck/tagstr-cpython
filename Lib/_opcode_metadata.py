# This file is generated by Tools/cases_generator/py_metadata_generator.py
# from:
#   Python/bytecodes.c
# Do not edit!
_specializations = {
    "RESUME": [
        "RESUME_CHECK",
    ],
    "TO_BOOL": [
        "TO_BOOL_ALWAYS_TRUE",
        "TO_BOOL_BOOL",
        "TO_BOOL_INT",
        "TO_BOOL_LIST",
        "TO_BOOL_NONE",
        "TO_BOOL_STR",
    ],
    "BINARY_OP": [
        "BINARY_OP_MULTIPLY_INT",
        "BINARY_OP_ADD_INT",
        "BINARY_OP_SUBTRACT_INT",
        "BINARY_OP_MULTIPLY_FLOAT",
        "BINARY_OP_ADD_FLOAT",
        "BINARY_OP_SUBTRACT_FLOAT",
        "BINARY_OP_ADD_UNICODE",
        "BINARY_OP_INPLACE_ADD_UNICODE",
    ],
    "BINARY_SUBSCR": [
        "BINARY_SUBSCR_DICT",
        "BINARY_SUBSCR_GETITEM",
        "BINARY_SUBSCR_LIST_INT",
        "BINARY_SUBSCR_STR_INT",
        "BINARY_SUBSCR_TUPLE_INT",
    ],
    "STORE_SUBSCR": [
        "STORE_SUBSCR_DICT",
        "STORE_SUBSCR_LIST_INT",
    ],
    "SEND": [
        "SEND_GEN",
    ],
    "UNPACK_SEQUENCE": [
        "UNPACK_SEQUENCE_TWO_TUPLE",
        "UNPACK_SEQUENCE_TUPLE",
        "UNPACK_SEQUENCE_LIST",
    ],
    "STORE_ATTR": [
        "STORE_ATTR_INSTANCE_VALUE",
        "STORE_ATTR_SLOT",
        "STORE_ATTR_WITH_HINT",
    ],
    "LOAD_GLOBAL": [
        "LOAD_GLOBAL_MODULE",
        "LOAD_GLOBAL_BUILTIN",
    ],
    "LOAD_SUPER_ATTR": [
        "LOAD_SUPER_ATTR_ATTR",
        "LOAD_SUPER_ATTR_METHOD",
    ],
    "LOAD_ATTR": [
        "LOAD_ATTR_INSTANCE_VALUE",
        "LOAD_ATTR_MODULE",
        "LOAD_ATTR_WITH_HINT",
        "LOAD_ATTR_SLOT",
        "LOAD_ATTR_CLASS",
        "LOAD_ATTR_PROPERTY",
        "LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN",
        "LOAD_ATTR_METHOD_WITH_VALUES",
        "LOAD_ATTR_METHOD_NO_DICT",
        "LOAD_ATTR_METHOD_LAZY_DICT",
        "LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES",
        "LOAD_ATTR_NONDESCRIPTOR_NO_DICT",
    ],
    "COMPARE_OP": [
        "COMPARE_OP_FLOAT",
        "COMPARE_OP_INT",
        "COMPARE_OP_STR",
    ],
    "CONTAINS_OP": [
        "CONTAINS_OP_SET",
        "CONTAINS_OP_DICT",
    ],
    "FOR_ITER": [
        "FOR_ITER_LIST",
        "FOR_ITER_TUPLE",
        "FOR_ITER_RANGE",
        "FOR_ITER_GEN",
    ],
    "CALL": [
        "CALL_BOUND_METHOD_EXACT_ARGS",
        "CALL_PY_EXACT_ARGS",
        "CALL_TYPE_1",
        "CALL_STR_1",
        "CALL_TUPLE_1",
        "CALL_BUILTIN_CLASS",
        "CALL_BUILTIN_O",
        "CALL_BUILTIN_FAST",
        "CALL_BUILTIN_FAST_WITH_KEYWORDS",
        "CALL_LEN",
        "CALL_ISINSTANCE",
        "CALL_LIST_APPEND",
        "CALL_METHOD_DESCRIPTOR_O",
        "CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS",
        "CALL_METHOD_DESCRIPTOR_NOARGS",
        "CALL_METHOD_DESCRIPTOR_FAST",
        "CALL_ALLOC_AND_ENTER_INIT",
        "CALL_PY_GENERAL",
        "CALL_BOUND_METHOD_GENERAL",
        "CALL_NON_PY_GENERAL",
    ],
}

_specialized_opmap = {
    'BINARY_OP_ADD_FLOAT': 150,
    'BINARY_OP_ADD_INT': 151,
    'BINARY_OP_ADD_UNICODE': 152,
    'BINARY_OP_INPLACE_ADD_UNICODE': 3,
    'BINARY_OP_MULTIPLY_FLOAT': 153,
    'BINARY_OP_MULTIPLY_INT': 154,
    'BINARY_OP_SUBTRACT_FLOAT': 155,
    'BINARY_OP_SUBTRACT_INT': 156,
    'BINARY_SUBSCR_DICT': 157,
    'BINARY_SUBSCR_GETITEM': 158,
    'BINARY_SUBSCR_LIST_INT': 159,
    'BINARY_SUBSCR_STR_INT': 160,
    'BINARY_SUBSCR_TUPLE_INT': 161,
    'CALL_ALLOC_AND_ENTER_INIT': 162,
    'CALL_BOUND_METHOD_EXACT_ARGS': 163,
    'CALL_BOUND_METHOD_GENERAL': 164,
    'CALL_BUILTIN_CLASS': 165,
    'CALL_BUILTIN_FAST': 166,
    'CALL_BUILTIN_FAST_WITH_KEYWORDS': 167,
    'CALL_BUILTIN_O': 168,
    'CALL_ISINSTANCE': 169,
    'CALL_LEN': 170,
    'CALL_LIST_APPEND': 171,
    'CALL_METHOD_DESCRIPTOR_FAST': 172,
    'CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS': 173,
    'CALL_METHOD_DESCRIPTOR_NOARGS': 174,
    'CALL_METHOD_DESCRIPTOR_O': 175,
    'CALL_NON_PY_GENERAL': 176,
    'CALL_PY_EXACT_ARGS': 177,
    'CALL_PY_GENERAL': 178,
    'CALL_STR_1': 179,
    'CALL_TUPLE_1': 180,
    'CALL_TYPE_1': 181,
    'COMPARE_OP_FLOAT': 182,
    'COMPARE_OP_INT': 183,
    'COMPARE_OP_STR': 184,
    'CONTAINS_OP_DICT': 185,
    'CONTAINS_OP_SET': 186,
    'FOR_ITER_GEN': 187,
    'FOR_ITER_LIST': 188,
    'FOR_ITER_RANGE': 189,
    'FOR_ITER_TUPLE': 190,
    'LOAD_ATTR_CLASS': 191,
    'LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN': 192,
    'LOAD_ATTR_INSTANCE_VALUE': 193,
    'LOAD_ATTR_METHOD_LAZY_DICT': 194,
    'LOAD_ATTR_METHOD_NO_DICT': 195,
    'LOAD_ATTR_METHOD_WITH_VALUES': 196,
    'LOAD_ATTR_MODULE': 197,
    'LOAD_ATTR_NONDESCRIPTOR_NO_DICT': 198,
    'LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES': 199,
    'LOAD_ATTR_PROPERTY': 200,
    'LOAD_ATTR_SLOT': 201,
    'LOAD_ATTR_WITH_HINT': 202,
    'LOAD_GLOBAL_BUILTIN': 203,
    'LOAD_GLOBAL_MODULE': 204,
    'LOAD_SUPER_ATTR_ATTR': 205,
    'LOAD_SUPER_ATTR_METHOD': 206,
    'RESUME_CHECK': 207,
    'SEND_GEN': 208,
    'STORE_ATTR_INSTANCE_VALUE': 209,
    'STORE_ATTR_SLOT': 210,
    'STORE_ATTR_WITH_HINT': 211,
    'STORE_SUBSCR_DICT': 212,
    'STORE_SUBSCR_LIST_INT': 213,
    'TO_BOOL_ALWAYS_TRUE': 214,
    'TO_BOOL_BOOL': 215,
    'TO_BOOL_INT': 216,
    'TO_BOOL_LIST': 217,
    'TO_BOOL_NONE': 218,
    'TO_BOOL_STR': 219,
    'UNPACK_SEQUENCE_LIST': 220,
    'UNPACK_SEQUENCE_TUPLE': 221,
    'UNPACK_SEQUENCE_TWO_TUPLE': 222,
}

opmap = {
    'CACHE': 0,
    'RESERVED': 17,
    'RESUME': 149,
    'INSTRUMENTED_LINE': 254,
    'BINARY_SLICE': 1,
    'BINARY_SUBSCR': 2,
    'BUILD_DECODED': 4,
    'CHECK_EG_MATCH': 5,
    'CHECK_EXC_MATCH': 6,
    'CLEANUP_THROW': 7,
    'DELETE_SUBSCR': 8,
    'END_ASYNC_FOR': 9,
    'END_FOR': 10,
    'END_SEND': 11,
    'EXIT_INIT_CHECK': 12,
    'FORMAT_SIMPLE': 13,
    'FORMAT_WITH_SPEC': 14,
    'GET_AITER': 15,
    'GET_ANEXT': 16,
    'GET_ITER': 18,
    'GET_LEN': 19,
    'GET_YIELD_FROM_ITER': 20,
    'INTERPRETER_EXIT': 21,
    'LOAD_BUILD_CLASS': 22,
    'LOAD_LOCALS': 23,
    'MAKE_FUNCTION': 24,
    'MATCH_KEYS': 25,
    'MATCH_MAPPING': 26,
    'MATCH_SEQUENCE': 27,
    'NOP': 28,
    'POP_EXCEPT': 29,
    'POP_TOP': 30,
    'PUSH_EXC_INFO': 31,
    'PUSH_NULL': 32,
    'RETURN_GENERATOR': 33,
    'RETURN_VALUE': 34,
    'SETUP_ANNOTATIONS': 35,
    'STORE_SLICE': 36,
    'STORE_SUBSCR': 37,
    'TO_BOOL': 38,
    'UNARY_INVERT': 39,
    'UNARY_NEGATIVE': 40,
    'UNARY_NOT': 41,
    'WITH_EXCEPT_START': 42,
    'BINARY_OP': 43,
    'BUILD_CONST_KEY_MAP': 44,
    'BUILD_INTERPOLATION': 45,
    'BUILD_LIST': 46,
    'BUILD_MAP': 47,
    'BUILD_SET': 48,
    'BUILD_SLICE': 49,
    'BUILD_STRING': 50,
    'BUILD_TUPLE': 51,
    'CALL': 52,
    'CALL_FUNCTION_EX': 53,
    'CALL_INTRINSIC_1': 54,
    'CALL_INTRINSIC_2': 55,
    'CALL_KW': 56,
    'COMPARE_OP': 57,
    'CONTAINS_OP': 58,
    'CONVERT_VALUE': 59,
    'COPY': 60,
    'COPY_FREE_VARS': 61,
    'DELETE_ATTR': 62,
    'DELETE_DEREF': 63,
    'DELETE_FAST': 64,
    'DELETE_GLOBAL': 65,
    'DELETE_NAME': 66,
    'DICT_MERGE': 67,
    'DICT_UPDATE': 68,
    'ENTER_EXECUTOR': 69,
    'EXTENDED_ARG': 70,
    'FOR_ITER': 71,
    'GET_AWAITABLE': 72,
    'IMPORT_FROM': 73,
    'IMPORT_NAME': 74,
    'IS_OP': 75,
    'JUMP_BACKWARD': 76,
    'JUMP_BACKWARD_NO_INTERRUPT': 77,
    'JUMP_FORWARD': 78,
    'LIST_APPEND': 79,
    'LIST_EXTEND': 80,
    'LOAD_ATTR': 81,
    'LOAD_COMMON_CONSTANT': 82,
    'LOAD_CONST': 83,
    'LOAD_DEREF': 84,
    'LOAD_FAST': 85,
    'LOAD_FAST_AND_CLEAR': 86,
    'LOAD_FAST_CHECK': 87,
    'LOAD_FAST_LOAD_FAST': 88,
    'LOAD_FROM_DICT_OR_DEREF': 89,
    'LOAD_FROM_DICT_OR_GLOBALS': 90,
    'LOAD_GLOBAL': 91,
    'LOAD_NAME': 92,
    'LOAD_SPECIAL': 93,
    'LOAD_SUPER_ATTR': 94,
    'MAKE_CELL': 95,
    'MAP_ADD': 96,
    'MATCH_CLASS': 97,
    'POP_JUMP_IF_FALSE': 98,
    'POP_JUMP_IF_NONE': 99,
    'POP_JUMP_IF_NOT_NONE': 100,
    'POP_JUMP_IF_TRUE': 101,
    'RAISE_VARARGS': 102,
    'RERAISE': 103,
    'RETURN_CONST': 104,
    'SEND': 105,
    'SET_ADD': 106,
    'SET_FUNCTION_ATTRIBUTE': 107,
    'SET_UPDATE': 108,
    'STORE_ATTR': 109,
    'STORE_DEREF': 110,
    'STORE_FAST': 111,
    'STORE_FAST_LOAD_FAST': 112,
    'STORE_FAST_STORE_FAST': 113,
    'STORE_GLOBAL': 114,
    'STORE_NAME': 115,
    'SWAP': 116,
    'UNPACK_EX': 117,
    'UNPACK_SEQUENCE': 118,
    'YIELD_VALUE': 119,
    'INSTRUMENTED_RESUME': 236,
    'INSTRUMENTED_END_FOR': 237,
    'INSTRUMENTED_END_SEND': 238,
    'INSTRUMENTED_RETURN_VALUE': 239,
    'INSTRUMENTED_RETURN_CONST': 240,
    'INSTRUMENTED_YIELD_VALUE': 241,
    'INSTRUMENTED_LOAD_SUPER_ATTR': 242,
    'INSTRUMENTED_FOR_ITER': 243,
    'INSTRUMENTED_CALL': 244,
    'INSTRUMENTED_CALL_KW': 245,
    'INSTRUMENTED_CALL_FUNCTION_EX': 246,
    'INSTRUMENTED_INSTRUCTION': 247,
    'INSTRUMENTED_JUMP_FORWARD': 248,
    'INSTRUMENTED_JUMP_BACKWARD': 249,
    'INSTRUMENTED_POP_JUMP_IF_TRUE': 250,
    'INSTRUMENTED_POP_JUMP_IF_FALSE': 251,
    'INSTRUMENTED_POP_JUMP_IF_NONE': 252,
    'INSTRUMENTED_POP_JUMP_IF_NOT_NONE': 253,
    'JUMP': 256,
    'JUMP_NO_INTERRUPT': 257,
    'LOAD_CLOSURE': 258,
    'POP_BLOCK': 259,
    'SETUP_CLEANUP': 260,
    'SETUP_FINALLY': 261,
    'SETUP_WITH': 262,
    'STORE_FAST_MAYBE_NULL': 263,
}

HAVE_ARGUMENT = 42
MIN_INSTRUMENTED_OPCODE = 236
