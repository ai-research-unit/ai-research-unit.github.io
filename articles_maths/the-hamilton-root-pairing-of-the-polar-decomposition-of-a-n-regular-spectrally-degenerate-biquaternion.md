# __The Hamilton Root Pairing of the Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion__

## Introduction

The Hamilton root pairing writes an invertible biquaternion as a complex modulus times a single exponential,

$$
\tilde Q=\Rho\exp(\vec U\Theta),
\qquad
\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}},
\qquad
\vec U=\frac{\vec Q}{B},
\qquad
\cos\Theta=\frac{Q_t}{\Rho},
\qquad
\sin\Theta=\frac{B}{\Rho},
$$

with $B^2=\langle\vec Q,\vec Q\rangle_{\natural}$. The exponent is a complex multiple of a root of $-e_t$. The pairing is the Hamilton counterpart of the quaternion pairing and the Cartan pairing: it groups the scale and the phase into the modulus and leaves the boost and the rotor in one exponential.

On the N-regular, spectrally degenerate sector $B^2=0$. The root $\vec U=\vec Q/B$ does not exist, and $\Theta$ is not defined by the displayed formulas. The pairing therefore has no literal form on the sector. It has a degeneration, and the degeneration is exact: the root is replaced by the nilpotent direction of the element, and the angle by the exact logarithm.

## The Root and Its Failure

The regular pairing needs three things: $B\neq0$, a choice of square root $B$, and the root $\vec U=\vec Q/B$ with $\vec U^2=-e_t$. On $\Sigma_{10}$ the vector part is null, $B^2=0$, so the second and third fail. The vector part is not a complex multiple of a root of $-e_t$; it is a nilpotent,

$$
\vec Q=Q_t\vec\Upsilon,
\qquad
\vec\Upsilon^2=0,
\qquad
\vec\Upsilon\neq0
$$

on the Jordan part. There is no unit axis parallel to it, because its length is zero.

The angle fails in the same way. In the regular sector $\cos\Theta=Q_t/\Rho$ and $\sin\Theta=B/\Rho$; on the wall $\sin\Theta=0$ and $\cos\Theta=\pm1$, so $\Theta$ is a multiple of $\pi$ and carries no continuous information. The exponent $\vec U\Theta$ is a product of a divergent root and a vanishing angle, and its limit depends on the path.

## The Degenerate Hamilton Form

The exact replacement is read from the normal form. Let

$$
\tilde Q=Q_t\bigl(e_t+\vec\Upsilon\bigr),
\qquad
\vec\Upsilon^2=0,
\qquad
Q_t\neq0,
\qquad
\Rho^2=Q_t^2,
\qquad
\varepsilon=\frac{Q_t}{\Rho}=\pm1.
$$

Then $Q_t=\varepsilon\Rho$ and

$$
\tilde Q=\Rho\bigl(\varepsilon e_t+\varepsilon\vec\Upsilon\bigr).
$$

Since $\exp(\vec\Upsilon)=e_t+\vec\Upsilon$, the element is

$$
\boxed{\;
\tilde Q=\Rho\exp\Bigl(\vec\Upsilon+i\pi\frac{1-\varepsilon}{2}\Bigr).
\;}
$$

The exponent has a nilpotent noncentral part $\vec\Upsilon$ and a central part $0$ or $i\pi$. The central part is the sign: for $\varepsilon=+1$ it is absent, and for $\varepsilon=-1$ it is the principal logarithm of $-1$.

**Theorem (the degenerate Hamilton form).** Every element of $\Sigma_{10}$ is the product of its complex modulus $\Rho$ and the exponential of $\vec\Upsilon+i\pi(1-\varepsilon)/2$. The factorization is unique, and the exponent is the exact logarithm of the unit factor.

*Proof.* The normal form gives $\tilde Q=Q_t(e_t+\vec\Upsilon)$ and $Q_t=\varepsilon\Rho$. The exponential of a nilpotent truncates, $\exp(\vec\Upsilon)=e_t+\vec\Upsilon$, and the central term contributes the sign. The exponent is $\Log\tilde Q-\log\Rho=\Log\tilde U$, which is unique in the branch of *Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion*, §*The Exact Logarithm*. $\square$

The first factor is the complex modulus, as in the regular pairing. The second factor is not the exponential of a root times an angle; it is the exponential of a nilpotent, and its noncentral part is the logarithm of a unipotent element.

## The Limit From the Regular Sector

Approach the wall along a regular family with $B\neq0$. The root $\vec U=\vec Q/B$ diverges as $B\to0$, and the angle obeys $\sin\Theta=B/\Rho\to0$. The limit of the product $\vec U\Theta$ depends on the sign $\varepsilon=Q_t/\Rho$.

For $\varepsilon=+1$, $\cos\Theta\to1$ and $\Theta\sim B/\Rho$. Then

$$
\vec U\Theta=\frac{\vec Q}{B}\Theta\longrightarrow\frac{\vec Q}{\Rho}=\vec\Upsilon,
\qquad
\exp(\vec U\Theta)\longrightarrow\exp(\vec\Upsilon)=e_t+\vec\Upsilon.
$$

For $\varepsilon=-1$, $\cos\Theta\to-1$ and $\Theta\to\pi$ while $\sin\Theta=B/\Rho$. Then

$$
\vec U\Theta=\frac{\vec Q}{B}\bigl(\pi+O(B)\bigr)
=\pi\frac{\vec Q}{B}+O(1),
$$

which diverges. The root-angle product has no finite limit, and the Hamilton pairing fails at the wall on this side. The exact form above is the replacement in both cases: it keeps the central sign and the nilpotent exponent together, and it does not require the divergent root.

The limit shows what survives and what does not. The modulus survives, the exponential survives, and the nilpotent direction survives. The root does not survive, and the angle does not survive as a continuous parameter. This is the same phenomenon as the survival of the polar word and the failure of the eigenbasis on the wall.

## Worked Examples

### The Standard Jordan Element

Take $\tilde Q=e_t+\vec e_x+i\vec e_y$. Then $Q_t=1$, $\Rho=1$, $\varepsilon=1$ and $\vec\Upsilon=\vec e_x+i\vec e_y$. The degenerate Hamilton form is

$$
\tilde Q=\exp(\vec e_x+i\vec e_y)=e_t+\vec e_x+i\vec e_y,
$$

because the square of the exponent vanishes. The regular root does not exist: $B=0$. The single exponential is exact, and its exponent is the logarithm of the element.

### The Negative Jordan Element

Take $\tilde Q=-e_t-\vec e_x-i\vec e_y$. Then $Q_t=-1$, $\Rho=1$, $\varepsilon=-1$ and $\vec\Upsilon=\vec e_x+i\vec e_y$. The form is

$$
\tilde Q=\exp\bigl(\vec e_x+i\vec e_y+i\pi\bigr)
=-\exp(\vec e_x+i\vec e_y)
=-e_t-\vec e_x-i\vec e_y.
$$

The central $i\pi$ is the sign of the scalar part. It is the only difference from the previous case, and it is the reason the degenerate pairing needs the exact logarithm rather than the regular root.

### The Scalar Line

On the scalar line $\vec\Upsilon=0$ and $\tilde Q=Q_te_t$. The form is

$$
\tilde Q=\Rho\exp\Bigl(i\pi\frac{1-\varepsilon}{2}\Bigr),
$$

which is $\Rho$ for $\varepsilon=+1$ and $-\Rho$ for $\varepsilon=-1$. This is the scalar limit of the Hamilton pairing: the root and the angle disappear, and only the modulus and the sign remain.

## Comparison with the Regular Pairing

| Property | Regular sector | Degenerate sector |
|---|---|---|
| modulus | $\Rho=\sqrt{N}$ | the same |
| exponent | $\vec U\Theta$, $\vec U^2=-e_t$ | $\vec\Upsilon+i\pi(1-\varepsilon)/2$, $\vec\Upsilon^2=0$ |
| root | $\vec U=\vec Q/B$ | none |
| angle | $\Theta$ with $\sin\Theta=B/\Rho$ | none; replaced by the exact logarithm |
| exponent type | complex multiple of a root of $-e_t$ | nilpotent plus a central sign |
| uniqueness | unique up to the branch of $B$ | unique in the branch of the logarithm |
| survives the wall | the root diverges | the exponent is finite and exact |

The Hamilton pairing is therefore the one pairing of the three that does not survive the wall as a pairing. The quaternion pairing survives as a regrouping, and the Cartan pairing survives as the polar decomposition of the unit group. The Hamilton pairing survives only after the root is replaced by the nilpotent direction, which is a different object.

## Summary

### Main Results

| Item | Value |
|---|---|
| regular form | $\tilde Q=\Rho\exp(\vec U\Theta)$ |
| degenerate form | $\tilde Q=\Rho\exp(\vec\Upsilon+i\pi(1-\varepsilon)/2)$ |
| exponent | nilpotent $\vec\Upsilon$ plus central $0$ or $i\pi$ |
| modulus | $\Rho$, the complex square root of $N$ |
| sign | $\varepsilon=Q_t/\Rho=\pm1$ |
| root | does not exist at $B=0$ |
| limit | $\vec U\Theta\to\vec\Upsilon$ for $\varepsilon=+1$; diverges for $\varepsilon=-1$ |
| exactness | $\exp(\vec\Upsilon)=e_t+\vec\Upsilon$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $N=\langle\tilde Q\rangle_{\natural}$ | the reduced product |
| $B^2=\langle\vec Q,\vec Q\rangle_{\natural}$ | the vector form |
| $\Sigma_{10}$ | the N-regular, spectrally degenerate sector |
| $\vec\Upsilon=\vec Q/Q_t$ | the null vector of the normal form |
| $\Rho$ | the modulus, principal square root of $N$ |
| $\varepsilon=Q_t/\Rho=\pm1$ | the sign of the scalar part of the unit factor |
| $\vec U=\vec Q/B$ | the Hamilton root, defined only for $B\neq0$ |
| $\Theta$ | the Hamilton angle |

## Further Reading

- [The Hamilton Root Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](the-hamilton-root-pairing-of-the-polar-decomposition-of-a-n-regular-spectrally-regular-biquaternion.html), for the regular pairing and its root.
- [Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html), for the exact logarithm and the word.
- [The Cartan Hermitian Pairing of the Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the pairing that survives without a root.
