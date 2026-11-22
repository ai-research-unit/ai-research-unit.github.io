# __One-Sided Operators on the N-Degenerate Sector__

## Introduction

**The two projectors of the algebra.** Two endomorphisms of $\mathbb{B}$ are not of the polar family and are worth naming at the start, because they act on every sector: $P_{0}=\tfrac12(\mathrm{id}+\natural)$ and $P_{1}=\tfrac12(\mathrm{id}-\natural)$, with $P_{0}^{2}=P_{0}$, $P_{1}^{2}=P_{1}$, $P_{0}P_{1}=0$ and $P_{0}+P_{1}=\mathrm{id}$. Their images are the centre $\mathbb{C}e_t$ and the complexified vector part $\mathbb{C}\mathfrak{k}$, the two summands of the Clebsch–Gordan series $V_{1/2}\otimes V_{1/2}=V_{1}\oplus V_{0}$ of the algebra. They are canonical, they carry no parameter, and nothing in this article depends on them; they are named here because they are the only two idempotent endomorphisms that come with the algebra itself. The decomposition is *The Clebsch–Gordan Decomposition of the Biquaternion Algebra*.

The quaternion norm $N=\langle\tilde Q\rangle_{\natural}=Q_t^{2}+B^{2}$ splits the biquaternion algebra in two. This article treats the second half, the **null cone** $N=0$, a closed set of real dimension six and real codimension two.

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $\vec e_x\vec e_y=\vec e_z$ and $\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t$. The Hermitian conjugation is $\tilde X^{*}=\overline{\tilde X^{\natural}}$. Two forms are used and they must be kept apart: the quaternionic norm $\langle\tilde X\rangle_{\natural}=\sum_\mu X_\mu^{2}$, which vanishes on the null cone, and the Hermitian norm $\langle\tilde X\rangle_{*}=\operatorname{Sc}(\tilde X\tilde X^{*})$, which does not. The matrix model $\mathsf M_2$ sends $e_t$ to $I_2$ and $\vec e_k$ to $-i\sigma_k$, and it is multiplicative.

The biquaternion algebra acts on itself by left and right multiplication,

$$
L_{\tilde Q}(\tilde X)=\tilde Q\tilde X,\qquad R_{\tilde Q}(\tilde X)=\tilde X\tilde Q .
$$

On the null cone the modulus $\varrho\,e^{i\theta_{\mathrm{pha}}}=\sqrt{\langle\tilde Q\rangle_{\natural}}$ vanishes, so the modulus–unit decomposition and the four-factor word $\tilde Q=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ do not exist. What survives is the two-factor **polar pair**

$$
\tilde Q=\tilde Q_H\tilde Q_0,\qquad \tilde Q_H=\bigl(\tilde Q\tilde Q^{*}\bigr)^{1/2},\qquad \tilde Q_0=\tilde Q_H^{+}\tilde Q,
$$

of *The Polar Decomposition of an N-Degenerate Biquaternion*. The factor $\tilde Q_H$ is Hermitian positive semidefinite of rank one and $\tilde Q_0$ is a partial isometry. The main result is that the one-sided operator is a scalar multiple of a partial isometry,

$$
L_{\tilde Q}=2a\,L_{\tilde Q_0},\qquad R_{\tilde Q}=2a\,R_{\tilde Q_0},
$$

with $2a>0$ the non-zero singular value of $\tilde Q$ in the matrix model, repeated twice.

**What the norm decides, and what the vector form decides.** Every global property of the one-sided operators is fixed by $N$ alone. On the whole null cone both operators are singular, both have complex rank two, both have a two-dimensional kernel, and both have a two-dimensional totally isotropic image, a left ideal for $L$ and a right ideal for $R$. The second condition $B^{2}=0$ decides only the **eigenvalue count and the Jordan type**, exactly as it does on the N-regular sector: the first stratum $\Sigma_{01}$ has the two distinct eigenvalues $c,0$ and no defect, and the second $\Sigma_{00}$ has the single eigenvalue $0$ and maximal defect, the minimal polynomial $X^{2}$. A reader who knows the rank two and the scalar $2a$ knows everything the norm decides; the wall decides the rest.

The two strata are therefore two sections of one theory and not two theories:

$$
\Sigma_{01}=\{N=0,\ B^{2}\neq0\}:\ \tilde Q=c\,\tilde\Pi,\quad c=2Q_t\neq0,\quad \tilde\Pi^{2}=\tilde\Pi\neq0,e_t,
$$

$$
\Sigma_{00}=\{N=0,\ B^{2}=0\}:\ \tilde Q=\tilde\nu=\vec A+i\vec B,\quad \lVert\vec A\rVert=\lVert\vec B\rVert=a>0,\quad \vec A\cdot\vec B=0,\quad \tilde\nu^{2}=0 .
$$

The first is the set of non-zero complex multiples of non-trivial idempotents; the second is the set of non-zero nilpotents, with the origin as its only semisimple element. The word **N-degenerate** refers to the vanishing of the quaternionic norm, the word **spectrally degenerate** to the vanishing of $B^{2}$.

The article is organized as follows. §*The Polar Pair* proves the rank-one singular value decomposition for $\Sigma_{01}$ and the canonical Hermitian pair for $\Sigma_{00}$. §*The One-Sided Operators* computes the composition laws, the rank, the spectrum, the image and the kernel on both strata. §*The Polar Pair, One-Sided* proves the scalar collapse and reads the operator through the pair. §*The Eigenbasis and the Two Slots* gives the diagonal form and the spinorial reading for $\Sigma_{01}$. §*The Exponential* computes the one-parameter group on both strata. §*Worked Examples* treats a Hermitian idempotent, a non-Hermitian idempotent, the standard nilpotent and a complex scalar multiple. The article closes with the summary, the notation and the readings.
## The Polar Pair

The two strata carry two different polar pairs, and the difference is the eigenvalue at which the positive factor acts. On $\Sigma_{01}$ the pair is a rank-one projection scaled by $2a$ and the partial isometry is a scalar times an idempotent. On $\Sigma_{00}$ the positive factor is $2a\tilde\Pi_+$ and the partial isometry is itself nilpotent. The common statement is the scalar collapse of §*The Polar Pair, One-Sided*.

### The rank-one singular value decomposition

**Theorem (the null cone as normalized rank-one partial isometries).** Let $\tilde Q\in\mathbb{B}$ be non-zero. Then $\tilde Q$ lies on the null cone $\mathcal N=\{\langle\tilde Q\rangle_{\natural}=0\}$ if and only if

$$
\tilde Q=2a\,\tilde Q_0
$$

with $a>0$ and $\tilde Q_0$ a rank-one partial isometry,

$$
\tilde Q_0\tilde Q_0^{*}\tilde Q_0=\tilde Q_0,\qquad \tilde Q_0\neq0,\qquad \operatorname{rank}\mathsf M_2(\tilde Q_0)=1 .
$$

The scalar and the partial isometry are unique:

$$
a=\sqrt{\frac{\langle\tilde Q\rangle_{*}}{2}},\qquad \tilde Q_0=\frac{\tilde Q}{2a}.
$$

*Proof.* The determinant of $\mathsf M_2(\tilde Q)$ is $\langle\tilde Q\rangle_{\natural}$. On the null cone and for $\tilde Q\neq0$ the matrix is non-zero of determinant zero, hence of rank one. Its singular value decomposition is

$$
\mathsf M_2(\tilde Q)=2a\,u v^{\dagger},
$$

with $a>0$ and $u,v$ unit vectors of $\mathbb{C}^{2}$. The Frobenius norm is $\langle\mathsf M_2(\tilde Q)\rangle_*=4a^{2}=2\langle\tilde Q\rangle_{*}$, hence $a=\sqrt{\langle\tilde Q\rangle_{*}/2}$. The matrix $u v^{\dagger}$ is a rank-one partial isometry, because $(u v^{\dagger})(u v^{\dagger})^{\dagger}(u v^{\dagger})=u v^{\dagger}$. Translating back gives $\tilde Q=2a\tilde Q_0$ with $\tilde Q_0=\tilde Q/(2a)$. Conversely, a non-zero rank-one partial isometry has determinant zero, hence $\langle\tilde Q\rangle_{\natural}=0$.

The two factors of the decomposition are the **left slot** $u$ and the **right slot** $v$ of the rank-one matrix. They are defined up to a common phase; the relative phase is the phase of $\tilde Q$. The overlap

$$
v^{\dagger}u=\frac{\operatorname{tr}\mathsf M_2(\tilde Q)}{2a}=\frac{2Q_t}{2a}=\frac{c}{2a}=\frac{Q_t}{a}
$$

measures the angle between the two slots. Its modulus is at most one, by the Cauchy–Schwarz inequality. The sector $\Sigma_{01}$ is exactly the case $v^{\dagger}u\neq0$; the wall $\Sigma_{00}$ is the case $v^{\dagger}u=0$. The two slots are therefore **not orthogonal** on $\Sigma_{01}$, and they become orthogonal exactly at the spectral wall.

### The Hermitian factor and the partial-isometry factor

**Theorem (the polar pair on the null cone).** For $\tilde Q\neq0$ on the null cone, put

$$
a=\sqrt{\frac{\langle\tilde Q\rangle_{*}}{2}},\qquad
P=\frac{\tilde Q\tilde Q^{*}}{4a^{2}},\qquad
\tilde Q_H=2a\,P,\qquad
\tilde Q_0=\frac{\tilde Q}{2a}.
$$

Then:

**(a)** $P$ is a rank-one Hermitian idempotent, $P^{2}=P$, $P^{*}=P$, and $\tilde Q_H=2aP$ is Hermitian positive semidefinite of rank one, with spectrum $\{0,2a\}$;

**(b)** $\tilde Q_0$ is a partial isometry, with

$$
\tilde Q_0\tilde Q_0^{*}=P,\qquad \tilde Q_0^{*}\tilde Q_0=P',
$$

where $P'=Q_0^{*}Q_0$ is the initial projection of the partial isometry;

**(c)** $\tilde Q=\tilde Q_H\tilde Q_0=2a\tilde Q_0$;

**(d)** in the matrix model, with $\mathsf M_2(\tilde Q)=2a\,u v^{\dagger}$,

$$
P=u u^{\dagger},\qquad \tilde Q_H=2a\,u u^{\dagger},\qquad \tilde Q_0=u v^{\dagger},\qquad P'=v v^{\dagger}.
$$

*Proof.* (d) is the singular value decomposition. The identities in (a)–(c) follow by direct matrix multiplication: $P^{2}=u u^{\dagger}u u^{\dagger}=u u^{\dagger}=P$, $P^{*}=P$, and

$$
\tilde Q\tilde Q^{*}
=(2a)^{2}u v^{\dagger}v u^{\dagger}
=4a^{2}u u^{\dagger}
=4a^{2}P ,
$$

so $\tilde Q_H^{2}=\tilde Q\tilde Q^{*}$. The products $\tilde Q_0\tilde Q_0^{*}=P$ and $\tilde Q_0^{*}\tilde Q_0=P'$ are immediate. In the matrix model the partial-isometry identity is

$$
\tilde Q_0\tilde Q_0^{*}\tilde Q_0
=u(v^{\dagger}v)(u^{\dagger}u)v^{\dagger}
=u v^{\dagger}
=\tilde Q_0 .
$$

Finally $\tilde Q_H\tilde Q_0=2aP\tilde Q_0=2a\tilde Q_0=\tilde Q$.

The pair $(\tilde Q_H,\tilde Q_0)$ is the general pair of *The Polar Decomposition of an N-Degenerate Biquaternion*, specialized to the rank-one case. It is not the modulus–unit pair: the modulus $\varrho\,e^{i\theta_{\mathrm{pha}}}=\sqrt{\langle\tilde Q\rangle_{\natural}}$ is zero, while $\tilde Q_H$ is a non-zero rank-one element. The number $2a$ is the non-zero singular value of $\tilde Q$; it is not an eigenvalue in general (it coincides with $c$ when $\kappa=1$ and $c>0$).

### The closed form on $\Sigma_{01}$

Let $\tilde Q=c\tilde\Pi$ with $c=2Q_t\neq0$ and $\tilde\Pi$ a non-trivial idempotent. Put

$$
\tilde{Ζ}=2\tilde\Pi-e_t,\qquad
\tilde\Pi'=e_t-\tilde\Pi,\qquad
\kappa=2\langle\tilde\Pi\rangle_{*}=\frac{1+\lVert\tilde{Ζ}\rVert^{2}}{2},
$$

where $\lVert\tilde{Ζ}\rVert^{2}=\lvertΖ_x\rvert^{2}+\lvertΖ_y\rvert^{2}+\lvertΖ_z\rvert^{2}$. The root satisfies $\tilde{Ζ}^{2}=e_t$ and $\tilde{Ζ}\neq\pm e_t$; the idempotent has $\langle\tilde\Pi\rangle_{\natural}=0$ and $B^{2}(\tilde\Pi)=-\tfrac14$. The number $\kappa$ is real and $\kappa\ge1$, with equality exactly when $\tilde\Pi$ is Hermitian.

**Proposition (the closed form).** On $\Sigma_{01}$,

$$
\boxed{\;
a=\frac{\lvert c\rvert\sqrt{\kappa}}{2}=\lvert Q_t\rvert\sqrt{\kappa},\qquad
P=\frac{\tilde\Pi\tilde\Pi^{*}}{\kappa},\qquad
\tilde Q_H=\lvert c\rvert\sqrt{\kappa}\,P,\qquad
\tilde Q_0=\frac{c}{\lvert c\rvert}\frac{\tilde\Pi}{\sqrt{\kappa}}=\frac{Q_t}{a}\tilde\Pi .
\;}
$$

*Proof.* The Hermitian norm of $\tilde\Pi=(e_t+\tilde{Ζ})/2$ is

$$
\langle\tilde\Pi\rangle_{*}
=\frac14\bigl(1+\langle\tilde{Ζ}\tilde{Ζ}^{*}\rangle_{*}\bigr)
=\frac{1+\lVert\tilde{Ζ}\rVert^{2}}{4}
=\frac{\kappa}{2},
$$

because $\operatorname{Sc}\tilde{Ζ}=0$ and $\operatorname{Sc}(\tilde{Ζ}\tilde{Ζ}^{*})=\lVert\tilde{Ζ}\rVert^{2}$. Hence $\langle\tilde Q\rangle_{*}=\lvert c\rvert^{2}\kappa/2$ and $a=\lvert c\rvert\sqrt{\kappa}/2$. The formula for $P$ is $\tilde Q\tilde Q^{*}/(4a^{2})=\tilde\Pi\tilde\Pi^{*}/\kappa$. The partial-isometry factor is

$$
\tilde Q_0=\frac{\tilde Q}{2a}=\frac{c\tilde\Pi}{\lvert c\rvert\sqrt{\kappa}}
=\frac{c}{\lvert c\rvert}\frac{\tilde\Pi}{\sqrt{\kappa}},
$$

and $Q_t/a=c/(2a)$.

The normalized element $\tilde Q_0$ is a partial isometry although neither factor is a partial isometry in general: $\tilde\Pi$ is a projection but not an orthogonal projection, and $\lvert Q_t\rvert/a=1/\sqrt{\kappa}\le1$. The product is a partial isometry because the obliqueness of $\tilde\Pi$ compensates the scalar. In the matrix picture, $\tilde\Pi=u v^{\dagger}/(v^{\dagger}u)$ and

$$
\tilde Q_0=u v^{\dagger},\qquad
v^{\dagger}u=\frac{Q_t}{a},\qquad
\lvert v^{\dagger}u\rvert=\frac{1}{\sqrt{\kappa}}.
$$

The angle $\theta$ between the two slots is therefore given by $\cos\theta=1/\sqrt{\kappa}$. The idempotent is Hermitian exactly when the slots coincide, $\kappa=1$ and $\cos\theta=1$.

**Corollary (the square of the partial isometry).** On $\Sigma_{01}$,

$$
\tilde Q_0^{2}=\frac{Q_t}{a}\,\tilde Q_0 .
$$

The scalar $Q_t/a$ is non-zero, so $\tilde Q_0/(Q_t/a)=\tilde\Pi$ is an idempotent. This is the algebraic form of the spectral regularity: the normalized element is a scalar times an idempotent, not a nilpotent. The spectral wall is the boundary at which the overlap $v^{\dagger}u$ vanishes; there the normalized element is nilpotent, not a scalar times an idempotent.

### The canonical Hermitian pair

Let $\tilde\nu=\vec A+i\vec B$ with $\vec A,\vec B$ real, orthogonal and of equal norm $a>0$. The vector

$$
\vec c=\frac{\vec A\times\vec B}{a^{2}}
$$

is real and unit. Define

$$
\tilde\Pi_+=\frac{e_t+i\vec c}{2},
\qquad
\tilde\Pi_-=\frac{e_t-i\vec c}{2},
\qquad
\tilde\Pi_++\tilde\Pi_-=e_t,
\qquad
\tilde\Pi_\pm^{2}=\tilde\Pi_\pm,
\qquad
\tilde\Pi_\pm^{*}=\tilde\Pi_\pm .
$$

These are the canonical Hermitian idempotents of *The N-Degenerate, Spectrally Degenerate Sector*. They satisfy

$$
\tilde\Pi_+\tilde\nu=\tilde\nu,
\qquad
\tilde\nu\tilde\Pi_+=0,
\qquad
\tilde\Pi_-\tilde\nu=0,
\qquad
\tilde\nu\tilde\Pi_-=\tilde\nu .
$$

Thus $\tilde\nu=\tilde\Pi_+\tilde\nu\tilde\Pi_-$ lies in the mixed corner $\mathbb{B}_{+-}$ of the pair, and it is annihilated by the two products that would put it in a diagonal corner. In particular

$$
\langle\tilde\nu\rangle_{\natural}
=\operatorname{Sc}(\tilde\nu^{2})=0,
\qquad
\langle\tilde\nu\rangle_{*}
=\operatorname{Sc}(\tilde\nu\tilde\nu^{*})=2a^{2},
\qquad
\tilde\nu\tilde\nu^{*}=4a^{2}\tilde\Pi_+,
\qquad
\tilde\nu^{*}\tilde\nu=4a^{2}\tilde\Pi_- .
$$

### The polar pair on the nilpotents

With $a=\sqrt{\langle\tilde\nu\rangle_{*}/2}$, the polar pair is

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

The Hermitian factor is positive semidefinite of rank one and spectrum $\{0,2a\}$. The partial-isometry factor is nilpotent:

$$
\tilde Q_0\tilde Q_0^{*}=\tilde\Pi_+,
\qquad
\tilde Q_0^{*}\tilde Q_0=\tilde\Pi_-,
\qquad
\tilde Q_0\tilde Q_0^{*}\tilde Q_0=\tilde Q_0,
\qquad
\tilde Q_0^{2}=0 .
$$

A nilpotent partial isometry is not a contradiction: the Jordan block $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ is a partial isometry and squares to zero. The polar pair is the rank-one singular value decomposition of the nilpotent; the "$*$-unitary" factor is a nilpotent partial isometry.

### The matrix model

In the matrix model $\mathsf M_2(e_t)=I_2$, $\mathsf M_2(\vec e_k)=-i\sigma_k$. The null element is a rank-one matrix,

$$
\mathsf M_2(\tilde\nu)=2a\,u v^{\dagger},
\qquad
v^{\dagger}u=\frac{Q_t}{a}=0,
\qquad
u^{\dagger}u=v^{\dagger}v=1,
\qquad
u\perp v .
$$

The two singular vectors are orthogonal; this is the matrix form of the spectral degeneracy. The polar factors are

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

The overlap $v^{\dagger}u=Q_t/a$ vanishes exactly on $\Sigma_{00}$. On $\Sigma_{01}$ it was $1/\sqrt{\kappa}\neq0$; the wall is the orthogonality of the two slots.

### The standard nilpotent

For

$$
\tilde\nu=\vec e_x+i\vec e_y,
$$

one has $a=1$, $\vec c=\vec e_z$, and

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

The singular value is $2$, the only eigenvalue is $0$, and the two singular vectors may be taken as $u=(1,0)$ and $v=(0,i)$, which are orthogonal.

## The One-Sided Operators

The composition laws, the rank and the singular values are the same on the two strata; the spectrum and the Jordan type are not. The composition laws are

$$
L_{\tilde Q}\circ L_{\tilde Q'}=L_{\tilde Q\tilde Q'},\qquad R_{\tilde Q}\circ R_{\tilde Q'}=R_{\tilde Q'\tilde Q},\qquad L_{\tilde Q}\circ R_{\tilde Q'}=R_{\tilde Q'}\circ L_{\tilde Q},
$$

and both operators are invertible exactly when $\tilde Q$ is invertible, which on the null cone never happens. Rank two, kernel of dimension two and image of dimension two therefore hold throughout the sector.

### Elementary properties on the idempotent multiples

**Proposition.** Let $\tilde Q,\tilde Q'\in\mathbb{B}$. Then:

**(a)** $L_{\tilde Q}$ and $R_{\tilde Q}$ are $\mathbb{C}$-linear;

**(b)** $L_{\tilde Q}\circ L_{\tilde Q'}=L_{\tilde Q\tilde Q'}$ and $R_{\tilde Q}\circ R_{\tilde Q'}=R_{\tilde Q'\tilde Q}$;

**(c)** $L_{\tilde Q}\circ R_{\tilde Q'}=R_{\tilde Q'}\circ L_{\tilde Q}$;

**(d)** the parameter maps are injective;

**(e)** $L_{\tilde Q}$ and $R_{\tilde Q}$ are invertible exactly when $\tilde Q$ is invertible.

On $\Sigma_{01}$ the element is a zero divisor, so neither operator is invertible. The properties are those of *Operators of the Polar Word: The Common Framework*; the sector only changes the values.

### The projection up to scale

Let $\tilde Q=c\tilde\Pi$. Since $\tilde\Pi^{2}=\tilde\Pi$,

$$
L_{\tilde Q}=c\,L_{\tilde\Pi},\qquad
L_{\tilde\Pi}^{2}=L_{\tilde\Pi},\qquad
L_{\tilde Q}^{2}=c\,L_{\tilde Q},
$$

and the same identities hold on the right,

$$
R_{\tilde Q}=c\,R_{\tilde\Pi},\qquad
R_{\tilde\Pi}^{2}=R_{\tilde\Pi},\qquad
R_{\tilde Q}^{2}=c\,R_{\tilde Q}.
$$

Thus $L_{\tilde Q}/c$ and $R_{\tilde Q}/c$ are projections of the operator space. They are not orthogonal projections unless $\tilde\Pi$ is Hermitian; their singular values are $\sqrt{\kappa}$, not one.

**Theorem (rank, spectrum and Jordan form).** On $\Sigma_{01}$:

**(a)** $L_{\tilde Q}$ and $R_{\tilde Q}$ have complex rank $2$;

**(b)** their spectrum is $\{c,0\}$, with algebraic multiplicities $2$ and $2$, and geometric multiplicities $2$ and $2$;

**(c)** they are diagonalizable, with minimal polynomial $X(X-c)$;

**(d)** $\operatorname{tr}L_{\tilde Q}=\operatorname{tr}R_{\tilde Q}=4Q_t=2c$ and $\det L_{\tilde Q}=\det R_{\tilde Q}=0$;

**(e)** for every $\tilde X$, $\langle L_{\tilde Q}\tilde X\rangle_{\natural}=\langle R_{\tilde Q}\tilde X\rangle_{\natural}=0$; both images lie on the null cone.

*Proof.* In the matrix model, $\mathsf M_2(\tilde Q)=c\,\mathsf M_2(\tilde\Pi)$ with $\mathsf M_2(\tilde\Pi)$ a rank-one idempotent. Left multiplication is $X\mapsto \mathsf M_2(\tilde Q)X$, which is the tensor product $\mathsf M_2(\tilde Q)\otimes I_2$. The eigenvalues of $\mathsf M_2(\tilde Q)$ are $c$ and $0$, each repeated twice under the tensor product; the rank of $\mathsf M_2(\tilde Q)$ is one, so the rank of the left multiplication is $1\cdot2=2$. The minimal polynomial of the idempotent is $X(X-1)$; scaling by $c$ gives $X(X-c)$, which is squarefree, so the operator is diagonalizable. The trace is $2\operatorname{tr}\mathsf M_2(\tilde Q)=2c=4Q_t$, and the determinant is $(\det\mathsf M_2(\tilde Q))^{2}=0$. The norm is multiplicative, and $\langle\tilde Q\rangle_{\natural}=0$.

The rank is the same as on $\Sigma_{00}$, where the operator is nilpotent; the difference between the two sectors is the Jordan type, not the rank. The rank is governed by the vanishing of the norm, the Jordan type by the vanishing of $B^{2}$.

### The image and the kernel

The spectral pair of $\tilde Q$ is $(\tilde\Pi,\tilde\Pi')$. Let

$$
\mathbb{B}_{st}=e_s\mathbb{B}e_t,\qquad s,t\in\{+,-\},\qquad e_+=\tilde\Pi,\quad e_-=\tilde\Pi',
$$

be the four Peirce corners; each is one-dimensional. Choose nilpotents $\vec\Upsilon_-\in\mathbb{B}_{+-}$ and $\vec\Upsilon_+\in\mathbb{B}_{-+}$ with $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi$ and $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi'$. In the eigenbasis $(\tilde\Pi,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi')$ the one-sided operators are diagonal:

$$
\boxed{\;
\mathsf M\bigl(L_{\tilde Q}\bigr)=\operatorname{diag}(c,c,0,0),\qquad
\mathsf M\bigl(R_{\tilde Q}\bigr)=\operatorname{diag}(c,0,c,0).
\;}
$$

Hence

$$
\operatorname{im}L_{\tilde Q}=\mathbb{C}\tilde\Pi\oplus\mathbb{C}\vec\Upsilon_-,
\qquad
\ker L_{\tilde Q}=\mathbb{C}\vec\Upsilon_+\oplus\mathbb{C}\tilde\Pi',
$$

$$
\operatorname{im}R_{\tilde Q}=\mathbb{C}\tilde\Pi\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
\ker R_{\tilde Q}=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi'.
$$

The kernel of $L_{\tilde Q}$ is the right annihilator $A(\tilde Q)=\{\tilde X:\tilde Q\tilde X=0\}$, and the kernel of $R_{\tilde Q}$ is the left annihilator $B(\tilde Q)=\{\tilde X:\tilde X\tilde Q=0\}$. The two annihilators are distinct planes; they meet in the line $\mathbb{C}\tilde\Pi'$ of the kernel projector. The image of $L_{\tilde Q}$ is the right ideal $\tilde Q\mathbb{B}$, and the image of $R_{\tilde Q}$ is the left ideal $\mathbb{B}\tilde Q$. The image is a totally isotropic plane: for $\tilde X=\tilde Q\tilde Y$,

$$
\langle\tilde X\rangle_{\natural}
=\langle\tilde Q\rangle_{\natural}\langle\tilde Y\rangle_{\natural}=0 .
$$

The direct-sum decompositions

$$
\mathbb{B}=\operatorname{im}L_{\tilde Q}\oplus\ker L_{\tilde Q}
=\operatorname{im}R_{\tilde Q}\oplus\ker R_{\tilde Q}
$$

hold because $L_{\tilde Q}/c$ and $R_{\tilde Q}/c$ are projections.

### Singular values

The operator $L_{\tilde Q}$ is $c$ times the idempotent operator $L_{\tilde\Pi}$. The latter is not a partial isometry unless $\tilde\Pi$ is Hermitian. Its singular values are $\sqrt{\kappa}$ (twice) and $0$ (twice), because

$$
L_{\tilde\Pi}L_{\tilde\Pi}^{*}=L_{\tilde\Pi\tilde\Pi^{*}},
\qquad
\tilde\Pi\tilde\Pi^{*}=\kappa P,
$$

and $L_P$ is an orthogonal projection of rank two. Hence the singular values of $L_{\tilde Q}$ are $\lvert c\rvert\sqrt{\kappa}=2a$ (twice) and $0$ (twice). The same holds for $R_{\tilde Q}$. The non-zero singular value $2a$ is the singular value of the element $\tilde Q$ itself; the one-sided operator repeats it twice.

### The square, the rank and the spectrum

**Theorem.** On $\Sigma_{00}$:

**(a)** $L_{\tilde\nu}^{2}=0$ and $R_{\tilde\nu}^{2}=0$;

**(b)** $L_{\tilde\nu}$ and $R_{\tilde\nu}$ have complex rank $2$;

**(c)** their only eigenvalue is $0$, with algebraic multiplicity $4$ and geometric multiplicity $2$;

**(d)** their Jordan form is $J_2(0)\oplus J_2(0)$, with minimal polynomial $X^{2}$;

**(e)** $\operatorname{tr}L_{\tilde\nu}=\operatorname{tr}R_{\tilde\nu}=0$ and $\det L_{\tilde\nu}=\det R_{\tilde\nu}=0$;

**(f)** for every $\tilde X$, $\langle L_{\tilde\nu}\tilde X\rangle_{\natural}=\langle R_{\tilde\nu}\tilde X\rangle_{\natural}=0$; both images lie on the null cone.

*Proof.* The square is $L_{\tilde\nu}^{2}=L_{\tilde\nu^{2}}=L_0=0$, and similarly on the right. In the matrix model, $\mathsf M_2(\tilde\nu)=2a\,u v^{\dagger}$ is a rank-one nilpotent. Left multiplication is $X\mapsto 2a\,u v^{\dagger}X$; its image is $\{u w^{\dagger}:w\in\mathbb{C}^{2}\}$, of dimension two, and its kernel is $\{X:v^{\dagger}X=0\}$, also of dimension two. Since the square is zero, the image is contained in the kernel, and the two dimensions are equal, so the image equals the kernel. The eigenvalues of left multiplication by a matrix are the eigenvalues of the matrix, each repeated twice; the only eigenvalue of $2a\,u v^{\dagger}$ is $0$, so the algebraic multiplicity is four. The geometric multiplicity is the dimension of the kernel, two. The minimal polynomial is $X^{2}$ because the operator is non-zero and squares to zero. The trace is $2\operatorname{tr}\mathsf M_2(\tilde\nu)=0$, and the determinant is $(\det\mathsf M_2(\tilde\nu))^{2}=0$. The norm is multiplicative and $\langle\tilde\nu\rangle_{\natural}=0$.
The same arguments apply to the right multiplication $X\mapsto 2a\,X u v^{\dagger}$.

### The image and the kernel on the nilpotents

The image and the kernel of $L_{\tilde\nu}$ coincide, and likewise for $R_{\tilde\nu}$. The two common planes are distinct and meet in the line of the nilpotent.

**Proposition (the two planes).** On $\Sigma_{00}$,

$$
\boxed{\;
\operatorname{im}L_{\tilde\nu}
=\ker L_{\tilde\nu}
=\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_+,
\qquad
\operatorname{im}R_{\tilde\nu}
=\ker R_{\tilde\nu}
=\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_- .
\;}
$$

The two planes are distinct and

$$
\bigl(\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_+\bigr)
\cap
\bigl(\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_-\bigr)
=\mathbb{C}\tilde\nu .
$$

*Proof.* The multiplications by the canonical idempotents give

$$
\tilde\nu\tilde\Pi_+=0,
\qquad
\tilde\nu\tilde\Pi_-=\tilde\nu,
\qquad
\tilde\Pi_+\tilde\nu=\tilde\nu,
\qquad
\tilde\Pi_-\tilde\nu=0 .
$$

Hence $L_{\tilde\nu}(\tilde\Pi_+)=0$ and $L_{\tilde\nu}(\tilde\Pi_-)=\tilde\nu$, so the image contains $\mathbb{C}\tilde\nu$ and $\mathbb{C}\tilde\Pi_+$ after one more step: the corner vector $\vec X$ of §*The Peirce Matrices* satisfies $\tilde\nu\vec X\in\mathbb{C}\tilde\Pi_+$. The image is therefore the plane $\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_+$; the kernel contains the same plane by the square-zero property, and the dimensions agree. The right-hand statement is the mirror, using $\tilde\Pi_+\tilde\nu=\tilde\nu$ and $\tilde\Pi_-\tilde\nu=0$. The intersection is the common line $\mathbb{C}\tilde\nu$ because $\tilde\Pi_+$ and $\tilde\Pi_-$ are independent modulo $\tilde\nu$.

The image planes are totally isotropic: for $\tilde X=\tilde\nu\tilde Y$,

$$
\langle\tilde X\rangle_{\natural}
=\langle\tilde\nu\rangle_{\natural}\langle\tilde Y\rangle_{\natural}=0 .
$$

The kernels are the same planes, so the operator does not split the algebra into an image and a complement: the image is contained in the kernel, and the algebra is a non-trivial extension. This is the operator form of the absence of a spectral decomposition.

### The Peirce matrices

Let $\tilde\Pi_\pm$ be the canonical Hermitian idempotents. Choose a non-zero corner vector

$$
\vec X\in\tilde\Pi_-\mathbb{B}\tilde\Pi_+,
$$

and normalize it so that

$$
\tilde\nu\vec X=\tilde\Pi_+,
\qquad
\vec X\tilde\nu=\varkappa\,\tilde\Pi_-,
\qquad
\varkappa\neq0 .
$$

In the standard example one may take $\varkappa=1$. The four elements

$$
\bigl(\tilde\Pi_+,\ \tilde\nu,\ \vec X,\ \tilde\Pi_-\bigr)
$$

form a basis, the canonical Jordan basis of *The Jordan Basis of a Spectrally Degenerate Biquaternion*, with the Peirce form purely off-diagonal:

$$
\tilde\nu=\tilde\Pi_+\tilde\nu\tilde\Pi_-,
\qquad
\tilde\Pi_\pm\tilde\nu\tilde\Pi_\pm=0,
\qquad
\tilde\Pi_\pm\tilde\nu\tilde\Pi_\mp=0 \text{ except } \tilde\Pi_+\tilde\nu\tilde\Pi_-=\tilde\nu .
$$

The one-sided operators have the matrices

$$
\boxed{\;
\mathsf M\bigl(L_{\tilde\nu}\bigr)=
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
\qquad
\mathsf M\bigl(R_{\tilde\nu}\bigr)=
\begin{pmatrix}
0&0&0&0\\
1&0&0&0\\
0&0&0&0\\
0&0&\varkappa&0
\end{pmatrix}.
\;}
$$

The columns are the images of the basis vectors:

$$
L_{\tilde\nu}:\quad
\tilde\Pi_+\mapsto0,\quad
\tilde\nu\mapsto0,\quad
\vec X\mapsto\tilde\Pi_+,\quad
\tilde\Pi_-\mapsto\tilde\nu,
$$

$$
R_{\tilde\nu}:\quad
\tilde\Pi_+\mapsto\tilde\nu,\quad
\tilde\nu\mapsto0,\quad
\vec X\mapsto\varkappa\tilde\Pi_-,\quad
\tilde\Pi_-\mapsto0 .
$$

The Jordan chains are therefore

$$
L_{\tilde\nu}:\quad
\vec X\to\tilde\Pi_+\to0,
\qquad
\tilde\Pi_-\to\tilde\nu\to0,
$$

$$
R_{\tilde\nu}:\quad
\tilde\Pi_+\to\tilde\nu\to0,
\qquad
\vec X\to\varkappa\tilde\Pi_-\to0 .
$$

Each operator has two chains of length two. The chain starts are the two directions outside the common image plane; the chain ends are the two directions inside it.

## The Polar Pair, One-Sided

On both strata the operator is a scalar times the operator of the partial isometry, and the scalar is the non-zero singular value. The factor $2a$ acts as the scalar on the image, so the collapse is exact rather than approximate.

### The scalar collapse on the idempotent multiples

By the polar pair theorem, $\tilde Q=2a\tilde Q_0$ and $\tilde Q_0$ is a partial isometry. The composition laws give

$$
\boxed{\;
L_{\tilde Q}=2a\,L_{\tilde Q_0},\qquad
R_{\tilde Q}=2a\,R_{\tilde Q_0}.
\;}
$$

The operators $L_{\tilde Q_0}$ and $R_{\tilde Q_0}$ are partial isometries of the operator space:

$$
L_{\tilde Q_0}L_{\tilde Q_0}^{*}L_{\tilde Q_0}
=L_{\tilde Q_0\tilde Q_0^{*}\tilde Q_0}
=L_{\tilde Q_0},
$$

and similarly on the right. Hence **the one-sided operator is $2a$ times a partial isometry**. Its non-zero singular value is $2a$, twice, and its rank is two.

The canonical left polar factor of $L_{\tilde Q}$ is $\lvert L_{\tilde Q}\rvert=(L_{\tilde Q}L_{\tilde Q}^{*})^{1/2}=L_{\tilde Q_H}=2aL_P$, which is positive semidefinite of rank two. On the image of $L_{\tilde Q_0}$ it acts as the scalar $2a$, because $P\tilde Q_0=\tilde Q_0$ and therefore $L_PL_{\tilde Q_0}=L_{\tilde Q_0}$. This is the **scalar collapse** of the polar pair: the positive factor is not a scalar globally, but the product only sees its value $2a$ on the image. The factorisation $L_{\tilde Q}=L_{\tilde Q_H}L_{\tilde Q_0}$ remains the polar decomposition of the operator; the simplified form $L_{\tilde Q}=2aL_{\tilde Q_0}$ is its scalar reduction.

The same statements hold on the right, with the order reversed:

$$
R_{\tilde Q}=R_{\tilde Q_0}R_{\tilde Q_H}=2a\,R_{\tilde Q_0}.
$$

### The phase

The partial-isometry factor is

$$
\tilde Q_0=\frac{c}{\lvert c\rvert}\frac{\tilde\Pi}{\sqrt{\kappa}}.
$$

The phase $c/\lvert c\rvert$ is carried by $\tilde Q_0$; the modulus $2a=\lvert c\rvert\sqrt{\kappa}$ is the scalar. The one-sided operator therefore keeps the phase. The two-sided operator of the companion article keeps only $\lvert c\rvert^{2}$ and cancels the phase.

When $\tilde\Pi$ is Hermitian, $\kappa=1$ and $\tilde Q_0=(c/\lvert c\rvert)\tilde\Pi$. Then $L_{\tilde Q}=cL_{\tilde\Pi}$ with $L_{\tilde\Pi}$ an orthogonal projection, and the clean word is a scale $c$ times a projection. When $\tilde\Pi$ is not Hermitian, $L_{\tilde\Pi}$ is only $\sqrt{\kappa}$ times a partial isometry; the scalar collapse through $\tilde Q_0$ is the correct statement. The non-Hermitian example of §*Worked Examples* shows the difference.

### The modulus and the singular value

The element modulus is $\varrho\,e^{i\theta_{\mathrm{pha}}}=\sqrt{\langle\tilde Q\rangle_{\natural}}=0$. The number $2a$ is not a modulus in that sense: it is the non-zero singular value of $\tilde Q$ in the matrix model, equivalently the non-zero spectral value of the Hermitian factor $\tilde Q_H$. The operator $L_{\tilde Q}$ is singular, but it is not the zero operator: it has rank two and non-zero singular value $2a$. The vanishing of $\varrho\,e^{i\theta_{\mathrm{pha}}}$ says that the element is a zero divisor; it does not say that the operator is nilpotent. On $\Sigma_{00}$, where $B^{2}=0$ and $Q_t=0$, the operator is nilpotent; on $\Sigma_{10}$, where $Q_t\neq0$, it is unipotent instead.

### The phase and the sign

For a complex multiple

$$
\tilde\nu=c_0(\vec e_x+i\vec e_y),
\qquad
c_0=\lvert c_0\rvert e^{i\beta},
$$

one has $a=\lvert c_0\rvert$ and

$$
\tilde Q_0=\frac{c_0}{\lvert c_0\rvert}\frac{\vec e_x+i\vec e_y}{2},
\qquad
\tilde Q_H=2\lvert c_0\rvert\,\tilde\Pi_+,
\qquad
\tilde\Pi_+=\frac{e_t+i\vec e_z}{2}.
$$

The phase $e^{i\beta}$ is carried by $\tilde Q_0$ and by $L_{\tilde\nu}$; the scalar $2a=2\lvert c_0\rvert$ is positive. The nilpotent direction $\vec e_x+i\vec e_y$ is unchanged. The two-sided operator of the companion article sees only $\lvert c_0\rvert$ and the canonical pair; the phase cancels. The sign $\tilde\nu\mapsto-\tilde\nu$ is also carried by $\tilde Q_0$; the scalar $2a$ is unchanged.

### The modulus and the singular value on the nilpotents

The element modulus is zero, while the operator has rank two and non-zero singular value $2a$. The vanishing of the norm says that the element is a null vector and that both multiplications have a non-trivial kernel; it does not say that the operator is zero. The spectral degeneration $B^{2}=0$ makes the operator nilpotent; the norm degeneration makes its rank two. The two defects are independent.

## The Eigenbasis and the Two Spinor Spaces on the Idempotent Multiples

Since $B^{2}\neq0$, the eigenbasis of *The Eigenbasis of a Spectrally Regular Biquaternion* exists. Its spectral projectors are $\tilde\Pi$ and $\tilde\Pi'$, and the Peirce form of $\tilde Q$ is

$$
\tilde\Pi\tilde Q\tilde\Pi=c\tilde\Pi,\qquad
\tilde\Pi\tilde Q\tilde\Pi'=0,\qquad
\tilde\Pi'\tilde Q\tilde\Pi=0,\qquad
\tilde\Pi'\tilde Q\tilde\Pi'=0.
$$

In the eigenbasis the one-sided operators are the diagonal matrices displayed in §*The Image and the Kernel*. The two chiral spinor spaces are

$$
S_+=\mathbb{B}\tilde\Pi=\mathbb{C}\tilde\Pi\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}\tilde\Pi'=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi',
\qquad
\mathbb{B}=S_+\oplus S_- .
$$

On each chirality, left multiplication by $\tilde Q$ has the matrix $\operatorname{diag}(c,0)$; right multiplication is $c$ on $S_+$ and $0$ on $S_-$. The zero eigenvalue is a value on a component, not a missing direction. This is the specialisation to $\Sigma_{01}$ of the spinorial reading of *The N-Degenerate, Spectrally Regular Sector*, §*Spinors and Chirality*. The reading is spinorial in the module sense, not in the little-group sense: the generator is a scaled projection rather than a rotor or a boost, so there is no half-angle to read and the half-angle theorem of the regular sector does not apply.

In the matrix model the two slots are the singular vectors $u$ and $v$. The left multiplication $L_{\tilde Q}$ writes on the left slot $u$ and reads the right covector $v^{\dagger}$; the right multiplication reads the $u$-component and writes on the $v$-slot. The one-sided operator sees the complex overlap $v^{\dagger}u=Q_t/a$. Its eigenvalue is $c=2a\,v^{\dagger}u$, twice. The modulus of the overlap is $\cos\theta=1/\sqrt{\kappa}$; the phase of the overlap is the phase of $c$. The two-sided operator of the companion article sees only the squared modulus $\cos^{2}\theta$; this is the precise form of the one-sided/two-sided contrast in this sector.

## The Exponential

On both strata the exponential of the singular operator is invertible for every $t\neq0$. The rates differ: the one-sided rate is $c$ on $\Sigma_{01}$, and on $\Sigma_{00}$ the unipotent flow removes the norm degeneration while preserving the spectral one.

### The exponential on the idempotent multiples

**The operator exponential.** Since $L_{\tilde Q}=cL_{\tilde\Pi}$ and $L_{\tilde\Pi}^{2}=L_{\tilde\Pi}$,

$$
\boxed{\;
\exp\bigl(tL_{\tilde Q}\bigr)
=I+\bigl(e^{tc}-1\bigr)L_{\tilde\Pi}
\;}
$$

for every complex $t$, and the same formula holds for $R_{\tilde Q}$. The eigenvalues of $\exp(tL_{\tilde Q})$ are $e^{tc}$ (twice) and $1$ (twice); the determinant is $e^{2tc}$. The group is a line of projections interpolating between the identity and the kernel projection. It is invertible for every $t$, even though $L_{\tilde Q}$ is singular.

**The element exponential.** Since $\tilde Q=c\tilde\Pi$ and $\tilde\Pi^{2}=\tilde\Pi$,

$$
\exp\bigl(t\tilde Q\bigr)
=e_t+\bigl(e^{tc}-1\bigr)\tilde\Pi .
$$

The quaternionic norm of the exponential is

$$
\bigl\langle\exp(t\tilde Q)\bigr\rangle_{\natural}
=e^{tc},
$$

because $\tilde\Pi^{\natural}=\tilde\Pi'$ and $\tilde\Pi\tilde\Pi'=0$. The exponential is invertible for every $t$. Its $B^{2}$ is $-\tfrac14(e^{tc}-1)^{2}$, which is non-zero for generic $t\neq0$; it vanishes exactly when $e^{tc}=1$, where the exponential is $e_t$ on the wall $\Sigma_{10}$. Hence the flow lies in the doubly regular sector $\Sigma_{11}$ for generic $t\neq0$. For generic $t$, a zero divisor of $\Sigma_{01}$ has an exponential that is invertible with distinct eigenvalues. The one-sided rate is $c$; the two-sided rate of the companion article is $\lvert c\rvert^{2}$.

### The exponential on the nilpotents

**The operator exponential.** Since $L_{\tilde\nu}^{2}=0$,

$$
\boxed{\;
\exp\bigl(tL_{\tilde\nu}\bigr)=I+tL_{\tilde\nu}
\;}
$$

for every complex $t$, and the same formula holds for $R_{\tilde\nu}$. The eigenvalues are all $1$; the Jordan form is $J_2(1)\oplus J_2(1)$; the determinant is $1$. The group is unipotent: it is a shear, not a dilation. It is invertible for every $t$, although the generator $L_{\tilde\nu}$ is nilpotent and singular.

**The element exponential.** Since $\tilde\nu^{2}=0$,

$$
\exp\bigl(t\tilde\nu\bigr)=e_t+t\tilde\nu .
$$

The quaternionic norm is

$$
\bigl\langle\exp(t\tilde\nu)\bigr\rangle_{\natural}=1,
$$

and the vector form is

$$
B^{2}\bigl(\exp(t\tilde\nu)\bigr)=t^{2}B^{2}(\tilde\nu)=0 .
$$

Hence the exponential is invertible with $B^{2}=0$: for every $t$ it lies in the N-regular, spectrally degenerate sector $\Sigma_{10}$ (at $t=0$ it is $e_t$), not in the doubly regular sector. This is the mirror of the generic $\Sigma_{01}$ flow, which leaves both walls and lies in $\Sigma_{11}$. The exponential moves the element one wall away: it removes the norm degeneration and preserves the spectral one.

The one-sided operator exponential is unipotent with two Jordan blocks of size two at eigenvalue one; this is the operator type of the N-regular, spectrally degenerate one-sided operator of *One-Sided Operators on the N-Regular Sector*. The two-sided companion is a unipotent Lorentz flow of Jordan type $2+1+1$. The one-sided exponential is a shear of the operator space, not a Lorentz transformation.

## Worked Examples

Two examples on each stratum, the second at the boundary of its canonical form.

### Example 1: a Hermitian idempotent

Take

$$
\tilde Q=e_t+i\vec e_x .
$$

Then $c=2$, $\tilde\Pi=(e_t+i\vec e_x)/2$, $\kappa=1$, $a=1$, $P=\tilde\Pi$, and

$$
\tilde Q_H=\tilde Q,\qquad \tilde Q_0=\tilde\Pi .
$$

The element is twice the partial isometry $\tilde\Pi$ (a Hermitian idempotent scaled by $2$): $\tilde Q^{2}=2\tilde Q$. The matrix model is

$$
\mathsf M_2(\tilde Q)=
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
$$

In the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ the left multiplication is

$$
\mathsf M\bigl(L_{\tilde Q}\bigr)=
\begin{pmatrix}
1&-i&0&0\\
i&1&0&0\\
0&0&1&-i\\
0&0&i&1
\end{pmatrix},
$$

with eigenvalues $2,2,0,0$, rank two, trace $4$ and determinant zero. The singular values are $2,2,0,0$. The exponential is

$$
\exp\bigl(tL_{\tilde Q}\bigr)=I+\bigl(e^{2t}-1\bigr)L_{\tilde\Pi}.
$$

### Example 2: a non-Hermitian idempotent

Take

$$
\tilde Q=e_t+\vec e_x+i\sqrt2\,\vec e_z .
$$

Then $c=2$, $\tilde\Pi=(e_t+\vec e_x+i\sqrt2\,\vec e_z)/2$, $\tilde{Ζ}=\vec e_x+i\sqrt2\,\vec e_z$, $\kappa=2$, $a=\sqrt2$. The idempotent is not Hermitian; its Hermitian projection is

$$
P=\frac{\tilde\Pi\tilde\Pi^{*}}{\kappa}
=\frac12 e_t-\frac{i\sqrt2}{4}\vec e_y+\frac{i\sqrt2}{4}\vec e_z,
$$

and

$$
\tilde Q_H=\sqrt2\,e_t-i\vec e_y+i\vec e_z,
\qquad
\tilde Q_0=\frac{\sqrt2}{4}e_t+\frac{\sqrt2}{4}\vec e_x+\frac{i}{2}\vec e_z .
$$

The element is not Hermitian, $\tilde Q^{*}\neq\tilde Q$, and its Hermitian factor is not $\tilde Q$: $\tilde Q_H\neq\tilde Q$. The partial-isometry factor satisfies $\tilde Q_0^{2}=\tfrac{1}{\sqrt2}\tilde Q_0$; the scalar $1/\sqrt2=1/\sqrt\kappa$ has modulus less than one, and the idempotent $\tilde\Pi$ is oblique, with $\kappa=2$. The one-sided operator is

$$
L_{\tilde Q}=2L_{\tilde\Pi}=2\sqrt2\,L_{\tilde Q_0},
$$

with eigenvalues $2,2,0,0$ and singular values $2\sqrt2,2\sqrt2,0,0$. The example shows that the scalar collapse uses the partial isometry $\tilde Q_0$, not the idempotent $\tilde\Pi$, and that the non-zero singular value $2a$ can be strictly larger than the eigenvalue modulus $\lvert c\rvert$.

### Example 3: the standard nilpotent

For

$$
\tilde\nu=\vec e_x+i\vec e_y,
$$

one has $a=1$, $\vec c=\vec e_z$, and

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

The singular value is $2$, the only eigenvalue is $0$, and the two singular vectors may be taken as $u=(1,0)$ and $v=(0,i)$, which are orthogonal.

### Example 4: a complex scalar multiple

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
\tilde Q_H=2\lvert c_0\rvert\,\tilde\Pi_+,
\qquad
L_{\tilde\nu}=2\lvert c_0\rvert\,L_{\tilde Q_0}.
$$

The phase $e^{i\beta}$ is in $\tilde Q_0$; the singular value $2\lvert c_0\rvert$ is positive and phase-blind. The two-sided operator of the companion article is $4\lvert c_0\rvert^{2}\mathrm{Sd}_{\tilde Q_0}$, also phase-blind. This is the cleanest illustration of the one-sided/two-sided contrast in the sector.

## Summary

### Main Results on the Idempotent Multiples

| item | value |
|---|---|
| sector | $\Sigma_{01}=\{\langle\tilde Q\rangle_{\natural}=0,\ B^{2}\neq0\}$ |
| parameter | $\tilde Q=c\tilde\Pi$, $c=2Q_t\neq0$, $\tilde\Pi^{2}=\tilde\Pi$ |
| polar pair | $\tilde Q=2a\tilde Q_0$, $\tilde Q_H=2aP$, $P=\tilde Q\tilde Q^{*}/(4a^{2})$ |
| scalar | $a=\sqrt{\langle\tilde Q\rangle_{*}/2}=\lvert c\rvert\sqrt{\kappa}/2$ |
| partial isometry | $\tilde Q_0=\tilde Q/(2a)=(c/\lvert c\rvert)\tilde\Pi/\sqrt{\kappa}$ |
| overlap | $v^{\dagger}u=Q_t/a=c/(2a)$, $\lvert v^{\dagger}u\rvert=1/\sqrt{\kappa}$ |
| one-sided operators | $L_{\tilde Q}=cL_{\tilde\Pi}$, $R_{\tilde Q}=cR_{\tilde\Pi}$ |
| squares | $L_{\tilde Q}^{2}=cL_{\tilde Q}$, $R_{\tilde Q}^{2}=cR_{\tilde Q}$ |
| rank | $2$ for both |
| spectrum | $\{c,0\}$, algebraic multiplicities $2,2$, geometric multiplicities $2,2$ |
| Jordan form | diagonal, $\operatorname{diag}(c,c,0,0)$ and $\operatorname{diag}(c,0,c,0)$ |
| trace | $4Q_t=2c$ |
| the determinant of the image | $0$ |
| singular values | $2a$ (twice), $0$ (twice) |
| image | $\tilde Q\mathbb{B}$ and $\mathbb{B}\tilde Q$, totally isotropic planes |
| kernel | the annihilator planes, meeting in $\mathbb{C}\tilde\Pi'$ |
| scalar collapse | $L_{\tilde Q}=2aL_{\tilde Q_0}$, $R_{\tilde Q}=2aR_{\tilde Q_0}$ |
| exponential | $\exp(tL_{\tilde Q})=I+(e^{tc}-1)L_{\tilde\Pi}$ |
| element flow | $\exp(t\tilde Q)=e_t+(e^{tc}-1)\tilde\Pi$, a unit in $\Sigma_{11}$ for generic $t\neq0$ |

### Main Results on the Nilpotents

| item | value |
|---|---|
| sector | $\Sigma_{00}=\{\langle\tilde Q\rangle_{\natural}=0,\ B^{2}=0\}$ |
| parameter | $\tilde\nu=\vec A+i\vec B$, $\lVert\vec A\rVert=\lVert\vec B\rVert=a>0$, $\vec A\cdot\vec B=0$ |
| canonical pair | $\tilde\Pi_\pm=(e_t\pm i\vec c)/2$, $\vec c=\vec A\times\vec B/a^{2}$ |
| polar pair | $\tilde Q_H=2a\tilde\Pi_+$, $\tilde Q_0=\tilde\nu/(2a)$, $\tilde Q_0^{2}=0$ |
| one-sided operators | $L_{\tilde\nu}$, $R_{\tilde\nu}$ |
| squares | $L_{\tilde\nu}^{2}=0$, $R_{\tilde\nu}^{2}=0$ |
| rank | $2$ for both |
| spectrum | $\{0\}$, algebraic multiplicity $4$, geometric multiplicity $2$ |
| Jordan form | $J_2(0)\oplus J_2(0)$ |
| trace | $0$ |
| the determinant of the image | $0$ |
| singular values | $2a$ (twice), $0$ (twice) |
| image | $\operatorname{im}L_{\tilde\nu}=\ker L_{\tilde\nu}=\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_+$ |
| mirror | $\operatorname{im}R_{\tilde\nu}=\ker R_{\tilde\nu}=\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_-$ |
| intersection | the two planes meet in $\mathbb{C}\tilde\nu$ |
| scalar collapse | $L_{\tilde\nu}=2aL_{\tilde Q_0}$, $R_{\tilde\nu}=2aR_{\tilde Q_0}$ |
| exponential | $\exp(tL_{\tilde\nu})=I+tL_{\tilde\nu}$ |
| element flow | $\exp(t\tilde\nu)=e_t+t\tilde\nu$, a unit in $\Sigma_{10}$ for every $t$ (at $t=0$ it is $e_t$) |

### What the Operator Shows

The norm fixes the rank and the spectral condition fixes the defect, on both strata.

- The norm degeneration fixes the rank: on the null cone the one-sided operator has rank two, and its image is a totally isotropic plane, a left ideal for $L$ and a right ideal for $R$.
- The spectral regularity fixes the Jordan type: on $\Sigma_{01}$ the operator is a projection up to scale, not a nilpotent, and its minimal polynomial is squarefree.
- The spectral degeneration fixes the Jordan type on $\Sigma_{00}$: the operator is nilpotent with two blocks of size two and minimal polynomial $X^{2}$.
- The polar pair collapses to a scalar times a partial isometry, $L_{\tilde Q}=2aL_{\tilde Q_0}$; the positive factor acts as the scalar $2a$ on the image.
- The non-zero singular value $2a$ is the singular value of the element, repeated twice. The gap between the spectrum and the singular values is the measure of the defect, and it is largest on $\Sigma_{00}$, where the only eigenvalue is zero.
- The phase and the sign are one-sided: they sit in $\tilde Q_0$ and in the eigenvalue $c$. The two-sided operator of the companion article sees only $\lvert c\rvert^{2}$ on $\Sigma_{01}$ and $4a^{2}=(2a)^{2}$ on $\Sigma_{00}$.
- On $\Sigma_{00}$ the image equals the kernel, so there is no spectral splitting: the algebra is a non-trivial extension with kernel equal to image.
- The exponential is a line of projections on $\Sigma_{01}$ and unipotent on $\Sigma_{00}$; in both cases it removes the norm degeneration and, on $\Sigma_{01}$ generically, the spectral one as well.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde Q\rangle_{\natural}$, $\langle\tilde Q\rangle_{*}$ | the quaternionic norm $Q_t^{2}+B^{2}$, zero on the null cone, and the Hermitian norm $\operatorname{Sc}(\tilde Q\tilde Q^{*})$, positive there |
| $\tilde Q=c\tilde\Pi$ | an element of $\Sigma_{01}$ |
| $\tilde\Pi'=e_t-\tilde\Pi$ | the complementary idempotent |
| $\tilde{Ζ}=2\tilde\Pi-e_t$ | the pure root of $e_t$ |
| $\kappa=2\langle\tilde\Pi\rangle_{*}$ | the obliqueness, $\kappa\ge1$ |
| $a=\sqrt{\langle\tilde Q\rangle_{*}/2}$ | the half singular value, $2a$ the non-zero singular value |
| $P=\tilde Q\tilde Q^{*}/(4a^{2})$ | the rank-one Hermitian idempotent |
| $\tilde Q_H=2aP$ | the Hermitian factor of the polar pair |
| $\tilde Q_0=\tilde Q/(2a)$ | the partial-isometry factor |
| $L_{\tilde Q},R_{\tilde Q}$ | left and right multiplication |
| $A(\tilde Q)=\ker L_{\tilde Q}$ | the right annihilator |
| $B(\tilde Q)=\ker R_{\tilde Q}$ | the left annihilator |
| $u,v$ | the left and right singular vectors of $\mathsf M_2(\tilde Q)$ |
| $v^{\dagger}u=Q_t/a$ | the overlap of the two slots |
| $\theta$ | the angle between the slots, $\cos\theta=1/\sqrt{\kappa}$ |
| $\tilde\nu=\vec A+i\vec B$ | a non-zero element of $\Sigma_{00}$ |
| $a=\lVert\vec A\rVert=\lVert\vec B\rVert$ | the half singular value, $2a$ the non-zero singular value |
| $\vec c=\vec A\times\vec B/a^{2}$ | the unit spectral direction |
| $\tilde\Pi_\pm=(e_t\pm i\vec c)/2$ | the canonical Hermitian idempotents |
| $\tilde Q_H=2a\tilde\Pi_+$ | the Hermitian factor |
| $\tilde Q_0=\tilde\nu/(2a)$ | the nilpotent partial-isometry factor |
| $L_{\tilde\nu},R_{\tilde\nu}$ | left and right multiplication |
| $\vec X$ | a normalized corner vector, $\tilde\nu\vec X=\tilde\Pi_+$ |
| $\varkappa$ | the corner constant, $\vec X\tilde\nu=\varkappa\tilde\Pi_-$ |
| $J_2(0)$ | the nilpotent Jordan block of size two |

## Further Reading

- [Two-Sided Operators on the N-Degenerate Sector](two-sided-operators-on-the-n-degenerate-sector.html), for the two-sided operator on the same two strata.
- [One-Sided Operators on the N-Regular Sector](one-sided-operators-on-the-n-regular-sector.html), §*The Exponential of the One-Sided Operator*, for the operator exponential off the null cone, where the four-factor word exists.
- [The Polar Decomposition of an N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the two-factor polar pair used throughout.
- [Introduction to the Operators on the Four Sectors](introduction-to-the-operators-on-the-four-sectors.html), for the three operators, the doubling rule and the table of the four sectors.
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html) and [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the element-level descriptions of $\Sigma_{01}$ and $\Sigma_{00}$.
