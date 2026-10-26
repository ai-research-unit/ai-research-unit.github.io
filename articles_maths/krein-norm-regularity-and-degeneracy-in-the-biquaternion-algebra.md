# __K-Regularity and Degeneracy in the Biquaternion Algebra__

## Introduction

The biquaternion algebra carries four norms; the **Krein norm** is the indefinite one, the general quaternionic sesquilinear form read at its two equal arguments. It is real-valued, it is not multiplicative, and it does not decide invertibility. Its zero set is a real cone of codimension one on which units and zero divisors both occur, and its sign is not a ring-theoretic invariant.

This article defines the Krein norm, records its homogeneity, proves that it is not multiplicative, and separates the algebra into the two cases of its value: the **Krein-regular** case of non-zero value, split into the positive and the negative regions, and the **Krein-degenerate** case of zero value, the null set. The closure of the positive case is the Krein cone. It then compares the metric partition with the algebraic partition of the algebra into units, origin and zero divisors, which is the partition carried by the quaternionic norm, and explains why the Krein problem admits no second axis along the spectral condition: the Krein norm and the spectrum are invariants of different groups, and the plane that the quaternionic norm supports does not transfer. The two halves of the partition are treated in *The K-Regular Sector* and *The K-Degenerate Sector*.

**Notation.** An element is $\tilde Q=Q_t e_t+\vec Q$, with $Q_\mu=q_\mu+iq'_\mu$ complex and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The natural conjugation is $\tilde Q^{\natural}=Q_t-\vec Q$, the Hermitian conjugation is $\tilde Q^*=\bar Q_t-\overline{\vec Q}$, and the coefficient signs are $\varepsilon=(1,-1,-1,-1)$. The **definite companion** is $\langle\tilde Q_1,\tilde Q_2\rangle_*=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$, with $\langle\tilde Q\rangle_*=\lVert\tilde Q\rVert_E^2=\sum_\mu|Q_\mu|^2$. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of complex dimension four and real dimension eight. The product is the plain product $\tilde P\tilde Q$, associative and with the two-sided unit $e_t$. The **quaternionic norm** is $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$; it is complex-valued and multiplicative. Its regular and degenerate cases, the unit group and the zero-divisor cone, are the subject of *N-Regularity and N-Degeneracy in the Biquaternion Algebra*. The form itself, its Gram matrix and its inertia are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; its fundamental symmetry and the bridge are *The Fundamental Symmetry of the Form*; this article studies the norm the form carries, with the isotropic elements, the doubly null lines and the cone they close.

## The Krein Norm

The **Krein norm** is the general quaternionic sesquilinear form read at its two equal arguments,
$$
\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu|Q_\mu|^2
=|Q_t|^2-\lVert\vec Q\rVert_E^2 .
$$
It is real-valued and homogeneous of degree two, $\langle\lambda\tilde Q\rangle_{\natural*}=|\lambda|^2\langle\tilde Q\rangle_{\natural*}$ for complex $\lambda$. The form is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; this article studies the norm it carries.

**Theorem (non-multiplicativity).** The Krein norm is not multiplicative. With $\tilde P=e_t+\vec e_x$ and $\tilde Q=e_t-\vec e_x$,
$$
\langle\tilde P\rangle_{\natural*}=\langle\tilde Q\rangle_{\natural*}=0,
\qquad
\tilde P\tilde Q=2e_t,
\qquad
\langle\tilde P\tilde Q\rangle_{\natural*}=4.
$$
Moreover $\tilde P^2=2\vec e_x$ and $\langle\tilde P^2\rangle_{\natural*}=-4$.

*Proof.* $\tilde P\tilde Q=e_t^2-\vec e_x^2=2e_t$ and $\tilde P^2=e_t+2\vec e_x+\vec e_x^2=2\vec e_x$, since $\vec e_x^2=-e_t$. The values are $|1|^2-|1|^2=0$, $\langle 2e_t\rangle_{\natural*}=4$ and $\langle 2\vec e_x\rangle_{\natural*}=-4$.

**Consequence.** No multiplicative law survives in either direction: the product of two null elements can be regular, and the product of two regular elements can be null (§*The regular case: the positive and the negative regions*). What is preserved is the homogeneity under complex scalars and the invariance under the isometry group $\mathrm{U}_J(\mathbb{B})\cong\mathrm{U}(1,3)$; multiplication by an algebra element preserves neither the value nor its sign.

## The Two Cases

The value of the Krein norm separates the algebra into three sets.

| condition on $\langle\tilde Q\rangle_{\natural*}$ | set | name |
|---|---|---|
| $>0$ | $\mathbb{B}^{\natural*}_{+}=\{|Q_t|>\lVert\vec Q\rVert_E\}$ | the **positive-regular** region |
| $<0$ | $\mathbb{B}^{\natural*}_{-}=\{|Q_t|<\lVert\vec Q\rVert_E\}$ | the **negative-regular** region |
| $=0$ | $\mathcal K=\{|Q_t|=\lVert\vec Q\rVert_E\}$ | the **null set**, the **Krein-degenerate** case |

The **Krein-regular** set is the union
$$
\mathbb{B}^{\natural*}=\mathbb{B}^{\natural*}_{+}\uplus\mathbb{B}^{\natural*}_{-}
=\{\tilde Q:\langle\tilde Q\rangle_{\natural*}\neq0\},
$$
and the algebra is the disjoint union
$$
\mathbb{B}=\mathbb{B}^{\natural*}_{+}\uplus\mathcal K\uplus\mathbb{B}^{\natural*}_{-}.
$$
The split is by the value of the norm, not by invertibility. The origin lies in $\mathcal K$ and is neither a unit nor a zero divisor, and it is the only Krein-degenerate point with vanishing scalar part. Every other point of $\mathcal K$ is a unit or a zero divisor: it is a unit exactly when its algebraic norm does not vanish, and a zero divisor exactly when it does. So the degeneracy case is the origin together with units and zero divisors.

**Remark (the word regular).** In ring theory a regular element is a non-zero-divisor, so the ring-regular set is $\mathbb{B}^{\times}\uplus\{0\}$. The title uses **Krein-regular** in the metric sense: the regular side is the complement of the null set. The two readings are different, and §*The Two Partitions* shows that the only implication between them is positive implies unit.

## The regular case: the positive and the negative regions

**Definition.** The **Krein-regular set** is
$$
\mathbb{B}^{\natural*}=\{\tilde Q:\langle\tilde Q\rangle_{\natural*}\neq0\}
=\mathbb{B}^{\natural*}_{+}\uplus\mathbb{B}^{\natural*}_{-}.
$$
It is the complement of the null set, and it is the union of the two sign regions.

**Theorem (the regular set).** The set $\mathbb{B}^{\natural*}$ is open and dense in $\mathbb{B}$, and its complement is the null set $\mathcal K$. The null set is closed, of empty interior and of real codimension one, and it is the common boundary
$$
\partial\mathbb{B}^{\natural*}_{+}=\partial\mathbb{B}^{\natural*}_{-}=\mathcal K .
$$
The regular set has exactly two connected components, the positive and the negative regions.

*Proof.* The function $f(\tilde Q)=\langle\tilde Q\rangle_{\natural*}$ is a real polynomial, so its non-zero set is open and its zero set is closed. Off the origin the gradient of $f$ in the real coordinates $(\Re Q_t,\Im Q_t,\Re\vec Q,\Im\vec Q)$ is $2(\Re Q_t,\Im Q_t,-\Re\vec Q,-\Im\vec Q)\neq0$, so the null set is a real hypersurface of real dimension $7$, of empty interior and real codimension one. The sign is locally constant on the complement, and every point of $\mathcal K$ is a boundary point of both sign regions, because $f$ has no local extremum there: the origin is its only critical point, and near the origin $e_t$ and $\vec e_x$ give both signs. The positive region is homotopy equivalent to $S^1$ and the negative region to $S^5$ (*The Krein Level Sets and the Hyperbolic Structure*), so each is connected; the complement of the null set has at most two components, because the sign takes two values.

**Theorem (positive implies unit).** If $\langle\tilde Q\rangle_{\natural*}>0$, then $\tilde Q$ is a unit of the plain product.

*Proof.* Positivity gives $|Q_t|>\lVert\vec Q\rVert_E$, hence $Q_t\neq0$. If $\tilde Q$ were a zero divisor, then $\langle\tilde Q\rangle_{\natural}=0$ by the criterion of *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, so $Q_t^2=-\sum_kQ_k^2$ and
$$
|Q_t|^2=\Bigl|\sum_kQ_k^2\Bigr|\leq\sum_k|Q_k|^2=\lVert\vec Q\rVert_E^2,
$$
in contradiction with positivity. A non-zero element that is not a zero divisor is a unit.

**Theorem (not a group).** The Krein-regular set is not a group under the plain product and is not stable under it: the Krein-regular elements $\vec e_x$ and $\vec e_x+i\vec e_y$ have the null product $-e_t+i\vec e_z$, and the two null elements $e_t+\vec e_x$ and $e_t-\vec e_x$ have the Krein-regular product $2e_t$. It is stable under multiplication by non-zero complex scalars and under the Krein isometry group.

*Proof.* Closure under scalars and isometries is the homogeneity and the invariance of §*The Krein Norm*. The failure of closure under the product is the first example: $\vec e_x(\vec e_x+i\vec e_y)=\vec e_x^2+i\vec e_x\vec e_y=-e_t+i\vec e_z$, of Krein norm $1-1=0$, while $\langle\vec e_x\rangle_{\natural*}=-1$ and $\langle\vec e_x+i\vec e_y\rangle_{\natural*}=-2$. The second example shows that the Krein-degenerate set is not stable either.

### Krein Orthogonality and the Complement

**Definition.** Two elements are **Krein-orthogonal**, written $\tilde Q_1\perp_K\tilde Q_2$, when $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=0$; two subspaces are Krein-orthogonal when every element of one is orthogonal to every element of the other. The **Krein-orthogonal complement** of $\mathbb{W}$ is
$$
\mathbb{W}^{\perp_K}=\{\tilde Q:\langle\tilde Q,\tilde W\rangle_{\natural*}=0\ \text{for every}\ \tilde W\in\mathbb{W}\}.
$$

**Example (a self-orthogonal line).** The line $\mathbb{W}=\mathbb{C}(e_t+\vec e_x)$ is isotropic, $\langle e_t+\vec e_x\rangle_{\natural*}=0$, so $\mathbb{W}\subseteq\mathbb{W}^{\perp_K}$ and $\mathbb{W}+\mathbb{W}^{\perp_K}=\mathbb{W}^{\perp_K}$ has dimension three. The sum is not the algebra, and no direct sum decomposition is obtained from that line alone.

**Theorem (the line criterion).** For $\tilde Q\neq0$ the line $\mathbb{C}\tilde Q$ is non-degenerate for the Krein form exactly when $\langle\tilde Q\rangle_{\natural*}\neq0$. In that case
$$
\mathbb{B}=\mathbb{C}\tilde Q\oplus(\mathbb{C}\tilde Q)^{\perp_K},
\qquad
\dim_{\mathbb{C}}(\mathbb{C}\tilde Q)^{\perp_K}=3,
$$
and the restriction of the form to the line is positive definite when the value is positive and negative definite when it is negative. When the value vanishes the line is totally isotropic and lies in its own complement.

*Proof.* The Gram matrix of the restriction to the line is the single entry $\langle\tilde Q\rangle_{\natural*}$, so the line is non-degenerate exactly when that entry is non-zero, and its sign is the sign of the entry. For a non-degenerate line the complement is non-degenerate and the sum is direct, of dimensions $1$ and $4-1=3$. For a vanishing entry every vector of the line is orthogonal to the line, so the line is its own radical.

**Corollary (the sign of the line).** The line $\mathbb{C}\tilde Q$ is positive definite exactly in the positive-regular case and negative definite exactly in the negative-regular case. The value of the norm, its sign and the definiteness of the line are one datum.

### The Krein Cone

**Definition.** The **Krein cone** is the closure of the positive-regular region,
$$
P_K=\{\tilde Q:\langle\tilde Q\rangle_{\natural*}\ge0\}
=\{\tilde Q:|Q_t|\ge\lVert\vec Q\rVert_E\}.
$$

**Theorem (the shape of the cone).** $P_K$ is closed, invariant under multiplication by positive real scalars, and star-shaped with respect to the origin. Its interior is the positive-regular region, its boundary is the null set $\mathcal K$, and it is neither convex nor pointed.

*Proof.* Closedness is the closedness of the inequality. Homogeneity is $\langle\lambda\tilde Q\rangle_{\natural*}=\lambda^2\langle\tilde Q\rangle_{\natural*}$ for real $\lambda>0$, and the straight-line homotopy $\tilde Q\mapsto t\tilde Q$, $t\in[0,1]$, preserves the inequality, so the cone is star-shaped. The interior is the strict inequality and the boundary the equality. The cone is not pointed because it is invariant under $\tilde Q\mapsto-\tilde Q$, so $P_K\cap(-P_K)=P_K$. It is not convex by the example below.

**Example (the cone is not convex).** The elements $e_t+\vec e_y$ and $-e_t+\vec e_y$ both lie in $P_K$, with value $1-1=0$; their midpoint $\vec e_y$ has value $-1$ and lies outside.

## The degeneracy case: the null set

**Definition.** The **null set** is
$$
\mathcal K=\{\tilde Q:\langle\tilde Q\rangle_{\natural*}=0\}
=\{\tilde Q:|Q_t|=\lVert\vec Q\rVert_E\}.
$$
Its elements are **isotropic**; the non-zero ones are the **Krein-null** elements. The **doubly null set** is
$$
\mathcal K_{\mathrm d}=\{\tilde Q\in\mathcal K:\langle\tilde Q\rangle_{\natural}=0\}
=\mathcal K\cap\mathcal N,
$$
where $\mathcal N=\{\langle\tilde Q\rangle_{\natural}=0\}$ is the algebraic null cone, whose punctured part is the zero-divisor set $\mathcal Z$.

The null set is a real cone of real dimension $7$, smooth off the origin, by the gradient computation above. Every non-zero element of it has $Q_t\neq0$; the origin is the only null point with vanishing scalar part.

**Theorem (the doubly null elements).** Let $\tilde Q\neq0$ with $\langle\tilde Q\rangle_{\natural}=0$. Then
$$
\langle\tilde Q\rangle_{\natural*}\leq0,
$$
and equality holds exactly on the doubly null Peirce lines, that is, exactly when $\tilde Q\in\mathbb{C}(e_t+i\vec u)$ for some $\vec u\in S^2$.

*Proof.* The vanishing of the algebraic norm gives $Q_t^2=-\sum_kQ_k^2$, hence
$$
|Q_t|^2=\Bigl|\sum_kQ_k^2\Bigr|\leq\sum_k|Q_k|^2=\lVert\vec Q\rVert_E^2
$$
by the triangle inequality, which is $\langle\tilde Q\rangle_{\natural*}\leq0$. The equality case is the classification of *The K-Degenerate Sector*, §*The Doubly Null Stratum*: the lines that are null for both norms are exactly the Peirce lines.

**Corollary (the shape of the doubly null set).** $\mathcal K_{\mathrm d}=\bigcup_{\vec u\in S^2}\mathbb{C}(e_t+i\vec u)$ is a real cone of real dimension $4$.

*Proof.* Each line is a real plane, and the parameter $\vec u$ runs over $S^2$; distinct unit vectors give distinct lines, so the dimension is $2+2=4$.

**Corollary (the two strata).** The null set splits as
$$
\mathcal K=\mathcal K_{\mathrm d}\uplus\mathcal K_{\mathrm u},
\qquad
\mathcal K_{\mathrm u}=\mathcal K\setminus\mathcal K_{\mathrm d}.
$$
The points of $\mathcal K_{\mathrm d}$ are the zero divisors together with the origin; the points of $\mathcal K_{\mathrm u}$ are non-zero and are units. The set $\mathcal K_{\mathrm u}$ is open and dense in $\mathcal K$.

*Proof.* By the criterion of *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, a non-zero element is a zero divisor exactly when its algebraic norm vanishes, that is exactly on $\mathcal K_{\mathrm d}$; the origin is the remaining point of $\mathcal K_{\mathrm d}$. The elements of $\mathcal K_{\mathrm u}$ have non-zero algebraic norm, hence are units. The set $\mathcal K_{\mathrm d}$ is closed in $\mathcal K$, being the trace of the closed algebraic null cone, and it has real dimension $4$ by the preceding corollary; a set of dimension $4$ has empty interior in the cone $\mathcal K$ of dimension $7$, so $\mathcal K_{\mathrm d}$ is nowhere dense in $\mathcal K$ and its complement $\mathcal K_{\mathrm u}$ is open and dense.

**Remark (the null set is not the zero-divisor set).** The element $e_t+\vec e_x$ is null and a unit; the element $\vec e_x+i\vec e_y$ is a zero divisor and not null. The null set has real codimension one and the zero-divisor set real codimension two; their intersection is $\mathcal K_{\mathrm d}$, of real dimension four.

## The Two Partitions

The algebra carries two partitions: the metric partition by the sign of the Krein norm and the algebraic partition by invertibility. The following table records them together; the pair is $(\langle\tilde Q\rangle_{\natural*},\langle\tilde Q\rangle_{\natural})$.

| sign of $\langle\tilde Q\rangle_{\natural*}$ | unit | zero divisor |
|---|---|---|
| positive | $e_t$ $(1,1)$ | none |
| negative | $e_t+2\vec e_x$ $(-3,5)$ | $\vec e_x+i\vec e_y$ $(-2,0)$ |
| null | $e_t+\vec e_x$ $(0,2)$ | $e_t+i\vec e_x$ $(0,0)$ |

The origin has the pair $(0,0)$ and is neither a unit nor a zero divisor.

**Theorem (the comparison).** The following hold.

1. If $\langle\tilde Q\rangle_{\natural*}>0$ then $\tilde Q$ is a unit.
2. If $\tilde Q$ is a zero divisor then $\langle\tilde Q\rangle_{\natural*}\leq0$.
3. The converses fail: negative units, negative zero divisors, null units and null zero divisors all exist.
4. The positive region is contained in the unit group; the zero-divisor set is contained in the closed set $\{\langle\tilde Q\rangle_{\natural*}\le0\}$. Neither inclusion is an equality.

*Proof.* The first point is §*The regular case: the positive and the negative regions*. The second is the inequality of §*The degeneracy case: the null set*, applied to the algebraic null cone. The examples of the table give the third. For the fourth, $e_t+2\vec e_x$ is a negative unit and $e_t+\vec e_x$ is a null unit, so the unit group is not the positive region; $\vec e_x+i\vec e_y$ is a negative zero divisor, so the zero-divisor set is not the null set.

**Remark (the shape of the two degeneracies).** The algebraic null cone has real codimension two, so the unit group is open and dense. The Krein null set has real codimension one. The zero-divisor set lies in the closed set $\{\langle\tilde Q\rangle_{\natural*}\le0\}$ and meets the null set exactly in the non-zero points of the doubly null Peirce lines; elsewhere it lies in the open negative region. The unit group meets the positive region, the negative region and the null set.

**Theorem (the algebraic norm on the null set).** The restriction of the algebraic norm to the null set is onto $\mathbb{C}$; on the punctured null set it is onto $\mathbb{C}^*$. Hence the algebraic norm is not a function of the Krein norm.

*Proof.* For $\tilde Q=c(e_t+\vec e_x)$ one has $\langle\tilde Q\rangle_{\natural*}=|c|^2(1-1)=0$ and $\langle\tilde Q\rangle_{\natural}=c^2(1+1)=2c^2$. As $c$ ranges over $\mathbb{C}$, or over $\mathbb{C}^*$, the value $2c^2$ ranges over $\mathbb{C}$, or over $\mathbb{C}^*$.

**Remark (the contrast with the quaternionic norm).** For the quaternionic norm the non-zero set is exactly the unit group, and the zero set is the algebraic null cone, whose punctured part is the zero-divisor set. For the Krein norm the non-zero set is a union of two sign regions that is not a group, and the zero set is a real cone of codimension one that meets both the unit group and the zero-divisor set. The independence is two-way: $e_t$ and $\vec e_x$ have the same algebraic norm $1$ and Krein norms $1$ and $-1$, while the null set carries every algebraic norm. The Krein norm measures a metric position; the quaternionic norm measures invertibility.

## Why There Is No Spectral Split

**The question.** The quaternionic norm and the square of the vector part are the constant term and the discriminant of one characteristic polynomial, $p_{\tilde Q}(X)=X^2-2Q_tX+N$ with $N=Q_t^2+B^2$. The corpus therefore reads them as the two coordinates of one plane and cuts that plane into four sectors, one to each spectral pattern. The Krein norm invites the same treatment: one axis the sign of $\langle\tilde Q\rangle_{\natural*}$, the other the vanishing of $B^2$, giving a regular and a degenerate article with two spectral halves each. That plane is declined here. The reason is structural: the Krein norm and the spectral condition are invariants of **different groups**, so the two axes are not commensurable. The four reasons follow, and the last subsection records the refinement that is available.

**The quaternionic plane, and why it works.** On $\mathbb{B}$ the pair $(N,B^2)$ is equivalent to the pair $(2Q_t,N)$, that is, to the characteristic polynomial. Both entries are polynomial invariants of the element under similarity, $\tilde Q\mapsto\tilde P\tilde Q\tilde P^{-1}$ with $\tilde P$ a unit: the trace, the norm and the discriminant are coefficients of $p_{\tilde Q}$, and $p_{\tilde P\tilde Q\tilde P^{-1}}=p_{\tilde Q}$. The four sectors are therefore four **similarity-invariant** conditions, and the four spectral patterns — an eigenvalue zero or not, the two eigenvalues equal or not — are exactly the four cells. The plane is well posed because both axes live in the same invariant ring, that of the algebra automorphisms.

### The Null Set Is a Single Orbit

**Theorem (transitivity on the null set).** The isometry group $\mathrm{U}(1,3)$ of the Krein form acts transitively on $\mathcal K\setminus\{0\}$.

*Proof.* Two steps. First, the group is transitive on the isotropic lines: by Witt's theorem every isometry of a subspace extends, and the null lines are the points of the null quadric, on which $\mathrm{U}(1,3)$ acts transitively. So an isometry carries $\mathbb{C}\tilde Q_1$ to $\mathbb{C}\tilde Q_2$, and the image of $\tilde Q_1$ is $\mu\tilde Q_2$ for some $\mu\neq0$. Second, the stabiliser of a null line acts transitively on the line minus its origin. Let $\tilde Q$ be null and choose $\tilde V$ with $\langle\tilde V,\tilde V\rangle_{\natural*}=1$ and $\langle\tilde V,\tilde Q\rangle_{\natural*}\neq0$, possible because the radical of $\tilde Q^{\perp_K}$ is exactly $\mathbb{C}\tilde Q$. Replacing $\tilde Q$ by a multiple, take $\langle\tilde V,\tilde Q\rangle_{\natural*}=1$. In the basis $(\tilde Q,\tilde V)$ the Gram matrix is
$$
E=\begin{pmatrix}0&1\\1&1\end{pmatrix},
$$
of signature $(1,1)$, so its orthogonal complement is negative definite and every isometry of the plane extends by the identity. For $\mu\neq0$ the matrix
$$
M_\mu=\begin{pmatrix}\mu&b\\0&1/\bar\mu\end{pmatrix},
\qquad
2\operatorname{Re}\bigl(b/\mu\bigr)=1-\frac{1}{\lvert\mu\rvert^2},
$$
satisfies $M_\mu^{*}EM_\mu=E$ with $E$ that Gram matrix, and $M_\mu\tilde Q=\mu\tilde Q$. Such a $b$ exists for every $\mu\neq0$. Hence the stabiliser rescales the line by any non-zero factor, and the two steps compose.

**Corollary (the spectral type is not a Krein invariant).** Every function on $\mathcal K\setminus\{0\}$ invariant under $\mathrm{U}(1,3)$ is constant there, because the set is a single orbit. The square of the vector part is not constant:
$$
B^2(e_t+\vec e_x)=1,\qquad
B^2\Bigl(e_t+\tfrac{1}{\sqrt2}(\vec e_x+i\vec e_y)\Bigr)=\tfrac12+\tfrac{i^2}{2}=0,
$$
and both elements are null, of Krein norms $1-1=0$ and $1-\tfrac12-\tfrac12=0$. **An isometry of the form therefore carries a spectrally regular null element to a spectrally degenerate one.** The would-be sectors are not stable under $\mathrm{U}(1,3)$, whereas the quaternionic sectors are stable under the unit group acting by conjugation. This is the decisive difference: $B^2$ is an invariant of the algebra and not of the form, and the isometry group contains transformations that are not algebra automorphisms.

### The Krein Norm Is Not a Spectral Coefficient

**The Krein norm is not a function of the characteristic polynomial.** Take $Q_t=1$ and the two vector parts $(i,0,0)$ and $(1,i,i)$. Both give $B^2=-1$ and therefore $N=0$, so both have the same characteristic polynomial $X^2-2X$, and the same spectrum $\{0,2\}$. Their Krein norms are
$$
1-\lvert i\rvert^2=0,\qquad
1-\bigl(1+\lvert i\rvert^2+\lvert i\rvert^2\bigr)=-2.
$$
The same polynomial therefore carries a null value and a negative value. The Krein norm is not a coefficient of $p_{\tilde Q}$, and $p_{\tilde Q}$ is not a function of the Krein norm.

**The Krein norm is not similarity-invariant.** For the unit $\tilde P=e_t+2i\vec e_x$ one has $\langle\tilde P\rangle_{\natural}=1+(2i)^2=-3$ and $\tilde P^{-1}=\tfrac13(-e_t+2i\vec e_x)$, and a direct computation gives
$$
\tilde P\,\vec e_y\,\tilde P^{-1}=-\tfrac53\vec e_y-\tfrac43 i\vec e_z .
$$
The square of the vector part is $25/9-16/9=1$ before and after, as it must be, while the Krein norm moves from $0-1=-1$ to $0-\bigl(25/9+16/9\bigr)=-41/9$. A similarity, which is the natural change of element in the spectral problem, does not preserve the Krein norm; an isometry, which preserves the Krein norm, does not preserve the spectral type. The two problems are carried by different groups, and neither group contains the other.

**In the other direction, $B^2$ is not a function of the Krein norm.** The elements
$$
\tilde Q_1=e_t+\tfrac{1}{\sqrt2}\vec e_x,\qquad
\tilde Q_2=e_t+\tfrac12(\vec e_x+i\vec e_y)
$$
have the same Krein norm $\tfrac12$, since $\lVert\vec Q_1\rVert_E^2=\tfrac12=\lVert\vec Q_2\rVert_E^2$, and different vector squares, $\tfrac12$ and $\tfrac14-\tfrac14=0$. Neither condition is a function of the other.

### Every Krein Stratum Meets Both Spectral Types

The examples of the preceding subsection already show that no Krein stratum is spectrally uniform. The table collects one witness of each type in each stratum.

| Krein stratum | real dimension | spectrally degenerate witness | spectrally regular witness |
|---|---|---|---|
| positive region | $8$ | $e_t$, with $B^2=0$ | $e_t+\tfrac12\vec e_x$, with $B^2=\tfrac14$ |
| negative region | $8$ | $\vec e_x+i\vec e_y$, with $B^2=0$ | $\vec e_x$, with $B^2=1$ |
| doubly null set $\mathcal K_{\mathrm d}\setminus\{0\}$ | $4$ | none | $e_t+i\vec e_x$, with $B^2=-1$ |
| isotropic units $\mathcal K_{\mathrm u}$ | $7$ | $e_t+\tfrac{1}{\sqrt2}(\vec e_x+i\vec e_y)$, with $B^2=0$ | $e_t+\vec e_x$, with $B^2=1$ |

The third row is the sharp one: **the doubly null set off the origin is entirely spectrally regular.** There $N=0$ and $\langle\tilde Q\rangle_{\natural*}=0$ give $Q_t^2+B^2=0$ and $Q_t\neq0$, hence $B^2=-Q_t^2\neq0$. A spectral subdivision would have nothing to subdivide there, and it would still leave both cases to be treated inside each of the other three strata.

### The Split Would Group the Wrong Things

The four cells of the proposed plane are all non-empty, so the plane is definable; it is the grouping that fails.

- The origin is in $\mathcal K_{\mathrm d}$ and is spectrally degenerate, $B^2=0$; the Peirce lines are in $\mathcal K_{\mathrm d}$ and are spectrally regular, $B^2=-Q_t^2\neq0$. A spectral split separates the origin from the Peirce lines, while the algebraic partition groups them: both are zero divisors, and both are doubly null. The natural stratum $\mathcal K_{\mathrm d}$ is destroyed.
- The spectral split separates $\mathcal K_{\mathrm u}$ into the set $\mathcal K_{\mathrm u}\cap\{B^2=0\}$, of real dimension $5$, and its complement, of dimension $7$. The first set is a cone of null elements with a repeated eigenvalue and non-zero algebraic norm; every non-zero point of it is a unit. It is not an object of the Krein theory, and it is not an object of the spectral theory either: it is cut by the algebraic norm and the discriminant together, and the algebraic norm is what decides invertibility there.
- The negative region is cut into the points with a repeated eigenvalue and the rest, although both halves contain units and zero divisors and both have the same Krein sign.

The plane would therefore produce four articles that are each a mixture of algebraic classes and none of which is invariant under the isometry group of the form.

### What Does Refine It

There is a second plane, and it is the one the corpus uses: the Krein value against the **algebraic** value $\langle\tilde Q\rangle_{\natural}$, not the discriminant. Its cells are those of the table of §*The Two Partitions*: the positive cell of the zero-divisor column is empty, by the theorem that a positive element is a unit, and every other cell is non-empty. Each cell is an invariant set: the Krein value is preserved by $\mathrm{U}(1,3)$ and the algebraic value by the algebra automorphisms, so each cell is carved by a genuine invariant of one of the two structures. The refinement is the trace of the algebraic partition on the three Krein strata, and it is the one that decides the operator theory — the polar decomposition and the sandwich follow $\langle\cdot\rangle_{\natural}$, while the adjoint and the isometries follow $\langle\cdot\rangle_{\natural*}$.

The two articles that follow this partition are *The K-Regular Sector*, for the first two rows, and *The K-Degenerate Sector*, for the last. The spectral condition appears in both only as a remark on the operator theory, never as a subdivision.

## The Two Cases on the Remarkable Subspaces

The restriction of the Krein norm to each of the six remarkable subspaces has the realified signature tabulated in *Remarkable Subspaces under the General Quaternionic Sesqualgebra*. What the signatures leave open is the algebraic status of the null elements, and it is settled here: the equation $\langle\tilde Q\rangle_{\natural*}=0$ has non-zero solutions only on the four Lorentzian subspaces, and there the solutions are units on two of them and zero divisors on the other two.

| remarkable subspace | non-zero Krein-null elements | algebraic status |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | none | — |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | none | — |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | a cone of dimension $3$ | every one is a unit |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | a cone of dimension $3$ | every one is a unit |
| $\mathbb{M}_{+}$, the Hermitian subspace | a cone of dimension $3$ | every one is a zero divisor |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | a cone of dimension $3$ | every one is a zero divisor |

**Theorem (the restrictions).** On the centre the Krein norm is positive definite and on the vector subspace negative definite, so neither carries a non-zero null element; on each of the four four-dimensional subspaces it is Lorentzian, and each carries a null cone of real dimension $3$. The non-zero null elements are units on the quaternion and anti-quaternion subspaces and zero divisors on the Hermitian and anti-Hermitian subspaces. On the last two the null cone is exactly the trace of the doubly null Peirce lines.

*Proof.* The signatures are the restriction table of the cited article. The algebraic status is read from the coefficients. On the quaternion subspace $Q_t=q_t$ and $Q_k=q_k$ are real, so $\langle\tilde Q\rangle_{\natural}=q_t^2+\sum_kq_k^2$ and $\langle\tilde Q\rangle_{\natural*}=q_t^2-\sum_kq_k^2$; a null element has $q_t^2=\sum_kq_k^2$, hence $\langle\tilde Q\rangle_{\natural}=2q_t^2\neq0$ off the origin, and it is a unit. On the anti-quaternion subspace $Q_t=iq_t$ and $Q_k=iq_k$ with $q_\mu$ real, so $\langle\tilde Q\rangle_{\natural*}=q_t^2-\sum_kq_k^2$ and $\langle\tilde Q\rangle_{\natural}=-(q_t^2+\sum_kq_k^2)$, which is non-zero off the origin. On the Hermitian subspace $Q_t=a_0$ is real and $Q_k=ia_k$ with $a_k$ real, so $\langle\tilde Q\rangle_{\natural}=a_0^2-\sum_ka_k^2$, which vanishes exactly with $\langle\tilde Q\rangle_{\natural*}=a_0^2-\sum_ka_k^2$; a non-zero null element there is a zero divisor. The anti-Hermitian subspace is $i$ times the Hermitian one and has the same property. The traces are the Peirce lines because a null element of $\mathbb{M}_{+}$ is $a_0(e_t+i\vec u)$ with $\vec u=\vec a/|a_0|$ a real unit vector, and $\mathbb{M}_{-}=i\mathbb{M}_{+}$.

**Corollary.** Every non-zero element of the centre, the quaternion subspace and the anti-quaternion subspace is a unit of the plain product. The vector subspace, the Hermitian subspace and the anti-Hermitian subspace contain zero divisors; on the last two a non-zero element is a zero divisor exactly when it is Krein-null, while the vector subspace has no non-zero Krein-null element.

**Remark.** The table records six restrictions, not a cover: a generic null element has all four coefficients non-zero and lies in none of the six subspaces.

## Summary

The Krein norm $\langle\tilde Q\rangle_{\natural*}=|Q_t|^2-\lVert\vec Q\rVert_E^2$ is real, indefinite and not multiplicative: $e_t+\vec e_x$ and $e_t-\vec e_x$ are both null and their product $2e_t$ has value four, while the regular elements $\vec e_x$ and $\vec e_x+i\vec e_y$ have a null product. The regular set is therefore not a group, although it is open and dense; it has exactly two connected components, the positive and the negative regions, separated by the null set. The closure of the positive region is the Krein cone $P_K=\{|Q_t|\ge\lVert\vec Q\rVert_E\}$, closed and star-shaped but neither convex nor pointed.

The comparison with invertibility is one-sided. Every positive element is a unit and every zero divisor has non-positive Krein norm, but negative units, negative zero divisors, null units and null zero divisors all occur. The equality case of the inequality is the doubly null Peirce lines, so the zero-divisor set lies in the closed set $\{\langle\cdot\rangle_{\natural*}\le0\}$ and meets the null set exactly in those lines. The null set splits into the doubly null set, the origin together with the Peirce lines, of real dimension four, and the isotropic units, its open dense complement. The algebraic norm is onto $\mathbb{C}$ on the null set, so it is not a function of the Krein norm; in the other direction $e_t$ and $\vec e_x$ have the same algebraic norm, $1$, and Krein norms of both signs.

On the six remarkable subspaces the Krein norm is definite on the centre and on the vector subspace, and Lorentzian on the four four-dimensional subspaces; the null elements of the quaternion and anti-quaternion subspaces are units, and those of the Hermitian and anti-Hermitian subspaces are zero divisors.

The quaternionic norm decides invertibility: its non-zero set is the unit group and its zero set is the algebraic null cone. The Krein norm decides only a metric position, and the two partitions agree only in the implication positive implies unit.

No spectral split is available. The quaternionic plane works because the norm and the discriminant are two coefficients of one characteristic polynomial, hence two similarity-invariant conditions; the Krein norm is neither a coefficient nor similarity-invariant. The isometry group acts transitively on the non-zero null set, so it carries a spectrally regular null element to a spectrally degenerate one; the Krein norm is not a function of the characteristic polynomial; every Krein stratum meets both spectral types; and the doubly null set off the origin is entirely spectrally regular, so a spectral subdivision would separate the origin from the Peirce lines. The refinement that does exist is the Krein value against the algebraic value, and it is the partition of the two sector articles.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, $e_t$ the identity |
| $\tilde Q=Q_te_t+\vec Q$ | an element and its scalar–vector split |
| $Q_\mu=q_\mu+iq'_\mu$ | the complex coefficients |
| $\varepsilon=(1,-1,-1,-1)$ | the coefficient signs |
| $\tilde Q^{\natural}=Q_t-\vec Q$ | the natural conjugation |
| $\tilde Q^*=\bar Q_t-\overline{\vec Q}$ | the Hermitian conjugation |
| $\lVert\tilde Q\rVert_E^2=\sum_\mu|Q_\mu|^2$ | the Euclidean norm |
| $\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu|Q_\mu|^2$ | the Krein norm |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the quaternionic norm, the algebraic norm |
| $\mathbb{B}^{\natural*}_{+},\mathbb{B}^{\natural*}_{-}$ | the positive-regular and negative-regular regions |
| $\mathcal K=\{\langle\cdot\rangle_{\natural*}=0\}$ | the null set, the Krein-degenerate case |
| $P_K=\{\langle\cdot\rangle_{\natural*}\ge0\}$ | the Krein cone, the closure of the positive region |
| $\mathcal K_{\mathrm d}=\mathcal K\cap\mathcal N$ | the doubly null set; the Peirce lines and the origin |
| $\mathcal K_{\mathrm u}=\mathcal K\setminus\mathcal K_{\mathrm d}$ | the isotropic units |
| $\mathcal N=\{\langle\cdot\rangle_{\natural}=0\}$ | the algebraic null cone |
| $\mathcal Z=\mathcal N\setminus\{0\}$ | the zero-divisor set |
| $\mathbb{B}^{\times}$ | the unit group of the plain product |
| $\mathbb{C}(e_t+i\vec u)$, $\vec u\in S^2$ | the doubly null Peirce lines |

## Further Reading

- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the form, its Gram matrix and its inertia.
- [The Fundamental Symmetry of the Form](the-fundamental-symmetry-of-the-form.html), for the fundamental symmetry and the bridge $\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\langle\tilde Q_2,J\tilde Q_1\rangle_{*}$.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the quaternionic norm, its multiplicativity, the unit group and the zero-divisor cone.
- [The K-Regular Sector](the-krein-norm-regular-sector.html), for the positive and negative regions, their geometry, their products and inversion, and their relation to the unit group.
- [The K-Degenerate Sector](the-krein-norm-degenerate-sector.html), for the null set, the doubly null Peirce lines, the isotropic units and their products.
- [The Krein Level Sets and the Hyperbolic Structure](the-krein-level-sets-and-the-hyperbolic-structure.html), for the level sets, the positive region, the negative region, the null set and the complex hyperbolic ball.
- [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the restriction of the Krein form to the six remarkable subspaces and their signatures.
- [The Krein Isometry Group and Its Cartan Decomposition](the-krein-isometry-group-and-its-cartan-decomposition.html), for the isometry group $\mathrm{U}(1,3)$, its actions and its Cartan decomposition.
- [J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra](j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra.html), for the operator theory of the form and the Krein adjoint.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the comparison of the four forms and of the four norms.
- [The Realification of the General Quaternionic Sesqualgebra](the-realification-of-the-general-quaternionic-sesqualgebra.html), for the real matrix of the form and the signature $(2,6)$.
- [Zero Divisors of the General Quaternionic Algebra](zero-divisors-of-the-general-quaternionic-algebra.html), for the zero-divisor set and its criterion.
- [Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the Peirce idempotents and the minimal left ideals behind the doubly null lines.
- [Indefinite Inner Product Spaces](indefinite-inner-product-spaces.html), for the classification of subspaces and the isotropic structure of an indefinite form.
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the fundamental decomposition and the theory of Krein spaces.
- Thomas Ya. Azizov and Iosif S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the Pontryagin space and the indefinite metric.
