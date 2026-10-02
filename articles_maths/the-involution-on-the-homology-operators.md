
# __The Involution on the Homology Operators__

## Introduction

An involution of a manifold acts on its homology, and therefore acts on the **operators** on the homology: on the linear endomorphisms of $H_*(M;k)$ by conjugation, and on each natural operator of the theory — the intersection form, the Poincaré duality isomorphism, the cup product, the surgery and handle operators, the Dehn twist. This article is the operator-layer synthesis: it determines which operators are equivariant, it computes the induced action on the algebra of operators, and it reads the Lefschetz number as the supertrace of the induced involution.

The structure is the one of the two earlier articles on the homology with one layer added. The endomorphism algebra decomposes into the invariant operators, which are block diagonal with respect to the fixed and the anti-fixed parts, and the anti-invariant operators, which are off diagonal; the natural operators of topology are equivariant up to the degree sign of *The Involution on the Homology*, and the supertrace of the induced involution is the Lefschetz number, which the Lefschetz fixed point theorem relates to the fixed set.

**The article assumes** everything of the group: *The Involution as an Operator on the Homology* (the module $H_*$ over $k[\mathbb{Z}/2]$ and the transfer), *The Involution on the Homology* (the interaction with the intersection form), *The Surgery Operator*, *The Handle Operator*, *The Dehn Twist as an Operator* and *The Mapping Class Group Action* (the operators whose equivariance is decided here), and the Steenrod operations of *The Steenrod Squares and the Cohomology Operations*.

**The boundaries of the article.** The homology of an involution and the intersection form are the two articles of the group's first-homology family; the classification of the Hermitian forms and the surgery obstruction groups are *Hermitian Pairings and the Signature*, the next article of this group; the equivariant signature is *Hermitian Pairings and the Equivariant Signature*. The index theory of an equivariant elliptic operator is Part IV (*Index Theory and the Atiyah–Singer Theorem*). No analysis and no smooth structure is used beyond the statement of the Lefschetz fixed point theorem.

## The Conjugation Action on the Operators

**Definition.** Let $T$ be an involution of a finite complex $M$ and let $H = H_*(M;k)$ be its homology over a ring $k$ in which $2$ is invertible. The involution acts on the endomorphism algebra by **conjugation**,
$$
\alpha\longmapsto T_*\,\alpha\,T_*^{-1}, \qquad \alpha\in\operatorname{End}_k(H),
$$
and makes $\operatorname{End}_k(H)$ a module over $k[\mathbb{Z}/2]$. An operator is **equivariant** (or invariant) if it is fixed by the action, that is, if it commutes with $T_*$; it is **anti-equivariant** if it satisfies $T_*\alpha T_*^{-1} = -\alpha$.

**Theorem (the invariant operators are the block-diagonal ones).** Write $H = H^{+}\oplus H^{-}$ for the fixed and the anti-fixed parts and, for a homogeneous operator, its block decomposition
$$
\alpha = \begin{pmatrix} \alpha^{++} & \alpha^{+-} \\ \alpha^{-+} & \alpha^{--} \end{pmatrix};
$$
then $\alpha$ is equivariant exactly when the off-diagonal blocks vanish, $\alpha^{+-} = \alpha^{-+} = 0$, and anti-equivariant exactly when the diagonal blocks vanish. Hence
$$
\operatorname{End}_k(H)^{\mathbb{Z}/2} \;\cong\; \operatorname{End}_k(H^{+})\oplus\operatorname{End}_k(H^{-}) \,\subseteq\, \operatorname{End}_k(H)
$$
and the anti-invariant operators form the complementary summand $\operatorname{Hom}_k(H^{+},H^{-})\oplus\operatorname{Hom}_k(H^{-},H^{+})$; over a field the algebra decomposes as a $k[\mathbb{Z}/2]$-module into these two summands, and $\operatorname{End}_k(H)$ is the direct sum of the invariant and the anti-invariant operators.

**Proof.** The action on a matrix is conjugation by the diagonal matrix $\operatorname{diag}(1,-1)$ on $H^{+}\oplus H^{-}$; conjugating a block by that matrix multiplies the off-diagonal blocks by $-1$ and fixes the diagonal ones. A matrix is therefore fixed exactly when its off-diagonal blocks vanish, and negated exactly when its diagonal blocks vanish. The direct-sum statement follows from the invertibility of $2$.

**Corollary (the commutant and the bimodule structure).** The invariant operators form the commutant $C(T_*) = \operatorname{End}_k(H)^{\mathbb{Z}/2}$, an algebra acting on each of the two parts, and the module $H$ is a module over this algebra with $H^{+}$ and $H^{-}$ as the two isotypic components. The centraliser of the image of $k[\mathbb{Z}/2]$ in $\operatorname{End}_k(H)$ is exactly the commutant, and the double centraliser statement gives the Morita equivalence between the module structure over $k[\mathbb{Z}/2]$ and the module structure over the commutant.

**Proof.** The commutant is the centraliser, and the isotypic decomposition of a module over the semisimple ring $k[\mathbb{Z}/2]$ is the decomposition into the two characters; the standard double centraliser theorem for semisimple modules gives the stated equivalence.

**Example (the identity and the involutions).** The identity operator is equivariant, and the operator $T_*$ itself is equivariant; the projection $P^{+} = (1+T_*)/2$ onto the fixed part and the projection $P^{-} = (1-T_*)/2$ onto the anti-fixed part are equivariant idempotents summing to the identity, and the two projections are the trace of the module structure. An operator mapping $H^{+}$ to $H^{-}$ is anti-equivariant; the intersection form of an orientation-reversing involution is such an operator, as *The Involution on the Homology* shows.

## The Equivariance of the Natural Operators

**Theorem (the natural operators of the homology are equivariant up to degree).** The following operators of the theory are equivariant for an orientation-preserving involution and equivariant up to the degree sign for an orientation-reversing one:

**(a)** the Poincaré duality isomorphism $D : H^k(M)\to H_{n-k}(M)$, which intertwines the two actions and preserves the isotropy parts for an orientation-preserving involution and exchanges them for an orientation-reversing one;

**(b)** the cup product $\smile : H^p\times H^q\to H^{p+q}$, which satisfies $T^{*}(\alpha\smile\beta) = T^{*}\alpha\smile T^{*}\beta$;

**(c)** the cap product and the evaluation pairing, by the naturality of the product;

**(d)** the intersection form $Q$, with $Q(T_*x,T_*y) = \deg(T)Q(x,y)$;

**(e)** the Steenrod squares $Sq^i$ and the Bockstein, which are natural operations and therefore commute with every induced map, hence with $T_*$; in particular the action of $\mathbb{Z}/2$ on $H^*(M;\mathbb{F}_2)$ commutes with the whole Steenrod algebra.

**Proof.** (a) is the equivariant Poincaré duality of *The Involution on the Homology*; (b) and (c) are the naturality of the cup and cap products under a homeomorphism; (d) is the theorem of *The Involution on the Homology*; (e) is the naturality of the cohomology operations, which are defined on the category of spaces and maps.

**Theorem (the equivariance of the geometric operators).** Let $T$ be an involution of a manifold $M$.

**(a)** A Dehn twist $T_a$ on a surface is equivariant with respect to the involution of the mapping class group if and only if the curve $a$ is invariant (up to isotopy) under the involution; then the induced operator on the homology satisfies $T_*(T_a)_*T_*^{-1} = (T_{T(a)})_*$, and for an invariant non-separating curve the direction of the transvection is taken to the direction of the image class.

**(b)** The surgery and handle operators of *The Surgery Operator* and *The Handle Operator* are equivariant exactly when the attaching data (the sphere, the framing and the normal representation) are equivariant; the equivariant operators are the ones whose traces are the equivariant surgery obstructions of *Involutions on Manifolds and Equivariant Surgery*.

**(c)** The symplectic representation of the mapping class group is equivariant for the action of a surface involution on the mapping class group and on the homology.

**Proof.** (a) is the conjugation formula of the mapping class group action: $\rho(\phi T_a\phi^{-1}) = \rho(\phi)\rho(T_a)\rho(\phi)^{-1}$, applied to $\phi$ the involution; (b) is the naturality of the handle and surgery constructions under an equivariant homeomorphism, with the local model of the normal representation required for the equivariance; (c) is the compatibility of the action on $H_1$ with the action on the mapping class group.

**Corollary (which operators descend to the quotient).** An equivariant operator on $H_*(M)$ restricts to operators on the fixed part $H^{+}$ and on the anti-fixed part $H^{-}$; over a field in which $2$ is invertible, an equivariant operator therefore descends to an operator on the invariants and to one on the coinvariants, and the natural operators that are equivariant descend to the homology of the quotient and to the homology of the fixed set, as in *The Involution as an Operator on the Homology*.

## The Supertrace and the Lefschetz Number

**Definition.** Let $H = \bigoplus_i H_i$ be a graded module with a degree-zero endomorphism $\alpha$ of finite rank. The **supertrace** is
$$
\operatorname{Str}(\alpha) = \sum_i(-1)^i\operatorname{tr}\bigl(\alpha\,|\,H_i\bigr),
$$
and the **Lefschetz number** of the involution is $L(T) = \operatorname{Str}(T_*)$.

**Proposition (the Lefschetz number and the Euler characteristic).** For a locally linear (or smooth) involution $T$ of a closed manifold, the Lefschetz number is the Euler characteristic of the fixed set,
$$
L(T) = \chi(F), \qquad F = M^{T}.
$$
In particular $L(T) = \#F$ when the fixed set is finite, and $L(T) = 0$ for a free involution; the identity $L(T)\equiv\chi(M)\pmod 2$ also holds, because the trace of an involution on a vector space has the parity of the dimension.

**Proof sketch.** The Lefschetz fixed point theorem computes $L(T)$ as the sum of the local contributions of the fixed set, which for a locally linear involution is the Euler characteristic of the fixed set because the local model $F\times D^k$ with the reflection contributes $\chi(F)$ and the normal reflection contributes $1$ to each fixed component. The examples check the formula: for the involution $-I$ of the torus the four fixed points give $L = 1 + 2 + 1 = 4$, for the reflection of a sphere the two fixed components give the Euler characteristic of the equator, and for the involution of $S^2$ with two fixed points $L = 2$. The general statement is the Atiyah–Bott form of the Lefschetz theorem for a periodic map.

**Corollary (the supertrace detects the fixed set).** The supertrace of the induced involution on the homology is a homeomorphism invariant of the action computing the Euler characteristic of the fixed set; it is the first and the simplest of the equivariant invariants of the action, and it is refined by the equivariant signature of *Hermitian Pairings and the Equivariant Signature*, which is the corresponding supertrace for the intersection form in dimension $4k$.

**Proof.** The Lefschetz number is homotopy invariant and the formula computes it from the fixed set; the refinement to the signature is the observation that the intersection form on the middle homology is a Hermitian form whose equivariant supertrace is the multisignature.

**Remark (the index interpretation).** The supertrace is the index of the "supersymmetric" operator $T_*$ on the graded module, and the equality $L(T) = \chi(F)$ is the equality of two indices: the index of the equivariant operator $1 - T_*$ and the index of the Euler characteristic of the fixed set. For the equivariant elliptic operators this becomes the Atiyah–Singer index theorem with the character $g$, which is Part IV; the present article keeps the algebraic form.

## Examples

**Example (the identity operator and the projections).** The projections $P^{\pm} = (1\pm T_*)/2$ are equivariant idempotents with $\operatorname{rank}$ the dimensions of the two parts; their supertraces are $\operatorname{Str}(P^{+}) = \sum_i(-1)^i\dim H_i^{+} = \chi(M/T)$ up to normalisation and $\operatorname{Str}(P^{-}) = \chi(M)-\chi(M/T)$, which is the Euler-characteristic splitting of *The Involution on the Homology*.

**Example (the transvection and the invariant curve).** On a surface with an involution fixing a non-separating curve $a$, the transvection $(T_a)_*$ is equivariant, with the direction $A$ either fixed or negated by the involution; the operator decomposes into its restrictions to the fixed and anti-fixed parts, and the decomposition is the operator form of the equivariant splitting of the intersection form. The example is the operator-level statement of the Dehn twist article.

**Example (the Steenrod squares on a projective space).** On $\mathbb{RP}^n$ the cohomology is the truncated polynomial ring $\mathbb{F}_2[x]/(x^{n+1})$ with $Sq^i(x^j) = \binom{j}{i}x^{i+j}$; the antipodal involution acts trivially on the mod $2$ cohomology and the Steenrod algebra is invariant, illustrating the naturality of the operations under the action. The example is the simplest computation of the equivariant cohomology operations.

**Example (the Lefschetz number of the torus involution).** For $T = -I$ on $T^2$ the induced map on $H_1$ has trace $-2$ and the map on $H_2$ has degree $+1$, so $L(T) = 1 + 2 + 1 = 4$, the number of two-torsion points, the fixed set of the involution; the computation is the standard verification of $L(T) = \chi(F)$.

## Summary

An involution of a space acts on the operators of its homology by conjugation, and the operators fixed by the action are precisely the ones commuting with the induced involution, that is, the block-diagonal operators with respect to the splitting of the homology into the fixed and the anti-fixed parts; the anti-equivariant operators are the block off-diagonal ones. The natural operators of topology — Poincaré duality, the cup and cap products, the intersection form, the Steenrod squares and the Bockstein — are equivariant up to the degree sign of the action, and the geometric operators — the Dehn twist, the surgery and handle operators, the symplectic representation — are equivariant exactly when their defining data are invariant. Equivariant operators restrict to the two eigenspaces and descend to the homology of the quotient and of the fixed set. The supertrace of the induced involution is the Lefschetz number, which for a locally linear involution equals the Euler characteristic of the fixed set, and it is the first equivariant invariant of the action, refined by the equivariant signature in the middle dimension of a $4k$-manifold.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_*$, conjugation $\alpha\mapsto T_*\alpha T_*^{-1}$ | the induced action on the homology and on the operators |
| $H = H^{+}\oplus H^{-}$ | the fixed and anti-fixed parts of the homology |
| invariant / anti-equivariant operator | commuting with $T_*$, respectively anti-commuting |
| $\operatorname{End}_k(H)^{\mathbb{Z}/2}\cong\operatorname{End}_k(H^{+})\oplus\operatorname{End}_k(H^{-})$ | the commutant, the block-diagonal operators |
| $P^{\pm} = (1\pm T_*)/2$ | the equivariant projections onto the two parts |
| $Q(T_*x,T_*y) = \deg(T)Q(x,y)$ | the equivariance of the intersection form |
| $Sq^i$, Bockstein | the natural cohomology operations, commuting with the action |
| $\operatorname{Str}(\alpha) = \sum_i(-1)^i\operatorname{tr}(\alpha|H_i)$ | the supertrace; $L(T) = \operatorname{Str}(T_*)$ the Lefschetz number |
| $L(T) = \chi(F)$ | the Lefschetz number of a locally linear involution is the Euler characteristic of the fixed set |

## Further Reading

- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the fixed-set formula for the Lefschetz number and the equivariant neighbourhoods.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the Lefschetz fixed point theorem, the trace and the supertrace formalism.
- Norman Steenrod and David Epstein, *Cohomology Operations* (Princeton University Press, 1962), for the Steenrod squares and their naturality, used in *The Steenrod Squares and the Cohomology Operations*.
- Benson Farb and Dan Margalit, *A Primer on Mapping Class Groups* (Princeton University Press, 2012), for the conjugation formula of the Dehn twist and the equivariance of the symplectic representation.
- Michael F. Atiyah and Raoul Bott, "A Lefschetz Fixed Point Formula for Elliptic Complexes I", *Annals of Mathematics* 86 (1967), 374–407, for the analytic refinement of the supertrace and the fixed-set formula.
- Michael F. Atiyah and Isadore M. Singer, "The Index of Elliptic Operators: III", *Annals of Mathematics* 87 (1968), 546–604, for the equivariant index theorem, the analytic home of the equivariant supertrace in Part IV.
- Karl Heinz Dovermann and Reinhard Schultz, *Equivariant Surgery Theories and Their Periodicity Properties* (Springer Lecture Notes 1443, 1990), for the equivariant operators and the traces in the surgery theory.
