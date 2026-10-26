# __The N-Regular Sector__

## Introduction

The quaternionic norm $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ is the one multiplicative norm of the biquaternion algebra. Its non-zero set is the **$\natural$-regular sector**,

$$
\mathbb{B}^{\times}=\{\tilde Q\in\mathbb{B}:\langle\tilde Q\rangle_{\natural}\neq0\},
$$

and it is exactly the group of units of the plain product. This article studies that sector as a set: its characterisation, its matrix model, its multiplicative and topological structure, and the place of the spectral condition inside it. Its partner is *The N-Degenerate Sector*, the null cone, on which the norm vanishes.

The sector is defined by one condition, and the spectrum does not split it into two open halves. It is connected. The spectral condition cuts inside it a closed stratum of real codimension two, the spectrally degenerate units, and leaves its complement, the spectrally regular units, open and dense. The two pieces are the cells $\Sigma_{11}$ and $\Sigma_{10}$ of *The N-Regular, Spectrally Regular Sector* and *The N-Regular, Spectrally Degenerate Sector*; this article records their place in the sector and cites their internal study.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, of complex dimension four and real dimension eight, with $\vec e_x\vec e_y=\vec e_z$ and $\vec e_k^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The natural conjugation is $\tilde Q^{\natural}=Q_t-\vec Q$ and the Hermitian conjugation is $\tilde Q^{*}=\overline{Q_t}-\overline{\vec Q}$. The **quaternionic norm** is

$$
\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2,\qquad B^2=Q_x^2+Q_y^2+Q_z^2,
$$

a complex scalar; it is multiplicative and it decides invertibility. Its zero set is the **null cone** $\mathcal{N}$. The **spectral-degenerate cone** is $\mathcal{S}=\{B^2=0\}$. The product is the plain product, with unit $e_t$.

The words are fixed as follows. A **sector** is one of the two halves selected by the norm, as in the title of this article; a **cell** is one of the four intersections $\Sigma_{ij}$ selected by the norm and the spectrum together, called a sector in the spectral articles. The two uses are kept apart here. The **norm-one group** is $\mathbb{B}^{\times}_1=\{N=1\}$, called the **unit factor** in the polar articles; the word *unit* alone means an invertible element, an element of $\mathbb{B}^{\times}$. The two senses are kept apart, as in *Conventions in Mathematics*, §*The Form Convention, the Norm Convention and the Unitary Convention*.

## Definition and Characterisation

**Definition.** The **$\natural$-regular sector** is

$$
\mathbb{B}^{\times}=\{\tilde Q\in\mathbb{B}:\langle\tilde Q\rangle_{\natural}\neq0\}.
$$

**Theorem (the criterion).** For $\tilde Q\in\mathbb{B}$ the following are equivalent:

(i) $\langle\tilde Q\rangle_{\natural}\neq0$;

(ii) $\tilde Q$ is invertible in the plain product;

(iii) $\det\mathsf{M}_2(\tilde Q)\neq0$;

(iv) the left translation $L_{\tilde Q}(\tilde X)=\tilde Q\tilde X$ is bijective;

(v) the right translation $R_{\tilde Q}(\tilde X)=\tilde X\tilde Q$ is bijective.

For $\tilde Q\neq0$ they are also equivalent to:

(vi) $\tilde Q$ is not a zero divisor.

*Proof.* (i)$\iff$(ii): if $\langle\tilde Q\rangle_{\natural}\neq0$, the inverse is $\tilde Q^{\natural}/N$, by the identity $\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural} e_t$; conversely an invertible element has a non-zero norm, since the norm is multiplicative and $\langle e_t\rangle_{\natural}=1$. (ii)$\iff$(iii): the matrix model is an algebra isomorphism and its determinant is the norm. (ii)$\Rightarrow$(iv),(v): multiplication by a unit is a bijection with inverse multiplication by $\tilde Q^{-1}$. (iv)$\Rightarrow$(i): if $\langle\tilde Q\rangle_{\natural}=0$ and $\tilde Q\neq0$, the left translation kills the non-zero element $\tilde Q^{\natural}$; if $\tilde Q=0$, it is the zero map. The right-hand side is the same. (i)$\Rightarrow$(vi): a unit cannot annihilate a non-zero element. (vi)$\Rightarrow$(i): if $\langle\tilde Q\rangle_{\natural}=0$ and $\tilde Q\neq0$, then $\tilde Q\tilde Q^{\natural}=0$ with $\tilde Q^{\natural}\neq0$, so $\tilde Q$ is a left zero divisor.

**Corollary (inverse and norm of the inverse).** For $\tilde Q\in\mathbb{B}^{\times}$,

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{\langle\tilde Q\rangle_{\natural}},\qquad \langle\tilde Q^{-1}\rangle_{\natural}=\frac{1}{\langle\tilde Q\rangle_{\natural}}.
$$

**Theorem (the group).** $\mathbb{B}^{\times}$ is a group under the plain product.

*Proof.* Closure is multiplicativity: $\langle\tilde P\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}\neq0$. Associativity is that of the algebra. The unit is $e_t$, of norm one. The inverse is the corollary above.

**Remark (the other products).** For the product $\tilde P^{\natural}\tilde Q$ there is a left unit $e_t$ and no right unit, so there is no group of units. The criterion is unchanged: the one-sided equations with $e_t$ have the common unique solution $\tilde Q/\langle\tilde Q\rangle_{\natural}$ exactly when $\langle\tilde Q\rangle_{\natural}\neq0$. The sector is therefore a plain-product object; the other products select the same set and lose the group (*N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The $\natural$-regular case: The Group of Units*).

**Remark (the name).** In ring theory a regular element is a non-zero-divisor, and the origin qualifies; there the regular elements are $\mathbb{B}^{\times}\cup\{0\}$. The title uses **$\natural$-regular** in the sense of the norm, so the origin is excluded and the sector is exactly the unit group. The two readings differ at one point, the apex.

## The Matrix Picture

**Theorem (the matrix identifications).** The representation $\mathsf{M}_2$ restricts to an isomorphism of complex Lie groups

$$
\mathbb{B}^{\times}\cong GL_2(\mathbb{C}),
$$

and under it the quaternionic norm is the determinant, $\langle\tilde Q\rangle_{\natural}=\det\mathsf{M}_2(\tilde Q)$. The norm-one group is the special linear group,

$$
\mathbb{B}^{\times}_1=\{N=1\}\cong SL_2(\mathbb{C}).
$$

*Proof.* The representation is an algebra isomorphism, so an element is invertible exactly when its image is; the determinant of the image is $Q_t^2+Q_x^2+Q_y^2+Q_z^2=\langle\tilde Q\rangle_{\natural}$; and the condition $\langle\tilde Q\rangle_{\natural}=1$ is the condition $\det=1$.

**Theorem (the determinant sequence).** The norm is a surjective homomorphism of complex Lie groups,

$$
1\longrightarrow\mathbb{B}^{\times}_1\longrightarrow\mathbb{B}^{\times}\xrightarrow{\ N\ }\mathbb{C}^{\times}\longrightarrow1,
$$

and the real dimensions add as $8=6+2$.

*Proof.* Multiplicativity makes $\langle\tilde Q\rangle_{\natural}$ a homomorphism and its kernel is $\mathbb{B}^{\times}_1$ by definition. Surjectivity holds because $\langle Ae_t\rangle_{\natural}=A^2$ and every non-zero complex number is a square. The dimensions are those of $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and $\mathbb{C}^{\times}$.

**Remark (no splitting along the centre).** The sequence does not split by the centre. The restriction of $\langle\tilde Q\rangle_{\natural}$ to $\mathbb{C}^{\times}e_t$ is the squaring map $A\mapsto A^2$, which is two-to-one and not an isomorphism. It does split as groups, by the non-central section $\lambda\mapsto\mathrm{diag}(\lambda,1)$; what fails is a splitting by the scalars, and the centre meets $SL_2(\mathbb{C})$ in $\{\pm e_t\}$. The multiplication map

$$
\mathbb{C}^{\times}e_t\times\mathbb{B}^{\times}_1\longrightarrow\mathbb{B}^{\times},\qquad (Ze_t,\tilde U)\longmapsto Ze_t\tilde U,
$$

is a connected two-to-one covering with kernel $\{\pm(e_t,e_t)\}$, so that $\mathbb{B}^{\times}\cong(\mathbb{C}^{\times}\times SL_2(\mathbb{C}))/\{\pm1\}$.

**Proposition (the norm is a submersion).** The norm has non-zero derivative at every point of $\mathbb{B}^{\times}$. Hence the norm $\mathbb{B}^{\times}\to\mathbb{C}^{\times}$ is a locally trivial fibre bundle with fibre $\mathbb{B}^{\times}_1\cong SL_2(\mathbb{C})$, and each level set $\{\langle\tilde Q\rangle_{\natural}=c\}$ with $c\neq0$ is a closed complex hypersurface of complex dimension three and real dimension six.

*Proof.* In the complex coordinates $(Q_t,Q_x,Q_y,Q_z)$ the gradient is $2(Q_t,Q_x,Q_y,Q_z)$, which vanishes only at the origin, and the origin lies on the cone. The fibre over $1$ is $\mathbb{B}^{\times}_1$; the other fibres are its translates by $Ze_t$ with $Z^2=c$.

**Remark (the level sets are homogeneous).** For $c\neq0$ the level set $\{N=c\}$ is a single orbit of the special orthogonal group $\mathrm{SO}(4,\mathbb{C})$ of the norm. Two vectors of equal non-zero value are carried one to the other by an isometry of a non-degenerate quadratic form, by Witt's theorem, and the isometry may be taken of determinant one because a reflection in a non-isotropic vector orthogonal to the target has determinant minus one and fixes that target. The isometry group is not the group of units; it is the group that preserves the quadratic form, and it acts on the level sets but not on the product.

**Remark (complex scaling).** For $\lambda\in\mathbb{C}^{\times}$, $\langle\lambda\tilde Q\rangle_{\natural}=\lambda^2\langle\tilde Q\rangle_{\natural}$. The sector is therefore invariant under the action of $\mathbb{C}^{\times}$ by scalar multiplication; it is a union of punctured complex lines, and the apex of each line is omitted.

## Multiplication and Inversion

**Proposition (the norm is conjugation invariant).** For all $\tilde P,\tilde Q$,

$$
\langle\tilde P\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural},\qquad
\langle\tilde Q^{-1}\rangle_{\natural}=\frac{1}{\langle\tilde Q\rangle_{\natural}},\qquad
\langle\tilde P\tilde Q\tilde P^{-1}\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}.
$$

For every integer $n$, $\langle\tilde Q^n\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}^n$.

*Proof.* The first two are multiplicativity and the inverse formula; the third follows by cancelling $\langle\tilde P\rangle_{\natural}$; the last is induction, with the negative exponents given by the inverse.

**Remark (the inverse in coordinates).** Writing $\tilde Q=Q_te_t+\vec Q$ and $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$,

$$
\tilde Q^{-1}=\frac{Q_te_t-\vec Q}{Q_t^2+B^2},
$$

a rational function of the four coefficients. The denominator is the norm, so the formula is defined exactly on the sector.

**Theorem (the exponential is onto).** The exponential map $\exp:\mathbb{B}\to\mathbb{B}^{\times}$ is surjective and not injective. Every unit has a logarithm; no continuous single-valued branch of the logarithm exists on the whole sector.

*Proof.* The exponential is the matrix exponential under $\mathsf{M}_2$, and every invertible complex matrix has a logarithm. The failure of injectivity and of a global continuous branch are those of the matrix logarithm, read in the algebra (*Biquaternion Elementary Functions*, §*The Logarithm*).

**Remark (the polar decomposition).** Every unit is

$$
\tilde Q=\tilde Q_H\tilde Q_0,
$$

with $\tilde Q_H=(\tilde Q\tilde Q^{*})^{1/2}$ Hermitian positive definite and $\tilde Q_0=\tilde Q_H^{-1}\tilde Q$ unitary. The pair is unique and depends continuously on $\tilde Q$. The four-factor word $r\zeta\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ refines it: a positive scale $r$, a unit phase $\zeta$, a Hermitian positive boost $\tilde U_{\mathrm b}$ of norm one, and a unit real quaternion $\tilde u_{\mathrm r}$ (*The Polar Decomposition of a N-Regular Biquaternion*, §*The Four Factors*).

**Remark (the two decompositions are not the same).** The modulus-unit decomposition $\tilde Q=\Rho\tilde U$ with $\Rho^2=\langle\tilde Q\rangle_{\natural}$ and $\langle\tilde U\rangle_{\natural}=1$ is a bijection onto $\mathcal{H}\times\mathbb{B}^{\times}_1$, where $\mathcal{H}=\{\Rho:\operatorname{Re}\Rho>0\}\cup\{it:t>0\}$ is the half-plane of the principal modulus. It is a bijection of sets, not a homeomorphism: the branch of the square root jumps across the negative real axis, and so does $\tilde U$. The smooth product structure is the non-central one: the section $\lambda\mapsto\mathrm{diag}(\lambda,1)$ trivialises the determinant bundle, so $\mathbb{B}^{\times}$ is diffeomorphic to $\mathbb{C}^{\times}\times SL_2(\mathbb{C})$, while the central multiplication map $\mathbb{C}^{\times}e_t\times\mathbb{B}^{\times}_1\to\mathbb{B}^{\times}$ is a connected two-to-one covering.

## Geometry

**Theorem (open, dense, and boundary).** The sector $\mathbb{B}^{\times}$ is open and dense in $\mathbb{B}$, of real dimension eight. Its complement $\mathcal{N}$ is closed, of empty interior and of real codimension two, and it is the boundary:

$$
\partial\mathbb{B}^{\times}=\mathcal{N}.
$$

*Proof.* The norm is a complex polynomial, so its non-zero set is open and its zero set is closed. The cone is a proper algebraic subset, hence of empty interior, and its complement is dense. The gradient of the norm is non-zero off the apex, so the cone is a smooth real submanifold of real dimension six there; it is defined by two real equations, hence of real codimension two. The boundary of the open set is the intersection of the closures of the set and of its complement, that is the cone.

**Remark (the sector is not convex).** The units $e_t$ and $-e_t$ have the origin as midpoint, and the origin is not a unit. The sector is a union of punctured complex lines, and a line may lie entirely in the cone; on the real line through $e_t$ the sector is the complement of the origin. Convexity fails already there.

**Remark (the Euclidean sphere).** The Euclidean unit sphere $S^7_E$ is not contained in the sector. Its intersection with the cone is the link $L\cong S^2\times S^3$, a closed five-manifold, and the intersection with the sector is the complement of $L$ in $S^7_E$, open and dense in the sphere.

**Remark (the real forms).** The six subspaces are the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$, the vector subspace $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\vec e_x\oplus\mathbb{C}\vec e_y\oplus\mathbb{C}\vec e_z$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_t\oplus\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_{+}=\mathbb{R}e_t\oplus i\mathbb{R}\vec e_x\oplus i\mathbb{R}\vec e_y\oplus i\mathbb{R}\vec e_z$, and the anti-Hermitian subspace $\mathbb{M}_{-}=i\mathbb{R}e_t\oplus\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$. The distribution of the units over them is read from the realified signature of the norm:

| subspace | signature | units |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | $(1,1)$ | the non-zero scalars |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | $(3,3)$ | the complement of the isotropic cone |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | $(4,0)$ | every non-zero element |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | $(0,4)$ | every non-zero element |
| $\mathbb{M}_{+}$, the Hermitian subspace | $(1,3)$ | the complement of its null cone |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | $(3,1)$ | the complement of its null cone |

The norm vanishes only at the origin on the centre, the quaternion subspace and the anti-quaternion subspace, so none of the three contains a zero divisor. On the vector, Hermitian and anti-Hermitian subspaces it is indefinite, and the sector meets each of them in the complement of its null cone (*Remarkable Subspaces under the General Quaternionic Algebra*, §*The Signatures and the Restriction Matrices*).

## The Topology

**Theorem (the homotopy type).** The sector is connected and non-compact, and it retracts onto its maximal compact subgroup,

$$
\mathbb{B}^{\times}\simeq \mathrm{U}(\mathbb{B})=\{\tilde Q:\tilde Q^{*}\tilde Q=e_t\}\cong \mathrm{U}(2)\simeq S^1\times S^3.
$$

Its homotopy groups are

$$
\pi_1(\mathbb{B}^{\times})\cong\mathbb{Z},\qquad
\pi_2(\mathbb{B}^{\times})=0,\qquad
\pi_3(\mathbb{B}^{\times})\cong\mathbb{Z},
$$

and its universal cover is $\mathbb{R}\times S^3$.

*Proof.* The polar decomposition $\tilde Q=\tilde Q_H\tilde Q_0$ retracts the sector onto the unitary group by $\tilde Q\mapsto\tilde Q_0$, continuously and fixing the unitary elements. The unitary group is $\mathrm{U}(2)$, and $\mathrm{U}(2)\cong(S^1\times S^3)/\{\pm e_t\}$ through the phase and the unit quaternions. The homotopy groups and the universal cover are those of $\mathrm{U}(2)$ (*The Unitary Group of the Biquaternion Algebra*; *The Biquaternion Unit Group as a Topological Group*, §*The Topology of the Group*). Non-compactness is witnessed by the unbounded family $c\,e_t+i\sqrt{c^2-1}\,\vec e_x$ with $c\ge1$.

**Theorem (the maximal compact subgroup).** The maximal compact subgroup of $\mathbb{B}^{\times}$ is

$$
\mathrm{U}(\mathbb{B})=\{\tilde Q:\tilde Q^{*}\tilde Q=e_t\}\cong\mathrm{U}(2),
$$

the set of unitary biquaternions. It is generated by the two compact factors, $\mathrm{U}(\mathbb{B})=S^1\cdot S^3$ with $S^1=\mathrm{U}(1)e_t$ the centre circle and $S^3=\{\tilde q\in\mathbb{H}_{\mathbb{B}}:\tilde q\tilde q^{*}=e_t\}$ the unit quaternions, and $S^1\cap S^3=\{\pm e_t\}$.

*Proof.* Let $K\subset\mathbb{B}^{\times}$ be compact. Average the Euclidean inner product over $K$: the form $\langle X,Y\rangle_K=\int_K\langle kX,kY\rangle_E\,dk$ is a positive definite Hermitian form invariant under $K$. Its unitary group is $\mathrm{U}(2)$ in a suitable basis, so $K$ is conjugate into $\mathrm{U}(\mathbb{B})$. Conversely $\mathrm{U}(\mathbb{B})$ is compact, so it is the maximal compact subgroup.

**Theorem (the determinant-one group).** The norm-one group $\mathbb{B}^{\times}_1$ is a closed connected normal subgroup of real dimension six, isomorphic to $SL_2(\mathbb{C})$, homotopy equivalent to $S^3$, and non-compact. It is the fibre of the determinant sequence.

*Proof.* It is the kernel of the continuous homomorphism $\langle\tilde Q\rangle_{\natural}$, hence closed and normal; it is $SL_2(\mathbb{C})$ by the matrix picture; it retracts onto the unit quaternions $S^3$ by the polar decomposition; and the family $c\,e_t+i\sqrt{c^2-1}\,\vec e_x$ lies in it and is unbounded.

**Remark (the two circles).** The centre circle $\mathrm{U}(1)e_t$ is contained in $\mathbb{B}^{\times}$ and not in $\mathbb{B}^{\times}_1$, because $\langle Ae_t\rangle_{\natural}=A^2$ is not one in general. The unit quaternions $S^3$ are contained in $\mathbb{B}^{\times}_1$ and not in the centre. The two-to-one covering $\mathbb{C}^{\times}e_t\times SL_2(\mathbb{C})\to\mathbb{B}^{\times}$ is the precise statement that neither factor alone covers the sector.

**Remark (the Euclidean sphere is not a group).** The Euclidean sphere $\|\tilde Q\|_E=1$ is a genuine $S^7$ and is not a group: the Euclidean norm is not multiplicative, and the sphere contains zero divisors. The sphere that carries a group structure is $S^3$, the compact part of the norm-one group, and it is not the Euclidean one (*The Euclidean Topology of the Biquaternion Algebra*, §*The Euclidean Unit Sphere*).

## The Two Spectral Halves

**Theorem (the spectral partition of the sector).** The sector is the disjoint union

$$
\mathbb{B}^{\times}=\Sigma_{11}\uplus\Sigma_{10},
\qquad
\Sigma_{11}=\{N\neq0,\ B^2\neq0\},\qquad
\Sigma_{10}=\{N\neq0,\ B^2=0\}.
$$

On the sector the eigenvalues are $\lambda_\pm=Q_t\pm iB$, both non-zero, and $\langle\tilde Q\rangle_{\natural}=\lambda_+\lambda_-$.

*Proof.* The two cells are the intersections of the sector with the complement and with the zero set of $B^2$. The eigenvalues satisfy $\lambda_++\lambda_-=2Q_t$ and $\lambda_+\lambda_-=Q_t^2+B^2=N$, so neither vanishes when $\langle\tilde Q\rangle_{\natural}\neq0$.

**Theorem (the two types).**

(i) On $\Sigma_{11}$ the eigenvalues are distinct and non-zero; $\tilde Q$ is diagonalisable, with a unique two-term spectral decomposition $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ into orthogonal idempotents.

(ii) On $\Sigma_{10}$ the two eigenvalues coincide at the value $Q_t$, which is non-zero on the cell. The element is either the scalar $Q_t e_t$, with minimal polynomial $X-Q_t$, or a Jordan element $Q_t e_t+\vec\Upsilon$ with $\vec\Upsilon\neq0$ and $\vec\Upsilon^2=0$, with minimal polynomial $(X-Q_t)^2$; the second is not diagonalisable.

*Proof.* The discriminant is $-4B^2$, so it vanishes exactly on $\Sigma_{10}$. On $\Sigma_{10}$ the element is $Q_te_t+\vec\Upsilon$ with $\vec\Upsilon^2=0$, and the centraliser is the algebra of dual numbers, whose only idempotents are $0$ and $e_t$; hence there is no non-trivial spectral decomposition off the scalar line (*Relations between Quaternionic Norm and Spectral Regularity and Degeneracy*, §*The Two Decompositions*).

**Definition.** The **scalar line** and the **Jordan cone** of the sector are

$$
\Sigma_{10}^{\mathrm{s}}=\mathbb{C}^{\times}e_t,\qquad
\Sigma_{10}^{\mathrm{J}}=\{Q_t(e_t+\vec\Upsilon):Q_t\in\mathbb{C}^{\times},\ \vec\Upsilon\in\mathcal{N}_{\mathrm p}\},
$$

with $\mathcal{N}_{\mathrm p}=\{\vec\Upsilon\neq0:\vec\Upsilon^2=0\}$ the pure stratum of the null cone.

**Theorem (the shapes of the halves).** The cell $\Sigma_{11}$ is open and dense in $\mathbb{B}$, of real dimension eight, and connected. The cell $\Sigma_{10}$ is closed in $\mathbb{B}^{\times}$, of real dimension six, and connected; it is the disjoint union of the scalar line and the Jordan cone. The sector is connected: $\Sigma_{11}$ is connected and dense, and every point of $\Sigma_{10}$ lies in its closure. The spectral split is a stratification, not a partition into two open halves.

*Proof.* $\Sigma_{11}$ is the complement of the union of the two closed cones $\mathcal{N}$ and $\mathcal{S}$, each of real codimension two; the complement is open and dense, and it is connected because the removal of a closed subset of codimension at least two from a connected manifold leaves a connected manifold. $\Sigma_{10}$ is the trace on the sector of the closed cone $\mathcal{S}$, hence closed in the sector. It is the union of the connected scalar line and the connected Jordan cone, and the closure of the Jordan cone contains the scalar line; hence it is connected. Its real dimension is that of $\mathcal{S}\setminus\mathcal{N}$, namely six.

**Theorem (multiplication does not follow the spectrum).** Neither cell is closed under multiplication, and both are stable under inversion.

*Proof.* Inversion preserves the eigenvalues, hence preserves each cell. For the products, put $\nu_1=\vec e_x+i\vec e_y$ and $\nu_2=\vec e_x+i\vec e_z$. Both are square-zero, so $e_t+\nu_1$ and $e_t+\nu_2$ lie in $\Sigma_{10}$; their product is

$$
(e_t+\nu_1)(e_t+\nu_2)=\vec e_x,
$$

which has $B^2=1$ and lies in $\Sigma_{11}$. In the other direction, $e_t+\vec e_x$ and $e_t-\vec e_x$ lie in $\Sigma_{11}$, and their product is $2e_t$, which lies in $\Sigma_{10}$.

**Remark (the exponential on the cell).** The exponential carries the scalar line onto itself, and

$$
\exp\bigl(\mathbb{C}e_t+\{\vec\Upsilon:\vec\Upsilon^2=0\}\bigr)=\Sigma_{10}.
$$

Indeed $\exp(a e_t+\vec\Upsilon)=e^a(e_t+\vec\Upsilon)$ for $\vec\Upsilon^2=0$, and every element of $\Sigma_{10}$ is of that form (*Biquaternion Elementary Functions*, §*The Logarithm*).

**Remark (why the split is not a second sector).** The norm split is multiplicative and inversion-stable, and it is the partition that the group law follows. The spectral split is inversion-stable but not multiplicative: a product of two spectrally degenerate units can be spectrally regular, and a product of two spectrally regular units can be degenerate. It is therefore a stratification of the sector, not a second partition of the algebra at the same level. The four-cell grid is the simultaneous refinement, and its two regular cells are the two halves above.

## Comparison with the N-Degenerate Sector

The two sectors are complementary, and the comparison is the content of the norm partition.

| | $\mathbb{B}^{\times}$, the $\natural$-regular sector | $\mathcal{N}$, the $\natural$-degenerate sector |
|---|---|---|
| condition | $\langle\tilde Q\rangle_{\natural}\neq0$ | $\langle\tilde Q\rangle_{\natural}=0$ |
| real dimension | $8$ | $6$ |
| topology | open and dense, connected, $\simeq S^1\times S^3$ | closed cone, contractible, singular at the apex |
| multiplication | group | semigroup with absorbing $0$, no identity |
| inverse | two-sided | none |
| matrix model | invertible, rank $2$ | rank at most $1$ |
| polar factors | $\tilde Q_H$ positive definite, $\tilde Q_0$ unitary | $\tilde Q_H$ positive semidefinite of rank one, $\tilde Q_0$ a partial isometry |
| spectrum | $\lambda_\pm\neq0$ | $0$ is an eigenvalue |
| boundary | $\partial\mathbb{B}^{\times}=\mathcal{N}$ | the cone is the boundary |

**Theorem (the boundary).** The cone is the boundary of the sector, and it has empty interior:

$$
\partial\mathbb{B}^{\times}=\mathcal{N},\qquad
\operatorname{int}\mathcal{N}=\varnothing.
$$


*Proof.* The sector is open and dense, and its complement is the cone.

**Remark (the two halves of the algebra).** The partition is by the value of one multiplicative invariant. It is a partition that the product and the inverse respect: a product of two units is a unit, a product of a unit and a non-unit is a non-unit, and the inverse of a unit is a unit. The finer partitions by the spectrum do not have this property, and they are treated as stratifications inside each sector.

## Consequences

The sector is the domain of the group law, of the polar decomposition, of the logarithm and of the determinant sequence. Its norm is onto $\mathbb{C}^{\times}$, its norm-one fibre is $SL_2(\mathbb{C})$, and its centre is the scalars.

The sector retracts onto $\mathrm{U}(2)\cong(S^1\times S^3)/\{\pm e_t\}$. The fundamental group is infinite cyclic and is carried by the phase; the universal cover is $\mathbb{R}\times S^3$. The Euclidean sphere is not a group and is not the compact part of the sector; the compact part is the unitary group.

The spectral condition cuts the sector into an open dense cell and a closed thin cell. The open cell is the generic case of distinct eigenvalues; the thin cell is the union of the scalar line and the Jordan cone. Neither is a subsemigroup, and the sector remains connected across both. The detailed study of the two cells is the subject of *The N-Regular, Spectrally Regular Sector* and *The N-Regular, Spectrally Degenerate Sector*.

The boundary of the sector is the null cone. The two articles together carry the norm partition: this one the invertible half, *The N-Degenerate Sector* the half on which the norm vanishes.

## Summary

The $\natural$-regular sector is the non-zero set of the quaternionic norm, $\mathbb{B}^{\times}=\{N\neq0\}$, and it is exactly the group of units of the plain product. Its inverse is $\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$; it is open and dense, of real dimension eight, with boundary the null cone $\mathcal{N}$.

Under the matrix model it is $GL_2(\mathbb{C})$, the norm is the determinant, and the norm-one group is $SL_2(\mathbb{C})$. The norm is a surjective homomorphism onto $\mathbb{C}^{\times}$, with the determinant sequence $1\to SL_2(\mathbb{C})\to GL_2(\mathbb{C})\to\mathbb{C}^{\times}\to1$; the sequence does not split along the centre, and the multiplication map $\mathbb{C}^{\times}e_t\times SL_2(\mathbb{C})\to\mathbb{B}^{\times}$ is a connected two-to-one covering.

The sector is connected and non-compact and retracts onto $\mathrm{U}(2)\cong(S^1\times S^3)/\{\pm e_t\}$; its homotopy groups are $\mathbb{Z},0,\mathbb{Z}$ and its universal cover is $\mathbb{R}\times S^3$. The exponential is onto, and no continuous single-valued logarithm exists on the sector.

The spectrum does not split the sector into two open halves. The spectrally regular units form an open dense cell of real dimension eight, the spectrally degenerate units a closed cell of real dimension six, the union of the scalar line and the Jordan cone. Both cells are inversion-stable, neither is product-stable, and the sector is connected. The two cells are studied in their own articles; this article owns the sector that contains them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, complex dimension four, real dimension eight |
| $\tilde Q=Q_te_t+\vec Q$ | an element and its scalar–vector split |
| $\tilde Q^{\natural}=Q_t-\vec Q$ | the natural conjugation |
| $\tilde Q^{*}=\overline{Q_t}-\overline{\vec Q}$ | the Hermitian conjugation |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the quaternionic norm, multiplicative and complex-valued |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part |
| $\mathbb{B}^{\times}=\{N\neq0\}$ | the $\natural$-regular sector, the group of units |
| $\mathbb{B}^{\times}_1=\{N=1\}$ | the norm-one group, the unit factor; $SL_2(\mathbb{C})$ |
| $\mathcal{N}=\{N=0\}$ | the null cone, the $\natural$-degenerate sector |
| $\mathcal{S}=\{B^2=0\}$ | the spectral-degenerate cone |
| $\Sigma_{11}=\{N\neq0,\ B^2\neq0\}$ | the spectrally regular units |
| $\Sigma_{10}=\{N\neq0,\ B^2=0\}$ | the spectrally degenerate units |
| $\Sigma_{10}^{\mathrm{s}}=\mathbb{C}^{\times}e_t$ | the scalar line |
| $\Sigma_{10}^{\mathrm{J}}$ | the Jordan cone, $Q_t(e_t+\vec\Upsilon)$ with $\vec\Upsilon^2=0$ |
| $\mathcal{N}_{\mathrm p}=\{\vec\Upsilon\neq0:\vec\Upsilon^2=0\}$ | the pure stratum of the null cone |
| $\mathsf{M}_2(\tilde Q)$ | the $2\times2$ matrix model; $\det=N$ |
| $\mathrm{U}(\mathbb{B})=\{\tilde Q^{*}\tilde Q=e_t\}\cong \mathrm{U}(2)$ | the maximal compact subgroup |
| $\tilde Q=\tilde Q_H\tilde Q_0$ | the polar decomposition; $\tilde Q_H$ positive definite, $\tilde Q_0$ unitary |

## Further Reading

- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm, the criterion, the inverse formula and the two cases
- [The N-Degenerate Sector](the-n-degenerate-sector.html), for the partner article and the null cone
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the modulus, the four factors and the group of units
- [The N-Regular, Spectrally Regular Sector](the-n-regular-spectrally-regular-sector.html), for the open dense cell
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the scalar line and the Jordan cone
- [Relations between Quaternionic Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the four cells and the chain of invariants
- [The Biquaternion Unit Group as a Topological Group](the-biquaternion-unit-group-as-a-topological-group.html), for the determinant sequence, the centre and the covering
- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html), for the polar retraction, the homotopy groups and the universal cover
- [The Topology of the Zero-Divisor Cone](the-topology-of-the-zero-divisor-cone.html), for the boundary of the sector and its link
- [$M_2(\mathbb{C})$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant](m2c-representation-gl2-sl2-and-the-determinant.html), for the matrix model and the determinant
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential and the logarithm
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed. 2015).
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002).
