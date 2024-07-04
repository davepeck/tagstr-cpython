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
    'CHECK_EG_MATCH': 4,
    'CHECK_EXC_MATCH': 5,
    'CLEANUP_THROW': 6,
    'DELETE_SUBSCR': 7,
    'END_ASYNC_FOR': 8,
    'END_FOR': 9,
    'END_SEND': 10,
    'EXIT_INIT_CHECK': 11,
    'FORMAT_SIMPLE': 12,
    'FORMAT_WITH_SPEC': 13,
    'GET_AITER': 14,
    'GET_ANEXT': 15,
    'GET_ITER': 16,
    'GET_LEN': 18,
    'GET_YIELD_FROM_ITER': 19,
    'INTERPRETER_EXIT': 20,
    'LOAD_BUILD_CLASS': 21,
    'LOAD_LOCALS': 22,
    'MAKE_FUNCTION': 23,
    'MATCH_KEYS': 24,
    'MATCH_MAPPING': 25,
    'MATCH_SEQUENCE': 26,
    'NOP': 27,
    'POP_EXCEPT': 28,
    'POP_TOP': 29,
    'PUSH_EXC_INFO': 30,
    'PUSH_NULL': 31,
    'RETURN_GENERATOR': 32,
    'RETURN_VALUE': 33,
    'SETUP_ANNOTATIONS': 34,
    'STORE_SLICE': 35,
    'STORE_SUBSCR': 36,
    'TO_BOOL': 37,
    'UNARY_INVERT': 38,
    'UNARY_NEGATIVE': 39,
    'UNARY_NOT': 40,
    'WITH_EXCEPT_START': 41,
    'BINARY_OP': 42,
    'BUILD_CONST_KEY_MAP': 43,
    'BUILD_INTERPOLATION': 44,
    'BUILD_LIST': 45,
    'BUILD_MAP': 46,
    'BUILD_SET': 47,
    'BUILD_SLICE': 48,
    'BUILD_STRING': 49,
    'BUILD_TUPLE': 50,
    'CALL': 51,
    'CALL_FUNCTION_EX': 52,
    'CALL_INTRINSIC_1': 53,
    'CALL_INTRINSIC_2': 54,
    'CALL_KW': 55,
    'COMPARE_OP': 56,
    'CONTAINS_OP': 57,
    'CONVERT_VALUE': 58,
    'COPY': 59,
    'COPY_FREE_VARS': 60,
    'DELETE_ATTR': 61,
    'DELETE_DEREF': 62,
    'DELETE_FAST': 63,
    'DELETE_GLOBAL': 64,
    'DELETE_NAME': 65,
    'DICT_MERGE': 66,
    'DICT_UPDATE': 67,
    'ENTER_EXECUTOR': 68,
    'EXTENDED_ARG': 69,
    'FOR_ITER': 70,
    'GET_AWAITABLE': 71,
    'IMPORT_FROM': 72,
    'IMPORT_NAME': 73,
    'IS_OP': 74,
    'JUMP_BACKWARD': 75,
    'JUMP_BACKWARD_NO_INTERRUPT': 76,
    'JUMP_FORWARD': 77,
    'LIST_APPEND': 78,
    'LIST_EXTEND': 79,
    'LOAD_ATTR': 80,
    'LOAD_COMMON_CONSTANT': 81,
    'LOAD_CONST': 82,
    'LOAD_DEREF': 83,
    'LOAD_FAST': 84,
    'LOAD_FAST_AND_CLEAR': 85,
    'LOAD_FAST_CHECK': 86,
    'LOAD_FAST_LOAD_FAST': 87,
    'LOAD_FROM_DICT_OR_DEREF': 88,
    'LOAD_FROM_DICT_OR_GLOBALS': 89,
    'LOAD_GLOBAL': 90,
    'LOAD_NAME': 91,
    'LOAD_SPECIAL': 92,
    'LOAD_SUPER_ATTR': 93,
    'MAKE_CELL': 94,
    'MAP_ADD': 95,
    'MATCH_CLASS': 96,
    'POP_JUMP_IF_FALSE': 97,
    'POP_JUMP_IF_NONE': 98,
    'POP_JUMP_IF_NOT_NONE': 99,
    'POP_JUMP_IF_TRUE': 100,
    'RAISE_VARARGS': 101,
    'RERAISE': 102,
    'RETURN_CONST': 103,
    'SEND': 104,
    'SET_ADD': 105,
    'SET_FUNCTION_ATTRIBUTE': 106,
    'SET_UPDATE': 107,
    'STORE_ATTR': 108,
    'STORE_DEREF': 109,
    'STORE_FAST': 110,
    'STORE_FAST_LOAD_FAST': 111,
    'STORE_FAST_STORE_FAST': 112,
    'STORE_GLOBAL': 113,
    'STORE_NAME': 114,
    'SWAP': 115,
    'UNPACK_EX': 116,
    'UNPACK_SEQUENCE': 117,
    'YIELD_VALUE': 118,
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

HAVE_ARGUMENT = 41
MIN_INSTRUMENTED_OPCODE = 236
