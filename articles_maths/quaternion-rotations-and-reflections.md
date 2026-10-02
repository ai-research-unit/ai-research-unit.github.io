
# __Quaternion Rotations and Reflections__

## Introduction

This article describes the orthogonal group of three-dimensional Euclidean space as it is realised by the units of the quaternion algebra $\mathbb{H}$. The starting point is the group $Sp(1)$ of unit quaternions and the identification of its adjoint action on the imaginary quaternions with the rotation group $SO(3)$; the endpoint is the full orthogonal group $O(3)$ and, more generally, the two-sided action of $Sp(1)\times Sp(1)$ on $\mathbb{H}$ that exhausts $SO(4)$. Along the way the article explains why the covering $Sp(1)\to SO(3)$ is two-to-one, why the quaternion parametrisation of a rotation has period $4\pi$ where the rotation itself has period $2\pi$, and how reflections sit inside the same algebra as the signed inner conjugation action of the unit vectors. The sandwich $S_q(x) = qx\tilde{q}^{\natural}$ is treated beside the adjoint action: it agrees with it on the unit sphere and carries a scale everywhere else.

The treatment is mathematical throughout. A rotation is an element of $SO(3)$ and a reflection is an element of $O(3)$; no physical object is introduced, no state of a physical system is named, and no physical interpretation is invoked. The group $Sp(1)$ is treated as a group of quaternions, and the maps $Sp(1)\to SO(3)$ and $Sp(1)\times Sp(1)\to SO(4)$ are treated as covering homomorphisms of Lie groups.

The quaternion algebra, its basis $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, its conjugation, its quaternion norm $N(\tilde q) = \tilde q\tilde{q}^{\natural}$ and its imaginary subspace $\operatorname{Im}\mathbb{H}\cong\mathbb{R}^3$ are taken from *Quaternion Algebra*. The structure of $\mathbb{H}$ as a simple algebra is taken from *Quaternion Ideals and Simplicity*. The general construction of the Clifford, Pin and Spin groups, of which the results below are the three-dimensional instance, is the subject of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the parity of the Cartan–Dieudonné reflection length is taken from *The Rotation Group and Orientation* and from *Isometries and Orthogonal Transformations*. The complex plane, where the same questions have the degenerate answer that multiplication by a unit is already a rotation and the sandwich action is trivial, is treated in *Rotations and Reflections in the Complex Plane*.

Throughout, a general quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with scalar part $q_0$ and vector part $\mathbf{q} = q_1e_1+q_2e_2+q_3e_3 \in \operatorname{Im}\mathbb{H}$, the conjugate is $\tilde{q}^{\natural} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$, the quaternion norm is $N(\tilde q) = \tilde q\tilde{q}^{\natural} = |\tilde q|^2$, and the real inner product of two vectors of $\operatorname{Im}\mathbb{H}$ is $\langle x, y\rangle = \mathrm{Sc}(x y^{\natural}) = \sum_{k=1}^{3} x_ky_k$. A point of $\operatorname{Im}\mathbb{H}$ is a **vector**, and $|x|^2 = \langle x,x\rangle$. The transpose of a matrix $A$ is $A^{T}$ and the conjugate transpose is $A^{\dagger}$.

## The Group of Unit Quaternions

### Definition and Group Structure

**Definition.** The **unit quaternions**, or the **quaternion unit group**, are

$$
Sp(1) = \{\tilde q \in \mathbb{H} : N(\tilde q) = 1\} = \{\tilde q \in \mathbb{H} : |\tilde q| = 1\}.
$$

As a subset of $\mathbb{H}\cong\mathbb{R}^4$ it is the unit sphere $S^3$.

**Theorem.** $Sp(1)$ is a group under quaternion multiplication and is the kernel of the quaternion norm homomorphism $\mathbb{H}^{\times}\to\mathbb{R}_{>0}$, $\tilde q\mapsto|\tilde q|$.

**Proof.** The quaternion norm is multiplicative, $N(uv) = N(u)N(v)$, because $uv(uv)^{\natural} = uvv^{\natural}u^{\natural} = uN(v)u^{\natural} = N(u)N(v)$; hence if $|u| = |v| = 1$ then $|uv| = 1$, and if $|u| = 1$ then $u^{-1} = u^{\natural}$ has $|u^{-1}| = 1$. Associativity and the identity $1\in Sp(1)$ are inherited from $\mathbb{H}$, and multiplication is a surjective homomorphism $\mathbb{H}^{\times}\to\mathbb{R}_{>0}$ with kernel exactly $Sp(1)$.

For every unit quaternion $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ one has $\tilde q^{-1} = \tilde{q}^{\natural} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$, so inversion is quaternion conjugation. The group is non-abelian; its centre is the two-element group

$$
Z(Sp(1)) = \{\pm 1\},
$$

because a quaternion commuting with every element of $\mathbb{H}$ is real.

### Polar Form and the Exponential

**Theorem (polar form).** Every unit quaternion has an expression

$$
\tilde q = \cos\theta + u\sin\theta, \qquad 0 \leq \theta \leq \pi, \ u \in \operatorname{Im}\mathbb{H},\ |u| = 1,
$$

in which the angle $\theta$ is unique; the axis $u$ is unique when $0 < \theta < \pi$, while for $\theta = 0$ and $\theta = \pi$ the quaternion is $\tilde q = 1$ and $\tilde q = -1$ respectively and $u$ is arbitrary.

**Proof.** A unit quaternion has $q_0^2 + |\mathbf{q}|^2 = 1$, so there is a unique $\theta\in[0,\pi]$ with $q_0 = \cos\theta$ and $|\mathbf{q}| = \sin\theta$. If $\sin\theta\neq0$ then $u = \mathbf{q}/\sin\theta$ is a unit vector, uniquely determined by $\tilde q$, and $\tilde q = \cos\theta+u\sin\theta$; if $\sin\theta = 0$ then $\mathbf{q} = 0$ and $\tilde q = \pm1$.

**Theorem (exponential).** For a unit vector $u\in\operatorname{Im}\mathbb{H}$ and real $\theta$,

$$
\exp(u\theta) = \sum_{n\ge0}\frac{(u\theta)^n}{n!} = \cos\theta + u\sin\theta,
$$

the series converging absolutely. Consequently $Sp(1)$ is the image of the exponential map of the Lie algebra $\operatorname{Im}\mathbb{H}$, and every unit quaternion is $\exp(u\theta)$ for some unit vector $u$ and real $\theta$.

**Proof.** Since $u^2 = -1$, the even part of the series is $\sum_k(-1)^k\theta^{2k}/(2k)! = \cos\theta$ and the odd part is $u\sum_k(-1)^k\theta^{2k+1}/(2k+1)! = u\sin\theta$. The polar form exhibits each unit quaternion in this shape.

The exponential satisfies $\exp(u(\theta+2\pi)) = -\exp(u\theta)$ because $\exp(2\pi u) = -1$, and $\exp(u(\theta+4\pi)) = \exp(u\theta)$; this doubling is the algebraic root of the periodicity discussed below.

### The Versor, and the Arc Picture

Hamilton's word for a unit quaternion is a **versor**, from the Latin *versari*, to turn. He wrote $U\tilde q = \tilde q/|\tilde q|$ for the versor of a general quaternion and $T\tilde q = |\tilde q|$ for its norm, which he called the tensor, so that the polar decomposition of *Quaternion Norm and Invertibility* reads $\tilde q = T\tilde q\,U\tilde q$. In this vocabulary $Sp(1)$ is the group of versors.

**Proposition.** A versor is the quotient of two unit vectors: for unit vectors $a, b$ the element $\tilde q = b\bar a = ba^{-1}$ is a unit quaternion, and every versor arises in this way.

**Proof.** The norm is multiplicative and $|\bar a| = 1$, so $|\tilde q| = 1$. Conversely let $\tilde q = \cos\theta + u\sin\theta$ with $u$ a unit vector; choose a unit vector $a\perp u$ and set $b = a\cos\theta + (u\times a)\sin\theta$. Then $b$ is a unit vector, $\langle a, b\rangle = \cos\theta$ and $a\times b = u\sin\theta$, and since $b\bar a = \langle a, b\rangle + a\times b$ for unit vectors $a, b$, the quotient is $\tilde q$.

**Remark (the arc picture).** For a fixed plane $\Pi$ through the origin the quotient of two unit vectors of $\Pi$ depends only on the directed angle between them, so a versor with axis $u$ is the quotient of any two unit vectors of the plane with normal $u$ separated by the directed angle $\theta$. Hamilton pictured the versor as the directed arc of the great circle $\Pi\cap S^2$ joining the first vector to the second, arcs of equal direction and length defining the same versor, and he called the multiplication of versors the **sum of arcs**. The arc is the versor and not the path of the rotated point: the rotation the versor represents has twice the subtended angle, by the half-angle formula of §*The Half-Angle Formula*.

**Definition.** A **right versor** is a versor of angle $\pi/2$, that is a unit vector of $\operatorname{Im}\mathbb{H}$; the right versors are exactly the unit square roots of $-1$, and they form the sphere $S^2\subset\operatorname{Im}\mathbb{H}$ of *Quaternion Roots of Minus One*.

**Remark (two senses of the word).** This is Hamilton's sense of *versor*. In the Clifford vocabulary of Part II (*Versors, Rotors and the Sandwich Action with Signed Inner Conjugation*) a versor is any product of non-isotropic vectors, of either parity; in the three-dimensional Euclidean case $\mathrm{Cl}_{3,0}$ Hamilton's versors are exactly the even versors of Clifford norm one, which that vocabulary calls rotors, while the odd versors are the unit vectors acting as reflections. The corpus keeps *versor* for the Clifford sense and *rotor* for the even norm-one one, so the word is used here in the historical sense only.

### The Group $\mathrm{SU}(2)$

**Theorem.** The group $Sp(1)$ of unit quaternions is the special unitary group $\mathrm{SU}(2)$, the group of $2\times2$ complex unitary matrices of determinant one.

This is the standard identification of the unit sphere of the quaternion division algebra with the special unitary group, quoted here as standard; its infinitesimal form is the Lie algebra identification $\operatorname{Im}\mathbb{H}\cong\mathrm{SU}(2)$.

**Theorem.** $Sp(1)\cong S^3$ is compact, connected, and simply connected, and it is a three-dimensional real Lie group with Lie algebra $\operatorname{Im}\mathbb{H}$.

**Proof.** As $S^3$ it is a closed bounded subset of $\mathbb{R}^4$, hence compact, and connected. The sphere $S^n$ is simply connected for $n\geq2$, by the standard argument that a loop in $S^n$ can be pushed off a point and contracted in the complementary ball; hence $S^3$ is simply connected. The smooth structure and the group law make it a Lie group of dimension $3$, and its Lie algebra is the tangent space at the identity, which is $\operatorname{Im}\mathbb{H}$ with the commutator bracket.

## The Adjoint Action on the Imaginary Quaternions

### The Adjoint Action

**Definition.** For $\tilde q\in Sp(1)$ the **adjoint action** is

$$
\operatorname{Ad}_q : \mathbb{H}\longrightarrow\mathbb{H}, \qquad \operatorname{Ad}_q(x) = qxq^{-1} = qx\tilde{q}^{\natural}.
$$

**Theorem.** For every $\tilde q\in Sp(1)$ the map $\operatorname{Ad}_q$ is an $\mathbb{R}$-algebra automorphism of $\mathbb{H}$ that preserves the quaternion norm and the scalar part. It restricts to a linear isometry of $\operatorname{Im}\mathbb{H}$, and the assignment $\tilde q\mapsto\operatorname{Ad}_q$ is a group homomorphism $Sp(1)\to GL(\operatorname{Im}\mathbb{H})$.

**Proof.** Conjugation by an invertible element is an algebra automorphism: the map $x\mapsto qxq^{-1}$ is $\mathbb{R}$-linear and a bijection with inverse $x\mapsto \tilde q^{-1}xq$, and it respects multiplication because $(qaq^{-1})(qbq^{-1}) = \tilde q(ab)\tilde q^{-1}$; for $|\tilde q| = 1$ the inverse is $x\mapsto\tilde{q}^{\natural}xq$. Norm preservation: $N(qxq^{-1}) = N(\tilde q)N(x)N(\tilde q)^{-1} = N(x)$. Scalar part: if $x\in\operatorname{Im}\mathbb{H}$ then conjugation reverses the order of the factors, so $\overline{\operatorname{Ad}_q(x)} = (\tilde q^{-1})^{\natural}\,x^{\natural}\,\tilde{q}^{\natural} = \tilde q\,(-x)\,\tilde{q}^{\natural} = -qx\tilde{q}^{\natural} = -\operatorname{Ad}_q(x)$, and the scalar part of $\operatorname{Ad}_q(x)$ vanishes. Hence $\operatorname{Ad}_q$ preserves $\operatorname{Im}\mathbb{H}$, and since it preserves the quaternion norm there it is an isometry. Finally $\operatorname{Ad}_{q_1}\circ\operatorname{Ad}_{q_2} = \operatorname{Ad}_{q_1q_2}$ and $\operatorname{Ad}_1 = \mathrm{id}$ by associativity.

### The Homomorphism to SO(3)

**Definition.** The **orthogonal group** of $\mathbb{R}^3$ is $O(3) = \{A\in GL_3(\mathbb{R}) : A^{T}A = I\}$, and the **rotation group** is the subgroup $SO(3)$ of matrices of determinant $+1$.

**Theorem.** For every $\tilde q\in Sp(1)$ the isometry $\operatorname{Ad}_q$ of $\operatorname{Im}\mathbb{H}$ has determinant $+1$. Hence the homomorphism $\tilde q\mapsto\operatorname{Ad}_q$ takes values in $SO(3)$.

**Proof.** An isometry of a three-dimensional real inner product space has determinant $\pm1$. The determinant function $\det\circ\operatorname{Ad} : Sp(1)\to\{\pm1\}$ is continuous, and $Sp(1)$ is connected, so its image is connected in the discrete two-point set; hence it is constant, and its value at $\tilde q = 1$ is $\det(\mathrm{id}) = 1$.

In the basis $(e_1, e_2, e_3)$ of $\operatorname{Im}\mathbb{H}$ the matrix of $\operatorname{Ad}_q$, with $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$, is

$$
R_q = \begin{pmatrix}
1 - 2(q_2^2 + q_3^2) & 2(q_1q_2 - q_0q_3) & 2(q_1q_3 + q_0q_2) \\
2(q_1q_2 + q_0q_3) & 1 - 2(q_1^2 + q_3^2) & 2(q_2q_3 - q_0q_1) \\
2(q_1q_3 - q_0q_2) & 2(q_2q_3 + q_0q_1) & 1 - 2(q_1^2 + q_2^2)
\end{pmatrix},
$$

whose trace is $\operatorname{tr}R_q = 4q_0^2 - 1$. The formula is the coordinate expression of $\operatorname{Ad}_q$ and is the standard quaternion parametrisation of the rotation group.

**Remark (reading the quaternion off the matrix, and the largest entry).** The parametrisation is two-to-one, $R_q = R_{-q}$, so the matrix determines the pair $\{\pm\tilde q\}$ and no more. The four quantities

$$
1+\operatorname{tr}R_q = 4q_0^2,
\qquad
1+R_{11}-R_{22}-R_{33} = 4q_1^2,
\qquad
1+R_{22}-R_{33}-R_{11} = 4q_2^2,
\qquad
1+R_{33}-R_{11}-R_{22} = 4q_3^2
$$

are the squares of the four coefficients, and they sum to $4$ because $|\tilde q| = 1$; hence the largest of them is at least $1$, and it is the one to take the square root of. The remaining three coefficients then follow from the off-diagonal entries: the antisymmetric combinations carry the products with the scalar part,

$$
4q_0q_1 = R_{21}-R_{12},
\qquad
4q_0q_2 = R_{02}-R_{20},
\qquad
4q_0q_3 = R_{10}-R_{01},
$$

and the symmetric combinations the products of the imaginary coefficients,

$$
4q_1q_2 = R_{01}+R_{10},
\qquad
4q_1q_3 = R_{02}+R_{20},
\qquad
4q_2q_3 = R_{12}+R_{21}.
$$

Choosing the largest of the four is not a convenience but the point: recovering $q_0$ from the trace and dividing by it is exact for a generic rotation and fails precisely when $q_0 = 0$, that is at a rotation through $\pi$, where the trace is $-1$ and the quotient is $0/0$. Since the largest of the four quantities is at least $1$ for every rotation, the branch that uses it never divides by a small number. The trace also reads off the angle, $\operatorname{tr}R_q = 1+2\cos\theta$, which is the same statement as $q_0 = \cos(\theta/2)$: at $\theta = \pi$ the scalar part vanishes and the matrix alone cannot distinguish the two senses of the axis, which is the degeneracy just described. Finally, replacing the parametrising quaternion by its inverse — that is, reversing the orientation of the rotation — transposes the matrix, $R_{\tilde q^{-1}} = R_q^{T}$, since the adjoint action of $\tilde q^{-1}$ inverts the automorphism $\operatorname{Ad}_q$ on $\operatorname{Im}\mathbb{H}$.

### The Closest Rotation and the Largest Eigenvalue

The parametrisation above recovers $\{\pm\tilde q\}$ from a rotation matrix, and it uses the largest of the four diagonal quantities to avoid the division by a small number. The inverse problem is not always posed with a rotation: measured data give a matrix that is a rotation only up to error, and the question is which rotation is closest to it. The same four numbers, read as a vector, and one symmetric matrix answer that question, and the passage between the two problems is the reason the quaternion is preferred to the three angles in the applied literature.

**Definition (the fitting matrix).** For a real $3\times3$ matrix $Q$ with entries $Q_{ij}$, the **fitting matrix** is the symmetric $4\times4$ matrix

$$
K(Q) = \begin{pmatrix}
\operatorname{tr}Q & Q_{32}-Q_{23} & Q_{13}-Q_{31} & Q_{21}-Q_{12} \\
Q_{32}-Q_{23} & 2Q_{11}-\operatorname{tr}Q & Q_{12}+Q_{21} & Q_{13}+Q_{31} \\
Q_{13}-Q_{31} & Q_{12}+Q_{21} & 2Q_{22}-\operatorname{tr}Q & Q_{23}+Q_{32} \\
Q_{21}-Q_{12} & Q_{13}+Q_{31} & Q_{23}+Q_{32} & 2Q_{33}-\operatorname{tr}Q
\end{pmatrix},
$$

whose rows and columns are indexed by $(e_0, e_1, e_2, e_3)$.

**Theorem (the fitting matrix is the correlation matrix of the rotation).** For every unit quaternion $\tilde q$ with coefficient vector $q = (q_0, q_1, q_2, q_3)$ and every real $3\times3$ matrix $Q$,

$$
q^{T}K(Q)\,q = \operatorname{tr}\bigl(R_q^{T}Q\bigr) = \sum_{i,j=1}^{3}(R_q)_{ij}Q_{ij},
$$

the sum being the **correlation** of the rotation $R_q$ with $Q$.

*Proof.* Both sides are quadratic forms in $q$, and $K(Q)$ is linear in $Q$, so it suffices to expand and collect the coefficient of each $Q_{ij}$. The diagonal entries of $K(Q)$ give $q_0^2+q_i^2-q_j^2-q_k^2$ for the coefficient of $Q_{ii}$ with $\{i,j,k\} = \{1,2,3\}$, which is $1-2(q_j^2+q_k^2) = (R_q)_{ii}$ because $|\tilde q| = 1$; the off-diagonal entries give $2q_0q_k+2q_iq_j$ for the coefficient of $Q_{ij}$ with the cyclic order $(i,j,k)$, which is $(R_q)_{ij}$ by the displayed matrix. Hence the two quadratic forms agree on every matrix unit $Q = E_{ij}$ and therefore everywhere. $\square$

**Theorem (the closest rotation).** Let $Q$ be a real $3\times3$ matrix and let $q_\ast$ be a unit eigenvector of $K(Q)$ for its **largest** eigenvalue $\lambda_\ast$. Then

$$
\lambda_\ast = \max_{|\tilde q| = 1}\operatorname{tr}\bigl(R_q^{T}Q\bigr) = \operatorname{tr}\bigl(R_{q_\ast}^{T}Q\bigr),
$$

so $R_{q_\ast}$ is the rotation that **best fits** $Q$: among all matrices of $SO(3)$ it minimises the sum of squares $\sum_{i,j}(R_{ij}-Q_{ij})^2$, because $\sum_{ij}(R_{ij}-Q_{ij})^2 = 3+\sum_{ij}Q_{ij}^2-2\operatorname{tr}(R^{T}Q)$ and only the last term depends on $R$.

*Proof.* By the identity of the previous theorem, $\operatorname{tr}(R_q^{T}Q) = q^{T}K(Q)q$ for unit $\tilde q$. The spectral theorem for a real symmetric matrix exhibits $K(Q) = \sum_k\lambda_kv_kv_k^{T}$ with orthonormal $v_k$, so $q^{T}K(Q)q = \sum_k\lambda_k\langle v_k, q\rangle^2$, a convex combination of the eigenvalues; its maximum over the unit sphere is $\lambda_\ast$, attained exactly at the eigenvectors for $\lambda_\ast$. The expansion of the sum of squares is immediate. $\square$

**Corollary (the exact case, and the eigenvalue as a test of fit).** If $Q$ is itself a rotation, $Q = R_{q_0}$, then $\lambda_\ast = 3$, the eigenvectors for $\lambda_\ast$ are $\pm q_0$, and the best fit is exact. Equivalently, the largest eigenvalue of $\frac{1}{3}K(Q)$ is $1$ for a rotation matrix, and its eigenvector is the quaternion of the rotation; the value $\lambda_\ast$ is the achieved correlation, and the gap $3-\lambda_\ast$ measures how far $Q$ is from a rotation.

*Proof.* For $Q = R_{q_0}$ one has $\operatorname{tr}(R_q^{T}Q) = \operatorname{tr}(R_q^{T}R_{q_0}) = \operatorname{tr}(R_{q^{\natural} q_0})$, and the trace is $4(q_0')^2-1\le3$ with the scalar part $q_0' = \langle \tilde q,\tilde q_0\rangle$ of the product, so the maximum is $3$, attained exactly at $\tilde q = \pm\tilde q_0$. The factor $\frac{1}{3}$ is the normalisation of the definition. $\square$

**Remark (why the eigenvector, and not the four square roots).** The four quantities of the preceding remark are the diagonal entries of the eigenvector problem in disguise: $1+\operatorname{tr}R_q = 4q_0^2$ and the three others are $\frac{1}{3}K(Q)$'s diagonal deviations, and when $Q$ is a rotation the eigenvector for $\lambda_\ast = 3$ has components proportional to $(\sqrt{1+\operatorname{tr}Q}, \pm\sqrt{1+R_{11}-R_{22}-R_{33}}, \dots)$. The largest-eigenvalue route is the numerically stable version of the largest-square-root route: it never divides by a component that may vanish, and it extends off the rotation matrices, where the four-branch formulas have no meaning. The problem of finding the rotation that carries one set of measured vectors to another in the least-squares sense is the same computation with $Q$ the correlation matrix of the two sets, and it is posed in that form in the attitude-determination literature cited below.

**Remark (the arithmetic cost, and what the four numbers buy).** Representing a rotation by a quaternion costs four real numbers subject to one constraint, against nine for the matrix; composing two rotations is one quaternion product, sixteen multiplications and twelve additions, against twenty-seven multiplications for the matrix product; and renormalising a drifting quaternion is a four-term operation against the re-orthogonalisation of a matrix. The single respect in which the matrix is cheaper is the action on a vector: nine multiplications against the two quaternion products, thirty-two multiplications, of the sandwich. The eigenvector computation above is the fourth operation for which the four numbers are used, and the double cover is its only price: the eigenvector is determined up to sign, which is exactly the two-to-one redundancy of the parametrisation.

### The Differential and the Lie Algebra

**Theorem.** The Lie algebra of $Sp(1)$ is $\operatorname{Im}\mathbb{H}$ with the commutator bracket $[x,y] = xy - yx = 2(x\times y)$, where $\times$ is the cross product. The differential of the adjoint action at the identity is the map $\operatorname{Im}\mathbb{H}\to\mathrm{SO}(3)$, $x\mapsto \operatorname{ad}_x = [x,\cdot]$, and the map $x\mapsto \operatorname{ad}_x$ is an isomorphism of Lie algebras $\operatorname{Im}\mathbb{H}\cong\mathrm{SO}(3)$.

**Proof.** The tangent space of $Sp(1) = S^3$ at $1$ is the orthogonal complement of $1$, which is $\operatorname{Im}\mathbb{H}$. For pure imaginary $x,y$, the product is $xy = x\times y - \langle x, y\rangle$, so $xy - yx = 2(x\times y)$ and the bracket is $\mathbb{R}$-bilinear and antisymmetric. The adjoint action of $Sp(1)$ differentiates to the bracket of the Lie algebra, $\operatorname{ad}_x(y) = [x,y]$, and $\operatorname{ad}_x$ is skew-symmetric because $\langle x\times y, z\rangle = -\langle y, x\times z\rangle$. The map $x\mapsto\operatorname{ad}_x$ is injective: if $\operatorname{ad}_x = 0$ then $x\times y = 0$ for every $y$, so $x = 0$. Both $\operatorname{Im}\mathbb{H}$ and $\mathrm{SO}(3)$ are three-dimensional, so it is a linear isomorphism, and it preserves brackets because it is the derivative of a homomorphism of groups.

The Lie algebra isomorphism $\operatorname{Im}\mathbb{H}\cong\mathrm{SO}(3)$ is the differential form of the group isomorphism established below; it also identifies $\operatorname{Im}\mathbb{H}$ with $\mathrm{SU}(2)$, and the factor $2$ in the bracket is the infinitesimal shadow of the half-angle.

## The Double Cover of SO(3)

### The Kernel

**Theorem.** The kernel of the homomorphism $Sp(1)\to SO(3)$, $\tilde q\mapsto\operatorname{Ad}_q$, is $\{\pm1\}$.

**Proof.** If $\operatorname{Ad}_q = \mathrm{id}$ on $\operatorname{Im}\mathbb{H}$, then $qx = xq$ for every $x\in\operatorname{Im}\mathbb{H}$. Since $\tilde q$ commutes with $1$ and with its own vector part, it commutes with every element of $\mathbb{H}$, so $\tilde q\in Z(\mathbb{H}) = \mathbb{R}$. Together with $|\tilde q| = 1$ this gives $\tilde q = \pm1$. Conversely $\pm1$ act trivially.

Thus two unit quaternions $\tilde q$ and $-\tilde q$ determine the same rotation, and no other coincidence occurs.

### Surjectivity and the Covering

**Theorem.** The homomorphism $\operatorname{Ad} : Sp(1)\to SO(3)$ is surjective, and it induces an isomorphism of groups

$$
SO(3) \cong Sp(1)/\{\pm1\}.
$$

**Proof.** The differential at the identity is the isomorphism $\operatorname{Im}\mathbb{H}\to\mathrm{SO}(3)$ of the preceding section, so by the inverse function theorem $\operatorname{Ad}$ is a local diffeomorphism near $1$, and therefore its image is an open subset of $SO(3)$. The image is a subgroup, and it is compact as a continuous image of the compact group $Sp(1)$, hence closed in the Hausdorff group $SO(3)$. The group $SO(3)$ is connected, so the only non-empty subset that is both open and closed is the whole of it; therefore $\operatorname{Ad}$ is surjective. The first isomorphism theorem for groups, together with the computation of the kernel, gives $SO(3)\cong Sp(1)/\{\pm1\}$.

**Theorem (double cover).** The quotient map $Sp(1)\to Sp(1)/\{\pm1\}\cong SO(3)$ is a two-sheeted covering map of Lie groups, and it is the universal cover of $SO(3)$.

**Proof.** The group $\{\pm1\}$ is a discrete normal subgroup, so the quotient map is a covering map with fibres of two elements. Since $Sp(1)\cong S^3$ is simply connected, it is the universal cover of the quotient, which is $SO(3)$.

**Corollary.** The fundamental group of the rotation group is

$$
\pi_1(SO(3)) \cong \mathbb{Z}/2\mathbb{Z}.
$$

**Proof.** Since $Sp(1)$ is simply connected, the covering $p$ is the universal cover of $SO(3)$, and the group of deck transformations of the universal cover is isomorphic to $\pi_1(SO(3))$. The deck transformations are $\tilde q\mapsto -\tilde q$, a group of order two; hence $\pi_1(SO(3))\cong\mathbb{Z}/2\mathbb{Z}$.

The covering is non-trivial: the two elements $1$ and $-1$ of the fibre over the identity of $SO(3)$ are distinct, and no continuous section $SO(3)\to Sp(1)$ exists, because $SO(3)$ is not simply connected. This is the precise sense in which a rotation has two quaternion representatives and not one.

## The Exponential and the Composition of Rotations

### Conjugation by a Unit Quaternion

**Theorem.** Let $u$ be a unit vector and let $\tilde q = \cos\frac{\theta}{2} + u\sin\frac{\theta}{2}$. Then for $x\in\operatorname{Im}\mathbb{H}$,

$$
\operatorname{Ad}_q(x) = \cos\theta\, x + \sin\theta\, (u\times x) + (1-\cos\theta)\,\langle x, u\rangle\, u .
$$

In particular $\operatorname{Ad}_q(u) = u$, and on the plane $u^{\perp}\subset\operatorname{Im}\mathbb{H}$ the map $\operatorname{Ad}_q$ is the rotation through the angle $\theta$ that carries $x$ toward $u\times x$.

**Proof.** Write $x = x_{\parallel} + x_{\perp}$ with $x_{\parallel} = \langle x,u\rangle u$ parallel to $u$ and $x_{\perp}\perp u$. Since $\tilde q$ is a polynomial in $u$ it commutes with $u$, and $u^{-1} = -u$; hence $qx_{\parallel}\tilde q^{-1} = \langle x,u\rangle quq^{-1} = \langle x,u\rangle u = x_{\parallel}$. For the perpendicular part put $y = u\times x_{\perp}$; then $ux_{\perp} = u\times x_{\perp} - \langle u, x_{\perp}\rangle = y$ and $x_{\perp}u = -y$, while $yu = x_{\perp}$ by the vector triple product. With $c = \cos\frac{\theta}{2}$, $s = \sin\frac{\theta}{2}$ and $\tilde q^{-1} = c - su$,

$$
qx_{\perp}\tilde q^{-1} = (cx_{\perp}+sy)(c-su) = c^2x_{\perp} - cs\,x_{\perp}u + cs\,y - s^2\,yu = (c^2-s^2)x_{\perp} + 2cs\,y,
$$

using $x_{\perp}u = -y$ and $yu = x_{\perp}$. Since $c^2 - s^2 = \cos\theta$ and $2cs = \sin\theta$, the perpendicular part is rotated by $\theta$ in the plane spanned by $x_{\perp}$ and $y = u\times x_{\perp}$, and adding the fixed parallel part gives the displayed formula.

### The Half-Angle Formula

**Theorem (rotation by a unit quaternion).** Let $u$ be a unit vector and let $\theta$ be real. The rotation of $\operatorname{Im}\mathbb{H}$ about the axis $u$ through the angle $\theta$ is $\operatorname{Ad}_q$ with

$$
\tilde q = \cos\frac{\theta}{2} + u\sin\frac{\theta}{2} = \exp\!\Bigl(\frac{u\theta}{2}\Bigr),
$$

and $\tilde q$ is determined by the rotation up to the replacement $\tilde q\mapsto -\tilde q$.

**Proof.** The preceding theorem identifies $\operatorname{Ad}_q$ as the rotation about $u$ through $\theta$. If $\operatorname{Ad}_q = \operatorname{Ad}_{\tilde q'}$ then $\tilde q'\tilde q^{-1}$ lies in the kernel $\{\pm1\}$, so $\tilde q' = \pm \tilde q$.

The occurrence of the half-angle is the algebraic expression of the double cover: the rotation angle is $\theta$, but the quaternion carries $\theta/2$, so a rotation through $2\pi$, whose matrix is the identity, is represented by $\exp(\pi u) = -1$ and not by $1$.

### The Composition of Rotations

**Theorem.** For $q_1, q_2\in Sp(1)$,

$$
\operatorname{Ad}_{q_1}\circ\operatorname{Ad}_{q_2} = \operatorname{Ad}_{q_1q_2},
$$

and the rotation by $\theta_1$ about $u$ followed by the rotation by $\theta_2$ about $u$ is the rotation by $\theta_1+\theta_2$ about $u$.

**Proof.** The first identity is the multiplicativity of the adjoint action proved above, extended to any number of factors by induction. For the second, $\exp(\frac{u\theta_1}{2})\exp(\frac{u\theta_2}{2}) = \exp(\frac{u(\theta_1+\theta_2)}{2})$ because $u$ commutes with itself.

Thus composition of rotations is quaternion multiplication, and the failure of commutativity of $Sp(1)$ is exactly the failure of rotations about different axes to commute. The correspondence is a group homomorphism with kernel $\{\pm1\}$, hence two-to-one onto $SO(3)$.

## The Sandwich and the Action Table

### The Sandwich

**Definition.** The **sandwich** of an element $\tilde q$ is the map

$$
S_q : \mathbb{H}\longrightarrow\mathbb{H}, \qquad S_q(x) = qx\tilde{q}^{\natural}.
$$

For a unit quaternion the conjugate is the inverse, so on $Sp(1)$ the sandwich is the adjoint action of the preceding sections; off the unit sphere it differs from it by one factor.

**Theorem.** For every $\tilde q$,

$$
S_q = N(\tilde q)\,\operatorname{Ad}_q,
$$

so that the sandwich and the adjoint action coincide on the unit slice $N(\tilde q) = 1$; the sandwich scales the quaternion norm by $N(\tilde q)^2$, its determinant as a map of the four-dimensional space is $\det S_q = N(\tilde q)^4$, and it is invertible exactly when $\tilde q$ is a unit.

**Proof.** For $\tilde q\neq0$ one has $\tilde{q}^{\natural} = N(\tilde q)\tilde q^{-1}$, so $S_q(x) = qx\tilde{q}^{\natural} = N(\tilde q)\,qxq^{-1} = N(\tilde q)\operatorname{Ad}_q(x)$, and the two agree when $N(\tilde q) = 1$. The adjoint action has determinant one on the four-dimensional space, being the identity on the scalar line and a rotation on the vector subspace, so the determinant of the sandwich is $N(\tilde q)^4$, and an operator with nonzero determinant is invertible.

**Theorem.** The sandwich preserves the quaternion norm up to the square of $N(\tilde q)$,

$$
N\bigl(S_q(x)\bigr) = N(\tilde q)^2N(x),
$$

and it maps the scalar subspace to itself and the vector subspace to itself.

**Proof.** By multiplicativity of the quaternion norm, $N(qx\tilde{q}^{\natural}) = N(\tilde q)N(x)N(\tilde{q}^{\natural}) = N(\tilde q)^2N(x)$, since $N(\tilde{q}^{\natural}) = N(\tilde q)$. For a scalar $s$ one has $S_q(s) = qs\tilde{q}^{\natural} = s\,q\tilde{q}^{\natural} = sN(\tilde q)$, again a scalar, so the scalar line is preserved; for $\tilde q\neq0$ the sandwich is invertible and preserves the quaternion norm, hence it preserves the orthogonal complement of the scalar line, which is the vector subspace.

**Proposition.** For $\tilde q\neq0$ each of the operators $L_q(x) = qx$, $\rho_q(x) = xq$, $\operatorname{Ad}_q$ and $S_q$ is invertible, with kernel $0$ and image $\mathbb{H}$; for $\tilde q = 0$ all four are the zero operator.

**Proof.** The operators $L_q$ and $\rho_q$ of the regular representation are invertible exactly for a unit, as shown in *Quaternion 4x4 Regular Matrix Element Representation*; the adjoint action has inverse $\operatorname{Ad}_{\tilde q^{-1}}$, and the sandwich has inverse $N(\tilde q)^{-1}\operatorname{Ad}_{\tilde q^{-1}}$. At $\tilde q = 0$ every product with $\tilde q$ vanishes.

**Proposition.** The fixed subspace of the adjoint action of a unit $\tilde q$ is its centraliser in $\mathbb{H}$: all of $\mathbb{H}$ when $\tilde q$ is real, and the two-dimensional subalgebra $F[\tilde q] = \{a+b\tilde q\}$ otherwise. On the vector subspace the fixed directions are the axis line $\mathbb{R}\mathbf{q}$.

**Proof.** One has $\operatorname{Ad}_q(x) = x$ if and only if $qx = xq$, so the fixed space is the centraliser. A real element is central; the centraliser of a non-real element is the subalgebra generated by $\tilde q$ and $1$, of dimension two. On $\operatorname{Im}\mathbb{H}$ the fixed line is the rotation axis, and a rotation fixes no other direction.

### The Action on the Subspaces

Left and right multiplication are the operators of the regular representation, treated in *Quaternion 4x4 Regular Matrix Element Representation*; the adjoint action and the sandwich are those of the preceding sections. Throughout, $L_q(x) = qx$ is the left multiplication operator and $\rho_q(x) = xq$ the right one — the operator the regular-representation article writes $R_q$, renamed here because that symbol is the matrix of the adjoint action on $\operatorname{Im}\mathbb{H}$.

**Definition.** The **action table** of the operator representation records, for each operator, its effect on the scalar subspace $\mathbb{R}_{\mathbb{H}}$ and on the vector subspace $\operatorname{Im}\mathbb{H}$.

| Operator | On $\mathbb{R}_{\mathbb{H}}$ | On $\operatorname{Im}\mathbb{H}$ |
|---|---|---|
| $L_q$, left multiplication | $s\mapsto qs$, lands in the span of $1,\mathbf{q}$ | $\mathbf{x}\mapsto -\langle\mathbf{q},\mathbf{x}\rangle+q_0\mathbf{x}+\mathbf{q}\times\mathbf{x}$ |
| $\rho_q$, right multiplication | $s\mapsto sq = qs$ | $\mathbf{x}\mapsto -\langle\mathbf{x},\mathbf{q}\rangle+q_0\mathbf{x}+\mathbf{x}\times\mathbf{q}$ |
| $\operatorname{Ad}_q$, adjoint | identity | rotation by the angle and axis of $\tilde q$ |
| $S_q$, sandwich | $N(\tilde q)\,\mathrm{id}$ | $N(\tilde q)$ times the rotation of $\operatorname{Ad}_q$ |

**Proposition.** Left and right multiplication do not preserve the two subspaces individually — each sends the scalar line into the plane spanned by $1$ and the acting element — while the adjoint action and the sandwich do preserve the decomposition, acting as the identity, respectively the scale $N(\tilde q)$, on the scalar line and as a rotation, respectively a scaled rotation, on the vector subspace.

**Proof.** The element $L_q(s) = qs$ lies in the span of $1$ and $\tilde q$, and $L_q(\mathbf{x})$ has scalar part $-\langle\mathbf{q},\mathbf{x}\rangle$, so neither subspace is preserved in general; the same holds for $\rho_q$. The adjoint action fixes every scalar and carries the vector subspace to itself, and the sandwich is $N(\tilde q)$ times it.

**Corollary.** The adjoint action of a unit acts on the whole algebra as the direct sum of the identity on the scalar line and a rotation on the vector subspace, the representations of dimensions one and three into which the four-dimensional operator decomposes.

**Proof.** The decomposition $\mathbb{H} = \mathbb{R}_{\mathbb{H}}\oplus\operatorname{Im}\mathbb{H}$ is preserved, the first summand is fixed and the second carries the rotation.

### The Sandwich and the Polar Form

**Theorem.** Every non-zero quaternion has the polar form $\tilde q = |\tilde q|u$ with $u\in Sp(1)$, and the adjoint action depends only on the unit factor, $\operatorname{Ad}_q = \operatorname{Ad}_u$, while the sandwich carries the scale, $S_q = |\tilde q|^2\operatorname{Ad}_u$. The axis and angle of the rotation $\operatorname{Ad}_u$ are those of the polar form, $\mu = \mathbf{q}/|\mathbf{q}|$ and $\cos\frac{\theta}{2} = q_0/|\tilde q|$.

**Proof.** The scale cancels in the adjoint action because $\tilde q$ and $\tilde q^{-1}$ contribute $|\tilde q|$ and $|\tilde q|^{-1}$, while the sandwich carries $N(\tilde q) = |\tilde q|^2$; the axis-angle identification is the polar form of *Quaternion Polar Element Representation*, where the half-angle is the angle of the unit factor.

The biquaternion reading is in *Biquaternion Rotations and Lorentz Transformations*: there the sandwich is taken with the Hermitian dagger, $x\mapsto \tilde Qx\tilde{Q}^{*}$, and realises Lorentz transformations rather than rotations, an indefinite possibility closed here by the definiteness of the quaternion norm.

## Reflections and the Orthogonal Group

### The Reflection Formula

**Definition.** For a unit vector $v\in\operatorname{Im}\mathbb{H}$ define

$$
\rho_v : \mathbb{H}\longrightarrow\mathbb{H}, \qquad \rho_v(x) = -v\,x\,v^{-1} .
$$

**Theorem.** For a unit vector $v$, $\rho_v(x) = vxv$, and on $\operatorname{Im}\mathbb{H}$

$$
\rho_v(x) = x - 2\langle x, v\rangle v .
$$

Hence $\rho_v$ is the **reflection in the plane** $v^{\perp}\subset\operatorname{Im}\mathbb{H}$: it fixes every vector perpendicular to $v$, sends $v$ to $-v$, is $\mathbb{R}$-linear, preserves the quaternion norm, is an involution, and has determinant $-1$ on $\operatorname{Im}\mathbb{H}$.

**Proof.** Since $v^{-1} = v^{\natural} = -v$, we have $-vxv^{-1} = -vx(-v) = vxv$. For pure imaginary $v, x$ the product is $vx = v\times x - \langle v, x\rangle$, so $xv = -v\times x - \langle v,x\rangle$ and $vx + xv = -2\langle v,x\rangle$. Therefore

$$
vxv = (vx)v = -xv^2 - 2\langle v,x\rangle v = x - 2\langle v,x\rangle v,
$$

using $v^2 = -1$. The formula shows that $\rho_v$ is the identity on the hyperplane $\langle x,v\rangle = 0$ and equals $-v$ on $\mathbb{R}v$; linearity and norm preservation are immediate, and $\rho_v^2 = \mathrm{id}$ because the eigenvalues are $+1$ on the plane and $-1$ on the line, so the determinant is $-1$.

**Remark.** On the whole algebra $\mathbb{H}$, and not merely on $\operatorname{Im}\mathbb{H}$, the map $\rho_v$ is not the reflection in a hyperplane of $\mathbb{R}^4$: it also multiplies the scalar line by $-1$, so its fixed space is the two-dimensional plane $\operatorname{span}(e_0,v)^{\perp}$ and it acts as a rotation through $\pi$ in the plane $\operatorname{span}(e_0,v)$. The reflection statement above is the statement about the three-dimensional imaginary subspace, which is the space the rotation and reflection groups act on. This is the quaternionic instance of the signed inner conjugation action $\widetilde{\operatorname{Ad}}_v(x) = \alpha(v)xv^{-1}$ of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, in which the grade involution supplies the sign that distinguishes odd from even elements.

### Products of Two Reflections

**Theorem.** For unit vectors $v_1, v_2$,

$$
\rho_{v_1}\circ\rho_{v_2} = \operatorname{Ad}_{v_1v_2}.
$$

Consequently the composition of two reflections is a rotation, namely the rotation about the axis $v_1\times v_2$ through twice the angle between the planes $v_1^{\perp}$ and $v_2^{\perp}$.

**Proof.** Using $\rho_{v}(x) = -vxv^{-1}$,

$$
\rho_{v_1}(\rho_{v_2}(x)) = -v_1\bigl(-v_2xv_2^{-1}\bigr)v_1^{-1} = (v_1v_2)\,x\,(v_1v_2)^{-1} = \operatorname{Ad}_{v_1v_2}(x).
$$

The product $v_1v_2$ is $v_1\times v_2 - \langle v_1,v_2\rangle$, whose vector part is $v_1\times v_2$; by the half-angle formula the rotation angle $\theta$ of $\operatorname{Ad}_{v_1v_2}$ satisfies $\cos\frac{\theta}{2} = -\langle v_1,v_2\rangle = -\cos\phi$, where $\phi$ is the angle between $v_1$ and $v_2$. Hence $\theta \equiv 2\phi \pmod{2\pi}$ in the appropriate orientation, and the axis is $v_1\times v_2$, the direction of the intersection of the two planes.

Conversely every rotation is a product of two reflections. By the half-angle formula the rotation through $\theta$ about $u$ is $\operatorname{Ad}_q$ with $\tilde q = \cos\frac{\theta}{2}+u\sin\frac{\theta}{2}$; if $a$ is a unit vector perpendicular to $u$ and $v_1 = a$, $v_2 = (u\times a)\sin\frac{\theta}{2} - a\cos\frac{\theta}{2}$, then $v_1$ and $v_2$ are unit vectors in the plane $u^{\perp}$ and $v_1v_2 = \sin\frac{\theta}{2}\,a(u\times a) + \cos\frac{\theta}{2} = u\sin\frac{\theta}{2} + \cos\frac{\theta}{2} = \tilde q$, using $a(u\times a) = a\times(u\times a) = u$.

### Cartan–Dieudonné in Three Dimensions

**Theorem (Cartan–Dieudonné, dimension three).** Every element of $O(3)$ is a product of at most three reflections in planes through the origin. The orientation-preserving isometries are exactly the products of an even number of reflections, and the orientation-reversing isometries the products of an odd number.

**Proof.** This is the general Cartan–Dieudonné theorem of *Isometries and Orthogonal Transformations* specialised to a three-dimensional non-degenerate space: every isometry is a product of reflections in hyperplanes, and the number of factors can be reduced to at most the dimension, so at most three suffice. The parity is the determinant, which is $(-1)^{(\text{number of factors})}$ because each reflection has determinant $-1$.

In the quaternion algebra the two-factor products are $\tilde q = v_1v_2$, acting as the rotation $\operatorname{Ad}_q$, and conversely every unit quaternion is a product of two unit vectors: given $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with $q_0^2+|\mathbf q|^2 = 1$, choose a unit vector $a\perp\mathbf q$ and put $b = \mathbf q\times a - q_0a$, so that $ab = a\times b - \langle a,b\rangle = \mathbf q + q_0 = \tilde q$. Hence the even products of unit vectors are exactly the elements of $Sp(1)$, and the odd products are the elements of $\mathrm{Pin}(3)$ outside its even part, whose signed inner conjugations are the orientation-reversing isometries.

### The Pin Group

**Theorem (Pin and Spin).** Let $\mathrm{Pin}(3)$ be the subgroup of the units of the Clifford algebra $\mathrm{Cl}_{3,0}$ generated by the unit vectors, and let $\mathrm{Spin}(3) = \mathrm{Pin}(3)\cap \mathrm{Cl}^0_{3,0}$ be its even part. The signed inner conjugation action defines a surjective homomorphism

$$
\mathrm{Pin}(3)\longrightarrow O(3)
$$

with kernel $\{\pm1\}$, whose restriction to the even part is a surjective homomorphism $\mathrm{Spin}(3)\to SO(3)$ with kernel $\{\pm1\}$. The even Clifford algebra is $\mathrm{Cl}^0_{3,0}\cong\mathbb{H}$, and $\mathrm{Spin}(3)\cong Sp(1)$.

**Proof.** The general construction and the isomorphism $\mathrm{Cl}_{3,0}\cong\mathbb{H}\oplus\mathbb{H}$, whose even part $\mathrm{Cl}^0_{3,0}$ is a copy of $\mathbb{H}$, are those of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the signed inner conjugation of a unit vector is the reflection $\rho_v$, and the signed inner conjugation of an even unit is the conjugation $\operatorname{Ad}_q$. Surjectivity follows from Cartan–Dieudonné above, and the kernel $\{\pm1\}$ is computed as in the case of $Sp(1)$.

**Corollary.** There is a short exact sequence

$$
1 \longrightarrow \{\pm1\} \longrightarrow \mathrm{Pin}(3) \longrightarrow O(3) \longrightarrow 1,
$$

and an element of $O(3)$ is orientation-preserving exactly when it is a product of an even number of reflections. In particular $O(3)\cong SO(3)\rtimes \mathbb{Z}/2\mathbb{Z}$, the quotient by $SO(3)$ being the determinant.

## The Two-Sided Action and SO(4)

The adjoint action uses one unit quaternion. Using one on each side gives the full four-dimensional rotation group.

**Definition.** For $(q_1, q_2)\in Sp(1)\times Sp(1)$ define

$$
\Phi_{(q_1,q_2)} : \mathbb{H}\longrightarrow\mathbb{H}, \qquad \Phi_{(q_1,q_2)}(x) = q_1\,x\,q_2^{-1} = q_1x\tilde{q}^{\natural}_2 .
$$

**Theorem.** Each $\Phi_{(q_1,q_2)}$ is an $\mathbb{R}$-linear isometry of $\mathbb{H}\cong\mathbb{R}^4$ with determinant $+1$, and

$$
\Phi : Sp(1)\times Sp(1)\longrightarrow SO(4), \qquad (q_1,q_2)\mapsto\Phi_{(q_1,q_2)},
$$

is a surjective homomorphism with kernel $\{\pm(1,1)\}$. Hence

$$
SO(4) \cong (Sp(1)\times Sp(1))/\{\pm(1,1)\} \cong \mathrm{Spin}(4).
$$

**Proof.** Linearity is clear. Norm preservation: $N(q_1xq_2^{-1}) = N(q_1)N(x)N(q_2)^{-1} = N(x)$. Homomorphism: $\Phi_{(q_1,q_2)}\circ\Phi_{(r_1,r_2)} = \Phi_{(q_1r_1, q_2r_2)}$. Determinant: $\det\Phi_{(q_1,q_2)} = \pm1$ and depends continuously on $(q_1,q_2)$, which ranges over the connected set $Sp(1)\times Sp(1)$, so it is constant and equals its value $\det(\mathrm{id}) = 1$ at $(1,1)$. Kernel: if $\Phi_{(q_1,q_2)} = \mathrm{id}$ then evaluating at $x = 1$ gives $q_1q_2^{-1} = 1$, so $q_1 = q_2 = \tilde q$, and then $qxq^{-1} = x$ for all $x$, so $\tilde q\in\{\pm1\}$. Surjectivity: the differential of $\Phi$ at the identity is the linear map $(x,y)\mapsto\bigl(z\mapsto xz - zy\bigr)$ from $\operatorname{Im}\mathbb{H}\oplus\operatorname{Im}\mathbb{H}$ to $\mathrm{SO}(4)$; it is injective, because $xz = zy$ for all $z$ gives $x = y$ on taking $z = 1$ and then forces $x$ to be central, hence $x = y = 0$; since both spaces have dimension $6$, it is an isomorphism. Hence $\Phi$ is a local diffeomorphism, its image is open, and, being a compact subgroup, it is also closed in the connected group $SO(4)$, so the image is everything.

The kernel has order two, so $SO(4)$ is doubly covered by $Sp(1)\times Sp(1)$, which is simply connected as $S^3\times S^3$; this is the Spin group $\mathrm{Spin}(4)$ of the four-dimensional Euclidean space. Whereas $SO(3)$ is simple and its universal cover is the simple group $Sp(1)$, the group $SO(4)$ is not simple, and the two factors of the cover are the left and the right multiplications. The adjoint action of the diagonal subgroup $q_1 = q_2 = \tilde q$ is $\operatorname{Ad}_q$ on $\operatorname{Im}\mathbb{H}$ together with the identity on the scalar line, and it is the copy of $SO(3)$ found earlier.

## Homotopy Groups and the Double Cover

The double covering of the rotation group has a quantitative consequence for the parametrisation of a rotation by an angle.

**Theorem (periodicity).** Let $u$ be a unit vector and let $\tilde q(\theta) = \exp\!\bigl(\frac{u\theta}{2}\bigr) = \cos\frac{\theta}{2} + u\sin\frac{\theta}{2}$. Then

$$
\tilde q(\theta+2\pi) = -\tilde q(\theta), \qquad \tilde q(\theta+4\pi) = \tilde q(\theta),
$$

and $\operatorname{Ad}_{\tilde q(\theta+2\pi)} = \operatorname{Ad}_{\tilde q(\theta)}$. Consequently the map $\theta\mapsto\operatorname{Ad}_{\tilde q(\theta)}$ describing the rotation has period $2\pi$, while its quaternion lift $\tilde q$ has period $4\pi$.

**Proof.** Since $\exp(\frac{u(\theta+2\pi)}{2}) = \exp(\frac{u\theta}{2})\exp(\pi u) = -\tilde q(\theta)$ and $\exp(2\pi u) = 1$. The adjoint action is unchanged by $\tilde q\mapsto -\tilde q$ because the kernel is $\{\pm1\}$.

**Theorem.** The path $t\mapsto\exp(ut)$, $t\in[0,\pi]$, is a path in $Sp(1)$ from $1$ to $-1$; its image under the covering $Sp(1)\to SO(3)$ is a closed loop in $SO(3)$ that is not homotopic to the constant loop. Hence a rotation through the angle $2\pi$ corresponds to the non-identity element $-1$ of the fibre, and the identity quaternion is recovered only after the angle $4\pi$.

**Proof.** The path from $1$ to $-1$ does not close in $Sp(1)$, but its image does close in $SO(3)$ because $\operatorname{Ad}_{-1} = \operatorname{Ad}_1$. Since the covering is two-to-one with fibre $\{\pm1\}$, a loop in $SO(3)$ is null-homotopic if and only if its lift in $Sp(1)$ closes; here the lift does not close, so the loop is not null-homotopic, and it represents the generator of $\pi_1(SO(3))\cong\mathbb{Z}/2\mathbb{Z}$. Doubling the loop lifts to the path $t\mapsto\exp(ut)$, $t\in[0,2\pi]$, which closes at $\exp(2\pi u) = 1$.

This is the failure of the period $2\pi$: the rotation through $2\pi$ about $u$ is the identity of $SO(3)$, but the quaternion that represents it is $-1$, not $1$. The parametrisation returns to its initial value only after $4\pi$. The non-triviality of the covering is therefore not a convention but the statement $\pi_1(SO(3))\cong\mathbb{Z}/2\mathbb{Z}$, and it is the same statement as the existence of closed loops in $SO(3)$ that are not null-homotopic.

**Remark.** The biquaternion treatment of the same questions carries hyperbolic rotations, the Lorentz group and a family of retractions, because its norm is indefinite and its exponential takes values in a non-compact group. Here the quaternion norm is positive definite: the exponential of a vector is a unit quaternion, the group of units is $\mathbb{R}_{>0}\times Sp(1)$ with $Sp(1)$ compact, and there are no hyperbolic directions, so the only orthogonal groups that arise are the compact $SO(3)$ and $SO(4)$.

## Summary

The unit quaternions $Sp(1) = \{\tilde q : |\tilde q| = 1\} = S^3$ form a compact connected simply connected Lie group, non-abelian with centre $\{\pm1\}$, isomorphic to $SU(2)$, and every unit quaternion is $\cos\theta + u\sin\theta = \exp(u\theta)$ for an angle $\theta$ and a unit axis $u$. Hamilton's word for a unit quaternion is a versor, the unit part $U\tilde q$ of the polar decomposition $\tilde q = T\tilde q\,U\tilde q$; a versor is the quotient of two unit vectors, pictured as a directed arc of the great circle it turns about, and the right versors are the unit square roots of $-1$.

Conjugation by a unit, $\operatorname{Ad}_q(x) = qxq^{-1}$, is an algebra automorphism that preserves the quaternion norm and stabilises the imaginary subspace $\operatorname{Im}\mathbb{H}\cong\mathbb{R}^3$, where it acts as an isometry of determinant $+1$. The assignment $\tilde q\mapsto\operatorname{Ad}_q$ is a surjective homomorphism $Sp(1)\to SO(3)$ with kernel $\{\pm1\}$, so $SO(3)\cong Sp(1)/\{\pm1\}$ and the map is a two-sheeted covering, indeed the universal cover, giving $\pi_1(SO(3))\cong\mathbb{Z}/2\mathbb{Z}$.

The rotation about the unit axis $u$ through the angle $\theta$ is $\operatorname{Ad}_q$ with $\tilde q = \cos\frac{\theta}{2} + u\sin\frac{\theta}{2}$, the half-angle formula; composition of rotations is quaternion multiplication, $\operatorname{Ad}_{q_1}\circ\operatorname{Ad}_{q_2} = \operatorname{Ad}_{q_1q_2}$; and the parametrisation has period $4\pi$, since a rotation through $2\pi$ is represented by $-1$.

The reflection in the plane $v^{\perp}$ with unit normal $v$ is $\rho_v(x) = -vxv^{-1} = x - 2\langle x,v\rangle v$, an orientation-reversing involution; the product of two reflections is the rotation $\operatorname{Ad}_{v_1v_2}$ about the intersection line, and by Cartan–Dieudonné every isometry of $\mathbb{R}^3$ is a product of at most three reflections. The reflections and rotations together are the image of the Pin group $\mathrm{Pin}(3)$, whose even part is $\mathrm{Spin}(3)\cong Sp(1)$, and $O(3)\cong SO(3)\rtimes\mathbb{Z}/2\mathbb{Z}$.

Finally, the two-sided action $\Phi_{(q_1,q_2)}(x) = q_1xq_2^{-1}$ is a surjective homomorphism $Sp(1)\times Sp(1)\to SO(4)$ with kernel $\{\pm(1,1)\}$, so $SO(4)\cong \mathrm{Spin}(4)\cong (Sp(1)\times Sp(1))/\{\pm1\}$; the diagonal copy of $Sp(1)$ in it is the adjoint action that gives the rotations of the three-dimensional imaginary subspace.

The sandwich $S_q(x) = qx\tilde{q}^{\natural}$ is the adjoint action rescaled, $S_q = N(\tilde q)\operatorname{Ad}_q$, so the two coincide exactly on the unit slice and differ elsewhere by the factor $N(\tilde q)$; the sandwich multiplies the quaternion norm by $N(\tilde q)^2$ and has determinant $N(\tilde q)^4$. It preserves the scalar and the vector subspaces, acting by the identity, respectively by the scale $N(\tilde q)$, on the scalar line and by a rotation, respectively a scaled rotation, on the vector subspace; the action table records this beside the behaviour of the left and right multiplications $L_q$ and $\rho_q$ of the regular representation, which preserve neither subspace. For $\tilde q\neq0$ all four operators are invertible, and the fixed subspace of the adjoint action is the centraliser of $\tilde q$, with the axis line as the fixed direction on the imaginary subspace. The adjoint action depends only on the unit factor of the polar form while the sandwich carries the scale $|\tilde q|^2$; the biquaternion reading takes the sandwich with the Hermitian dagger and realises an indefinite group instead, a possibility closed here by the definiteness of the quaternion norm.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3 = \sum_\mu q_\mu e_\mu$ | General quaternion, scalar part $q_0$, vector part $\mathbf{q}$ |
| $\tilde{q}^{\natural} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ | Quaternion conjugate |
| $N(\tilde q) = \tilde q\tilde{q}^{\natural} = \lvert \tilde q\rvert^2$ | Quaternion norm and modulus |
| $U\tilde q = \tilde q/\lvert\tilde q\rvert$, $T\tilde q = \lvert\tilde q\rvert$ | Versor and tensor of $\tilde q$ (Hamilton); a versor is a unit quaternion, so $Sp(1)$ is the group of versors |
| $\operatorname{Im}\mathbb{H}\cong\mathbb{R}^3$ | Imaginary quaternions, the space of vectors |
| $\langle x, y\rangle = \mathrm{Sc}(x y^{\natural})$ | Real inner product on $\operatorname{Im}\mathbb{H}$ |
| $Sp(1) = \{\tilde q : \lvert \tilde q\rvert = 1\} = S^3$ | Group of unit quaternions |
| $Z(Sp(1)) = \{\pm1\}$ | Centre of $Sp(1)$ |
| $\exp(u\theta) = \cos\theta + u\sin\theta$ | Exponential of a unit vector |
| $SU(2)$ | Special unitary group, $Sp(1)\cong SU(2)$ |
| $\operatorname{Ad}_q(x) = qxq^{-1}$ | Adjoint action |
| $S_q(x) = qx\tilde{q}^{\natural} = N(\tilde q)\operatorname{Ad}_q$ | Sandwich; equals the adjoint action on the unit slice |
| $L_q(x) = qx$, $\rho_q(x) = xq$ | Left and right multiplication operators of the regular representation |
| $R_q$ | Matrix of $\operatorname{Ad}_q$ on $\operatorname{Im}\mathbb{H}$ |
| $K(Q)$ | Fitting matrix of a real $3\times3$ matrix $Q$, with $q^{T}K(Q)q = \operatorname{tr}(R_q^{T}Q)$; its largest eigenvector is the quaternion of the rotation closest to $Q$ |
| $\operatorname{ad}_x(y) = [x,y] = 2(x\times y)$ | Adjoint map of the Lie algebra $\operatorname{Im}\mathbb{H}$ |
| $\operatorname{Im}\mathbb{H}\cong\mathrm{SO}(3)\cong\mathrm{SU}(2)$ | Lie algebra of $Sp(1)\cong SU(2)$ and of $SO(3)$ |
| $SO(3)$ | Rotation group of $\mathbb{R}^3$, $\cong Sp(1)/\{\pm1\}$ |
| $O(3)\cong SO(3)\rtimes\mathbb{Z}/2\mathbb{Z}$ | Orthogonal group of $\mathbb{R}^3$ |
| $\rho_v(x) = -vxv^{-1}$ | Reflection in the plane $v^{\perp}$, $v$ a unit vector |
| $\mathrm{Pin}(3)$ | Pin group, generated by the unit vectors |
| $\mathrm{Spin}(3) = \mathrm{Pin}(3)\cap\mathrm{Cl}^0_{3,0}\cong Sp(1)$ | Spin group; $\mathrm{Cl}_{3,0}$ is the Clifford algebra of the Euclidean form on $\mathbb{R}^3$ and $\mathrm{Cl}^0_{3,0}$ its even part |
| $\Phi_{(q_1,q_2)}(x) = q_1xq_2^{-1}$ | Two-sided action of $Sp(1)\times Sp(1)$ |
| $SO(4)\cong\mathrm{Spin}(4)\cong(Sp(1)\times Sp(1))/\{\pm1\}$ | Rotation group of $\mathbb{R}^4$ |
| $\pi_1(SO(3))\cong\mathbb{Z}/2\mathbb{Z}$ | Fundamental group of the rotation group |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, 1853), for the origin of the quaternion representation of rotations, of the conjugation action, and of the versor and tensor notation.
- William Rowan Hamilton, *Elements of Quaternions*, 2nd edition, edited by Charles Jasper Joly (Longmans, Green & Company, 1899), for the versor and tensor notation, the quotient of two vectors and the composition of versors as the sum of arcs.
- Peter Guthrie Tait, *An Elementary Treatise on Quaternions* (Cambridge University Press, 3rd ed. 1890), for the operator form of quaternion multiplication and rotation.
- Olinde Rodrigues, "Des lois géométriques qui régissent les déplacements d'un système solide", *Journal de Mathématiques Pures et Appliquées* **5** (1840) 380–440, for the Euler–Rodrigues rotation formula.
- Felix Klein, *Vorlesungen über das Ikosaeder und die Auflösung der Gleichungen vom fünften Grade* (Teubner, 1884), for the rotation-group viewpoint on the unit quaternions.
- Simon L. Altmann, *Rotations, Quaternions and Double Groups* (Oxford University Press, 1986), for the double cover, the half-angle formula and the topology of the rotation group.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the reflections, the Pin and Spin groups and the quaternion parametrisation.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the Lie group $SU(2)$, its relation to $SO(3)$ and the covering-space argument.
- Alexander Kirillov Jr., *An Introduction to Lie Groups and Lie Algebras* (Cambridge University Press, 2008), for the exponential map, the adjoint representation and the structure of $SO(3)$ and $SO(4)$.
- Emil Artin, *Geometric Algebra* (Interscience, 1957), for the Cartan–Dieudonné theorem and the structure of the orthogonal group.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the conjugation action and the rotation groups.
- Grace Wahba, "A least squares estimate of satellite attitude", *SIAM Review* **7** (1965) 409, for the least-squares attitude problem whose solution is the eigenvector problem of the fitting matrix.
- Berthold K. P. Horn, "Closed-form solution of absolute orientation using unit quaternions", *Journal of the Optical Society of America A* **4** (1987) 629–642, for the closed-form solution by the largest eigenvector of the symmetric $4\times4$ matrix, the version of the computation given here.
- Samuel W. Shepperd, "Quaternion from rotation matrix", *Journal of Guidance and Control* **1** (1978) 223–224, for the branch that takes the square root of the largest of the four diagonal quantities, the numerically stable form of the reconstruction.
- Malcolm D. Shuster, "A survey of attitude representations", *Journal of the Astronautical Sciences* **41** (1993) 439–517, for the taxonomy of the attitude representations and for the conventions — active against passive, frame against vector — that the matrix and quaternion formulas of this article fix by the adjoint action $\operatorname{Ad}_q(x) = qxq^{-1}$.
