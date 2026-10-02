
# __The Signed Adjoint of the Left Multiplication on the Group Algebra__

## Introduction

The signed left multiplication is the one-sided operator $f\mapsto a*\alpha(f)$, the left convolution twisted by the grade involution, and it is the integer of the signed block on which the other operators specialise. Its adjoint with respect to the Haar pairing is again a signed left multiplication, the one in the parameter $\sigma(a) = \alpha(a^*)$; because the parametrisation of the signed left multiplications is faithful, the self-adjointness of the operator is exactly the fixed-point condition $\sigma(a) = a$, without any centrality, and the unitarity and the involution are likewise clean: unitary exactly when the parameter is a unitary element, an involution exactly when the parameter lies in the inverted-subgroup carrier $\alpha(a) = a^{-1}$. This article computes the adjoint, its relations with the composition laws and the factorization of the sandwich, and the criteria for self-adjointness, unitarity and involution.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the group algebra, its involution and its completions from *The Convolution Algebra $L^1(G)$* and *The Group Algebra as an Involutive Algebra*; the grade involution, the operator $\mathrm{A}$, the signed sandwich and its composition laws from *The Signed Sandwich on the Group Algebra*; the signed left multiplication $\Lambda_a = L_a\mathrm{A}$, its composition laws $\Lambda_a\Lambda_b = L_{a*\alpha(b)}$, $\Lambda_a^2 = L_{a*\alpha(a)}$, its invertibility, its fixed set and its relation to the sandwich from *The Signed Left Multiplication on the Group Algebra*; the reflection as the two-sided case from *Reflections as Signed Two-Sided Operators on the Group Algebra*; the adjoint of the signed sandwich from *The Signed Adjoint Sandwich on the Group Algebra*; the adjoint of the reflection from *The Signed Adjoint of the Reflection on the Group Algebra*, immediately preceding; and the adjoint on the group algebra from *Hermitian Operators on a Group Algebra*. The graded adjoint action on a module is next; the adjoint of a convolution operator on its own terms is *The Adjoint of a Convolution Operator*, later in this group; the discrete version is *The Signed Adjoint of the Left Multiplication on a Topological Group*.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$; $\mathcal{A} = L^1(G)$ carries the involution $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ and the Haar pairing; $\alpha$ is a **grade involution**, $\mathrm{A}f = \alpha(f)$, $\sigma = \alpha\circ\,^*$, $\sigma(a) = \alpha(a^*)$, and the **signed left multiplication** and its right-handed mirror are

$$
\Lambda_a = L_a\mathrm{A}, \quad \Lambda_a(f) = a*\alpha(f); \qquad \Lambda^{\mathrm R}_b = \mathrm{A}R_b, \quad \Lambda^{\mathrm R}_b(f) = \alpha(f)*b .
$$

The adjoint is taken with respect to the Haar pairing; the left-handed identities hold for every $G$ and the right-handed ones in the **unimodular** case.

## The Adjoint of the Signed Left Multiplication

**Theorem (the adjoint).** With respect to the Haar pairing,

$$
\bigl(\Lambda_a\bigr)^* = \mathrm{A}\,L_{a^*} = L_{\alpha(a^*)}\,\mathrm{A} = \Lambda_{\alpha(a^*)} = \Lambda_{\sigma(a)} ,
$$

and in the unimodular case $\bigl(\Lambda^{\mathrm R}_b\bigr)^* = \Lambda^{\mathrm R}_{\alpha(b^*)}$; the adjoint operation is an involution on the family of signed left multiplications, $\bigl((\Lambda_a)^*\bigr)^* = \Lambda_a$.

**Proof.** By the elementary adjoints $(L_a)^* = L_{a^*}$ and $\mathrm{A}^* = \mathrm{A}$, and the composition of adjoints, $(\Lambda_a)^* = (L_a\mathrm{A})^* = \mathrm{A}^*L_a^* = \mathrm{A}L_{a^*}$; the intertwining $\mathrm{A}L_c = L_{\alpha(c)}\mathrm{A}$ turns this into $L_{\alpha(a^*)}\mathrm{A} = \Lambda_{\alpha(a^*)}$. The right-handed formula is the mirror image. The double adjoint uses $\alpha^2 = \mathrm{id}$ and $a^{**} = a$. $\square$

**Corollary (compatibility with the composition laws).** The adjoint is compatible with the composition laws of the signed left multiplication,

$$
\bigl(\Lambda_a\Lambda_b\bigr)^* = \Lambda_b^*\Lambda_a^* = \Lambda_{\alpha(b^*)}\Lambda_{\alpha(a^*)} = L_{\alpha(b^*)*a^*} = L_{(a*\alpha(b))^*} = \bigl(L_{a*\alpha(b)}\bigr)^* ,
$$

and it preserves the coset $\Lambda(\mathcal{A}) = L(\mathcal{A})\mathrm{A}$, carrying the signed family to itself and the unsigned to the unsigned.

**Proof.** The first equality is the anti-automorphism property of the adjoint, the second the theorem, and the third the composition law $\Lambda_c\Lambda_d = L_{c*\alpha(d)}$; the identification with $L_{(a*\alpha(b))^*}$ uses $\alpha(b^*) = \alpha(b)^*$, which holds because the grade involution commutes with the involution (the sign character trivially, a measure-preserving group automorphism because $\Delta\circ\theta^{-1} = \Delta$). The coset statement is immediate from $\Lambda_a^* = \Lambda_{\alpha(a^*)}$. $\square$

**Corollary (the sandwich factorisation is adjoint-compatible).** Since the signed sandwich factorises as $S_{a,b} = \Lambda_a R_{\alpha(b)} = L_a\Lambda^{\mathrm R}_b$, the adjoint of the sandwich is the product of the adjoints of the factors in the reverse order, which is the identity $(S_{a,b})^* = S_{\alpha(a^*),\alpha(b^*)}$ of *The Signed Adjoint Sandwich on the Group Algebra*.

**Proof.** $S_{a,b} = \Lambda_aR_{\alpha(b)}$ and $(\Lambda_aR_{\alpha(b)})^* = R_{\alpha(b)}^*\Lambda_a^* = R_{\alpha(b)^*}\Lambda_{\alpha(a^*)} = S_{\alpha(a^*),\alpha(b^*)}$, using $\alpha(b)^* = \alpha(b^*)$ from the previous corollary. $\square$

## The Three Criteria

**Definition.** The signed left multiplication is **self-adjoint** when $\Lambda_a^* = \Lambda_a$, **unitary** when $\Lambda_a^*\Lambda_a = \Lambda_a\Lambda_a^* = 1$, and an **involution** when $\Lambda_a^2 = \mathrm{id}$.

**Theorem (the parametrisation is faithful).** The map $a\mapsto\Lambda_a$ is injective: $\Lambda_a = \Lambda_b$ if and only if $a = b$. Consequently $\Lambda_a^* = \Lambda_a$ if and only if $\sigma(a) = a$.

**Proof.** $\Lambda_a = \Lambda_b$ means $L_a\mathrm{A} = L_b\mathrm{A}$; composing with $\mathrm{A}^{-1} = \mathrm{A}$ on the right gives $L_a = L_b$, and left convolution is injective, so $a = b$. The self-adjointness criterion is then the theorem read with $\Lambda_{\alpha(a^*)} = \Lambda_a$. $\square$

**Theorem (self-adjointness and the fixed set of $\sigma$).** The signed left multiplication $\Lambda_a$ is self-adjoint if and only if $a$ lies in the fixed set of the composite anti-automorphism $\sigma = \alpha\circ\,^*$,

$$
\Lambda_a^* = \Lambda_a \iff \sigma(a) = a ,
$$

a closed real subspace of $\mathcal{A}$; on the point masses this is the fixed subgroup $G^\sigma$ of the continuous involution $\sigma = \alpha\iota$.

**Proof.** Immediate from the faithful parametrisation and the adjoint formula; the fixed set of an anti-linear involution is a closed real subspace, and on point masses $\sigma(\delta_x) = \delta_{\sigma(x)}$ gives the subgroup condition. $\square$

**Theorem (unitarity).** The signed left multiplication is unitary if and only if the parameter is a unitary element,

$$
\Lambda_a^*\Lambda_a = \Lambda_a\Lambda_a^* = 1 \iff a^*\!*a = a*\!a^* = 1 .
$$

On a non-discrete group algebra there are no unitary elements and no unitary signed left multiplication; on a discrete group every point mass gives a unitary operator $\Lambda_{\delta_g}$.

**Proof.** $\Lambda_{\alpha(a^*)}\Lambda_a = L_{\alpha(a^*)*\alpha(a)} = L_{\alpha(a^**a)}$ and $\Lambda_a\Lambda_{\alpha(a^*)} = L_{a*\alpha(\alpha(a^*))} = L_{a*a^*}$; left convolution is injective, so each product is the identity exactly when the corresponding convolution parameter is the identity, giving $a^*\!*a = 1$ and $a*\!a^* = 1$. The absence of unitary elements on a non-discrete $L^1(G)$, and the unitarity of the point masses $\delta_g^* = \delta_{g^{-1}}$, are *The Group Algebra as an Involutive Algebra*. $\square$

**Theorem (involution and the carrier).** The signed left multiplication is an involution if and only if $\alpha(a) = a^{-1}$, that is if and only if $a$ lies in the carrier of the inverted subgroup,

$$
\Lambda_a^2 = \mathrm{id} \iff a*\alpha(a) = 1 \iff \alpha(a) = a^{-1} \iff a\in I(\alpha) = G^\sigma .
$$

**Proof.** $\Lambda_a^2 = L_{a*\alpha(a)}$, and $L_{a*\alpha(a)} = \mathrm{id}$ exactly when $a*\alpha(a) = 1$ by the injectivity of left convolution; the carrier condition is the dictionary of *Involutive Topological Groups*. $\square$

**Corollary (the clean coincidence).** For the signed left multiplication the three criteria decouple as $\sigma(a) = a$, $a$ unitary, and $\alpha(a) = a^{-1}$; the operator of a point mass $\delta_g$ on a discrete group with the sign character is self-adjoint exactly when $g^2 = e$ and $\varepsilon(g) = 1$, unitary in every case, and an involution exactly when $\varepsilon(g)\,g = g^{-1}$, that is when $g^2 = e$ and $\varepsilon(g) = g^{-1}g$ — the last clause reducing to $\varepsilon(g) = 1$ on a $2$-torsion element.

**Proof.** The first clause is the three theorems restated; for $a = \delta_g$ and the sign character, $\sigma(a) = \alpha(a^*) = \alpha(\delta_{g^{-1}}) = \varepsilon(g^{-1})\delta_{g^{-1}} = \varepsilon(g)\delta_{g^{-1}}$, which equals $\delta_g$ exactly when $g^{-1} = g$ and $\varepsilon(g) = 1$, that is $g^2 = e$ and $\varepsilon(g) = 1$; the unitarity and the involution conditions specialise similarly, the involution condition $a*\alpha(a) = 1$ becoming $\varepsilon(g)\delta_{g^2} = \delta_e$. $\square$

## The Relation to the Sandwich and the Reflection

**Theorem (the one-sided operators inside the sandwich).** The signed sandwich factorises through the signed left multiplication, $S_{a,b} = \Lambda_aR_{\alpha(b)} = L_a\Lambda^{\mathrm R}_b$, and the signed left multiplication is the one-sided specialisation obtained by putting one factor equal to the identity, $S_{a,1} = \Lambda_a$ in the unital case; the adjoint formulas of the three articles agree where the families overlap.

**Proof.** $\Lambda_aR_{\alpha(b)}(f) = a*\alpha(f*b) = a*\alpha(f)*\alpha(b) = S_{a,b}(f)$; putting $b = 1$ gives $S_{a,1} = \Lambda_a$ in the unital case, and the adjoint formula $S_{\alpha(a^*),\alpha(b^*)}$ specialises at $b = 1$ to $\Lambda_{\alpha(a^*)}$. $\square$

**Corollary (the reflection case).** For the reflection $\rho_u = S_{u,u^{-1}}$ the adjoint is $\rho_{\alpha(u^*)} = \rho_{\sigma(u)}$, in agreement with *The Signed Adjoint of the Reflection on the Group Algebra*; the reflection is self-adjoint iff $\sigma(u)$ and $u$ determine the same reflection (a centrality condition), whereas the signed left multiplication is self-adjoint iff $\sigma(a) = a$ exactly, the difference being the non-faithfulness of the reflection parametrisation.

**Proof.** The adjoint of the reflection is the special case of the sandwich formula; the reflection $\rho_u = S_{u,u^{-1}} = \Lambda_uR_{\alpha(u^{-1})}$ is the two-sided case, and the identity criterion for reflections carries the central ambiguity that the faithful parametrisation of the signed left multiplications does not have. $\square$

## The Degenerate Cases

**Theorem (the trivial grade involution).** If $\alpha = \mathrm{id}$ then $\Lambda_a = L_a$ is the unsigned left convolution, and its adjoint is $L_{a^*}$: it is self-adjoint exactly when $a^* = a$, unitary exactly when $a$ is unitary, and an involution exactly when $a = 1$.

**Proof.** With $\mathrm{A} = \mathrm{id}$ the operator is $L_a$; the adjoint formula gives $L_{a^*}$, and the three criteria specialise the theorems with $\sigma = \,^*$ and $\alpha = \mathrm{id}$. $\square$

**Corollary (the inner grade involution).** If $\alpha = c_z$ then $\Lambda_a(f) = a*z*f*z^{-1} = L_{a*z}c_{z^{-1}}(f)$, the product of a left convolution and an inner automorphism, and the adjoint is $\Lambda_{\alpha(a^*)}$; the self-adjointness criterion becomes $\alpha(a^*) = a$, which is the conjugation by $z$ condition $z^{-1}*a*z\cdot$ fixed.

**Proof.** $\Lambda_a(f) = a*(z*f*z^{-1})$ by the inner form of the grade involution; the adjoint is the general formula, and the criterion is read on the parameters. $\square$

**Remark (what the article does not do).** The graded adjoint action on a module over the group algebra is the next article; the adjoint of a general convolution operator, its form on $L^p$ and the involutive algebra of convolution operators are *The Adjoint of a Convolution Operator*, the last of this group; the discrete version with the bilinear signed form, where the adjoint is $\Lambda_a^\dagger = \Lambda_{\alpha(a)^{-1}}$, is *The Signed Adjoint of the Left Multiplication on a Topological Group*. The grade involution is an automorphism and the involution an anti-automorphism; the composite $\sigma$ is what the adjoint of the signed left multiplication detects.

## Summary

The signed left multiplication $\Lambda_a = L_a\mathrm{A}$, $\Lambda_a(f) = a*\alpha(f)$, has adjoint $(\Lambda_a)^* = \mathrm{A}L_{a^*} = L_{\alpha(a^*)}\mathrm{A} = \Lambda_{\alpha(a^*)} = \Lambda_{\sigma(a)}$ with respect to the Haar pairing, $\sigma = \alpha\circ\,^*$; the adjoint is compatible with the composition laws, with the factorisation of the sandwich $S_{a,b} = \Lambda_aR_{\alpha(b)}$, and with the coset $\Lambda(\mathcal{A}) = L(\mathcal{A})\mathrm{A}$. Because the parametrisation $a\mapsto\Lambda_a$ is faithful, the three criteria are clean: the operator is self-adjoint exactly when $\sigma(a) = a$, that is when the parameter lies in the fixed set of the composite involution (the fixed subgroup $G^\sigma$ on the point masses), unitary exactly when $a$ is a unitary element (nonvacuous only on a discrete group or in the measure algebra), and an involution exactly when $\alpha(a) = a^{-1}$, that is when $a$ lies in the carrier of the inverted subgroup. The reflection is the two-sided case, where the non-faithful parametrisation replaces the fixed-point condition by a centrality condition, and the unsigned left convolution is recovered when the grade involution is trivial. The discrete version with the bilinear signed form is the neighbouring Part II article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda_a = L_a\mathrm{A}$, $\Lambda_a(f) = a*\alpha(f)$ | The signed left multiplication |
| $\Lambda^{\mathrm R}_b = \mathrm{A}R_b$ | The signed right multiplication |
| $\sigma = \alpha\circ\,^*$, $\sigma(a) = \alpha(a^*)$ | The composite anti-automorphism |
| $(\Lambda_a)^* = \Lambda_{\alpha(a^*)}$ | The adjoint |
| $\Lambda_a\Lambda_b = L_{a*\alpha(b)}$, $\Lambda_a^2 = L_{a*\alpha(a)}$ | The composition laws |
| $\Lambda_a^* = \Lambda_a\iff\sigma(a) = a$ | Self-adjointness criterion |
| $\Lambda_a^*\Lambda_a = 1\iff a$ unitary | Unitarity criterion |
| $\Lambda_a^2 = \mathrm{id}\iff\alpha(a) = a^{-1}$ | The involution carrier $I(\alpha) = G^\sigma$ |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the adjoint, self-adjointness, unitarity and the involutions of an operator algebra.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the involutive algebra of the group and its fixed subspaces.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the composite of an automorphism and an involution and the carriers it defines.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, second edition, 1979), for the involution, the unitary elements and the point masses of the group algebra.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the signed left multiplication, its adjoint and the coset it forms.
