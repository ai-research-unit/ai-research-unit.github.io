# __The Cartan Decomposition of $\mathrm{GL}_2(\mathbb{C})$__

## Introduction

**The group $\mathrm{GL}_2(\mathbb{C})$ is the product of the unitary group with the exponential of the Hermitian half, each element has a unique such product, and the two factors are the eigenspaces of the Cartan involution $g\mapsto(g^{*})^{-1}$.**

The article defines the Cartan involution, computes its two eigenspaces, proves that the involution is an automorphism of the group and that its derivative is the map $X\mapsto-X^{*}$ on the Lie algebra, derives the group decomposition from the polar decomposition of the previous article, proves the bracket relations between the two summands, and identifies the symmetric space and the two real forms. It assumes *The Polar Decomposition from the Two Halves at $n=2$*, *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$* and *The Exponential of a $2\times2$ Matrix and Its Image*.

It follows the biquaternion article *The Endomorphisms of the Biquaternion Algebra* for the involution read on the eight real coordinates.

## The Cartan Involution

**Definition.** The **Cartan involution** is $\theta(g)=(g^{*})^{-1}$ for an invertible $g$.

**Proposition.** The map $\theta$ is an involutive automorphism of the group $\mathrm{GL}_2(\mathbb{C})$, and its fixed subgroup is the unitary group.

**Proof.** $\theta(gh)=((gh)^{*})^{-1}=(h^{*}g^{*})^{-1}=(g^{*})^{-1}(h^{*})^{-1}=\theta(g)\theta(h)$, and $\theta(\theta(g))=(g^{-1})^{*}{}^{-1}=g$. A matrix is fixed exactly when $g^{*}=g^{-1}$, which is the definition of unitarity.

**Corollary.** The fixed subgroup is compact and is the unitary group $\mathrm{U}(2)$.

**Proof.** The unitary matrices are closed and bounded in the space of matrices, and they form a group.

**Corollary.** On the scalars the involution is complex conjugation, so its fixed points on the scalar circle are the two signs.

**Proof.** For $g=cI$ the involution gives $\bar cI$, and the fixed scalars of modulus one are $\pm1$.

## The Two Eigenspaces

**Proposition.** The derivative of $\theta$ at the identity is the map $X\mapsto-X^{*}$, whose eigenvalues are $+1$ and $-1$ with the anti-Hermitian and the Hermitian matrices as eigenspaces.

**Proof.** Differentiating $g\mapsto(g^{*})^{-1}$ at $g=I$ in the direction $X$ gives $-X^{*}$; a matrix satisfying $X^{*}=-X$ is anti-Hermitian and one satisfying $X^{*}=X$ is Hermitian, and every matrix splits accordingly as $X=\tfrac12(X-X^{*})+\tfrac12(X+X^{*})$.

**Corollary.** The Lie algebra splits as $\mathfrak{gl}_2(\mathbb{C})=\mathfrak{u}(2)\oplus\operatorname{Herm}_2$, with the anti-Hermitian part of real dimension four and the Hermitian part of real dimension four.

**Proof.** The two eigenspaces have real dimension four each, because an anti-Hermitian matrix has four independent real entries and a Hermitian one has four as well.

**Corollary.** The summand $\mathfrak{p}=\operatorname{Herm}_2$ is not a Lie subalgebra, while $\mathfrak{u}(2)$ is one.

**Proof.** The bracket of two Hermitian matrices is anti-Hermitian, so it leaves the summand; the bracket of two anti-Hermitian matrices stays anti-Hermitian.

## The Bracket Relations

**Theorem.** The three bracket relations hold: $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$, $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$ and $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$, where $\mathfrak{k}=\mathfrak{u}(2)$ and $\mathfrak{p}=\operatorname{Herm}_2$.

**Proof.** For anti-Hermitian $K_{1},K_{2}$ the bracket has adjoint $[K_{2},K_{1}]=-[K_{1},K_{2}]$, so it is anti-Hermitian; for anti-Hermitian $K$ and Hermitian $H$ the bracket has adjoint $[H,K]=-[K,H]$, so it is Hermitian; for Hermitian $H_{1},H_{2}$ the bracket has adjoint $[H_{2},H_{1}]$, so it is anti-Hermitian.

**Corollary.** The pair $(\mathfrak{gl}_2(\mathbb{C}),\mathfrak{k})$ is a symmetric Lie algebra, and the summand $\mathfrak{p}$ is a module for $\mathfrak{k}$.

**Proof.** The relations are exactly the axioms of a symmetric Lie algebra, and the second relation says that the bracket with $\mathfrak{k}$ preserves $\mathfrak{p}$.

**Corollary.** The pair $(\mathrm{GL}_2(\mathbb{C}),\mathrm{U}(2))$ is a symmetric pair, and its infinitesimal data are the two summands.

**Proof.** The involution $\theta$ fixes the group $\mathrm{U}(2)$ and its derivative fixes $\mathfrak{k}$.

## The Group Decomposition

**Theorem.** Every invertible matrix is uniquely $g=up$ with $u$ unitary and $p$ positive definite Hermitian, so $\mathrm{GL}_2(\mathbb{C})=\mathrm{U}(2)\exp(\operatorname{Herm}_2)$.

**Proof.** This is the polar decomposition of *The Polar Decomposition from the Two Halves at $n=2$*, and the positive factor is the exponential of a Hermitian matrix by the logarithm of the symmetric half.

**Corollary.** The multiplication map $\mathrm{U}(2)\times\operatorname{Herm}_2\to\mathrm{GL}_2(\mathbb{C})$, $(u,H)\mapsto u\,e^{H}$, is a bijection.

**Proof.** The polar decomposition gives existence and the uniqueness of the positive factor plus the logarithm gives uniqueness of $H$.

**Corollary.** The map is a diffeomorphism, so the group is diffeomorphic to the product of a compact group and a vector space.

**Proof.** The factors depend smoothly on the matrix, and the product is smooth with smooth inverse.

## The Symmetric Space

**Proposition.** The quotient $\mathrm{GL}_2(\mathbb{C})/\mathrm{U}(2)$ is diffeomorphic to the Hermitian half, and the group acts on it by left multiplication, which in the model sends $H$ to the logarithm of the positive factor of $ge^{H}$.

**Proof.** The quotient is the set of left cosets, and the map sending a coset to the logarithm of the positive factor of its elements is a bijection with the Hermitian half.

**Corollary.** The quotient is a symmetric space with the involution induced by $\theta$, and the geodesics through the origin are the one-parameter groups $e^{tH}$.

**Proof.** The symmetric space structure comes from the involution, and the geodesics are the exponentials of the summand $\mathfrak{p}$.

**Corollary.** The scalar circle acts on the quotient and the action is nontrivial only through the modulus of the scalar.

**Proof.** A scalar $cI$ has the polar decomposition with the unitary factor of phase $c/|c|$ and the positive factor $|c|I$, so only the modulus survives in the quotient.

## The Real Form

**Proposition.** For the real form $M_2(\mathbb{R})$ the same construction gives $\mathrm{GL}_2(\mathbb{R})=\mathrm{O}(2)\exp(\operatorname{Sym}_2(\mathbb{R}))$.

**Proof.** The involution is now $\theta(g)=(g^{\mathsf T})^{-1}$, whose fixed group is the orthogonal group; the polar decomposition of a real matrix has an orthogonal factor and a positive definite symmetric factor.

**Corollary.** The Hermitian half is replaced by the symmetric half, and the anti-Hermitian half by the antisymmetric line.

**Proof.** The transpose involution has the symmetric matrices as the $+1$ eigenspace and the antisymmetric line as the $-1$ eigenspace.

**Corollary.** The quotient $\mathrm{GL}_2(\mathbb{R})/\mathrm{O}(2)$ is diffeomorphic to the symmetric half, a space of dimension three.

**Proof.** The same map to the logarithm of the positive factor is a bijection.

## The Comparison with the Trace Form

**Proposition.** The two summands are orthogonal for the form $\operatorname{Re}\operatorname{tr}(X^{*}Y)$, and the form is positive definite on the whole Lie algebra.

**Proof.** For anti-Hermitian $K$ and Hermitian $H$ one has $\overline{\operatorname{tr}(K^{*}H)}=\operatorname{tr}(H^{*}K)=\operatorname{tr}(HK)=-\operatorname{tr}(K^{*}H)$, so the number is purely imaginary and its real part vanishes; on each summand the form is a sum of squares on the four real entries, which gives positive definiteness.

**Corollary.** The Hilbert–Schmidt form makes the decomposition into the two summands an orthogonal decomposition.

**Proof.** The two summands are the eigenspaces of a self-adjoint involution for a positive definite form, so they are orthogonal.

**Corollary.** The Cartan decomposition is the group version of the orthogonal splitting of the Lie algebra.

**Proof.** Both come from the same involution, and the group decomposition integrates the algebra one.

## Summary

The Cartan involution $\theta(g)=(g^{*})^{-1}$ is an involutive automorphism of $\mathrm{GL}_2(\mathbb{C})$ whose fixed subgroup is the unitary group. Its derivative is $X\mapsto-X^{*}$, with the anti-Hermitian matrices as the $+1$ eigenspace and the Hermitian matrices as the $-1$ eigenspace, and the three bracket relations hold with $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$.

The group is the product $\mathrm{U}(2)\exp(\operatorname{Herm}_2)$, and the product map is a diffeomorphism. The quotient by the unitary group is the Hermitian half with its symmetric space structure, and the real form replaces the unitary group by the orthogonal group and the Hermitian half by the symmetric half.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\theta(g)=(g^{*})^{-1}$ | the Cartan involution |
| $\mathfrak{k}=\mathfrak{u}(2)$ | the anti-Hermitian summand |
| $\mathfrak{p}=\operatorname{Herm}_2$ | the Hermitian summand |
| $\mathrm{U}(2)\exp(\mathfrak{p})$ | the Cartan decomposition |
| $\mathrm{GL}_2(\mathbb{C})/\mathrm{U}(2)$ | the symmetric space |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for Cartan decompositions and symmetric pairs.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2002), for the structure theory of the decomposition.
- [The Polar Decomposition from the Two Halves at $n=2$](the-polar-decomposition-from-the-two-halves-at-n-2.html), for the group decomposition used here.
- [The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$](the-two-halves-over-c-hermitian-and-anti-hermitian-at-n-2.html), for the two summands of the Lie algebra.
- [The Exponential of $\operatorname{Sym}_2$: Stretches and the Positive Cone](the-exponential-of-sym-2-stretches-and-the-positive-cone.html), for the logarithm used on the Hermitian summand.
