
# __Split-Quaternion Null Quadric and Projective Geometry__

## Introduction

The split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$ carries a non-degenerate quadratic form of signature $(2,2)$, the split-quaternion norm $N(\tilde q) = q_0^2 + q_1^2 - q_2^2 - q_3^2$, of signature $(2,2)$. Its zero set, the **null cone**, is the zero-divisor set together with the origin, and its projectivisation is a smooth quadric surface in $\mathbb{P}^3$. This article describes the null cone, the two families of isotropic lines, the rank-one description of its nonzero points, the Segre embedding of the quadric, the doubly ruled description of the quadric, and the relations to the projective geometry of the biquaternions and to the Lorentzian geometry of the vector subspace.

The article owns the projective and quadric structure of the algebra. It relies on *Split-Quaternion Norm and Invertibility* for the form and the units, on *Split-Quaternion Zero Divisors* for the null structure, on *Split-Quaternion Topology* for the link and the rulings as topological objects, and on *Split-Quaternion Geometry* for the geometric reading. The split-quaternion norm and its polarisation are developed in *Split-Quaternion Norm and Invertibility* and are used here only geometrically. No physics is invoked.

**Conventions.** Coordinates are $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with $N = q_0^2+q_1^2-q_2^2-q_3^2$ and polarisation $B(\tilde q,\tilde p) = q_0 p_0 + q_1 p_1 - q_2 p_2 - q_3 p_3$, whose matrix in the basis $1, e_1, e_2, e_3$ is $G = \operatorname{diag}(1,1,-1,-1)$, so that $B(\tilde q,\tilde p) = X^{\mathsf{T}} G Y$ for the coordinate columns $X, Y$. The vector subspace is $V = \operatorname{span}\{e_1,e_2,e_3\}$ with $N|_V = q_1^2-q_2^2-q_3^2$. The projective space of $\mathbb{H}_{\mathrm{s}}$ is $\mathbb{P}^3 = \mathbb{P}(\mathbb{H}_{\mathrm{s}})$.

## The Null Cone

**Definition.** The **null cone** is the quadric

$$
\mathcal{N} = \{\, \tilde q \in \mathbb{H}_{\mathrm{s}} : N(\tilde q) = 0 \,\} = \{\, q_0^2 + q_1^2 = q_2^2 + q_3^2 \,\},
$$

the union of the origin and the zero divisors.

**Theorem.** The null cone is a real cone of dimension $3$, singular only at its vertex $0$; away from the origin it is a smooth three-manifold, and it is the boundary between the two components $\{N>0\}$ and $\{N<0\}$ of the group of units. Its projectivisation $\mathbb{P}(\mathcal{N}) \subset \mathbb{P}^3$ is a smooth quadric surface.

**Proof.** The form has signature $(2,2)$, so it is indefinite and non-degenerate; the cone is the zero set of a non-degenerate quadratic form, hence a cone of dimension $3$ with smooth part the complement of the vertex. The gradient $2GX$ vanishes only at the origin, so the projective quadric is smooth.

Restricted to the vector subspace $V$, where $q_0 = 0$, the null cone meets $V$ in the **Minkowski light cone** $q_1^2 = q_2^2 + q_3^2$, a cone of dimension $2$ in $V$; the intersection $\mathcal{N} \cap V$ is the light cone of the Lorentzian geometry of $V$.

## The Two Families of Isotropic Lines

**Definition.** An **isotropic** subspace is a subspace on which $N$ (equivalently $B$) vanishes identically; a **maximal isotropic** subspace is one not properly contained in another.

**Theorem.** The form has Witt index $2$: every maximal isotropic subspace has dimension $2$. The maximal isotropic planes fall into two families

$$
\mathcal{L} = \{\, L_\lambda : \lambda \in \mathbb{P}^1 \,\}, \qquad \mathcal{M} = \{\, M_\mu : \mu \in \mathbb{P}^1 \,\},
$$

each parametrised by a projective line; the two families are disjoint, every maximal isotropic plane lies in exactly one of them, and their union is the null cone. In the examples,

$$
L = \operatorname{span}\Bigl\{ \tfrac12(1+e_2),\; e_1+e_3 \Bigr\}
$$

is a member of one family, with both generators null and mutually $B$-orthogonal.

**Proof.** A totally isotropic subspace of a non-degenerate form of signature $(2,2)$ has dimension at most $2$; the displayed plane shows the bound is attained, so the Witt index is $2$. That the maximal isotropic planes form exactly two projective lines follows from the classification of the maximal isotropic subspaces of $O(2,2)$, which is the split orthogonal group of a four-dimensional form; the two families are the two $O(2,2)$-orbits, exchanged by an isometry of determinant $-1$, such as $e_2 \mapsto -e_2$.

**Remark (isotropic lines versus isotropic planes).** In the vector space the isotropic objects are the two-dimensional planes; in the projective space $\mathbb{P}^3$ the images of these planes are **lines**, and it is in this projective sense that one speaks of the two families of isotropic lines on the quadric. The distinction between "isotropic plane" in the vector space and "isotropic line" in the projective space is one of dimension bookkeeping and is kept explicit here.

## The Rank-One Description

**Theorem.** Under the identification $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$ of *Split-Quaternion Algebra*, the nonzero null elements are exactly the matrices of rank one:

$$
\{\, \tilde q \neq 0 : N(\tilde q) = 0 \,\} \longleftrightarrow \{\text{matrices of rank } 1\}.
$$

Every such element is an outer product

$$
\tilde q = u v^{\mathsf{T}}, \qquad u = \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \neq 0, \qquad v = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} \neq 0,
$$

determined by the pair $(u,v)$ up to $(u,v) \mapsto (\lambda u, \lambda^{-1} v)$ with $\lambda \in \mathbb{R}^\times$. Fixing $u$ and varying $v$ traces one of the two families of isotropic lines, and fixing $v$ and varying $u$ traces the other; each family is therefore a projective line, in agreement with *Split-Quaternion Zero Divisors*, §*The Two Families*.

**Proof.** The determinant of the image of $\tilde q$ is $N(\tilde q)$ by *Split-Quaternion Norm and Invertibility*, so $\tilde q$ is null exactly when its image is a singular matrix; a nonzero singular $2\times2$ matrix has rank exactly one, hence is an outer product $uv^{\mathsf{T}}$ of nonzero columns, and the pair $(u,v)$ is determined only up to the stated rescaling. An outer product satisfies $uv^{\mathsf{T}} = \lambda u\,(\lambda^{-1} v)^{\mathsf{T}}$, so the two factors are defined up to this rescaling. Fixing $u$ leaves a one-parameter family of outer products whose span is an isotropic plane, and fixing $v$ leaves the other; the two are exchanged by transposition, so they are the two families of the previous section.

## The Segre Embedding and the Projective Null Quadric

**Theorem.** The projective quadric $Q = \mathbb{P}(\mathcal{N}) \subset \mathbb{P}^3$ is, up to a projective transformation, the image of the **Segre embedding**

$$
\sigma : \mathbb{P}^1 \times \mathbb{P}^1 \longrightarrow \mathbb{P}^3, \qquad ([s:t],[u:v]) \longmapsto (su : sv : tu : tv),
$$

whose image is the smooth quadric surface $\{q_0 q_3 - q_1 q_2 = 0\}$. The two factors of $\mathbb{P}^1\times\mathbb{P}^1$ are the two families of isotropic lines, and $Q \cong \mathbb{P}^1 \times \mathbb{P}^1$.

**Proof.** Over $\mathbb{R}$ the form $N$ of signature $(2,2)$ is linearly equivalent to $q_0q_3 - q_1q_2$: the change of variables

$$
q_0 = q_0 + q_1 + q_2 + q_3, \quad q_1 = q_0 - q_1 + q_2 - q_3, \quad q_2 = -q_0 + q_1 + q_2 - q_3, \quad q_3 = q_0 + q_1 - q_2 - q_3
$$

sends $q_0q_3 - q_1q_2$ to $2(q_0^2+q_1^2-q_2^2-q_3^2)$, a nonzero multiple of $N$, so the two quadrics are projectively equivalent; and the image of the Segre map is exactly $\{q_0q_3 = q_1q_2\}$, a smooth quadric surface with the two rulings given by fixing one of the two factors. The identification of the two rulings with the two families of isotropic lines is the statement of the previous section read projectively.

The Segre embedding makes the two families explicit: fixing $[s:t]$ and letting $[u:v]$ vary traces one isomorphism $\mathbb{P}^1 \to Q$ whose image is an isotropic line of one family, and fixing $[u:v]$ and varying $[s:t]$ traces the other family.

## The Ruled-Surface Description

**Theorem.** The quadric $Q$ is a doubly ruled surface: through every point pass exactly two isotropic lines, one from each family, and the two rulings are the two factors of the product $\mathbb{P}^1 \times \mathbb{P}^1$.

**Proof.** The Segre embedding is a bijection of $\mathbb{P}^1\times\mathbb{P}^1$ onto $Q$, and the two families of coordinate lines of the product map to the two families of isotropic lines of $Q$; each point of the product lies on exactly one line of each family.

Thus the projective quadric is determined by its two rulings, and the parametrisation of the rulings by $\mathbb{P}^1$ is the split, real analogue of the corresponding description of the biquaternion quadric.

## The Relation to the Projective Geometry of $\mathbb{B}$

The biquaternion article *Biquaternion Topology* treats the null quadric of the complex form on $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of complex signature $(4,0)$ and split over $\mathbb{C}$, whose projective quadric is a smooth quadric in $\mathbb{P}^3_{\mathbb{C}}$. The real split-quaternion quadric is the real form of the same projective object: the algebra $\mathbb{H}_{\mathrm{s}}$ is a real form of $M_2(\mathbb{C}) \cong \mathbb{B}$ under complexification, and the real quadric $Q = \mathbb{P}(\mathcal{N})$ is the real locus of the complex quadric. The Segre embedding, the two rulings and the ruled-surface description are common to both; what differs is the reality condition — the split-quaternion quadric is a real doubly ruled surface with real lines, whereas the biquaternion quadric over $\mathbb{R}$ has a reality structure from the complex conjugation. No biquaternion-specific object — the central imaginary unit $i$, the Hermitian reality condition, the definite form on the quaternion half — is imported; only the projective shape is shared.

## The Relation to the Lorentzian Geometry

The same form determines two geometries, and the two-dimensional isotropic structure above is the common source.

**The projective geometry on the algebra.** The isometry group of $N$ is $O(2,2)$, of dimension $6$; its action on $\mathbb{P}^3$ preserves the quadric $Q$ and permutes its two rulings, with the identity component $\mathrm{SO}^{+}(2,2)$ preserving each ruling. The group of units acts through $\mathrm{PGL}_2(\mathbb{R}) \cong SO(2,1) \subset SO(2,2)$, the algebra automorphisms of *Split-Quaternion Automorphisms and Derivations*, which is the subgroup fixing the projective point $\mathbb{P}(S)$ of the scalar line and the plane at infinity.

**The Lorentzian geometry on the vector subspace.** The restricted form $N|_V = q_1^2-q_2^2-q_3^2$ of signature $(2,1)$ has null cone $q_1^2 = q_2^2 + q_3^2 = \mathcal{N}\cap V$; its isometry group is $O(2,1)$, and its projectivisation is the conic $\mathbb{P}(\mathcal{N}\cap V) \subset \mathbb{P}^2$, the absolute of the hyperbolic plane. This is the Lorentzian geometry of the vector subspace developed in *Split-Quaternion Geometry* and *Split-Quaternions and Hyperbolic Geometry*: the two isotropic lines of the conic are the two points at infinity of the hyperbolic plane, and the Lorentzian geometry of Part II of the corpus is exactly the geometry of this conic.

## Summary

The split-quaternion norm $N(\tilde q) = q_0^2+q_1^2-q_2^2-q_3^2$ is a form of signature $(2,2)$, with polarisation $B$ and matrix $G = \operatorname{diag}(1,1,-1,-1)$; the conjugation is the antiautomorphism with $\tilde q\tilde{q}^{\natural} = N(\tilde q)$. Its zero set is the null cone, a three-dimensional cone singular at the origin and smooth elsewhere, whose projectivisation $Q \subset \mathbb{P}^3$ is a smooth quadric surface. Under the identification $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$ the nonzero null elements are exactly the rank-one matrices, each an outer product $uv^{\mathsf{T}}$ of nonzero columns, determined up to $(\lambda u, \lambda^{-1}v)$. The form has Witt index $2$: the maximal isotropic subspaces are two-dimensional, forming the two families of isotropic planes, each parametrised by a projective line and each becoming a family of isotropic *lines* on $Q$. The quadric is the image of the Segre embedding $\mathbb{P}^1\times\mathbb{P}^1 \to \mathbb{P}^3$, hence $\cong\mathbb{P}^1\times\mathbb{P}^1$, and equivalently it is the doubly ruled surface $\mathbb{P}^1\times\mathbb{P}^1$, the two rulings being the two factors. The group $O(2,2)$ acts on the quadric and permutes the rulings, with the algebra automorphisms $\mathrm{PGL}_2(\mathbb{R}) \cong SO(2,1)$ as the subgroup fixing the scalar point; the restriction to $V$ gives the Minkowski conic and the Lorentzian geometry of the hyperbolic plane. The projective structure is the real form of the biquaternion quadric, differing only in the reality condition.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $N(\tilde q) = q_0^2+q_1^2-q_2^2-q_3^2$ | the split-quaternion norm, signature $(2,2)$ | *Split-Quaternion Norm and Invertibility* |
| $B(\tilde q,\tilde p)$, $G = \operatorname{diag}(1,1,-1,-1)$ | the polarisation and its matrix | this article |
| $\mathcal{N} = \{N=0\}$ | the null cone / zero-divisor set | *Split-Quaternion Zero Divisors* |
| $uv^{\mathsf{T}}$ | the rank-one (outer-product) form of a nonzero null element | this article |
| $\mathcal{L}, \mathcal{M}$ | the two families of maximal isotropic planes | this article |
| $Q = \mathbb{P}(\mathcal{N}) \subset \mathbb{P}^3$ | the projective null quadric | this article |
| $\sigma$, $\mathbb{P}^1\times\mathbb{P}^1$ | the Segre embedding and its image $\{q_0q_3-q_1q_2=0\}$ | this article |
| $O(2,2)$, $\mathrm{SO}^{+}(2,2)$ | the isometry group of the form and its identity component | this article |
| $O(2,1)$, $\mathrm{SO}^{+}(2,1)$ | the Lorentz group of the restricted form on $V$ | *Split-Quaternion Rotations and the Lorentz Group* |

## Further Reading

- Joe Harris, *Algebraic Geometry: A First Course*, Graduate Texts in Mathematics 133 (Springer, 1992), for the Segre embedding, the rulings of a smooth quadric surface and the rank-one locus.
- Miles Reid, *Undergraduate Algebraic Geometry*, London Mathematical Society Student Texts 12 (Cambridge University Press, 1988), for quadrics in $\mathbb{P}^3$ and their two rulings.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the isotropic subspaces and the Witt index of an indefinite form.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the Witt index, the split form and the classification of quadratic forms.
- John Stillwell, *The Four Pillars of Geometry* (Springer, 2005), for the projective and hyperbolic readings of a conic and a quadric.
