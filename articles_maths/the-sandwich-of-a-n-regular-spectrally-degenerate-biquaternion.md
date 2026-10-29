# __The Sandwich of a N-Regular, Spectrally Degenerate Biquaternion__

## Introduction

The Hermitian sandwich of the biquaternion algebra is the operator

$$
\Theta_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},
\qquad
\Theta_{\tilde Q}(\tilde X)=\tilde Q\,\tilde X\,\tilde Q^{*}.
$$

It is the sandwich of the polar decomposition, and its theory in the regular sector is *The Sandwich of a N-Regular, Spectrally Regular Biquaternion*. On the N-regular, spectrally degenerate sector the sandwich becomes especially simple: it is a positive scalar times a unipotent operator. The scalar is $|Q_t|^2$; on the Jordan part the unipotent operator has one Jordan block of size three and one of size one, while on the scalar line it is the identity.

The article states the sandwich, proves the Jordan structure, reads the polar decomposition of the operator, computes the fixed directions, and explains how the two spinor slots of the regular article coalesce at the wall. The exponential of the operator is the companion *The Sandwich Exponential of a N-Regular, Spectrally Degenerate Biquaternion*.

## The Sandwich of the Word

The elementary properties are unchanged:

$$
\Theta_{\tilde Q\tilde Q'}=\Theta_{\tilde Q}\circ\Theta_{\tilde Q'},
\qquad
\Theta_{\tilde Q}^{-1}=\Theta_{\tilde Q^{-1}},
\qquad
\Theta_{\tilde Q}(e_t)=\tilde Q\tilde Q^{*},
$$

and $\Theta_{\tilde Q}$ preserves the Hermitian and anti-Hermitian subspaces. The norm scales by

$$
\langle\Theta_{\tilde Q}(\tilde X)\rangle_{\natural}
=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}.
$$

The closed form of the word is

$$
\Theta_{\tilde Q}(\tilde X)
=r^{2}\,\tilde U_{\mathrm b}\bigl(\tilde u_{\mathrm r}\tilde X\tilde u_{\mathrm r}^{-1}\bigr)\tilde U_{\mathrm b},
$$

and the central phase cancels, $\Theta_{\exp(i\alpha)}=\mathrm{id}$.

On the sector,

$$
\tilde Q=Q_t\bigl(e_t+\vec\Upsilon\bigr),
\qquad
\vec\Upsilon^2=0,
\qquad
\tilde U=e_t+\vec\Upsilon,
\qquad
\Theta_{\tilde Q}=\lvert Q_t\rvert^{2}\,\Theta_{\tilde U}.
$$

The problem is therefore reduced to the sandwich by the unipotent element $\tilde U$.

## The Unipotent Operator

Let $A=L_{\vec\Upsilon}$ and $B=R_{\vec\Upsilon^{*}}$, the left multiplication by $\vec\Upsilon$ and the right multiplication by $\vec\Upsilon^{*}$. They commute, and

$$
A^2=0,
\qquad
B^2=0,
\qquad
\Theta_{\tilde U}=I+A+B+AB.
$$

**Proposition (the Jordan structure).** On the Jordan part, $\Theta_{\tilde U}$ has the single eigenvalue $1$, and its nilpotent part

$$
\mathsf N=\Theta_{\tilde U}-I=A+B+AB
$$

satisfies $\mathsf N^2=2AB$, $\mathsf N^3=0$, with $\operatorname{rank}\mathsf N=2$ and $\operatorname{rank}\mathsf N^2=1$. The Jordan form is one block of size three and one block of size one.

*Proof.* The operators $A$ and $B$ commute and square to zero, so

$$
\mathsf N^2=2AB,
\qquad
\mathsf N^3=3AB(A+B)=0,
$$

because $A^2=B^2=0$. The rank of $A$ is two, and the rank of $B$ is two; their product $AB$ has rank one because the image of $B$ is the right ideal $\vec\Upsilon^{*}\mathbb{B}$ and the kernel of $A$ is the right annihilator of $\vec\Upsilon$, whose intersection with that image is one complex line. Hence $\operatorname{rank}\mathsf N=2$ and $\operatorname{rank}\mathsf N^2=1$. A nilpotent on a four-dimensional space with $\mathsf N^3=0$ and $\operatorname{rank}\mathsf N^2=1$ has one block of size three and one of size one.

Consequently $\Theta_{\tilde Q}$ has the single eigenvalue $|Q_t|^2$, with one $3\times3$ Jordan block and one $1\times1$ block. Its determinant is

$$
\det\Theta_{\tilde Q}=\lvert Q_t\rvert^{8},
$$

the fourth power of the element determinant, as in the regular sector.

The fixed subspace of $\Theta_{\tilde U}$ is two-dimensional. It is not the centralizer of $\tilde U$: the norm-one element is not $*$-unitary, and $\Theta_{\tilde U}$ is not a conjugation. One fixed vector comes from the $3\times3$ block and one from the $1\times1$ block; both are written explicitly in §*The Fixed Directions*.

## The Polar Decomposition of the Sandwich

Write the Cartan pairing of the element as $\tilde Q=\tilde H\tilde V$ with $\tilde H=r\tilde U_{\mathrm b}$ positive and $\tilde V=e^{i\alpha}\tilde u_{\mathrm r}$ $*$-unitary. Then

$$
\Theta_{\tilde Q}=\Theta_{\tilde H}\circ\Theta_{\tilde V},
\qquad
\Theta_{\tilde H}(\tilde X)=\tilde H\tilde X\tilde H^{*},
\qquad
\Theta_{\tilde V}(\tilde X)=\tilde V\tilde X\tilde V^{*}.
$$

The first factor is a positive operator on $\mathbb{B}$, because $\tilde H$ is positive. The second is a $*$-unitary operator, because $\tilde V$ is $*$-unitary. This is the polar decomposition of the operator $\Theta_{\tilde Q}$.

The product $\Theta_{\tilde Q}$ is $\lvert Q_t\rvert^{2}$ times a unipotent operator, while the two factors are not unipotent. The positive factor has eigenvalues $r^{2}e^{\pm\psi}$ on the two spinor slots, and the $*$-unitary factor has eigenvalues $e^{\pm i\theta}$ after the phase cancels. The product has the single eigenvalue $\lvert Q_t\rvert^{2}$. The factors do not commute, and the non-commutativity is the Jordan defect of the sandwich.

## The Two Slots

In the regular sector the sandwich has two spinor slots, and the rotor angle and the rapidity are doubled on them. On the wall the slots do not disappear; they coalesce into the Jordan chain. The $3\times3$ block and the $1\times1$ block are the remnants of the two slots: one slot keeps a fixed vector, and the other carries the nilpotent chain of length three.

The central phase is invisible in the sandwich, as in the regular sector: $\Theta_{e^{i\alpha}}=\mathrm{id}$. The phase is visible only in the one-sided operator. The sector therefore preserves the one-sided/sandwich contrast: the phase is a one-sided datum, and the sandwich sees only the scale, the boost and the rotor.

## The Fixed Directions

The fixed subspace is $\ker\mathsf N$, of dimension two. Put $\vec c=\vec A\times\vec B/a^2$, so that $\lvert\vec c\rvert=1$, and $X=e_t+i\vec c$.

*Proposition.* $\Theta_{\tilde U}$ fixes $\vec A$ and $X$. These two vectors span the fixed subspace. On $\mathbb{M}_-$ the fixed null vector is $iX=ie_t-\vec c$.

*Proof.* From $\vec A\cdot\vec B=0$ and $\lvert\vec A\rvert=\lvert\vec B\rvert=a$,

$$
\Upsilon\vec A=-a^2-i\vec A\times\vec B=\vec A\bar\Upsilon,\qquad
\bar\Upsilon^2=0,
$$

and

$$
\Upsilon\vec c=-\vec B+i\vec A,\qquad
\vec c\bar\Upsilon=\vec B+i\vec A.
$$

Hence $\Upsilon X=\Upsilon+i\Upsilon\vec c=0$ and $X\bar\Upsilon=\bar\Upsilon+i\vec c\bar\Upsilon=0$. Therefore

$$
\Theta_{\tilde U}(\vec A)
=\vec A+\Upsilon\vec A-\vec A\bar\Upsilon-\Upsilon\vec A\bar\Upsilon=\vec A,
$$

because the two middle terms are equal and cancel, and $\Upsilon\vec A\bar\Upsilon=\vec A\bar\Upsilon^2=0$; and

$$
\Theta_{\tilde U}(X)
=X+\Upsilon X-X\bar\Upsilon-\Upsilon X\bar\Upsilon=X.
$$

The vector $\vec A$ has zero scalar part and $X$ has scalar part one, so they are independent. Since $\ker\mathsf N$ is two-dimensional, they span it.

The vector $X$ is null, $\langle X\rangle_{\natural}=1-\lvert\vec c\rvert^2=0$, so the fixed line is the null line of the rotation. The vector $\vec A$ is spacelike, of norm $-a^2$.

## Worked Example

Take $\tilde Q=e_t+\vec e_x+i\vec e_y$. In the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$,

$$
\mathsf M(\Theta_{\tilde Q})=
\begin{pmatrix}
3 & 0 & -2i & 2i\\
0 & 1 & 0 & 0\\
2i & 0 & 1 & -2\\
2i & 0 & 2 & -1
\end{pmatrix}.
$$

The matrix is the identity plus

$$
\mathsf N=
\begin{pmatrix}
2 & 0 & -2i & 2i\\
0 & 0 & 0 & 0\\
2i & 0 & 0 & -2\\
2i & 0 & 2 & -2
\end{pmatrix}.
$$

The rank of $\mathsf N$ is two, the rank of $\mathsf N^2$ is one, and $\mathsf N^3=0$. The second coordinate is fixed, and the remaining three coordinates carry one Jordan block of size three. The determinant is one.

The Cartan factors are

$$
\tilde H=\sqrt2\,e_t+i\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\tilde V=\frac{e_t+\vec e_x}{\sqrt2},
$$

and the sandwich is the composition of the positive operator $\Theta_{\tilde H}$ and the $*$-unitary operator $\Theta_{\tilde V}$. The example shows the general structure: the product is unipotent, the factors are not, and the fixed coordinate is the remnant of the $1\times1$ block.



## Summary

### Main Results

| Item | Value |
|---|---|
| stratum | $\vec\Upsilon\neq0$, the Jordan part of $\Sigma_{10}$ |
| operator | $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ |
| sector form | $\Theta_{\tilde Q}=\lvert Q_t\rvert^{2}\Theta_{e_t+\vec\Upsilon}$ |
| nilpotent part | $\mathsf N=A+B+AB$, $A=L_{\vec\Upsilon}$, $B=R_{\vec\Upsilon^{*}}$ |
| powers | $\mathsf N^2=2AB$, $\mathsf N^3=0$ |
| ranks | $\operatorname{rank}\mathsf N=2$, $\operatorname{rank}\mathsf N^2=1$ |
| Jordan form | one block of size three and one of size one |
| eigenvalue | $\lvert Q_t\rvert^{2}$ |
| determinant | $\lvert Q_t\rvert^{8}$ |
| polar factors | $\Theta_{\tilde H}$ positive, $\Theta_{\tilde V}$ $*$-unitary |
| phase | invisible, $\Theta_{e^{i\alpha}}=\mathrm{id}$ |
| fixed subspace | the span of $\vec A$ and $e_t+i\vec c$, $\vec c=\vec A\times\vec B/a^2$ |

On the scalar line $\vec\Upsilon=0$ the sandwich is $\lvert Q_t\rvert^{2}I_4$: rank four, spectrum $\lvert Q_t\rvert^{2}$ with geometric multiplicity four, Jordan type $1+1+1+1$, and $\mathsf N=0$. The Jordan data in the table are those of the Jordan part. The exponential of the operator is the companion *The Sandwich Exponential of a N-Regular, Spectrally Degenerate Biquaternion*.

### What the Sandwich Shows

- On the Jordan part the sandwich is a scalar times a unipotent operator with a single $3\times3$ block and a single $1\times1$ block; on the scalar line it is a scalar.
- Its polar decomposition is the sandwich of the Cartan factors; the factors are positive and $*$-unitary, and their product is unipotent.
- The two spinor slots of the regular sector coalesce into the Jordan chain.
- The phase cancels, so the sandwich sees only the scale, the boost and the rotor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $N=\langle\tilde Q\rangle_{\natural}$ | the reduced product |
| $B^2=\langle\vec Q,\vec Q\rangle_{\natural}$ | the vector form |
| $\Sigma_{10}$ | the N-regular, spectrally degenerate sector |
| $\vec\Upsilon=\vec Q/Q_t$ | the null vector of the normal form |
| $\Theta_{\tilde Q}$ | the sandwich $\tilde X\mapsto\tilde Q\tilde X\tilde Q^{*}$ |
| $L_{\tilde Q},R_{\tilde Q}$ | left and right multiplication |
| $\tilde H,\tilde V$ | the positive and $*$-unitary Cartan factors |
| $\psi,\theta$ | the rapidity and the rotor angle |
| $\vec A,\vec B$ | the real and imaginary parts of $\vec\Upsilon$; the arrows distinguish them from the operators $A,B$ |
| $a$ | the null parameter, $\lvert\vec A\rvert=\lvert\vec B\rvert=a$ |
| $\vec c$ | $\vec A\times\vec B/a^2$, the unit vector of the fixed null direction |
| $\mathsf N$ | $\Theta_{\tilde U}-I=A+B+AB$ |

## Further Reading

- [The Sandwich of a N-Regular, Spectrally Regular Biquaternion](the-sandwich-of-a-n-regular-spectrally-regular-biquaternion.html), for the general sandwich and its two slots.
- [The Sandwich Exponential of a N-Regular, Spectrally Degenerate Biquaternion](the-sandwich-exponential-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the null rotation and the locked parameter.
- [The One-Sided Operators of a N-Regular, Spectrally Degenerate Biquaternion](the-one-sided-operators-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the one-sided companion.
- [The Cartan Hermitian Pairing of the Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the element-level factorization used here.
