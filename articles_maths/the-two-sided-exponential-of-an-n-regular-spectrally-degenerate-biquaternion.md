# __The Two-Sided Exponential of an N-Regular, Spectrally Degenerate Biquaternion__

## Introduction

This article is the analytic companion of *Hermitian Pair of N-Regular, Spectrally Degenerate Operators Acting on Two Sides*. On the sector the two-sided operator is $\lvert Q_t\rvert^{2}$ times a unipotent operator, $\mathrm{Sd}_{\tilde Q}=\lvert Q_t\rvert^{2}(I+\mathsf N)$ with $\mathsf N^{3}=0$, so its exponential is a finite polynomial and the one-parameter group is a family of null rotations.

The algebra of the two-sided operator — the $3+1$ Jordan structure, the polar decomposition of the operator, the two slots and the fixed directions — is in the companion. This article reads the exponent: the closed form of $\mathrm{Sd}_{\tilde Q}$ as $e^{A+B}$, the one-parameter group, the interpretation as a null rotation, and the exponents that the boost and the rotor keep.

## The Exponential at the Wall

**The exponent of the two-sided operator.** Write $\vec\Upsilon=\vec A+i\vec B$ with $\vec A$ and $\vec B$ real, so that $\vec A\cdot\vec B=0$ and $\lvert\vec A\rvert=\lvert\vec B\rvert=a$, and put $A=L_{\vec\Upsilon}$ and $B=R_{\vec\Upsilon^{*}}$. Write $\bar\Upsilon=\vec A-i\vec B$ for the coefficient conjugate. The operators $A$ and $B$ commute and square to zero. Since $\tilde U=e^{\vec\Upsilon}$ and $\tilde U^{*}=e^{\vec\Upsilon^{*}}$,

$$
\mathrm{Sd}_{\tilde U}=L_{e^{\vec\Upsilon}}\circ R_{e^{\vec\Upsilon^{*}}}=e^{A}e^{B}=e^{A+B},
$$

and $(A+B)^2=2AB$ and $(A+B)^3=0$. Hence

$$
\boxed{\;\mathrm{Sd}_{\tilde Q}=\lvert Q_t\rvert^{2}\mathrm{Sd}_{\tilde U}
=\lvert Q_t\rvert^{2}e^{A+B}
=\lvert Q_t\rvert^{2}\bigl(I+A+B+AB\bigr)
=\lvert Q_t\rvert^{2}(I+\mathsf N).\;}
$$

**The one-parameter group.** Since $\mathsf N^2=2AB$ and $\mathsf N^3=0$,

$$
\boxed{\;\exp\bigl(t\mathrm{Sd}_{\tilde Q}\bigr)
=e^{t\lvert Q_t\rvert^{2}}
\Bigl(I+t\lvert Q_t\rvert^{2}\mathsf N+\frac{t^{2}\lvert Q_t\rvert^{4}}{2}\mathsf N^{2}\Bigr)\;}
$$

for every complex $t$.

*Proof.* $\mathrm{Sd}_{\tilde Q}=\lvert Q_t\rvert^{2}(I+\mathsf N)$, and $I$ commutes with $\mathsf N$; hence the exponential is $e^{t\lvert Q_t\rvert^{2}}\exp(t\lvert Q_t\rvert^{2}\mathsf N)$, and the second factor truncates at $\mathsf N^3=0$.

**Interpretation: a null rotation.** On $\mathbb{B}_{\Phi}$ the factor $\tilde U$ has norm one, so $\mathrm{Sd}_{\tilde U}$ preserves the Minkowski form $\langle X\rangle_{\natural}$; the path $\mathrm{Sd}_{e^{t\vec\Upsilon}}$, $0\le t\le1$, connects it to the identity, so it is a proper orthochronous Lorentz transformation. Its single eigenvalue is $1$, and its Jordan form is one block of size three and one of size one. A Lorentz transformation of that type is a **null rotation** (a parabolic element): it fixes a null direction and shears the two transverse directions. The exponential displays the finite shear as $I+s\mathsf N+\frac{s^2}{2}\mathsf N^2$ with $s=t\lvert Q_t\rvert^2$. It contains no rotation angle and no rapidity; the two are locked to the single null parameter $a$. The modulus scales the shear, and the phase cancels.

**What the factors keep.** The factors are not degenerate in the same way as their product. $\mathrm{Sd}_{\tilde U_{\mathrm b}}$ has the simple eigenvalues $e^{\theta_{\mathrm{rpd}}}$ and $e^{-\theta_{\mathrm{rpd}}}$ and the eigenvalue $1$ with multiplicity two; $\mathrm{Sd}_{\tilde u_{\mathrm r}}$ has the simple eigenvalues $e^{i\theta}$ and $e^{-i\theta}$ and the eigenvalue $1$ with multiplicity two. The product has the single eigenvalue $\lvert Q_t\rvert^{2}$, four times. The boost and the angle are therefore present in the factors and absent from the spectrum of the product. In the product they survive only through the locked parameter $a$, with $\varepsilon\tan\frac{\theta}{2}=\sinh\frac{\theta_{\mathrm{rpd}}}{2}=a$.

The rate is the square of the one-sided rate: $\lvert Q_t\rvert^{2}$ here, $Q_t$ there. The reason is the slot count. The two-sided operator carries $\vec\Upsilon$ in its left slot and $\vec\Upsilon^{*}$ in its right slot, so the scalar $Q_t$ appears once on each side and the modulus is squared; the one-sided operator carries the left slot only. This is the wall form of the doubling rule: on a vector the two slots add their exponents, and at the wall they add $\vec\Upsilon$ and $\vec\Upsilon^{*}$.

## Worked Example

The companion gives the matrix of $\mathrm{Sd}_{\tilde Q}$ and its nilpotent part $\mathsf N$. Its exponential is the finite null rotation

$$
\exp\bigl(t\mathrm{Sd}_{\tilde Q}\bigr)
=e^{t}\Bigl(I+t\mathsf N+\frac{t^{2}}{2}\mathsf N^{2}\Bigr)
=e^{t}
\begin{pmatrix}
1+2t+2t^{2}&0&-2it&2it(1+t)\\
0&1&0&0\\
2it&0&1&-2t\\
2it(1+t)&0&2t&1-2t-2t^{2}
\end{pmatrix},
$$

with the matrix $\mathsf N$ above. The fixed coordinate is the second one, which is the $1\times1$ block; the remaining three coordinates carry the chain of length three.

## Summary

The two-sided operator is a scalar times a unipotent operator. With $A=L_{\vec\Upsilon}$ and $B=R_{\vec\Upsilon^{*}}$, the two commute and square to zero, and

$$
\mathrm{Sd}_{\tilde Q}=\lvert Q_t\rvert^{2}e^{A+B}
=\lvert Q_t\rvert^{2}(I+\mathsf N),
\qquad \mathsf N=A+B+AB,
\qquad \mathsf N^{2}=2AB,\quad \mathsf N^{3}=0 .
$$

Its one-parameter group is the finite polynomial

$$
\exp\bigl(t\mathrm{Sd}_{\tilde Q}\bigr)
=e^{t\lvert Q_t\rvert^{2}}
\Bigl(I+t\lvert Q_t\rvert^{2}\mathsf N
+\frac{t^{2}\lvert Q_t\rvert^{4}}{2}\mathsf N^{2}\Bigr).
$$

On $\mathbb{B}_{\Phi}$ it is a null rotation: a proper orthochronous Lorentz transformation with the single eigenvalue $1$ and the Jordan form $J_3(1)\oplus J_1(1)$. It fixes a null direction and shears the two transverse directions; it contains no rotation angle and no rapidity.

The boost and the rotor keep their angles in the factors, with the eigenvalues $e^{\pm\theta_{\mathrm{rpd}}}$ and $e^{\pm i\theta}$ and the eigenvalue $1$ twice each, but the product has the single eigenvalue $\lvert Q_t\rvert^{2}$. The two parameters are locked to the null parameter $a$, and the rate is $\lvert Q_t\rvert^{2}$, the square of the one-sided rate.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ | the Hermitian pair |
| $A=L_{\vec\Upsilon}$, $B=R_{\vec\Upsilon^{*}}$ | the two commuting square-zero operators |
| $\mathsf N=A+B+AB$ | the nilpotent part, $\mathsf N^{2}=2AB$, $\mathsf N^{3}=0$ |
| $\vec\Upsilon=\vec A+i\vec B$ | the null vector, with $\vec A\cdot\vec B=0$ and $\lvert\vec A\rvert=\lvert\vec B\rvert=a$ |
| $\vec c=\vec A\times\vec B/a^{2}$ | the unit vector of the fixed null direction |
| $\tilde U_{\mathrm b},\tilde u_{\mathrm r}$ | the positive factor and the rotor |
| $\theta_{\mathrm{rpd}},\theta$ | the rapidity and the rotor angle |
| $a$ | the null parameter |

## Further Reading

- [Hermitian Pair of N-Regular, Spectrally Degenerate Operators Acting on Two Sides](hermitian-pair-of-n-regular-spectrally-degenerate-operators-acting-on-two-sides.html), for the algebraic companion: the Jordan structure, the polar decomposition and the fixed directions.
- [The One-Sided Operator Exponential of an N-Regular, Spectrally Degenerate Biquaternion](the-one-sided-operator-exponential-of-an-n-regular-spectrally-degenerate-biquaternion.html), for the shear generated by one multiplication.
- [Exponential Polar Decomposition of an N-Regular, Spectrally Degenerate Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html), for the element word, the exact logarithm and the log defect.
- [Introduction to N and Spectrally Regular and Degenerate Operators](introduction-to-n-and-spectrally-regular-and-degenerate-operators.html), for the three operators and the sector table.
