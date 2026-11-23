# __Two-Sided Operators on the N-Degenerate Sector__

## Introduction

**The two projectors of the algebra.** Two endomorphisms of $\mathbb{B}$ are not of the polar family and are worth naming at the start, because they act on every sector: $P_{0}=\tfrac12(\mathrm{id}+\natural)$ and $P_{1}=\tfrac12(\mathrm{id}-\natural)$, with $P_{0}^{2}=P_{0}$, $P_{1}^{2}=P_{1}$, $P_{0}P_{1}=0$ and $P_{0}+P_{1}=\mathrm{id}$. Their images are the centre $\mathbb{C}e_t$ and the complexified vector part $\mathbb{C}\mathfrak{k}$, the two summands of the Clebsch–Gordan series $V_{1/2}\otimes V_{1/2}=V_{1}\oplus V_{0}$ of the algebra. They are canonical, they carry no parameter, and nothing in this article depends on them; they are named here because they are the only two idempotent endomorphisms that come with the algebra itself. The decomposition is *The Clebsch–Gordan Decomposition of the Biquaternion Algebra*.

This article treats the two-sided operator, the Hermitian pair $\mathrm{Sd}_{\tilde Q}$, on the **null cone** $N=\langle\tilde Q\rangle_{\natural}=0$, the closed set of real codimension two. It is the two-sided companion of *One-Sided Operators on the N-Degenerate Sector*, the same polar pair read on two sides.

The two-sided operator is the Hermitian congruence

$$
\mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}.
$$

**What the norm decides, and what the vector form decides.** The norm decides the collapse: on the whole null cone the operator has rank one, its image is a single null line, and its kernel has dimension three. Nothing about that changes inside the sector. The second condition $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ decides the **spectrum and the Jordan type**: on $\Sigma_{01}$ the operator has the eigenvalue $\lvert c\rvert^{2}=4a^{2}\cos^{2}\theta$ and is a projection up to scale, and on $\Sigma_{00}$ the operator is square-zero, with the single eigenvalue zero, one Jordan block of size two and two further zero directions.

The polar pair of *The Polar Decomposition of an N-Degenerate Biquaternion* survives on both strata,

$$
\tilde Q=\tilde Q_H\tilde Q_0,
\qquad
\tilde Q_H=\bigl(\tilde Q\tilde Q^{*}\bigr)^{1/2},
\qquad
\tilde Q_0=\tilde Q_H^{+}\tilde Q,
$$

with $\tilde Q_H$ Hermitian positive semidefinite of rank one and $\tilde Q_0$ a partial isometry. The main result is the scalar collapse of the operator,

$$
\mathrm{Sd}_{\tilde Q}=4a^{2}\,\mathrm{Sd}_{\tilde Q_0},
$$

with $4a^{2}=(2a)^{2}$ the square of the one-sided singular value. On $\Sigma_{00}$ the partial isometry is itself nilpotent, $\tilde Q_0^{2}=0$, so the operator is $4a^{2}$ times a nilpotent partial isometry. On $\Sigma_{01}$ the partial isometry is a scalar times an idempotent, and the operator is $4a^{2}$ times a projection.

The plan is the following. §*The Polar Pair* describes the polar pair on both strata. §*The Two-Sided Operator* computes the composition, the closed form, the image, the eigenvalues and the Jordan data. §*The Polar Decomposition of the Two-Sided Operator* proves the scalar collapse and reads the phase. §*The Two Slots* reads the operator through the Peirce corners and through the singular vectors. §*The Exponential* computes the one-parameter group. §*Worked Examples* treats a Hermitian idempotent, a non-Hermitian idempotent, the standard nilpotent and a complex scalar multiple.
## The Polar Pair

On the null cone the spectral decomposition fails and the polar pair survives. The two strata differ in what the partial isometry is: a scalar times an idempotent on $\Sigma_{01}$, a nilpotent on $\Sigma_{00}$. The positive factor is a rank-one Hermitian projection scaled by $2a$ in both cases.

The conventions, including the two forms, are those of the companion article.

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
P=\frac{\tilde\Pi_{\mathrm{id}}\tilde\Pi_{\mathrm{id}}^{*}}{\kappa},
\qquad
\tilde Q_0=\frac{c}{\lvert c\rvert}\frac{\tilde\Pi_{\mathrm{id}}}{\sqrt{\kappa}},
\qquad
\kappa=\frac{1+\lVert\tilde{Ζ}\rVert^{2}}{2},
$$

where $\tilde{Ζ}=2\tilde\Pi_{\mathrm{id}}-e_t$ and $\kappa\ge1$. The overlap is $v^{\dagger}u=Q_t/a=c/(2a)$, with modulus $1/\sqrt{\kappa}=\cos\theta$, where $\theta$ is the angle between the two slots.

The two-sided operator of the pair is computed in the matrix model. For any $\tilde X$,

$$
\mathsf M_2\bigl(\mathrm{Sd}_{\tilde Q}(\tilde X)\bigr)
=(2a)^{2}u v^{\dagger}\,\mathsf M_2(\tilde X)\,v u^{\dagger}
=4a^{2}\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)u u^{\dagger}.
$$

Thus the image is the line $\mathbb{C}u u^{\dagger}=\mathbb{C}P$ and the value is the scalar $v^{\dagger}\mathsf M_2(\tilde X)v$. This formula is the source of every result below.

### The canonical Hermitian pair

Let $\tilde\pi_{\mathrm{nil}}=\vec A+i\vec B$ with $\vec A,\vec B$ real, orthogonal and of equal norm $a>0$. Put

$$
\vec c=\frac{\vec A\times\vec B}{a^{2}},
\qquad
\tilde\Pi_{\mathrm{id},+}=\frac{e_t+i\vec c}{2},
\qquad
\tilde\Pi_{\mathrm{id},-}=\frac{e_t-i\vec c}{2}.
$$

The vector $\vec c$ is real and unit; the idempotents are Hermitian and complementary. They satisfy

$$
\tilde\Pi_{\mathrm{id},+}\tilde\pi_{\mathrm{nil}}=\tilde\pi_{\mathrm{nil}},
\qquad
\tilde\pi_{\mathrm{nil}}\tilde\Pi_{\mathrm{id},+}=0,
\qquad
\tilde\Pi_{\mathrm{id},-}\tilde\pi_{\mathrm{nil}}=0,
\qquad
\tilde\pi_{\mathrm{nil}}\tilde\Pi_{\mathrm{id},-}=\tilde\pi_{\mathrm{nil}},
$$

so $\tilde\pi_{\mathrm{nil}}=\tilde\Pi_{\mathrm{id},+}\tilde\pi_{\mathrm{nil}}\tilde\Pi_{\mathrm{id},-}$ lies in the mixed corner $\mathbb{B}_{+-}$. The element is annihilated by the two products that would place it in a diagonal corner. Its norms are

$$
\langle\tilde\pi_{\mathrm{nil}}\rangle_{\natural}=0,
\qquad
\langle\tilde\pi_{\mathrm{nil}}\rangle_{*}=2a^{2},
\qquad
\tilde\pi_{\mathrm{nil}}\tilde\pi_{\mathrm{nil}}^{*}=4a^{2}\tilde\Pi_{\mathrm{id},+},
\qquad
\tilde\pi_{\mathrm{nil}}^{*}\tilde\pi_{\mathrm{nil}}=4a^{2}\tilde\Pi_{\mathrm{id},-} .
$$

### The polar pair on the nilpotents

The polar pair is

$$
\boxed{\;
P=\tilde\Pi_{\mathrm{id},+},
\qquad
\tilde Q_H=2a\tilde\Pi_{\mathrm{id},+},
\qquad
\tilde Q_0=\frac{\tilde\pi_{\mathrm{nil}}}{2a},
\qquad
\tilde Q=\tilde Q_H\tilde Q_0,
\qquad
\tilde Q_0^{2}=0 .
\;}
$$

The Hermitian factor is positive semidefinite of rank one, with spectrum $\{0,2a\}$. The partial-isometry factor is nilpotent:

$$
\tilde Q_0\tilde Q_0^{*}=\tilde\Pi_{\mathrm{id},+},
\qquad
\tilde Q_0^{*}\tilde Q_0=\tilde\Pi_{\mathrm{id},-},
\qquad
\tilde Q_0\tilde Q_0^{*}\tilde Q_0=\tilde Q_0,
\qquad
\tilde Q_0^{2}=0 .
$$

The polar pair is the rank-one singular value decomposition of the nilpotent. The "$*$-unitary" factor is a nilpotent partial isometry, not a $*$-unitary; the pair is still the general pair of *The Polar Decomposition of an N-Degenerate Biquaternion*, but it is as far as possible from the modulus–unit form.

### The matrix model

In the matrix model $\mathsf M_2(\tilde\pi_{\mathrm{nil}})=2a\,u v^{\dagger}$ with $u,v$ unit and orthogonal:

$$
v^{\dagger}u=\frac{Q_t}{a}=0,
\qquad
u^{\dagger}u=v^{\dagger}v=1,
\qquad
u\perp v .
$$

The polar factors are

$$
P=u u^{\dagger}=\tilde\Pi_{\mathrm{id},+},
\qquad
\tilde Q_H=2a\,u u^{\dagger},
\qquad
\tilde Q_0=u v^{\dagger},
\qquad
\tilde Q_0^{*}=v u^{\dagger},
\qquad
\tilde Q_0^{2}=u(v^{\dagger}u)v^{\dagger}=0 .
$$

The two slots are orthogonal. The overlap $v^{\dagger}u$ vanishes; this is the matrix form of the spectral degeneration. The two-sided operator is computed from the same decomposition:

$$
\mathsf M_2\bigl(\mathrm{Sd}_{\tilde Q}(\tilde X)\bigr)
=(2a)^{2}u v^{\dagger}\mathsf M_2(\tilde X)v u^{\dagger}
=4a^{2}\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)u u^{\dagger}.
$$

Because $v^{\dagger}u=0$, applying the operator twice gives zero. The single chain is visible in the formula: the scalar $v^{\dagger}\mathsf M_2(\tilde X)v$ is written on the line $u u^{\dagger}$, and the line is annihilated on the next step.

## The Two-Sided Operator

The composition and the rank are fixed by the norm; the closed form, the spectrum and the Jordan data are fixed by $B^{2}$. Both strata share the rank one and the single null image line.

### Elementary properties on the idempotent multiples

**Proposition.** Let $\tilde Q,\tilde Q'\in\mathbb{B}$. Then:

**(a)** $\mathrm{Sd}_{\tilde Q}$ is $\mathbb{C}$-linear;

**(b)** $\mathrm{Sd}_{\tilde Q\tilde Q'}=\mathrm{Sd}_{\tilde Q}\circ\mathrm{Sd}_{\tilde Q'}$;

**(c)** $\mathrm{Sd}_{\tilde Q}$ is invertible exactly when $\tilde Q$ is invertible, with inverse $\mathrm{Sd}_{\tilde Q^{-1}}$;

**(d)** $\mathrm{Sd}_{\tilde Q}$ preserves the real forms $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$;

**(e)** the adjoint is $\mathrm{Sd}_{\tilde Q}^{*}=\mathrm{Sd}_{\tilde Q^{*}}$;

**(f)** the norm scales as

$$
\bigl\langle\mathrm{Sd}_{\tilde Q}(\tilde X)\bigr\rangle_{\natural}
=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}.
$$

On $\Sigma_{01}$ the element is a zero divisor, so $\mathrm{Sd}_{\tilde Q}$ is not invertible. The properties are those of *Operators of the Polar Word: The Common Framework*; the sector changes the values.

### The closed form on the idempotent multiples

Let $\tilde Q=c\tilde\Pi_{\mathrm{id}}$. Since $\tilde\Pi_{\mathrm{id}}^{2}=\tilde\Pi_{\mathrm{id}}$,

$$
\mathrm{Sd}_{\tilde Q}
=\lvert c\rvert^{2}\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}},
\qquad
\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}^{2}
=\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}},
\qquad
\mathrm{Sd}_{\tilde Q}^{2}
=\lvert c\rvert^{2}\mathrm{Sd}_{\tilde Q}.
$$

Thus $\mathrm{Sd}_{\tilde Q}/\lvert c\rvert^{2}$ is an idempotent of the operator space, and $\mathrm{Sd}_{\tilde Q}$ is an idempotent up to scale. It is not an orthogonal projection unless $\tilde\Pi_{\mathrm{id}}$ is Hermitian.

**Theorem (rank, spectrum and Jordan form).** On $\Sigma_{01}$:

**(a)** $\mathrm{Sd}_{\tilde Q}$ has complex rank $1$;

**(b)** its spectrum is $\{\lvert c\rvert^{2},0\}$, with algebraic multiplicities $1$ and $3$, and geometric multiplicities $1$ and $3$;

**(c)** it is diagonalizable, with minimal polynomial $X(X-\lvert c\rvert^{2})$;

**(d)** $\operatorname{tr}\mathrm{Sd}_{\tilde Q}=\lvert c\rvert^{2}=4a^{2}\cos^{2}\theta$ and $\det\mathrm{Sd}_{\tilde Q}=0$;

**(e)** for every $\tilde X$, $\langle\mathrm{Sd}_{\tilde Q}(\tilde X)\rangle_{\natural}=0$; the image lies on the null cone.

*Proof.* In the matrix model, the formula above gives

$$
\mathrm{Sd}_{\tilde Q}(\tilde X)=4a^{2}\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)u u^{\dagger}.
$$

The image is contained in the line $\mathbb{C}u u^{\dagger}$, and it is non-zero because $u u^{\dagger}$ is in the image: take $\tilde X$ with $\mathsf M_2(\tilde X)=u u^{\dagger}$; then $v^{\dagger}u u^{\dagger}v=\lvert v^{\dagger}u\rvert^{2}\neq0$. Hence the rank is one. The square is

$$
\mathrm{Sd}_{\tilde Q}^{2}
=(4a^{2})^{2}\lvert v^{\dagger}u\rvert^{2}
\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)u u^{\dagger}
=\lvert c\rvert^{2}\mathrm{Sd}_{\tilde Q},
$$

because $c=2a\,v^{\dagger}u$. The operator is a non-zero scalar multiple of an idempotent, so it is diagonalizable with eigenvalues $\lvert c\rvert^{2}$ and $0$. The trace is $\lvert c\rvert^{2}$ and the determinant is zero. The norm is $\langle\mathrm{Sd}_{\tilde Q}(\tilde X)\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}=0$.
The image is a null line because $\langle\tilde Q\tilde X\tilde Q^{*}\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}=0$.

### The image and the kernel

The image is the line

$$
\operatorname{im}\mathrm{Sd}_{\tilde Q}=\mathbb{C}P,
\qquad
P=\frac{\tilde Q\tilde Q^{*}}{4a^{2}}=\frac{\tilde\Pi_{\mathrm{id}}\tilde\Pi_{\mathrm{id}}^{*}}{\kappa}.
$$

The line is null: $\langle P\rangle_{\natural}=0$ because $P$ is a non-trivial idempotent. The kernel is the hyperplane

$$
\ker\mathrm{Sd}_{\tilde Q}
=\bigl\{\tilde X:\tilde\Pi_{\mathrm{id}}\tilde X\tilde\Pi_{\mathrm{id}}^{*}=0\bigr\},
\qquad
\dim_{\mathbb{C}}\ker\mathrm{Sd}_{\tilde Q}=3.
$$

In the matrix model it is $\{X:v^{\dagger}Xv=0\}$, the hyperplane orthogonal to the rank-one functional $X\mapsto v^{\dagger}Xv$. The kernel contains the right annihilator $A(\tilde Q)=\ker L_{\tilde Q}$ and the left annihilator of $\tilde Q^{*}$, because $\tilde Q\tilde X=0$ or $\tilde X\tilde Q^{*}=0$ implies $\tilde Q\tilde X\tilde Q^{*}=0$, and it is strictly larger than each of them.

When $\tilde\Pi_{\mathrm{id}}$ is Hermitian, the Peirce form is diagonal in the eigenbasis $(\tilde\Pi_{\mathrm{id}},\vec\Pi_{\mathrm{nil},-},\vec\Pi_{\mathrm{nil},+},\tilde\Pi_{\mathrm{id}}')$:

$$
\boxed{\;
\mathsf M\bigl(\mathrm{Sd}_{\tilde Q}\bigr)
=\operatorname{diag}\bigl(\lvert c\rvert^{2},0,0,0\bigr).
\;}
$$

Only the $(+,+)$ corner survives; the kernel is the sum of the other three corners. When $\tilde\Pi_{\mathrm{id}}$ is not Hermitian, the matrix is not diagonal in that basis, but the spectrum and the rank are the same. The image is still the line $\mathbb{C}P$, and the kernel is still the hyperplane above.

### Eigenvalues and singular values

The eigenvalue of $\mathrm{Sd}_{\tilde Q}$ on its image is $\lvert c\rvert^{2}$. Its non-zero singular value is $4a^{2}$: indeed

$$
\mathrm{Sd}_{\tilde Q}\mathrm{Sd}_{\tilde Q}^{*}
=\mathrm{Sd}_{\tilde Q\tilde Q^{*}}
=\mathrm{Sd}_{4a^{2}P}
=(4a^{2})^{2}\mathrm{Sd}_P,
$$

and $\mathrm{Sd}_P$ is an orthogonal projection of rank one, with singular value one. Hence the singular value is $4a^{2}$. The ratio is

$$
\frac{\lvert c\rvert^{2}}{4a^{2}}
=\lvert v^{\dagger}u\rvert^{2}
=\cos^{2}\theta .
$$

This ratio is one exactly when $\tilde\Pi_{\mathrm{id}}$ is Hermitian ($\kappa=1$, the slots coincide), and it lies strictly between $0$ and $1$ for a non-Hermitian idempotent. It vanishes at the wall $\Sigma_{00}$. The distinction between eigenvalue and singular value is the measure of the obliqueness of the projection.

The idempotent $\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}$ itself has singular value $\kappa$, because

$$
\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}^{*}
=\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}\tilde\Pi_{\mathrm{id}}^{*}}
=\mathrm{Sd}_{\kappa P}
=\kappa^{2}\mathrm{Sd}_P .
$$

Thus $\mathrm{Sd}_{\tilde Q}=\lvert c\rvert^{2}\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}$ has singular value $\lvert c\rvert^{2}\kappa=4a^{2}$. The operator $\mathrm{Sd}_{\tilde Q}$ is not a partial isometry in general: its singular value is $4a^{2}$, not one. It is $4a^{2}$ times the partial isometry $\mathrm{Sd}_{\tilde Q_0}$.

### The square, the rank and the spectrum

**Theorem.** On $\Sigma_{00}$:

**(a)** $\mathrm{Sd}_{\tilde Q}^{2}=0$;

**(b)** $\mathrm{Sd}_{\tilde Q}$ has complex rank $1$;

**(c)** its only eigenvalue is $0$, with algebraic multiplicity $4$ and geometric multiplicity $3$;

**(d)** its Jordan form is $J_2(0)\oplus0\oplus0$, with minimal polynomial $X^{2}$;

**(e)** $\operatorname{tr}\mathrm{Sd}_{\tilde Q}=0$ and $\det\mathrm{Sd}_{\tilde Q}=0$;

**(f)** for every $\tilde X$, $\langle\mathrm{Sd}_{\tilde Q}(\tilde X)\rangle_{\natural}=0$; the image lies on the null cone.

*Proof.* In the matrix model,

$$
\mathrm{Sd}_{\tilde Q}(\tilde X)
=4a^{2}\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)u u^{\dagger}.
$$

The image is contained in the line $\mathbb{C}u u^{\dagger}$, and it is non-zero because $\mathrm{Sd}_{\tilde Q}(e_t)=\tilde\pi_{\mathrm{nil}}\tilde\pi_{\mathrm{nil}}^{*}=4a^{2}\tilde\Pi_{\mathrm{id},+}$. Hence the rank is one. Applying the formula twice,

$$
\mathrm{Sd}_{\tilde Q}^{2}(\tilde X)
=(4a^{2})^{2}\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)
(v^{\dagger}u)(u^{\dagger}v)u u^{\dagger}=0,
$$

because $v^{\dagger}u=0$. The only eigenvalue of a square-zero operator is zero; the algebraic multiplicity is four, the geometric multiplicity is the dimension of the kernel, three; the Jordan form is one block of size two and two blocks of size one. The trace is zero and the determinant is zero. The norm is $\langle\mathrm{Sd}_{\tilde Q}(\tilde X)\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}=0$.
The image is a null line because $\langle\tilde Q\tilde X\tilde Q^{*}\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}=0$.

### The image and the kernel on the nilpotents

The image is the null line

$$
\operatorname{im}\mathrm{Sd}_{\tilde Q}
=\mathbb{C}\tilde\Pi_{\mathrm{id},+},
\qquad
\tilde\Pi_{\mathrm{id},+}=\frac{\tilde Q\tilde Q^{*}}{4a^{2}}.
$$

The kernel is the hyperplane

$$
\ker\mathrm{Sd}_{\tilde Q}
=\bigl\{\tilde X:\tilde\pi_{\mathrm{nil}}\tilde X\tilde\pi_{\mathrm{nil}}^{*}=0\bigr\},
\qquad
\dim_{\mathbb{C}}\ker\mathrm{Sd}_{\tilde Q}=3.
$$

In the matrix model it is $\{X:v^{\dagger}Xv=0\}$. The kernel contains the right annihilator $A(\tilde\pi_{\mathrm{nil}})=\ker L_{\tilde\pi_{\mathrm{nil}}}$ and the left annihilator of $\tilde\pi_{\mathrm{nil}}^{*}$, because $\tilde\pi_{\mathrm{nil}}\tilde X=0$ or $\tilde X\tilde\pi_{\mathrm{nil}}^{*}=0$ implies $\tilde\pi_{\mathrm{nil}}\tilde X\tilde\pi_{\mathrm{nil}}^{*}=0$. The image is contained in the kernel, since the operator is square-zero; the kernel is strictly larger, because the rank is one.

### The explicit Jordan chain

The canonical Hermitian pair gives a very explicit chain. Since $\tilde\pi_{\mathrm{nil}}\tilde\Pi_{\mathrm{id},-}=\tilde\pi_{\mathrm{nil}}$ and $\tilde\pi_{\mathrm{nil}}\tilde\pi_{\mathrm{nil}}^{*}=4a^{2}\tilde\Pi_{\mathrm{id},+}$, one has

$$
\boxed{\;
\mathrm{Sd}_{\tilde Q}(\tilde\Pi_{\mathrm{id},-})
=\tilde\pi_{\mathrm{nil}}\tilde\Pi_{\mathrm{id},-}\tilde\pi_{\mathrm{nil}}^{*}
=\tilde\pi_{\mathrm{nil}}\tilde\pi_{\mathrm{nil}}^{*}
=4a^{2}\tilde\Pi_{\mathrm{id},+},
\qquad
\mathrm{Sd}_{\tilde Q}(\tilde\Pi_{\mathrm{id},+})=0 .
\;}
$$

Thus

$$
\tilde\Pi_{\mathrm{id},-}\longmapsto 4a^{2}\tilde\Pi_{\mathrm{id},+}\longmapsto0
$$

is a chain of length two. The other two basis vectors are killed:

$$
\mathrm{Sd}_{\tilde Q}(\tilde\pi_{\mathrm{nil}})=0,
\qquad
\mathrm{Sd}_{\tilde Q}(\vec X)=0,
$$

where $\vec X$ is the corner vector spanning $\tilde\Pi_{\mathrm{id},-}\mathbb{B}\tilde\Pi_{\mathrm{id},+}$. In the basis

$$
\bigl(\tilde\Pi_{\mathrm{id},+},\ \tilde\pi_{\mathrm{nil}},\ \vec X,\ \tilde\Pi_{\mathrm{id},-}\bigr)
$$

the two-sided operator is therefore the single nilpotent block

$$
\boxed{\;
\mathsf M\bigl(\mathrm{Sd}_{\tilde Q}\bigr)=
\begin{pmatrix}
0&0&0&4a^{2}\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
\;}
$$

This matrix is the cleanest form of the operator: rank one, square zero, image $\mathbb{C}\tilde\Pi_{\mathrm{id},+}$, kernel $\mathbb{C}\tilde\Pi_{\mathrm{id},+}\oplus\mathbb{C}\tilde\pi_{\mathrm{nil}}\oplus\mathbb{C}\vec X$, and the single chain from $\tilde\Pi_{\mathrm{id},-}$ to $\tilde\Pi_{\mathrm{id},+}$.

The chain crosses the Peirce diagram from the $(--)$ corner to the $(+,+)$ corner. The element $\tilde\pi_{\mathrm{nil}}$ lies in the mixed corner $(+-)$; the other mixed corner $(-+)$ is represented by $\vec X$. The two-sided maps the $(--)$ corner to the $(+,+)$ corner and kills the two mixed corners and the $(+,+)$ corner itself. This is the exact two-step collapse of the spectral degeneracy.

### Eigenvalues and singular values on the nilpotents

The only eigenvalue is zero. The non-zero singular value is $4a^{2}$: indeed

$$
\mathrm{Sd}_{\tilde Q}\mathrm{Sd}_{\tilde Q}^{*}
=\mathrm{Sd}_{\tilde Q\tilde Q^{*}}
=\mathrm{Sd}_{4a^{2}\tilde\Pi_{\mathrm{id},+}}
=(4a^{2})^{2}\mathrm{Sd}_{\tilde\Pi_{\mathrm{id},+}},
$$

and $\mathrm{Sd}_{\tilde\Pi_{\mathrm{id},+}}$ is an orthogonal projection of rank one, with singular value one. Hence the singular value is $4a^{2}$. The eigenvalue-to-singular-value ratio is zero. This is the maximal defect: the operator has a non-zero singular value but no non-zero eigenvalue, and its image is a null line.

The operator $\mathrm{Sd}_{\tilde Q}=4a^{2}\mathrm{Sd}_{\tilde Q_0}$ is not a partial isometry in general: its singular value is $4a^{2}$, not one. It is $4a^{2}$ times the nilpotent partial isometry $\mathrm{Sd}_{\tilde Q_0}$.

## The Polar Decomposition of the Two-Sided Operator

The polar decomposition of the operator is the congruence of the polar decomposition of the element. The scalar $4a^{2}$ is the square of the element's singular value $2a$; the phase of the element never appears.

### The scalar collapse on the idempotent multiples

By the polar pair theorem, $\tilde Q=2a\tilde Q_0$ and $\tilde Q_0$ is a partial isometry. The multiplicativity of $\Theta$ gives

$$
\mathrm{Sd}_{\tilde Q}
=\mathrm{Sd}_{2a\tilde Q_0}
=4a^{2}\mathrm{Sd}_{\tilde Q_0}.
$$

This is the scalar collapse. The canonical left polar factor of $\mathrm{Sd}_{\tilde Q}$ is

$$
\lvert\mathrm{Sd}_{\tilde Q}\rvert
=\bigl(\mathrm{Sd}_{\tilde Q}\mathrm{Sd}_{\tilde Q}^{*}\bigr)^{1/2}
=\mathrm{Sd}_{\tilde Q_H}
=4a^{2}\mathrm{Sd}_P,
$$

which is positive semidefinite of rank one. On the image of $\mathrm{Sd}_{\tilde Q_0}$ it acts as the scalar $4a^{2}$, because $P\tilde Q_0=\tilde Q_0$ and therefore $\mathrm{Sd}_P\mathrm{Sd}_{\tilde Q_0}=\mathrm{Sd}_{\tilde Q_0}$. Hence

$$
\boxed{\;
\mathrm{Sd}_{\tilde Q}
=\mathrm{Sd}_{\tilde Q_H}\circ\mathrm{Sd}_{\tilde Q_0}
=4a^{2}\mathrm{Sd}_{\tilde Q_0},
\qquad
\mathrm{Sd}_{\tilde Q_0}\mathrm{Sd}_{\tilde Q_0}^{*}\mathrm{Sd}_{\tilde Q_0}
=\mathrm{Sd}_{\tilde Q_0}.
\;}
$$

The two-sided operator is $4a^{2}$ times a partial isometry. Its non-zero singular value is $4a^{2}$, the square of the one-sided singular value $2a$. Its eigenvalue is $\lvert c\rvert^{2}=4a^{2}\cos^{2}\theta$, the squared overlap of the two slots.

### The phase on the idempotent multiples

The partial-isometry factor is $\tilde Q_0=(c/\lvert c\rvert)\tilde\Pi_{\mathrm{id}}/\sqrt{\kappa}$. Since $\Theta$ is quadratic in $\tilde Q_0$ and $\tilde Q_0^{*}$,

$$
\mathrm{Sd}_{\tilde Q_0}
=\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}/\kappa,
$$

independent of the phase of $c$. The two-sided operator therefore cancels the phase:

$$
\mathrm{Sd}_{\tilde Q}
=\lvert c\rvert^{2}\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}
=4a^{2}\mathrm{Sd}_{\tilde Q_0}.
$$

The one-sided operator of the companion article keeps the phase in its eigenvalue $c$; the two-sided operator keeps only the modulus $\lvert c\rvert^{2}$ and the Hermitian projection $P$. When $\tilde\Pi_{\mathrm{id}}$ is Hermitian and $c=\varrho e^{i\theta_{\mathrm{pha}}}$, the polar pair is $\tilde Q_H=r\tilde\Pi_{\mathrm{id}}$ and $\tilde Q_0=e^{i\theta_{\mathrm{pha}}}\tilde\Pi_{\mathrm{id}}$, and the two-sided operator is $r^{2}\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}$: the phase has cancelled between $\tilde Q_0$ and $\tilde Q_0^{*}$.

### The polar pair of the element and of the operator on the idempotent multiples

The element pair is $(\tilde Q_H,\tilde Q_0)$, with $\tilde Q_H=2aP$ and $\tilde Q_0$ a partial isometry. The operator pair is $(\mathrm{Sd}_{\tilde Q_H},\mathrm{Sd}_{\tilde Q_0})$, with $\mathrm{Sd}_{\tilde Q_H}=4a^{2}\mathrm{Sd}_P$ positive and $\mathrm{Sd}_{\tilde Q_0}$ a partial isometry. The element pair is a rank-one singular value decomposition; the operator pair is its congruence. The scalar $4a^{2}$ is the square of the element's singular value $2a$, and the phase of the element is absent from the operator pair.

### The scalar collapse on the nilpotents

By the polar pair theorem, $\tilde Q=2a\tilde Q_0$ with $\tilde Q_0$ a nilpotent partial isometry. The multiplicativity of $\Theta$ gives

$$
\mathrm{Sd}_{\tilde Q}
=\mathrm{Sd}_{2a\tilde Q_0}
=4a^{2}\mathrm{Sd}_{\tilde Q_0}.
$$

This is the scalar collapse. The canonical left polar factor is

$$
\lvert\mathrm{Sd}_{\tilde Q}\rvert
=\bigl(\mathrm{Sd}_{\tilde Q}\mathrm{Sd}_{\tilde Q}^{*}\bigr)^{1/2}
=\mathrm{Sd}_{\tilde Q_H}
=4a^{2}\mathrm{Sd}_{\tilde\Pi_{\mathrm{id},+}},
$$

which is positive semidefinite of rank one. On the image of $\mathrm{Sd}_{\tilde Q_0}$ it acts as the scalar $4a^{2}$, because $\tilde\Pi_{\mathrm{id},+}\tilde Q_0=\tilde Q_0$ and therefore $\mathrm{Sd}_{\tilde\Pi_{\mathrm{id},+}}\mathrm{Sd}_{\tilde Q_0}=\mathrm{Sd}_{\tilde Q_0}$. Hence

$$
\boxed{\;
\mathrm{Sd}_{\tilde Q}
=\mathrm{Sd}_{\tilde Q_H}\circ\mathrm{Sd}_{\tilde Q_0}
=4a^{2}\mathrm{Sd}_{\tilde Q_0},
\qquad
\mathrm{Sd}_{\tilde Q_0}\mathrm{Sd}_{\tilde Q_0}^{*}\mathrm{Sd}_{\tilde Q_0}
=\mathrm{Sd}_{\tilde Q_0},
\qquad
\mathrm{Sd}_{\tilde Q_0}^{2}=0 .
\;}
$$

The two-sided operator is $4a^{2}$ times a nilpotent partial isometry. Its non-zero singular value is $4a^{2}=(2a)^{2}$; its only eigenvalue is zero. The polar decomposition of the operator is therefore a scalar times a nilpotent partial isometry, the extreme case of the collapse.

### The phase on the nilpotents

For a complex multiple

$$
\tilde\pi_{\mathrm{nil}}=c_0(\vec e_x+i\vec e_y),
\qquad
c_0=\lvert c_0\rvert e^{i\beta},
$$

one has $a=\lvert c_0\rvert$ and

$$
\tilde Q_0=e^{i\beta}\frac{\vec e_x+i\vec e_y}{2},
\qquad
\mathrm{Sd}_{\tilde Q_0}
=\mathrm{Sd}_{(\vec e_x+i\vec e_y)/2}
=\frac14\mathrm{Sd}_{\vec e_x+i\vec e_y},
$$

independent of the phase. The two-sided operator is

$$
\mathrm{Sd}_{\tilde Q}
=4\lvert c_0\rvert^{2}\mathrm{Sd}_{\tilde Q_0}
=\lvert c_0\rvert^{2}\mathrm{Sd}_{\vec e_x+i\vec e_y}
=\mathrm{Sd}_{\tilde\pi_{\mathrm{nil}}},
$$

so the phase has cancelled. The one-sided operator keeps the phase; the two-sided operator sees only $\lvert c_0\rvert^{2}$ and the canonical pair. The sign $\tilde\pi_{\mathrm{nil}}\mapsto-\tilde\pi_{\mathrm{nil}}$ also cancels.

### The polar pair of the element and of the operator on the nilpotents

The element pair is $(\tilde Q_H,\tilde Q_0)$, with $\tilde Q_H=2a\tilde\Pi_{\mathrm{id},+}$ positive of rank one and $\tilde Q_0$ a nilpotent partial isometry. The operator pair is $(\mathrm{Sd}_{\tilde Q_H},\mathrm{Sd}_{\tilde Q_0})$, with $\mathrm{Sd}_{\tilde Q_H}=4a^{2}\mathrm{Sd}_{\tilde\Pi_{\mathrm{id},+}}$ positive of rank one and $\mathrm{Sd}_{\tilde Q_0}$ a nilpotent partial isometry. The element pair is the rank-one singular value decomposition of the nilpotent; the operator pair is its congruence. The scalar $4a^{2}$ is the square of the element's singular value $2a$.

The spectral pair of the element does not exist off the origin: the element has only the eigenvalue zero, and no non-trivial idempotent commutes with it. The Hermitian form supplies the canonical pair $(\tilde\Pi_{\mathrm{id},+},\tilde\Pi_{\mathrm{id},-})$, and the polar decomposition uses exactly that pair. This is the precise sense in which the polar pair survives while the spectral decomposition fails.

## The Two Slots

The two slots of the two-sided operator survive the norm degeneration as the two singular vectors. On $\Sigma_{01}$ they are the column and the row of the rank-one matrix model, with overlap $\cos\theta=1/\sqrt{\kappa}$; on $\Sigma_{00}$ the overlap vanishes and the operator is square-zero.

### The Peirce picture on the idempotent multiples

On $\Sigma_{01}$ the eigenbasis exists because $B^{2}\neq0$. Its spectral projectors are $\tilde\Pi_{\mathrm{id}}$ and $\tilde\Pi_{\mathrm{id}}'$, and the four Peirce corners are one-dimensional. For a Hermitian $\tilde\Pi_{\mathrm{id}}$, the two-sided operator is the projection onto the $(+,+)$ corner:

$$
\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}(\tilde\Pi_{\mathrm{id}})=\tilde\Pi_{\mathrm{id}},
\qquad
\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}(\vec\Pi_{\mathrm{nil},-})=0,
\qquad
\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}(\vec\Pi_{\mathrm{nil},+})=0,
\qquad
\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}(\tilde\Pi_{\mathrm{id}}')=0.
$$

Thus the matrix is $\operatorname{diag}(1,0,0,0)$, and $\mathrm{Sd}_{\tilde Q}$ is $\operatorname{diag}(\lvert c\rvert^{2},0,0,0)$. The kernel is the sum of the three other corners. The two-sided operator pairs the two half-angles of the regular theory; on $\Sigma_{01}$ one half has eigenvalue zero, so only the $(+,+)$ pairing survives. The four eigenvalue products are

$$
c\bar c,\quad c\cdot0,\quad 0\cdot\bar c,\quad 0\cdot0,
$$

that is, $\lvert c\rvert^{2},0,0,0$. The full rotor of the regular two-sided operator has no angle or rapidity here: the element is not invertible, and the two-sided operator is not a conformal Lorentz transformation. It is an oblique projection onto a null line.

For a non-Hermitian $\tilde\Pi_{\mathrm{id}}$ the eigenbasis still exists, but the two-sided operator is not diagonal in it. The invariant statement is the spectrum: the four products are still $\lvert c\rvert^{2},0,0,0$, and the image is still the null line $\mathbb{C}P$, with $P=\tilde\Pi_{\mathrm{id}}\tilde\Pi_{\mathrm{id}}^{*}/\kappa\neq\tilde\Pi_{\mathrm{id}}$.

### The singular-vector picture on the idempotent multiples

In the matrix model the two slots are the singular vectors $u$ and $v$. The two-sided operator is

$$
\mathrm{Sd}_{\tilde Q}(\tilde X)
=4a^{2}\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)u u^{\dagger}.
$$

It reads the $v$-slot of $\tilde X$ through the scalar $v^{\dagger}\mathsf M_2(\tilde X)v$ and writes it on the $u$-slot. The relative phase of $u$ and $v$ cancels, because the two-sided operator uses $u$ and $u^{\dagger}$ on the outside and $v$ and $v^{\dagger}$ on the inside. The eigenvalue is $4a^{2}\lvert v^{\dagger}u\rvert^{2}=\lvert c\rvert^{2}$; the singular value is $4a^{2}$. The two slots are not orthogonal on $\Sigma_{01}$: their overlap has modulus $\cos\theta=1/\sqrt{\kappa}$. At the wall $\Sigma_{00}$ the overlap vanishes, the slots are orthogonal, and the two-sided operator becomes nilpotent.

This is the precise form of the two-slot structure of the regular two-sided operator. In the regular sector the two slots are the two chiralities, and the two-sided operator carries the full angle and rapidity as the product of the two half-factors. On the null cone the two slots are the singular vectors of the rank-one element, and the two-sided operator carries only the squared overlap $\cos^{2}\theta$. The angle between the slots replaces the angle of the Lorentz transformation.

### The Peirce picture on the nilpotents

In the canonical basis $(\tilde\Pi_{\mathrm{id},+},\tilde\pi_{\mathrm{nil}},\vec X,\tilde\Pi_{\mathrm{id},-})$ the two-sided operator is the single block of §*The Explicit Jordan Chain*:

$$
\mathsf M\bigl(\mathrm{Sd}_{\tilde Q}\bigr)=
\begin{pmatrix}
0&0&0&4a^{2}\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
$$

The chain is $\tilde\Pi_{\mathrm{id},-}\to4a^{2}\tilde\Pi_{\mathrm{id},+}\to0$. The image is the $(+,+)$ corner, the chain starts in the $(--)$ corner, and the two mixed corners are killed. In the regular sector the two-sided operator is a conformal Lorentz transformation with four eigenvalue products $\lambda_i\bar\lambda_j$; here all four products vanish. In the N-regular, spectrally degenerate sector the two-sided operator is a unipotent operator of Jordan type $3+1$; here it is a nilpotent operator of Jordan type $2+1+1$. The two chiral slots of the regular theory coalesce into the single chain $\tilde\Pi_{\mathrm{id},-}\to\tilde\Pi_{\mathrm{id},+}$.

### The singular-vector picture on the nilpotents

In the matrix model the two slots are the singular vectors $u$ and $v$, and they are orthogonal:

$$
v^{\dagger}u=0,
\qquad
\mathrm{Sd}_{\tilde Q}(\tilde X)
=4a^{2}\bigl(v^{\dagger}\mathsf M_2(\tilde X)v\bigr)u u^{\dagger}.
$$

The two-sided operator reads the $v$-slot of $\tilde X$ and writes it on the $u$-slot. Because $u\perp v$, the line on which it writes is annihilated on the next step. The relative phase of $u$ and $v$ cancels, and the overlap is zero. The angle $\theta$ between the slots is $\pi/2$; the eigenvalue-to-singular-value ratio is $\cos^{2}\theta=0$. The two-sided operator sees only the orthogonality.

This is the extreme case of the two-slot structure. On $\Sigma_{01}$ the slots had overlap $\cos\theta=1/\sqrt{\kappa}\in(0,1]$, and the two-sided operator was a projection up to scale. Here the overlap is zero, and the two-sided operator is nilpotent. The spectral wall is the orthogonality of the two slots.

## The Exponential

On $\Sigma_{01}$ the exponential is a line of projections; on $\Sigma_{00}$ it is unipotent. In both cases it removes the norm degeneration, and on $\Sigma_{01}$ it also removes the spectral one.

### The exponential on the idempotent multiples

**The operator exponential.** Since $\mathrm{Sd}_{\tilde Q}=\lvert c\rvert^{2}\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}$ and $\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}^{2}=\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}$,

$$
\boxed{\;
\exp\bigl(t\mathrm{Sd}_{\tilde Q}\bigr)
=I+\bigl(e^{t\lvert c\rvert^{2}}-1\bigr)\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}
\;}
$$

for every complex $t$. The eigenvalues are $e^{t\lvert c\rvert^{2}}$ and $1$ (three times); the determinant is $e^{t\lvert c\rvert^{2}}$. The group is invertible for every $t$, although the generator $\mathrm{Sd}_{\tilde Q}$ is singular. It dilates the image line and fixes the kernel hyperplane.

**The element flow.** The exponential $\exp(t\tilde Q)=e_t+(e^{tc}-1)\tilde\Pi_{\mathrm{id}}$ is invertible for every $t$, and it lies in $\Sigma_{11}$ for generic $t\neq0$; at the exceptional values $e^{tc}=1$ it is $e_t$ on the wall $\Sigma_{10}$. Its two-sided operator $\mathrm{Sd}_{\exp(t\tilde Q)}$ is therefore a conformal Lorentz transformation, with the generator $\mathrm{Sd}_{\tilde Q}$:

$$
\mathrm{Sd}_{\exp(t\tilde Q)}
=\exp\bigl(t\mathrm{Sd}_{\tilde Q}\bigr).
$$

The generator is singular, but the one-parameter group it generates is invertible. The one-sided rate is $c$; the two-sided operator rate is $\lvert c\rvert^{2}$, the squared modulus. The generator is now an oblique projection rather than a conformal Lorentz transformation.

### The exponential on the nilpotents

**The operator exponential.** Since $\mathrm{Sd}_{\tilde Q}^{2}=0$,

$$
\boxed{\;
\exp\bigl(t\mathrm{Sd}_{\tilde Q}\bigr)=I+t\mathrm{Sd}_{\tilde Q}
\;}
$$

for every complex $t$. The eigenvalues are all $1$; the Jordan form is $J_2(1)\oplus1\oplus1$; the determinant is $1$. The group is unipotent: it is a shear, not a dilation. It is invertible for every $t$, although the generator is nilpotent and singular.

**The element flow.** Since $\tilde\pi_{\mathrm{nil}}^{2}=0$,

$$
\exp\bigl(t\tilde\pi_{\mathrm{nil}}\bigr)=e_t+t\tilde\pi_{\mathrm{nil}} .
$$

The quaternionic norm is $1$, and the vector form is

$$
B^{2}\bigl(\exp(t\tilde\pi_{\mathrm{nil}})\bigr)=t^{2}B^{2}(\tilde\pi_{\mathrm{nil}})=0 .
$$

Hence the exponential is invertible with $B^{2}=0$: for every $t$ it lies in the N-regular, spectrally degenerate sector $\Sigma_{10}$ (at $t=0$ it is $e_t$). The element flow moves one wall away: it removes the norm degeneration and preserves the spectral one. Its two-sided operator is

$$
\mathrm{Sd}_{\exp(t\tilde\pi_{\mathrm{nil}})}
=\exp\bigl(t\mathrm{Sd}_{\tilde Q}\bigr),
$$

a unipotent Lorentz flow of Jordan type $2+1+1$. It fixes the kernel hyperplane and shears along the single chain. The generator $\mathrm{Sd}_{\tilde Q}$ is singular; the one-parameter group it generates is invertible.

The one-sided exponential of the companion article is a unipotent shear of the operator space, not a Lorentz transformation. The two-sided exponential is a unipotent Lorentz flow. The difference is the same as in the regular sector, at the level of the slots: the one-sided operator reads one slot and the two-sided operator pairs two. The analogy stops there. In the regular sector the one-sided slot carries the half-angle $\theta/2$; here there is no angle to halve, and the one-sided exponential is unipotent.

## Worked Examples

Two examples on each stratum.

### Example 1: a Hermitian idempotent

Take $\tilde Q=e_t+i\vec e_x$. Then $c=2$, $\tilde\Pi_{\mathrm{id}}=(e_t+i\vec e_x)/2$, $\kappa=1$, $a=1$, $P=\tilde\Pi_{\mathrm{id}}$, and $\tilde Q_H=\tilde Q$, $\tilde Q_0=\tilde\Pi_{\mathrm{id}}$. The two-sided operator is $\mathrm{Sd}_{\tilde Q}=4\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}$, with rank one, eigenvalue $4$, singular value $4$, and image the line $\mathbb{C}\tilde Q$. In the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$,

$$
\mathsf M\bigl(\mathrm{Sd}_{\tilde Q}\bigr)=
\begin{pmatrix}
2&-2i&0&0\\
2i&2&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
$$

with trace $4$, rank one and square $\mathrm{Sd}_{\tilde Q}^{2}=4\mathrm{Sd}_{\tilde Q}$. The exponential is

$$
\exp\bigl(t\mathrm{Sd}_{\tilde Q}\bigr)=I+\bigl(e^{4t}-1\bigr)\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}.
$$

### Example 2: a non-Hermitian idempotent

Take $\tilde Q=e_t+\vec e_x+i\sqrt2\,\vec e_z$. Then $c=2$, $\kappa=2$, $a=\sqrt2$, $\tilde{Ζ}=\vec e_x+i\sqrt2\,\vec e_z$, and

$$
P=\frac12 e_t-\frac{i\sqrt2}{4}\vec e_y+\frac{i\sqrt2}{4}\vec e_z,
\qquad
\tilde Q_H=\sqrt2\,e_t-i\vec e_y+i\vec e_z,
\qquad
\tilde Q_0=\frac{\sqrt2}{4}e_t+\frac{\sqrt2}{4}\vec e_x+\frac{i}{2}\vec e_z .
$$

The two-sided operator is $\mathrm{Sd}_{\tilde Q}=4\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}$, with rank one, eigenvalue $4$, and singular value $8$. The eigenvalue-to-singular-value ratio is $\tfrac12=\cos^{2}\theta$, because $\cos\theta=1/\sqrt2$. The image is the null line $\mathbb{C}P$, with $P\neq\tilde\Pi_{\mathrm{id}}$; the two-sided operator is not self-adjoint, and its Peirce matrix in the spectral basis is not diagonal. The example shows the difference between the eigenvalue $\lvert c\rvert^{2}$ and the singular value $4a^{2}$ for an oblique idempotent.

### Example 3: the standard nilpotent

Take

$$
\tilde\pi_{\mathrm{nil}}=\vec e_x+i\vec e_y .
$$

Then $a=1$, $\vec c=\vec e_z$, and

$$
\tilde\Pi_{\mathrm{id},+}=\frac{e_t+i\vec e_z}{2},
\qquad
\tilde\Pi_{\mathrm{id},-}=\frac{e_t-i\vec e_z}{2},
\qquad
\tilde Q_H=e_t+i\vec e_z,
\qquad
\tilde Q_0=\frac{\vec e_x+i\vec e_y}{2}.
$$

The matrix model is

$$
\mathsf M_2(\tilde\pi_{\mathrm{nil}})=
\begin{pmatrix}0&-2i\\0&0\end{pmatrix},
\qquad
\mathsf M_2(\tilde Q_H)=
\begin{pmatrix}2&0\\0&0\end{pmatrix},
\qquad
\mathsf M_2(\tilde Q_0)=
\begin{pmatrix}0&-i\\0&0\end{pmatrix}.
$$

In the standard basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ the two-sided operator is

$$
\mathsf M\bigl(\mathrm{Sd}_{\tilde\pi_{\mathrm{nil}}}\bigr)=
\begin{pmatrix}
2&0&0&2i\\
0&0&0&0\\
0&0&0&0\\
2i&0&0&-2
\end{pmatrix},
$$

with trace zero, rank one and square zero. The image is the line $\mathbb{C}(e_t+i\vec e_z)=\mathbb{C}\tilde\Pi_{\mathrm{id},+}$; the first column is $2(e_t+i\vec e_z)=4\tilde\Pi_{\mathrm{id},+}$.

For the Peirce form, take

$$
\vec X=\frac{-\vec e_x+i\vec e_y}{4},
\qquad
\tilde\pi_{\mathrm{nil}}\vec X=\tilde\Pi_{\mathrm{id},+},
\qquad
\vec X\tilde\pi_{\mathrm{nil}}=\tilde\Pi_{\mathrm{id},-} .
$$

In the basis $(\tilde\Pi_{\mathrm{id},+},\tilde\pi_{\mathrm{nil}},\vec X,\tilde\Pi_{\mathrm{id},-})$,

$$
\mathsf M\bigl(\mathrm{Sd}_{\tilde\pi_{\mathrm{nil}}}\bigr)=
\begin{pmatrix}
0&0&0&4\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
$$

the single chain being $\tilde\Pi_{\mathrm{id},-}\to4\tilde\Pi_{\mathrm{id},+}\to0$. The exponential is

$$
\exp\bigl(t\mathrm{Sd}_{\tilde\pi_{\mathrm{nil}}}\bigr)=I+t\mathrm{Sd}_{\tilde\pi_{\mathrm{nil}}}.
$$

### Example 4: a complex scalar multiple

For

$$
\tilde\pi_{\mathrm{nil}}=c_0(\vec e_x+i\vec e_y),
\qquad
c_0=\lvert c_0\rvert e^{i\beta},
$$

the element has $a=\lvert c_0\rvert$, and

$$
\tilde Q_0=e^{i\beta}\frac{\vec e_x+i\vec e_y}{2},
\qquad
\mathrm{Sd}_{\tilde\pi_{\mathrm{nil}}}
=4\lvert c_0\rvert^{2}\mathrm{Sd}_{\tilde Q_0}.
$$

The phase $e^{i\beta}$ cancels in the two-sided operator. The two-sided operator depends only on $\lvert c_0\rvert$ and the canonical pair; the one-sided operator of the companion article keeps the phase.

## Summary

### Main Results on the Idempotent Multiples

| item | value |
|---|---|
| sector | $\Sigma_{01}=\{\langle\tilde Q\rangle_{\natural}=0,\ B^{2}\neq0\}$ |
| parameter | $\tilde Q=c\tilde\Pi_{\mathrm{id}}$, $c=2Q_t\neq0$ |
| two-sided operator | $\mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ |
| closed form | $\mathrm{Sd}_{\tilde Q}=\lvert c\rvert^{2}\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}$, $\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}^{2}=\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}$ |
| square | $\mathrm{Sd}_{\tilde Q}^{2}=\lvert c\rvert^{2}\mathrm{Sd}_{\tilde Q}$ |
| rank | $1$ |
| spectrum | $\{\lvert c\rvert^{2},0\}$, multiplicities $1,3$ |
| Jordan form | diagonal, $\operatorname{diag}(\lvert c\rvert^{2},0,0,0)$; the eigenbasis of $\tilde Q$ diagonalizes it only when $\tilde\Pi_{\mathrm{id}}$ is Hermitian |
| trace | $\lvert c\rvert^{2}=4a^{2}\cos^{2}\theta$ |
| the determinant of the image | $0$ |
| eigenvalue on the image | $\lvert c\rvert^{2}$ |
| singular value | $4a^{2}$ |
| image | the null line $\mathbb{C}P$, $P=\tilde Q\tilde Q^{*}/(4a^{2})$ |
| kernel | $\{\tilde X:\tilde\Pi_{\mathrm{id}}\tilde X\tilde\Pi_{\mathrm{id}}^{*}=0\}$, a hyperplane |
| scalar collapse | $\mathrm{Sd}_{\tilde Q}=4a^{2}\mathrm{Sd}_{\tilde Q_0}$ |
| exponential | $\exp(t\mathrm{Sd}_{\tilde Q})=I+(e^{t\lvert c\rvert^{2}}-1)\mathrm{Sd}_{\tilde\Pi_{\mathrm{id}}}$ |
| element flow | $\exp(t\tilde Q)=e_t+(e^{tc}-1)\tilde\Pi_{\mathrm{id}}$, a unit in $\Sigma_{11}$ for generic $t\neq0$ |

### Main Results on the Nilpotents

| item | value |
|---|---|
| sector | $\Sigma_{00}=\{\langle\tilde Q\rangle_{\natural}=0,\ B^{2}=0\}$ |
| parameter | $\tilde\pi_{\mathrm{nil}}=\vec A+i\vec B$, $\lVert\vec A\rVert=\lVert\vec B\rVert=a>0$, $\vec A\cdot\vec B=0$ |
| canonical pair | $\tilde\Pi_{\mathrm{id},\pm}=(e_t\pm i\vec c)/2$, $\vec c=\vec A\times\vec B/a^{2}$ |
| polar pair | $\tilde Q_H=2a\tilde\Pi_{\mathrm{id},+}$, $\tilde Q_0=\tilde\pi_{\mathrm{nil}}/(2a)$, $\tilde Q_0^{2}=0$ |
| two-sided operator | $\mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ |
| square | $\mathrm{Sd}_{\tilde Q}^{2}=0$ |
| rank | $1$ |
| spectrum | $\{0\}$, algebraic multiplicity $4$, geometric multiplicity $3$ |
| Jordan form | $J_2(0)\oplus0\oplus0$ |
| trace | $0$ |
| the determinant of the image | $0$ |
| eigenvalue | $0$ |
| singular value | $4a^{2}$ |
| image | the null line $\mathbb{C}\tilde\Pi_{\mathrm{id},+}$ |
| kernel | $\{\tilde X:\tilde\pi_{\mathrm{nil}}\tilde X\tilde\pi_{\mathrm{nil}}^{*}=0\}$, a hyperplane |
| chain | $\tilde\Pi_{\mathrm{id},-}\mapsto4a^{2}\tilde\Pi_{\mathrm{id},+}\mapsto0$ |
| scalar collapse | $\mathrm{Sd}_{\tilde Q}=4a^{2}\mathrm{Sd}_{\tilde Q_0}$ |
| exponential | $\exp(t\mathrm{Sd}_{\tilde Q})=I+t\mathrm{Sd}_{\tilde Q}$ |
| element flow | $\exp(t\tilde\pi_{\mathrm{nil}})=e_t+t\tilde\pi_{\mathrm{nil}}$, a unit in $\Sigma_{10}$ for every $t$ (at $t=0$ it is $e_t$) |

### What the Two-Sided Operator Shows

The norm fixes the rank and the image; the spectral condition fixes the eigenvalue and the Jordan type.

- The norm degeneration fixes the rank: on the null cone the two-sided operator has rank one, its image is a single null line, and its kernel has dimension three.
- On $\Sigma_{01}$ the operator is $\lvert c\rvert^{2}=4a^{2}\cos^{2}\theta$ times a projection, with spectrum $\{\lvert c\rvert^{2},0,0,0\}$ and no defect.
- On $\Sigma_{00}$ the operator is square-zero, $\mathrm{Sd}_{\tilde\pi_{\mathrm{nil}}}^{2}=0$, with the single eigenvalue zero, one Jordan block of size two and two fixed zero directions: the maximal collapse.
- The singular value $4a^{2}$ is the square of the one-sided singular value $2a$, and it is independent of the phase.
- The polar decomposition of the operator is the congruence of the polar decomposition of the element; the positive factor is $4a^{2}\mathrm{Sd}_P$ or $4a^{2}\mathrm{Sd}_{\tilde\Pi_{\mathrm{id},+}}$.
- The phase and the sign cancel: the two-sided operator sees only $\lvert c\rvert^{2}$ and the canonical pair.
- The two slots survive as the singular vectors; their overlap $1/\sqrt{\kappa}$ vanishes exactly at the wall $\Sigma_{00}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde Q\rangle_{\natural}$, $\langle\tilde Q\rangle_{*}$ | the quaternionic norm $Q_t^{2}+B^{2}$, zero on the null cone, and the Hermitian norm $\operatorname{Sc}(\tilde Q\tilde Q^{*})$, positive there |
| $\tilde Q=c\tilde\Pi_{\mathrm{id}}$ | an element of $\Sigma_{01}$ |
| $\mathrm{Sd}_{\tilde Q}$ | the two-sided operator $\tilde X\mapsto\tilde Q\tilde X\tilde Q^{*}$ |
| $\kappa=2\langle\tilde\Pi_{\mathrm{id}}\rangle_{*}$ | the obliqueness, $\kappa\ge1$ |
| $a=\sqrt{\langle\tilde Q\rangle_{*}/2}$ | the half singular value, $2a$ the non-zero singular value |
| $P=\tilde Q\tilde Q^{*}/(4a^{2})$ | the rank-one Hermitian idempotent and the image line |
| $\tilde Q_H=2aP$ | the Hermitian factor |
| $\tilde Q_0=\tilde Q/(2a)$ | the partial-isometry factor |
| $u,v$ | the left and right singular vectors |
| $v^{\dagger}u=Q_t/a$ | the overlap, modulus $1/\sqrt{\kappa}$ |
| $\theta$ | the angle between the slots, $\cos\theta=1/\sqrt{\kappa}$ |
| $\tilde\pi_{\mathrm{nil}}=\vec A+i\vec B$ | a non-zero element of $\Sigma_{00}$ |
| $a=\lVert\vec A\rVert=\lVert\vec B\rVert$ | the half singular value |
| $\vec c=\vec A\times\vec B/a^{2}$ | the unit spectral direction |
| $\tilde\Pi_{\mathrm{id},\pm}=(e_t\pm i\vec c)/2$ | the canonical Hermitian idempotents |
| $\tilde Q_H=2a\tilde\Pi_{\mathrm{id},+}$ | the Hermitian factor |
| $\tilde Q_0=\tilde\pi_{\mathrm{nil}}/(2a)$ | the nilpotent partial-isometry factor |
| $L_{\tilde\pi_{\mathrm{nil}}},R_{\tilde\pi_{\mathrm{nil}}}$ | the one-sided operators of the companion article |
| $\vec X$ | a normalized corner vector, $\tilde\pi_{\mathrm{nil}}\vec X=\tilde\Pi_{\mathrm{id},+}$ |
| $J_2(0)$ | the nilpotent Jordan block of size two |

## Further Reading

- [One-Sided Operators on the N-Degenerate Sector](one-sided-operators-on-the-n-degenerate-sector.html), for the one-sided companion on the same two strata.
- [Two-Sided Operators on the N-Regular Sector](two-sided-operators-on-the-n-regular-sector.html), §*The Exponential of the Two-Sided Operator*, for the exponential of the two-sided operator off the null cone.
- [The Polar Decomposition of an N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the two-factor polar pair used here.
- [Introduction to the Operators on the Four Sectors](introduction-to-the-operators-on-the-four-sectors.html), for the three operators, the doubling rule and the table of the four sectors.
