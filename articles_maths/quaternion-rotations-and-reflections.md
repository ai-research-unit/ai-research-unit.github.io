
# __Quaternion Rotations and Reflections__

## Introduction

This article describes the orthogonal group of three-dimensional Euclidean space as it is realised by the units of the quaternion algebra $\mathbb{H}$. The starting point is the group $Sp(1)$ of unit quaternions and the identification of its adjoint action on the imaginary quaternions with the rotation group $SO(3)$; the endpoint is the full orthogonal group $O(3)$ and, more generally, the two-sided action of $Sp(1)\times Sp(1)$ on $\mathbb{H}$ that exhausts $SO(4)$. Along the way the article explains why the covering $Sp(1)\to SO(3)$ is two-to-one, why the quaternion parametrisation of a rotation has period $4\pi$ where the rotation itself has period $2\pi$, and how reflections sit inside the same algebra as the twisted adjoint action of the unit vectors.

The treatment is mathematical throughout. A rotation is an element of $SO(3)$ and a reflection is an element of $O(3)$; no physical object is introduced, no state of a physical system is named, and no physical interpretation is invoked. The group $Sp(1)$ is treated as a group of quaternions, and the maps $Sp(1)\to SO(3)$ and $Sp(1)\times Sp(1)\to SO(4)$ are treated as covering homomorphisms of Lie groups.

The quaternion algebra, its basis $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, its conjugation, its norm form $N(q) = q\bar{q}$ and its imaginary subspace $\operatorname{Im}\mathbb{H}\cong\mathbb{R}^3$ are taken from *Quaternion Algebra*. The structure of $\mathbb{H}$ as a simple algebra and its matrix representations are taken from *Quaternion Representations*. The general construction of the Clifford, Pin and Spin groups, of which the results below are the three-dimensional instance, is the subject of *The Clifford, Pin and Spin Groups*; the parity of the Cartan–Dieudonné reflection length is taken from *The Rotation Group and Orientation* and from *Isometries and Orthogonal Transformations*. The complex plane, where the same questions have the degenerate answer that multiplication by a unit is already a rotation and the sandwich action is trivial, is treated in *Rotations and Reflections in the Complex Plane*.

Throughout, a general quaternion is $q = q_0 + \mathbf{q}$ with scalar part $q_0$ and vector part $\mathbf{q} = q_1e_1+q_2e_2+q_3e_3 \in \operatorname{Im}\mathbb{H}$, the conjugate is $\bar{q} = q_0 - \mathbf{q}$, the norm form is $N(q) = q\bar{q} = |q|^2$, and the real inner product of two vectors of $\operatorname{Im}\mathbb{H}$ is $\langle x, y\rangle = \operatorname{Sc}(x\bar{y}) = \sum_{k=1}^{3} x_ky_k$. A point of $\operatorname{Im}\mathbb{H}$ is a **vector**, and $|x|^2 = \langle x,x\rangle$. The transpose of a matrix $A$ is $A^{T}$ and the conjugate transpose is $A^{\dagger}$.

## The Unit Quaternions

### Definition and Group Structure

**Definition.** The **unit quaternions**, or the **quaternion unit group**, are

$$
Sp(1) = \{q \in \mathbb{H} : N(q) = 1\} = \{q \in \mathbb{H} : |q| = 1\}.
$$

As a subset of $\mathbb{H}\cong\mathbb{R}^4$ it is the unit sphere $S^3$.

**Theorem.** $Sp(1)$ is a group under quaternion multiplication and is the kernel of the norm homomorphism $\mathbb{H}^{\times}\to\mathbb{R}_{>0}$, $q\mapsto|q|$.

**Proof.** The norm form is multiplicative, $N(uv) = N(u)N(v)$, because $uv\overline{uv} = uv\bar{v}\bar{u} = uN(v)\bar{u} = N(u)N(v)$; hence if $|u| = |v| = 1$ then $|uv| = 1$, and if $|u| = 1$ then $u^{-1} = \bar{u}$ has $|u^{-1}| = 1$. Associativity and the identity $1\in Sp(1)$ are inherited from $\mathbb{H}$, and multiplication is a surjective homomorphism $\mathbb{H}^{\times}\to\mathbb{R}_{>0}$ with kernel exactly $Sp(1)$. $\square$

For every unit quaternion $q = q_0 + \mathbf{q}$ one has $q^{-1} = \bar{q} = q_0 - \mathbf{q}$, so inversion is quaternion conjugation. The group is non-abelian; its centre is the two-element group

$$
Z(Sp(1)) = \{\pm 1\},
$$

because a quaternion commuting with every element of $\mathbb{H}$ is real.

### Polar Form and the Exponential

**Theorem (polar form).** Every unit quaternion has an expression

$$
q = \cos\theta + u\sin\theta, \qquad 0 \leq \theta \leq \pi, \ u \in \operatorname{Im}\mathbb{H},\ |u| = 1,
$$

in which the angle $\theta$ is unique; the axis $u$ is unique when $0 < \theta < \pi$, while for $\theta = 0$ and $\theta = \pi$ the quaternion is $q = 1$ and $q = -1$ respectively and $u$ is arbitrary.

**Proof.** A unit quaternion has $q_0^2 + |\mathbf{q}|^2 = 1$, so there is a unique $\theta\in[0,\pi]$ with $q_0 = \cos\theta$ and $|\mathbf{q}| = \sin\theta$. If $\sin\theta\neq0$ then $u = \mathbf{q}/\sin\theta$ is a unit vector, uniquely determined by $q$, and $q = \cos\theta+u\sin\theta$; if $\sin\theta = 0$ then $\mathbf{q} = 0$ and $q = \pm1$. $\square$

**Theorem (exponential).** For a unit vector $u\in\operatorname{Im}\mathbb{H}$ and real $\theta$,

$$
\exp(u\theta) = \sum_{n\ge0}\frac{(u\theta)^n}{n!} = \cos\theta + u\sin\theta,
$$

the series converging absolutely. Consequently $Sp(1)$ is the image of the exponential map of the Lie algebra $\operatorname{Im}\mathbb{H}$, and every unit quaternion is $\exp(u\theta)$ for some unit vector $u$ and real $\theta$.

**Proof.** Since $u^2 = -1$, the even part of the series is $\sum_k(-1)^k\theta^{2k}/(2k)! = \cos\theta$ and the odd part is $u\sum_k(-1)^k\theta^{2k+1}/(2k+1)! = u\sin\theta$. The polar form exhibits each unit quaternion in this shape. $\square$

The exponential satisfies $\exp(u(\theta+2\pi)) = -\exp(u\theta)$ because $\exp(2\pi u) = -1$, and $\exp(u(\theta+4\pi)) = \exp(u\theta)$; this doubling is the algebraic root of the periodicity discussed below.

### The Identification with SU(2)

**Definition.** Let $\sigma_1, \sigma_2, \sigma_3$ be the Pauli matrices, in which $i$ denotes the imaginary unit of $\mathbb{C}$,

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
\sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad
\sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$

and define the real-linear map

$$
\iota : \mathbb{H}\longrightarrow M_2(\mathbb{C}), \qquad
\iota(e_0) = I, \quad \iota(e_1) = -i\sigma_1, \quad \iota(e_2) = -i\sigma_2, \quad \iota(e_3) = -i\sigma_3 .
$$

**Theorem.** The map $\iota$ is an injective homomorphism of real algebras, and it restricts to an isomorphism of groups $Sp(1)\cong SU(2)$.

**Proof.** The matrices $\iota(e_k) = -i\sigma_k$ are traceless with square $-I$, and they satisfy the quaternion relations $\iota(e_j)\iota(e_k) = \iota(e_j e_k)$: for instance $\iota(e_1)\iota(e_2) = (-i\sigma_1)(-i\sigma_2) = -\sigma_1\sigma_2 = -i\sigma_3 = \iota(e_3)$ and $\iota(e_2)\iota(e_1) = \iota(-e_3)$, so the relations $e_1e_2 = e_3$ and $e_2e_1 = -e_3$ are carried over, and the remaining relations follow by the same computation. Hence $\iota$ is a homomorphism, and it is injective because $\iota(e_0),\dots,\iota(e_3)$ are linearly independent over $\mathbb{R}$. The conjugate transpose satisfies $\iota(q)^{\dagger} = \iota(\bar{q})$, and the determinant is $\det\iota(q) = q_0^2 + q_1^2 + q_2^2 + q_3^2 = |q|^2$, since $\iota(q) = q_0I + N$ with $N$ traceless with $N^2 = -(q_1^2+q_2^2+q_3^2)I$ and eigenvalues $\pm i\sqrt{q_1^2+q_2^2+q_3^2}$. Therefore $|q| = 1$ is equivalent to $\iota(q)$ being unitary with determinant $1$, which is the definition of $SU(2)$. $\square$

**Theorem.** $Sp(1)\cong S^3$ is compact, connected, and simply connected, and it is a three-dimensional real Lie group with Lie algebra $\operatorname{Im}\mathbb{H}$.

**Proof.** As $S^3$ it is a closed bounded subset of $\mathbb{R}^4$, hence compact, and connected. The sphere $S^n$ is simply connected for $n\geq2$, by the standard argument that a loop in $S^n$ can be pushed off a point and contracted in the complementary ball; hence $S^3$ is simply connected. The smooth structure and the group law make it a Lie group of dimension $3$, and its Lie algebra is the tangent space at the identity, which is $\operatorname{Im}\mathbb{H}$ with the commutator bracket. $\square$

## The Adjoint Action on the Imaginary Quaternions

### The Adjoint Action

**Definition.** For $q\in Sp(1)$ the **adjoint action** is

$$
\operatorname{Ad}_q : \mathbb{H}\longrightarrow\mathbb{H}, \qquad \operatorname{Ad}_q(x) = qxq^{-1} = qx\bar{q}.
$$

**Theorem.** For every $q\in Sp(1)$ the map $\operatorname{Ad}_q$ is an $\mathbb{R}$-algebra automorphism of $\mathbb{H}$ that preserves the norm form and the scalar part. It restricts to a linear isometry of $\operatorname{Im}\mathbb{H}$, and the assignment $q\mapsto\operatorname{Ad}_q$ is a group homomorphism $Sp(1)\to GL(\operatorname{Im}\mathbb{H})$.

**Proof.** Conjugation by an invertible element is an algebra automorphism: the map $x\mapsto qxq^{-1}$ is $\mathbb{R}$-linear and a bijection with inverse $x\mapsto q^{-1}xq$, and it respects multiplication because $(qaq^{-1})(qbq^{-1}) = q(ab)q^{-1}$; for $|q| = 1$ the inverse is $x\mapsto\bar{q}xq$. Norm preservation: $N(qxq^{-1}) = N(q)N(x)N(q)^{-1} = N(x)$. Scalar part: if $x\in\operatorname{Im}\mathbb{H}$ then conjugation reverses the order of the factors, so $\overline{\operatorname{Ad}_q(x)} = \overline{q^{-1}}\,\bar{x}\,\bar{q} = q\,(-x)\,\bar{q} = -qx\bar{q} = -\operatorname{Ad}_q(x)$, and the scalar part of $\operatorname{Ad}_q(x)$ vanishes. Hence $\operatorname{Ad}_q$ preserves $\operatorname{Im}\mathbb{H}$, and since it preserves the norm form there it is an isometry. Finally $\operatorname{Ad}_{q_1}\circ\operatorname{Ad}_{q_2} = \operatorname{Ad}_{q_1q_2}$ and $\operatorname{Ad}_1 = \mathrm{id}$ by associativity. $\square$

### The Homomorphism to SO(3)

**Definition.** The **orthogonal group** of $\mathbb{R}^3$ is $O(3) = \{A\in GL_3(\mathbb{R}) : A^{T}A = I\}$, and the **rotation group** is the subgroup $SO(3)$ of matrices of determinant $+1$.

**Theorem.** For every $q\in Sp(1)$ the isometry $\operatorname{Ad}_q$ of $\operatorname{Im}\mathbb{H}$ has determinant $+1$. Hence the homomorphism $q\mapsto\operatorname{Ad}_q$ takes values in $SO(3)$.

**Proof.** An isometry of a three-dimensional real inner product space has determinant $\pm1$. The determinant function $\det\circ\operatorname{Ad} : Sp(1)\to\{\pm1\}$ is continuous, and $Sp(1)$ is connected, so its image is connected in the discrete two-point set; hence it is constant, and its value at $q = 1$ is $\det(\mathrm{id}) = 1$. $\square$

In the basis $(e_1, e_2, e_3)$ of $\operatorname{Im}\mathbb{H}$ the matrix of $\operatorname{Ad}_q$, with $q = q_0 + q_1e_1 + q_2e_2 + q_3e_3$, is

$$
R_q = \begin{pmatrix}
1 - 2(q_2^2 + q_3^2) & 2(q_1q_2 - q_0q_3) & 2(q_1q_3 + q_0q_2) \\
2(q_1q_2 + q_0q_3) & 1 - 2(q_1^2 + q_3^2) & 2(q_2q_3 - q_0q_1) \\
2(q_1q_3 - q_0q_2) & 2(q_2q_3 + q_0q_1) & 1 - 2(q_1^2 + q_2^2)
\end{pmatrix},
$$

whose trace is $\operatorname{tr}R_q = 4q_0^2 - 1$. The formula is the coordinate expression of $\operatorname{Ad}_q$ and is the standard quaternion parametrisation of the rotation group.

### The Differential and the Lie Algebra

**Theorem.** The Lie algebra of $Sp(1)$ is $\operatorname{Im}\mathbb{H}$ with the commutator bracket $[x,y] = xy - yx = 2(x\times y)$, where $\times$ is the cross product. The differential of the adjoint action at the identity is the map $\operatorname{Im}\mathbb{H}\to\mathfrak{so}(3)$, $x\mapsto \operatorname{ad}_x = [x,\cdot]$, and the map $x\mapsto \operatorname{ad}_x$ is an isomorphism of Lie algebras $\operatorname{Im}\mathbb{H}\cong\mathfrak{so}(3)$.

**Proof.** The tangent space of $Sp(1) = S^3$ at $1$ is the orthogonal complement of $1$, which is $\operatorname{Im}\mathbb{H}$. For pure imaginary $x,y$, the product is $xy = x\times y - \langle x, y\rangle$, so $xy - yx = 2(x\times y)$ and the bracket is $\mathbb{R}$-bilinear and antisymmetric. The adjoint representation of $Sp(1)$ differentiates to the adjoint representation of the Lie algebra, $\operatorname{ad}_x(y) = [x,y]$, and $\operatorname{ad}_x$ is skew-symmetric because $\langle x\times y, z\rangle = -\langle y, x\times z\rangle$. The map $x\mapsto\operatorname{ad}_x$ is injective: if $\operatorname{ad}_x = 0$ then $x\times y = 0$ for every $y$, so $x = 0$. Both $\operatorname{Im}\mathbb{H}$ and $\mathfrak{so}(3)$ are three-dimensional, so it is a linear isomorphism, and it preserves brackets because it is the derivative of a homomorphism of groups. $\square$

The Lie algebra isomorphism $\operatorname{Im}\mathbb{H}\cong\mathfrak{so}(3)$ is the differential form of the group isomorphism established below; it also identifies $\operatorname{Im}\mathbb{H}$ with $\mathfrak{su}(2)$ through the matrices $\iota$ of the preceding section, and the factor $2$ in the bracket is the infinitesimal shadow of the half-angle.

## The Double Cover of SO(3)

### The Kernel

**Theorem.** The kernel of the homomorphism $Sp(1)\to SO(3)$, $q\mapsto\operatorname{Ad}_q$, is $\{\pm1\}$.

**Proof.** If $\operatorname{Ad}_q = \mathrm{id}$ on $\operatorname{Im}\mathbb{H}$, then $qx = xq$ for every $x\in\operatorname{Im}\mathbb{H}$. Since $q$ commutes with $1$ and with its own vector part, it commutes with every element of $\mathbb{H}$, so $q\in Z(\mathbb{H}) = \mathbb{R}$. Together with $|q| = 1$ this gives $q = \pm1$. Conversely $\pm1$ act trivially. $\square$

Thus two unit quaternions $q$ and $-q$ determine the same rotation, and no other coincidence occurs.

### Surjectivity and the Covering

**Theorem.** The homomorphism $\operatorname{Ad} : Sp(1)\to SO(3)$ is surjective, and it induces an isomorphism of groups

$$
SO(3) \cong Sp(1)/\{\pm1\}.
$$

**Proof.** The differential at the identity is the isomorphism $\operatorname{Im}\mathbb{H}\to\mathfrak{so}(3)$ of the preceding section, so by the inverse function theorem $\operatorname{Ad}$ is a local diffeomorphism near $1$, and therefore its image is an open subset of $SO(3)$. The image is a subgroup, and it is compact as a continuous image of the compact group $Sp(1)$, hence closed in the Hausdorff group $SO(3)$. The group $SO(3)$ is connected, so the only non-empty subset that is both open and closed is the whole of it; therefore $\operatorname{Ad}$ is surjective. The first isomorphism theorem for groups, together with the computation of the kernel, gives $SO(3)\cong Sp(1)/\{\pm1\}$. $\square$

**Theorem (double cover).** The quotient map $Sp(1)\to Sp(1)/\{\pm1\}\cong SO(3)$ is a two-sheeted covering map of Lie groups, and it is the universal cover of $SO(3)$.

**Proof.** The group $\{\pm1\}$ is a discrete normal subgroup, so the quotient map is a covering map with fibres of two elements. Since $Sp(1)\cong S^3$ is simply connected, it is the universal cover of the quotient, which is $SO(3)$. $\square$

**Corollary.** The fundamental group of the rotation group is

$$
\pi_1(SO(3)) \cong \mathbb{Z}/2\mathbb{Z}.
$$

**Proof.** Since $Sp(1)$ is simply connected, the covering $p$ is the universal cover of $SO(3)$, and the group of deck transformations of the universal cover is isomorphic to $\pi_1(SO(3))$. The deck transformations are $q\mapsto -q$, a group of order two; hence $\pi_1(SO(3))\cong\mathbb{Z}/2\mathbb{Z}$. $\square$

The covering is non-trivial: the two elements $1$ and $-1$ of the fibre over the identity of $SO(3)$ are distinct, and no continuous section $SO(3)\to Sp(1)$ exists, because $SO(3)$ is not simply connected. This is the precise sense in which a rotation has two quaternion representatives and not one.

## The Half-Angle Formula and the Composition of Rotations

### Conjugation by a Unit Quaternion

**Theorem.** Let $u$ be a unit vector and let $q = \cos\frac{\theta}{2} + u\sin\frac{\theta}{2}$. Then for $x\in\operatorname{Im}\mathbb{H}$,

$$
\operatorname{Ad}_q(x) = \cos\theta\, x + \sin\theta\, (u\times x) + (1-\cos\theta)\,\langle x, u\rangle\, u .
$$

In particular $\operatorname{Ad}_q(u) = u$, and on the plane $u^{\perp}\subset\operatorname{Im}\mathbb{H}$ the map $\operatorname{Ad}_q$ is the rotation through the angle $\theta$ that carries $x$ toward $u\times x$.

**Proof.** Write $x = x_{\parallel} + x_{\perp}$ with $x_{\parallel} = \langle x,u\rangle u$ parallel to $u$ and $x_{\perp}\perp u$. Since $q$ is a polynomial in $u$ it commutes with $u$, and $u^{-1} = -u$; hence $qx_{\parallel}q^{-1} = \langle x,u\rangle quq^{-1} = \langle x,u\rangle u = x_{\parallel}$. For the perpendicular part put $y = u\times x_{\perp}$; then $ux_{\perp} = u\times x_{\perp} - \langle u, x_{\perp}\rangle = y$ and $x_{\perp}u = -y$, while $yu = x_{\perp}$ by the vector triple product. With $c = \cos\frac{\theta}{2}$, $s = \sin\frac{\theta}{2}$ and $q^{-1} = c - su$,

$$
qx_{\perp}q^{-1} = (cx_{\perp}+sy)(c-su) = c^2x_{\perp} - cs\,x_{\perp}u + cs\,y - s^2\,yu = (c^2-s^2)x_{\perp} + 2cs\,y,
$$

using $x_{\perp}u = -y$ and $yu = x_{\perp}$. Since $c^2 - s^2 = \cos\theta$ and $2cs = \sin\theta$, the perpendicular part is rotated by $\theta$ in the plane spanned by $x_{\perp}$ and $y = u\times x_{\perp}$, and adding the fixed parallel part gives the displayed formula. $\square$

### The Half-Angle Formula

**Theorem (rotation by a unit quaternion).** Let $u$ be a unit vector and let $\theta$ be real. The rotation of $\operatorname{Im}\mathbb{H}$ about the axis $u$ through the angle $\theta$ is $\operatorname{Ad}_q$ with

$$
q = \cos\frac{\theta}{2} + u\sin\frac{\theta}{2} = \exp\!\Bigl(\frac{u\theta}{2}\Bigr),
$$

and $q$ is determined by the rotation up to the replacement $q\mapsto -q$.

**Proof.** The preceding theorem identifies $\operatorname{Ad}_q$ as the rotation about $u$ through $\theta$. If $\operatorname{Ad}_q = \operatorname{Ad}_{q'}$ then $q'q^{-1}$ lies in the kernel $\{\pm1\}$, so $q' = \pm q$. $\square$

The occurrence of the half-angle is the algebraic expression of the double cover: the rotation angle is $\theta$, but the quaternion carries $\theta/2$, so a rotation through $2\pi$, whose matrix is the identity, is represented by $\exp(\pi u) = -1$ and not by $1$.

### The Composition of Rotations

**Theorem.** For $q_1, q_2\in Sp(1)$,

$$
\operatorname{Ad}_{q_1}\circ\operatorname{Ad}_{q_2} = \operatorname{Ad}_{q_1q_2},
$$

and the rotation by $\theta_1$ about $u$ followed by the rotation by $\theta_2$ about $u$ is the rotation by $\theta_1+\theta_2$ about $u$.

**Proof.** The first identity is the multiplicativity of the adjoint action proved above, extended to any number of factors by induction. For the second, $\exp(\frac{u\theta_1}{2})\exp(\frac{u\theta_2}{2}) = \exp(\frac{u(\theta_1+\theta_2)}{2})$ because $u$ commutes with itself. $\square$

Thus composition of rotations is quaternion multiplication, and the failure of commutativity of $Sp(1)$ is exactly the failure of rotations about different axes to commute. The correspondence is a group homomorphism with kernel $\{\pm1\}$, hence two-to-one onto $SO(3)$.

## Reflections

### The Reflection Formula

**Definition.** For a unit vector $v\in\operatorname{Im}\mathbb{H}$ define

$$
\rho_v : \mathbb{H}\longrightarrow\mathbb{H}, \qquad \rho_v(x) = -v\,x\,v^{-1} .
$$

**Theorem.** For a unit vector $v$, $\rho_v(x) = vxv$, and on $\operatorname{Im}\mathbb{H}$

$$
\rho_v(x) = x - 2\langle x, v\rangle v .
$$

Hence $\rho_v$ is the **reflection in the plane** $v^{\perp}\subset\operatorname{Im}\mathbb{H}$: it fixes every vector perpendicular to $v$, sends $v$ to $-v$, is $\mathbb{R}$-linear, preserves the norm form, is an involution, and has determinant $-1$ on $\operatorname{Im}\mathbb{H}$.

**Proof.** Since $v^{-1} = \bar{v} = -v$, we have $-vxv^{-1} = -vx(-v) = vxv$. For pure imaginary $v, x$ the product is $vx = v\times x - \langle v, x\rangle$, so $xv = -v\times x - \langle v,x\rangle$ and $vx + xv = -2\langle v,x\rangle$. Therefore

$$
vxv = (vx)v = -xv^2 - 2\langle v,x\rangle v = x - 2\langle v,x\rangle v,
$$

using $v^2 = -1$. The formula shows that $\rho_v$ is the identity on the hyperplane $\langle x,v\rangle = 0$ and equals $-v$ on $\mathbb{R}v$; linearity and norm preservation are immediate, and $\rho_v^2 = \mathrm{id}$ because the eigenvalues are $+1$ on the plane and $-1$ on the line, so the determinant is $-1$. $\square$

**Remark.** On the whole algebra $\mathbb{H}$, and not merely on $\operatorname{Im}\mathbb{H}$, the map $\rho_v$ is not the reflection in a hyperplane of $\mathbb{R}^4$: it also multiplies the scalar line by $-1$, so its fixed space is the two-dimensional plane $\operatorname{span}(e_0,v)^{\perp}$ and it acts as a rotation through $\pi$ in the plane $\operatorname{span}(e_0,v)$. The reflection statement above is the statement about the three-dimensional imaginary subspace, which is the space the rotation and reflection groups act on. This is the quaternionic instance of the twisted adjoint action $\widetilde{\operatorname{Ad}}_v(x) = \alpha(v)xv^{-1}$ of *The Clifford, Pin and Spin Groups*, in which the grade involution supplies the sign that distinguishes odd from even elements.

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

The product $v_1v_2$ is $v_1\times v_2 - \langle v_1,v_2\rangle$, whose vector part is $v_1\times v_2$; by the half-angle formula the rotation angle $\theta$ of $\operatorname{Ad}_{v_1v_2}$ satisfies $\cos\frac{\theta}{2} = -\langle v_1,v_2\rangle = -\cos\phi$, where $\phi$ is the angle between $v_1$ and $v_2$. Hence $\theta \equiv 2\phi \pmod{2\pi}$ in the appropriate orientation, and the axis is $v_1\times v_2$, the direction of the intersection of the two planes. $\square$

Conversely every rotation is a product of two reflections. By the half-angle formula the rotation through $\theta$ about $u$ is $\operatorname{Ad}_q$ with $q = \cos\frac{\theta}{2}+u\sin\frac{\theta}{2}$; if $a$ is a unit vector perpendicular to $u$ and $v_1 = a$, $v_2 = (u\times a)\sin\frac{\theta}{2} - a\cos\frac{\theta}{2}$, then $v_1$ and $v_2$ are unit vectors in the plane $u^{\perp}$ and $v_1v_2 = \sin\frac{\theta}{2}\,a(u\times a) + \cos\frac{\theta}{2} = u\sin\frac{\theta}{2} + \cos\frac{\theta}{2} = q$, using $a(u\times a) = a\times(u\times a) = u$.

### Cartan–Dieudonné in Three Dimensions

**Theorem (Cartan–Dieudonné, dimension three).** Every element of $O(3)$ is a product of at most three reflections in planes through the origin. The orientation-preserving isometries are exactly the products of an even number of reflections, and the orientation-reversing isometries the products of an odd number.

**Proof.** This is the general Cartan–Dieudonné theorem of *Isometries and Orthogonal Transformations* specialised to a three-dimensional non-degenerate space: every isometry is a product of reflections in hyperplanes, and the number of factors can be reduced to at most the dimension, so at most three suffice. The parity is the determinant, which is $(-1)^{(\text{number of factors})}$ because each reflection has determinant $-1$. $\square$

In the quaternion algebra the two-factor products are $q = v_1v_2$, acting as the rotation $\operatorname{Ad}_q$, and conversely every unit quaternion is a product of two unit vectors: given $q = q_0+\mathbf{q}$ with $q_0^2+|\mathbf q|^2 = 1$, choose a unit vector $a\perp\mathbf q$ and put $b = \mathbf q\times a - q_0a$, so that $ab = a\times b - \langle a,b\rangle = \mathbf q + q_0 = q$. Hence the even products of unit vectors are exactly the elements of $Sp(1)$, and the odd products are the elements of $\mathrm{Pin}(3)$ outside its even part, whose twisted adjoints are the orientation-reversing isometries.

### The Pin Group

**Theorem (Pin and Spin).** Let $\mathrm{Pin}(3)$ be the subgroup of the units of the Clifford algebra $\mathrm{Cl}_{3,0}$ generated by the unit vectors, and let $\mathrm{Spin}(3) = \mathrm{Pin}(3)\cap \mathrm{Cl}^0_{3,0}$ be its even part. The twisted adjoint action defines a surjective homomorphism

$$
\mathrm{Pin}(3)\longrightarrow O(3)
$$

with kernel $\{\pm1\}$, whose restriction to the even part is a surjective homomorphism $\mathrm{Spin}(3)\to SO(3)$ with kernel $\{\pm1\}$. The even Clifford algebra is $\mathrm{Cl}^0_{3,0}\cong\mathbb{H}$, and $\mathrm{Spin}(3)\cong Sp(1)$.

**Proof.** The general construction and the isomorphism $\mathrm{Cl}_{3,0}\cong\mathbb{H}\oplus\mathbb{H}$, whose even part $\mathrm{Cl}^0_{3,0}$ is a copy of $\mathbb{H}$, are those of *The Clifford, Pin and Spin Groups*; the twisted adjoint of a unit vector is the reflection $\rho_v$, and the twisted adjoint of an even unit is the conjugation $\operatorname{Ad}_q$. Surjectivity follows from Cartan–Dieudonné above, and the kernel $\{\pm1\}$ is computed as in the case of $Sp(1)$. $\square$

**Corollary.** There is a short exact sequence

$$
1 \longrightarrow \{\pm1\} \longrightarrow \mathrm{Pin}(3) \longrightarrow O(3) \longrightarrow 1,
$$

and an element of $O(3)$ is orientation-preserving exactly when it is a product of an even number of reflections. In particular $O(3)\cong SO(3)\rtimes \mathbb{Z}/2\mathbb{Z}$, the quotient by $SO(3)$ being the determinant.

## The Two-Sided Action and SO(4)

The adjoint action uses one unit quaternion. Using one on each side gives the full four-dimensional rotation group.

**Definition.** For $(q_1, q_2)\in Sp(1)\times Sp(1)$ define

$$
\Phi_{(q_1,q_2)} : \mathbb{H}\longrightarrow\mathbb{H}, \qquad \Phi_{(q_1,q_2)}(x) = q_1\,x\,q_2^{-1} = q_1x\bar{q}_2 .
$$

**Theorem.** Each $\Phi_{(q_1,q_2)}$ is an $\mathbb{R}$-linear isometry of $\mathbb{H}\cong\mathbb{R}^4$ with determinant $+1$, and

$$
\Phi : Sp(1)\times Sp(1)\longrightarrow SO(4), \qquad (q_1,q_2)\mapsto\Phi_{(q_1,q_2)},
$$

is a surjective homomorphism with kernel $\{\pm(1,1)\}$. Hence

$$
SO(4) \cong (Sp(1)\times Sp(1))/\{\pm(1,1)\} \cong \mathrm{Spin}(4).
$$

**Proof.** Linearity is clear. Norm preservation: $N(q_1xq_2^{-1}) = N(q_1)N(x)N(q_2)^{-1} = N(x)$. Homomorphism: $\Phi_{(q_1,q_2)}\circ\Phi_{(r_1,r_2)} = \Phi_{(q_1r_1, q_2r_2)}$. Determinant: $\det\Phi_{(q_1,q_2)} = \pm1$ and depends continuously on $(q_1,q_2)$, which ranges over the connected set $Sp(1)\times Sp(1)$, so it is constant and equals its value $\det(\mathrm{id}) = 1$ at $(1,1)$. Kernel: if $\Phi_{(q_1,q_2)} = \mathrm{id}$ then evaluating at $x = 1$ gives $q_1q_2^{-1} = 1$, so $q_1 = q_2 = q$, and then $qxq^{-1} = x$ for all $x$, so $q\in\{\pm1\}$. Surjectivity: the differential of $\Phi$ at the identity is the linear map $(x,y)\mapsto\bigl(z\mapsto xz - zy\bigr)$ from $\operatorname{Im}\mathbb{H}\oplus\operatorname{Im}\mathbb{H}$ to $\mathfrak{so}(4)$; it is injective, because $xz = zy$ for all $z$ gives $x = y$ on taking $z = 1$ and then forces $x$ to be central, hence $x = y = 0$; since both spaces have dimension $6$, it is an isomorphism. Hence $\Phi$ is a local diffeomorphism, its image is open, and, being a compact subgroup, it is also closed in the connected group $SO(4)$, so the image is everything. $\square$

The kernel has order two, so $SO(4)$ is doubly covered by $Sp(1)\times Sp(1)$, which is simply connected as $S^3\times S^3$; this is the Spin group $\mathrm{Spin}(4)$ of the four-dimensional Euclidean space. Whereas $SO(3)$ is simple and its universal cover is the simple group $Sp(1)$, the group $SO(4)$ is not simple, and the two factors of the cover are the left and the right multiplications. The adjoint action of the diagonal subgroup $q_1 = q_2 = q$ is $\operatorname{Ad}_q$ on $\operatorname{Im}\mathbb{H}$ together with the identity on the scalar line, and it is the copy of $SO(3)$ found earlier.

## The $4\pi$ Periodicity and the Double Cover

The double covering of the rotation group has a quantitative consequence for the parametrisation of a rotation by an angle.

**Theorem (periodicity).** Let $u$ be a unit vector and let $q(\theta) = \exp\!\bigl(\frac{u\theta}{2}\bigr) = \cos\frac{\theta}{2} + u\sin\frac{\theta}{2}$. Then

$$
q(\theta+2\pi) = -q(\theta), \qquad q(\theta+4\pi) = q(\theta),
$$

and $\operatorname{Ad}_{q(\theta+2\pi)} = \operatorname{Ad}_{q(\theta)}$. Consequently the map $\theta\mapsto\operatorname{Ad}_{q(\theta)}$ describing the rotation has period $2\pi$, while its quaternion lift $q$ has period $4\pi$.

**Proof.** Since $\exp(\frac{u(\theta+2\pi)}{2}) = \exp(\frac{u\theta}{2})\exp(\pi u) = -q(\theta)$ and $\exp(2\pi u) = 1$. The adjoint action is unchanged by $q\mapsto -q$ because the kernel is $\{\pm1\}$. $\square$

**Theorem.** The path $t\mapsto\exp(ut)$, $t\in[0,\pi]$, is a path in $Sp(1)$ from $1$ to $-1$; its image under the covering $Sp(1)\to SO(3)$ is a closed loop in $SO(3)$ that is not homotopic to the constant loop. Hence a rotation through the angle $2\pi$ corresponds to the non-identity element $-1$ of the fibre, and the identity quaternion is recovered only after the angle $4\pi$.

**Proof.** The path from $1$ to $-1$ does not close in $Sp(1)$, but its image does close in $SO(3)$ because $\operatorname{Ad}_{-1} = \operatorname{Ad}_1$. Since the covering is two-to-one with fibre $\{\pm1\}$, a loop in $SO(3)$ is null-homotopic if and only if its lift in $Sp(1)$ closes; here the lift does not close, so the loop is not null-homotopic, and it represents the generator of $\pi_1(SO(3))\cong\mathbb{Z}/2\mathbb{Z}$. Doubling the loop lifts to the path $t\mapsto\exp(ut)$, $t\in[0,2\pi]$, which closes at $\exp(2\pi u) = 1$. $\square$

This is the failure of the period $2\pi$: the rotation through $2\pi$ about $u$ is the identity of $SO(3)$, but the quaternion that represents it is $-1$, not $1$. The parametrisation returns to its initial value only after $4\pi$. The non-triviality of the covering is therefore not a convention but the statement $\pi_1(SO(3))\cong\mathbb{Z}/2\mathbb{Z}$, and it is the same statement as the existence of closed loops in $SO(3)$ that are not null-homotopic.

## Summary

The unit quaternions $Sp(1) = \{q : |q| = 1\} = S^3$ form a compact connected simply connected Lie group, non-abelian with centre $\{\pm1\}$, isomorphic to $SU(2)$ through the matrices $-i\sigma_k$, and every unit quaternion is $\cos\theta + u\sin\theta = \exp(u\theta)$ for an angle $\theta$ and a unit axis $u$.

Conjugation by a unit, $\operatorname{Ad}_q(x) = qxq^{-1}$, is an algebra automorphism that preserves the norm form and stabilises the imaginary subspace $\operatorname{Im}\mathbb{H}\cong\mathbb{R}^3$, where it acts as an isometry of determinant $+1$. The assignment $q\mapsto\operatorname{Ad}_q$ is a surjective homomorphism $Sp(1)\to SO(3)$ with kernel $\{\pm1\}$, so $SO(3)\cong Sp(1)/\{\pm1\}$ and the map is a two-sheeted covering, indeed the universal cover, giving $\pi_1(SO(3))\cong\mathbb{Z}/2\mathbb{Z}$.

The rotation about the unit axis $u$ through the angle $\theta$ is $\operatorname{Ad}_q$ with $q = \cos\frac{\theta}{2} + u\sin\frac{\theta}{2}$, the half-angle formula; composition of rotations is quaternion multiplication, $\operatorname{Ad}_{q_1}\circ\operatorname{Ad}_{q_2} = \operatorname{Ad}_{q_1q_2}$; and the parametrisation has period $4\pi$, since a rotation through $2\pi$ is represented by $-1$.

The reflection in the plane $v^{\perp}$ with unit normal $v$ is $\rho_v(x) = -vxv^{-1} = x - 2\langle x,v\rangle v$, an orientation-reversing involution; the product of two reflections is the rotation $\operatorname{Ad}_{v_1v_2}$ about the intersection line, and by Cartan–Dieudonné every isometry of $\mathbb{R}^3$ is a product of at most three reflections. The reflections and rotations together are the image of the Pin group $\mathrm{Pin}(3)$, whose even part is $\mathrm{Spin}(3)\cong Sp(1)$, and $O(3)\cong SO(3)\rtimes\mathbb{Z}/2\mathbb{Z}$.

Finally, the two-sided action $\Phi_{(q_1,q_2)}(x) = q_1xq_2^{-1}$ is a surjective homomorphism $Sp(1)\times Sp(1)\to SO(4)$ with kernel $\{\pm(1,1)\}$, so $SO(4)\cong \mathrm{Spin}(4)\cong (Sp(1)\times Sp(1))/\{\pm1\}$; the diagonal copy of $Sp(1)$ in it is the adjoint action that gives the rotations of the three-dimensional imaginary subspace.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $q = q_0 + \mathbf{q} = \sum_\mu q_\mu e_\mu$ | General quaternion, scalar part $q_0$, vector part $\mathbf{q}$ |
| $\bar{q} = q_0 - \mathbf{q}$ | Quaternion conjugate |
| $N(q) = q\bar{q} = \lvert q\rvert^2$ | Norm form and modulus |
| $\operatorname{Im}\mathbb{H}\cong\mathbb{R}^3$ | Imaginary quaternions, the space of vectors |
| $\langle x, y\rangle = \operatorname{Sc}(x\bar{y})$ | Real inner product on $\operatorname{Im}\mathbb{H}$ |
| $Sp(1) = \{q : \lvert q\rvert = 1\} = S^3$ | Group of unit quaternions |
| $Z(Sp(1)) = \{\pm1\}$ | Centre of $Sp(1)$ |
| $\exp(u\theta) = \cos\theta + u\sin\theta$ | Exponential of a unit vector |
| $\iota(e_k) = -i\sigma_k$ | Identification $Sp(1)\cong SU(2)$ |
| $\operatorname{Ad}_q(x) = qxq^{-1}$ | Adjoint action |
| $R_q$ | Matrix of $\operatorname{Ad}_q$ on $\operatorname{Im}\mathbb{H}$ |
| $\operatorname{ad}_x(y) = [x,y] = 2(x\times y)$ | Adjoint map of the Lie algebra $\operatorname{Im}\mathbb{H}$ |
| $\operatorname{Im}\mathbb{H}\cong\mathfrak{so}(3)\cong\mathfrak{su}(2)$ | Lie algebra of $Sp(1)\cong SU(2)$ and of $SO(3)$ |
| $SO(3)$ | Rotation group of $\mathbb{R}^3$, $\cong Sp(1)/\{\pm1\}$ |
| $O(3)\cong SO(3)\rtimes\mathbb{Z}/2\mathbb{Z}$ | Orthogonal group of $\mathbb{R}^3$ |
| $\rho_v(x) = -vxv^{-1}$ | Reflection in the plane $v^{\perp}$, $v$ a unit vector |
| $\mathrm{Pin}(3)$ | Pin group, generated by the unit vectors |
| $\mathrm{Spin}(3) = \mathrm{Pin}(3)\cap\mathrm{Cl}^0_{3,0}\cong Sp(1)$ | Spin group; $\mathrm{Cl}_{3,0}$ is the Clifford algebra of the Euclidean form on $\mathbb{R}^3$ and $\mathrm{Cl}^0_{3,0}$ its even part |
| $\Phi_{(q_1,q_2)}(x) = q_1xq_2^{-1}$ | Two-sided action of $Sp(1)\times Sp(1)$ |
| $SO(4)\cong\mathrm{Spin}(4)\cong(Sp(1)\times Sp(1))/\{\pm1\}$ | Rotation group of $\mathbb{R}^4$ |
| $\pi_1(SO(3))\cong\mathbb{Z}/2\mathbb{Z}$ | Fundamental group of the rotation group |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, 1853), for the origin of the quaternion representation of rotations.
- Felix Klein, *Vorlesungen über das Ikosaeder und die Auflösung der Gleichungen vom fünften Grade* (Teubner, 1884), for the rotation-group viewpoint on the unit quaternions.
- Simon L. Altmann, *Rotations, Quaternions and Double Groups* (Oxford University Press, 1986), for the double cover, the half-angle formula and the topology of the rotation group.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the reflections, the Pin and Spin groups and the quaternion parametrisation.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the Lie group $SU(2)$, its relation to $SO(3)$ and the covering-space argument.
- Alexander Kirillov Jr., *An Introduction to Lie Groups and Lie Algebras* (Cambridge University Press, 2008), for the exponential map, the adjoint representation and the structure of $SO(3)$ and $SO(4)$.
- Emil Artin, *Geometric Algebra* (Interscience, 1957), for the Cartan–Dieudonné theorem and the structure of the orthogonal group.
