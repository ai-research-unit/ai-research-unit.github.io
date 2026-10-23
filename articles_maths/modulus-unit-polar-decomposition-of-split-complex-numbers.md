# __Modulus–Unit Polar Decomposition of Split-Complex Numbers__

## Introduction

This article treats the **modulus–unit polar decomposition** of a split-complex number: the writing

$$
Q = r\,u, \qquad r \in \mathbb{R}, \quad r > 0, \qquad u \in \mathbb{D}, \quad \lvert \langle u\rangle_{*}\rvert = 1,
$$

with $r$ the **modulus** and $u$ the **unit factor**. It is the algebraic member of the polar decompositions of $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$. It uses only the norm, the conjugate and a square root, and chooses no coordinate on the unit factor. It is the split companion of *Modulus–Unit Polar Decomposition of Complex Numbers*.

The norm of $\mathbb{D}$ is indefinite of signature $(1,1)$. Three consequences organise the article. The modulus is the square root of an absolute value, so it is a positive scale on the invertible set and it vanishes on the null cone. The unit factor has norm $+1$ in one regime and $-1$ in the other, so a single decomposition never straddles the two regimes. The unit set has four connected components, each a branch homeomorphic to a line, so the group of units is non-compact and its maximal compact subgroup is the four-element group $\{\pm1,\pm j\}$, not a circle.

The article defines the norm and the two regimes (§*The Two Factors*), proves existence and uniqueness (§*Existence and Uniqueness*), describes the group of units and its maximal compact subgroup (§*The Group of Units and the Unit Set*), records the two axes (§*The Two Axes*), gives the matrix picture (§*The Matrix Picture*), computes examples (§*Worked Examples*) and compares the family (§*The Other Algebras*).

The conventions and the symbols are those of *Split-Complex Algebra*, *Norm and Invertibility in the General Split-Complex Algebra* and *Conventions in Mathematics*; the notation is collected in §*Summary of Notation*. The rational and exponential coordinates are the subjects of *Rational-Chart Polar Decomposition of Split-Complex Numbers* and *Exponential Polar Decomposition of Split-Complex Numbers*. Every numerical value displayed below was recomputed in double precision.

## The Two Factors

### The Norm and the Modulus

Let $Q = q + j q'$ with $q, q' \in \mathbb{R}$. The **norm** is

$$
\langle Q\rangle_{*} = Q\bar{Q} = (q+jq')(q-jq') = q^2 - q'^2 .
$$

It is a quadratic form of signature $(1,1)$, multiplicative under multiplication of the algebra,

$$
\langle QB\rangle_{*} = \langle Q\rangle_{*}\langle B\rangle_{*},
$$

and indefinite. Its sign partitions the algebra into three regions, which are the three regions of the Lorentzian plane.

| region | condition | sign of $\langle Q\rangle_{*}$ | contains |
|---|---|---|---|
| timelike | $\lvert q\rvert > \lvert q'\rvert$ | positive | the two sectors through $\pm1$ |
| null | $\lvert q\rvert = \lvert q'\rvert$ | zero | the null cone, the zero-divisor set |
| spacelike | $\lvert q\rvert < \lvert q'\rvert$ | negative | the two sectors through $\pm j$ |

The **null cone** is the pair of lines $q = \pm q'$, equivalently $\mathbb{R}\Pi_+ \cup \mathbb{R}\Pi_-$ with the idempotents $\Pi_\pm = \tfrac12(1\pm j)$. Away from the origin it is exactly the zero-divisor set: a nonzero element of zero norm has no inverse. The null cone is the boundary of the polar decomposition.

On the invertible set $\langle Q\rangle_{*}\neq0$ the **modulus** is

$$
r = \sqrt{\lvert \langle Q\rangle_{*}\rvert} = \sqrt{\lvert q^2-q'^2\rvert} > 0 .
$$

It is a positive square root of a non-negative real, with no sign or branch choice. It is multiplicative, because the norm is,

$$
r(QB) = r(Q)r(B).
$$

In the idempotent coordinates $Q = Q_+\Pi_+ + Q_-\Pi_-$, with $Q_\pm = q\pm q'$, the norm is the product $\langle Q\rangle_{*} = Q_+Q_-$, so the modulus is the geometric mean

$$
r = \sqrt{\lvert Q_+Q_-\rvert}.
$$

The modulus vanishes on the null cone, so it is not a norm: $r(1+j)=0$ while $1+j\neq0$. It is a multiplicative size on the group of units.

### The Unit Factor and the Unit Set

The **unit factor** of an invertible element is

$$
u = \frac{Q}{r}, \qquad \langle u\rangle_{*} = \frac{\langle Q\rangle_{*}}{r^2} = \operatorname{sign}\langle Q\rangle_{*} \in \{\pm1\}.
$$

The **unit set** is therefore

$$
\mathbb{D}^{(\pm1)} = \{\,u \in \mathbb{D} : \lvert \langle u\rangle_{*}\rvert = 1\,\} = \{\langle u\rangle_{*} = 1\} \sqcup \{\langle u\rangle_{*} = -1\},
$$

the union of the two hyperbolas $q^2-q'^2 = 1$ and $q'^2-q^2 = 1$. Each hyperbola has two branches, so the unit set has four connected components. With the hyperbolic angle $\phi \in \mathbb{R}$,

$$
\langle u\rangle_{*} = +1: \quad u = \pm\exp(\phi j) = \pm\bigl(\cosh\phi + j\sinh\phi\bigr),
$$

$$
\langle u\rangle_{*} = -1: \quad u = \pm j\exp(\phi j) = \pm\bigl(\sinh\phi + j\cosh\phi\bigr).
$$

The sign in front of the exponential is the branch sign, and $\phi$ is a coordinate on the branch, not a periodic angle. The phrase **unit factor** names the unit elements for the norm in view, the split norm $N$. It is not the **group of units** $\mathbb{D}^\times = \{\langle Q\rangle_{*}\neq0\}$, which is the wider set of invertible elements; the two senses of the word are kept apart throughout, as in *Conventions in Mathematics*, §*The Unitary Convention*.

### The Count of the Parameters

The decomposition has two real parameters on each component: the modulus $r>0$ and the branch coordinate $\phi\in\mathbb{R}$. The count matches the complex case, $2=1+1$; the range differs. On the circle the angle is a point of $\mathbb{R}/2\pi\mathbb{Z}$; on a branch the hyperbolic angle is a point of $\mathbb{R}$. The unit factor is one parameter and one discrete label.

## Existence and Uniqueness

**Theorem.** Every split-complex number $Q$ with $\langle Q\rangle_{*}\neq0$ has exactly one modulus–unit polar decomposition.

**Existence.** Put $r = \sqrt{\lvert \langle Q\rangle_{*}\rvert}$ and $u = Q/r$. Since $\langle Q\rangle_{*}\neq0$, $r>0$. Since $\langle \lambda Q\rangle_{*} = \lambda^2\langle Q\rangle_{*}$ for real $\lambda$, one has $\langle u\rangle_{*} = \langle Q\rangle_{*}/r^2 = \operatorname{sign}\langle Q\rangle_{*}$, so $\lvert \langle u\rangle_{*}\rvert = 1$. Hence $Q = ru$ with $r>0$ and $\lvert \langle u\rangle_{*}\rvert = 1$.

**Uniqueness.** Suppose $Q = ru = r_1u_1$ with $r,r_1>0$ and $\lvert \langle u\rangle_{*}\rvert = \lvert \langle u_1\rangle_{*}\rvert = 1$. Taking absolute values of the norm gives $r^2 = \lvert \langle Q\rangle_{*}\rvert = r_1^2$. Both are positive, so $r = r_1$. Dividing, $u = Q/r = u_1$.

The pair $(r,u)$ is unique, with no sign or branch ambiguity. The sign of the norm is a **regime**, forced by $\operatorname{sign}\langle u\rangle_{*} = \operatorname{sign}\langle Q\rangle_{*}$, so the modulus is always positive and the sign is carried by the unit factor. A negative real has positive modulus and unit factor $-1$; $j$ has modulus $1$ and unit factor $j$. The decomposition is defined exactly on $\mathbb{D}^\times = \{\langle Q\rangle_{*}\neq0\}$; on the null cone the modulus vanishes and the unit factor does not exist.

## The Group of Units and the Unit Set

### The Idempotent Coordinates and the Components

The group of units is $\mathbb{D}^\times = \{Q : \langle Q\rangle_{*}\neq0\}$. In the idempotent coordinates $Q = Q_+\Pi_+ + Q_-\Pi_-$ the multiplication is componentwise and

$$
\mathbb{D}^\times \cong \mathbb{R}^\times \times \mathbb{R}^\times, \qquad Q \longmapsto (Q_+,Q_-).
$$

Each factor $\mathbb{R}^\times$ has two components, so the product has four. The components are indexed by the signs of $Q_+$ and $Q_-$, equivalently by the four quadrants of the $(Q_+,Q_-)$ plane. Each component is an open quadrant in the $(Q_+,Q_-)$ coordinates, hence contractible and diffeomorphic to $\mathbb{R}^2$. The identity component is

$$
(\mathbb{D}^\times)_0 = \{Q : Q_+>0,\ Q_->0\} = \{q>\lvert q'\rvert\} = \{\langle Q\rangle_{*}>0,\ q>0\},
$$

the future cone of the indefinite form. It is the image of the exponential, treated in *Split-Complex Exponential and Lie Group Structure* and in *Exponential Polar Decomposition of Split-Complex Numbers*.

### The Polar Splitting of the Group

Every invertible element can be written in the normal form

$$
\boxed{\;Q = r\,\epsilon\,\exp(\phi j), \qquad r = \sqrt{\lvert \langle Q\rangle_{*}\rvert} > 0, \quad \phi \in \mathbb{R}, \quad \epsilon \in \{\pm1,\pm j\}\;}.
$$

The discrete factor $\epsilon$ records the component: $\epsilon = 1$ on the identity component, $\epsilon = -1$ on the opposite component, $\epsilon = j$ on the upper spacelike component and $\epsilon = -j$ on the lower spacelike component. The pair $(r,\phi)$ is the continuous part, and the triple $(r,\phi,\epsilon)$ is unique. The multiplication law is

$$
\boxed{\;(r_1,\phi_1,\epsilon_1)(r_2,\phi_2,\epsilon_2) = (r_1r_2,\ \phi_1+\phi_2,\ \epsilon_1\epsilon_2)\;},
$$

with $\epsilon_1\epsilon_2$ computed in the four-element group $\{\pm1,\pm j\}$, where $j^2 = 1$. Hence the polar decomposition read as a map is a group isomorphism

$$
\boxed{\;\mathbb{D}^\times \longrightarrow \mathbb{R}_{>0} \times \mathbb{R} \times (\mathbb{Z}/2\mathbb{Z})^2, \qquad Q \longmapsto (r,\phi,\epsilon)\;}.
$$

Equivalently, the map $(Q_+,Q_-)\mapsto(r,\phi,\operatorname{sign}Q_+,\operatorname{sign}Q_-)$ with $r=\sqrt{\lvert Q_+Q_-\rvert}$ and $\phi=\tfrac12\ln\lvert Q_+/Q_-\rvert$ is a diffeomorphism of $\mathbb{R}^\times\times\mathbb{R}^\times$ onto $\mathbb{R}_{>0}\times\mathbb{R}\times(\mathbb{Z}/2)^2$. The first factor is the scale, the second is the hyperbolic angle or rapidity, and the last two are the branch signs. The angle has no period: the unit factor ranges over a line, not over a circle.

### The Maximal Compact Subgroup

**Theorem.** The maximal compact subgroup of $\mathbb{D}^\times$ is the four-element group $\{\pm1,\pm j\}$, isomorphic to $(\mathbb{Z}/2\mathbb{Z})^2$.

**Proof.** Let $K\subset\mathbb{D}^\times$ be compact and let $Q = r\epsilon\exp(\phi j)$ be its polar form. The modulus $r : \mathbb{D}^\times\to\mathbb{R}_{>0}$ is a continuous homomorphism, so $r(K)$ is a compact subgroup of $\mathbb{R}_{>0}$, and the only such subgroup is $\{1\}$. The angle $\phi : \mathbb{D}^\times\to\mathbb{R}$ is also a continuous homomorphism, so $\phi(K)$ is a compact subgroup of the additive group $\mathbb{R}$, which is $\{0\}$. Hence $r=1$ and $\phi=0$ on $K$, and $K\subset\{\pm1,\pm j\}$. That four-element set is itself a compact subgroup, so it is the maximal one.

The contrast with the complex case is exact. There the group of units is $\mathbb{C}^\times\cong\mathbb{R}_{>0}\times\mathrm{U}(1)$, and the maximal compact subgroup is the circle $\mathrm{U}(1)$, connected and one-dimensional. Here the maximal compact subgroup is discrete of order four. There is no continuous compact factor: every compact subgroup lies in the four-element group.

### The Deformation Retraction

The unit set $\mathbb{D}^{(\pm1)}$ is a subgroup of $\mathbb{D}^\times$, because the product of two elements of norm $\pm1$ has norm $\pm1$, and the inverse of such an element has the same norm. The map

$$
H : [0,1]\times\mathbb{D}^\times \longrightarrow \mathbb{D}^\times, \qquad H(t,Q) = \Bigl((1-t)+\frac{t}{r(Q)}\Bigr)Q,
$$

is continuous, fixes every point of $\mathbb{D}^{(\pm1)}$ at every $t$, is the identity at $t=0$, and lands in $\mathbb{D}^{(\pm1)}$ at $t=1$. The group of units therefore deformation retracts onto the unit set. The unit set has four components, each homeomorphic to a line; a second retraction $\epsilon\exp(\phi j)\mapsto \epsilon\exp((1-t)\phi j)$ contracts each branch to its vertex, so $\mathbb{D}^\times$ deformation retracts onto $\{\pm1,\pm j\}$ and has the homotopy type of four points. In the complex case the same construction retracts $\mathbb{C}^\times$ onto the circle, which is already the maximal compact subgroup; here the first retract is the non-compact unit set of four branches, and a second retraction is needed.

## The Two Axes

### The Hermitian and Anti-Hermitian Directions

Conjugation fixes the real axis and negates the split-imaginary axis. An element $\nu$ is **Hermitian** if $\bar\nu = \nu$ and **anti-Hermitian** if $\bar\nu = -\nu$. The Hermitian elements are the real axis $\mathbb{R}$, and the anti-Hermitian elements are $j\mathbb{R}$. On the real axis the norm is $q^2$, positive definite; on the split-imaginary axis it is $-q'^2$, negative definite. Every nonzero element of either axis is invertible. The modulus lies on the positive real axis. The unit set meets the real axis at $\pm1$, where $N=1$, and the split-imaginary axis at $\pm j$, where $N=-1$. Thus $j$ is a unit direction of negative norm.

### The Roots of Plus One, Zero and Minus One

Let $\nu = q + jq'$ and solve $\nu^2 = c$ for $c\in\{-1,0,+1\}$. Since

$$
\nu^2 = (q^2+q'^2) + 2qq'\,j,
$$

the imaginary part vanishes when $qq' = 0$. The solutions are listed in the following table.

| equation | roots in $\mathbb{D}$ | row of the exponential | image of $t\mapsto\exp(\nu t)$ |
|---|---|---|---|
| $\nu^2 = -1$ | none | trigonometric | empty |
| $\nu^2 = 0$ | $\nu = 0$ | parabolic | $\{1\}$ |
| $\nu^2 = +1$ | $\nu = \pm1,\ \pm j$ | hyperbolic | $\mathbb{R}_{>0}$ for $\pm1$; the future branch of the hyperbola for $\pm j$ |

The trigonometric row is empty: $\mathbb{D}$ has no square root of $-1$. The parabolic row is degenerate: the only square-zero element is $0$, and $\exp(0)=1$. The hyperbolic row has four roots. The roots $\pm1$ generate the positive real scale $\exp(t)$, and the roots $\pm j$ generate the future branch $\exp(tj)=\cosh t+j\sinh t$ of the unit hyperbola; the past branch is reached by multiplying by $-1$. This is the exact exchange of the complex case, where $-1$ has the two roots $\pm i$ and $+1$ has the two roots $\pm1$; the split algebra moves the circle to the hyperbola and the compact generator to a non-compact one.

### Position and Signature

The two independent dichotomies of the family, position with respect to conjugation and the sign of the square of the direction, place the split unit factor in a slot that no definite algebra occupies.

| algebra | Hermitian direction | anti-Hermitian direction | unit factor |
|---|---|---|---|
| $\mathbb{C}$ | $\nu = \pm1$, $\nu^2 = +1$: the scale | $\nu = \pm i$, $\nu^2 = -1$ | anti-Hermitian, signature $-1$: the circle |
| $\mathbb{D}$ | $\nu = \pm1$, $\nu^2 = +1$: the scale | $\nu = \pm j$, $\nu^2 = +1$ | anti-Hermitian, signature $+1$: the hyperbola |

In $\mathbb{D}$ the generator $j$ is anti-Hermitian and has square $+1$, so the unit factor is the exponential of an anti-Hermitian direction of hyperbolic signature. In a definite algebra every anti-Hermitian direction has square $-1$, so every unit factor there is trigonometric and every unit group is compact. The discrete sign $\epsilon$ is not an exponential, because the image of the exponential is connected; it is the component label of the unit factor.

## The Matrix Picture

### Multiplication by j

In the real basis $\{1,j\}$ a split-complex number is the pair $(q,q')$, and multiplication by $Q = q+jq'$ is the linear map

$$
M_Q = \begin{pmatrix} q & q' \\ q' & q \end{pmatrix} = q\,I + q'\,K, \qquad K = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad K^2 = I .
$$

The matrix $K$ is a reflection, and $K^2 = I$ is the matrix form of $j^2 = +1$. The determinant and the trace are

$$
\det M_Q = q^2-q'^2 = \langle Q\rangle_{*}, \qquad \operatorname{tr}M_Q = 2q,
$$

so the norm is the determinant and the modulus is the square root of the absolute determinant, $r = \sqrt{\lvert\det M_Q\rvert}$.

### The Matrix of a Unit

For a unit $u = x+yj$ the matrix is

$$
M_u = x\,I + y\,K = \begin{pmatrix} x & y \\ y & x \end{pmatrix}, \qquad \lvert x^2-y^2\rvert = 1.
$$

It is symmetric, and its eigenvalues are $x+y$ and $x-y$. The four cases are as follows.

| regime | sign of $x$ | eigenvalues | definiteness of $M_u$ | orthogonal? |
|---|---|---|---|---|
| $\langle u\rangle_{*}=+1$ | $x>0$ | $x\pm y>0$ | positive definite | no, unless $u=\pm1$ |
| $\langle u\rangle_{*}=+1$ | $x<0$ | $x\pm y<0$ | negative definite | no, unless $u=\pm1$ |
| $\langle u\rangle_{*}=-1$ | $x>0$ or $x<0$ | opposite signs | indefinite | no, unless $u=\pm j$ |

The matrix $M_u$ is **not orthogonal** in general. Indeed

$$
M_u^{\mathsf T}M_u = M_u^2 = (x^2+y^2)I + 2xyK,
$$

which equals $I$ only when $x^2+y^2 = 1$ and $xy = 0$, that is only for $u\in\{\pm1,\pm j\}$. The algebraic unit factor and the orthogonal matrix factor of the Euclidean polar decomposition are different objects. In the complex case the two coincide because $M_u\in SO(2)$; in the split case they do not.

For a unit of norm $+1$ on the identity component, $x = \cosh\phi$ and $y = \sinh\phi$, so the eigenvalues are $\exp(\phi)$ and $\exp(-\phi)$, both positive. The matrix is symmetric positive definite; it is not orthogonal for the Euclidean metric, but it preserves the indefinite form because $\langle uv\rangle_{*} = \langle u\rangle_{*}\langle v\rangle_{*}$.

### The Matrix Polar Decomposition

Let $M_Q$ be an invertible matrix in the family, $M_Q = qI + q'K$. The Euclidean polar decomposition is $M_Q = PU$, with $P$ symmetric positive definite and $U$ orthogonal. Since $M_Q$ is symmetric, the factors are read from its eigenvalues $\lambda_1 = q+q'$ and $\lambda_2 = q-q'$.

| case | eigenvalues | $P$ | $U$ | determinant of $U$ |
|---|---|---|---|---|
| $\langle Q\rangle_{*}>0$, $q>0$ | both positive | $M_Q$ | $I$ | $+1$ |
| $\langle Q\rangle_{*}>0$, $q<0$ | both negative | $-M_Q$ | $-I$ | $+1$ |
| $\langle Q\rangle_{*}<0$ | opposite signs | $\lvert M_Q\rvert$ | reflection | $-1$ |

On the identity component the matrix is already positive definite, and the polar decomposition is $(M_Q,I)$. On the opposite component it is negative definite, and the polar decomposition is $(-M_Q,-I)$. On the spacelike region the eigenvalues have opposite signs, the positive factor is $\lvert M_Q\rvert$, and the orthogonal factor is a reflection with determinant $-1$. This is the precise form of the statement that the matrix polar factor is not the algebraic unit factor. In the complex case the two factors are $rI$ and $M_u\in SO(2)$; here the unit matrix is symmetric, and the orthogonal factor is either a sign or a reflection.

## Worked Examples

### A Generic Split-Complex Number

Take $Q = 5+3j$. Then $\langle Q\rangle_{*} = 25-9 = 16>0$, so

$$
r = 4, \qquad u = \frac{5+3j}{4} = 1.25+0.75j, \qquad \langle u\rangle_{*} = 1.5625-0.5625 = 1.
$$

The angle is fixed by $\tanh\phi = q'/q = 3/5$, hence

$$
\phi = \operatorname{artanh}\frac35 = \ln 2 = 0.6931471805599453,
$$

and

$$
\exp(\phi j) = \cosh\phi + j\sinh\phi = 1.25+0.75j = u.
$$

In the idempotent coordinates $Q_+ = 8$ and $Q_- = 2$, the modulus is the geometric mean $\sqrt{16} = 4$, and the angle is half the logarithm of their ratio, $\tfrac12\ln4 = \ln2$. The reconstruction $4(1.25+0.75j)$ is exact in the data.

### The Spacelike Regime

Take $Q = 1+2j$. Then $\langle Q\rangle_{*} = 1-4 = -3<0$, so

$$
r = \sqrt3 = 1.7320508075688772, \qquad u = \frac{1+2j}{\sqrt3} = 0.5773502691896258 + 1.1547005383792517\,j,
$$

and $\langle u\rangle_{*} = 1/3 - 4/3 = -1$. Here $u = j\exp(\phi j)$ with

$$
\phi = \operatorname{arsinh}\frac{1}{\sqrt3} = \operatorname{artanh}\frac{1}{2} = 0.5493061443340549,
$$

so that $\sinh\phi = 1/\sqrt3$ and $\cosh\phi = 2/\sqrt3$. The element $Q$ cannot be written with a unit factor of norm $+1$, because the sign of the norm is a regime.

### A Table of Examples

The following table applies the decomposition to elements of the four components and to the null cone.

| $Q$ | $\langle Q\rangle_{*}$ | $r$ | $u$ | $\langle u\rangle_{*}$ | $\epsilon$ | $\phi$ |
|---|---|---|---|---|---|---|
| $2$ | $4$ | $2$ | $1$ | $+1$ | $1$ | $0$ |
| $-2$ | $4$ | $2$ | $-1$ | $+1$ | $-1$ | $0$ |
| $j$ | $-1$ | $1$ | $j$ | $-1$ | $j$ | $0$ |
| $-j$ | $-1$ | $1$ | $-j$ | $-1$ | $-j$ | $0$ |
| $5+3j$ | $16$ | $4$ | $1.25+0.75j$ | $+1$ | $1$ | $\ln2$ |
| $1+2j$ | $-3$ | $\sqrt3$ | $0.5774+1.1547j$ | $-1$ | $j$ | $0.5493$ |
| $1+j$ | $0$ | — | — | — | — | no polar form |
| $\Pi_+$ | $0$ | — | — | — | — | no polar form |

The first four lines are the components. The fifth and sixth lines are the two nonzero-angle regimes. The last two lines are null: the modulus vanishes, the unit factor does not exist, and both are zero divisors.

### The Reconstruction Error

The reconstruction reproduces each invertible entry to machine precision, with error below $4\times10^{-16}$; the factorisation is exact in exact arithmetic.

## The Other Algebras

The modulus–unit decomposition exists in every algebra of the family, with the unit set of the norm in view.

| algebra | element | norm | modulus | unit set | topology of the unit set |
|---|---|---|---|---|---|
| $\mathbb{R}$ | $q$ | $q^2$ | $\lvert q\rvert$ | $\{\pm1\}$ | two points |
| $\mathbb{C}$ | $Q = q+iq'$ | $q^2+q'^2$, definite | $\sqrt{N}$ | $\mathrm{U}(1)$ | circle, compact and connected |
| $\mathbb{D}$ | $Q = q+jq'$ | $q^2-q'^2$, indefinite | $\sqrt{\lvert\langle Q\rangle_{*}\rvert}$, $\langle Q\rangle_{*}\neq0$ | $\{\langle Q\rangle_{*}=\pm1\}$ | four branches, non-compact |
| $\mathbb{H}$ | $\tilde q$ | sum of four squares, definite | $\sqrt{N}$ | $S^3$ | sphere, compact and connected |

The split column is the only one in which the norm is indefinite and the unit set has four components. The complex and quaternion columns are definite and their unit sets are compact and connected, a circle and a three-sphere. The split column has a non-empty null cone, a non-compact unit set, and a maximal compact subgroup of four points.

## Summary

Every split-complex number $Q$ with $\langle Q\rangle_{*}\neq0$ has exactly one modulus–unit polar decomposition $Q = ru$, with modulus $r = \sqrt{\lvert \langle Q\rangle_{*}\rvert}>0$ and unit factor $u = Q/r$ satisfying $\lvert \langle u\rangle_{*}\rvert = 1$. The sign of the norm is a regime, forced by $\operatorname{sign}\langle u\rangle_{*} = \operatorname{sign}\langle Q\rangle_{*}$; the unit factor has norm $+1$ in the timelike regime and $-1$ in the spacelike one. The unit set has four components, each a branch, parametrised as $\epsilon\exp(\phi j)$ with $\epsilon\in\{\pm1,\pm j\}$ and $\phi\in\mathbb{R}$.

The group of units splits as

$$
\mathbb{D}^\times \cong \mathbb{R}_{>0}\times\mathbb{R}\times(\mathbb{Z}/2\mathbb{Z})^2,
$$

the first factor the modulus, the second the hyperbolic angle, the last the four components. The maximal compact subgroup is $\{\pm1,\pm j\}\cong(\mathbb{Z}/2)^2$, discrete of order four, and it is a deformation retract of the group. There is no continuous compact factor: the complex circle has become four points.

Both axes are definite: the real axis has positive norm, the split-imaginary axis negative norm. The anti-Hermitian direction $j$ has square $+1$, so the unit factor is hyperbolic; there is no square root of $-1$, no trigonometric unit factor and no compact one-parameter group. The matrix of a unit is symmetric and generally not orthogonal; the matrix polar decomposition is $(M_Q,I)$ on the identity component, $(-M_Q,-I)$ on the opposite component, and $(\lvert M_Q\rvert,\text{reflection})$ on the spacelike region.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{D}$ | the split-complex algebra, basis $1$, $j$, $j^2=+1$ |
| $Q = q+jq'$ | a split-complex number, $q$ and $q'$ real |
| $\bar Q = q-jq'$ | the split-complex conjugate |
| $\langle Q\rangle_{*} = Q\bar Q = q^2-q'^2$ | the norm, indefinite of signature $(1,1)$ |
| $\Pi_\pm = \tfrac12(1\pm j)$ | the idempotents, $Q = Q_+\Pi_++Q_-\Pi_-$ |
| $Q_\pm = q\pm q'$ | the idempotent coordinates |
| $r = \sqrt{\lvert \langle Q\rangle_{*}\rvert} = \sqrt{\lvert Q_+Q_-\rvert}$ | the modulus, a positive real |
| $u = Q/r$ | the unit factor, $\lvert \langle u\rangle_{*}\rvert=1$ |
| $\epsilon$ | the component sign, an element of $\{\pm1,\pm j\}$ |
| $\phi$ | the hyperbolic angle or rapidity, $\phi\in\mathbb{R}$ |
| $\mathbb{D}^{(\pm1)}$ | the unit set $\{\lvert \langle Q\rangle_{*}\rvert=1\}$, four branches |
| $\mathbb{D}^\times = \{\langle Q\rangle_{*}\neq0\}$ | the group of units |
| $(\mathbb{D}^\times)_0 = \{q>\lvert q'\rvert\}$ | the identity component, the future cone |
| $K = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ | the reflection matrix of multiplication by $j$, $K^2=I$ |
| $M_Q = qI+q'K$ | the matrix of multiplication by $Q$, $\det M_Q=\langle Q\rangle_{*}$ |
| $M_u = xI+yK$ | the matrix of a unit, symmetric, generally not orthogonal |
| $O(1,1)$ | the Lorentz group of the plane, $\det=\pm1$ and form-preserving |
| $SO(1,1)$ | the determinant-one subgroup of $O(1,1)$, two components |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the polar form of split-complex numbers and the hyperbola as the unit locus.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split-complex algebra, its idempotents and its zero divisors.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the orthogonal groups, the circle and the Lorentz group of the plane.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for norms of arbitrary signature and the connected components of their isometry groups.
- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds* (Springer, Graduate Texts in Mathematics 149, 2nd ed. 2006), for hyperbolic geometry, its isometry groups and the parametrisation by rapidity.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for indefinite quadratic forms, their isotropic cones and their level sets.
