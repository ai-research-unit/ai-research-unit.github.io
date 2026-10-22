# __Eigenvalue Decomposition of a Split-Complex Number__

## Introduction

The split-complex algebra $\mathbb{D}=\mathbb{R}[x]/(x^2-1)=\mathbb{R}[j]$, $j^2=+1$, is commutative, associative and two-dimensional over $\mathbb{R}$. The idempotent decomposition $\mathbb{D}=\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$ makes it isomorphic to $\mathbb{R}\oplus\mathbb{R}$. This article reads the **eigenvalue decomposition** of a split-complex number $Q=q+jq'$ in the distinct case $q'\neq0$: the writing

$$
Q=\lambda_+\Pi_+ + \lambda_-\Pi_-,
\qquad
\lambda_+=q+q'=Q_+,
\quad
\lambda_-=q-q'=Q_-,
$$

where the coefficients $\lambda_\pm$ are the eigenvalues and the idempotents $\Pi_\pm$ are the eigenprojections. The eigenvalues are therefore the idempotent coordinates, and their values are displayed with them throughout. The article is the two-dimensional commutative counterpart of *Eigenvalue Decomposition of a Biquaternion*.

The general definition, the existence theorem and the uniqueness theorem are those of *The Eigenvalue Decomposition of an Element*. The split-complex content is that, in the distinct case, the eigenprojections are the standard idempotents $\Pi_\pm$, that these idempotents are central, and that the Peirce decomposition relative to either of them is the decomposition of the whole algebra. There is no vector part, the generator $j$ is part of the presentation rather than a root extracted from the element, and there is no continuous family of idempotents: the algebra has exactly four idempotents, and the nontrivial pair is unique.

**Placement.** The article is in the Algebra group of the Split-Complex Numbers category, after *Split-Complex Ideals and Peirce Decomposition* and before *The Specificities of the Split-Complex Algebra*. It uses the idempotents of *Split-Complex Idempotents and Projections*, the Peirce decomposition of *Split-Complex Ideals and Peirce Decomposition*, the norm and the invertibility criterion of *Split-Complex Norm and Invertibility*, and the eigenvalue computation of the regular representation in *Split-Complex Regular Element Representation*. The polar form is developed in *Modulus–Unit Polar Decomposition of Split-Complex Numbers* and *Exponential Polar Decomposition of Split-Complex Numbers*.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$, with basis $1,j$, $j^2=+1$, general element $Q=q+jq'$ with $q=\operatorname{Re}Q$ and $q'=\operatorname{Im}Q$, conjugate $\bar Q=q-jq'$, idempotents $\Pi_\pm=\tfrac12(1\pm j)$ and idempotent coordinates $Q_\pm=q\pm q'$, so that $Q=Q_+\Pi_+ + Q_-\Pi_-$. The norm is $\langle Q\rangle_{*}=Q\bar Q=q^2-q'^2$. The eigenvalues are written $\lambda_\pm=Q_\pm=q\pm q'$; a test scalar in the definition of an eigenvalue is written $\mu$, so the letter $\lambda$ is reserved for the two eigenvalues. The base is $\mathbb{R}$, as throughout the category.

**Scope.** The article proves the eigenvalue decomposition in the distinct case $q'\neq0$, identifies the eigenprojections with the standard idempotents $\Pi_\pm$, reads the decomposition as the Peirce decomposition relative to $\Pi_+$, and treats the degenerate regimes: the scalar element, where the eigenvalue is repeated, the zero divisor, where one eigenvalue vanishes, and the nilpotent regime, which is empty because the algebra is reduced.

**Boundaries.** The complex case is the subject of *Eigenvalues and Diagonalisation*; the reduced biquaternion case is *Eigenvalue Decomposition of a Reduced Biquaternion*; the biquaternion case is *Eigenvalue Decomposition of a Biquaternion*; the exponential and the logarithm built on the decomposition are those of *Split-Complex Exponential and Lie Group Structure*; and the polar forms are those of *Modulus–Unit Polar Decomposition of Split-Complex Numbers* and *Exponential Polar Decomposition of Split-Complex Numbers*.

## The Spectrum and the Characteristic Polynomial

**Definition.** Let $Q\in\mathbb{D}$. A real number $\mu$ is an **eigenvalue** of $Q$ if $Q-\mu$ is not invertible in $\mathbb{D}$; the set of eigenvalues is the **spectrum** $\sigma(Q)$. This is the definition of *The Eigenvalue Decomposition of an Element*, §*The Eigenvalues of an Element*.

**Theorem.** The spectrum of $Q=q+jq'$ is

$$
\sigma(Q)=\{\lambda_+,\lambda_-\},
\qquad
\lambda_+=q+q'=Q_+,
\qquad
\lambda_-=q-q'=Q_-.
$$

Thus the two eigenvalues are the two idempotent coordinates, and their sum and product are

$$
\lambda_++\lambda_-=2q,
\qquad
\lambda_+\lambda_-=q^2-q'^2=\langle Q\rangle_{*}.
$$

**Proof.** The element $Q-\mu=(q-\mu)+jq'$ has norm $(q-\mu)^2-q'^2$. By the criterion of *Split-Complex Norm and Invertibility*, §*Criterion for Invertibility*, it is invertible exactly when its norm is nonzero. Hence $Q-\mu$ is not invertible exactly when $(q-\mu)^2=q'^2$, that is, when $\mu=q+q'$ or $\mu=q-q'$. These two numbers are $\lambda_+$ and $\lambda_-$.

**Characteristic polynomial.** The characteristic polynomial of $Q$ is

$$
p_Q(X)=X^2-2qX+\langle Q\rangle_{*}
=(X-\lambda_+)(X-\lambda_-),
\qquad
\lambda_\pm=q\pm q'.
$$

It is the characteristic polynomial of the regular matrix

$$
\mathsf{M}_2(Q)=\begin{pmatrix}q&q'\\q'&q\end{pmatrix},
$$

whose trace is $\lambda_++\lambda_-=2q$ and whose determinant is $\lambda_+\lambda_-=\langle Q\rangle_{*}$ (*Split-Complex Regular Element Representation*, §*The Determinant, the Trace and the Norm*). Its discriminant is

$$
(\lambda_+-\lambda_-)^2=(2q')^2=4q'^2,
$$

so the eigenvalues are distinct exactly when $q'\neq0$, that is, exactly when $\lambda_+\neq\lambda_-$. The minimal polynomial is $p_Q$ when $q'\neq0$ and $X-q$ when $q'=0$, in which case $\lambda_+=\lambda_-=q$. Since $q,q'\in\mathbb{R}$, the spectrum is always real and the characteristic polynomial splits over $\mathbb{R}$.

The data of the spectrum are collected in the table.

| Quantity | Value |
|---|---|
| Spectrum | $\sigma(Q)=\{\lambda_+,\lambda_-\}$ |
| Eigenvalues | $\lambda_+=q+q'$, $\lambda_-=q-q'$ |
| Sum | $\lambda_++\lambda_-=2q$ |
| Product | $\lambda_+\lambda_-=q^2-q'^2=\langle Q\rangle_{*}$ |
| Discriminant | $(\lambda_+-\lambda_-)^2=4q'^2$ |
| Characteristic polynomial | $p_Q(X)=X^2-2qX+\langle Q\rangle_{*}=(X-\lambda_+)(X-\lambda_-)$ |
| Minimal polynomial | $(X-\lambda_+)(X-\lambda_-)$ if $q'\neq0$; $X-q$ if $q'=0$ |

## The Eigenprojections

**The eigenprojections of a non-scalar split-complex number are the two standard idempotents $\Pi_\pm$.**

Put

$$
\Pi_+=\frac{1+j}{2},\qquad \Pi_-=\frac{1-j}{2}.
$$

By *Split-Complex Idempotents and Projections*, §*The Standard Idempotents of $\mathbb{D}$*, they satisfy

$$
\Pi_+^2=\Pi_+,\qquad \Pi_-^2=\Pi_-,\qquad \Pi_+\Pi_-=\Pi_-\Pi_+=0,\qquad \Pi_++\Pi_-=1.
$$

They are therefore **complementary orthogonal idempotents**. In $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$ each is a minimal idempotent, and the pair $(\Pi_+,\Pi_-)$ is a **resolution of the identity** into minimal idempotents. Since $\mathbb{D}$ is commutative, $\Pi_\pm$ are **central**. By the classification of *Split-Complex Idempotents and Projections*, §*The Classification of the Idempotents*, the algebra has exactly four idempotents, $0,1,\Pi_+,\Pi_-$, so $\{\Pi_+,\Pi_-\}$ is the only nontrivial complementary pair.

For $q'\neq0$, they are the **eigenprojections** of $Q$, with eigenvalues $\lambda_+=q+q'$ and $\lambda_-=q-q'$:

$$
Q\Pi_+=\lambda_+\Pi_+=(q+q')\Pi_+,
\qquad
Q\Pi_-=\lambda_-\Pi_-=(q-q')\Pi_-.
$$

Indeed,

$$
(q+jq')\frac{1+j}{2}
=
\frac{q+qj+q'j+q'}{2}
=
\frac{(q+q')(1+j)}{2}
=\lambda_+\Pi_+,
$$

and the computation with $1-j$ and $q-q'$ gives the second relation.

Equivalently, by the Lagrange–Sylvester interpolation formula of *The Lagrange–Sylvester Eigenprojector Formula*, §*The Eigenprojector Formula*,

$$
\Pi_+=\frac{Q-\lambda_-}{\lambda_+-\lambda_-}
=\frac{Q-(q-q')}{2q'},
\qquad
\Pi_-=\frac{Q-\lambda_+}{\lambda_--\lambda_+}
=\frac{Q-(q+q')}{-2q'},
$$

with $\lambda_+-\lambda_-=2q'$. Hence $\Pi_\pm$ are polynomials in $Q$ when $q'\neq0$, and in particular commute with $Q$. When $q'=0$ the denominator vanishes and the formula does not apply: the eigenprojection of the single eigenvalue $\lambda_+=\lambda_-=q$ is then $1$, not $\Pi_\pm$.

The pair is collected in the table.

| Idempotent | Definition | Eigenvalue | Properties |
|---|---|---|---|
| $\Pi_+$ | $\tfrac12(1+j)$ | $\lambda_+=q+q'$ | $\Pi_+^2=\Pi_+$, central, primitive |
| $\Pi_-$ | $\tfrac12(1-j)$ | $\lambda_-=q-q'$ | $\Pi_-^2=\Pi_-$, central, primitive |

The two idempotents are complementary and orthogonal, $\Pi_++\Pi_-=1$ and $\Pi_+\Pi_-=0$.

## The Eigenvalue Decomposition

**Every split-complex number with distinct eigenvalues is the real linear combination of the two standard idempotents with its eigenvalues as coefficients.**

For $q'\neq0$, summing the two eigenvalue relations gives

$$
\boxed{\ Q=\lambda_+\Pi_+ + \lambda_-\Pi_-
=(q+q')\Pi_+ + (q-q')\Pi_-\ }.
$$

Equivalently, separating the $1$ and $j$ parts,

$$
Q
=
\frac{\lambda_++\lambda_-}{2}
+
\frac{\lambda_+-\lambda_-}{2}j
=
q+jq'.
$$

So in the distinct case the eigenvalue decomposition writes $Q$ as a real linear combination of two minimal idempotents, with its eigenvalues $\lambda_\pm=q\pm q'$ as coefficients. The scalar case $q'=0$, where $\lambda_+=\lambda_-=q$, is deferred to §*The Scalar Regime*. Under the regular representation the distinct case is the diagonalisation

$$
P\,\mathsf{M}_2(Q)\,P^{-1}
=
\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}
=
\begin{pmatrix}q+q'&0\\0&q-q'\end{pmatrix},
\qquad
P=\begin{pmatrix}1&1\\1&-1\end{pmatrix},
$$

of *Split-Complex Regular Element Representation*, §*Diagonalisation in the Idempotent Basis*.

**Uniqueness.** In the distinct case, the unordered pair $\{\lambda_+,\lambda_-\}=\{q+q',q-q'\}$ is determined by $Q$: it is the spectrum, the set of roots of $p_Q$. The ordered pair $(\lambda_+,\lambda_-)=(q+q',q-q')$ is determined once the two idempotents are labelled. The algebra alone, without the choice of the generator $j$, does not distinguish the labels, because the automorphism $j\mapsto-j$ exchanges $\Pi_+$ and $\Pi_-$ and with them $\lambda_+$ and $\lambda_-$. Relative to the convention, which fixes $j$, the ordered pair is the coordinate pair in the basis $(\Pi_+,\Pi_-)$. No other pair of eigenprojections exists, since $\{\Pi_+,\Pi_-\}$ is the only nontrivial complementary pair.

**Semisimplicity.** For $q'\neq0$, the minimal polynomial $p_Q=(X-\lambda_+)(X-\lambda_-)$ is squarefree, so $Q$ is semisimple. The eigenvalue decomposition is the diagonalisation of $Q$ with respect to the central idempotents $\Pi_\pm$.

## The Peirce Decomposition Relative to the Eigenprojection

**The Peirce decomposition relative to $\Pi_+$ is the direct product $\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$, with vanishing mixed corners.**

Let $e=\Pi_+$, so that $1-e=\Pi_-$. The **Peirce decomposition** of the algebra $\mathbb{D}$ relative to $e$ is

$$
\mathbb{D}
=
e\mathbb{D}e\oplus e\mathbb{D}(1-e)\oplus(1-e)\mathbb{D}e\oplus(1-e)\mathbb{D}(1-e).
$$

Write $\mathbb{D}_{st}=\Pi_s\mathbb{D}\Pi_t$ for $s,t\in\{+,-\}$; this is the sign-indexed form of the corners $\mathbb{D}_{11}=\mathbb{D}_{++}$ and $\mathbb{D}_{22}=\mathbb{D}_{--}$ of *Split-Complex Ideals and Peirce Decomposition*, §*Idempotents and the Peirce Decomposition*. Because $\mathbb{D}$ is commutative and $\Pi_+\Pi_-=0$, the off-diagonal Peirce components vanish:

$$
\mathbb{D}_{+-}=\Pi_+\mathbb{D}\Pi_-=0,
\qquad
\mathbb{D}_{-+}=\Pi_-\mathbb{D}\Pi_+=0.
$$

Hence the Peirce decomposition collapses to a **direct sum of algebras**

$$
\mathbb{D}
=
\mathbb{D}_{++}\oplus\mathbb{D}_{--}
=
\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-,
$$

of total dimension $1+1+0+0=2$. The summands $\mathbb{D}_{\pm\pm}=\mathbb{R}\Pi_\pm$ are the minimal two-sided ideals of $\mathbb{D}$, as in *Split-Complex Ideals and Peirce Decomposition*, §*The Two-Sided Ideals*.

The four corners are collected in the table.

| Corner | Definition | Value | Dimension over $\mathbb{R}$ |
|---|---|---|---|
| $\mathbb{D}_{++}$ | $\Pi_+\mathbb{D}\Pi_+$ | $\mathbb{R}\Pi_+$ | $1$ |
| $\mathbb{D}_{+-}$ | $\Pi_+\mathbb{D}\Pi_-$ | $0$ | $0$ |
| $\mathbb{D}_{-+}$ | $\Pi_-\mathbb{D}\Pi_+$ | $0$ | $0$ |
| $\mathbb{D}_{--}$ | $\Pi_-\mathbb{D}\Pi_-$ | $\mathbb{R}\Pi_-$ | $1$ |

The element $Q$ and every polynomial in $Q$ lie in the diagonal part

$$
\mathbb{D}_{++}\oplus\mathbb{D}_{--}
=
\operatorname{span}_{\mathbb{R}}\{\Pi_+,\Pi_-\}
=
\mathbb{D}.
$$

The last equality is the commutative phenomenon: the diagonal part is the whole algebra, because the off-diagonal corners vanish. Since $\mathbb{D}$ is commutative, the centraliser of $Q$ is $\mathbb{D}$ for every $Q$. The subalgebra generated by $Q$ is different: $\mathbb{R}[Q]=\mathbb{D}$ when $q'\neq0$, since $\{1,Q\}$ is then a basis, while $\mathbb{R}[Q]=\mathbb{R}$ in the scalar regime $q'=0$.

On $Q$ the Peirce decomposition reads

$$
Q=\lambda_+\Pi_+ + \lambda_-\Pi_-
=(q+q')\Pi_+ + (q-q')\Pi_-,
$$

with zero mixed components. The eigenvalue decomposition is therefore the Peirce decomposition read on the element: the element lies in the diagonal part, and its two diagonal Peirce coordinates are its eigenvalues $\lambda_+=q+q'$ and $\lambda_-=q-q'$. This is the commutative shadow of the biquaternion case, where the idempotents are noncentral, the mixed corners are nonzero, and the diagonal part is only the centraliser.

## Powers, Polynomial Calculus, and the Group of Units

**The eigenvalue decomposition carries the polynomial calculus, the inverse and the group isomorphism of the unit group.**

For any polynomial $f\in\mathbb{R}[X]$, the idempotent writing $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ gives

$$
f(Q)=f(\lambda_+)\Pi_+ + f(\lambda_-)\Pi_-
=f(q+q')\Pi_+ + f(q-q')\Pi_-.
$$

This follows from $Q^n=\lambda_+^n\Pi_+ + \lambda_-^n\Pi_-$ for $n\geq0$ (with $\Pi_++\Pi_-=1$ for $n=0$) and linearity. In particular,

$$
Q^n=\lambda_+^n\Pi_+ + \lambda_-^n\Pi_-
=(q+q')^n\Pi_+ + (q-q')^n\Pi_-,
\qquad n\geq0.
$$

When $Q$ is a unit, both eigenvalues are nonzero, and the formula extends to negative powers:

$$
Q^{-1}=\lambda_+^{-1}\Pi_+ + \lambda_-^{-1}\Pi_-
=\frac{1}{q+q'}\Pi_+ + \frac{1}{q-q'}\Pi_-.
$$

The result agrees with the inverse formula of *Split-Complex Norm and Invertibility*, §*The Inverse Formula*,

$$
Q^{-1}=\frac{\bar Q}{\langle Q\rangle_{*}},
$$

since $\bar Q=\lambda_-\Pi_+ + \lambda_+\Pi_-$ and $\langle Q\rangle_{*}=\lambda_+\lambda_-$.

**The group of units.** The map

$$
\mathbb{D}^\times\longrightarrow\mathbb{R}^\times\times\mathbb{R}^\times,
\qquad
Q\longmapsto(\lambda_+,\lambda_-)=(q+q',q-q')
$$

is an isomorphism of groups: multiplication is coordinatewise, and $Q$ is a unit if and only if both eigenvalues are nonzero, that is, if and only if $\lambda_+\lambda_-=\langle Q\rangle_{*}\neq0$. The identity is $1=(1,1)$, corresponding to $\Pi_++\Pi_-$. The inverse is the componentwise inverse displayed above.

## The Algebraic Fibre of the Decomposition

**The eigenvalue coordinates and the basis coordinates are two linear coordinate systems on the same algebra.**

Fix the pair, that is, fix the labelling of $\Pi_+$ and $\Pi_-$. Every element of $\mathbb{D}$ is

$$
Q_1=\mu_+\Pi_+ + \mu_-\Pi_-,
\qquad \mu_\pm\in\mathbb{R},
$$

and the map $(\mu_+,\mu_-)\mapsto Q_1$ is an $\mathbb{R}$-linear isomorphism $\mathbb{R}^2\to\mathbb{D}$. For $\mu_+\neq\mu_-$ this is the eigenvalue decomposition of $Q_1$, with the eigenprojections $\Pi_\pm$ and the eigenvalue data $(\mu_+,\mu_-)$. For $\mu_+=\mu_-=a$ the element is $Q_1=a$, scalar; the two-term writing is still valid, but its coefficients are not distinct, so it is not an eigenvalue decomposition in the sense of the general definition. The eigenvalue decomposition is then the one-term writing $Q_1=a\cdot1$ of §*The Scalar Regime*.

The unordered spectrum is the image of the map $(\mu_+,\mu_-)\mapsto\{\mu_+,\mu_-\}$. Off the diagonal it is two-to-one: the two preimages of $\{\mu_+,\mu_-\}$ are $\mu_+\Pi_+ + \mu_-\Pi_-$ and $\mu_-\Pi_+ + \mu_+\Pi_-$, which differ by $(\mu_+-\mu_-)(\Pi_+-\Pi_-)=(\mu_+-\mu_-)j\neq0$. The ambiguity is exactly the exchange of the two labels.

### The Coordinate Change to Basis Coordinates

The scalar and split-imaginary coordinates of $Q_1$ are

$$
Q_1
=
\frac{\mu_++\mu_-}{2}
+
\frac{\mu_+-\mu_-}{2}j
=
q+jq',
\qquad
q=\frac{\mu_++\mu_-}{2},
\quad
q'=\frac{\mu_+-\mu_-}{2}.
$$

The map $(\mu_+,\mu_-)\mapsto(q,q')$ is an $\mathbb{R}$-linear isomorphism of $\mathbb{R}^2$. The two coordinate systems are the eigenvalue coordinates and the basis coordinates on the same algebra: $(\Pi_+,\Pi_-)$ is a basis of idempotents, and $(1,j)$ is the basis of the algebra. In the eigenvalue coordinates the eigenvalues are simply the coordinates themselves.

### The Lattice of Eigenvalue Data

If the eigenvalue coordinates are restricted to $\mathbb{Z}^2$, that is, if $\mu_\pm=k_\pm\in\mathbb{Z}$, the basis-coordinate pair $(q,q')$ runs over the lattice

$$
L=\left\{\left(\frac{m}{2},\frac{n}{2}\right):\ m,n\in\mathbb{Z},\ m\equiv n\pmod2\right\}.
$$

Indeed, for $\mu_\pm=k_\pm\in\mathbb{Z}$ one has

$$
q=\frac{\mu_++\mu_-}{2}=\frac{k_++k_-}{2}=\frac{m}{2},
\qquad
q'=\frac{\mu_+-\mu_-}{2}=\frac{k_+-k_-}{2}=\frac{n}{2},
$$

with $m=k_++k_-$ and $n=k_+-k_-$. Then $m-n=2k_-$, so $m\equiv n\pmod2$; conversely, every pair $(m,n)$ of the same parity comes from the integers $k_\pm=(m\pm n)/2$. The parity condition reflects the fact that the idempotents mix the $1$ and $j$ directions: the integral shifts in the eigenvalue coordinates do not map to the rectangular lattice $\mathbb{Z}^2$ in the basis coordinates. For example, $\mu_+=\mu_-=1$ gives $(q,q')=(1,0)$ and $Q=1$, while $\mu_+=2$, $\mu_-=0$ gives $(q,q')=(1,1)$ and $Q=1+j=2\Pi_+$, a zero divisor.

The lattice $L$ is a coordinate lattice, not an intrinsic invariant of $Q$. Nor does it arise as the kernel of an exponential: the split-complex exponential is injective (*Split-Complex Exponential and Lie Group Structure*, §*The Exponential Map: Image and Kernel*). This is a difference from the biquaternion parity-matched lattice, where the corresponding lattice is the kernel of the exponential on the diagonal part.

### The Hyperbolic Polar Form

**On the identity component the decomposition is the hyperbolic polar form $Q=r(\cosh t+j\sinh t)$.**

Let $Q$ be a unit with $\langle Q\rangle_{*}>0$ and $q>0$, so that $Q$ lies in the identity component of $\mathbb{D}^\times$. Then $\lambda_+=q+q'>0$ and $\lambda_-=q-q'>0$. Put

$$
r=\sqrt{\lvert\langle Q\rangle_{*}\rvert}=\sqrt{\lambda_+\lambda_-}>0,
\qquad
t=\operatorname{artanh}\!\left(\frac{q'}{q}\right).
$$

Then

$$
Q=r\bigl(\cosh t+j\sinh t\bigr),
\qquad
\lambda_+=r\exp(t),
\qquad
\lambda_-=r\exp(-t).
$$

In this form,

$$
\lambda_+\lambda_-=r^2=\langle Q\rangle_{*},
\qquad
\frac{\lambda_+}{\lambda_-}=\exp(2t).
$$

Thus $\eta=\exp(t)=\lambda_+/r$ satisfies $\eta^2=\lambda_+/\lambda_-$, and

$$
\lambda_+=r\eta,
\qquad
\lambda_-=r\eta^{-1}.
$$

The eigenvalue formula and the hyperbolic polar form are related by the invertible coordinate change

$$
\lambda_\pm=q\pm q',
\qquad
q=\frac{\lambda_++\lambda_-}{2},
\quad
q'=\frac{\lambda_+-\lambda_-}{2}.
$$

The four components of $\mathbb{D}^\times$ are cut out by the signs of $\lambda_+$ and $\lambda_-$, in the patterns $(+,+)$, $(-,-)$, $(+,-)$ and $(-,+)$. The identity component is the pattern $(+,+)$. On the opposite timelike component, where $\langle Q\rangle_{*}>0$ and $q<0$, the pattern is $(-,-)$, and with the same $r$ and $t=\operatorname{artanh}(q'/q)$ the writing $Q=-r(\cosh t+j\sinh t)$ gives $\lambda_\pm=-r\exp(\pm t)$. In the spacelike regime $\langle Q\rangle_{*}<0$, the two eigenvalues have opposite signs; with the same modulus $r=\sqrt{\lvert\langle Q\rangle_{*}\rvert}$ and with $\varepsilon=\operatorname{sgn}q'\in\{\pm1\}$, one has $q=r\sinh s$, $q'=\varepsilon r\cosh s$, and

$$
\lambda_+=\varepsilon r\exp(\varepsilon s),
\qquad
\lambda_-=-\varepsilon r\exp(-\varepsilon s).
$$

The full modulus–unit statement is *Modulus–Unit Polar Decomposition of Split-Complex Numbers*, §*The Two Factors*. On the identity component the polar form writes $Q$ as a positive scale times a unit factor, while the eigenvalue decomposition writes $Q$ as a linear combination of the two idempotents with the eigenvalues $\lambda_\pm=q\pm q'$ as coefficients. The two readings carry the same data: the scale is $r=\sqrt{\lambda_+\lambda_-}$ and the unit factor is $\exp(tj)$, whose eigenvalues are $\exp(\pm t)$.

## Degenerate Regimes

The eigenvalue decomposition with distinct eigenvalues requires $q'\neq0$, equivalently $\lambda_+\neq\lambda_-$. The scalar and zero-divisor cases remain, and the nilpotent regime of the biquaternion case is absent.

### The Scalar Regime

**A scalar element has a repeated eigenvalue, the one-term eigenprojection $1$, and a unique two-term refinement.**

Suppose $q'=0$, so that $Q=q$ with $q\in\mathbb{R}$. Then $\lambda_+=\lambda_-=q$, a **repeated** eigenvalue: the characteristic polynomial is $(X-q)^2$, and the minimal polynomial is $X-q$. In the sense of the general definition the eigenvalue decomposition is the one-term writing

$$
Q=q\cdot 1=\lambda_+\cdot 1,
$$

with the single eigenprojection $1$.

A two-term writing with the repeated coefficient $q$ is a different object:

$$
Q=q\Pi_+ + q\Pi_-=\lambda_+\Pi_+ + \lambda_-\Pi_-,
\qquad
\lambda_+=\lambda_-=q.
$$

Every complete orthogonal pair of nontrivial idempotents gives such a writing, but the algebra has only one nontrivial pair, $\{\Pi_+,\Pi_-\}$. The nontrivial two-term refinement is therefore unique even though the eigenvalue is repeated. This is in contrast with the biquaternion scalar regime, where every complete orthogonal pair gives a two-term writing and the pair is not determined by the element.

### The Zero-Divisor Regime

**A nonzero zero divisor has one zero eigenvalue and one nonzero eigenvalue, and it admits an eigenvalue decomposition even though it is not a unit.**

Suppose $\langle Q\rangle_{*}=q^2-q'^2=0$ with $Q\neq0$. Then $q'=\pm q$ and $q\neq0$, so

$$
Q=q(1\pm j)=2q\,\Pi_\pm.
$$

Such an element is a nonzero scalar multiple of an idempotent. Its eigenvalues are

$$
\lambda_+=2q,\quad \lambda_-=0
\qquad\text{for } Q=2q\Pi_+,
$$

and the two values are exchanged for $Q=2q\Pi_-$. They are distinct because $q\neq0$. Hence $Q$ **does** admit an eigenvalue decomposition

$$
Q=2q\,\Pi_+ + 0\cdot\Pi_-=\lambda_+\Pi_+ + \lambda_-\Pi_-,
\qquad
\lambda_+=2q,\quad \lambda_-=0,
$$

even though it is not a unit. This is not a failure of the eigenvalue decomposition: it is the case in which one eigenvalue vanishes. The element is semisimple, with minimal polynomial $X(X-2q)$: this is $X(X-\lambda_+)$ for $Q=2q\Pi_+$ and $X(X-\lambda_-)$ for $Q=2q\Pi_-$.

### The Nilpotent Regime

**There are no nonzero nilpotent elements, so there is no Jordan-block regime.**

The algebra $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$ is a product of fields, hence reduced: it has **no nonzero nilpotent elements**. Indeed, if $Q^2=0$ then $\lambda_+^2=\lambda_-^2=0$, so $\lambda_+=\lambda_-=0$ and $Q=0$. Therefore the nilpotent (Jordan-block) regime of the biquaternion case has no analogue here. Every element of $\mathbb{D}$ has a squarefree minimal polynomial and is semisimple: $p_Q=(X-\lambda_+)(X-\lambda_-)$ for $q'\neq0$ (which is $X(X-2q)$ in the zero-divisor subcase, where $\{\lambda_+,\lambda_-\}=\{2q,0\}$), and $X-q=X-\lambda_+$ for $q'=0$. The only failure of distinct eigenvalues is the scalar case $q'=0$, where $\lambda_+=\lambda_-=q$.

## Remarks

1. **Relation to the model algebra.** Under $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$, the eigenvalue decomposition is literally the product decomposition: $\lambda_+=q+q'$ and $\lambda_-=q-q'$ are the two components, $\Pi_+$ and $\Pi_-$ are the standard minimal idempotents, and the Lagrange–Sylvester formulas are the interpolation formulas in the product algebra.

2. **Centrality and the Peirce decomposition.** The idempotents $\Pi_\pm$ are central, so the Peirce decomposition is a direct sum of two-sided ideals $\mathbb{D}=\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-\cong\mathbb{R}\oplus\mathbb{R}$, and the off-diagonal Peirce components vanish. This is the commutative shadow of the biquaternion Peirce decomposition, where the idempotents are noncentral and the off-diagonal components are nonzero.

3. **Uniqueness and labelling.** The pair $\{\Pi_+,\Pi_-\}$ is the only nontrivial complementary pair of idempotents in $\mathbb{D}$. The labels are exchanged by $j\mapsto-j$, which sends $q'$ to $-q'$ and exchanges $\lambda_+=q+q'$ and $\lambda_-=q-q'$. Unlike the biquaternion case, there is no non-discrete family of eigenprojections.

4. **Degenerate regimes.** The eigenvalue decomposition with distinct eigenvalues requires $q'\neq0$, equivalently $\lambda_+\neq\lambda_-$. The scalar regime $q'=0$ has the repeated eigenvalue $\lambda_+=\lambda_-=q$, the one-term eigenprojection $1$, and a unique two-term refinement. The zero-divisor regime $\langle Q\rangle_{*}=0$, $Q\neq0$, consists of scalar multiples of idempotents and still admits an eigenvalue decomposition, with eigenvalues $2q$ and $0$. There is no nilpotent regime, because the algebra is reduced, and every element is semisimple.

5. **The base field.** The corpus fixes the base $\mathbb{R}$. The computations use only that $2$ is invertible: over any field $k$ of characteristic not $2$, the algebra $k[j]$, $j^2=1$, has the same idempotents $\Pi_\pm$, the same eigenvalues $\lambda_\pm=q\pm q'$ for $q'\neq0$, and the same decomposition. The norm, its sign, the polar form and the topology use the order or the real structure and are not part of that general statement.

## Summary

For a split-complex number $Q=q+jq'$ with $q'\neq0$, the eigenvalue decomposition is the writing

$$
Q=\lambda_+\Pi_+ + \lambda_-\Pi_-
=(q+q')\Pi_+ + (q-q')\Pi_-,
\qquad
\Pi_\pm=\frac{1\pm j}{2}.
$$

The eigenvalues are the two values

$$
\lambda_+=q+q'=Q_+,
\qquad
\lambda_-=q-q'=Q_-,
$$

which are real; they are distinct exactly when $q'\neq0$. In that case the idempotents are primitive, orthogonal, complete and central, and they are the eigenprojections. The decomposition is then unique up to the exchange of the two labels.

### Main Results

| Result | Expression |
|---|---|
| Spectrum | $\sigma(Q)=\{\lambda_+,\lambda_-\}=\{q+q',q-q'\}$ |
| Characteristic polynomial | $p_Q(X)=X^2-2qX+\langle Q\rangle_{*}=(X-\lambda_+)(X-\lambda_-)$ |
| Distinctness | $\lambda_+\neq\lambda_-\iff q'\neq0$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$ |
| Eigenvalue decomposition | $Q=\lambda_+\Pi_++\lambda_-\Pi_-=(q+q')\Pi_++(q-q')\Pi_-$ |
| Peirce decomposition | $\mathbb{D}=\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$ |
| Polynomial calculus | $f(Q)=f(\lambda_+)\Pi_++f(\lambda_-)\Pi_-$ |
| Group of units | $\mathbb{D}^\times\cong\mathbb{R}^\times\times\mathbb{R}^\times$ |

### Regimes

The zero-divisor row is a subcase of the distinct row, separated because one eigenvalue vanishes; the scalar row includes $Q=0$.

| Regime | Condition | Spectrum | Minimal polynomial | Eigenvalue decomposition |
|---|---|---|---|---|
| Distinct, not a zero divisor | $q'\neq0$, $\langle Q\rangle_{*}\neq0$ | $\{\lambda_+,\lambda_-\}$, distinct | $(X-\lambda_+)(X-\lambda_-)$ | $Q=\lambda_+\Pi_+ + \lambda_-\Pi_-$ |
| Zero divisor | $q'\neq0$, $\langle Q\rangle_{*}=0$ | $\{\lambda_\sigma,\lambda_{-\sigma}\}=\{2q,0\}$ | $X(X-2q)$ | $Q=2q\Pi_\sigma + 0\cdot\Pi_{-\sigma}$ |
| Scalar | $q'=0$ | $\{q\}$ | $X-q$ | $Q=q\cdot1$; refinement $Q=q\Pi_+ + q\Pi_-$ |
| Nilpotent | absent; only $Q=0$ | — | — | — |

The Peirce decomposition relative to $\Pi_+$ has corners $\mathbb{D}_{st}=\Pi_s\mathbb{D}\Pi_t$. Its off-diagonal corners vanish, and its diagonal part is the whole algebra $\mathbb{D}=\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$. The element $Q$ has the diagonal coordinates $\lambda_+=q+q'$ and $\lambda_-=q-q'$ and zero mixed coordinates. The centraliser of $Q$ is all of $\mathbb{D}$; the subalgebra $\mathbb{R}[Q]$ is all of $\mathbb{D}$ exactly when $Q$ is not scalar. The polynomial calculus, the inverse and the group isomorphism $\mathbb{D}^\times\cong\mathbb{R}^\times\times\mathbb{R}^\times$ all follow from the decomposition. The hyperbolic polar form gives the same data as $\lambda_\pm=r \exp(\pm t)$ on the identity component.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$ | Split-complex algebra, dimension $2$ over $\mathbb{R}$ |
| $Q=q+jq'$ | General split-complex number, $q,q'\in\mathbb{R}$ |
| $\bar Q=q-jq'$ | Split-complex conjugate |
| $\langle Q\rangle_{*}=Q\bar Q=q^2-q'^2=\lambda_+\lambda_-$ | Norm, signature $(1,1)$ |
| $\Pi_\pm=\tfrac12(1\pm j)$ | Standard idempotents; the eigenprojections when $q'\neq0$ |
| $\lambda_\pm=q\pm q'$ | Eigenvalues, with $\lambda_+=q+q'$ and $\lambda_-=q-q'$ |
| $Q_\pm=q\pm q'$ | Idempotent coordinates, equal to the eigenvalues: $Q_\pm=\lambda_\pm$ |
| $\sigma(Q)=\{\lambda_+,\lambda_-\}=\{q+q',q-q'\}$ | Spectrum |
| $p_Q(X)=X^2-2qX+\langle Q\rangle_{*}=(X-\lambda_+)(X-\lambda_-)$ | Characteristic polynomial |
| $\mathsf{M}_2(Q)=\begin{pmatrix}q&q'\\q'&q\end{pmatrix}$ | Regular matrix, trace $2q=\lambda_++\lambda_-$, determinant $\langle Q\rangle_{*}=\lambda_+\lambda_-$ |
| $\mathbb{D}_{st}=\Pi_s\mathbb{D}\Pi_t$ | Peirce corners of the pair $\Pi_\pm$ |
| $\mathbb{R}[Q]$ | Subalgebra generated by $Q$ |
| $\mathbb{D}^\times=\{Q\in\mathbb{D}:\langle Q\rangle_{*}\neq0\}$ | Group of units, characterised by $\lambda_+\lambda_-\neq0$ |
| $L=\{(m/2,n/2):m,n\in\mathbb{Z},\ m\equiv n\pmod2\}$ | Lattice of basis-coordinate data for integral eigenvalue coordinates $\mu_\pm\in\mathbb{Z}$ |
| $r=\sqrt{\lvert\langle Q\rangle_{*}\rvert}$, $t=\operatorname{artanh}(q'/q)$ | Modulus and hyperbolic angle, with $\lambda_\pm=r \exp(\pm t)$ on the identity component |
| $\mu$ | A test scalar in the definition of an eigenvalue |
| $\mu_\pm$ | Eigenvalue coordinates on the diagonal part |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for idempotents, Peirce decompositions and the structure of finite-dimensional algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for semisimplicity and the structure of finite-dimensional algebras.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 1985), for the eigenvalue decomposition and the Lagrange–Sylvester formula.
- Nicholas J. Higham, *Functions of Matrices: Theory and Computation* (SIAM, Philadelphia, 2008), for the functional calculus and the matrix inverse.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split-complex algebra as a Clifford algebra and its norm.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the hyperbolic geometry of the split-complex plane.
- The corpus articles: [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), [The Lagrange–Sylvester Eigenprojector Formula](the-lagrange-sylvester-eigenprojector-formula.html), [Split-Complex Algebra](split-complex-algebra.html), [Split-Complex Idempotents and Projections](split-complex-idempotents-and-projections.html), [Split-Complex Ideals and Peirce Decomposition](split-complex-ideals-and-peirce-decomposition.html), [Split-Complex Norm and Invertibility](split-complex-norm-and-invertibility.html), [Split-Complex Regular Element Representation](split-complex-regular-element-representation.html), [Split-Complex Exponential and Lie Group Structure](split-complex-exponential-and-lie-group-structure.html), [Modulus–Unit Polar Decomposition of Split-Complex Numbers](modulus-unit-polar-decomposition-of-split-complex-numbers.html), [Exponential Polar Decomposition of Split-Complex Numbers](exponential-polar-decomposition-of-split-complex-numbers.html), [Eigenvalue Decomposition of a Biquaternion](eigenvalue-decomposition-of-a-biquaternion.html) and [Conventions in Mathematics](conventions-in-mathematics.html).
