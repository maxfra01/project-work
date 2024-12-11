import numpy as np

numpy_function_map = {
    # Trigonometric functions
    'sin': np.sin,
    'cos': np.cos,
    'tan': np.tan,
    # 'arcsin': np.arcsin,
    # 'asin': np.arcsin,
    # 'arccos': np.arccos,
    # 'acos': np.arccos,
    # 'arctan': np.arctan,
    # 'atan': np.arctan,
    # 'hypot': np.hypot,
    # 'arctan2': np.arctan2,
    # 'atan2': np.arctan2,
    # 'degrees': np.degrees,
    # 'radians': np.radians,
    # 'unwrap': np.unwrap,
    # 'deg2rad': np.deg2rad,
    # 'rad2deg': np.rad2deg,
    
    # # Hyperbolic functions
    # 'sinh': np.sinh,
    # 'cosh': np.cosh,
    # 'tanh': np.tanh,
    # 'arcsinh': np.arcsinh,
    # 'asinh': np.arcsinh,
    # 'arccosh': np.arccosh,
    # 'acosh': np.arccosh,
    # 'arctanh': np.arctanh,
    # 'atanh': np.arctanh,
    
    # # Rounding
    # 'round': np.round,
    # 'around': np.around,
    # 'rint': np.rint,
    # 'fix': np.fix,
    # 'floor': np.floor,
    # 'ceil': np.ceil,
    # 'trunc': np.trunc,
    
    # # Sums, products, differences
    # 'prod': np.prod,
    # 'sum': np.sum,
    # 'nanprod': np.nanprod,
    # 'nansum': np.nansum,
    # 'cumulative_sum': np.cumsum,
    # 'cumulative_prod': np.cumprod,
    # 'cumprod': np.cumprod,
    # 'cumsum': np.cumsum,
    # 'nancumprod': np.nancumprod,
    # 'nancumsum': np.nancumsum,
    # 'diff': np.diff,
    # 'ediff1d': np.ediff1d,
    # 'gradient': np.gradient,
    # 'cross': np.cross,
    # 'trapezoid': np.trapezoid,
    
    # Exponents and logarithms
    'exp': np.exp,
    #'expm1': np.expm1,
    # 'exp2': np.exp2,
    # 'log': np.log,
    # 'log10': np.log10,
    # 'log2': np.log2,
    #'log1p': np.log1p,
    #'logaddexp': np.logaddexp,
    # 'logaddexp2': np.logaddexp2,
    
    # Other special functions
    # 'i0': np.i0,
    # 'sinc': np.sinc,
    
    # # Floating point routines
    # 'signbit': np.signbit,
    # 'copysign': np.copysign,
    # 'frexp': np.frexp,
    # 'ldexp': np.ldexp,
    # 'nextafter': np.nextafter,
    # 'spacing': np.spacing,
    
    # # Rational routines
    # 'lcm': np.lcm,
    # 'gcd': np.gcd,
    
    # Arithmetic operations
    'add': np.add,
    # 'reciprocal': np.reciprocal,
    # 'positive': np.positive,
    # 'negative': np.negative,
    'multiply': np.multiply,
    'divide': np.divide,
    'power': np.power,
    'pow': np.power,
    'subtract': np.subtract,
    # 'true_divide': np.true_divide,
    # 'floor_divide': np.floor_divide,
    # 'float_power': np.float_power,
    # 'fmod': np.fmod,
    # 'mod': np.mod,
    # 'modf': np.modf,
    # 'remainder': np.remainder,
    # 'divmod': divmod,
    
    # Handling complex numbers
    # 'angle': np.angle,
    # 'real': np.real,
    # 'imag': np.imag,
    # 'conj': np.conj,
    # 'conjugate': np.conjugate,
    
    # # Extrema finding
    # 'maximum': np.maximum,
    # 'max': np.max,
    # 'amax': np.amax,
    # 'fmax': np.fmax,
    # 'nanmax': np.nanmax,
    # 'minimum': np.minimum,
    # 'min': np.min,
    # 'amin': np.amin,
    # 'fmin': np.fmin,
    # 'nanmin': np.nanmin,
    
    # # Miscellaneous
    # 'convolve': np.convolve,
    # 'clip': np.clip,
    # 'sqrt': np.sqrt,
    # 'cbrt': np.cbrt,
    # 'square': np.square,
    # 'absolute': np.absolute,
    # 'fabs': np.fabs,
    # 'sign': np.sign,
    # 'heaviside': np.heaviside,
    # 'nan_to_num': np.nan_to_num,
    # 'real_if_close': np.real_if_close,
    # 'interp': np.interp,
    # 'bitwise_count': np.bitwise_and
}

numpy_binary_operator_list = [ 'add', 'multiply', 'divide', 'power', 'pow', 'subtract' ]
numpy_unary_operator_list = [ 'exp', 'sin', 'cos', 'tan']
