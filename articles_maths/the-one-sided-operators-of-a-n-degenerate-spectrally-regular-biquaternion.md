# __The One-Sided Operators of a N-Degenerate, Spectrally Regular Biquaternion__

## Introduction

Throughout this article $\tilde Q$ lies in the N-degenerate, spectrally regular sector $\Sigma_{01}$, so $\langle\tilde Q\rangle_{\natural}=0$ and $B^{2}\neq0$. The sector is the set of non-zero complex multiples of non-trivial idempotents,

$$
\tilde Q=c\,\tilde\Pi,\qquad c=2Q_t\neq0,\qquad \tilde\Pi^{2}=\tilde\Pi,\qquad \tilde\Pi\neq0,e_t,
$$

as in *The N-Degenerate, Spectrally Regular Sector*. The element is a zero divisor; its spectrum is $\{c,0\}$, with distinct eigenvalues, so the spectral decomposition and the eigenbasis exist. The word **N-degenerate** refers to the vanishing of the quaternionic norm; the word **spectrally regular** to the non-vanishing of $B^{2}$.

The biquaternion algebra acts on itself by left and right multiplication,

$$
L_{\tilde Q}(\tilde X)=\tilde Q\tilde X,\qquad R_{\tilde Q}(\tilde X)=\tilde X\tilde Q .
$$

On the null cone the modulus $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$ vanishes, so the modulus–unit decomposition and the four-factor word $\tilde Q=\Rho\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ do not exist. What survives is the two-factor **polar pair**

$$
\tilde Q=\tilde Q_H\tilde Q_0,\qquad \tilde Q_H=\bigl(\tilde Q\tilde Q^{*}\bigr)^{1/2},\qquad \tilde Q_0=\tilde Q_H^{+}\tilde Q,
$$

of *The Polar Decomposition of a N-Degenerate Biquaternion*. The factor $\tilde Q_H$ is Hermitian positive semidefinite of rank one and $\tilde Q_0$ is a partial isometry. On $\Sigma_{01}$ the pair has a closed form: $\tilde Q_0$ is a scalar times the idempotent $\tilde\Pi$, and the scalar has modulus $1/\sqrt\kappa$, where $\kappa\ge1$ measures the obliqueness of $\tilde\Pi$.

The main result is that **the one-sided operator is a scalar multiple of a partial isometry**:

$$
\boxed{\;L_{\tilde Q}=2a\,L_{\tilde Q_0},\qquad R_{\tilde Q}=2a\,R_{\tilde Q_0},\qquad \tilde Q=2a\,\tilde Q_0\;}
$$

with $a=\sqrt{\langle\tilde Q\rangle_{*}/2}>0$. The scalar $2a$ is the non-zero singular value of $\tilde Q$ in the matrix model. The operator $L_{\tilde Q}$ has rank two, spectrum $\{c,c,0,0\}$ and no Jordan defect; it is a projection up to scale, not a nilpotent. The spectral wall $B^{2}=0$ is the boundary at which this projection gives way to the square-zero operator of *The One-Sided Operators of a N-Degenerate, Spectrally Degenerate Biquaternion*.

The article is organized as follows. §*The Polar Pair* proves the rank-one singular value decomposition. §*The One-Sided Operators* computes the composition laws, the rank, the spectrum, the image and the kernel. §*The Polar Pair, One-Sided* proves the scalar collapse and reads the operator through the pair. §*The Eigenbasis and the Two Slots* gives the diagonal form and the spinorial reading. §*The Exponential* computes the one-parameter group. §*Worked Examples* treats a Hermitian and a non-Hermitian idempotent. The article closes with the summary, the notation and the readings.

## The Polar Pair

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the product $\vec e_x\vec e_y=\vec e_z$ and the squares $\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t$. The scalar imaginary $i$ is central. The Hermitian conjugation is $\tilde X^{*}=\overline{\tilde X^{\natural}}$, and the Hermitian norm is

$$
\langle\tilde X\rangle_{*}=\operatorname{Sc}\bigl(\tilde X\tilde X^{*}\bigr)=\sum_{\mu\in\{t,x,y,z\}}\lvert X_\mu\rvert^{2}.
$$

It is positive definite. The quaternionic norm is $\langle\tilde X\rangle_{\natural}=\sum_\mu X_\mu^{2}$, and the vector form is $B^{2}=X_x^{2}+X_y^{2}+X_z^{2}$.

The matrix model is $\mathsf M_2:\mathbb{B}\to M_2(\mathbb{C})$, with $\mathsf M_2(e_t)=I_2$ and $\mathsf M_2(\vec e_k)=-i\sigma_k$. It is $\mathbb{C}$-linear, multiplicative, and satisfies

$$
\mathsf M_2(\tilde X^{*})=\mathsf M_2(\tilde X)^{\dagger},\qquad
\det\mathsf M_2(\tilde X)=\langle\tilde X\rangle_{\natural},\qquad
\tfrac12\operatorname{tr}\bigl(\mathsf M_2(\tilde X)\mathsf M_2(\tilde X)^{\dagger}\bigr)=\langle\tilde X\rangle_{*}.
$$

The last identity says that the Frobenius norm of $\mathsf M_2(\tilde X)$ is $\sqrt{2\langle\tilde X\rangle_{*}}$.

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

with $a>0$ and $u,v$ unit vectors of $\mathbb{C}^{2}$. The Frobenius norm is $\lVert\mathsf M_2(\tilde Q)\rVert_F^{2}=4a^{2}=2\langle\tilde Q\rangle_{*}$, hence $a=\sqrt{\langle\tilde Q\rangle_{*}/2}$. The matrix $u v^{\dagger}$ is a rank-one partial isometry, because $(u v^{\dagger})(u v^{\dagger})^{\dagger}(u v^{\dagger})=u v^{\dagger}$. Translating back gives $\tilde Q=2a\tilde Q_0$ with $\tilde Q_0=\tilde Q/(2a)$. Conversely, a non-zero rank-one partial isometry has determinant zero, hence $\langle\tilde Q\rangle_{\natural}=0$.

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

The pair $(\tilde Q_H,\tilde Q_0)$ is the general pair of *The Polar Decomposition of a N-Degenerate Biquaternion*, specialized to the rank-one case. It is not the modulus–unit pair: the modulus $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$ is zero, while $\tilde Q_H$ is a non-zero rank-one element. The number $2a$ is the non-zero singular value of $\tilde Q$; it is not an eigenvalue in general (it coincides with $c$ when $\kappa=1$ and $c>0$).

### The closed form on $\Sigma_{01}$

Let $\tilde Q=c\tilde\Pi$ with $c=2Q_t\neq0$ and $\tilde\Pi$ a non-trivial idempotent. Put

$$
\tilde\Xi=2\tilde\Pi-e_t,\qquad
\tilde\Pi'=e_t-\tilde\Pi,\qquad
\kappa=2\langle\tilde\Pi\rangle_{*}=\frac{1+\lVert\tilde\Xi\rVert_E^{2}}{2},
$$

where $\lVert\tilde\Xi\rVert_E^{2}=\lvert\Xi_x\rvert^{2}+\lvert\Xi_y\rvert^{2}+\lvert\Xi_z\rvert^{2}$. The root satisfies $\tilde\Xi^{2}=e_t$ and $\tilde\Xi\neq\pm e_t$; the idempotent has $\langle\tilde\Pi\rangle_{\natural}=0$ and $B^{2}(\tilde\Pi)=-\tfrac14$. The number $\kappa$ is real and $\kappa\ge1$, with equality exactly when $\tilde\Pi$ is Hermitian.

**Proposition (the closed form).** On $\Sigma_{01}$,

$$
\boxed{\;
a=\frac{\lvert c\rvert\sqrt{\kappa}}{2}=\lvert Q_t\rvert\sqrt{\kappa},\qquad
P=\frac{\tilde\Pi\tilde\Pi^{*}}{\kappa},\qquad
\tilde Q_H=\lvert c\rvert\sqrt{\kappa}\,P,\qquad
\tilde Q_0=\frac{c}{\lvert c\rvert}\frac{\tilde\Pi}{\sqrt{\kappa}}=\frac{Q_t}{a}\tilde\Pi .
\;}
$$

*Proof.* The Hermitian norm of $\tilde\Pi=(e_t+\tilde\Xi)/2$ is

$$
\langle\tilde\Pi\rangle_{*}
=\frac14\bigl(1+\langle\tilde\Xi\tilde\Xi^{*}\rangle_{*}\bigr)
=\frac{1+\lVert\tilde\Xi\rVert_E^{2}}{4}
=\frac{\kappa}{2},
$$

because $\operatorname{Sc}\tilde\Xi=0$ and $\operatorname{Sc}(\tilde\Xi\tilde\Xi^{*})=\lVert\tilde\Xi\rVert_E^{2}$. Hence $\langle\tilde Q\rangle_{*}=\lvert c\rvert^{2}\kappa/2$ and $a=\lvert c\rvert\sqrt{\kappa}/2$. The formula for $P$ is $\tilde Q\tilde Q^{*}/(4a^{2})=\tilde\Pi\tilde\Pi^{*}/\kappa$. The partial-isometry factor is

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

## The One-Sided Operators

### Elementary properties

**Proposition.** Let $\tilde Q,\tilde Q'\in\mathbb{B}$. Then:

**(a)** $L_{\tilde Q}$ and $R_{\tilde Q}$ are $\mathbb{C}$-linear;

**(b)** $L_{\tilde Q}\circ L_{\tilde Q'}=L_{\tilde Q\tilde Q'}$ and $R_{\tilde Q}\circ R_{\tilde Q'}=R_{\tilde Q'\tilde Q}$;

**(c)** $L_{\tilde Q}\circ R_{\tilde Q'}=R_{\tilde Q'}\circ L_{\tilde Q}$;

**(d)** the parameter maps are injective;

**(e)** $L_{\tilde Q}$ and $R_{\tilde Q}$ are invertible exactly when $\tilde Q$ is a unit.

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

## The Polar Pair, One-Sided

### The scalar collapse

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

The phase $c/\lvert c\rvert$ is carried by $\tilde Q_0$; the modulus $2a=\lvert c\rvert\sqrt{\kappa}$ is the scalar. The one-sided operator therefore keeps the phase. The sandwich of the companion article keeps only $\lvert c\rvert^{2}$ and cancels the phase.

When $\tilde\Pi$ is Hermitian, $\kappa=1$ and $\tilde Q_0=(c/\lvert c\rvert)\tilde\Pi$. Then $L_{\tilde Q}=cL_{\tilde\Pi}$ with $L_{\tilde\Pi}$ an orthogonal projection, and the clean word is a scale $c$ times a projection. When $\tilde\Pi$ is not Hermitian, $L_{\tilde\Pi}$ is only $\sqrt{\kappa}$ times a partial isometry; the scalar collapse through $\tilde Q_0$ is the correct statement. The non-Hermitian example of §*Worked Examples* shows the difference.

### The modulus and the singular value

The element modulus is $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}=0$. The number $2a$ is not a modulus in that sense: it is the non-zero singular value of $\tilde Q$ in the matrix model, equivalently the non-zero spectral value of the Hermitian factor $\tilde Q_H$. The operator $L_{\tilde Q}$ is singular, but it is not the zero operator: it has rank two and non-zero singular value $2a$. The vanishing of $\Rho$ says that the element is a zero divisor; it does not say that the operator is nilpotent. On $\Sigma_{00}$, where $B^{2}=0$ and $Q_t=0$, the operator is nilpotent; on $\Sigma_{10}$, where $Q_t\neq0$, it is unipotent instead.

## The Eigenbasis and the Two Slots

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

In the matrix model the two slots are the singular vectors $u$ and $v$. The left multiplication $L_{\tilde Q}$ writes on the left slot $u$ and reads the right covector $v^{\dagger}$; the right multiplication reads the $u$-component and writes on the $v$-slot. The one-sided operator sees the complex overlap $v^{\dagger}u=Q_t/a$. Its eigenvalue is $c=2a\,v^{\dagger}u$, twice. The modulus of the overlap is $\cos\theta=1/\sqrt{\kappa}$; the phase of the overlap is the phase of $c$. The sandwich of the companion article sees only the squared modulus $\cos^{2}\theta$; this is the precise form of the one-sided/two-sided contrast in this sector.

## The Exponential

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

because $\tilde\Pi^{\natural}=\tilde\Pi'$ and $\tilde\Pi\tilde\Pi'=0$. The exponential is a unit for every $t$. Its $B^{2}$ is $-\tfrac14(e^{tc}-1)^{2}$, which is non-zero for generic $t\neq0$; it vanishes exactly when $e^{tc}=1$, where the exponential is $e_t$ on the wall $\Sigma_{10}$. Hence the flow lies in the doubly regular sector $\Sigma_{11}$ for generic $t\neq0$. For generic $t$, a zero divisor of $\Sigma_{01}$ has an exponential that is a unit with distinct eigenvalues. The one-sided rate is $c$; the two-sided rate of the companion article is $\lvert c\rvert^{2}$.

## Worked Examples

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

Then $c=2$, $\tilde\Pi=(e_t+\vec e_x+i\sqrt2\,\vec e_z)/2$, $\tilde\Xi=\vec e_x+i\sqrt2\,\vec e_z$, $\kappa=2$, $a=\sqrt2$. The idempotent is not Hermitian; its Hermitian projection is

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

## Summary

### Main Results

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
| determinant | $0$ |
| singular values | $2a$ (twice), $0$ (twice) |
| image | $\tilde Q\mathbb{B}$ and $\mathbb{B}\tilde Q$, totally isotropic planes |
| kernel | the annihilator planes, meeting in $\mathbb{C}\tilde\Pi'$ |
| scalar collapse | $L_{\tilde Q}=2aL_{\tilde Q_0}$, $R_{\tilde Q}=2aR_{\tilde Q_0}$ |
| exponential | $\exp(tL_{\tilde Q})=I+(e^{tc}-1)L_{\tilde\Pi}$ |
| element flow | $\exp(t\tilde Q)=e_t+(e^{tc}-1)\tilde\Pi$, a unit in $\Sigma_{11}$ for generic $t\neq0$ |

### What the Operator Shows

- The norm degeneration fixes the rank: on the null cone the one-sided operator has rank two, and its image is a totally isotropic plane.
- The spectral regularity fixes the Jordan type: the operator is a projection up to scale, not a nilpotent; its minimal polynomial is squarefree.
- The polar pair collapses to a scalar times a partial isometry, $L_{\tilde Q}=2aL_{\tilde Q_0}$; the positive factor acts as the scalar $2a$ on the image.
- The non-zero singular value $2a$ is the singular value of the element, repeated twice; the idempotent projection $L_{\tilde\Pi}$ has singular value $\sqrt{\kappa}$, not one, unless $\tilde\Pi$ is Hermitian.
- The phase is one-sided: it sits in $\tilde Q_0$ and in the eigenvalue $c$; the sandwich of the companion article sees only $\lvert c\rvert^{2}$.
- The two slots of the matrix model are the singular vectors $u$ and $v$; their overlap $\cos\theta=1/\sqrt{\kappa}$ is the spectral invariant, and it vanishes exactly at the wall $\Sigma_{00}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q=c\tilde\Pi$ | an element of $\Sigma_{01}$ |
| $\tilde\Pi'=e_t-\tilde\Pi$ | the complementary idempotent |
| $\tilde\Xi=2\tilde\Pi-e_t$ | the pure root of $e_t$ |
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

## Further Reading

- [The One-Sided Operators of a N-Regular, Spectrally Regular Biquaternion](the-one-sided-operators-of-a-n-regular-spectrally-regular-biquaternion.html), for the general one-sided theory and the four-factor word.
- [The One-Sided Operators of a N-Regular, Spectrally Degenerate Biquaternion](the-one-sided-operators-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the unipotent two-block operator at the spectral wall of the regular sector.
- [The Two-Sided Operator of a N-Degenerate, Spectrally Regular Biquaternion](the-two-sided-operator-of-a-n-degenerate-spectrally-regular-biquaternion.html), for the companion sandwich, the rank-one projection and the cancellation of the phase.
- [The One-Sided Operators of a N-Degenerate, Spectrally Degenerate Biquaternion](the-one-sided-operators-of-a-n-degenerate-spectrally-degenerate-biquaternion.html), for the nilpotent case of the same sector pair.
- [The Polar Decomposition of a N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the general two-factor pair on the null cone.
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the definition, the spectral decomposition and the spinorial reading of the sector.
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the wall $B^{2}=0$, the nilpotents and the canonical Jordan pair.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the null cone and the quaternionic norm.
