
# __Comparison of Norms and Invertibility__

## Introduction

This article compares the norm and the invertibility theory of the eight algebras $\mathbb{R}, \mathbb{C}, \mathbb{D}, \mathbb{D}', \mathbb{H}, \mathbb{H}_{\mathrm{s}}, \mathbb{B}, \mathbb{H}_{\mathbb{D}}$. It states the norm of each, its signature and its definiteness, the form it polarises to, the multiplicativity that makes it a size function, the invertibility criterion it supplies, the group of units it cuts out, the topology of that group of units with its homotopy type, its components and its fundamental group, the classification of the elements by its sign, and the place of each algebra in the two polar series, in tables with the eight algebras as columns in the fixed order of *The Eight Algebras Compared*. Every entry restates a result of the eight norm articles and of the polar representation articles, cited to their sections. The factors into which the unit factor splits are the subject of *Comparison of the Polar Element Representation*, and the exponential of the unit factor is the subject of *Comparison of the Exponential and Lie Group Structure*.

The organising thread is the **signature of the norm**. Where the form is definite, the algebra is a division algebra, its unit group has a compact factor, and the polar decomposition has no boundary; where the form is indefinite, degenerate or ring-valued, the algebra has zero divisors, its unit group is non-compact, and the polar decomposition has a boundary that is the zero-divisor set. The ladder crosses the boundary once, between the distinct columns $\mathbb{C}$ and $\mathbb{D}$, where one sign in the norm changes and the whole analysis changes with it.

## The Norms

The following table compares the norm of the eight algebras: its formula, its signature, its definiteness, its isotropy, the Euclidean norm it polarises to, and the zero divisors it detects. The eight algebras are the columns, in the fixed order.

| norm | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| formula | $x^2$ | $a^2+b^2$ | $a^2-b^2$ | $a^2$ | $\sum_k q_k^2$ | $q_0^2+q_1^2-q_2^2-q_3^2$ | $\sum_\mu Q_\mu^2$ | $\sum_\mu Q_\mu^2$ |
| values in | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ |
| signature | $(1,0)$ | $(2,0)$ | $(1,1)$ | rank $1$, degenerate | $(4,0)$ | $(2,2)$ | complex-valued | split complex-valued |
| definiteness | definite | definite | indefinite | semidefinite | definite | indefinite | indefinite | anisotropic |
| isotropy | none | none | two null lines | nilpotent line | none | null cone | zero-divisor cone | none |
| Euclidean norm | $\lvert x\rvert$ | $\sqrt{N}$ | $\sqrt{a^2+b^2}$ | $\sqrt{a^2+b^2}$ | $\sqrt{N}$ | $\sqrt{\sum_k q_k^2}$ | $\sqrt{\sum_\mu\lvert Q_\mu\rvert^2}$ | $\sqrt{\sum_\mu(q_\mu^2+q'_\mu{}^2)}$ |
| norm multiplicative | yes | yes | yes | yes | yes | yes | yes | yes |
| Euclidean norm multiplicative | yes | yes | no | no | yes | no | no | no |
| zero divisors detected | none | none | $N=0$ | $N=0$ | none | $N=0$ | $N=0$ | by components |

The table divides at the column $\mathbb{D}$. The norm is multiplicative in every one of the eight columns, while the Euclidean norm that carries the topology is multiplicative only in the definite columns $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ and fails in the degenerate and the split columns. Left of $\mathbb{D}$ the norm takes real values; at $\mathbb{D}$ it takes the value $a^2-b^2$ and becomes **isotropic**, that is, it vanishes on the two null lines $\mathbb{R}(1\pm j)$ (*Split-Complex Norm and Invertibility*, §*The Norm*). The dual numbers carry the degeneracy to its limit: $N(Z)=a^2$ has rank one, it depends only on the real part, its radical is the maximal ideal $\mathrm{M}=(\varepsilon)$, and the Euclidean norm $\sqrt{a^2+b^2}$ that carries the topology is positive definite but **not** multiplicative (*Dual-Numbers Norm and Invertibility*, §*The Norm*; §*The Euclidean Form*). At the quaternion rung the sign returns: $N(\tilde q)=\sum q_k^2$ is positive definite of signature $(4,0)$ (*Quaternion Norm and Invertibility*, §*The Quaternion Norm*), and it is at the next column that the sign is exchanged again, $q_0^2+q_1^2$ becoming $q_0^2+q_1^2-q_2^2-q_3^2$ of signature $(2,2)$, the isotropic vectors satisfying $q_0^2+q_1^2=q_2^2+q_3^2$ (*Split-Quaternion Norm and Invertibility*, §*Isotropy*).

The last two columns are of a different kind, and the table records the difference rather than hiding it. In $\mathbb{B}$ the norm is complex-valued, the *semi-norm* of the literature; it is not positive definite, it vanishes on the zero-divisor cone, and of the usual norm axioms only the sign axiom survives, the triangle inequality being inapplicable to a complex value and the scaling axiom failing for complex scalars (*Biquaternion Norm and Invertibility*, §*The Biquaternion Norm as a Semi-Norm*). In $\mathbb{H}_{\mathbb{D}}$ the norm is split complex-valued and **anisotropic**: it vanishes only at the origin, because in the idempotent basis it is the pair of quaternion norms $N(\tilde Q)=(N(\tilde Q_+),N(\tilde Q_-))$ of the two components, and $\mathbb{H}$ is a division algebra. The consequence is stated in the last row: the norm of $\mathbb{H}_{\mathbb{D}}$ does **not** detect the zero divisors, and the criterion must be stated in terms of the ring $\mathbb{D}$ rather than of the value zero (*Split-Biquaternion Norm and Invertibility*, §*The Split-Biquaternion Norm*).

## The Quadratic and Hermitian Forms

Each norm is the diagonal of a bilinear or Hermitian form on the underlying real space, and the following table compares those forms and the Euclidean norm they supply. The eight algebras are the columns, in the fixed order.

| form | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| polarised form | $xy$ | $\operatorname{Re}(\bar ZW)$ | $ac-bd$ | $ac$ | $\operatorname{Sc}(p\bar{\tilde q})$ | $\operatorname{Sc}(p\bar{\tilde q})$ | $\operatorname{Sc}(\tilde P\tilde Q^\dagger)$ | $\operatorname{Sc}(\tilde P\tilde Q^\dagger)$ |
| Hermitian form | $xx$ | $Z\bar Z$ | $Z\bar Z$ | $Z\bar Z$ | $\tilde q\bar{\tilde q}$ | $\tilde q\bar{\tilde q}$ | $\tilde Q\tilde Q^\dagger$ | $\tilde Q\tilde Q^\dagger$ |
| Hermitian form scalar part | $x^2$ | $a^2+b^2$ | $a^2-b^2$ | $a^2$ | $\sum_kq_k^2$ | $q_0^2+q_1^2-q_2^2-q_3^2$ | $\sum_\mu\lvert Q_\mu\rvert^2$ | $\sum_\mu(q_\mu^2-q'_\mu{}^2)$ |
| signature of scalar part | $(1,0)$ | $(2,0)$ | $(1,1)$ | rank $1$ | $(4,0)$ | $(2,2)$ | $(8,0)$ | $(4,4)$ |

The table separates the two roles the norm plays. As a **quadratic form** it is the algebraic modulus of the element, the multiplicative size function of the algebra; as the diagonal of a **Hermitian form** it supplies the Euclidean topology. In the first six columns the two roles coincide or nearly so: for $\mathbb{R}$, $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$ and $\mathbb{H}$ the Hermitian form is real-valued and the norm is its own diagonal, and only in $\mathbb{H}_{\mathrm{s}}$ does the Hermitian form differ from the norm by the choice of the signature $(2,2)$ of the vector part (*Split-Quaternion Norm and Invertibility*, §*The Split-Quaternion Norm*). The last two columns are where the two roles separate. In $\mathbb{B}$ the Hermitian form $\tilde Q\tilde Q^\dagger$ is not scalar-valued in general; its scalar part is the non-negative quantity $\sum_\mu\lvert Q_\mu\rvert^2$, of signature $(8,0)$, and the Euclidean norm is the square root of that scalar part, while the norm $\sum_\mu Q_\mu^2$ is a different, complex-valued object (*Biquaternion Norm and Invertibility*, §*Relation Between the Biquaternion Norm and the Hermitian Form*). In $\mathbb{H}_{\mathbb{D}}$ the Hermitian form $\tilde Q\tilde Q^\dagger$ has scalar part of signature $(4,4)$, indefinite, so it does not define a Euclidean norm either, and the Euclidean norm is defined separately and is not multiplicative (*Split-Biquaternion Norm and Invertibility*, §*The Hermitian Form*).

## Multiplicativity and the Composition Law

The norm of every one of the eight algebras is multiplicative:

$$
N(xy)=N(x)\,N(y),
$$

as in *Real Norm and Invertibility*, §*Multiplicativity*, and its counterparts. For the six algebras whose norm is scalar-valued this is a genuine composition law: the form of the product is the product of the forms, so the vanishing set is closed under multiplication and the units are closed under multiplication and inversion. For $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ the composition law is the classical one of the real, complex and quaternion norms and the square root $\sqrt{N}$ is a multiplicative Euclidean norm; for $\mathbb{D}$ and $\mathbb{H}_{\mathrm{s}}$ the square root is taken of an absolute value and the composition law survives in the form of the multiplicative modulus $\rho=\sqrt{\lvert N\rvert}$; for $\mathbb{D}'$ the composition law is the collapse $a^2c^2=(ac)^2$ of a form that remembers only the real part (*Split-Complex Norm and Invertibility*, §*Multiplicativity*; *Dual-Numbers Norm and Invertibility*, §*Multiplicativity*).

The two biquaternion columns need the law stated separately, because the value of the form lies in a ring. The biquaternion norm is complex-valued and multiplicative, and $\sqrt{\lvert N\rvert}$ is the **unique** multiplicative real norm on the group of units normalised to agree with the absolute value on the real scalars (*Biquaternion Norm and Invertibility*, §*The Unique Real Norm, and the Polar Scale*). The split biquaternion norm is split complex-valued and multiplicative, and in the idempotent basis the law is componentwise, $N(xy)_\pm=N(x)_\pm N(y)_\pm$, which is the multiplicativity of the ordinary quaternion norm on each half. The single sharpening the last column needs is that a product of two nonzero values of $\mathbb{D}$ can be zero, so multiplicativity does not by itself give the vanishing set as a multiplicative closed class; that role is played by the ideal $\mathrm{M}=(\varepsilon)$.

**Remark (the commutative analogue of the last column).** The four-dimensional commutative algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C} \cong \mathbb{C}\oplus\mathbb{C}$ of *List of Algebras by Dimension* has no column in the table, and its norm theory is the complex analogue of the last column: it is what the ring-valued case looks like when the division ring is a field. In the idempotent coordinates $q = \lambda_+e_+ + \lambda_-e_-$, with $\lambda_\pm = z_1 \pm z_2 \in \mathbb{C}$, the norm is their product,
$$N(q) = \lambda_+\lambda_- = z_1^2 - z_2^2,$$
the determinant of the matrix representation: $\mathbb{C}$-valued, multiplicative, and componentwise in the idempotent basis exactly as in the last column, $N(qq')_\pm = N(q)_\pm N(q')_\pm$. It vanishes on $e_+$ and on $e_-$, since $N(e_\pm) = \tfrac14 - \tfrac14 = 0$, so the vanishing set is the union of the two ideals and the algebra has zero divisors; the two elements of zero norm whose sum is $1$ are $e_+$ and $e_-$, and they are the reason the triangle inequality fails here, the one property its authors report as different from the complex case. The distinction is worth stating because it also settles which object is multiplicative: the real form $\lvert\lambda_+\rvert^2 - \lvert\lambda_-\rvert^2 = a^2+b^2-c^2-d^2$, of signature $(2,2)$, is **not** multiplicative, so the multiplicativity of this case is a property of the ring-valued norm and not of any real quadratic form refined from it.

## The Invertibility Criterion

The following table compares the criterion of invertibility and the inverse formula for the eight algebras. The eight algebras are the columns, in the fixed order.

| invertibility | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| criterion | $x\neq 0$ | $N\neq 0$ | $N\neq 0$ | $a$ a unit of $R$ | $N\neq 0$ | $N\neq 0$ | $N\neq 0$ | $N$ a unit of $\mathbb{D}$ |
| equivalent to | divisibility | divisibility | divisibility | $a\neq 0$ over a field | divisibility | divisibility | divisibility | both components nonzero |
| inverse | $1/x$ | $\bar Z/N$ | $\bar Z/N$ | $a^{-1}-a^{-2}\varepsilon b$ | $\bar{\tilde q}/N$ | $\bar{\tilde q}/N$ | $\bar{\tilde Q}/N$ | $\bar{\tilde Q}/N$ |

The criterion is the same statement in seven of the eight columns and a genuinely different one in the eighth. For $\mathbb{R}$, $\mathbb{C}$, $\mathbb{D}$, $\mathbb{H}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$ the element is invertible exactly when its norm is nonzero, and the inverse is the conjugate divided by the norm: $x^{-1}=x/N(x)$ (*Real Norm and Invertibility*, §*Invertibility*), $Z^{-1}=\bar Z/N(Z)$ (*Complex Norm and Invertibility*, §*Invertibility*; *Split-Complex Norm and Invertibility*, §*Invertibility*), $\tilde q^{-1}=\bar{\tilde q}/N(\tilde q)$ (*Quaternion Norm and Invertibility*, §*Invertibility*; *Split-Quaternion Norm and Invertibility*, §*The Invertibility Criterion*), $\tilde Q^{-1}=\bar{\tilde Q}/N(\tilde Q)$ (*Biquaternion Norm and Invertibility*, §*Invertibility*). The dual numbers have the same inverse formula but the criterion is stated on the real part, because the norm is degenerate: $Z=a+\varepsilon b$ is invertible exactly when $a$ is a unit of the base ring, over a field exactly when $a\neq 0$, and the inverse is $a^{-1}-a^{-2}\varepsilon b$ (*Dual-Numbers Norm and Invertibility*, §*Invertibility*).

The split biquaternion column is the exception, and it is the one place where the norm is not the criterion. The norm is split complex-valued and anisotropic, so $N(\tilde Q)\neq 0$ holds for every nonzero $\tilde Q$ and says nothing. What decides invertibility is whether $N(\tilde Q)$ is a **unit of $\mathbb{D}$**, equivalently whether both idempotent components $\tilde Q_\pm$ are nonzero, equivalently whether $N(\tilde Q)$ is not a nonzero zero divisor of $\mathbb{D}$ (*Split-Biquaternion Norm and Invertibility*, §*Invertibility*). This is a linear condition in the idempotent basis, in contrast with the quadratic conditions of the other seven columns.

## The Group of Units

The following table compares the group of units of the eight algebras: its description, its number of connected components, and its compactness. The eight algebras are the columns, in the fixed order.

| units | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| unit group | $\mathbb{R}\setminus\{0\}$ | $\mathbb{C}\setminus\{0\}$ | $\{N\neq 0\}$ | $\{a \text{ unit}\}$ | $\mathbb{H}\setminus\{0\}$ | $\{N\neq 0\}$ | $\{N\neq 0\}$ | $N$ a unit of $\mathbb{D}$ |
| structure | $\mathbb{R}_{>0}\times\{\pm1\}$ | $\mathbb{R}_{>0}\times U(1)$ | $\mathbb{R}^\times\times\mathbb{R}^\times$ | $\mathbb{R}^\times\times(\mathbb{R},+)$ | $\mathbb{R}_{>0}\times Sp(1)$ | $\cong GL_2(\mathbb{R})$ | $\cong GL(2,\mathbb{C})$ | $\cong\mathbb{H}^\times\times\mathbb{H}^\times$ |
| components | $2$ | $1$ | $4$ | $2$ | $1$ | $2$ | $1$ | $1$ |
| compact | no | no | no | no | no | no | no | no |
| compact factor | $\{\pm1\}$ | $U(1)$ | $\{\pm1\}^2$ | $\{\pm1\}$ | $Sp(1)=S^3$ | $\{\pm1\}$ | $U(2)$ | $S^3\times S^3$ |
| abelian | yes | yes | yes | yes | no | no | no | no |

The table is the unit-group side of the classification of the norm. The definite columns $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ have unit groups whose compact factor grows with the dimension — the sign group $\{\pm1\}$, the circle $U(1)$, the sphere $Sp(1)=S^3$ — and it is the definiteness of the norm that makes this factor compact (*Real Norm and Invertibility*, §*The Group of Units*; *Complex Norm and Invertibility*, §*The Group of Units*; *Quaternion Norm and Invertibility*, §*The Group of Units*). At $\mathbb{D}$ the compact factors remain discrete and the group acquires four components, one for each choice of signs of the two idempotent coordinates; the dual numbers have two components, the two half-lines $a>0$ and $a<0$, with the shear group $1+\mathrm{M}$ as second factor (*Split-Complex Norm and Invertibility*, §*The Four Components*; *Dual-Numbers Norm and Invertibility*, §*The Group of Units*). The split quaternions are $GL_2(\mathbb{R})$, of two components $P=\{N>0\}$ and $Q=\{N<0\}$ (*Split-Quaternion Norm and Invertibility*, §*The Group of Units*). The two biquaternion systems return to a connected unit group, but no longer compact: $\mathbb{B}^\times\cong GL(2,\mathbb{C})$, with maximal compact subgroup $U(2)$, and $\mathbb{H}_{\mathbb{D}}^\times\cong\mathbb{H}^\times\times\mathbb{H}^\times$, with maximal compact subgroup $S^3\times S^3$ (*Biquaternion Norm and Invertibility*, §*The Group of Units*; *Split-Biquaternion Norm and Invertibility*, §*The Group of Units*). No unit group of the table is compact, since each contains the positive scalars $\mathbb{R}_{>0}$; the row of compact factors records the largest compact subgroup inside each.

## The Topology of the Group of Units

The following table compares the topology of the eight algebras and of their groups of units: the ambient space, the homotopy type of the units, the components and the fundamental group, and the boundary of the polar form. The eight algebras are the columns, in the fixed order.

| topology | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| the algebra | $\mathbb{R}$ | $\mathbb{R}^2$ | $\mathbb{R}^2$ | $\mathbb{R}^2$ | $\mathbb{R}^4$ | $\mathbb{R}^4$ | $\mathbb{R}^8$ | $\mathbb{R}^8$ |
| units contractible | no | no | no | no | no | no | no | no |
| homotopy type of the units | $S^0$ | $S^1$ | four points | $S^0$ | $S^3$ | $S^1$ on each component | $S^1\times S^3$ | $S^3\times S^3$ |
| $\pi_0$ of the units | $\mathbb{Z}/2$ | $1$ | $(\mathbb{Z}/2)^2$ | $\mathbb{Z}/2$ | $1$ | $\mathbb{Z}/2$ | $1$ | $1$ |
| $\pi_1$ of the units | $0$ | $\mathbb{Z}$ | $0$ | $0$ | $0$ | $\mathbb{Z}$ | $\mathbb{Z}$ | $0$ |
| boundary of the polar form | — | $\{0\}$ | two null lines | maximal ideal $\mathrm{M}$ | $\{0\}$ | null cone, link $T^2$ | null cone, dimension $6$ | zero-divisor set $Z_\pm$ |

The table is the topology of the ladder. The algebra is contractible in every column, since each is a Euclidean space with a continuous product; it is the groups of units that carry the topology, and their homotopy type is the unit sphere of the normed case: $S^0$ for $\mathbb{R}$, $S^1$ for $\mathbb{C}$, $S^3$ for $\mathbb{H}$, and the products $S^1\times S^3$ for $\mathbb{B}$ and $S^3\times S^3$ for $\mathbb{H}_{\mathbb{D}}$ (*Real Topology*; *Complex Topology*; *Quaternion Topology*; *Biquaternion Topology*; *Split-Biquaternion Topology*). The two split cases $\mathbb{D}$ and $\mathbb{H}_{\mathrm{s}}$ distort this: the four components of $\mathbb{D}^{\times}$ are contractible so that $\pi_1=0$ and only $\pi_0=(\mathbb{Z}/2)^2$ remains, and the two components of $GL_2(\mathbb{R})$ each deform to a circle so that $\pi_1\cong\mathbb{Z}$ while the norm-one group $SL_2(\mathbb{R})$ is homotopy equivalent to $S^1$ (*Split-Complex Topology*; *Split-Quaternion Topology*). The $\pi_1$ row separates the columns that wind from those that do not: it is $\mathbb{Z}$ exactly for $\mathbb{C}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$. The last row is the boundary of the polar domain, which coincides with the zero-divisor set whenever it is non-empty: the origin in the definite two- and four-dimensional cases, the two null lines in $\mathbb{D}$, the maximal ideal in $\mathbb{D}'$, the null cone in $\mathbb{H}_{\mathrm{s}}$, whose link is the torus $T^2$, the null cone of $\mathbb{B}$, of dimension six and singular at the apex, and the zero-divisor set $Z_+\cup Z_-$ of $\mathbb{H}_{\mathbb{D}}$, two four-dimensional pieces each homotopy equivalent to $S^3$ (*Real Polar Element Representation*; *Split-Complex Topology*; *Dual-Numbers Topology*; *Split-Quaternion Topology*; *Biquaternion Topology*; *Split-Biquaternion Topology*). The $\mathbb{R}$ cell of that row carries the marker because the real line has no boundary beyond the origin, which is the only excluded element.

## The Classification by the Sign of the Norm

The following table compares the classification of the elements of the eight algebras by the sign of the norm. The eight algebras are the columns, in the fixed order.

| classes | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| positive / invertible | $x>0$ | $Z\neq 0$ | spacelike $N>0$ | $a\neq 0$ | $\tilde q\neq 0$ | $N>0$ | $N\neq 0$ | both components nonzero |
| null / zero divisor | — | — | null $N=0$ | $\mathrm{M}\setminus\{0\}$ | — | lightlike $N=0$ | $N=0$ | exactly one component zero |
| negative | $x<0$ | — | timelike $N<0$ | — | — | $N<0$ | — | — |
| zero | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |

The table records the number of classes the sign of the norm produces: three for $\mathbb{R}$ (positive, zero, negative), but no nonzero null class, because the form is definite; two for the division algebras $\mathbb{C}$ and $\mathbb{H}$ (invertible, zero); three for $\mathbb{D}$ and $\mathbb{H}_{\mathrm{s}}$ (spacelike, null, timelike), the null class being the zero-divisor set; three for $\mathbb{D}'$ (invertible, zero divisor, zero); and three for the biquaternion systems (invertible, zero divisor, zero). The empty cells of $\mathbb{R}$, $\mathbb{C}$, $\mathbb{D}'$ and $\mathbb{H}$ in the third and fourth rows are genuine: $\mathbb{C}$ and $\mathbb{H}$ have no element of vanishing norm other than the origin, so their null class is empty and their classification is a dichotomy; $\mathbb{D}'$ has no negative value because its form is semidefinite; and $\mathbb{R}$ has no null class because the only real number of vanishing square is zero. For $\mathbb{D}$ and $\mathbb{H}_{\mathrm{s}}$ the classification is multiplicative — the product of two spacelike elements is spacelike, and so on — so it is a grading of the algebra compatible with its multiplication (*Split-Complex Norm and Invertibility*, §*Distribution of the Invertible Elements*; *Split-Quaternion Norm and Invertibility*, §*Distribution of the Invertible Elements*). For $\mathbb{H}_{\mathbb{D}}$ the midpoint of the table is the one case not read off from the sign of a scalar: the zero divisors are the elements with exactly one idempotent component zero, and the sign of the norm gives no such information, its value being a nonzero zero divisor of $\mathbb{D}$.

## The Two Polar Series

Each algebra of the table has a polar decomposition $x=\rho u$ of every element with non-vanishing norm into a modulus $\rho$ and a unit factor $u$, and the decompositions fall into two series according to the character of the norm and of the unit factor: the **definite polar series** $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{B}$, whose Hermitian scalar part is positive definite and whose unit factor carries a compact factor, and the **indefinite polar series** $\mathbb{D}, \mathbb{D}', \mathbb{H}_{\mathrm{s}}, \mathbb{H}_{\mathbb{D}}$, whose norm is indefinite, degenerate or split-valued and whose unit factor carries a non-compact hyperbolic or parabolic factor. The following table compares the two series and the place of each algebra in them: the modulus, the character of the unit factor, the boundary of the decomposition and the series. The eight algebras are the columns, in the fixed order. The factors into which the unit factor splits are the subject of *Comparison of the Polar Element Representation* and are not repeated here.

| polar data | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| modulus | $\lvert x\rvert$ | $\sqrt{N}$ | $\sqrt{\lvert N\rvert}$ | $\lvert a\rvert$ | $\sqrt{N}$ | $\sqrt{\lvert N\rvert}$ | $\sqrt{\lvert N\rvert}$ | $\rho_\pm=\lvert A\pm A'\rvert$ |
| unit factor | discrete, $\{\pm1\}$ | compact, $U(1)$ | hyperbolic, $e^{\phi j}$ | parabolic, $1+\mathrm{M}$ | compact, $Sp(1)$ | compact and hyperbolic | compact and hyperbolic | hyperbolic central, compact rotor |
| boundary | $\{0\}$ | $\{0\}$ | null cone | $\mathrm{M}$ | $\{0\}$ | null cone | null cone | none |
| series | definite | definite | indefinite | indefinite | definite | indefinite | definite | indefinite |

The table separates the two series by the character of the unit factor and by the boundary of the decomposition. In the definite series the norm is definite and the boundary is the origin alone, and the unit factor is compact in $\mathbb{C}$ and $\mathbb{H}$ — $U(1)$ and $Sp(1)=S^3$ — and discrete in $\mathbb{R}$, where it is the two-point set $\{\pm1\}$; $\mathbb{B}$ is the one column of the series that is not wholly compact, because its complex-valued form has a null cone and its unit factor acquires the hyperbolic rotation of the Hermitian subspace $\mathbb{M}_+$ (*Biquaternion Norm and Invertibility*, §*The Unique Real Norm, and the Polar Scale*; *Biquaternion Polar Element Representation*, §*The Four Factors and Their Meanings*). In the indefinite series the boundary is non-empty in every column but the last: the null cone in $\mathbb{D}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$, and the maximal ideal $\mathrm{M}$ in $\mathbb{D}'$, whose unit factor is the parabolic shear $1+\mathrm{M}$ rather than a hyperbola (*Dual-Numbers Polar Element Representation*, §*The Factors and Their Meanings*; *Split-Quaternion Polar Element Representation*, §*The Polar Decomposition*).

$\mathbb{H}_{\mathbb{D}}$ is the only column whose decomposition exists on the whole algebra. Its modulus is the pair $\rho_\pm=\lvert A\pm A'\rvert$ of the two idempotent components, a branch-free modulus of split complex type, and its unit factor combines the hyperbolic central phase $e^{j\tau}$ with the compact rotor $S^3\times S^3$, so that the column is the split counterpart of $\mathbb{B}$: the hyperbolic part is central rather than confined to a Hermitian subspace, and no boundary of the decomposition remains (*Split-Biquaternion Polar Element Representation*, §*The Theorem*; §*Comparison with the Other Algebras of the Series*). The two series thus differ in the form of the unit factor — compact rotor and elliptic phase in the first, hyperbolic phase and parabolic shear in the second — while the modulus in every column is read from the norm alone.

## Summary

The norm of each of the eight algebras is multiplicative, and the eight divide by its signature. $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ have definite norms of signatures $(1,0)$, $(2,0)$ and $(4,0)$, and are division algebras; $\mathbb{D}$ and $\mathbb{H}_{\mathrm{s}}$ have indefinite forms of signatures $(1,1)$ and $(2,2)$ and have null cones of zero divisors; $\mathbb{D}'$ has a degenerate form $a^2$ of rank one with the maximal ideal as its vanishing set; $\mathbb{B}$ has a complex-valued form vanishing on a zero-divisor cone and $\mathbb{H}_{\mathbb{D}}$ a split complex-valued form that is anisotropic and does not detect the zero divisors at all. The Hermitian form separates from the norm exactly in the two biquaternion columns, where its scalar part has signature $(8,0)$ and $(4,4)$ respectively. The invertibility criterion is $N\neq 0$ in seven columns, with the inverse the conjugate over the norm, and in $\mathbb{H}_{\mathbb{D}}$ it becomes the requirement that $N$ be a unit of $\mathbb{D}$, equivalently that both idempotent components be nonzero. The group of units is connected exactly for $\mathbb{C}$, $\mathbb{H}$, $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$, and never compact; its maximal compact subgroup grows from $\{\pm1\}$ through $U(1)$ and $Sp(1)$ to $U(2)$ and $S^3\times S^3$, and the homotopy type of the units is the unit sphere of the normed case — $S^0$, $S^1$, $S^3$ — extended to the products $S^1\times S^3$ for $\mathbb{B}$ and $S^3\times S^3$ for $\mathbb{H}_{\mathbb{D}}$, with $\pi_1\cong\mathbb{Z}$ exactly for $\mathbb{C}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$. The classification by the sign of the norm has three classes for $\mathbb{R}$, $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{H}_{\mathrm{s}}$, $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$, with different meanings, and two for $\mathbb{C}$ and $\mathbb{H}$. Finally, the polar decompositions fall into a definite series $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{B}$ and an indefinite series $\mathbb{D}, \mathbb{D}', \mathbb{H}_{\mathrm{s}}, \mathbb{H}_{\mathbb{D}}$, differing in the character of the unit factor — compact rotor and elliptic phase in the first, hyperbolic rotation and parabolic shear in the second — with the boundary of the decomposition coinciding with the zero-divisor set in every case where it is non-empty.

## Summary of Notation

| symbol | meaning |
|---|---|
| $N$ | the norm of the algebra under discussion |
| $N(x)=x^2$ | the norm of $\mathbb{R}$ |
| $N(Z)=a^2+b^2$ | the norm of $\mathbb{C}$ |
| $N(Z)=a^2-b^2$ | the norm of $\mathbb{D}$, signature $(1,1)$ |
| $N(Z)=a^2$ | the norm of $\mathbb{D}'$, degenerate |
| $N(\tilde q)=\sum_k q_k^2$ | the norm of $\mathbb{H}$ |
| $N(\tilde q)=q_0^2+q_1^2-q_2^2-q_3^2$ | the norm of $\mathbb{H}_{\mathrm{s}}$, signature $(2,2)$ |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | the biquaternion and split biquaternion norm |
| $Q_\mu$ | the four complex coordinates of a biquaternion |
| $\tilde Q=A+jA'$, $A,A'\in\mathbb{H}$ | a split biquaternion, in the split complex form |
| $\tilde Q_\pm$ | the two quaternion components of $\tilde Q$ in $\mathbb{H}_{\mathbb{D}}$ |
| $\mathrm{M}=(\varepsilon)$ | the maximal ideal of $\mathbb{D}'$ |
| $\tilde q^{-1}=\bar{\tilde q}/N(\tilde q)$ | the quaternion inverse |
| $\tilde Q\tilde Q^\dagger$ | the Hermitian form of $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$ |
| $U(1), Sp(1)=S^3$ | the compact unit groups of $\mathbb{C}$ and $\mathbb{H}$ |
| $\mathbb{R}_{>0}$ | the positive scalars, the identity component of $\mathbb{R}^\times$ |
| $x=\rho u$ | the polar decomposition of an element: modulus and unit factor |
| $e^{\phi j},e^{j\tau}$ | the hyperbolic unit factors of $\mathbb{D}$ and $\mathbb{H}_{\mathbb{D}}$ |
| $1+\mathrm{M}$ | the parabolic unit factor of $\mathbb{D}'$ |
| $GL_2(\mathbb{R}), GL(2,\mathbb{C})$ | unit groups of $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$ |
| $\pi_0,\pi_1$ | the components and the fundamental group of the group of units |
| $S^0,S^1,S^3$ | the homotopy types of the units of $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ |
| $T^2=S^1\times S^1$ | the link of the split-quaternion null cone |
| $Z_\pm$ | the two zero-divisor pieces of $\mathbb{H}_{\mathbb{D}}$ |
| `—` | an empty cell, stated and never filled |

## Further Reading

- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for signatures, isotropy and the Witt classification of quadratic forms.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the norm, the group of units and the splitting of a quaternion algebra.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the norm of a finite-dimensional algebra and the determinant of the multiplication map.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed. (Cambridge University Press, 2013), for the polar decomposition of a matrix and the role of the singular values.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the norms of the low-dimensional algebras and their indefinite refinements.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the homotopy groups of the classical groups and the topology of their homogeneous spaces.

- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022, for the reduced biquaternion algebra — the commutative four-dimensional algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, equivalently the double-complex, tessarine or commutative hypercomplex algebra — and for its norm formula, its zero divisors and its invertibility criterion.
