
# __The Rotation Group and Orientation__

## Introduction

The orthogonal group of a quadratic space splits into two halves according to the sign of the determinant. The half of determinant one is the **rotation group**, and in the definite real case it carries the geometry of angles: its elements act as rotations, it is connected, and in the plane it is the circle group. This article develops that split, the notion of orientation that underlies it and its description through the determinant line, the parity of the Cartan–Dieudonné reflection length, the definite case and the measurement of angles, the normal form of a rotation, the finite rotation groups of the plane, and the rotation groups of the plane and of space.

The base is a field $F$ of characteristic not $2$, and $V$ is finite-dimensional, except where the definite real case is treated. The isometry group, reflections, the equal-norm lemma and the Cartan–Dieudonné theorem are taken from *Isometries and Orthogonal Transformations*; the polar form $B$ and the signature are those of *Quadratic Forms and Polarisation*. The orthogonal Lie algebra appears only in the last section, where the rotation of space is described infinitesimally; the Lie-theoretic development is not covered here.

## Orientation

### Oriented Vector Spaces

Let $V$ be a finite-dimensional real vector space of dimension $n$. Two ordered bases $\mathcal{B}$ and $\mathcal{B}'$ are **equivalently oriented** if the change-of-basis matrix has positive determinant. This is an equivalence relation with exactly two classes, and an **orientation** of $V$ is a choice of one class. A basis in the chosen class is **positively oriented**, and a linear isomorphism $T$ is **orientation-preserving** if $\det T > 0$ and **orientation-reversing** if $\det T < 0$. Writing $GL^+(V)$ for the orientation-preserving automorphisms, the sequence

$$
1 \longrightarrow GL^+(V) \longrightarrow GL(V) \xrightarrow{\ \det\ } \mathbb{R}^\times
$$

exhibits $GL^+(V)$ as the kernel of the determinant, and the two components of $GL(V)$ correspond to the two orientations.

An **oriented vector space** is a pair $(V, \omega)$ with $\omega$ one of the two orientation classes. Choosing the opposite orientation corresponds to replacing every basis by a basis of opposite parity, equivalently to composing with any orientation-reversing automorphism.

### The Determinant Line

The two orientations have a coordinate-free description through the top exterior power. Let $\Lambda^n V$ be the top exterior power of $V$, a one-dimensional real space, as in *The Exterior Algebra*.

**Proposition.** For $T \in GL(V)$ the induced map $\Lambda^n T$ on the one-dimensional space $\Lambda^n V$ is the multiplication by $\det T$. Consequently $\Lambda^n V \setminus \{0\}$ has two components, $GL(V)$ acts on them through the sign of the determinant, and $T$ is orientation-preserving exactly when it fixes each component.

**Proof.** For a basis $e_1, \ldots, e_n$ with $Te_j = \sum_i a_{ij}e_i$, functoriality of the exterior power gives

$$
\Lambda^n T(e_1 \wedge \cdots \wedge e_n) = Te_1 \wedge \cdots \wedge Te_n = (\det A)\, e_1 \wedge \cdots \wedge e_n,
$$

which is the classical determinantal description of the top exterior power; since $\Lambda^n V$ is one-dimensional, this determines $\Lambda^n T$ completely. A nonzero element of $\Lambda^n V$ is $t\,e_1\wedge\cdots\wedge e_n$ with $t \neq 0$, so the map $T$ multiplies the class of the oriented basis by the sign of $\det T$; the two signs correspond to the two components. $\square$

The statement is the algebraic reason the orientation sign exists: an orientation of $V$ is the same thing as one of the two components of the determinant line, and the sign of the determinant of an automorphism measures whether it interchanges them. Over a general field the same construction gives the parity of an automorphism whenever the two scalars $1$ and $-1$ are distinct, that is whenever the characteristic is not two.

### Orientation over a General Field

Over a general field the order of $\mathbb{R}$ is unavailable, and the two orientations are not distinguished by a sign in $F$. What survives is the **parity** of an automorphism, defined by $\det T = \pm 1$. For an isometry this parity is always defined, because $\det(T)^2 = 1$ for a non-degenerate form; let

$$
\operatorname{O}^+(V, q) = \{T \in \operatorname{O}(V, q) : \det T = 1\}, \qquad \operatorname{O}^-(V, q) = \{T \in \operatorname{O}(V, q) : \det T = -1\}.
$$

Over a field of characteristic not $2$ these are the two cosets of the special orthogonal group, and they have intrinsic meaning as the even and odd reflection lengths by the Cartan–Dieudonné parity of *Isometries and Orthogonal Transformations*. Over $\mathbb{R}$ and for a definite form they are the two connected components of the orthogonal group, and the identification with orientation is the statement that the determinant is positive exactly on the orientation-preserving isometries.

### The Volume Element of a Form

An orientation of $V$ and a non-degenerate symmetric form $q$ together determine a volume element. If $\mathcal{B} = (e_1, \ldots, e_n)$ is positively oriented and $G$ is the Gram matrix of $B$ in $\mathcal{B}$, then

$$
\omega_q = \sqrt{|\det G|}\; e_1 \wedge \cdots \wedge e_n
$$

is independent of the positively oriented basis chosen and changes sign under a change of orientation; it scales by $t^{n/2}$ when $q$ is replaced by $tq$. The construction is the algebraic form of the statement that a positive definite form on an oriented space determines a volume element, up to the choice of a positive scale.

For a non-degenerate form and a general field the algebraic substitute for the volume element is the **discriminant**,

$$
\Delta(q) = \det G \in F^\times/(F^\times)^2,
$$

which is independent of the basis, as in *Bilinear Forms*. The determinant changes by the square of the change-of-basis determinant, so the discriminant is insensitive to orientation: the two orientations of $V$ give the same discriminant.

### The Signed Discriminant

For a form of dimension $n$ the **signed discriminant** is

$$
d(q) = (-1)^{n(n-1)/2}\,\Delta(q).
$$

It differs from the discriminant by the factor $(-1)^{n(n-1)/2}$, which is the sign of the reversal of the $n$ factors in the product $e_1 \cdots e_n$ of a basis; equivalently, in the Clifford algebra of $q$ the square of the volume element is the scalar $d(q)$, as recorded. It is the more convenient invariant for the Witt theory, where it is shown to descend to a homomorphism on the fundamental ideal. Here we record only its behaviour, together with that of $\Delta$, under the two operations of the category:

$$
\Delta(q \perp q') = \Delta(q)\,\Delta(q'), \qquad \Delta(\langle a\rangle) = a, \qquad \Delta(cq) = c^{\,n}\,\Delta(q),
$$

$$
d(q \perp q') = (-1)^{n_1n_2}\,d(q)\,d(q'), \qquad d(\langle a\rangle) = a, \qquad d(cq) = c^{\,n}\,d(q),
$$

where $n_1, n_2$ are the dimensions of $q, q'$ and $n = n_1 + n_2$. The sign $(-1)^{n_1n_2}$ in the first relation for $d$ follows from $n(n-1)/2 = n_1(n_1-1)/2 + n_2(n_2-1)/2 + n_1n_2$. The sign in the definition of $d(q)$ is chosen so that $d$ is unchanged by adding a hyperbolic plane $\langle 1, -1\rangle$, whose discriminant is $-1$, whose dimension is $2$, and whose signed discriminant is therefore $(-1)^1(-1) = 1$.

### Reflections Reverse, Rotations Preserve

**Proposition.** Let $V$ be oriented and let $q$ be non-degenerate. Then the reflections $\tau_v$ are orientation-reversing and every element of $\operatorname{SO}(V, q)$ is orientation-preserving. A product of $k$ reflections is orientation-preserving exactly when $k$ is even.

**Proof.** Each reflection has $\det \tau_v = -1$ by *Isometries and Orthogonal Transformations*, and the determinant is multiplicative, so a product of $k$ reflections has determinant $(-1)^k$. Over $\mathbb{R}$ this determinant is the orientation sign. $\square$

The proposition is the bridge between the two descriptions of the special orthogonal group: it is both the kernel of the determinant and the group of even reflection products, and in the definite real case it is the group of orientation-preserving isometries.

## The Rotation Group

### Definition

**Definition.** The **rotation group** of a non-degenerate quadratic space $(V, q)$ is

$$
\operatorname{SO}(V, q) = \{T \in \operatorname{O}(V, q) : \det T = 1\}.
$$

It is a normal subgroup of $\operatorname{O}(V, q)$ of index two over a field of characteristic not $2$, and over $\mathbb{R}$ with a definite form it is the connected component of the identity, the kernel of the determinant being the complement of the orientation-reversing component.

**Example (the indefinite real case).** For the form $q(x, y) = x^2 - y^2$ on $\mathbb{R}^2$ the group $\operatorname{O}(1, 1)$ has four components, each homeomorphic to a line, and $\operatorname{SO}(1, 1)$ has two; the determinant does not detect them. The four-component structure of an indefinite orthogonal group is the reason the definite case is the one in which orientation and connected component coincide.

### Rotations and Reflections

By the Cartan–Dieudonné theorem every isometry is a product of reflections, and by the parity statement the elements of $\operatorname{SO}(V, q)$ are exactly the products of an even number of reflections. Two reflections generate a rotation, and the composition rule for two reflections in the plane is the composition rule for angles, developed below. The decomposition is not unique: a rotation of the plane is a product of two reflections in many ways, related by the freedom in choosing the first mirror.

**Proposition.** Let $\tau_u$ and $\tau_v$ be reflections in non-isotropic vectors $u, v$ that span a non-degenerate plane. Then $\tau_u \tau_v$ acts as the identity on the hyperplane $u^\perp \cap v^\perp$ and is a rotation on the plane $\operatorname{span}\{u, v\}$.

**Proof.** Both reflections fix $u^\perp \cap v^\perp$ pointwise, so the product does; the plane $\operatorname{span}\{u, v\}$ is invariant because each reflection preserves it, and the restriction has determinant $(-1)^2 = 1$ on that plane. Since the plane is non-degenerate, $\operatorname{span}\{u,v\}$ and $u^\perp \cap v^\perp$ are complementary. $\square$

## The Definite Case and Angles

### The Euclidean Structure

Let $V$ be a finite-dimensional real space with a **positive definite** form $q$, so that $B$ is an inner product. The pair $(V, B)$ is a Euclidean space, and the orthogonal group $\operatorname{O}(V, B)$ is the group of Euclidean isometries fixing the origin, a compact Lie group. The positive definite forms on $V$ are in bijection with the inner products, and each determines a norm

$$
\|v\| = \sqrt{q(v)}.
$$

**Theorem (Cauchy–Schwarz).** For all $u, v$ in a Euclidean space,

$$
|B(u, v)| \leq \|u\|\,\|v\|,
$$

with equality if and only if $u$ and $v$ are linearly dependent.

**Proof.** For all real $t$ the form is positive definite, so $q(u + tv) = q(u) + 2tB(u, v) + t^2 q(v)$ is non-negative. If $q(v) \neq 0$, the discriminant of this quadratic in $t$ is $4B(u, v)^2 - 4q(u)q(v) \leq 0$, giving the inequality; equality forces a double root, that is $u + tv = 0$ for some $t$. If $q(v) = 0$ then $v = 0$ and the statement is trivial. $\square$

### Angles

Cauchy–Schwarz shows that for nonzero $u, v$ the quotient $B(u, v)/(\|u\|\,\|v\|)$ lies in $[-1, 1]$, so there is a unique $\theta \in [0, \pi]$ with

$$
\cos\theta = \frac{B(u, v)}{\|u\|\,\|v\|}.
$$

The number $\theta$ is the **angle** between $u$ and $v$. It satisfies $\theta = 0$ exactly when $u, v$ are positive multiples, $\theta = \pi/2$ exactly when they are orthogonal, and $\theta = \pi$ exactly when they are negative multiples. Rescaling the form, $q \mapsto cq$ with $c > 0$, replaces $B$ by $cB$ and $\|v\|$ by $\sqrt{c}\,\|v\|$, so the quotient is unchanged: the angle depends only on the conformal class of the inner product.

A **rotation** of a Euclidean space is an element of $\operatorname{SO}(V, q)$. Rotations preserve the norm and the angle, so they are the angle-preserving linear maps, and the rotation group is the group of orientation-preserving Euclidean isometries of the space.

### The Plane Case: $SO(2)$

Let $V = \mathbb{R}^2$ with the standard positive definite form $q(x, y) = x^2 + y^2$. Orientation is fixed by the standard basis, and the rotation group consists of the matrices

$$
R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}, \qquad \theta \in \mathbb{R}.
$$

**Proposition.** The assignment $\theta \mapsto R(\theta)$ is a surjective homomorphism $\mathbb{R} \to \operatorname{SO}(2)$ with kernel $2\pi\mathbb{Z}$. Hence

$$
\operatorname{SO}(2) \cong \mathbb{R}/2\pi\mathbb{Z} \cong S^1,
$$

the unit circle, and $\operatorname{SO}(2)$ is abelian.

**Proof.** Matrix multiplication gives $R(\theta)R(\phi) = R(\theta + \phi)$ and $R(\theta)^{-1} = R(-\theta)$, so the map is a homomorphism; the kernel is the set of $\theta$ with $\cos\theta = 1$ and $\sin\theta = 0$, namely $2\pi\mathbb{Z}$. An orientation-preserving orthogonal $2 \times 2$ matrix has columns that are orthonormal and positively oriented, hence is of the form $R(\theta)$; this proves surjectivity. $\square$

**Proposition.** Every element of $SO(2)$ is a product of two reflections, and the angle of the rotation is twice the angle between the two mirror lines.

**Proof.** Let $\tau_\phi$ denote the reflection of the plane in the line at angle $\phi$ from the positive $x$-axis. A computation gives $\tau_\phi \tau_\psi = R(2(\phi - \psi))$, so the product of two reflections is a rotation through twice the angle between the lines, and every angle is achieved. $\square$

The parametrisation by the circle is the plane case of the general fact that a compact connected abelian Lie group is a torus; the higher-dimensional tori appear.

### The Finite Rotation Groups of the Plane

The subgroups of the circle that arise from finite symmetry are cyclic, and this is the simplest instance of the classification of finite rotation groups.

**Proposition.** Every finite subgroup of $\operatorname{SO}(2)$ is cyclic. If $H$ is finite and nontrivial, there is an integer $m \geq 1$ with

$$
H = \langle R(2\pi/m)\rangle \cong \mathbb{Z}/m\mathbb{Z},
$$

and $m$ is the order of $H$.

**Proof.** Let $A = \{\theta \in \mathbb{R}/2\pi\mathbb{Z} : R(\theta) \in H\}$, a finite subgroup of the circle group. If $A \neq 0$ let $\alpha$ be its smallest positive element; for any $\beta \in A$ write $\beta = k\alpha + \rho$ with $k$ an integer and $0 \leq \rho < \alpha$, so that $\rho = \beta - k\alpha \in A$, and minimality of $\alpha$ forces $\rho = 0$. Hence $A = \mathbb{Z}\alpha$, and finiteness forces $m\alpha \equiv 0$ modulo $2\pi$ for some $m \geq 1$, so $\alpha = 2\pi/m$ and $A$ has order $m$. $\square$

**Proposition.** Every finite subgroup of $\operatorname{O}(2)$ is cyclic or dihedral. In the second case the rotations in it form a cyclic subgroup of index two, and a reflection $s$ conjugates $R(\theta)$ to $R(-\theta)$.

**Proof.** Let $H$ be finite and let $H_0 = H \cap \operatorname{SO}(2)$, cyclic of order $m$ by the previous proposition. If $H_0 = H$ the group is cyclic. Otherwise $H$ contains a reflection $s$, and every element of $H$ is either a rotation or $s$ composed with one, so $H_0$ has index two. With $s = \tau_{(0,1)} = \operatorname{diag}(1, -1)$,

$$
s\,R(\theta)\,s^{-1} = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta\end{pmatrix} = R(-\theta),
$$

so $s$ conjugates the cyclic group to itself, and $H$ is the dihedral group of order $2m$. $\square$

## The Normal Form of a Rotation

### The Invariant Planes

Euler's theorem generalises: a rotation of a definite space of any dimension is a product of planar rotations in mutually orthogonal planes.

**Theorem (normal form of a rotation).** Let $V$ be a finite-dimensional real space with a positive definite form $q$ and let $T \in \operatorname{SO}(V, q)$. Then there is an orthonormal basis of $V$ in which $T$ is the block diagonal matrix

$$
T = \operatorname{diag}\bigl(R(\theta_1), \ldots, R(\theta_m), \underbrace{1, \ldots, 1}_{n - 2m}\bigr), \qquad 0 < \theta_1 \leq \cdots \leq \theta_m \leq \pi,
$$

where $2m = n - \dim\ker(T - \mathrm{id})$ is the number of eigenvalues of $T$, counted with multiplicity, that differ from $1$; equivalently $2m$ is the codimension of the fixed subspace. In particular $T$ fixes pointwise a subspace of dimension $n - 2m$, and the multiset $\{\theta_1, \ldots, \theta_m\}$ is determined by $T$: the angles $\theta_j < \pi$ are read off from the non-real eigenvalues $e^{\pm i\theta_j}$, and $\theta_j = \pi$ corresponds to a pair of eigenvalues $-1$.

**Proof.** Because $T$ preserves $q$, every complex eigenvalue has modulus one: if $Tv = \lambda v$ with $v \neq 0$ then $q(v) = q(Tv) = |\lambda|^2 q(v)$, and $q(v) > 0$ gives $|\lambda| = 1$. The characteristic polynomial is real, so the non-real eigenvalues occur in conjugate pairs $\lambda, \bar\lambda$ with $\lambda \neq \bar\lambda$, and each such pair has $\lambda = \cos\theta + i\sin\theta$ for a unique $\theta \in (0, \pi)$. If $z = u + iv$ is an eigenvector for $\lambda$, then $u, v$ are real, linearly independent vectors of equal norm with $B(u, v) = 0$, and separating real and imaginary parts of $Tz = \lambda z$ gives

$$
Tu = (\cos\theta)\,u - (\sin\theta)\,v, \qquad Tv = (\sin\theta)\,u + (\cos\theta)\,v,
$$

so $W = \operatorname{span}\{u, v\}$ is a $T$-invariant plane on which $T$ acts as $R(\theta)$ after scaling $u, v$ to unit length. Distinguish now the pairs $\{\lambda, \bar\lambda\}$: if $v_\lambda$ and $w_\mu$ are eigenvectors for eigenvalues with $\lambda \neq \mu$ and $\lambda\mu \neq 1$, then

$$
B(v_\lambda, w_\mu) = B(Tv_\lambda, Tw_\mu) = \lambda\mu\,B(v_\lambda, w_\mu)
$$

so $B(v_\lambda, w_\mu) = 0$ whenever $\lambda\mu \neq 1$. For two distinct conjugate pairs the eigenvalues are $\lambda = e^{i\theta}$ and $\mu = e^{i\theta'}$ with $\theta \neq \theta'$ in $(0, \pi)$, so $\lambda\bar\mu = e^{i(\theta - \theta')} \neq 1$ and therefore $B(v_\lambda, \bar w_\mu) = 0$; conjugating this real-bilinear relation gives $B(\bar v_\lambda, w_\mu) = 0$ as well, and the two identities together give $B(x, y) = 0$ for every $x$ in the real plane of the pair $\lambda$ and every $y$ in the real plane of the pair $\mu$, since those planes are spanned by the real and imaginary parts of $v_\lambda$ and $w_\mu$. The same argument with $\mu = \pm 1$ shows that the planes are orthogonal to the eigenspaces $V_1$ and $V_{-1}$. The space therefore decomposes as an orthogonal direct sum of the planes $W$ and of the two eigenspaces, and the restriction of the positive definite form to each summand is again positive definite. Choose orthonormal bases: on $V_1$ the map is the identity, on $V_{-1}$ it is minus the identity, and on each plane $W$ it is the planar rotation $R(\theta_j)$. The determinant of $T$ is the product of the determinants of these restrictions, hence equals $(-1)^{k}$ where $k = \dim V_{-1}$; since $\det T = 1$ the number $k$ is even, and pairing the basis vectors of $V_{-1}$ exhibits that eigenspace as a sum of blocks $R(\pi)$. The multiset of angles is read off from the eigenvalues of $T$, which are invariants of $T$. $\square$

**Corollary.** For a positive definite form the group $\operatorname{SO}(V, q)$ is path-connected, and $\operatorname{O}(V, q)$ has exactly two components, the cosets of $\operatorname{SO}(V, q)$.

**Proof.** With the normal form in hand, the path $t \mapsto \operatorname{diag}(R(t\theta_1), \ldots, R(t\theta_m), 1, \ldots, 1)$ for $t \in [0, 1]$ runs from the identity to $T$ inside $\operatorname{SO}(V, q)$. Hence $\operatorname{SO}(V, q)$ is path-connected, and since a reflection exists for $n \geq 1$ the determinant is surjective onto $\{\pm 1\}$ and $\operatorname{O}(V, q)$ has two components. $\square$

**Remark.** In dimension three the theorem reads $m = 1$ and $n - 2m = 1$: a rotation fixes a line pointwise and rotates the orthogonal plane, which is Euler's theorem below. In dimension four the two possibilities $m = 1$ and $m = 2$ occur; the rotations with $m = 2$ have no fixed vector, which is the case mentioned in the next section. The normal form is the definite case of the Cartan decomposition of an orthogonal group, and the indefinite analogue has hyperbolic blocks $H(u)$ in place of the circular blocks $R(\theta)$.

## The Rotation Group of Space

### The Axis of a Rotation

Let $V = \mathbb{R}^3$ with the standard positive definite form. The elements of $\operatorname{SO}(3)$ are the rotations of space, and each has an axis.

**Theorem (Euler).** Every $T \in \operatorname{SO}(3)$ fixes a nonzero vector, the **axis** of the rotation, and acts on the orthogonal plane $v^\perp$ as a rotation through some angle $\theta$.

**Proof.** For any orthogonal $T$,

$$
T^T(T - I) = I - T^T = -(T - I)^T, \qquad \det\bigl(T^T(T - I)\bigr) = \det(T - I) = (-1)^{3}\det(T - I) = -\det(T - I),
$$

using $\det T = 1$ and $\det T^T = 1$ for the left side and $n = 3$ for the right. Hence $2\det(T - I) = 0$, and since $2 \neq 0$ in $\mathbb{R}$, $\det(T - I) = 0$: there is a nonzero $v$ with $Tv = v$. If $v$ is chosen with $q(v) = 1$, then $T$ preserves $v^\perp$ (as in *Isometries and Orthogonal Transformations*), and the restriction of $T$ to the plane $v^\perp$ is an element of $\operatorname{SO}(2)$, hence a rotation through some angle. $\square$

**Remark.** The argument uses that the dimension is odd; in even dimension a rotation need not have an axis. A rotation of $\mathbb{R}^4$ can be a product of two independent planar rotations with no fixed vector, which is the geometric content of the double-cover phenomena treated with the quaternions.

### Angles, Axes and the Matrix Form

A rotation $T$ of $\mathbb{R}^3$ with axis a unit vector $v = (v_1, v_2, v_3)$ and angle $\theta$ is given by Rodrigues' formula

$$
T(x) = x\cos\theta + (v \times x)\sin\theta + v\,B(v, x)(1 - \cos\theta),
$$

where $\times$ denotes the vector product and $B$ the Euclidean inner product. For $v = (0, 0, 1)$ this reduces to the block form $\operatorname{diag}(R(\theta), 1)$. The vector product is itself a bilinear form on $\mathbb{R}^3$ with values in $\mathbb{R}^3$, alternating in its two arguments, and it singles out the three-dimensional case among the vector products; the corresponding Lie-theoretic statement is the isomorphism $\mathfrak{so}(3) \cong \mathbb{R}^3$.

**Remark.** The unit quaternions form a group that double covers $\operatorname{SO}(3)$, the axis-angle data being recovered from the real and vector parts of a unit quaternion; the description of this cover, and its complex and indefinite analogues, belongs to the applications of the Clifford layer of this category, written in parallel with this article.

## Summary

An **orientation** of a finite-dimensional real space is one of the two equivalence classes of ordered bases under positive-determinant change of basis; an automorphism is orientation-preserving when its determinant is positive. Over a general field the intrinsic substitute for the orientation sign is the **parity** $\det T = \pm 1$, which for an isometry of a non-degenerate form is always available: the isometries split into the two cosets $\operatorname{O}^+(V, q)$ and $\operatorname{O}^-(V, q)$ of the rotation group. An orientation together with a non-degenerate form $q$ gives a **volume element** $\sqrt{|\det G|}\,e_1 \wedge \cdots \wedge e_n$, while the algebraic invariant of the form alone is the **discriminant** $\Delta(q) = \det G \in F^\times/(F^\times)^2$ and the **signed discriminant** $d(q) = (-1)^{n(n-1)/2}\Delta(q)$.

The **rotation group** $\operatorname{SO}(V, q)$ is the kernel of the determinant on $\operatorname{O}(V, q)$; it is normal of index two over a field of characteristic not $2$, and over $\mathbb{R}$ with a definite form it is the identity component. Its elements are exactly the products of an even number of reflections: each reflection reverses orientation and has determinant $-1$, so a product of $k$ reflections is a rotation precisely when $k$ is even. Two reflections generate a rotation acting on the plane spanned by their vectors.

In the **definite real case** the form is an inner product, Cauchy–Schwarz bounds the quotient $B(u, v)/(\|u\|\,\|v\|)$ by $1$ in absolute value, and the **angle** $\theta \in [0, \pi]$ is defined by its cosine; rotations are the angle-preserving orientation-preserving isometries. For the plane, $\operatorname{SO}(2)$ is the circle group $\mathbb{R}/2\pi\mathbb{Z}$, abelian and parametrised by $R(\theta)$, and every rotation is a product of two reflections with the angle doubled. For space, **Euler's theorem** says every $T \in \operatorname{SO}(3)$ has an axis, a fixed line on which the rotation acts trivially, and is a rotation through an angle on the orthogonal plane; the axis-angle form is Rodrigues' formula.

Orientation has a coordinate-free form: an orientation is a choice of one of the two components of the determinant line $\Lambda^n V \setminus \{0\}$, and the induced map $\Lambda^n T$ is the multiplication by $\det T$, which measures the parity of an automorphism over any field of characteristic not two.

**Normal form of a rotation.** For a positive definite form every $T \in \operatorname{SO}(V, q)$ is, in a suitable orthonormal basis, a diagonal sequence of planar rotation blocks $R(\theta_1), \ldots, R(\theta_m)$ with $0 < \theta_j \leq \pi$ and $n - 2m$ entries $1$, the angles being determined by $T$; the codimension $2m$ block is the fixed subspace. Consequently $\operatorname{SO}(V, q)$ is path-connected and $\operatorname{O}(V, q)$ has exactly two components; in dimension three the normal form is Euler's theorem. The finite subgroups of $\operatorname{SO}(2)$ are the cyclic groups $\langle R(2\pi/m)\rangle$, and every finite subgroup of $\operatorname{O}(2)$ is cyclic or dihedral.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | Field, of characteristic not $2$ unless stated |
| $V$ | Finite-dimensional $F$-space, or real space in the definite case |
| $q$ | Non-degenerate quadratic form on $V$ |
| $B$ | Polar form of $q$, $q(v) = B(v, v)$ |
| $G$ | Gram matrix of $B$ in a basis |
| $\det T$ | Determinant of a linear map |
| $GL(V)$, $GL^+(V)$ | General linear group, orientation-preserving automorphisms |
| $\operatorname{O}(V, q)$ | Orthogonal group of $q$ |
| $\operatorname{O}^\pm(V, q)$ | Cosets of determinant $\pm 1$ |
| $\operatorname{SO}(V, q)$ | Rotation group, isometries of determinant $+1$ |
| $\tau_v$ | Reflection in the non-isotropic vector $v$ |
| $\omega_q$ | Volume element $\sqrt{|\det G|}\,e_1 \wedge \cdots \wedge e_n$ |
| $\Delta(q)$ | Discriminant $\det G \in F^\times/(F^\times)^2$ |
| $d(q)$ | Signed discriminant $(-1)^{n(n-1)/2}\Delta(q)$ |
| $\|v\| = \sqrt{q(v)}$ | Norm in the definite real case |
| $\theta$ | Angle between two vectors, or angle of a rotation |
| $R(\theta)$, $S(\theta)$ | Rotation and reflection matrices of the plane |
| $H(u)$ | Hyperbolic rotation of the plane $x^2 - y^2$ |
| $\Lambda^n V$ | Top exterior power, the determinant line |
| $\theta_1, \ldots, \theta_m$ | Rotation angles in the normal form |
| $S^1$ | Unit circle, $\operatorname{SO}(2)$ |
| $\times$ | Vector product on $\mathbb{R}^3$ |
| $\mathbb{R}, \mathbb{C}$ | Real and complex numbers |





## Further Reading

- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1971), for the orthogonal groups, their components and the reflection parity.
- Larry C. Grove, *Classical Groups and Geometric Algebra*, Graduate Studies in Mathematics 39 (American Mathematical Society, 2002), for the Cartan–Dieudonné theorem and the rotation groups of low-dimensional real spaces.
- Michael Artin, *Algebra* (Prentice Hall, 1991), for orientation, the determinant and the geometry of the classical groups.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270 (Springer, 1985), for the discriminant and the structure of the orthogonal group.
- Morton L. Curtis, *Matrix Groups* (Springer, 1984), for the rotation groups of the plane and of space and their parametrisations.
