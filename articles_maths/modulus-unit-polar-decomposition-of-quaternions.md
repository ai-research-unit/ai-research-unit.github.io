# __Modulus–Unit Polar Decomposition of Quaternions__

## Introduction

This article treats the **modulus–unit polar decomposition** of a quaternion: the writing

$$ \boxed{\; \tilde q = r\,\tilde u_{\mathrm r}, \qquad r \in \mathbb{R}, \quad r > 0, \qquad \tilde u_{\mathrm r} \in \mathbb{H}, \quad \langle\tilde u_{\mathrm r}\rangle_{\natural} = 1 \;} ,$$

with $r$ the **modulus** and $\tilde u_{\mathrm r}$ the **unit factor**. It is the algebraic member of the polar decompositions of $\mathbb{H}$: it uses only the norm, the conjugate and the square root, and it chooses no coordinate on the unit factor. The unit factor is also called the **rotor**: a unit real quaternion is a rotor (*Conventions in Mathematics*, §*Symbols*), and the subscript $\mathrm r$ records the name. The exponential article writes it as $\tilde u_{\mathrm r}=\exp(\theta\vec n)$; the sandwich by it rotates by $2\theta$, so the exponent angle $\theta$ is the half-angle of the rotor (*Exponential Polar Decomposition of Quaternions*, §*The Rotor Part*). The unit factor is treated as a point of the unit sphere $S^3$, and the sphere as a set, as a manifold and as a group.

The decomposition is the four-dimensional definite case of the polar decomposition of the algebras of the family. Every algebra of the family splits an invertible element into a scale and a unit factor, and the differences between the algebras lie in the unit factor: a finite set in $\mathbb{R}$, a circle in $\mathbb{C}$, a sphere in $\mathbb{H}$, a level set of an indefinite form in the split cases. The complex case is the base case because the norm is definite and the unit group is abelian. The quaternion case is the first definite case in which the unit group is non-abelian, and the first in which the unit set is neither finite nor a circle; both changes are visible in the group of units, in the matrix picture and in the absence of a second continuous factor.

The plan is as follows. The two factors are defined (§*The Two Factors*), existence and uniqueness are proved (§*Existence and Uniqueness*), the group of units and the sphere are described (§*The Group of Units and the Sphere*), the two subspaces are classified (§*The Two Axes*), the matrix picture is given (§*The Matrix Picture*), examples are computed (§*Worked Examples*), and the place of the quaternion case in the family is recorded (§*The Other Algebras*).

The conventions and the symbols are those of *Quaternion Algebra*, *Norm and Invertibility in the Quaternion Algebra* and *Conventions in Mathematics*; the symbols are collected in §*Summary of Notation*.

Every numerical value displayed below was recomputed in double precision.

## The Two Factors

### The Quaternion Norm and the Modulus

The quaternion norm of $\tilde q = q_t e_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ is

$$
\langle\tilde q\rangle_{\natural} = \tilde q\tilde q^{\natural} = \tilde q^{\natural}\tilde q = q_t^2+q_x^2+q_y^2+q_z^2 .
$$

It is a sum of four squares, so it is strictly positive on the nonzero quaternions and vanishes only at the origin. It is real valued and central, $\langle\tilde q\rangle_{\natural}\in\mathbb{R}$, and it is multiplicative:

$$
\langle\tilde q_1\tilde q_2\rangle_{\natural} = \langle\tilde q_1\rangle_{\natural}\langle\tilde q_2\rangle_{\natural}.
$$

The **modulus** is its positive square root,

$$
r = \sqrt{\langle\tilde q\rangle_{\natural}} .
$$

The radicand is non-negative and vanishes only at $\tilde q=0$, so on the nonzero quaternions the square root is a strictly positive real number, with no sign choice and no branch choice. The requirement $r>0$ is met automatically, and the modulus is forced by the norm. It is multiplicative and positively homogeneous,

$$
\sqrt{\langle\tilde q_1\tilde q_2\rangle_{\natural}} = \sqrt{\langle\tilde q_1\rangle_{\natural}}\,\sqrt{\langle\tilde q_2\rangle_{\natural}}, \qquad \sqrt{\langle\lambda\tilde q\rangle_{\natural}} = \lvert\lambda\rvert\,\sqrt{\langle\tilde q\rangle_{\natural}} \quad (\lambda\in\mathbb{R}).
$$

### The Unit Factor and the Unit Sphere

The **unit factor** is

$$
\tilde u_{\mathrm r} = \frac{\tilde q}{r} = \frac{\tilde q}{\sqrt{\langle\tilde q\rangle_{\natural}}} .
$$

It satisfies $\langle\tilde u_{\mathrm r}\rangle_{\natural} = \langle\tilde q\rangle_{\natural}/r^2 = 1$, so it lies on the **unit sphere**

$$ \boxed{\; \mathrm{Sp}(1) = \{\,\tilde u\in\mathbb{H} : \langle\tilde u\rangle_{\natural} = 1\,\} = S^3 \;} .$$

The sphere is a group under multiplication. If $\langle\tilde u_1\rangle_{\natural} = \langle\tilde u_2\rangle_{\natural} = 1$ then multiplicativity gives $\langle\tilde u_1\tilde u_2\rangle_{\natural}=1$, and the inverse of a unit is its conjugate, $\tilde u^{-1}=\tilde u^{\natural}$, because $\tilde u\tilde u^{\natural}=1$. The sphere is a closed and bounded subset of $\mathbb{H}\cong\mathbb{R}^4$, hence compact, and it is connected. It is not abelian: $\vec e_x\vec e_y=\vec e_z$ while $\vec e_y\vec e_x=-\vec e_z$. The complex unit circle is abelian, and this is the first structural difference between the two cases.

The phrase **unit factor** names the norm-one elements. It is not the **group of units** $\mathbb{H}^{\times}$, which is the wider set of invertible elements; the two senses of the word *unit* are kept apart throughout, as in *Conventions in Mathematics*, §*The Unitary Convention*. In $\mathbb{H}$ every nonzero element is invertible, so $\mathbb{H}^{\times}=\mathbb{H}\setminus\{0\}$, but the unit factor is the smaller set of norm-one elements.

### The Count of the Parameters

A quaternion carries four real parameters. The modulus carries one, the positive real $r$. The unit factor is constrained by the single real equation $\langle\tilde u_{\mathrm r}\rangle_{\natural}=1$ on the four parameters of $\mathbb{H}$, so it retains three real degrees of freedom. The counts add:

$$
4 = 1+3 .
$$

The three is the dimension of the sphere $S^3$, not a triple of scalar parameters: no coordinate on the sphere has been chosen. What the three degrees of freedom are parametrised by is a separate question, answered by a chart of the sphere. The rational chart is the subject of *Rational-Chart Polar Decomposition of Quaternions*, the exponential chart the subject of *Exponential Polar Decomposition of Quaternions*, and this article chooses none.

## Existence and Uniqueness

**Theorem.** Every nonzero quaternion has exactly one modulus–unit polar decomposition.

**Existence.** Put $r=\sqrt{\langle\tilde q\rangle_{\natural}}$ and $\tilde u_{\mathrm r}=\tilde q/r$. Since $\langle\tilde q\rangle_{\natural}>0$, the number $r$ is a positive real. Since the norm is homogeneous of degree two, $\langle\tilde u_{\mathrm r}\rangle_{\natural}=\langle\tilde q\rangle_{\natural}/r^2=1$. Hence $\tilde q=r\tilde u_{\mathrm r}$ with $r>0$ and $\langle\tilde u_{\mathrm r}\rangle_{\natural}=1$.

**Uniqueness.** Suppose $\tilde q=r\tilde u_{\mathrm r}=r'\tilde u_{\mathrm r}'$ with $r,r'>0$ and $\langle\tilde u_{\mathrm r}\rangle_{\natural}=\langle\tilde u_{\mathrm r}'\rangle_{\natural}=1$. Taking norms gives $r^2=\langle\tilde q\rangle_{\natural}=r'^2$. Both are positive, so $r=r'$. Dividing, $\tilde u_{\mathrm r}=\tilde q/r=\tilde u_{\mathrm r}'$.

The pair is unique, with no sign ambiguity and no branch ambiguity. The two quaternions $\tilde q$ and $-\tilde q$ have the same modulus and opposite unit factors; the sign is carried by the unit factor, not by the modulus. This is a statement about the factorisation, not about a coordinate on the sphere: two different charts assign different parameters to the same unit factor.

## The Group of Units and the Sphere

### The Splitting of the Group of Units

The group of units of $\mathbb{H}$ is $\mathbb{H}^{\times}=\mathbb{H}\setminus\{0\}$. The polar decomposition read as a map

$$
\Phi : \mathbb{H}^{\times} \longrightarrow \mathbb{R}_{>0}\times S^3, \qquad \Phi(\tilde q) = \bigl(\sqrt{\langle\tilde q\rangle_{\natural}},\ \tilde q/\sqrt{\langle\tilde q\rangle_{\natural}}\bigr),
$$

is a group isomorphism. It is bijective, with inverse $(r,\tilde u_{\mathrm r})\mapsto r\tilde u_{\mathrm r}$, and it is a homomorphism, because the modulus is multiplicative and positive and because the scalar modulus is central:

$$
\Phi(\tilde q_1\tilde q_2) = \bigl(\sqrt{\langle\tilde q_1\rangle_{\natural}}\sqrt{\langle\tilde q_2\rangle_{\natural}},\ \tilde q_1\tilde q_2/(\sqrt{\langle\tilde q_1\rangle_{\natural}}\sqrt{\langle\tilde q_2\rangle_{\natural}})\bigr) = \Phi(\tilde q_1)\Phi(\tilde q_2).
$$

Hence

$$ \boxed{\; \mathbb{H}^{\times} \cong \mathbb{R}_{>0}\times S^3 \;} ,$$

the product of the positive scale line and the unit sphere. The product is direct because every positive real is central: the two factors commute, and their intersection is the identity.

### The Maximal Compact Subgroup

**Proposition.** The unit sphere $S^3$ is the maximal compact subgroup of $\mathbb{H}^{\times}$.

**Proof.** Let $K\subset\mathbb{H}^{\times}$ be a compact subgroup. The modulus is continuous, so the image of $K$ under the modulus is a compact subgroup of the multiplicative group $\mathbb{R}_{>0}$. A compact subgroup of $\mathbb{R}_{>0}$ is $\{1\}$: if $r>1$ then $r^n\to\infty$, and if $0<r<1$ then $r^n\to0\notin\mathbb{R}_{>0}$, so neither sequence can lie in a compact set. Therefore the image is $\{1\}$ and $K\subset S^3$. Since $S^3$ is itself compact, it is the maximal compact subgroup.

### The Deformation Retraction

The map

$$
H : [0,1]\times\mathbb{H}^{\times} \longrightarrow \mathbb{H}^{\times}, \qquad H(t,\tilde q) = \bigl((1-t)\sqrt{\langle\tilde q\rangle_{\natural}}+t,\ \tilde q/\sqrt{\langle\tilde q\rangle_{\natural}}\bigr),
$$

is continuous, fixes $S^3$ at every $t$, is the identity at $t=0$, and lands in $S^3$ at $t=1$. The group of units therefore deformation retracts onto the sphere, and the inclusion $S^3\hookrightarrow\mathbb{H}^{\times}$ is a homotopy equivalence. In particular the group of units is connected and simply connected, with $\pi_1(\mathbb{H}^{\times})=0$ and $\pi_3(\mathbb{H}^{\times})\cong\mathbb{Z}$, against $\pi_1(\mathbb{C}^{\times})=\mathbb{Z}$ for the complex case. The fundamental group of the rotation group, $\mathbb{Z}/2$, belongs to the quotient $S^3/\{\pm1\}\cong SO(3)$ and not to the units.

### The Absence of a Second Continuous Factor

The sphere is **simple modulo its centre**. Its Lie algebra is $\mathfrak{so}(3)$, which is simple, and the only proper normal subgroups of $S^3$ are $\{1\}$ and the centre $\{\pm1\}$; the quotient by the centre is the rotation group,

$$
S^3/\{\pm1\} \cong SO(3).
$$

Suppose that $S^3$ were a direct product $A\times B$ of two connected Lie groups of positive dimension. The factors would be connected normal subgroups of $S^3$, hence each would be $\{1\}$ or $S^3$, and one factor would be trivial. The sphere therefore has no product decomposition with two positive-dimensional factors. The connected normal subgroups of $S^3$ are exhausted by the trivial group and the whole sphere, because their Lie algebras are ideals of the simple algebra $\mathfrak{so}(3)$.

The group of units does split, $\mathbb{H}^{\times}\cong\mathbb{R}_{>0}\times S^3$, but the only factor beyond the sphere is the **central scale line**. That factor is one-dimensional and central, and it cannot be moved into the sphere. There is no circle factor and no hyperbolic line factor inside the sphere, in contrast with the split cases, where the unit set itself contains a hyperbolic line. The dimension count confirms the shape: $4=1+3$, and the three is irreducible.

## The Two Axes

### The Scalar and Vector Subspaces

Quaternion conjugation fixes the scalar part and negates the vector part:

$$
\tilde q^{\natural} = q_t e_t - q_x\vec e_x - q_y\vec e_y - q_z\vec e_z .
$$

An element is **Hermitian** if $\tilde\nu^{\natural}=\tilde\nu$ and **anti-Hermitian** if $\tilde\nu^{\natural}=-\tilde\nu$. The Hermitian elements are the scalar line $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_t$, and the anti-Hermitian elements are the pure quaternions

$$
\operatorname{Im}\mathbb{H} = \{\,q_x\vec e_x+q_y\vec e_y+q_z\vec e_z\,\}.
$$

The algebra splits as a direct sum of vector spaces,

$$
\mathbb{H} = \mathbb{R}_{\mathbb{H}}\oplus\operatorname{Im}\mathbb{H}, \qquad 4=1+3 .
$$

The scalar line is a subalgebra. The pure subspace is not: the product of two pure quaternions has a scalar part, $\vec v\vec w=-\vec v\cdot\vec w+\vec v\times\vec w$. The modulus lies on the scalar axis, and the unit sphere meets that axis at $\pm e_t$. Every unit quaternion other than $\pm e_t$ has a nonzero vector part, and it is written $\cos\theta+\vec n\sin\theta$ with $\vec n$ a unit pure quaternion and $\theta\in(0,\pi)$; this is the axis-angle form developed in *Exponential Polar Decomposition of Quaternions*.

### The Roots of Plus One, Zero and Minus One

Let $\tilde\nu=q_t e_t+\vec v$ with $\vec v$ pure and solve $\tilde\nu^2=c$ for $c\in\{-1,0,+1\}$. Since

$$
\tilde\nu^2=(q_t^2-\langle\vec v\rangle_{\natural})e_t+2q_t\vec v,
$$

the vector part vanishes when $q_t=0$ or $\vec v=0$. The solutions are listed in the following table.

| equation | roots in $\mathbb{H}$ | row of the exponential | image of $t\mapsto\exp(\tilde\nu t)$ |
|---|---|---|---|
| $\tilde\nu^2=-1$ | $\tilde\nu=\vec n$, a unit pure quaternion: the sphere $S^2$ | trigonometric | the circle $\cos t+\vec n\sin t$ |
| $\tilde\nu^2=0$ | $\tilde\nu=0$ | parabolic | $\{1\}$ |
| $\tilde\nu^2=+1$ | $\tilde\nu=\pm1$ | hyperbolic | $\mathbb{R}_{>0}$ for both signs |

The trigonometric row is the whole sphere $S^2$ of unit pure quaternions, not two points: this is the first place where the quaternion case differs from the complex and split-complex cases, where $-1$ has two roots and none respectively. The parabolic row is degenerate, as in the split case: the only square-zero element is $0$, and $\exp(0)=1$. The hyperbolic row has the two central roots $\pm1$, each of which generates the positive scale line. The unit sphere is generated by the roots of $-1$, and the negative real axis is reached from them at $\sqrt{\langle\vec v\rangle_{\natural}}=\pi$.

### Position and Signature

| subspace | elements | dimension | conjugation | norm | role |
|---|---|---|---|---|---|
| scalar $\mathbb{R}_{\mathbb{H}}$ | $q_t e_t$ | $1$ | fixed, Hermitian | $q_t^2\ge0$ | carries the modulus $r=\sqrt{\langle\tilde q\rangle_{\natural}}$ |
| vector $\operatorname{Im}\mathbb{H}$ | $q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ | $3$ | negated, anti-Hermitian | $q_x^2+q_y^2+q_z^2\ge0$ | the axis of the rotor |

Both subspaces are definite, unlike the split-quaternion case, where the pure subspace carries an indefinite form. The modulus is a positive scalar, the rotor is a unit sphere, and the sphere meets the scalar axis only at the two central points.

**No boundary.** If $\tilde q\neq0$ then $\langle\tilde q\rangle_{\natural}>0$, so $r>0$ and $\tilde u_{\mathrm r}=\tilde q/r$ is defined. There is no nonzero element of vanishing norm, and the only excluded element is the origin. This is the sharpest contrast with the split cases, where the null cone removes a whole hypersurface and the polar decomposition is defined only off it.

## The Matrix Picture

### The Embedding in M_2(C)

The algebra $\mathbb{H}$ embeds in $M_2(\mathbb{C})$ by

$$
\iota(e_t)=\begin{pmatrix}1&0\\0&1\end{pmatrix}, \qquad
\iota(\vec e_x)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}, \qquad
\iota(\vec e_y)=\begin{pmatrix}0&-1\\1&0\end{pmatrix}, \qquad
\iota(\vec e_z)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$

On a general quaternion,

$$
\iota(\tilde q)=\begin{pmatrix}q_t-iq_z&-iq_x-q_y\\-iq_x+q_y&q_t+iq_z\end{pmatrix}.
$$

Two identities hold. The determinant is the quaternion norm,

$$
\det\iota(\tilde q)=q_t^2+q_x^2+q_y^2+q_z^2=\langle\tilde q\rangle_{\natural},
$$

and the image of the unit sphere is the special $*$-unitary group,

$$
\iota\bigl(\mathrm{Sp}(1)\bigr)=SU(2).
$$

The image of $\mathbb{H}$ is the real subspace of matrices of the form $\begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix}$ with $\alpha,\beta\in\mathbb{C}$; it is a real form of $M_2(\mathbb{C})$, not the whole algebra.

### The Matrix of a Unit

For a unit $\tilde u_{\mathrm r}$ the matrix $M_{\tilde u}=\iota(\tilde u_{\mathrm r})$ satisfies

$$
M_{\tilde u}^{\dagger}M_{\tilde u}=I, \qquad \det M_{\tilde u}=1,
$$

so $M_{\tilde u}\in SU(2)$. Conversely every matrix of $SU(2)$ is the image of a unit quaternion, because the determinant condition is the norm-one condition in these coordinates. The polar decomposition becomes the matrix factorisation

$$
M_{\tilde q}=r\,M_{\tilde u}, \qquad r=\sqrt{\det M_{\tilde q}}>0, \quad M_{\tilde u}\in SU(2).
$$

### The Matrix Polar Decomposition

Let $B=M_{\tilde q}$. Since $\iota$ is an algebra homomorphism and $\iota(\tilde q^{\natural})=B^{\dagger}$, the norm identity reads

$$
B^{\dagger}B = \iota(\tilde q^{\natural}\tilde q) = \langle\tilde q\rangle_{\natural}I = r^2 I .
$$

The matrix $B$ is therefore conformal: its columns are orthogonal and of equal length $r$. The general polar decomposition of an invertible matrix is $B=PU$, with $P=(BB^{\dagger})^{1/2}$ positive definite Hermitian and $U$ $*$-unitary. Here $P=rI$ and $U=M_{\tilde u}\in SU(2)$, so the positive factor is a scalar and the $*$-unitary factor is special. The scalar factor is forced because the only positive definite Hermitian matrices in the image of $\mathbb{H}$ are the positive real multiples of the identity.

| factor | matrix | determinant | action |
|---|---|---|---|
| modulus | $rI$, $r>0$ | $r^2$ | similarity of ratio $r$ |
| unit factor | $M_{\tilde u}\in SU(2)$ | $1$ | rotation of the sphere |
| $\tilde q$ | $M_{\tilde q}$ | $r^2$ | conformal map |

In the split cases the matrix of a unit is not orthogonal: the form it preserves is indefinite, so the matrix is symmetric or hyperbolic rather than $*$-unitary. The contrast is a property of the norm and not of the matrix representation.

## Worked Examples

### A Generic Quaternion

Take

$$
\tilde q = e_t+2\vec e_x+3\vec e_y+4\vec e_z .
$$

The quaternion norm is $\langle\tilde q\rangle_{\natural}=1+4+9+16=30$, so the modulus is

$$
r=\sqrt{30}=5.477225575\ldots,
$$

and the unit factor is

$$
\tilde u_{\mathrm r}=\frac{\tilde q}{\sqrt{30}}=0.182574186\,e_t+0.365148372\,\vec e_x+0.547722558\,\vec e_y+0.730296743\,\vec e_z .
$$

The checks are exact in the data: $\langle\tilde u_{\mathrm r}\rangle_{\natural}=1$ to $2.2\times10^{-16}$, and $r\tilde u_{\mathrm r}$ reproduces $\tilde q$ to $4.4\times10^{-16}$ in each coefficient.

### A Table of Examples

| $\tilde q$ | $\langle\tilde q\rangle_{\natural}$ | $r$ | $\tilde u_{\mathrm r}=\tilde q/r$ | $\langle\tilde u_{\mathrm r}\rangle_{\natural}$ |
|---|---|---|---|---|
| $2e_t$ | $4$ | $2$ | $e_t$ | $1$ |
| $-3e_t$ | $9$ | $3$ | $-e_t$ | $1$ |
| $\vec e_x$ | $1$ | $1$ | $\vec e_x$ | $1$ |
| $3\vec e_x-4\vec e_z$ | $25$ | $5$ | $0.6\vec e_x-0.8\vec e_z$ | $1$ |
| $e_t+\vec e_x$ | $2$ | $\sqrt{2}$ | $(e_t+\vec e_x)/\sqrt{2}$ | $1$ |
| $e_t+2\vec e_x+3\vec e_y+4\vec e_z$ | $30$ | $\sqrt{30}$ | the unit factor above | $1$ |

The second line shows that the unit factor, not the modulus, carries the sign. A negative real quaternion has positive modulus and unit factor $-e_t$. The third line is a pure unit: its modulus is one and its unit factor is itself; the fourth line has modulus five and is not a unit, and its unit factor is $0.6\vec e_x-0.8\vec e_z$. The fifth line has unit factor $(e_t+\vec e_x)/\sqrt{2}$, a rotor of a quarter turn about $\vec e_x$: its square is $\vec e_x$, which is the check of the half-angle rule of the exponential article.

### The Reconstruction Error

For the six elements of the table the reconstruction $r\tilde u_{\mathrm r}$ reproduces $\tilde q$ to double precision; the largest coefficient error is $4.4\times10^{-16}$, attained on the generic element. The decomposition is exact in exact arithmetic.

## The Other Algebras

The modulus–unit decomposition exists in every algebra of the family, with the unit set of the norm in view. The table records the element, the norm, its signature, the modulus and the unit set; the last column records the topology.

| algebra | element | norm | signature | modulus | unit set | topology of the unit set |
|---|---|---|---|---|---|---|
| $\mathbb{R}$ | $q$ | $q^2$ | $(1,0)$ | $\lvert q\rvert$ | $\{\pm1\}$ | two points |
| $\mathbb{C}$ | $Q=q+iq'$ | $q^2+q'^2$ | $(2,0)$ | $\sqrt{\langle Q\rangle_{*}}$ | $\mathrm{U}(1)$ | circle, compact and connected |
| $\mathbb{D}$ | $Q=q+jq'$ | $q^2-q'^2$ | $(1,1)$ | $\sqrt{\lvert\langle Q\rangle_{*}\rvert}$, $\langle Q\rangle_{*}\neq0$ | $\{\langle Q\rangle_{*}=\pm1\}$ | four components, non-compact |
| $\mathbb{H}$ | $\tilde q$ | $q_t^2+q_x^2+q_y^2+q_z^2$ | $(4,0)$ | $\sqrt{\langle\tilde q\rangle_{\natural}}$ | $S^3=\mathrm{Sp}(1)$ | sphere, compact, connected, simply connected |
| $\mathbb{H}_{\mathrm{s}}$ | $\tilde q$ | $q_t^2+q_x^2-q_y^2-q_z^2$ | $(2,2)$ | $\sqrt{\lvert\langle\tilde q\rangle_{\natural}\rvert}$, $\langle\tilde q\rangle_{\natural}\neq0$ | $\{\langle\tilde q\rangle_{\natural}=\pm1\}$ | two components, non-compact |

The quaternion column is the first definite column whose unit set is neither finite nor a circle. The split-complex column has an indefinite norm, so its modulus uses an absolute value, its unit set has four components, and the decomposition is restricted to the complement of the null cone. The split-quaternion column has signature $(2,2)$; its norm-one set is $\mathrm{SL}_2(\mathbb{R})$, a non-compact three-dimensional group, and its full unit set $\{\langle\tilde q\rangle_{\natural}=\pm1\}$ has two connected components. Only the real, complex and quaternion columns have a definite norm, and among them the quaternion unit set is the only one that is non-abelian.

## Summary

Every nonzero quaternion has exactly one modulus–unit polar decomposition $\tilde q=r\tilde u_{\mathrm r}$, with modulus $r=\sqrt{\langle\tilde q\rangle_{\natural}}>0$ and unit factor $\tilde u_{\mathrm r}=\tilde q/r$ on the unit sphere. The pair is unique with no sign or branch choice. The modulus is a positive central scale, and the unit factor is a point of $S^3=\mathrm{Sp}(1)$, a compact, connected, simply connected, non-abelian group.

The group of units splits as $\mathbb{H}^{\times}\cong\mathbb{R}_{>0}\times S^3$, the sphere being the maximal compact subgroup and a deformation retract of the whole group. The scalar line is Hermitian and carries the modulus; the pure subspace is anti-Hermitian and is the axis of the rotor. The sphere is simple modulo its centre $\{\pm1\}$, with quotient $SO(3)$, so there is no second continuous factor. The norm is definite, so there is no boundary: the origin is the only excluded element.

In the matrix picture the decomposition is the polar decomposition $M_{\tilde q}=rM_{\tilde u}$ of the conformal matrix, with positive factor $rI$ and special $*$-unitary factor $M_{\tilde u}\in SU(2)$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra, basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$ |
| $\tilde q=q_t e_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ | a quaternion, $q_t$ its scalar part, $\vec q$ its vector part |
| $\tilde q^{\natural}=q_t e_t-\vec q$ | the quaternion conjugate |
| $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}=\sum_\mu q_\mu^2$ | the quaternion norm, positive definite |
| $r=\sqrt{\langle\tilde q\rangle_{\natural}}$ | the modulus, a positive real |
| $\tilde u_{\mathrm r}=\tilde q/r$ | the unit factor, of norm one |
| $\mathrm{Sp}(1)=S^3=\{\tilde u:\langle\tilde u\rangle_{\natural}=1\}$ | the unit sphere, a compact group |
| $\mathbb{H}^{\times}=\mathbb{H}\setminus\{0\}$ | the group of units |
| $\mathbb{H}^{\times}\cong\mathbb{R}_{>0}\times S^3$ | the polar splitting of the group of units |
| $\mathbb{R}_{\mathbb{H}}$ | the scalar line, the Hermitian subspace |
| $\operatorname{Im}\mathbb{H}$ | the pure quaternions, the anti-Hermitian subspace |
| $SO(3)\cong S^3/\{\pm1\}$ | the rotation group, the adjoint quotient |
| $\iota$ | the embedding $\mathbb{H}\to M_2(\mathbb{C})$ |
| $M_{\tilde q}$ | the matrix of $\tilde q$ |
| $M_{\tilde u}\in SU(2)$ | the matrix of a unit factor |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 1985), for the polar decomposition of an invertible matrix and the special $*$-unitary group.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd edition 2001), for the quaternion algebra, the unit sphere and the exponential.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for $SU(2)$, the unit quaternions and the covering of the rotation group.
- Michael Artin, *Algebra* (Prentice Hall, 2nd edition 2011), for the group of units, direct products and the maximal compact subgroup.
