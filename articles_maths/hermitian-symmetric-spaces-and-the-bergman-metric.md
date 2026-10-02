
# __Hermitian Symmetric Spaces and the Bergman Metric__

## Introduction

A **Hermitian symmetric space** is a connected complex manifold with a Hermitian metric such that every point is an isolated fixed point of an involutive holomorphic isometry — the geodesic symmetry — the Hermitian refinement of a Riemannian symmetric space in which the symmetry is holomorphic and the metric is compatible with the complex structure. The model is the bounded symmetric domain: a bounded domain $\Omega \subseteq \mathbb{C}^n$ such that every point is an isolated fixed point of an involutive holomorphic automorphism of $\Omega$. Such a domain carries a canonical metric, the **Bergman metric**
$$
g^{\mathrm{B}}_{i\bar j} = \partial_i\bar\partial_j \log K(z,z) ,
$$
built from the Bergman kernel $K$ of the domain; it is Kähler, it is invariant under every holomorphic automorphism, and it makes $\Omega$ a Hermitian symmetric space of noncompact type. The connection is a theorem of both directions: every bounded symmetric domain is a Hermitian symmetric space of noncompact type with the Bergman metric as its invariant metric, and every Hermitian symmetric space of noncompact type is realised as a bounded symmetric domain, its **Harish-Chandra embedding**. The compact and noncompact types, the flat factor and the classification of Cartan are the classification of the geometry that the Bergman metric defines.

The article has three sections: the Hermitian symmetric spaces and their symmetries; the bounded symmetric domains and the Bergman metric; and the classification and the two types. The Riemannian symmetric spaces, the geodesic symmetry and the symmetric pair $(G,K)$ are *Symmetric Spaces*, and the Hermitian symmetric case with its group and the compact/noncompact duality is *The Unitary Group and the Hermitian Symmetric Space*, both in *Geometry on Groups*, earlier in this Part; the Bergman kernel and projection are *The Bergman Operator*, the earlier article of this category; the Hermitian metric, the Kähler condition and the curvature are *Hermitian Geometry and Almost Complex Structures*, *Kähler Geometry*, *Kähler Manifolds and the Hermitian Form* and *The Curvature Operator of a Complex Manifold*; the unitary group, the Hermitian forms and the unitary frames are *Hermitian Geometry and the Unitary Group*, and the automorphism group of a bounded domain is the group-theoretic subject of *The Unitary Group and the Hermitian Symmetric Space*. None of that is re-derived.

Throughout, $M$ is a connected complex manifold of complex dimension $n$ with a Hermitian metric $g$, $s_p$ is the geodesic symmetry at $p$, $\Omega \subseteq \mathbb{C}^n$ is a bounded domain, $K$ is its Bergman kernel and $g^{\mathrm B}$ its Bergman metric, and $G$ is the identity component of the holomorphic automorphism group of $\Omega$ with $H$ the stabiliser of a point.

## Hermitian Symmetric Spaces

**Definition.** A **Hermitian symmetric space** is a connected complex manifold $M$ with a Hermitian metric $g$ such that for every $p \in M$ there is an involutive holomorphic isometry $s_p$ with $p$ as an isolated fixed point,
$$
s_p^2 = \mathrm{id}, \qquad s_p(p) = p, \qquad (ds_p)_p = -\mathrm{id}_{T_pM} .
$$
The map $s_p$ is the **geodesic symmetry** at $p$, and the condition that $M$ be Riemannian symmetric together with the Hermitian compatibility makes $M$ a **Kähler manifold**.

**Proposition (the operator form of the condition).** A Riemannian symmetric space with a complex structure $J$ is Hermitian symmetric exactly when $J$ is parallel for the metric, $\nabla J = 0$, and $J$ is invariant under the geodesic symmetries, $(s_p)_{*}J = J$; equivalently, when the Riemannian symmetric space is Kähler and the geodesic symmetry is holomorphic.

**Proof.** A Riemannian symmetric space has $\nabla R = 0$ and geodesic symmetries; the complex structure $J$ is Hermitian when $g(JX,JY) = g(X,Y)$, and the compatibility of the symmetric structure with $J$ is the invariance of the $(1,1)$-tensor $J$ under the transvections $\nabla$-parallel transport, which is $\nabla J = 0$; a parallel $J$ of square $-\mathrm{id}$ is a Kähler structure, and the symmetries, commuting with the parallel transport, preserve it. The Kähler condition is *Kähler Geometry*, the symmetric structure and $\nabla R = 0$ are *Symmetric Spaces*.

**Proposition (the group form of the condition).** A Hermitian symmetric space is a homogeneous space $M = G/H$ with $G$ the identity component of the isometry group and $H$ the stabiliser of a point, $H$ compact for the noncompact type; the complex structure comes from an element $J_0$ of the centre of the Lie algebra $\mathfrak{h}$ of $H$ with $J_0^2 = -\mathrm{id}$ on the tangent space, and the isotropy representation of $H$ on $T_pM$ is complex-linear for it.

**Proof.** The isometry group of a Riemannian symmetric space acts transitively and the stabiliser is the identity component of the fixed-point group of $s_p$, a compact subgroup in the noncompact type; the invariance of $J$ under $H$ is the Hermitian condition, and a $H$-invariant complex structure on the tangent space at $p$ is the same as an element of the centre of $\mathfrak h$ with the right square, by Schur's lemma for the isotropic representation. This is *The Unitary Group and the Hermitian Symmetric Space*.

**Remark (the two characteristics).** The two conditions in the propositions are the two available descriptions: the metric one, in which the symmetry $s_p$ is a holomorphic isometry and the operator $J$ is parallel, and the group one, in which the complex structure is a central element of the isotropy algebra. They are the same structure, and the bounded domains of the next section are the metric description; the compact symmetric spaces of the next-to-last section are the group description.

## Bounded Symmetric Domains and the Bergman Metric

**Definition.** A **bounded symmetric domain** is a bounded domain $\Omega \subseteq \mathbb{C}^n$ such that for every $p \in \Omega$ there is a holomorphic automorphism $s_p$ of $\Omega$, involutive, with $p$ as an isolated fixed point. Its **Bergman metric** is
$$
g^{\mathrm B}_{i\bar j}(z) = \partial_i\bar\partial_j \log K(z,z),
$$
where $K$ is the Bergman kernel of $\Omega$; the norm is invariant under the holomorphic automorphisms and is a Kähler metric.

**Theorem (the Bergman metric is Kähler, invariant and complete).** On a bounded symmetric domain $\Omega$ the Bergman metric is a Kähler metric, positive definite, invariant under every holomorphic automorphism of $\Omega$, and complete; the domain with the Bergman metric is a Hermitian symmetric space, and its geodesic symmetry at $p$ is the involutive automorphism $s_p$.

**Proof.** Positivity is the positive definiteness of the Bergman kernel: for the holomorphic $f = \sum_i c_i K(\cdot,z_i)$ one has $\sum_{i,j}c_i\bar c_j K(z_i,z_j) = \|f\|^2 \ge 0$ with equality only for $f = 0$, which by a Taylor expansion at $z$ gives positive definiteness of $\partial\bar\partial\log K$ (the strict positivity of the Bergman kernel of a domain is a theorem of its own, quoted). Invariance is the transformation law $K_{\Omega}(z,w) = \det F'(z)K_{\Omega}(Fz,Fw)\overline{\det F'(w)}$ of *The Bergman Operator*: the factor is holomorphic, so $\log K(Fz,Fz) - \log K(z,z)$ is the real part of a holomorphic function, and the metric, which is $\partial\bar\partial$ of the logarithm, is unchanged. Completeness and the realisation as a symmetric space are the theorem of Harish-Chandra, quoted: a bounded homogeneous domain carrying an involutive automorphism at each point has the Bergman metric complete and the symmetry realised by $s_p$. The kernel, the transformation law and the positivity are *The Bergman Operator* and *Reproducing Kernel Hilbert Spaces*.

**Corollary (the automorphisms are isometries).** The group $G$ of holomorphic automorphisms of $\Omega$ acts on $\Omega$ by Bergman isometries, transitively when $\Omega$ is a bounded symmetric domain; the stabiliser $H$ of a point is the compact subgroup of the unitary transformations of $T_p\Omega$ arising from the complex-linear automorphisms fixing $p$, and $\Omega = G/H$.

**Proof.** The invariance of the metric under every holomorphic automorphism is the transformation law; the transitivity of the automorphism group of a bounded symmetric domain is the theorem of Cartan quoted, that a bounded symmetric domain is homogeneous; the stabiliser is compact because it fixes a point and acts by an isometry group of the compact tangent ball, and the complex-linear part of it is a closed subgroup of the unitary group. This is the automorphism statement of *The Unitary Group and the Hermitian Symmetric Space*.

**Example (the unit disc and the polydisc).** The unit disc $\mathbb{D} \subseteq \mathbb{C}$ with the Bergman metric $g^{\mathrm B}_{z\bar z} = c\,(1-|z|^2)^{-2}$ for the positive constant $c$ fixed by the normalisation of the Bergman kernel of *The Bergman Operator* is the hyperbolic disc of constant negative curvature; its holomorphic automorphisms are the Möbius transformations $z \mapsto e^{i\theta}(z-a)/(1-\bar a z)$, which are exactly its Bergman isometries. The polydisc $\mathbb{D}^n$ is a bounded symmetric domain whose Bergman metric is the product of the disc metrics, a Hermitian symmetric space of noncompact type which is not irreducible; the ball $\mathbb{B}^n$ with the Bergman metric is the irreducible one, of rank one.

## The Classification and the Two Types

**Theorem (the two types and the flat factor).** A Hermitian symmetric space with no Euclidean factor decomposes as a product of a **compact type** and a **noncompact type**, dual to one another; the noncompact type is realised as a bounded symmetric domain with its Bergman metric, and the compact type as the compact dual of that domain, a simply connected compact Kähler manifold with positive curvature and with the same complex dimension.

**Proof.** The duality of compact and noncompact symmetric spaces is the general Lie-theoretic duality of *Symmetric Spaces*: complexifying the Lie algebra of a noncompact Hermitian symmetric space and taking the compact real form produces the compact dual, and the two have the same complexification of the isotropy representation; the noncompact side is the bounded domain of Harish-Chandra and the compact side is its compact dual, the two being the two real forms of the same complex symmetric space. The metric realisation of the noncompact side is the previous section. This is *The Unitary Group and the Hermitian Symmetric Space*.

**Theorem (Cartan's classification).** The irreducible bounded symmetric domains, equivalently the irreducible Hermitian symmetric spaces of noncompact type, fall into four infinite families and two exceptional domains: the domains of type I, the bounded symmetric domains whose compact dual is a complex Grassmannian; of type II, the symmetric ones inside type I; of type III, those whose compact dual is a Lagrangian Grassmannian; of type IV, the Lie balls; and the two exceptional domains of dimensions $16$ and $27$.

**Proof.** The classification is the classification of the real simple Lie algebras with a centre in the isotropy algebra, equivalently of the Hermitian symmetric pairs $(\mathfrak g, \mathfrak k)$, which is Cartan's list; the four families are the classical ones $A_n, B_n, C_n, D_n$ and the two exceptions are the $E_6$ and $E_7$ cases. The classification and the list are *The Unitary Group and the Hermitian Symmetric Space*, and the domains appear here only as the noncompact realisations; the rank of the domain is the rank of the symmetric space.

**Remark (the operator and the metric).** The Bergman metric is an operator object in the sense of the category: it is built from the Bergman operator of the domain by applying $\partial\bar\partial\log$ to the diagonal of the kernel, and its invariance, completeness and Kähler-Einstein property are the geometric facts that make the domain a symmetric space. The metric is Kähler–Einstein, $\rho = \lambda\Omega$ with the same $\lambda$, and the curvature is negative for the noncompact type and positive for the compact dual, which is the operator content of the duality.

## Summary

A Hermitian symmetric space is a connected complex manifold with a Hermitian metric admitting an involutive holomorphic isometry $s_p$ with $p$ as isolated fixed point; equivalently it is a Riemannian symmetric space that is Kähler with $\nabla J = 0$, and equivalently a homogeneous space $G/H$ whose complex structure comes from a central element of the isotropy algebra. A bounded symmetric domain is a bounded domain with an involutive automorphism at each point; its Bergman metric $g^{\mathrm B}_{i\bar j} = \partial_i\bar\partial_j\log K(z,z)$, built from the Bergman kernel of *The Bergman Operator*, is Kähler, positive definite, invariant under every holomorphic automorphism and complete, so the domain with it is a Hermitian symmetric space of noncompact type, and the automorphism group acts transitively by isometries with compact stabiliser. Every Hermitian symmetric space without Euclidean factor is the product of a compact and a noncompact type, dual to one another, and the irreducible noncompact ones, the bounded symmetric domains, are classified by Cartan into four infinite families and two exceptional domains. The symmetric spaces and the Hermitian symmetric pair are *Symmetric Spaces* and *The Unitary Group and the Hermitian Symmetric Space*; the kernel is *The Bergman Operator*; the metric and curvature are *Kähler Geometry*, *Kähler Manifolds and the Hermitian Form* and *The Curvature Operator of a Complex Manifold*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $s_p$ | the geodesic symmetry, $s_p^2=\mathrm{id}$, $(ds_p)_p=-\mathrm{id}$ |
| $\nabla J=0$ | the Hermitian symmetric condition, Kähler |
| $M=G/H$ | the group form, $H$ the compact stabiliser |
| $\Omega\subseteq\mathbb{C}^n$ | a bounded symmetric domain |
| $K(z,w)$ | the Bergman kernel |
| $g^{\mathrm B}_{i\bar j}=\partial_i\bar\partial_j\log K(z,z)$ | the Bergman metric |
| $G$, $\Omega=G/H$ | the holomorphic automorphism group and its orbit |

## Further Reading

- Elie Cartan, *Sur les domaines bornés homogènes de l'espace de $n$ variables complexes* (Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg **11**, 1935), for the bounded domains and their classification.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (American Mathematical Society, 2001), for the symmetric spaces, the duality of the two types and the Hermitian case.
- Steven G. Krantz, *Function Theory of Several Complex Variables* (American Mathematical Society, second edition, 2001), for the Bergman metric, its invariance and its completeness on a symmetric domain.
- Ichiro Satake, *Algebraic Structures of Symmetric Domains* (Princeton University Press, 1980), for the classification of the bounded symmetric domains and their compact duals.
