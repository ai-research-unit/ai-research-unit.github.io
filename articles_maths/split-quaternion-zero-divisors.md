
# __Split-Quaternion Zero Divisors__

## Introduction

This article studies the zero divisors of the split-quaternion algebra. It defines them, proves the criterion that identifies them with the null cone of the determinant form, describes them as the rank-one matrices of the matrix model, exhibits the two families into which the null cone splits, proves the existence of nonzero nilpotents, and describes the distribution of the zero divisors among the distinguished subspaces.

The split-quaternion algebra, its matrix model $\Phi$, its norm form $N$, its idempotents $u_\pm$ and its subspaces $S$, $V$, $\mathbb{D}_2$, $\mathbb{D}_3$ are assumed from *Split-Quaternion Algebra*. The invertibility criterion and the identification of the norm form with the determinant are assumed from *Split-Quaternion Norm and Invertibility*, §*The Invertibility Criterion* and §*The Norm Form and the Determinant Form*; the criterion is not re-proved here. The rank and the kernel of a $2 \times 2$ matrix are assumed from *Matrix Algebras*. Nothing physical is invoked.

## Definition and Criterion

**Definition.** A nonzero element $x \in \mathbb{H}_{\mathrm{s}}$ is a **zero divisor** if there exists a nonzero $y \in \mathbb{H}_{\mathrm{s}}$ with $xy = 0$ or a nonzero $z \in \mathbb{H}_{\mathrm{s}}$ with $zx = 0$. The **zero divisor set** is

$$
Z = \{x \in \mathbb{H}_{\mathrm{s}} : x \neq 0 \text{ and } x \text{ is a zero divisor}\}.
$$

**Theorem (The Criterion).** Let $x$ be nonzero. Then $x$ is a zero divisor if and only if $N(x) = 0$. Equivalently, the zero divisor set is the null cone of the determinant form with the origin removed:

$$
Z = \{x \neq 0 : N(x) = 0\} = \{x \neq 0 : \det \Phi(x) = 0\}.
$$

**Proof.** The criterion is the corollary of the invertibility criterion proved in *Split-Quaternion Norm and Invertibility*, §*The Invertibility Criterion*: a nonzero element is a zero divisor exactly when it is not invertible, and it is invertible exactly when $N(x) \neq 0$. The second form is the identity $N(x) = \det \Phi(x)$ proved in the same article, §*The Norm Form and the Determinant Form*. $\square$

The set

$$
\mathcal{N} = \{x : N(x) = 0\} = Z \cup \{0\}
$$

is the **null cone** of $N$. It is a cone: if $N(x) = 0$ then $N(\lambda x) = \lambda^2 N(x) = 0$ for every real $\lambda$. It is closed, it has real dimension $3$, and its only singular point is the origin; away from the origin it is a smooth three-dimensional cone. The complement of $Z$ in $\mathbb{H}_{\mathrm{s}} \setminus \{0\}$ is the set of units, an open dense set of full measure by *Split-Quaternion Norm and Invertibility*, §*Distribution of the Invertible Elements*.

The zero divisor set is **connected**. Indeed, every isotropic vector $x$ is a positive multiple of a vector $(\cos\alpha, \sin\alpha, \cos\beta, \sin\beta)$ by *Split-Quaternion Norm and Invertibility*, §*Isotropy*, and the parametrisation is continuous in the pair of angles; the set of isotropic vectors is therefore homeomorphic to a cone on a connected base, and removing the vertex leaves it connected.

## The Zero Divisor Set as the Null Cone

The null cone has a concrete description in the matrix model.

**Theorem (The Zero Divisors Are the Rank-One Matrices).** Let $x$ be nonzero. Then $x$ is a zero divisor if and only if $\Phi(x)$ is a **rank-one** matrix. Consequently

$$
\Phi(Z) = \{M \in M_2(\mathbb{R}) : M \neq 0, \ \operatorname{rank} M = 1\},
$$

and every nonzero singular $2 \times 2$ matrix is the image of a zero divisor.

**Proof.** The matrix $\Phi(x)$ is singular exactly when $\det \Phi(x) = N(x) = 0$. For a nonzero $2 \times 2$ matrix, singularity means rank one, since the rank can only be $0$ or $1$; rank $0$ is excluded because $x \neq 0$ and $\Phi$ is injective. Thus $\Phi(Z)$ is exactly the set of nonzero singular matrices, which is the set of rank-one matrices. $\square$

**Corollary (The Rank-One Description).** Every zero divisor has the form

$$
x = \Phi^{-1}(u v^{\top}), \qquad u, v \in \mathbb{R}^2 \setminus \{0\},
$$

and the pair $(u,v)$ is determined by $x$ up to the replacement $(u,v) \mapsto (\lambda u, \lambda^{-1} v)$ for $\lambda \in \mathbb{R}^{\times}$. The line $\mathbb{R}u$ is the **image line** of $x$ and the line $\mathbb{R}v$ is the **kernel line**; together they characterise $x$ up to a nonzero scalar.

**Proof.** A rank-one matrix is $uv^{\top}$ for nonzero column vectors $u$ and $v$, and two such representations give the same matrix exactly when the pairs differ by the stated replacement. The image of $uv^{\top}$ is $\mathbb{R}u$, and its kernel is $\{v\}^{\perp} = \mathbb{R} v^{\perp}$ where $v^{\perp} = (-v_2, v_1)$; the statement follows. $\square$

**Corollary (The Isotropic Lines).** Every isotropic line $\mathbb{R}x$ is a line of rank-one matrices, and the isotropic lines are precisely the projective null quadric

$$
Q = \{[x] \in \mathbb{P}^3 : N(x) = 0\}.
$$

The line of $x$ determines, and is determined by, the pair consisting of the image line and the kernel line of $\Phi(x)$.

**Proof.** Immediate from the criterion and the rank-one description: an isotropic line consists of scalar multiples of one zero divisor, and a zero divisor is a rank-one matrix. $\square$

## The Two Families

A rank-one matrix carries two one-dimensional data, its image line and its kernel line, and the maximal totally isotropic subspaces organise these data into two families.

### The Two Families of Maximal Isotropic Subspaces

**Definition.** For a line $\ell \subset \mathbb{R}^2$, define

$$
R_\ell = \{M \in M_2(\mathbb{R}) : \operatorname{im} M \subseteq \ell\}, \qquad
K_\ell = \{M \in M_2(\mathbb{R}) : \ker M \supseteq \ell\}.
$$

Both are real linear subspaces of $M_2(\mathbb{R})$, and both are **totally isotropic** for the determinant form and **maximal** with that property.

**Theorem (The Two Families).** For every line $\ell$, the subspaces $R_\ell$ and $K_\ell$ are two-dimensional, they satisfy $\det M = 0$ for every $M$ in them, and they are maximal totally isotropic. Every maximal totally isotropic subspace of $M_2(\mathbb{R})$ is one of the $R_\ell$ or one of the $K_\ell$. The two collections

$$
\mathcal{R} = \{R_\ell : \ell \in \mathbb{P}^1\}, \qquad \mathcal{K} = \{K_\ell : \ell \in \mathbb{P}^1\}
$$

are the **two families** of the null cone; each is parametrised by the projective line $\mathbb{P}^1$, and the two families are disjoint.

**Proof.** *Dimension.* The condition $\operatorname{im} M \subseteq \ell$ restricts the two columns of $M$ to a one-dimensional space, leaving two real parameters, so $\dim R_\ell = 2$; dually, the condition $\ker M \supseteq \ell$ restricts the two rows of $M$ to the annihilator of $\ell$, again leaving two parameters, so $\dim K_\ell = 2$. *Isotropy.* If $\operatorname{im} M \subseteq \ell$ then the columns of $M$ are linearly dependent, so $\operatorname{rank} M \leq 1$ and $\det M = 0$; if $\ker M \supseteq \ell$ then $M$ has a nonzero kernel, so $M$ is singular, so $\det M = 0$. *Maximality.* The form has signature $(2,2)$, so a totally isotropic subspace has dimension at most $2$, by the inertia law of *Quadratic Forms and Polarisation*; since $R_\ell$ and $K_\ell$ have dimension $2$ and are isotropic, they are maximal. *Classification.* Let $P$ be a two-dimensional totally isotropic subspace. Then $P$ contains a nonzero matrix, and every nonzero matrix of $P$ is singular because $P$ is isotropic, hence of rank one; so $P = \operatorname{span}\{M, N\}$ with $M = uv^{\top}$ and $N = xy^{\top}$ for nonzero column vectors $u, v, x, y$. The condition that every element of $P$ be singular is the single condition $B(M,N) = 0$, since $\det(M + tN)$ is a quadratic polynomial in $t$ whose vanishing for all $t$ forces the vanishing of its three coefficients, which are $\det M$, $B(M,N)$ and $\det N$. Now $M + N = [\,u \ x\,]\,[\,v \ y\,]^{\top}$ in block form, so by the multiplicativity of the determinant

$$
B(M,N) = \det(M+N) = \det(u, x) \cdot \det(v, y),
$$

where $\det(u,x) = u_1 x_2 - u_2 x_1$. Hence $x$ is proportional to $u$, or $y$ is proportional to $v$. In the first case $N$ and $M$ both have image contained in the line $\mathbb{R}u$, so $P \subseteq R_{\mathbb{R}u}$, and the two dimensions force $P = R_{\mathbb{R}u}$. In the second case $N$ and $M$ both have kernel containing the line $\mathbb{R}v^{\perp}$, so $P \subseteq K_{\mathbb{R}v^{\perp}}$, and again $P = K_{\mathbb{R}v^{\perp}}$. The two cases cannot occur together, since their conjunction would place $P$ in the one-dimensional space $R_{\mathbb{R}u} \cap K_{\mathbb{R}v^{\perp}} = \operatorname{span}\{uv^{\top}\}$. *Disjointness.* Were $R_\ell = K_{\ell'}$, the space $R_\ell \cap K_{\ell'}$ would be two-dimensional; but $R_\ell \cap K_{\ell'}$ consists of the matrices $uv^{\top}$ with $\mathbb{R}u = \ell$ and $\mathbb{R}v^{\perp} = \ell'$, a one-dimensional space. Hence the two families are disjoint. $\square$

**Corollary (Each Zero Divisor Lies in One Plane of Each Family).** Let $x$ be a zero divisor with image line $\ell_1$ and kernel line $\ell_2$ under $\Phi$. Then

$$
\Phi(x) \in R_{\ell_1} \cap K_{\ell_2},
$$

and $R_{\ell_1}$ is the unique member of $\mathcal{R}$ containing $\Phi(x)$, while $K_{\ell_2}$ is the unique member of $\mathcal{K}$ containing it. Hence the null cone is the union of the planes of the two families, and through every isotropic line pass exactly two maximal isotropic planes, one from each family.

**Proof.** The image of $\Phi(x)$ is $\ell_1$, so $\Phi(x) \in R_{\ell_1}$; if also $\Phi(x) \in R_{\ell'}$ then $\operatorname{im}\Phi(x) \subseteq \ell \cap \ell'$, which is zero for $\ell \neq \ell'$ and would force $\Phi(x) = 0$; hence $\ell_1 = \ell'$ and the member is unique. The kernel statement is dual. Every zero divisor is a rank-one matrix and therefore belongs to the two displayed planes. $\square$

**Corollary (Transposition Swaps the Families).** The transpose $M \mapsto M^{\top}$ is an anti-automorphism of $M_2(\mathbb{R})$ and satisfies

$$
R_\ell^{\top} = K_{\ell^{\perp}} \qquad (\ell \in \mathbb{P}^1),
$$

where $\ell^{\perp}$ is the orthogonal line with respect to the standard inner product of $\mathbb{R}^2$. In the algebra, the corresponding anti-automorphism $\tau = \Phi^{-1} \circ (\cdot)^{\top} \circ \Phi$ satisfies $\tau(e_1) = -e_1$, $\tau(e_2) = e_2$, $\tau(e_3) = e_3$, and it exchanges the two families.

**Proof.** $\operatorname{im} M \subseteq \ell$ is equivalent to $\operatorname{im} M \perp \ell^{\perp}$, which is equivalent to $\ell^{\perp} \subseteq \ker M^{\top}$. This gives the identity of the subspaces, and it exhibits the exchange of families. The action of $\tau$ on the generators is read from the matrices $\Phi(e_k)$ of (*Split-Quaternion Algebra*, §*The Matrix Model*): the transpose of the rotation matrix $\Phi(e_1) = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$ is its negative, while $\Phi(e_2)$ and $\Phi(e_3)$ are symmetric. $\square$

### The Two Families in the Algebra

Transporting the two families back through $\Phi$ gives a statement about the algebra itself.

**Definition.** For a line $\ell \subset \mathbb{R}^2$, put

$$
\mathcal{R}_\ell = \Phi^{-1}(R_\ell), \qquad \mathcal{K}_\ell = \Phi^{-1}(K_\ell).
$$

These are the two families of **maximal isotropic subspaces of the algebra**: each is a two-dimensional real subspace of $\mathbb{H}_{\mathrm{s}}$ on which $N$ vanishes identically.

**Proposition (The Minimal Ideals Are Members of the Families).** Let $\ell_v$ be the line spanned by $v = (1,1)$ and $\ell_w$ the line spanned by $w = (1,-1)$. Then

$$
u_+ \mathbb{H}_{\mathrm{s}} = \mathcal{R}_{\ell_v}, \qquad \mathbb{H}_{\mathrm{s}} u_+ = \mathcal{K}_{\ell_w}, \qquad
u_- \mathbb{H}_{\mathrm{s}} = \mathcal{R}_{\ell_w}, \qquad \mathbb{H}_{\mathrm{s}} u_- = \mathcal{K}_{\ell_v}.
$$

Thus the four minimal ideals of the algebra are the four distinguished members of the two families, and the total isotropy of the minimal ideals proved in *Split-Quaternion Norm and Invertibility*, §*The Minimal Left and Right Ideals* is the statement that they are members of the families.

**Proof.** In the matrix model, $u_+ \mapsto \tfrac12(I + K) = \tfrac12 vv^{\top}$ with $v = (1,1)$, and $u_- \mapsto \tfrac12(I - K) = \tfrac12 ww^{\top}$ with $w = (1,-1)$. A product $u_+ M \propto v v^{\top} M$ has image contained in $\mathbb{R}v$, so $u_+ M_2(\mathbb{R}) = R_{\ell_v}$; a product $M u_+ \propto M v v^{\top}$ is annihilated on the right by every vector orthogonal to $v$, so its kernel contains $\ell_w$, and $\mathbb{H}_{\mathrm{s}} u_+ = K_{\ell_w}$. The other two identities are identical with $v$ and $w$ exchanged. $\square$

## Nonzero Nilpotents

**Definition.** A nonzero element $x$ is **nilpotent** if $x^2 = 0$.

**Theorem (The Nilpotents).** A nonzero element $x$ is nilpotent if and only if

$$
x \in V \quad \text{and} \quad N(x) = 0,
$$

that is, if and only if $x$ is a nonzero vector of the vector subspace lying on the light cone $b^2 = c^2 + d^2$. The set of nilpotents is therefore a two-dimensional cone, and in particular

$$
(e_1 + e_3)^2 = e_1^2 + e_1 e_3 + e_3 e_1 + e_3^2 = -1 + 0 + 1 = 0 .
$$

Every nilpotent is a zero divisor, and the nilpotents form a proper subset of the zero divisor set.

**Proof.** Write $x = a + u$ with $a \in S$ and $u \in V$. Since $e_1, e_2, e_3$ are traceless and the product of two distinct generators is the third with a sign, the square is

$$
x^2 = a^2 + 2au + u^2 = a^2 + 2au - N(u),
$$

where $u^2 = -N(u)$ is the identity for pure vectors recorded in (*Split-Quaternion Algebra*, §*The Restricted Form on the Vector Subspace*). If $x^2 = 0$, then comparing the components in $S$ and in $V$ gives $2au = 0$, so $a = 0$ or $u = 0$. If $u = 0$ then $a^2 = 0$, so $a = 0$ and $x = 0$, excluded by hypothesis; hence $a = 0$ and $x = u \in V$. Then $x^2 = -N(x)$, so $x^2 = 0$ exactly when $N(x) = 0$. Conversely every such $x$ has $x^2 = 0$. The computation for $e_1 + e_3$ uses $e_1 e_3 = -e_3 e_1$ and $e_1^2 = -1$, $e_3^2 = +1$. Every nilpotent satisfies $N(x)^2 = N(x^2) = 0$, hence $N(x) = 0$, so it is a zero divisor; the element $1 + e_2$ is a zero divisor with $N(1+e_2) = 0$ but $(1+e_2)^2 = 2(1+e_2) \neq 0$, so the inclusion is proper. $\square$

The nilpotent set is the light cone of the signature-$(2,1)$ form of $V$; by *Split-Quaternion Norm and Invertibility*, §*Isotropy*, its lines are the circle $\mathbb{R}(e_1 + \cos\theta\, e_2 + \sin\theta\, e_3)$.

### The Contrast with the Division Algebras

The existence of nilpotents is the sharpest structural contrast the category has.

**Theorem (No Nilpotents in the Division Algebras).** The quaternion algebra $\mathbb{H}$ has no nonzero nilpotent, and the eight-dimensional $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ has no nonzero nilpotent.

**Proof.** The quaternion algebra is a division algebra by *Quaternion Algebra*, so $x \neq 0$ implies $x$ invertible, and $x^2 = 0$ would give $x = 0$ after multiplying by $x^{-1}$. The eight-dimensional algebra is a product of two copies of $\mathbb{H}$ by the dictionary of *The Number Systems as Clifford Algebras*, and a nilpotent in a product of algebras would have a nilpotent component in one of the factors; a division algebra has none, so the product has none. $\square$

**Remark.** The comparison isolates the phenomenon. A **simple** real algebra with nilpotents, such as $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$, and a **semisimple, non-simple** product of division algebras without nilpotents, such as $\mathbb{H}_{\mathbb{D}}$, lie on opposite sides of the line that the nilpotent draws. The eight-dimensional algebra is treated later in Part V, under Split-Biquaternions; nothing of it is used here beyond the identification already stated in *The Number Systems as Clifford Algebras*.

## Distribution of the Zero Divisors

The zero divisors are distributed over the distinguished subspaces as follows. The subspaces are those of *Split-Quaternion Algebra*.

| Subspace | Zero divisors | Description |
|---|---|---|
| $S = \mathbb{R}\cdot 1$ | none | every nonzero scalar is a unit |
| $V$ | the nonzero vectors with $b^2 = c^2 + d^2$ | the light cone, a two-dimensional cone, every nonzero point of which is nilpotent |
| $\mathbb{D}_2 = \operatorname{span}\{1,e_2\}$ | the nonzero multiples of $1 \pm e_2$ | two isotropic lines |
| $\mathbb{D}_3 = \operatorname{span}\{1,e_3\}$ | the nonzero multiples of $1 \pm e_3$ | two isotropic lines |
| $\mathbb{H}_{\mathrm{s}} u_\pm$, $u_\pm \mathbb{H}_{\mathrm{s}}$ | the whole subspace minus the origin | four maximal isotropic planes |
| $u_\pm$ themselves | $u_+$ and $u_-$ | the two non-central idempotents |

The table is completed by the following observations.

**The vector subspace.** On $V$ the zero divisors are exactly the lightlike vectors, and by *Nonzero Nilpotents* they are exactly the nonzero nilpotents. Every zero divisor of $V$ has square zero; this is peculiar to the traceless part and does not hold in the whole algebra.

**The idempotents.** The idempotents $u_\pm = \tfrac12(1 \pm e_2)$ are zero divisors with $u_+ u_- = 0$; they are not nilpotent, since $u_\pm^2 = u_\pm \neq 0$. Together with $0$ and $1$ they are two of the idempotents of the algebra: the general non-scalar idempotent is $\tfrac12(1 \pm \eta)$ for a root $\eta$ of $+1$ in the vector subspace, a one-sheeted hyperboloid's worth of idempotents, as recorded in *Split-Quaternion Roots of Minus One*.

**The splitting.** The zero divisor set is connected, and it is the union of the planes of the two families of *The Two Families*. The nilpotent set is the two-dimensional subcone of $V$, and the non-scalar idempotents form a one-sheeted hyperboloid of points of the zero divisor set lying outside that subcone.

**Measure.** The zero divisor set is closed and has Lebesgue measure zero in $\mathbb{R}^4$, since it is the zero set of a nonconstant polynomial; the units are its open dense complement.

## Summary

A nonzero split-quaternion is a zero divisor exactly when $N(x) = 0$, and the zero divisor set is the null cone of the determinant form with the origin removed. Under the matrix model it is the set of rank-one $2 \times 2$ real matrices, and a zero divisor is described by its image line and its kernel line.

The null cone splits into the two families of maximal totally isotropic subspaces, $\mathcal{R}_\ell$ and $\mathcal{K}_\ell$, indexed by the lines $\ell$ of $\mathbb{R}^2$; each is two-dimensional, each consists of singular matrices, and they are the two rulings of the projective null quadric. Every zero divisor lies in exactly one member of each family, the two families are exchanged by transposition, and the four minimal ideals of the algebra are members of the families: $u_+ \mathbb{H}_{\mathrm{s}} = \mathcal{K}_{\ell_w}$, $\mathbb{H}_{\mathrm{s}} u_+ = \mathcal{R}_{\ell_v}$, and their analogues.

The algebra has nonzero nilpotents: a nonzero element is nilpotent exactly when it lies in the vector subspace and on its light cone, and $(e_1 + e_3)^2 = 0$. The quaternion algebra and the eight-dimensional $\mathbb{H}_{\mathbb{D}}$ have no nonzero nilpotent, the first because it is a division algebra and the second because it is a product of division algebras. The zero divisor set is a connected three-dimensional cone of measure zero, the nilpotents form its two-dimensional subcone inside $V$, and the two non-central idempotents are two further points of it.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $Z$ | the zero divisor set $\{x \neq 0 : N(x) = 0\}$ | this article |
| $\mathcal{N}$ | the null cone $\{x : N(x) = 0\}$ | this article |
| $\Phi(Z)$ | the rank-one matrices of $M_2(\mathbb{R})$ | this article |
| image line, kernel line | the two lines attached to a rank-one matrix | this article |
| $\mathbb{R}x$, $[x]$ | an isotropic line of the projective null quadric $Q$ | this article |
| $R_\ell$, $K_\ell$ | $\{M : \operatorname{im} M \subseteq \ell\}$, $\{M : \ker M \supseteq \ell\}$ | this article |
| $\mathcal{R}$, $\mathcal{K}$ | the two families of maximal isotropic subspaces | this article |
| $\mathcal{R}_\ell$, $\mathcal{K}_\ell$ | the same, transported to $\mathbb{H}_{\mathrm{s}}$ | this article |
| $\tau$ | the anti-automorphism $\Phi^{-1}\circ(\cdot)^{\top}\circ\Phi$ | this article |
| nilpotent | nonzero $x$ with $x^2 = 0$ | this article |
| $\ell_v, \ell_w$ | the lines $\mathbb{R}(1,1)$ and $\mathbb{R}(1,-1)$ | this article |
| $u_\pm = \tfrac12(1 \pm e_2)$ | the non-central idempotents | *Split-Quaternion Algebra* |
| $N(x) = \det \Phi(x)$ | the norm and determinant form | *Split-Quaternion Norm and Invertibility* |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the coquaternions, their idempotents and their nilpotents.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for maximal isotropic subspaces and the ruling of the null quadric.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic forms, the inertia law and the geometry of the null cone.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the split composition algebras and their zero divisors.
