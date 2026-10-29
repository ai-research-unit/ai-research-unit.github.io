# __The Two-Sided Operator of a N-Degenerate, Spectrally Regular Biquaternion__

## Introduction

This article is the vector-side companion of *The One-Sided Operators of a N-Degenerate, Spectrally Regular Biquaternion*. The element $\tilde Q$ lies in the N-degenerate, spectrally regular sector $\Sigma_{01}$,

$$
\tilde Q=c\,\tilde\Pi,\qquad c=2Q_t\neq0,\qquad \tilde\Pi^{2}=\tilde\Pi,\qquad \tilde\Pi\neq0,e_t,
$$

so $\langle\tilde Q\rangle_{\natural}=0$ and $B^{2}\neq0$. The two-sided operator is the Hermitian sandwich

$$
\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}.
$$

On the null cone the modulus $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$ vanishes, so the four-factor word does not exist. The two-factor polar pair $\tilde Q=\tilde Q_H\tilde Q_0$ survives, and the sandwich reads it as

$$
\Theta_{\tilde Q}
=\Theta_{\tilde Q_H}\circ\Theta_{\tilde Q_0},
\qquad
\tilde Q_H=2aP,
\qquad
\tilde Q_0=\frac{\tilde Q}{2a},
$$

with $a=\sqrt{\langle\tilde Q\rangle_{*}/2}>0$ and $P$ a rank-one Hermitian idempotent. The main result is that **the sandwich collapses to a scalar times a partial isometry**:

$$
\boxed{\;\Theta_{\tilde Q}=4a^{2}\,\Theta_{\tilde Q_0}\;}
$$

because the positive factor $\Theta_{\tilde Q_H}=4a^{2}\Theta_P$ acts as the scalar $4a^{2}$ on the image of $\Theta_{\tilde Q_0}$. The operator has rank one, spectrum $\{\lvert c\rvert^{2},0,0,0\}$ and is diagonalizable; it is an oblique projection onto a null line, not a nilpotent. The wall $B^{2}=0$ is the boundary at which this projection gives way to the square-zero sandwich of *The Two-Sided Operator of a N-Degenerate, Spectrally Degenerate Biquaternion*.

The article is organized as follows. §*The Polar Pair* recalls the rank-one pair and the matrix model. §*The Sandwich* computes the closed form, the rank, the spectrum, the image and the kernel. §*The Polar Decomposition of the Sandwich* reads the pair and proves the scalar collapse. §*The Two Slots* gives the Peirce and singular-vector pictures and the cancellation of the phase. §*The Exponential* computes the one-parameter group. §*Worked Examples* treats a Hermitian and a non-Hermitian idempotent.

## The Polar Pair

The conventions are those of the companion article. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $\vec e_x\vec e_y=\vec e_z$ and $\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t$. The Hermitian conjugation is $\tilde X^{*}=\overline{\tilde X^{\natural}}$, the Hermitian norm is $\langle\tilde X\rangle_{*}=\operatorname{Sc}(\tilde X\tilde X^{*})$, and the quaternionic norm is $\langle\tilde X\rangle_{\natural}=\sum_\mu X_\mu^{2}$.

The matrix model $\mathsf M_2$ sends $e_t$ to $I_2$ and $\vec e_k$ to $-i\sigma_k$; it is multiplicative, and

$$
\det\mathsf M_2(\tilde X)=\langle\tilde X\rangle_{\natural},
\qquad
\tfrac12\operatorname{tr}\bigl(\mathsf M_2(\tilde X)\mathsf M_2(\tilde X)^{\dagger}\bigr)=\langle\tilde X\rangle_{*}.
$$

The non-zero null cone is the set of rank-one matrices. For $\tilde Q\neq0$ on $\mathcal N$ there are unit vectors $u,v\in\mathbb{C}^{2}$ and $a>0$ with

$$
\mathsf M_2(\tilde Q)=2a\,u v^{\dagger},
\qquad
2a=\sqrt{2\langle\tilde Q\rangle_{*}},
\qquad
v^{\dagger}u=\frac{Q_t}{a}=\frac{c}{2a}.
$$

The two factors are the left and right slots of the rank-one matrix. The overlap $v^{\dagger}u$ is non-zero exactly on $\Sigma_{01}$; on $\Sigma_{00}$ the slots are orthogonal. The polar pair is

$$
P=u u^{\dagger}=\frac{\tilde Q\tilde Q^{*}}{4a^{2}},
\qquad
\tilde Q_H=2aP,
\qquad
\tilde Q_0=u v^{\dagger}=\frac{\tilde Q}{2a},
$$

with $P$ a rank-one Hermitian idempotent and $\tilde Q_0$ a partial isometry. In the closed form of the sector,

$$
a=\frac{\lvert c\rvert\sqrt{\kappa}}{2}=\lvert Q_t\rvert\sqrt{\kappa},
\qquad
P=\frac{\tilde\Pi\tilde\Pi^{*}}{\kappa},
\qquad
\tilde Q_0=\frac{c}{\lvert c\rvert}\frac{\tilde\Pi}{\sqrt{\kappa}},
\qquad
\kappa=\frac{1+\lVert\tilde\Xi\rVert_E^{2}}{2},
$$

where $\tilde\Xi=2\tilde\Pi-e_t$ and $\kappa\ge1$. The overlap is $v^{\dagger}u=Q_t/a=c/(2a)$, with modulus $1/\sqrt{\kappa}=\cos\theta$, where $\theta$ is the angle between the two slots.

The sandwich of the pair is computed in the matrix model. For any $\tilde X$,

$$
\mathsf M_2\bigl(\Theta_{\tilde Q}(\tilde X)\bigr)
=(2a)^{2}u v^{\dagger}\,\mathsf M_2(\tilde X)\,v u^{\dagger}
=4a^{2}\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)u u^{\dagger}.
$$

Thus the image is the line $\mathbb{C}u u^{\dagger}=\mathbb{C}P$ and the value is the scalar $v^{\dagger}\mathsf M_2(\tilde X)v$. This formula is the source of every result below.

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

On $\Sigma_{01}$ the element is a zero divisor, so $\Theta_{\tilde Q}$ is not invertible. The properties are those of *Operators of the Polar Word: The Common Framework*; the sector changes the values.

### The closed form

Let $\tilde Q=c\tilde\Pi$. Since $\tilde\Pi^{2}=\tilde\Pi$,

$$
\Theta_{\tilde Q}
=\lvert c\rvert^{2}\Theta_{\tilde\Pi},
\qquad
\Theta_{\tilde\Pi}^{2}
=\Theta_{\tilde\Pi},
\qquad
\Theta_{\tilde Q}^{2}
=\lvert c\rvert^{2}\Theta_{\tilde Q}.
$$

Thus $\Theta_{\tilde Q}/\lvert c\rvert^{2}$ is an idempotent of the operator space, and $\Theta_{\tilde Q}$ is an idempotent up to scale. It is not an orthogonal projection unless $\tilde\Pi$ is Hermitian.

**Theorem (rank, spectrum and Jordan form).** On $\Sigma_{01}$:

**(a)** $\Theta_{\tilde Q}$ has complex rank $1$;

**(b)** its spectrum is $\{\lvert c\rvert^{2},0\}$, with algebraic multiplicities $1$ and $3$, and geometric multiplicities $1$ and $3$;

**(c)** it is diagonalizable, with minimal polynomial $X(X-\lvert c\rvert^{2})$;

**(d)** $\operatorname{tr}\Theta_{\tilde Q}=\lvert c\rvert^{2}=4a^{2}\cos^{2}\theta$ and $\det\Theta_{\tilde Q}=0$;

**(e)** for every $\tilde X$, $\langle\Theta_{\tilde Q}(\tilde X)\rangle_{\natural}=0$; the image lies on the null cone.

*Proof.* In the matrix model, the formula above gives

$$
\Theta_{\tilde Q}(\tilde X)=4a^{2}\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)u u^{\dagger}.
$$

The image is contained in the line $\mathbb{C}u u^{\dagger}$, and it is non-zero because $u u^{\dagger}$ is in the image: take $\tilde X$ with $\mathsf M_2(\tilde X)=u u^{\dagger}$; then $v^{\dagger}u u^{\dagger}v=\lvert v^{\dagger}u\rvert^{2}\neq0$. Hence the rank is one. The square is

$$
\Theta_{\tilde Q}^{2}
=(4a^{2})^{2}\lvert v^{\dagger}u\rvert^{2}
\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)u u^{\dagger}
=\lvert c\rvert^{2}\Theta_{\tilde Q},
$$

because $c=2a\,v^{\dagger}u$. The operator is a non-zero scalar multiple of an idempotent, so it is diagonalizable with eigenvalues $\lvert c\rvert^{2}$ and $0$. The trace is $\lvert c\rvert^{2}$ and the determinant is zero. The norm is $\langle\Theta_{\tilde Q}(\tilde X)\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}=0$.
The image is a null line because $\langle\tilde Q\tilde X\tilde Q^{*}\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}=0$.

### The image and the kernel

The image is the line

$$
\operatorname{im}\Theta_{\tilde Q}=\mathbb{C}P,
\qquad
P=\frac{\tilde Q\tilde Q^{*}}{4a^{2}}=\frac{\tilde\Pi\tilde\Pi^{*}}{\kappa}.
$$

The line is null: $\langle P\rangle_{\natural}=0$ because $P$ is a non-trivial idempotent. The kernel is the hyperplane

$$
\ker\Theta_{\tilde Q}
=\bigl\{\tilde X:\tilde\Pi\tilde X\tilde\Pi^{*}=0\bigr\},
\qquad
\dim_{\mathbb{C}}\ker\Theta_{\tilde Q}=3.
$$

In the matrix model it is $\{X:v^{\dagger}Xv=0\}$, the hyperplane orthogonal to the rank-one functional $X\mapsto v^{\dagger}Xv$. The kernel contains the right annihilator $A(\tilde Q)=\ker L_{\tilde Q}$ and the left annihilator of $\tilde Q^{*}$, because $\tilde Q\tilde X=0$ or $\tilde X\tilde Q^{*}=0$ implies $\tilde Q\tilde X\tilde Q^{*}=0$, and it is strictly larger than each of them.

When $\tilde\Pi$ is Hermitian, the Peirce form is diagonal in the eigenbasis $(\tilde\Pi,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi')$:

$$
\boxed{\;
\mathsf M\bigl(\Theta_{\tilde Q}\bigr)
=\operatorname{diag}\bigl(\lvert c\rvert^{2},0,0,0\bigr).
\;}
$$

Only the $(+,+)$ corner survives; the kernel is the sum of the other three corners. When $\tilde\Pi$ is not Hermitian, the matrix is not diagonal in that basis, but the spectrum and the rank are the same. The image is still the line $\mathbb{C}P$, and the kernel is still the hyperplane above.

### Eigenvalues and singular values

The eigenvalue of $\Theta_{\tilde Q}$ on its image is $\lvert c\rvert^{2}$. Its non-zero singular value is $4a^{2}$: indeed

$$
\Theta_{\tilde Q}\Theta_{\tilde Q}^{*}
=\Theta_{\tilde Q\tilde Q^{*}}
=\Theta_{4a^{2}P}
=(4a^{2})^{2}\Theta_P,
$$

and $\Theta_P$ is an orthogonal projection of rank one, with singular value one. Hence the singular value is $4a^{2}$. The ratio is

$$
\frac{\lvert c\rvert^{2}}{4a^{2}}
=\lvert v^{\dagger}u\rvert^{2}
=\cos^{2}\theta .
$$

This ratio is one exactly when $\tilde\Pi$ is Hermitian ($\kappa=1$, the slots coincide), and it lies strictly between $0$ and $1$ for a non-Hermitian idempotent. It vanishes at the wall $\Sigma_{00}$. The distinction between eigenvalue and singular value is the measure of the obliqueness of the projection.

The idempotent $\Theta_{\tilde\Pi}$ itself has singular value $\kappa$, because

$$
\Theta_{\tilde\Pi}\Theta_{\tilde\Pi}^{*}
=\Theta_{\tilde\Pi\tilde\Pi^{*}}
=\Theta_{\kappa P}
=\kappa^{2}\Theta_P .
$$

Thus $\Theta_{\tilde Q}=\lvert c\rvert^{2}\Theta_{\tilde\Pi}$ has singular value $\lvert c\rvert^{2}\kappa=4a^{2}$. The operator $\Theta_{\tilde Q}$ is not a partial isometry in general: its singular value is $4a^{2}$, not one. It is $4a^{2}$ times the partial isometry $\Theta_{\tilde Q_0}$.

## The Polar Decomposition of the Sandwich

### The scalar collapse

By the polar pair theorem, $\tilde Q=2a\tilde Q_0$ and $\tilde Q_0$ is a partial isometry. The multiplicativity of $\Theta$ gives

$$
\Theta_{\tilde Q}
=\Theta_{2a\tilde Q_0}
=4a^{2}\Theta_{\tilde Q_0}.
$$

This is the scalar collapse. The canonical left polar factor of $\Theta_{\tilde Q}$ is

$$
\lvert\Theta_{\tilde Q}\rvert
=\bigl(\Theta_{\tilde Q}\Theta_{\tilde Q}^{*}\bigr)^{1/2}
=\Theta_{\tilde Q_H}
=4a^{2}\Theta_P,
$$

which is positive semidefinite of rank one. On the image of $\Theta_{\tilde Q_0}$ it acts as the scalar $4a^{2}$, because $P\tilde Q_0=\tilde Q_0$ and therefore $\Theta_P\Theta_{\tilde Q_0}=\Theta_{\tilde Q_0}$. Hence

$$
\boxed{\;
\Theta_{\tilde Q}
=\Theta_{\tilde Q_H}\circ\Theta_{\tilde Q_0}
=4a^{2}\Theta_{\tilde Q_0},
\qquad
\Theta_{\tilde Q_0}\Theta_{\tilde Q_0}^{*}\Theta_{\tilde Q_0}
=\Theta_{\tilde Q_0}.
\;}
$$

The sandwich is $4a^{2}$ times a partial isometry. Its non-zero singular value is $4a^{2}$, the square of the one-sided singular value $2a$. Its eigenvalue is $\lvert c\rvert^{2}=4a^{2}\cos^{2}\theta$, the squared overlap of the two slots.

### The phase

The partial-isometry factor is $\tilde Q_0=(c/\lvert c\rvert)\tilde\Pi/\sqrt{\kappa}$. Since $\Theta$ is quadratic in $\tilde Q_0$ and $\tilde Q_0^{*}$,

$$
\Theta_{\tilde Q_0}
=\Theta_{\tilde\Pi}/\kappa,
$$

independent of the phase of $c$. The sandwich therefore cancels the phase:

$$
\Theta_{\tilde Q}
=\lvert c\rvert^{2}\Theta_{\tilde\Pi}
=4a^{2}\Theta_{\tilde Q_0}.
$$

The one-sided operator of the companion article keeps the phase in its eigenvalue $c$; the sandwich keeps only the modulus $\lvert c\rvert^{2}$ and the Hermitian projection $P$. When $\tilde\Pi$ is Hermitian and $c=r e^{i\alpha}$, the polar pair is $\tilde Q_H=r\tilde\Pi$ and $\tilde Q_0=e^{i\alpha}\tilde\Pi$, and the sandwich is $r^{2}\Theta_{\tilde\Pi}$: the phase has cancelled between $\tilde Q_0$ and $\tilde Q_0^{*}$.

### The polar pair of the element and of the operator

The element pair is $(\tilde Q_H,\tilde Q_0)$, with $\tilde Q_H=2aP$ and $\tilde Q_0$ a partial isometry. The operator pair is $(\Theta_{\tilde Q_H},\Theta_{\tilde Q_0})$, with $\Theta_{\tilde Q_H}=4a^{2}\Theta_P$ positive and $\Theta_{\tilde Q_0}$ a partial isometry. The element pair is a rank-one singular value decomposition; the operator pair is its congruence. The scalar $4a^{2}$ is the square of the element's singular value $2a$, and the phase of the element is absent from the operator pair.

## The Two Slots

### The Peirce picture

On $\Sigma_{01}$ the eigenbasis exists because $B^{2}\neq0$. Its spectral projectors are $\tilde\Pi$ and $\tilde\Pi'$, and the four Peirce corners are one-dimensional. For a Hermitian $\tilde\Pi$, the sandwich is the projection onto the $(+,+)$ corner:

$$
\Theta_{\tilde\Pi}(\tilde\Pi)=\tilde\Pi,
\qquad
\Theta_{\tilde\Pi}(\vec\Upsilon_-)=0,
\qquad
\Theta_{\tilde\Pi}(\vec\Upsilon_+)=0,
\qquad
\Theta_{\tilde\Pi}(\tilde\Pi')=0.
$$

Thus the matrix is $\operatorname{diag}(1,0,0,0)$, and $\Theta_{\tilde Q}$ is $\operatorname{diag}(\lvert c\rvert^{2},0,0,0)$. The kernel is the sum of the three other corners. The sandwich pairs the two half-spins of the regular theory; on $\Sigma_{01}$ one half has eigenvalue zero, so only the $(+,+)$ pairing survives. The four eigenvalue products are

$$
c\bar c,\quad c\cdot0,\quad 0\cdot\bar c,\quad 0\cdot0,
$$

that is, $\lvert c\rvert^{2},0,0,0$. The "full spin" of the regular sandwich has no angle or rapidity here: the element is not a unit, and the sandwich is not a conformal Lorentz transformation. It is an oblique projection onto a null line.

For a non-Hermitian $\tilde\Pi$ the eigenbasis still exists, but the sandwich is not diagonal in it. The invariant statement is the spectrum: the four products are still $\lvert c\rvert^{2},0,0,0$, and the image is still the null line $\mathbb{C}P$, with $P=\tilde\Pi\tilde\Pi^{*}/\kappa\neq\tilde\Pi$.

### The singular-vector picture

In the matrix model the two slots are the singular vectors $u$ and $v$. The sandwich is

$$
\Theta_{\tilde Q}(\tilde X)
=4a^{2}\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)u u^{\dagger}.
$$

It reads the $v$-slot of $\tilde X$ through the scalar $v^{\dagger}\mathsf M_2(\tilde X)v$ and writes it on the $u$-slot. The relative phase of $u$ and $v$ cancels, because the sandwich uses $u$ and $u^{\dagger}$ on the outside and $v$ and $v^{\dagger}$ on the inside. The eigenvalue is $4a^{2}\lvert v^{\dagger}u\rvert^{2}=\lvert c\rvert^{2}$; the singular value is $4a^{2}$. The two slots are not orthogonal on $\Sigma_{01}$: their overlap has modulus $\cos\theta=1/\sqrt{\kappa}$. At the wall $\Sigma_{00}$ the overlap vanishes, the slots are orthogonal, and the sandwich becomes nilpotent.

This is the precise form of the two-slot structure of the regular sandwich. In the regular sector the two slots are the two chiralities, and the sandwich carries the full angle and rapidity as the product of the two half-factors. On the null cone the two slots are the singular vectors of the rank-one element, and the sandwich carries only the squared overlap $\cos^{2}\theta$. The angle between the slots replaces the angle of the Lorentz transformation.

## The Exponential

**The operator exponential.** Since $\Theta_{\tilde Q}=\lvert c\rvert^{2}\Theta_{\tilde\Pi}$ and $\Theta_{\tilde\Pi}^{2}=\Theta_{\tilde\Pi}$,

$$
\boxed{\;
\exp\bigl(t\Theta_{\tilde Q}\bigr)
=I+\bigl(e^{t\lvert c\rvert^{2}}-1\bigr)\Theta_{\tilde\Pi}
\;}
$$

for every complex $t$. The eigenvalues are $e^{t\lvert c\rvert^{2}}$ and $1$ (three times); the determinant is $e^{t\lvert c\rvert^{2}}$. The group is invertible for every $t$, although the generator $\Theta_{\tilde Q}$ is singular. It dilates the image line and fixes the kernel hyperplane.

**The element flow.** The exponential $\exp(t\tilde Q)=e_t+(e^{tc}-1)\tilde\Pi$ is a unit for every $t$, and it lies in $\Sigma_{11}$ for generic $t\neq0$; at the exceptional values $e^{tc}=1$ it is $e_t$ on the wall $\Sigma_{10}$. Its sandwich $\Theta_{\exp(t\tilde Q)}$ is therefore a conformal Lorentz transformation, with the generator $\Theta_{\tilde Q}$:

$$
\Theta_{\exp(t\tilde Q)}
=\exp\bigl(t\Theta_{\tilde Q}\bigr).
$$

The generator is singular, but the one-parameter group it generates is invertible. The one-sided rate is $c$; the two-sided rate is $\lvert c\rvert^{2}$, the squared modulus. The generator is now an oblique projection rather than a conformal Lorentz transformation.

## Worked Examples

### Example 1: a Hermitian idempotent

Take $\tilde Q=e_t+i\vec e_x$. Then $c=2$, $\tilde\Pi=(e_t+i\vec e_x)/2$, $\kappa=1$, $a=1$, $P=\tilde\Pi$, and $\tilde Q_H=\tilde Q$, $\tilde Q_0=\tilde\Pi$. The sandwich is $\Theta_{\tilde Q}=4\Theta_{\tilde\Pi}$, with rank one, eigenvalue $4$, singular value $4$, and image the line $\mathbb{C}\tilde Q$. In the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$,

$$
\mathsf M\bigl(\Theta_{\tilde Q}\bigr)=
\begin{pmatrix}
2&-2i&0&0\\
2i&2&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
$$

with trace $4$, rank one and square $\Theta_{\tilde Q}^{2}=4\Theta_{\tilde Q}$. The exponential is

$$
\exp\bigl(t\Theta_{\tilde Q}\bigr)=I+\bigl(e^{4t}-1\bigr)\Theta_{\tilde\Pi}.
$$

### Example 2: a non-Hermitian idempotent

Take $\tilde Q=e_t+\vec e_x+i\sqrt2\,\vec e_z$. Then $c=2$, $\kappa=2$, $a=\sqrt2$, $\tilde\Xi=\vec e_x+i\sqrt2\,\vec e_z$, and

$$
P=\frac12 e_t-\frac{i\sqrt2}{4}\vec e_y+\frac{i\sqrt2}{4}\vec e_z,
\qquad
\tilde Q_H=\sqrt2\,e_t-i\vec e_y+i\vec e_z,
\qquad
\tilde Q_0=\frac{\sqrt2}{4}e_t+\frac{\sqrt2}{4}\vec e_x+\frac{i}{2}\vec e_z .
$$

The sandwich is $\Theta_{\tilde Q}=4\Theta_{\tilde\Pi}$, with rank one, eigenvalue $4$, and singular value $8$. The eigenvalue-to-singular-value ratio is $\tfrac12=\cos^{2}\theta$, because $\cos\theta=1/\sqrt2$. The image is the null line $\mathbb{C}P$, with $P\neq\tilde\Pi$; the sandwich is not self-adjoint, and its Peirce matrix in the spectral basis is not diagonal. The example shows the difference between the eigenvalue $\lvert c\rvert^{2}$ and the singular value $4a^{2}$ for an oblique idempotent.

## Summary

### Main Results

| item | value |
|---|---|
| sector | $\Sigma_{01}=\{\langle\tilde Q\rangle_{\natural}=0,\ B^{2}\neq0\}$ |
| parameter | $\tilde Q=c\tilde\Pi$, $c=2Q_t\neq0$ |
| sandwich | $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ |
| closed form | $\Theta_{\tilde Q}=\lvert c\rvert^{2}\Theta_{\tilde\Pi}$, $\Theta_{\tilde\Pi}^{2}=\Theta_{\tilde\Pi}$ |
| square | $\Theta_{\tilde Q}^{2}=\lvert c\rvert^{2}\Theta_{\tilde Q}$ |
| rank | $1$ |
| spectrum | $\{\lvert c\rvert^{2},0\}$, multiplicities $1,3$ |
| Jordan form | diagonal, $\operatorname{diag}(\lvert c\rvert^{2},0,0,0)$; the eigenbasis of $\tilde Q$ diagonalizes it only when $\tilde\Pi$ is Hermitian |
| trace | $\lvert c\rvert^{2}=4a^{2}\cos^{2}\theta$ |
| determinant | $0$ |
| eigenvalue on the image | $\lvert c\rvert^{2}$ |
| singular value | $4a^{2}$ |
| image | the null line $\mathbb{C}P$, $P=\tilde Q\tilde Q^{*}/(4a^{2})$ |
| kernel | $\{\tilde X:\tilde\Pi\tilde X\tilde\Pi^{*}=0\}$, a hyperplane |
| scalar collapse | $\Theta_{\tilde Q}=4a^{2}\Theta_{\tilde Q_0}$ |
| exponential | $\exp(t\Theta_{\tilde Q})=I+(e^{t\lvert c\rvert^{2}}-1)\Theta_{\tilde\Pi}$ |
| element flow | $\exp(t\tilde Q)=e_t+(e^{tc}-1)\tilde\Pi$, a unit in $\Sigma_{11}$ for generic $t\neq0$ |

### What the Sandwich Shows

- The norm degeneration fixes the rank: the sandwich has rank one and its image is a null line.
- The spectral regularity fixes the Jordan type: the sandwich is an oblique projection up to scale, not a nilpotent.
- The polar pair collapses: $\Theta_{\tilde Q}=4a^{2}\Theta_{\tilde Q_0}$, with $\Theta_{\tilde Q_0}$ a partial isometry; the positive factor acts as the scalar $4a^{2}$ on the image.
- The non-zero singular value is $4a^{2}=(2a)^{2}$, the square of the one-sided singular value; the eigenvalue is $\lvert c\rvert^{2}=4a^{2}\cos^{2}\theta$.
- The phase is cancelled; the sandwich sees only $\lvert c\rvert^{2}$ and the Hermitian projection $P$.
- The two slots are the singular vectors $u$ and $v$; their overlap $\cos\theta=1/\sqrt{\kappa}$ determines the eigenvalue-to-singular-value ratio, and it vanishes at the wall $\Sigma_{00}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q=c\tilde\Pi$ | an element of $\Sigma_{01}$ |
| $\Theta_{\tilde Q}$ | the sandwich $\tilde X\mapsto\tilde Q\tilde X\tilde Q^{*}$ |
| $\kappa=2\langle\tilde\Pi\rangle_{*}$ | the obliqueness, $\kappa\ge1$ |
| $a=\sqrt{\langle\tilde Q\rangle_{*}/2}$ | the half singular value, $2a$ the non-zero singular value |
| $P=\tilde Q\tilde Q^{*}/(4a^{2})$ | the rank-one Hermitian idempotent and the image line |
| $\tilde Q_H=2aP$ | the Hermitian factor |
| $\tilde Q_0=\tilde Q/(2a)$ | the partial-isometry factor |
| $u,v$ | the left and right singular vectors |
| $v^{\dagger}u=Q_t/a$ | the overlap, modulus $1/\sqrt{\kappa}$ |
| $\theta$ | the angle between the slots, $\cos\theta=1/\sqrt{\kappa}$ |

## Further Reading

- [The Two-Sided Operator of a N-Regular, Spectrally Regular Biquaternion](the-two-sided-operator-of-a-n-regular-spectrally-regular-biquaternion.html), for the general sandwich and the conformal Lorentz action.
- [The Two-Sided Operator of a N-Regular, Spectrally Degenerate Biquaternion](the-two-sided-operator-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the unipotent three-plus-one sandwich at the spectral wall of the regular sector.
- [The One-Sided Operators of a N-Degenerate, Spectrally Regular Biquaternion](the-one-sided-operators-of-a-n-degenerate-spectrally-regular-biquaternion.html), for the companion one-sided operator and the phase.
- [The Two-Sided Operator of a N-Degenerate, Spectrally Degenerate Biquaternion](the-two-sided-operator-of-a-n-degenerate-spectrally-degenerate-biquaternion.html), for the nilpotent sandwich of the same sector pair.
- [The Polar Decomposition of a N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the general two-factor pair on the null cone.
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the sector, the spinors and the eigenbasis.
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the wall $B^{2}=0$ and the canonical Jordan pair.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the null cone and the quaternionic norm.
