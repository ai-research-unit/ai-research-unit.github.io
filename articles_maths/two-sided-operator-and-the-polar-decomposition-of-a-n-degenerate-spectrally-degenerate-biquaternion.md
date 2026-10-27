# __Two-Sided Operator and the Polar Decomposition of a N-Degenerate, Spectrally Degenerate Biquaternion__

## Introduction

This article is the vector-side companion of *One-Sided Operator and the Polar Decomposition of a N-Degenerate, Spectrally Degenerate Biquaternion*. The element is a pure null vector

$$
\tilde Q=\tilde\nu=\vec A+i\vec B,
\qquad
\vec A,\vec B\in\mathbb{R}^{3},
\qquad
\lVert\vec A\rVert=\lVert\vec B\rVert=a>0,
\qquad
\vec A\cdot\vec B=0,
\qquad
\tilde\nu^{2}=0 .
$$

The word **N-degenerate** refers to $\langle\tilde Q\rangle_{\natural}=0$; the word **spectrally degenerate** to $B^{2}=0$. The two-sided operator is the Hermitian sandwich

$$
\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}.
$$

On this sector the sandwich has rank one and is square-zero. It is the maximal collapse of the two-sided operator: one Jordan block of size two at eigenvalue zero, and two further fixed zero directions. The polar pair of *The Polar Decomposition of a N-Degenerate Biquaternion* survives,

$$
\tilde Q=\tilde Q_H\tilde Q_0,
\qquad
\tilde Q_H=2a\tilde\Pi_+,
\qquad
\tilde Q_0=\frac{\tilde\nu}{2a},
\qquad
\tilde\Pi_+=\frac{e_t+i\vec c}{2},
\qquad
\vec c=\frac{\vec A\times\vec B}{a^{2}},
$$

with $\tilde Q_0$ a **nilpotent** partial isometry. The main result is the scalar collapse

$$
\boxed{\;\Theta_{\tilde Q}=4a^{2}\,\Theta_{\tilde Q_0}\;}
$$

with $\Theta_{\tilde Q_0}$ a nilpotent partial isometry. The non-zero singular value is $4a^{2}=(2a)^{2}$; the only eigenvalue is zero. The sandwich kills the whole algebra in two steps.

The article is organized as follows. §*The Polar Pair* recalls the canonical Hermitian pair and the rank-one singular value decomposition. §*The Sandwich* computes the square, the rank, the spectrum, the image, the kernel and the explicit Jordan chain. §*The Polar Decomposition of the Sandwich* proves the scalar collapse and explains the phase cancellation. §*The Two Slots* gives the Peirce and singular-vector pictures. §*The Exponential* computes the unipotent flow. §*Worked Example* treats the standard nilpotent.

## The Polar Pair

The conventions are those of the companion articles. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $\vec e_x\vec e_y=\vec e_z$ and $\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t$. The Hermitian conjugation is $\tilde X^{*}=\overline{\tilde X^{\natural}}$, the Hermitian norm is $\langle\tilde X\rangle_{*}=\operatorname{Sc}(\tilde X\tilde X^{*})$, and the quaternionic norm is $\langle\tilde X\rangle_{\natural}=\sum_\mu X_\mu^{2}$.

### The canonical Hermitian pair

Let $\tilde\nu=\vec A+i\vec B$ with $\vec A,\vec B$ real, orthogonal and of equal norm $a>0$. Put

$$
\vec c=\frac{\vec A\times\vec B}{a^{2}},
\qquad
\tilde\Pi_+=\frac{e_t+i\vec c}{2},
\qquad
\tilde\Pi_-=\frac{e_t-i\vec c}{2}.
$$

The vector $\vec c$ is real and unit; the idempotents are Hermitian and complementary. They satisfy

$$
\tilde\Pi_+\tilde\nu=\tilde\nu,
\qquad
\tilde\nu\tilde\Pi_+=0,
\qquad
\tilde\Pi_-\tilde\nu=0,
\qquad
\tilde\nu\tilde\Pi_-=\tilde\nu,
$$

so $\tilde\nu=\tilde\Pi_+\tilde\nu\tilde\Pi_-$ lies in the mixed corner $\mathbb{B}_{+-}$. The element is annihilated by the two products that would place it in a diagonal corner. Its norms are

$$
\langle\tilde\nu\rangle_{\natural}=0,
\qquad
\langle\tilde\nu\rangle_{*}=2a^{2},
\qquad
\tilde\nu\tilde\nu^{*}=4a^{2}\tilde\Pi_+,
\qquad
\tilde\nu^{*}\tilde\nu=4a^{2}\tilde\Pi_- .
$$

### The polar pair

The polar pair is

$$
\boxed{\;
P=\tilde\Pi_+,
\qquad
\tilde Q_H=2a\tilde\Pi_+,
\qquad
\tilde Q_0=\frac{\tilde\nu}{2a},
\qquad
\tilde Q=\tilde Q_H\tilde Q_0,
\qquad
\tilde Q_0^{2}=0 .
\;}
$$

The Hermitian factor is positive semidefinite of rank one, with spectrum $\{0,2a\}$. The partial-isometry factor is nilpotent:

$$
\tilde Q_0\tilde Q_0^{*}=\tilde\Pi_+,
\qquad
\tilde Q_0^{*}\tilde Q_0=\tilde\Pi_-,
\qquad
\tilde Q_0\tilde Q_0^{*}\tilde Q_0=\tilde Q_0,
\qquad
\tilde Q_0^{2}=0 .
$$

The polar pair is the rank-one singular value decomposition of the nilpotent. The "unitary" factor is a nilpotent partial isometry, not a unitary; the pair is still the general pair of *The Polar Decomposition of a N-Degenerate Biquaternion*, but it is as far as possible from the modulus–unit form.

### The matrix model

In the matrix model $\mathsf M_2(\tilde\nu)=2a\,u v^{\dagger}$ with $u,v$ unit and orthogonal:

$$
v^{\dagger}u=\frac{Q_t}{a}=0,
\qquad
u^{\dagger}u=v^{\dagger}v=1,
\qquad
u\perp v .
$$

The polar factors are

$$
P=u u^{\dagger}=\tilde\Pi_+,
\qquad
\tilde Q_H=2a\,u u^{\dagger},
\qquad
\tilde Q_0=u v^{\dagger},
\qquad
\tilde Q_0^{*}=v u^{\dagger},
\qquad
\tilde Q_0^{2}=u(v^{\dagger}u)v^{\dagger}=0 .
$$

The two slots are orthogonal. The overlap $v^{\dagger}u$ vanishes; this is the matrix form of the spectral degeneration. The sandwich is computed from the same decomposition:

$$
\mathsf M_2\bigl(\Theta_{\tilde Q}(\tilde X)\bigr)
=(2a)^{2}u v^{\dagger}\mathsf M_2(\tilde X)v u^{\dagger}
=4a^{2}\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)u u^{\dagger}.
$$

Because $v^{\dagger}u=0$, applying the operator twice gives zero. The single chain is visible in the formula: the scalar $v^{\dagger}\mathsf M_2(\tilde X)v$ is written on the line $u u^{\dagger}$, and the line is annihilated on the next step.

## The Sandwich

### Elementary properties

**Proposition.** Let $\tilde Q,\tilde Q'\in\mathbb{B}$. Then:

**(a)** $\Theta_{\tilde Q}$ is $\mathbb{C}$-linear;

**(b)** $\Theta_{\tilde Q\tilde Q'}=\Theta_{\tilde Q}\circ\Theta_{\tilde Q'}$;

**(c)** $\Theta_{\tilde Q}$ is invertible exactly when $\tilde Q$ is a unit, with inverse $\Theta_{\tilde Q^{-1}}$;

**(d)** $\Theta_{\tilde Q}$ preserves the real forms $\mathbb{M}_+$ and $\mathbb{M}_-$;

**(e)** the adjoint is $\Theta_{\tilde Q}^{*}=\Theta_{\tilde Q^{*}}$;

**(f)** the norm scales as

$$
\bigl\langle\Theta_{\tilde Q}(\tilde X)\bigr\rangle_{\natural}
=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}.
$$

On $\Sigma_{00}$ the element is a zero divisor, so $\Theta_{\tilde Q}$ is not invertible. The properties are those of *Operators of the Polar Word: The Common Framework*; the sector changes the values.

### The square, the rank and the spectrum

**Theorem.** On $\Sigma_{00}$:

**(a)** $\Theta_{\tilde Q}^{2}=0$;

**(b)** $\Theta_{\tilde Q}$ has complex rank $1$;

**(c)** its only eigenvalue is $0$, with algebraic multiplicity $4$ and geometric multiplicity $3$;

**(d)** its Jordan form is $J_2(0)\oplus0\oplus0$, with minimal polynomial $X^{2}$;

**(e)** $\operatorname{tr}\Theta_{\tilde Q}=0$ and $\det\Theta_{\tilde Q}=0$;

**(f)** for every $\tilde X$, $\langle\Theta_{\tilde Q}(\tilde X)\rangle_{\natural}=0$; the image lies on the null cone.

*Proof.* In the matrix model,

$$
\Theta_{\tilde Q}(\tilde X)
=4a^{2}\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)u u^{\dagger}.
$$

The image is contained in the line $\mathbb{C}u u^{\dagger}$, and it is non-zero because $\Theta_{\tilde Q}(e_t)=\tilde\nu\tilde\nu^{*}=4a^{2}\tilde\Pi_+$. Hence the rank is one. Applying the formula twice,

$$
\Theta_{\tilde Q}^{2}(\tilde X)
=(4a^{2})^{2}\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)
(v^{\dagger}u)(u^{\dagger}v)u u^{\dagger}=0,
$$

because $v^{\dagger}u=0$. The only eigenvalue of a square-zero operator is zero; the algebraic multiplicity is four, the geometric multiplicity is the dimension of the kernel, three; the Jordan form is one block of size two and two blocks of size one. The trace is zero and the determinant is zero. The norm is $\langle\Theta_{\tilde Q}(\tilde X)\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}=0$.
The image is a null line because $\langle\tilde Q\tilde X\tilde Q^{*}\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}=0$.

### The image and the kernel

The image is the null line

$$
\operatorname{im}\Theta_{\tilde Q}
=\mathbb{C}\tilde\Pi_+,
\qquad
\tilde\Pi_+=\frac{\tilde Q\tilde Q^{*}}{4a^{2}}.
$$

The kernel is the hyperplane

$$
\ker\Theta_{\tilde Q}
=\bigl\{\tilde X:\tilde\nu\tilde X\tilde\nu^{*}=0\bigr\},
\qquad
\dim_{\mathbb{C}}\ker\Theta_{\tilde Q}=3.
$$

In the matrix model it is $\{X:v^{\dagger}Xv=0\}$. The kernel contains the right annihilator $A(\tilde\nu)=\ker L_{\tilde\nu}$ and the left annihilator of $\tilde\nu^{*}$, because $\tilde\nu\tilde X=0$ or $\tilde X\tilde\nu^{*}=0$ implies $\tilde\nu\tilde X\tilde\nu^{*}=0$. The image is contained in the kernel, since the operator is square-zero; the kernel is strictly larger, because the rank is one.

### The explicit Jordan chain

The canonical Hermitian pair gives a very explicit chain. Since $\tilde\nu\tilde\Pi_-=\tilde\nu$ and $\tilde\nu\tilde\nu^{*}=4a^{2}\tilde\Pi_+$, one has

$$
\boxed{\;
\Theta_{\tilde Q}(\tilde\Pi_-)
=\tilde\nu\tilde\Pi_-\tilde\nu^{*}
=\tilde\nu\tilde\nu^{*}
=4a^{2}\tilde\Pi_+,
\qquad
\Theta_{\tilde Q}(\tilde\Pi_+)=0 .
\;}
$$

Thus

$$
\tilde\Pi_-\longmapsto 4a^{2}\tilde\Pi_+\longmapsto0
$$

is a chain of length two. The other two basis vectors are killed:

$$
\Theta_{\tilde Q}(\tilde\nu)=0,
\qquad
\Theta_{\tilde Q}(\vec X)=0,
$$

where $\vec X$ is the corner vector spanning $\tilde\Pi_-\mathbb{B}\tilde\Pi_+$. In the basis

$$
\bigl(\tilde\Pi_+,\ \tilde\nu,\ \vec X,\ \tilde\Pi_-\bigr)
$$

the sandwich is therefore the single nilpotent block

$$
\boxed{\;
\mathsf M\bigl(\Theta_{\tilde Q}\bigr)=
\begin{pmatrix}
0&0&0&4a^{2}\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
\;}
$$

This matrix is the cleanest form of the operator: rank one, square zero, image $\mathbb{C}\tilde\Pi_+$, kernel $\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\tilde\nu\oplus\mathbb{C}\vec X$, and the single chain from $\tilde\Pi_-$ to $\tilde\Pi_+$.

The chain crosses the Peirce diagram from the $(--)$ corner to the $(+,+)$ corner. The element $\tilde\nu$ lies in the mixed corner $(+-)$; the other mixed corner $(-+)$ is represented by $\vec X$. The sandwich maps the $(--)$ corner to the $(+,+)$ corner and kills the two mixed corners and the $(+,+)$ corner itself. This is the exact two-step collapse of the spectral degeneracy.

### Eigenvalues and singular values

The only eigenvalue is zero. The non-zero singular value is $4a^{2}$: indeed

$$
\Theta_{\tilde Q}\Theta_{\tilde Q}^{*}
=\Theta_{\tilde Q\tilde Q^{*}}
=\Theta_{4a^{2}\tilde\Pi_+}
=(4a^{2})^{2}\Theta_{\tilde\Pi_+},
$$

and $\Theta_{\tilde\Pi_+}$ is an orthogonal projection of rank one, with singular value one. Hence the singular value is $4a^{2}$. The eigenvalue-to-singular-value ratio is zero. This is the maximal defect: the operator has a non-zero singular value but no non-zero eigenvalue, and its image is a null line.

The operator $\Theta_{\tilde Q}=4a^{2}\Theta_{\tilde Q_0}$ is not a partial isometry in general: its singular value is $4a^{2}$, not one. It is $4a^{2}$ times the nilpotent partial isometry $\Theta_{\tilde Q_0}$.

## The Polar Decomposition of the Sandwich

### The scalar collapse

By the polar pair theorem, $\tilde Q=2a\tilde Q_0$ with $\tilde Q_0$ a nilpotent partial isometry. The multiplicativity of $\Theta$ gives

$$
\Theta_{\tilde Q}
=\Theta_{2a\tilde Q_0}
=4a^{2}\Theta_{\tilde Q_0}.
$$

This is the scalar collapse. The canonical left polar factor is

$$
\lvert\Theta_{\tilde Q}\rvert
=\bigl(\Theta_{\tilde Q}\Theta_{\tilde Q}^{*}\bigr)^{1/2}
=\Theta_{\tilde Q_H}
=4a^{2}\Theta_{\tilde\Pi_+},
$$

which is positive semidefinite of rank one. On the image of $\Theta_{\tilde Q_0}$ it acts as the scalar $4a^{2}$, because $\tilde\Pi_+\tilde Q_0=\tilde Q_0$ and therefore $\Theta_{\tilde\Pi_+}\Theta_{\tilde Q_0}=\Theta_{\tilde Q_0}$. Hence

$$
\boxed{\;
\Theta_{\tilde Q}
=\Theta_{\tilde Q_H}\circ\Theta_{\tilde Q_0}
=4a^{2}\Theta_{\tilde Q_0},
\qquad
\Theta_{\tilde Q_0}\Theta_{\tilde Q_0}^{*}\Theta_{\tilde Q_0}
=\Theta_{\tilde Q_0},
\qquad
\Theta_{\tilde Q_0}^{2}=0 .
\;}
$$

The sandwich is $4a^{2}$ times a nilpotent partial isometry. Its non-zero singular value is $4a^{2}=(2a)^{2}$; its only eigenvalue is zero. The polar decomposition of the operator is therefore a scalar times a nilpotent partial isometry, the extreme case of the collapse.

### The phase

For a complex multiple

$$
\tilde\nu=c_0(\vec e_x+i\vec e_y),
\qquad
c_0=\lvert c_0\rvert e^{i\beta},
$$

one has $a=\lvert c_0\rvert$ and

$$
\tilde Q_0=e^{i\beta}\frac{\vec e_x+i\vec e_y}{2},
\qquad
\Theta_{\tilde Q_0}
=\Theta_{(\vec e_x+i\vec e_y)/2}
=\frac14\Theta_{\vec e_x+i\vec e_y},
$$

independent of the phase. The sandwich is

$$
\Theta_{\tilde Q}
=4\lvert c_0\rvert^{2}\Theta_{\tilde Q_0}
=\lvert c_0\rvert^{2}\Theta_{\vec e_x+i\vec e_y}
=\Theta_{\tilde\nu},
$$

so the phase has cancelled. The one-sided operator keeps the phase; the sandwich sees only $\lvert c_0\rvert^{2}$ and the canonical pair. The sign $\tilde\nu\mapsto-\tilde\nu$ also cancels.

### The polar pair of the element and of the operator

The element pair is $(\tilde Q_H,\tilde Q_0)$, with $\tilde Q_H=2a\tilde\Pi_+$ positive of rank one and $\tilde Q_0$ a nilpotent partial isometry. The operator pair is $(\Theta_{\tilde Q_H},\Theta_{\tilde Q_0})$, with $\Theta_{\tilde Q_H}=4a^{2}\Theta_{\tilde\Pi_+}$ positive of rank one and $\Theta_{\tilde Q_0}$ a nilpotent partial isometry. The element pair is the rank-one singular value decomposition of the nilpotent; the operator pair is its congruence. The scalar $4a^{2}$ is the square of the element's singular value $2a$.

The spectral pair of the element does not exist off the origin: the element has only the eigenvalue zero, and no non-trivial idempotent commutes with it. The Hermitian form supplies the canonical pair $(\tilde\Pi_+,\tilde\Pi_-)$, and the polar decomposition uses exactly that pair. This is the precise sense in which the polar pair survives while the spectral decomposition fails.

## The Two Slots

### The Peirce picture

In the canonical basis $(\tilde\Pi_+,\tilde\nu,\vec X,\tilde\Pi_-)$ the sandwich is the single block of §*The Explicit Jordan Chain*:

$$
\mathsf M\bigl(\Theta_{\tilde Q}\bigr)=
\begin{pmatrix}
0&0&0&4a^{2}\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
$$

The chain is $\tilde\Pi_-\to4a^{2}\tilde\Pi_+\to0$. The image is the $(+,+)$ corner, the chain starts in the $(--)$ corner, and the two mixed corners are killed. In the regular sector the sandwich is a conformal Lorentz transformation with four eigenvalue products $\lambda_i\bar\lambda_j$; here all four products vanish. In the N-regular, spectrally degenerate sector the sandwich is a unipotent operator of Jordan type $3+1$; here it is a nilpotent operator of Jordan type $2+1+1$. The two chiral slots of the regular theory coalesce into the single chain $\tilde\Pi_-\to\tilde\Pi_+$.

### The singular-vector picture

In the matrix model the two slots are the singular vectors $u$ and $v$, and they are orthogonal:

$$
v^{\dagger}u=0,
\qquad
\Theta_{\tilde Q}(\tilde X)
=4a^{2}\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)u u^{\dagger}.
$$

The sandwich reads the $v$-slot of $\tilde X$ and writes it on the $u$-slot. Because $u\perp v$, the line on which it writes is annihilated on the next step. The relative phase of $u$ and $v$ cancels, and the overlap is zero. The angle $\theta$ between the slots is $\pi/2$; the eigenvalue-to-singular-value ratio is $\cos^{2}\theta=0$. The sandwich sees only the orthogonality.

This is the extreme case of the two-slot structure. On $\Sigma_{01}$ the slots had overlap $\cos\theta=1/\sqrt{\kappa}\in(0,1]$, and the sandwich was a projection up to scale. Here the overlap is zero, and the sandwich is nilpotent. The spectral wall is the orthogonality of the two slots.

## The Exponential

**The operator exponential.** Since $\Theta_{\tilde Q}^{2}=0$,

$$
\boxed{\;
\exp\bigl(t\Theta_{\tilde Q}\bigr)=I+t\Theta_{\tilde Q}
\;}
$$

for every complex $t$. The eigenvalues are all $1$; the Jordan form is $J_2(1)\oplus1\oplus1$; the determinant is $1$. The group is unipotent: it is a shear, not a dilation. It is invertible for every $t$, although the generator is nilpotent and singular.

**The element flow.** Since $\tilde\nu^{2}=0$,

$$
\exp\bigl(t\tilde\nu\bigr)=e_t+t\tilde\nu .
$$

The quaternionic norm is $1$, and the vector form is

$$
B^{2}\bigl(\exp(t\tilde\nu)\bigr)=t^{2}B^{2}(\tilde\nu)=0 .
$$

Hence the exponential is a unit with $B^{2}=0$: for every $t$ it lies in the N-regular, spectrally degenerate sector $\Sigma_{10}$ (at $t=0$ it is $e_t$). The element flow moves one wall away: it removes the norm degeneration and preserves the spectral one. Its sandwich is

$$
\Theta_{\exp(t\tilde\nu)}
=\exp\bigl(t\Theta_{\tilde Q}\bigr),
$$

a unipotent Lorentz flow of Jordan type $2+1+1$. It fixes the kernel hyperplane and shears along the single chain. The generator $\Theta_{\tilde Q}$ is singular; the one-parameter group it generates is invertible.

The one-sided exponential of the companion article is a unipotent shear of the operator space, not a Lorentz transformation. The two-sided exponential is a unipotent Lorentz flow; the difference is the same as in the regular sector, where the one-sided operator acts on spinors and the sandwich acts on the vector side.

## Worked Example

### The standard nilpotent

Take

$$
\tilde\nu=\vec e_x+i\vec e_y .
$$

Then $a=1$, $\vec c=\vec e_z$, and

$$
\tilde\Pi_+=\frac{e_t+i\vec e_z}{2},
\qquad
\tilde\Pi_-=\frac{e_t-i\vec e_z}{2},
\qquad
\tilde Q_H=e_t+i\vec e_z,
\qquad
\tilde Q_0=\frac{\vec e_x+i\vec e_y}{2}.
$$

The matrix model is

$$
\mathsf M_2(\tilde\nu)=
\begin{pmatrix}0&-2i\\0&0\end{pmatrix},
\qquad
\mathsf M_2(\tilde Q_H)=
\begin{pmatrix}2&0\\0&0\end{pmatrix},
\qquad
\mathsf M_2(\tilde Q_0)=
\begin{pmatrix}0&-i\\0&0\end{pmatrix}.
$$

In the standard basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ the sandwich is

$$
\mathsf M\bigl(\Theta_{\tilde\nu}\bigr)=
\begin{pmatrix}
2&0&0&2i\\
0&0&0&0\\
0&0&0&0\\
2i&0&0&-2
\end{pmatrix},
$$

with trace zero, rank one and square zero. The image is the line $\mathbb{C}(e_t+i\vec e_z)=\mathbb{C}\tilde\Pi_+$; the first column is $2(e_t+i\vec e_z)=4\tilde\Pi_+$.

For the Peirce form, take

$$
\vec X=\frac{-\vec e_x+i\vec e_y}{4},
\qquad
\tilde\nu\vec X=\tilde\Pi_+,
\qquad
\vec X\tilde\nu=\tilde\Pi_- .
$$

In the basis $(\tilde\Pi_+,\tilde\nu,\vec X,\tilde\Pi_-)$,

$$
\mathsf M\bigl(\Theta_{\tilde\nu}\bigr)=
\begin{pmatrix}
0&0&0&4\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
$$

the single chain being $\tilde\Pi_-\to4\tilde\Pi_+\to0$. The exponential is

$$
\exp\bigl(t\Theta_{\tilde\nu}\bigr)=I+t\Theta_{\tilde\nu}.
$$

### A complex scalar multiple

For

$$
\tilde\nu=c_0(\vec e_x+i\vec e_y),
\qquad
c_0=\lvert c_0\rvert e^{i\beta},
$$

the element has $a=\lvert c_0\rvert$, and

$$
\tilde Q_0=e^{i\beta}\frac{\vec e_x+i\vec e_y}{2},
\qquad
\Theta_{\tilde\nu}
=4\lvert c_0\rvert^{2}\Theta_{\tilde Q_0}.
$$

The phase $e^{i\beta}$ cancels in the sandwich. The sandwich depends only on $\lvert c_0\rvert$ and the canonical pair; the one-sided operator of the companion article keeps the phase.

## Summary

### Main Results

| item | value |
|---|---|
| sector | $\Sigma_{00}=\{\langle\tilde Q\rangle_{\natural}=0,\ B^{2}=0\}$ |
| parameter | $\tilde\nu=\vec A+i\vec B$, $\lVert\vec A\rVert=\lVert\vec B\rVert=a>0$, $\vec A\cdot\vec B=0$ |
| canonical pair | $\tilde\Pi_\pm=(e_t\pm i\vec c)/2$, $\vec c=\vec A\times\vec B/a^{2}$ |
| polar pair | $\tilde Q_H=2a\tilde\Pi_+$, $\tilde Q_0=\tilde\nu/(2a)$, $\tilde Q_0^{2}=0$ |
| sandwich | $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ |
| square | $\Theta_{\tilde Q}^{2}=0$ |
| rank | $1$ |
| spectrum | $\{0\}$, algebraic multiplicity $4$, geometric multiplicity $3$ |
| Jordan form | $J_2(0)\oplus0\oplus0$ |
| trace | $0$ |
| determinant | $0$ |
| eigenvalue | $0$ |
| singular value | $4a^{2}$ |
| image | the null line $\mathbb{C}\tilde\Pi_+$ |
| kernel | $\{\tilde X:\tilde\nu\tilde X\tilde\nu^{*}=0\}$, a hyperplane |
| chain | $\tilde\Pi_-\mapsto4a^{2}\tilde\Pi_+\mapsto0$ |
| scalar collapse | $\Theta_{\tilde Q}=4a^{2}\Theta_{\tilde Q_0}$ |
| exponential | $\exp(t\Theta_{\tilde Q})=I+t\Theta_{\tilde Q}$ |
| element flow | $\exp(t\tilde\nu)=e_t+t\tilde\nu$, a unit in $\Sigma_{10}$ for every $t$ (at $t=0$ it is $e_t$) |

### What the Sandwich Shows

- The norm degeneration fixes the rank: the sandwich has rank one and its image is a null line.
- The spectral degeneration fixes the Jordan type: the sandwich is square-zero, with one block of size two and two further fixed zero directions.
- The image is contained in the kernel; the algebra is a non-trivial extension, and the two-step collapse is visible in the single chain $\tilde\Pi_-\to\tilde\Pi_+\to0$.
- The polar pair collapses to $\Theta_{\tilde Q}=4a^{2}\Theta_{\tilde Q_0}$ with $\Theta_{\tilde Q_0}$ a nilpotent partial isometry; the positive factor acts as the scalar $4a^{2}$ on the image.
- The non-zero singular value is $4a^{2}=(2a)^{2}$, the square of the one-sided singular value; the only eigenvalue is zero.
- The phase and the sign cancel. The sandwich sees only $\lvert c_0\rvert^{2}$ and the canonical Hermitian pair.
- The two slots are orthogonal; the angle $\theta=\pi/2$ and the eigenvalue-to-singular-value ratio $\cos^{2}\theta=0$ are the quantitative form of the spectral wall.
- The exponential is unipotent; it moves the element from $\Sigma_{00}$ to $\Sigma_{10}$, removing the norm degeneration and preserving the spectral one.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\nu=\vec A+i\vec B$ | a non-zero element of $\Sigma_{00}$ |
| $a=\lVert\vec A\rVert=\lVert\vec B\rVert$ | the half singular value |
| $\vec c=\vec A\times\vec B/a^{2}$ | the unit spectral direction |
| $\tilde\Pi_\pm=(e_t\pm i\vec c)/2$ | the canonical Hermitian idempotents |
| $\Theta_{\tilde Q}$ | the sandwich $\tilde X\mapsto\tilde Q\tilde X\tilde Q^{*}$ |
| $\tilde Q_H=2a\tilde\Pi_+$ | the Hermitian factor |
| $\tilde Q_0=\tilde\nu/(2a)$ | the nilpotent partial-isometry factor |
| $L_{\tilde\nu},R_{\tilde\nu}$ | the one-sided operators of the companion article |
| $\vec X$ | a normalized corner vector, $\tilde\nu\vec X=\tilde\Pi_+$ |
| $J_2(0)$ | the nilpotent Jordan block of size two |

## Further Reading

- [Two-Sided Operator and the Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](two-sided-operator-and-the-polar-decomposition-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the unipotent three-plus-one sandwich at the spectral wall of the regular sector.
- [Two-Sided Operator and the Polar Decomposition of a N-Degenerate, Spectrally Regular Biquaternion](two-sided-operator-and-the-polar-decomposition-of-a-n-degenerate-spectrally-regular-biquaternion.html), for the projection case of the same sector pair.
- [One-Sided Operator and the Polar Decomposition of a N-Degenerate, Spectrally Degenerate Biquaternion](one-sided-operator-and-the-polar-decomposition-of-a-n-degenerate-spectrally-degenerate-biquaternion.html), for the companion one-sided operator.
- [The Polar Decomposition of a N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the general two-factor pair on the null cone.
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the canonical Hermitian pair, the Peirce data and the no-eigenbasis theorem.
- [The Jordan Basis of a Spectrally Degenerate Biquaternion](the-spectrally-degenerate-sector-and-construction-of-the-jordan-basis-of-a-biquaternion.html), for the Jordan basis used in the chain.
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the contrasting spectrally regular case.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the null cone and the quaternionic norm.
