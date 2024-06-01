import sys
from collections.abc import Iterable
from typing import Protocol, SupportsFloat, SupportsIndex, TypeVar, overload
from typing_extensions import TypeAlias

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)

_SupportsFloatOrIndex: TypeAlias = SupportsFloat | SupportsIndex

e: float
pi: float
inf: float
nan: float
tau: float

def acos(x: _SupportsFloatOrIndex, /) -> float: ...
def acosh(x: _SupportsFloatOrIndex, /) -> float: ...
def asin(x: _SupportsFloatOrIndex, /) -> float: ...
def asinh(x: _SupportsFloatOrIndex, /) -> float: ...
def atan(x: _SupportsFloatOrIndex, /) -> float: ...
def atan2(y: _SupportsFloatOrIndex, x: _SupportsFloatOrIndex, /) -> float: ...
def atanh(x: _SupportsFloatOrIndex, /) -> float: ...

if sys.version_info >= (3, 11):
    def cbrt(x: _SupportsFloatOrIndex, /) -> float: ...

class _SupportsCeil(Protocol[_T_co]):
    def __ceil__(self) -> _T_co: ...

@overload
def ceil(x: _SupportsCeil[_T], /) -> _T: ...
@overload
def ceil(x: _SupportsFloatOrIndex, /) -> int: ...
def comb(n: SupportsIndex, k: SupportsIndex, /) -> int: ...
def copysign(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, /) -> float: ...
def cos(x: _SupportsFloatOrIndex, /) -> float: ...
def cosh(x: _SupportsFloatOrIndex, /) -> float: ...
def degrees(x: _SupportsFloatOrIndex, /) -> float: ...
def dist(p: Iterable[_SupportsFloatOrIndex], q: Iterable[_SupportsFloatOrIndex], /) -> float: ...
def erf(x: _SupportsFloatOrIndex, /) -> float: ...
def erfc(x: _SupportsFloatOrIndex, /) -> float: ...
def exp(x: _SupportsFloatOrIndex, /) -> float: ...

if sys.version_info >= (3, 11):
    def exp2(x: _SupportsFloatOrIndex, /) -> float: ...

def expm1(x: _SupportsFloatOrIndex, /) -> float: ...
def fabs(x: _SupportsFloatOrIndex, /) -> float: ...
def factorial(x: SupportsIndex, /) -> int: ...

class _SupportsFloor(Protocol[_T_co]):
    def __floor__(self) -> _T_co: ...

@overload
def floor(x: _SupportsFloor[_T], /) -> _T: ...
@overload
def floor(x: _SupportsFloatOrIndex, /) -> int: ...
def fmod(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, /) -> float: ...
def frexp(x: _SupportsFloatOrIndex, /) -> tuple[float, int]: ...
def fsum(seq: Iterable[_SupportsFloatOrIndex], /) -> float: ...
def gamma(x: _SupportsFloatOrIndex, /) -> float: ...

if sys.version_info >= (3, 9):
    def gcd(*integers: SupportsIndex) -> int: ...

else:
    def gcd(x: SupportsIndex, y: SupportsIndex, /) -> int: ...

def hypot(*coordinates: _SupportsFloatOrIndex) -> float: ...
def isclose(
    a: _SupportsFloatOrIndex,
    b: _SupportsFloatOrIndex,
    *,
    rel_tol: _SupportsFloatOrIndex = 1e-09,
    abs_tol: _SupportsFloatOrIndex = 0.0,
) -> bool: ...
def isinf(x: _SupportsFloatOrIndex, /) -> bool: ...
def isfinite(x: _SupportsFloatOrIndex, /) -> bool: ...
def isnan(x: _SupportsFloatOrIndex, /) -> bool: ...
def isqrt(n: SupportsIndex, /) -> int: ...

if sys.version_info >= (3, 9):
    def lcm(*integers: SupportsIndex) -> int: ...

def ldexp(x: _SupportsFloatOrIndex, i: int, /) -> float: ...
def lgamma(x: _SupportsFloatOrIndex, /) -> float: ...
def log(x: _SupportsFloatOrIndex, base: _SupportsFloatOrIndex = ...) -> float: ...
def log10(x: _SupportsFloatOrIndex, /) -> float: ...
def log1p(x: _SupportsFloatOrIndex, /) -> float: ...
def log2(x: _SupportsFloatOrIndex, /) -> float: ...
def modf(x: _SupportsFloatOrIndex, /) -> tuple[float, float]: ...

if sys.version_info >= (3, 12):
    def nextafter(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, /, *, steps: SupportsIndex | None = None) -> float: ...

elif sys.version_info >= (3, 9):
    def nextafter(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, /) -> float: ...

def perm(n: SupportsIndex, k: SupportsIndex | None = None, /) -> int: ...
def pow(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, /) -> float: ...
@overload
def prod(iterable: Iterable[SupportsIndex], /, *, start: SupportsIndex = 1) -> int: ...  # type: ignore[overload-overlap]
@overload
def prod(iterable: Iterable[_SupportsFloatOrIndex], /, *, start: _SupportsFloatOrIndex = 1) -> float: ...
def radians(x: _SupportsFloatOrIndex, /) -> float: ...
def remainder(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, /) -> float: ...
def sin(x: _SupportsFloatOrIndex, /) -> float: ...
def sinh(x: _SupportsFloatOrIndex, /) -> float: ...

if sys.version_info >= (3, 12):
    def sumprod(p: Iterable[float], q: Iterable[float], /) -> float: ...

def sqrt(x: _SupportsFloatOrIndex, /) -> float: ...
def tan(x: _SupportsFloatOrIndex, /) -> float: ...
def tanh(x: _SupportsFloatOrIndex, /) -> float: ...

# Is different from `_typeshed.SupportsTrunc`, which is not generic
class _SupportsTrunc(Protocol[_T_co]):
    def __trunc__(self) -> _T_co: ...

def trunc(x: _SupportsTrunc[_T], /) -> _T: ...

if sys.version_info >= (3, 9):
    def ulp(x: _SupportsFloatOrIndex, /) -> float: ...

if sys.version_info >= (3, 13):
    def fma(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, z: _SupportsFloatOrIndex, /) -> float: ...
