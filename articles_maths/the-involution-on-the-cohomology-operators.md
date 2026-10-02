# __The Involution on the Cohomology Operators__

## Introduction

A continuous involution of a space acts on its cohomology by the contravariant functoriality of the cohomology theory, and the operator it induces is again an involution of the cohomology ring: the fixed part of that operator is the **invariant cohomology** of the space, and the coinvariant part is the part the involution negates. The article studies the operator, its fixed part and the relation of the fixed part to the **equivariant cohomology**, the cohomology of the Borel construction of *Two-Fold Coverings and the Borel Construction*. The relation is exact: the invariant cohomology is the zeroth group cohomology of the group of order two with coefficients in the cohomology of the space, it is the zeroth column of the Serre spectral sequence of the Borel fibration, and in the free case it is the cohomology of the quotient, pulled back along the orbit map. In the language of the operator group, the induced operator on the cohomology is the archetypal **cohomology operator** of the involution, and the article computes its fixed part and its anti-fixed part.

The article continues *Two-Fold Coverings and the Borel Construction*, which gives the homotopy quotient and the classifying space, and *Equivariant Operators under a Continuous Involution*, whose conjugation action it specialises to the cohomology operators. It uses the cohomology ring, the cup product and the functoriality of *Cup and Cap Products* and *Cohomology and the Universal Coefficient Theorem*, and it prepares *The Antipodal Map and the Adjoint* and *Hermitian Pairings on a Topological Space*. The group cohomology of the group of order two and the spectral sequence of a fibration are Part I's *Homological Algebra* and *Spectral Sequences* and the fibrations of this Part, and they are cited where they are needed; the elementary part of the article, the involution on the cohomology and the fixed part, is proved here.

Nothing analytic and nothing geometric is used. The cohomology is the algebraic cohomology of the cochain complex, the coefficients are a commutative ring, and the group of order two acts on the modules; no norm, no measure and no differentiability occurs, and the spectral sequence is used as a computational device only.

## The Involution on the Cohomology

### Functoriality

Throughout, $R$ is a commutative ring with identity, $X$ is a space, and $\sigma : X \to X$ is a continuous involution. Cohomology is taken with coefficients in $R$ and is written $H^{*}(X) = \bigoplus_{n \geq 0} H^{n}(X;R)$.

**Theorem.** The involution induces a graded ring homomorphism

$$
\sigma^{*} : H^{*}(X) \longrightarrow H^{*}(X), \qquad \sigma^{*} = (\sigma^{-1})^{*},
$$

because $\sigma$ is a homeomorphism; it preserves the degree and the cup product,

$$
\sigma^{*}(H^{n}(X)) \subseteq H^{n}(X), \qquad \sigma^{*}(u \cup v) = \sigma^{*}u \cup \sigma^{*}v, \qquad \sigma^{*}(1) = 1,
$$

and it is an involution of the cohomology ring, $(\sigma^{*})^{2} = \mathrm{id}$, since $\sigma^{2} = \mathrm{id}$ and the cohomology is a functor.

**Proof.** Contravariant functoriality gives a graded ring homomorphism for each continuous map, and it is compatible with the cup product and the unit; the identity map induces the identity, and a composite induces the composite, so $\sigma^{*}\sigma^{*} = (\sigma\sigma)^{*} = (\mathrm{id})^{*} = \mathrm{id}$.

**Corollary.** The cohomology ring is a module over the group ring $R[\mathbb{Z}/2]$ through $\sigma^{*}$, and the cohomology is a representation of the group of order two on each degree: the module $H^{n}(X)$ is a $\mathbb{Z}/2$-module, and the article studies the module structure that this representation carries.

**Proof.** The homomorphism $\mathbb{Z}/2 \to \operatorname{Aut}_{\text{ring}}(H^{*}(X))$ sending the generator to $\sigma^{*}$ is a well-defined group homomorphism because $(\sigma^{*})^{2} = \mathrm{id}$; a group action on an abelian group is a module structure over the group ring.

### The Fixed Part

**Definition.** The **invariant cohomology**, or the **fixed part**, is

$$
H^{*}(X)^{\sigma^{*}} = \{u \in H^{*}(X) : \sigma^{*}u = u\},
$$

and the **anti-invariant** part is $H^{*}(X)^{-\sigma^{*}} = \{u : \sigma^{*}u = -u\}$. An invariant class is a class fixed by the induced operator.

**Theorem.** The invariant cohomology is a graded subring of $H^{*}(X)$, and the anti-invariant part is a graded module over it: the cup product of two invariant classes is invariant, the product of an invariant and an anti-invariant class is anti-invariant, and the product of two anti-invariant classes is invariant. If two is invertible in $R$, the cohomology splits as a module,

$$
H^{*}(X) = H^{*}(X)^{\sigma^{*}} \oplus H^{*}(X)^{-\sigma^{*}},
$$

the projections being $(1 \pm \sigma^{*})/2$, and if two is not invertible the two parts need not span.

**Proof.** The product rule is that $\sigma^{*}$ is a ring homomorphism: $\sigma^{*}(uv) = \sigma^{*}u\,\sigma^{*}v$, so the signs multiply. The splitting is the eigenspace decomposition of the linear involution $\sigma^{*}$ when two is invertible, with the projections $(1\pm\sigma^{*})/2$.

**Remark.** The fixed part is the module of invariants of the group action, and its description as $H^{0}$ of the group cohomology below is the reason the group cohomology is the right bookkeeping device. The anti-invariant part, when two is invertible, is the module of coinvariants up to the identification; when two is not invertible, as for the field with two elements, the two parts collapse and only the fixed part remains, the situation already met in *The Induced Involution on the Power Set*.

## The Cohomology Operators

### The Conjugation Action

**Definition.** The **cohomology operators** of $X$ are the elements of the endomorphism algebra $\operatorname{End}_{R}(H^{*}(X))$ of the cohomology module. The involution acts on them by **conjugation**,

$$
\operatorname{Ad}_{\sigma^{*}}(T) = \sigma^{*} T \sigma^{*}, \qquad T \in \operatorname{End}_{R}(H^{*}(X)),
$$

because $(\sigma^{*})^{-1} = \sigma^{*}$; an operator is **equivariant** when it commutes with $\sigma^{*}$.

**Theorem.** The conjugation is an algebra automorphism of $\operatorname{End}_{R}(H^{*}(X))$ of order two; its fixed points are the equivariant cohomology operators, which form a subalgebra; and every operator splits into an equivariant and an anti-equivariant part when two is invertible. The induced map $\sigma^{*}$ itself is an equivariant operator of order two, and its fixed elements in the module $H^{*}(X)$ are the invariant classes.

**Proof.** The statements are those of *Equivariant Operators under a Continuous Involution*, applied to the module $V = H^{*}(X)$ and the involution $\sigma = \sigma^{*}$; the identification of the fixed elements of $\sigma^{*}$ with the invariant classes is the definition.

**Corollary.** The equivariant cohomology operators preserve the fixed part and the anti-invariant part when two is invertible, and they act on the invariant cohomology as the elements of $\operatorname{End}_{R}(H^{*}(X)^{\sigma^{*}})$; the equivariant operators form the subalgebra $\operatorname{End}_{R}(H^{*}(X)^{\sigma^{*}}) \oplus \operatorname{End}_{R}(H^{*}(X)^{-\sigma^{*}})$ when two is invertible.

**Proof.** The eigenspace theorem of *Equivariant Operators under a Continuous Involution*, applied to the cohomology representation.

### The Restriction and the Transfer

**Theorem (the free case).** Let $\sigma$ be free, so that $\pi : X \to X/\sigma$ is a two-fold covering, and let $R$ be a ring in which two is invertible. Then the pullback along the orbit map,

$$
\pi^{*} : H^{*}(X/\sigma) \longrightarrow H^{*}(X),
$$

is injective with image the invariant cohomology $H^{*}(X)^{\sigma^{*}}$, so that

$$
H^{*}(X/\sigma) \;\cong\; H^{*}(X)^{\sigma^{*}} .
$$

**Proof sketch.** The **transfer** is the additive map $\tau : H^{*}(X) \to H^{*}(X/\sigma)$ obtained from the two sheets of the covering: on the level of cochains it sums a cochain over the two points of each fibre, using that the deck group acts on the cochain complex and that the two sheets give a direct sum decomposition of the complex of $X$ over the quotient. The composites satisfy $\pi^{*}\tau = 1 + \sigma^{*}$ and $\tau\pi^{*} = 2$; on the fixed part the first identity reads $\pi^{*}\tau u = 2u$, so $2^{-1}\tau$ is a retraction of $\pi^{*}$, and $\pi^{*}$ is injective with image the fixed part, because a class fixed by $\sigma^{*}$ is $2^{-1}\pi^{*}\tau u$ for the class $\tau u$ of the quotient. The construction is the standard one of the covering theory and is stated without the chain-level details.

**Corollary.** In the free case with two invertible, the invariant cohomology is the cohomology of the quotient, and the fixed part of the involution on the cohomology is therefore a topological invariant of the orbit space. In the fixed-point case no such identification holds, and the invariant cohomology carries information about the involution that the orbit space alone does not see.

**Proof.** The isomorphism is the theorem; the contrast is the failure of the transfer when the covering is not free.

## Equivariant Cohomology

### The Borel Construction

**Definition.** The **equivariant cohomology** of the space with involution is

$$
H^{*}_{\mathbb{Z}/2}(X;R) = H^{*}(X \times_{\mathbb{Z}/2} S^{\infty}; R),
$$

the cohomology of the Borel construction of *Two-Fold Coverings and the Borel Construction*, with the classifying space $B\mathbb{Z}/2 = \mathbb{RP}^{\infty}$.

**Theorem.** There is a map, the **restriction to the fibre**,

$$
H^{*}_{\mathbb{Z}/2}(X;R) \longrightarrow H^{*}(X;R),
$$

induced by the inclusion of a fibre $X \to X \times_{\mathbb{Z}/2} S^{\infty}$, and its image lies in the invariant cohomology $H^{*}(X)^{\sigma^{*}}$ when the Borel construction is read equivariantly; the map is the edge homomorphism of the spectral sequence below. In the free case with two invertible the equivariant cohomology is the cohomology of the quotient, $H^{*}_{\mathbb{Z}/2}(X) \cong H^{*}(X/\sigma)$, and the restriction is the pullback $\pi^{*}$.

**Proof.** The first clauses are the functoriality of the Borel construction and the equivariance of the fibre inclusion, which is equivariant up to the trivial action after quotienting; the free case is the homotopy equivalence $X\times_{\mathbb{Z}/2}S^{\infty}\simeq X/\sigma$ of *Two-Fold Coverings and the Borel Construction*, composed with the identification of the restriction with $\pi^{*}$.

### The Fixed Part as the Zeroth Column

**Theorem.** The group cohomology of the group of order two with coefficients in the module $H^{*}(X)$ is the cohomology of the fixed complex, and its degree-zero part is the invariant cohomology:

$$
H^{0}(\mathbb{Z}/2; H^{*}(X)) = H^{*}(X)^{\sigma^{*}} .
$$

The Serre spectral sequence of the Borel fibration $X \times_{\mathbb{Z}/2} S^{\infty} \to \mathbb{RP}^{\infty}$ has the second page

$$
E_{2}^{p,q} = H^{p}(\mathbb{Z}/2; H^{q}(X)) \;\Longrightarrow\; H^{p+q}_{\mathbb{Z}/2}(X),
$$

so that the invariant cohomology is the zeroth column $E_{2}^{0,*}$ of the spectral sequence, while the anti-invariant part contributes to the first column $E_{2}^{1,*}$, where the group cohomology of the group of order two is concentrated in degrees zero and one and is periodic.

**Proof.** The degree-zero group cohomology of a group with coefficients in a module is the submodule of the fixed elements; the identification is the definition of group cohomology, in *Homological Algebra* and *Spectral Sequences* of Part I. The spectral sequence of the Borel fibration is the Serre spectral sequence with local coefficients in the cohomology of the fibre, the coefficients being the representation of the group on $H^{*}(X)$; its construction belongs to *Spectral Sequences* and to the fibrations of this Part.

**Corollary.** The invariant cohomology is the target of the restriction from the equivariant cohomology in the free case, and in general it is the lowest-degree approximation to the equivariant cohomology from the fibre. The equivariant cohomology is a graded module over the cohomology of the classifying space, $H^{*}(\mathbb{RP}^{\infty};\mathbb{Z}/2) = \mathbb{Z}/2[t]$ with $t$ of degree one, and the module structure records the differentials of the spectral sequence that leave the zeroth column.

**Proof.** The identification of the invariant part with the zeroth column is the theorem; the module structure is the functoriality of the Borel construction in the classifying space, standard for the homotopy quotient.

**Remark.** The picture is the operator-theoretic one: the involution on the space induces an involution on the cohomology modules and on their endomorphism algebras, by conjugation; the fixed part of the first is the invariant cohomology and the fixed part of the second is the algebra of equivariant cohomology operators; and the equivariant cohomology is the device that converts the fixed part into a computable object, through the zeroth column of its spectral sequence and, in the free case, through the identification with the cohomology of the quotient.

## Summary

A continuous involution of a space induces an involution $\sigma^{*}$ of its cohomology ring, preserving the degree and the cup product; the fixed part is the invariant cohomology, a graded subring, and the anti-invariant part is a module over it, the two spanning the cohomology when two is invertible. The cohomology operators form the endomorphism algebra of the cohomology module, the involution acts on them by conjugation, and the equivariant operators are those commuting with $\sigma^{*}$; they preserve the fixed and the anti-invariant parts. In the free case the pullback along the orbit map is injective with image the invariant cohomology, $H^{*}(X/\sigma) \cong H^{*}(X)^{\sigma^{*}}$, when two is invertible, by the transfer. The equivariant cohomology is the cohomology of the Borel construction $X \times_{\mathbb{Z}/2} S^{\infty}$; it is the cohomology of the quotient in the free case, it maps to the cohomology of the space, and the invariant cohomology is the zeroth group cohomology $H^{0}(\mathbb{Z}/2; H^{*}(X))$ and the zeroth column of the Serre spectral sequence of the Borel fibration. The spectral sequence and the group cohomology are the deferred input; the involution on the cohomology and its fixed part are proved here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H^{*}(X)$, $R$ | Cohomology with coefficients in the ring $R$ |
| $\sigma^{*}$ | The induced involution of the cohomology ring, $(\sigma^{*})^{2}=\mathrm{id}$ |
| $H^{*}(X)^{\sigma^{*}}$ | The invariant cohomology, a graded subring |
| $H^{*}(X)^{-\sigma^{*}}$ | The anti-invariant part, a module over the fixed part |
| $(1\pm\sigma^{*})/2$ | The eigenspace projections, two invertible |
| $\operatorname{Ad}_{\sigma^{*}}(T) = \sigma^{*}T\sigma^{*}$ | The conjugation on the cohomology operators |
| equivariant cohomology operator | An operator commuting with $\sigma^{*}$ |
| $\pi : X \to X/\sigma$, free | Two-fold covering; transfer $\tau$ |
| $\pi^{*}\tau = 1+\sigma^{*}$ | The transfer identity; $\tau\pi^{*}=2$ |
| $H^{*}(X/\sigma) \cong H^{*}(X)^{\sigma^{*}}$ | The free case, two invertible |
| $H^{*}_{\mathbb{Z}/2}(X)$ | Equivariant cohomology $H^{*}(X\times_{\mathbb{Z}/2}S^{\infty})$ |
| $H^{0}(\mathbb{Z}/2;H^{*}(X)) = H^{*}(X)^{\sigma^{*}}$ | The fixed part as degree-zero group cohomology |
| $E_{2}^{p,q} = H^{p}(\mathbb{Z}/2;H^{q}(X)) \Rightarrow H^{p+q}_{\mathbb{Z}/2}(X)$ | Serre spectral sequence of the Borel fibration |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for cohomology, the cup product, the transfer for a covering and the cohomology of $\mathbb{RP}^{\infty}$.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the involution on the cohomology, invariant classes and equivariant cohomology.
- Tammo tom Dieck, *Transformation Groups* (de Gruyter, 1987), for equivariant cohomology, the Borel construction and the fixed-part spectral sequence.
- Kenneth S. Brown, *Cohomology of Groups* (Springer, 1982), for the group cohomology of the group of order two and the identification of the degree-zero part with the invariants.
- John McCleary, *A User's Guide to Spectral Sequences*, 2nd ed. (Cambridge University Press, 2001), for the Serre spectral sequence of a fibration and its low-degree columns.
- James R. Munkres, *Elements of Algebraic Topology* (Addison-Wesley, 1984), for the functoriality of cohomology, the cup product and the transfer of a finite covering.
