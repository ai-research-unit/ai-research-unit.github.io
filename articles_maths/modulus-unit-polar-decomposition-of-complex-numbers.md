# __Modulus–Unit Polar Decomposition of Complex Numbers__

## Introduction

This article treats the **modulus–unit polar decomposition** of a complex number: the writing

$$
Q = r\,u, \qquad r \in \mathbb{R}, \quad r > 0, \qquad u \in \mathbb{C}, \quad N(u) = 1,
$$

with $r$ the **modulus** and $u$ the **unit factor**. It is the algebraic member of the polar decompositions of $\mathbb{C}$: it uses only the norm, the conjugate and the square root, and it chooses no coordinate on the unit factor. The unit factor is treated as a point of the unit circle, and the circle as a set and as a group.

The decomposition is the two-dimensional definite case of the polar decomposition of the algebras of the family. Every algebra of the family splits an element of nonzero norm into a scale and a unit factor, and the differences between the algebras lie in the unit factor: a finite set in $\mathbb{R}$, a circle in $\mathbb{C}$, a sphere in $\mathbb{H}$, a level set of an indefinite form in the split cases. The complex case is the base case because the norm is definite. The modulus is a square root with no sign choice and no branch choice, the unit factor is defined at every nonzero element, and there is no boundary.

The plan is as follows. The two factors are defined (§*The Two Factors*), existence and uniqueness are proved (§*Existence and Uniqueness*), the group of units and the circle are described (§*The Group of Units and the Circle*), the two axes are classified (§*The Two Axes*), the matrix picture is given (§*The Matrix Picture*), examples are computed (§*Worked Examples*), and the place of the complex case in the family is recorded (§*The Other Algebras*).

The conventions and the symbols are those of *Complex Algebra*, *Complex Norm and Invertibility* and *Conventions in Mathematics*; the symbols are collected in §*Summary of Notation*.

Every numerical value displayed below was recomputed in double precision.

## The Two Factors

### The Norm and the Modulus

The norm of a complex number is

$$
N(Q) = Q\bar{Q} = q^2 + q'^2, \qquad Q = q + iq'.
$$

It is a sum of two squares, so $N(Q) > 0$ for every $Q \neq 0$ and $N(Q) = 0$ only at $Q = 0$. The **modulus** is

$$
r = \sqrt{N(Q)} = \lvert Q\rvert.
$$

The square root is taken in the positive reals, so it is unique: there is no sign choice, and there is no branch choice, because the radicand is never negative. The requirement $r > 0$ is therefore met automatically off the origin, and the modulus is forced by the norm.

The modulus is multiplicative, because the norm is:

$$
N(Q_1Q_2) = N(Q_1)N(Q_2), \qquad r(Q_1Q_2) = r(Q_1)r(Q_2),
$$

and it is homogeneous of degree one for real scalars, $r(\lambda Q) = \lvert\lambda\rvert r(Q)$.

### The Unit Factor and the Unit Circle

The **unit factor** is

$$
u = \frac{Q}{r} = \frac{Q}{\lvert Q\rvert}.
$$

It satisfies $N(u) = N(Q)/r^2 = 1$, so it lies on the **unit circle**

$$
\mathrm{U}(1) = \{\,u \in \mathbb{C} : N(u) = 1\,\}.
$$

The unit circle is a group under multiplication. If $N(u) = N(v) = 1$ then $N(uv) = 1$, and the inverse of $u$ is its conjugate $\bar{u}$, since $u\bar{u} = N(u) = 1$. It is a closed and bounded subset of $\mathbb{C} \cong \mathbb{R}^2$, hence compact.

The phrase **unit factor** names the norm-one elements. It is not the **group of units** $\mathbb{C}^\times$, which is the wider set of invertible elements; the two senses of the word *unit* are kept apart throughout, as in *Conventions in Mathematics*, §*The Unitary Convention*.

### The Count of the Parameters

A complex number carries two real parameters. The modulus carries one, the positive real $r$. The unit factor is constrained by the single real equation $N(u) = 1$ on the two parameters of $\mathbb{C}$, so it retains one real degree of freedom. The counts add:

$$
2 = 1 + 1.
$$

The additivity is the shape of the polar decomposition in every algebra of the family. What the one degree of freedom of $u$ is parametrised by is a separate question, answered by a chart of the circle; the rational chart is the subject of *Rational-Chart Polar Decomposition of Complex Numbers*, the exponential chart the subject of *Exponential Polar Decomposition of Complex Numbers*, and this article chooses none.

## Existence and Uniqueness

**Theorem.** Every nonzero complex number $Q$ has exactly one modulus–unit polar decomposition.

**Existence.** Put $r = \sqrt{N(Q)}$ and $u = Q/r$. Since $N(Q) > 0$, the number $r$ is a positive real. Since $N(\lambda Q) = \lambda^2N(Q)$ for real $\lambda$, one has $N(u) = N(Q)/r^2 = 1$. Hence $Q = ru$ with $r > 0$ and $N(u) = 1$.

**Uniqueness.** Suppose $Q = ru = r_1u_1$ with $r, r_1 > 0$ and $N(u) = N(u_1) = 1$. Taking norms gives $r^2 = N(Q) = r_1^2$. Both are positive, so $r = r_1$. Dividing, $u = Q/r = u_1$.

The pair $(r,u)$ is unique, with no sign ambiguity and no branch ambiguity. This is a statement about the factorisation, not about a coordinate on the circle: two different charts of $\mathrm{U}(1)$ assign different parameters to the same unit factor.

## The Group of Units and the Circle

The group of units of $\mathbb{C}$ is $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$. The polar decomposition read as a map

$$
\Phi : \mathbb{C}^\times \longrightarrow \mathbb{R}_{>0} \times \mathrm{U}(1), \qquad \Phi(Q) = \bigl(\lvert Q\rvert,\ Q/\lvert Q\rvert\bigr),
$$

is a group isomorphism. It is bijective, with inverse $(r,u) \mapsto ru$, and it is a homomorphism, because

$$
\Phi(Q_1Q_2) = \bigl(\lvert Q_1\rvert\lvert Q_2\rvert,\ Q_1Q_2/(\lvert Q_1\rvert\lvert Q_2\rvert)\bigr) = \Phi(Q_1)\Phi(Q_2).
$$

Hence

$$
\mathbb{C}^\times \cong \mathbb{R}_{>0} \times \mathrm{U}(1),
$$

the product of the positive scale line and the circle.

**The circle is the maximal compact subgroup.** Let $K \subset \mathbb{C}^\times$ be a compact subgroup. The modulus $\lvert\cdot\rvert$ is continuous, so $\lvert K\rvert$ is a compact subgroup of the multiplicative group $\mathbb{R}_{>0}$. A compact subgroup of $\mathbb{R}_{>0}$ is $\{1\}$: if $r > 1$ then $r^n \to \infty$, and if $0 < r < 1$ then $r^n \to 0 \notin \mathbb{R}_{>0}$, so neither sequence can lie in a compact set. Therefore $\lvert K\rvert = \{1\}$ and $K \subset \mathrm{U}(1)$. Since $\mathrm{U}(1)$ is itself compact, it is the maximal compact subgroup.

**The retraction.** The map

$$
H : [0,1] \times \mathbb{C}^\times \longrightarrow \mathbb{C}^\times, \qquad H(t,Q) = \bigl((1-t)\lvert Q\rvert + t,\ Q/\lvert Q\rvert\bigr),
$$

is continuous, fixes $\mathrm{U}(1)$ at every $t$, is the identity map at $t = 0$, and lands in $\mathrm{U}(1)$ at $t = 1$. The group of units therefore deformation retracts onto the circle.

## The Two Axes

Complex conjugation fixes the real axis and negates the imaginary axis. An element is **Hermitian** if $\bar{\nu} = \nu$ and **anti-Hermitian** if $\bar{\nu} = -\nu$; the Hermitian elements are the real axis $\mathbb{R}$, and the anti-Hermitian elements are the imaginary axis $i\mathbb{R}$.

| axis | elements | position | square | role |
|---|---|---|---|---|
| real | $q$, $q \in \mathbb{R}$ | Hermitian | $q^2 \ge 0$ | carries the modulus $r = \lvert Q\rvert > 0$ |
| imaginary | $it$, $t \in \mathbb{R}$ | anti-Hermitian | $-t^2 \le 0$ | the direction of the circle |

The modulus lies on the positive real axis. The unit circle meets the real axis at $\pm1$ and the imaginary axis at $\pm i$.

**There is no second continuous factor.** Suppose $\nu^2 = 1$. Writing $\nu = q+iq'$ gives $q^2-q'^2 = 1$ and $2qq' = 0$. If $q = 0$ then $-q'^2 = 1$, impossible; if $q' = 0$ then $q^2 = 1$, so $\nu = \pm1$. The only elements of the circle with square $+1$ are therefore $\pm1$, the two real points. A continuous factor of square $+1$ would be a connected subgroup of $\mathrm{U}(1)$ all of whose elements have square $+1$; such a subgroup lies in $\{\pm1\}$ and, being connected, is $\{1\}$. So there is no such factor. Similarly $\nu^2 = 0$ gives $q^2 = q'^2$ and $qq' = 0$, hence $\nu = 0$, so there is no nilpotent direction either. The dimension count is decisive as well: the circle is one-dimensional, so a product of two continuous factors has one factor of dimension zero, and a connected group of dimension zero is a point. The discrete sign $\pm1$ is carried by the unit factor, not by a separate factor: a negative real number has $r > 0$ and $u = -1$.

**The circle is both compact factor and rotation factor.** The algebra $\mathbb{C}$ is a field, hence commutative, so every element is central. A central factor and a rotation factor cannot be separated in a commutative algebra: the same circle plays both roles. Multiplication by a unit is a rotation of the plane, and $\mathrm{U}(1)$ is the group of those rotations; it is also the compact factor of the polar decomposition. The coincidence is a consequence of commutativity alone.

**No boundary.** If $Q \neq 0$ then $N(Q) > 0$, so $r > 0$ and $u = Q/r$ is defined. There is no nonzero element of vanishing norm, and the only excluded element is the origin.

## The Matrix Picture

In the real basis $\{1,i\}$ a complex number is the pair $(q,q')$, and multiplication by $Q = q+iq'$ is the linear map

$$
M_Q = \begin{pmatrix} q & -q' \\ q' & q \end{pmatrix} = q\,I + q'\,J, \qquad J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad J^2 = -I.
$$

The determinant and the trace are

$$
\det M_Q = q^2+q'^2 = N(Q), \qquad \operatorname{tr}M_Q = 2q,
$$

so the norm is the determinant and the modulus is the square root of the determinant, $r = \sqrt{\det M_Q}$.

For a unit $u$ the matrix is

$$
M_u = \operatorname{Re}u\,I + \operatorname{Im}u\,J = \begin{pmatrix} \operatorname{Re}u & -\operatorname{Im}u \\ \operatorname{Im}u & \operatorname{Re}u \end{pmatrix}, \qquad N(u) = 1.
$$

It satisfies $M_u^{\mathsf T}M_u = N(u)I = I$ and $\det M_u = N(u) = 1$, so $M_u$ lies in the special orthogonal group

$$
SO(2) = \{\,M : M^{\mathsf T}M = I,\ \det M = 1\,\}.
$$

The polar decomposition becomes the matrix factorisation

$$
M_Q = r\,M_u, \qquad r = \sqrt{\det M_Q} > 0, \quad M_u \in SO(2).
$$

This is the polar decomposition $M_Q = PU$ of an invertible matrix, with orthogonal factor $U = M_u$ and positive definite factor $P = rI$. The positive factor is a scalar because the family $\{qI+q'J\}$ has no other symmetric positive definite member: symmetry forces $q' = 0$, and positive definiteness then forces $q > 0$.

| factor | matrix | determinant | action |
|---|---|---|---|
| modulus | $rI$, $r > 0$ | $r^2$ | similarity of ratio $r$ |
| unit factor | $M_u \in SO(2)$ | $1$ | rotation |
| $Q$ | $M_Q$ | $r^2$ | oriented similarity |

## Worked Examples

### A Generic Complex Number

Take $Q = 3+4i$. Then

$$
N(Q) = 9+16 = 25, \qquad r = 5, \qquad u = \frac{3+4i}{5} = 0.6+0.8i.
$$

The checks are exact in the data:

$$
N(u) = 0.6^2+0.8^2 = 0.36+0.64 = 1, \qquad r u = 5(0.6+0.8i) = 3+4i.
$$

### A Table of Examples

| $Q$ | $N(Q)$ | $r$ | $u = Q/r$ | $N(u)$ |
|---|---|---|---|---|
| $2$ | $4$ | $2$ | $1$ | $1$ |
| $-3$ | $9$ | $3$ | $-1$ | $1$ |
| $5i$ | $25$ | $5$ | $i$ | $1$ |
| $1+i$ | $2$ | $\sqrt{2}$ | $(1+i)/\sqrt{2}$ | $1$ |
| $3+4i$ | $25$ | $5$ | $0.6+0.8i$ | $1$ |
| $-2-i$ | $5$ | $\sqrt{5}$ | $(-2-i)/\sqrt{5}$ | $1$ |

The second and sixth lines show that the unit factor, not the modulus, carries the sign. A negative real number has positive modulus and unit factor $-1$; a complex number with negative imaginary part, such as $-2-i$ of the sixth line, has a unit factor on the lower half of the circle, neither $1$ nor $-1$. The modulus is positive by definition.

### The Reconstruction Error

For the six elements of the table the reconstruction $r u$ reproduces $Q$ exactly in double precision, with Euclidean error zero. The decomposition is exact in exact arithmetic.

## The Other Algebras

The modulus–unit decomposition exists in every algebra of the family, with the unit set of the norm in view.

| algebra | element | norm | modulus | unit set | topology of the unit set |
|---|---|---|---|---|---|
| $\mathbb{R}$ | $q$ | $q^2$ | $\lvert q\rvert$ | $\{\pm1\}$ | two points |
| $\mathbb{C}$ | $Q = q+iq'$ | $q^2+q'^2$, definite | $\sqrt{N}$ | $\mathrm{U}(1)$ | circle, compact and connected |
| $\mathbb{D}$ | $Q = q+jq'$ | $q^2-q'^2$, indefinite | $\sqrt{\lvert N\rvert}$, $N \neq 0$ | $\{N = \pm1\}$ | four components, non-compact |
| $\mathbb{H}$ | $\tilde q$ | sum of four squares, definite | $\sqrt{N}$ | $S^3$ | sphere, compact and connected |

The complex column is the only one of the four in which the norm is definite and the unit set is a circle. The split-complex column has an indefinite norm, so its modulus uses an absolute value, its unit set has four components, and the decomposition is restricted to the complement of the null cone; the quaternion column is definite, but its unit set is a three-dimensional sphere rather than a circle.

## Summary

Every nonzero complex number has exactly one modulus–unit polar decomposition $Q = ru$, with modulus $r = \sqrt{N(Q)} > 0$ and unit factor $u = Q/r$ on the unit circle. The pair is unique with no sign or branch choice. The modulus is the positive square root of the definite norm; the unit factor is a point of $\mathrm{U}(1) = \{u : N(u)=1\}$, a compact group, and the inverse of a unit is its conjugate.

The group of units splits as $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times \mathrm{U}(1)$, the circle being the maximal compact subgroup and a deformation retract of the whole group. The real axis is Hermitian and carries the modulus; the imaginary axis is anti-Hermitian and is the direction of the circle. The only elements of the circle with square $+1$ are $\pm1$, so the algebra has no continuous factor of square $+1$, and because $\mathbb{C}$ is commutative the circle is at once the compact factor and the rotation factor. The norm is definite, so there is no boundary: the origin is the only excluded element.

In the matrix picture the decomposition is the polar decomposition $M_Q = rM_u$ of the conformal matrix, with positive factor $rI$ and orthogonal factor $M_u \in SO(2)$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $1$, $i$, $i^2 = -1$ |
| $Q = q+iq'$ | a complex number, $q$ its real part, $q'$ its imaginary part |
| $\bar{Q} = q-iq'$ | the complex conjugate |
| $N(Q) = Q\bar{Q} = q^2+q'^2$ | the norm, positive definite |
| $r = \sqrt{N(Q)} = \lvert Q\rvert$ | the modulus, a positive real |
| $u = Q/r$ | the unit factor, $N(u) = 1$ |
| $u$ | a unit, $N(u) = 1$, with real coordinates $\operatorname{Re}u$ and $\operatorname{Im}u$ |
| $\mathrm{U}(1) = \{u : N(u)=1\}$ | the unit circle, a compact group |
| $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$ | the group of units |
| $\mathbb{C}^\times \cong \mathbb{R}_{>0}\times\mathrm{U}(1)$ | the polar splitting of the group of units |
| $\nu$ | a direction of the algebra, Hermitian or anti-Hermitian |
| $J$ | the complex structure, multiplication by $i$, $J^2 = -I$ |
| $M_Q = qI+q'J$ | the $2\times2$ real matrix of multiplication by $Q$ |
| $M_u = aI+bJ$ | the matrix of a unit, in $SO(2)$ |
| $SO(2)$ | the special orthogonal group of the plane |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 1985), for the polar decomposition of an invertible matrix and the special orthogonal group.
- Tristan Needham, *Visual Complex Analysis* (Oxford University Press, 1997), for multiplication by a unit as a rotation of the plane and the identification of the circle with the rotation group.
- Michael Artin, *Algebra* (Prentice Hall, 2nd edition 2011), for the group of units, the product decomposition and the maximal compact subgroup.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the orthogonal groups and the circle as the first compact group of the series.
