
# __Multipliers of a Banach Algebra__

## Introduction

The multiplications of a Banach algebra $A$ act on $A$ from the left and from the right, and an operator that acts like a multiplication without coming from an element of $A$ is a **multiplier**. In its cleanest form a multiplier is a **double centraliser**: a pair $(L,R)$ of bounded operators with $L(ab) = L(a)b$, $R(ab) = aR(b)$ and $aL(b) = R(a)b$. On a unital algebra there are no others, and the multipliers are exactly the multiplications; on a non-unital algebra they are genuinely more, and they form the **multiplier algebra** $M(A)$, a unital Banach algebra in which $A$ sits as an essential two-sided ideal. The multiplier algebra carries a natural locally convex topology, the **strict topology**, in which $A$ is dense and $M(A)$ complete, so that $M(A)$ is the completion of $A$ in the strict topology and the unitisation when $A$ has a bounded approximate identity. This article develops that construction: the double centralisers and their algebra, the multiplier algebra and its completeness, the strict topology and the density of $A$, and the relation to the double centraliser theorem of the one-sided multiplications.

The article assumes the Banach algebra, its norm, the unit group and the Banach-algebra structure from *Topological Algebras and Banach Algebras*; the bounded operators, the one-sided multiplications, the multiplier definitions, the separating space and the automatic continuity from *Operators on a Banach Algebra*, the first article of this group; the composition and centraliser theorem of the one-sided multiplications and the multiplication algebra from *Left and Right Multiplication in a Banach Algebra*; the closed ideals, the quotients and the unitisation from *Ideals and Quotients of Algebras*; and the bounded operators of a Banach space, the closed ideals and the compact operators from *The Operator Algebra of a Banach Space*. The involution on the elements and the multiplier algebra of a $\mathrm{C}^*$-algebra are the `- * Theory` and `- * Operator Theory` groups of this category and are not used; the strict topology of a Hilbert module and the von Neumann algebra are *Operator Algebras*. No form, no measure and no Fourier theory occurs.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$; $A$ is a Banach algebra over $\mathbb{K}$ with submultiplicative norm $\lVert\cdot\rVert$, not assumed unital; $B(A)$ is the Banach algebra of bounded linear operators. A left multiplier is a bounded $L$ with $L(ab) = L(a)b$, a right multiplier a bounded $R$ with $R(ab) = aR(b)$, and a **double centraliser** a pair $(L,R)$ of a left and a right multiplier with $aL(b) = R(a)b$ for all $a,b$. The unitisation of $A$ is written $A^\sharp = A \oplus \mathbb{K}$.

## Double Centralisers

**Definition.** A **double centraliser** on $A$ is a pair $(L,R)$ of bounded linear operators on $A$ with

$$
L(ab) = L(a)\,b , \qquad R(ab) = a\,R(b) , \qquad a\,L(b) = R(a)\,b \qquad \text{for all } a,b \in A .
$$

The set of double centralisers is written $M(A)$, the **multiplier algebra** of $A$.

**Proposition (the algebra structure).** With the operations

$$
(L_1,R_1) + (L_2,R_2) = (L_1 + L_2,\,R_1 + R_2) , \qquad (L_1,R_1)(L_2,R_2) = (L_1L_2,\,R_2R_1) , \qquad \lambda(L,R) = (\lambda L,\,\lambda R) ,
$$

the set $M(A)$ is a unital associative algebra with identity $(\mathrm{id},\mathrm{id})$, and the two components determine each other on an algebra with $A^2 = A$.

**Proof.** The sum of two double centralisers is a double centraliser, and the product $(L_1L_2,R_2R_1)$ is one: $L_1L_2(ab) = L_1(L_2(a)b) = L_1L_2(a)b$, $R_2R_1(ab) = aR_2R_1(b)$, and $aL_1L_2(b) = aL_1(L_2(b))$ while $R_2R_1(a)b = R_2(R_1(a))b$; the two agree by the centralising relations applied twice. Associativity is the associativity of composition, and $(\mathrm{id},\mathrm{id})$ is the identity. The components determine each other when $A^2 = A$ because $aL(b) = R(a)b$ for all $a,b$ forces $L$ to determine $R$ on the ideal $A^2$ and $R$ to determine $L$. $\square$

**Theorem ($M(A)$ is a Banach algebra).** Give $M(A)$ the norm

$$
\lVert(L,R)\rVert = \max\{\lVert L\rVert,\lVert R\rVert\} ,
$$

where $\lVert L\rVert,\lVert R\rVert$ are the operator norms. Then $M(A)$ is a unital Banach algebra under the product above, the maps $(L,R) \mapsto L$ and $(L,R) \mapsto R$ are contractions, and $\lVert(L,R)\rVert = \lVert L\rVert = \lVert R\rVert$ on the double centralisers of a faithful algebra.

**Proof.** The norm is a norm because it is the max of two norms, and it is submultiplicative: $\lVert L_1L_2\rVert \leq \lVert L_1\rVert\lVert L_2\rVert$ and $\lVert R_2R_1\rVert \leq \lVert R_2\rVert\lVert R_1\rVert$, so $\lVert(L_1,R_1)(L_2,R_2)\rVert \leq \lVert(L_1,R_1)\rVert\lVert(L_2,R_2)\rVert$. Completeness: a Cauchy sequence of double centralisers has Cauchy components in the complete spaces $B(A)$, with limits $L,R$; the defining relations pass to the limit by continuity of the products, so the limit is a double centraliser, and the norm converges. The identity has norm one. The equality of the norms on a faithful algebra is the standard consequence of $aL(b) = R(a)b$. $\square$

**Proposition (the canonical embedding).** The map

$$
\iota : A \longrightarrow M(A) , \qquad \iota(a) = (L_a,R_a) ,
$$

is an isometric algebra homomorphism when $A$ is unital and a bounded algebra homomorphism in general, with image $\iota(A)$ a two-sided ideal of $M(A)$; it is injective on a faithful algebra and, in particular, on a unital one. The identity of $M(A)$ lies in $\iota(A)$ exactly when $A$ is unital, and then $\iota$ is onto.

**Proof.** $(L_a,R_a)$ is a double centraliser by *Operators on a Banach Algebra*, and $\iota(ab) = (L_{ab},R_{ab}) = (L_aL_b,R_bR_a) = \iota(a)\iota(b)$ by the composition laws, so $\iota$ is a homomorphism. On a unital algebra $\lVert L_a\rVert = \lVert R_a\rVert = \lVert a\rVert$, giving the isometry, and $\iota$ is onto by the unital identification of the multipliers. That $\iota(A)$ is an ideal: for a double centraliser $(L,R)$ and $a \in A$, $(L,R)(L_a,R_a) = (LL_a, R_aR)$, and $LL_a = L_{L(a)}$, $R_aR = R_{R(a)}$ by the multiplier identities, so the product lies in $\iota(A)$, and likewise on the left. $\square$

**Corollary (the unital case).** If $A$ is unital then $M(A) = \iota(A) \cong A$, the multiplier algebra is the algebra itself, and the construction adds nothing. The multipliers are genuinely new only for a non-unital algebra.

**Proof.** On a unital algebra every left multiplier is $L_{L(1)}$ and every right multiplier is $R_{R(1)}$, and the centralising relation forces $L(1) = R(1)$; hence every double centraliser is $\iota(c)$ with $c = L(1)$, and $\iota$ is a bijection. $\square$

## The Multiplier Algebra

**Theorem (the multiplier algebra is unital with essential ideal $A$).** Let $A$ be a Banach algebra with $A^2 = A$ (in particular a non-unital algebra with a bounded approximate identity). Then $\iota(A)$ is a two-sided ideal of $M(A)$ with $\iota(A)^2 = \iota(A)$, the algebra $M(A)$ is unital, and $\iota(A)$ is **essential**: a double centraliser $(L,R)$ with $(L,R)\iota(A) = 0$ is zero, and the same on the other side.

**Proof.** $\iota(A)$ is an ideal by the proposition, and it is essential because $(L,R)\iota(a) = 0$ for all $a$ gives $(LL_a, R_aR) = 0$, so $LL_a = 0$ for all $a$ and $L = 0$ on $A^2 = A$, that is $L = 0$; then $R = 0$ by the centralising relation on a faithful algebra. The unit is $(\mathrm{id},\mathrm{id})$. $\square$

**Theorem (the multiplier algebra as the double centraliser algebra).** Let $A$ be a unital Banach algebra and let $\lambda(A)$ and $\rho(A)$ be the two regular representations in $B(A)$. Then the double centraliser algebra of the pair $(\lambda(A),\rho(A))$ is $\lambda(A)' = \rho(A)$ and $\rho(A)' = \lambda(A)$, and $M(A) = \iota(A)$. In the non-unital case, if the algebra is faithful and has a bounded approximate identity, then

$$
M(A) \cong \{\,T \in B(A) : T\lambda(A) \subseteq \lambda(A),\ \lambda(A)T \subseteq \lambda(A),\ T\rho(A) \subseteq \rho(A),\ \rho(A)T \subseteq \rho(A)\,\} ,
$$

the operators normalising both regular representations, and the isomorphism pairs $T$ with the double centraliser of the two inclusions.

**Proof.** The centraliser identities in the unital case are *Left and Right Multiplication in a Banach Algebra*, and the identification with $\iota(A)$ is the corollary above. In the non-unital case a double centraliser $(L,R)$ defines, through the inclusions $L\lambda(a) = \lambda(L(a))$ and $\rho(a)R = \rho(R(a))$, an operator normalising both families, and conversely such an operator gives a double centraliser by its actions; the correspondence is bijective on a faithful algebra with an approximate identity. $\square$

**Remark (the boundary).** The identification of the multiplier algebra with the operators normalising the regular representations is the operator form of the double centraliser theorem; the abstract form is in *Left and Right Multiplication in a Banach Algebra*. The multiplier algebra of a $\mathrm{C}^*$-algebra is again a $\mathrm{C}^*$-algebra, and the multiplier algebra of a Hilbert $\mathrm{C}^*$-module is the source of the strongly continuous strict topology, both owned by the involutive groups of this category and by *Operator Algebras*.

## The Strict Topology

**Definition.** The **strict topology** on $M(A)$ is the locally convex topology generated by the seminorms

$$
(L,R) \longmapsto \lVert L(a)\rVert , \qquad (L,R) \longmapsto \lVert R(a)\rVert , \qquad a \in A .
$$

The **strict topology** on $A$ is the topology generated by the seminorms $x \mapsto \lVert ax\rVert$ and $x \mapsto \lVert xa\rVert$ for $a \in A$, pulled back along $\iota$.

**Proposition (the strict topology is well defined and the multiplications are strictly continuous).** The family of seminorms above separates the points of $M(A)$ on a faithful algebra with $A^2 = A$, so the strict topology is Hausdorff; for each fixed $a$ the maps $(L,R) \mapsto L(a)$ and $(L,R) \mapsto R(a)$ are strictly continuous, and the product of $M(A)$ is strictly continuous in each variable separately.

**Proof.** If all seminorms vanish then $L(a) = 0$ for every $a$, so $L = 0$, and $R = 0$ by faithfulness; hence the topology is Hausdorff. Continuity of evaluation is the definition of the seminorms. For the product in the first variable: $((L_1,R_1)(L,R))(a) = L_1L(a) = L_1(L(a))$, which depends strictly continuously on $(L,R)$ through $L(a)$ and then on $L_1$ through its value at $L(a)$; the second variable is the mirror. $\square$

**Theorem ($A$ is strictly dense in $M(A)$).** Let $A$ be a Banach algebra with a bounded approximate identity $(u_\lambda)$. Then $\iota(A)$ is dense in $M(A)$ in the strict topology, and $M(A)$ is complete in the strict topology; consequently $M(A)$ is the strict completion of $A$ and the identity of $M(A)$ is the strict limit of the approximate identity.

**Proof.** For a double centraliser $(L,R)$ and $a \in A$ one has $L(u_\lambda a) = L(u_\lambda)a \to L(a)$ and $L(u_\lambda)$ is a bounded net in $A$, so $\iota(L(u_\lambda)) \to (L,R)$ in the seminorms generated by $L$, using the boundedness of $L$; the right component is handled by $R(u_\lambda)$. Hence $\iota(A)$ is strictly dense. Completeness is the standard statement that a strict Cauchy net has strictly convergent left and right components by completeness of $B(A)$ and the boundedness of the approximate identity; the limit double centraliser is $(L,R)$, and the identity is the limit of $\iota(u_\lambda)$. $\square$

**Corollary (the strict topology and the norm topology).** The strict topology is coarser than the norm topology on $M(A)$, and it agrees with the norm topology on a unital algebra; on the unit ball of $M(A)$ the strict topology is the topology of pointwise convergence on the image of $\iota$, and the closed unit ball is strictly bounded but need not be strictly compact.

**Proof.** The seminorms are dominated by the norm, since $\lVert L(a)\rVert \leq \lVert L\rVert\lVert a\rVert$, so strict is coarser; on a unital algebra $a = 1$ gives $\lVert L\rVert \leq \lVert L(1)\rVert$ and the two topologies agree. The ball statement is the definition of the seminorms. $\square$

**Remark (bounded approximate identities).** The existence of a bounded approximate identity is a hypothesis, not automatic for a Banach algebra; it holds for $c_0$, for $K(H)$, for $C_0(X)$ and for the group algebra $\ell^1(G)$ for an amenable $G$. The strict density theorem is stated under this hypothesis, and the multiplier algebra is defined in general.

## Examples

**Example ($c_0$ and $\ell^\infty$).** Let $A = c_0$ with the sup norm; the approximate identity is the sequence of truncations, which is bounded. Every multiplier of $c_0$ is multiplication by a bounded sequence, so $M(c_0) = \ell^\infty$, the strict topology is the topology of pointwise convergence on the coordinates, and $c_0$ is strictly dense in $\ell^\infty$. The unit of $M(c_0)$ is the constant sequence $1$.

**Example ($K(H)$ and $B(H)$).** Let $A = K(H)$ be the compact operators on an infinite-dimensional Hilbert space. Its multiplier algebra is $M(K(H)) = B(H)$, the bounded operators, with the strict topology the strong-$*$ topology of pointwise convergence; $K(H)$ is strictly dense in $B(H)$, and the unit of $B(H)$ is the strict limit of the finite-rank projections. The double centraliser of $T \in B(H)$ is the pair of left and right multiplication by $T$.

**Example ($C_0(X)$ and $C_b(X)$).** Let $A = C_0(X)$ for a locally compact Hausdorff space $X$, with the sup norm. The multipliers are the multiplication operators by bounded continuous functions, $M(C_0(X)) = C_b(X)$, and the strict topology is that of uniform convergence on compact subsets of $X$; the unitisation of $C_0(X)$ is contained in $C_b(X)$ and is strictly dense.

**Example (the unitisation).** For any Banach algebra $A$, the unitisation $A^\sharp = A \oplus \mathbb{K}$ is a unital Banach algebra containing $A$ as an ideal of codimension one, and $M(A^\sharp) = A^\sharp$; the multiplier algebra of $A$ contains the unitisation when the latter contains $A$ as an essential ideal, and for $A$ with a bounded approximate identity the relation $M(A) = M(A^\sharp)$ holds.

## Summary

A double centraliser on a Banach algebra $A$ is a pair $(L,R)$ of bounded operators with $L(ab) = L(a)b$, $R(ab) = aR(b)$ and $aL(b) = R(a)b$; the double centralisers form the multiplier algebra $M(A)$ under the product $(L_1,R_1)(L_2,R_2) = (L_1L_2,R_2R_1)$, a unital Banach algebra for the max norm, in which $A$ embeds by $a \mapsto (L_a,R_a)$ as a two-sided ideal, essential when $A^2 = A$ and faithful. On a unital algebra the embedding is an isomorphism $M(A) \cong A$, and the multipliers are exactly the multiplications; the construction is new only in the non-unital case. The multiplier algebra is the algebra of bounded operators normalising both regular representations, which is the operator form of the double centraliser theorem of *Left and Right Multiplication in a Banach Algebra*. The strict topology, generated by the seminorms $(L,R) \mapsto \lVert L(a)\rVert$ and $(L,R) \mapsto \lVert R(a)\rVert$, is Hausdorff and coarser than the norm topology and agrees with it in the unital case; when $A$ has a bounded approximate identity, $A$ is strictly dense in $M(A)$, the multiplier algebra is strictly complete, and it is the strict completion of $A$, with the unit as the strict limit of the approximate identity. The multiplier algebra of a $\mathrm{C}^*$-algebra and the strict topology of a Hilbert module are the involutive refinements, owned by the later groups of this category and by *Operator Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $\lVert\cdot\rVert$ | Banach algebra, not assumed unital; its norm |
| $L$, $R$ | Left multiplier $L(ab)=L(a)b$; right multiplier $R(ab)=aR(b)$ |
| $(L,R)$, $aL(b)=R(a)b$ | A double centraliser |
| $M(A)$ | The multiplier algebra of double centralisers |
| $(L_1,R_1)(L_2,R_2) = (L_1L_2,R_2R_1)$ | Product in $M(A)$ |
| $\lVert(L,R)\rVert = \max\{\lVert L\rVert,\lVert R\rVert\}$ | The norm, submultiplicative and complete |
| $\iota : a \mapsto (L_a,R_a)$ | The embedding of $A$ as an essential ideal |
| $(\mathrm{id},\mathrm{id})$ | The unit of $M(A)$ |
| $\lVert L(a)\rVert$, $\lVert R(a)\rVert$ | The seminorms of the strict topology |
| $x \mapsto \lVert ax\rVert$, $\lVert xa\rVert$ | The strict topology on $A$ |
| $(u_\lambda)$ | A bounded approximate identity, strictly convergent to the unit |
| $A^\sharp = A \oplus \mathbb{K}$ | The unitisation |

## Further Reading

- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume I* (Cambridge University Press, 1994), for the multiplier algebra, the double centralisers and the strict topology.
- Ronald Larsen, *An Introduction to the Theory of Multipliers* (Springer, 1971), for the multiplier algebra of a Banach algebra and its structure.
- Frank F. Bonsall and John Duncan, *Complete Normed Algebras* (Springer, 1973), for the double centralisers, the approximate identities and the strict topology.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the multiplier algebra of a $\mathrm{C}^*$-algebra and the strict topology in the operator-algebra setting.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the double centraliser theorem and the algebra of the regular representation.
