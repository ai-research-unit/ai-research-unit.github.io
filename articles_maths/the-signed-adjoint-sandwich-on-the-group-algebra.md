
# __The Signed Adjoint Sandwich on the Group Algebra__

## Introduction

The signed sandwich is the two-sided operator $f\mapsto a*\alpha(f)*b$, built from the two convolutions and the grade involution, and its adjoint with respect to the Haar pairing is another signed sandwich, with both parameters carried through the composite of the grade involution and the involution of the algebra. The adjoint turns out to be an involution on the family of signed sandwiches, compatible with their coset structure and their composition law, and the comparison of the adjoint with the inverse gives the unitarity condition: a signed sandwich is unitary exactly when both its parameters are unitary elements of the algebra, which on the group algebra forces the group to be discrete or the reading to be taken in the measure algebra. The elements fixed by the composite involution give self-adjoint sandwiches. This article computes the adjoint, states the unitarity and self-adjointness criteria, and records the degenerate cases.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the group algebra, its involution and the regular representation from *The Convolution Algebra $L^1(G)$*, *The Group Algebra as an Involutive Algebra*, *The Group Algebra as an Algebra of Operators* and *The Left and Right Regular Representation*; the grade involution $\alpha$, the operator $\mathrm{A}f = \alpha(f)$, the signed and unsigned sandwiches, their composition laws, their inverses and the signed conjugations from *The Signed Sandwich on the Group Algebra*; the signed left multiplication from *The Signed Left Multiplication on the Group Algebra*; the adjoints of the elementary operators, $(L_a)^* = L_{a^*}$, $(R_b)^* = R_{b^*}$, $\mathrm{A}^* = \mathrm{A}$, from *Hermitian Operators on a Group Algebra* and *Unitary Representations and the Adjoint*, immediately preceding; the involution on the measure algebra from *The Involution on the Measure Algebra*; and the bounded operators and the adjoint from *Operator Algebras*. The signed adjoint of the reflection and of the left multiplication are *The Signed Adjoint of the Reflection on the Group Algebra* and *The Signed Adjoint of the Left Multiplication on the Group Algebra*, next; the adjoint of a convolution operator on its own terms is *The Adjoint of a Convolution Operator*, the last article of this group; the discrete version, with the natural and signed bilinear forms, is *The Signed Adjoint Sandwich on a Topological Group*.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$; $\mathcal{A} = L^1(G)$ carries the involution $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ and the **Haar pairing** $\langle f,h\rangle = \int_G f\overline{h}\,dx$; $\alpha$ is a **grade involution**, a continuous involutive automorphism of the Banach algebra $\mathcal{A}$ (a sign character or a measure-preserving group automorphism), $\mathrm{A}f = \alpha(f)$, and the **unsigned** and **signed sandwiches** are

$$
T_{a,b} = L_aR_b, \quad T_{a,b}(f) = a*f*b ; \qquad S_{a,b} = L_a\mathrm{A}R_b, \quad S_{a,b}(f) = a*\alpha(f)*b .
$$

The adjoint is taken with respect to the Haar pairing; the right-handed identities are stated in the **unimodular** case, the left-handed ones hold for every $G$.

## The Adjoints of the Elementary Operators

**Theorem (recalled).** With respect to the Haar pairing,

$$
(L_a)^* = L_{a^*}\ \ (\text{every } G), \qquad (R_b)^* = R_{b^*}, \qquad \mathrm{A}^* = \mathrm{A}\ \ (\text{unimodular } G),
$$

and the adjoint is an anti-linear involution, $(ST)^* = T^*S^*$, $(T^*)^* = T$.

**Proof.** These are the computations of *Hermitian Operators on a Group Algebra*, obtained from the unitary representation $\lambda$ for the left identity and from the right regular representation in the unimodular case for the right identity; the operator identities are general. $\square$

**Corollary (the inversion in the parameter).** $a^{**} = a$ and $(a^{-1})^* = (a^*)^{-1}$, so the adjoint of an elementary operator is the elementary operator of the involuted parameter; for a point mass $\delta_x$ on a discrete group, $\delta_x^* = \delta_{x^{-1}}$ and $(L_{\delta_x})^* = L_{\delta_{x^{-1}}}$.

**Proof.** $(a^{-1})^* = (a^*)^{-1}$ is the anti-automorphism law applied to $a*a^{-1} = 1$; the point-mass statement is the discrete case of $a^*$. $\square$

## The Adjoint of the Signed Sandwich

**Theorem (the explicit form of the adjoint).** With respect to the Haar pairing, in the unimodular case,

$$
\bigl(T_{a,b}\bigr)^* = T_{a^*,\,b^*} , \qquad \bigl(S_{a,b}\bigr)^* = S_{\alpha(a^*),\,\alpha(b^*)} ,
$$

and the adjoint operation is an involution on each family, $\bigl((S_{a,b})^*\bigr)^* = S_{a,b}$.

**Proof.** By the anti-automorphism property and the elementary adjoints, $(S_{a,b})^* = (L_a\mathrm{A}R_b)^* = R_b^*\mathrm{A}^*L_a^* = R_{b^*}\mathrm{A}L_{a^*}$. Now $\mathrm{A}L_c = L_{\alpha(c)}\mathrm{A}$ and $R_d\mathrm{A} = \mathrm{A}R_{\alpha^{-1}(d)} = \mathrm{A}R_{\alpha(d)}$, so $R_{b^*}\mathrm{A}L_{a^*} = L_{\alpha(a^*)}\mathrm{A}R_{\alpha(b^*)} = S_{\alpha(a^*),\alpha(b^*)}$. The unsigned formula is the case $\alpha = \mathrm{id}$ read off the same computation, and the double adjoint uses $\alpha^2 = \mathrm{id}$ and $a^{**} = a$. $\square$

**Corollary (compatibility with the coset structure and the composition law).** The adjoint carries the signed sandwiches to the signed sandwiches and the unsigned to the unsigned, and it is compatible with the composition law of *The Signed Sandwich on the Group Algebra*,

$$
\bigl(S_{c,d}S_{a,b}\bigr)^* = S_{a,b}^*\,S_{c,d}^* , \qquad S_{a,b}^* = T_{a,b}^*\,\mathrm{A} = S_{\alpha(a^*),\alpha(b^*)} ,
$$

and it respects the coset decomposition $S_{a,b} = T_{a,b}\mathrm{A}$, carrying $\mathrm{A}$ to itself.

**Proof.** The first identity is the anti-automorphism property of the adjoint applied to the composition; the second is the decomposition $S_{a,b}^* = (T_{a,b}\mathrm{A})^* = \mathrm{A}^*T_{a,b}^* = \mathrm{A}T_{a^*,b^*}$ and the intertwining relations; the coset statement is immediate from $\mathrm{A}^* = \mathrm{A}$. $\square$

## The Unitarity Condition

**Definition.** A signed sandwich is **unitary** when $S_{a,b}^*S_{a,b} = 1$ and $S_{a,b}S_{a,b}^* = 1$; equivalently when it preserves the Haar pairing, $\langle S_{a,b}f,S_{a,b}h\rangle = \langle f,h\rangle$ for all $f,h$.

**Theorem (the unitarity criterion).** In the unital case (in particular for a discrete group, or in the measure algebra $M(G)$) the signed sandwich $S_{a,b}$ is unitary if and only if both parameters are unitary elements of $\mathcal{A}$,

$$
S_{a,b}^*S_{a,b} = S_{a,b}S_{a,b}^* = 1 \iff a^*\!*a = a*\!a^* = 1 \ \text{and}\ b^*\!*b = b*\!b^* = 1 .
$$

On the group algebra $L^1(G)$ of a non-discrete group there are no unitary elements, so no signed sandwich is unitary there; the unitarity condition is nonvacuous exactly on a discrete group or in the measure algebra, where the point masses are unitary.

**Proof.** By the composition law, $S_{\alpha(a^*),\alpha(b^*)}S_{a,b} = T_{\alpha(a^*)*\alpha(a),\,\alpha(b)*\alpha(b^*)}$ and $S_{a,b}S_{\alpha(a^*),\alpha(b^*)} = T_{a*a^*,\,b^*\!*b}$; the identity criterion for unsigned sandwiches, $T_{c,d} = 1$ iff $c = d = 1$ in the unital case, gives $\alpha(a^*\!*a) = 1$ and $\alpha(b*\!b^*) = 1$ for the first product and $a*a^* = 1$, $b^*\!*b = 1$ for the second. Applying $\alpha^{-1}$ and combining, the condition is that $a$ and $b$ be unitary. The absence of unitary elements on a non-discrete $L^1(G)$ is *The Group Algebra as an Involutive Algebra*. $\square$

**Corollary (the fixed elements give self-adjoint sandwiches).** If $\alpha(a^*) = a$ and $\alpha(b^*) = b$, then $S_{a,b}^* = S_{a,b}$, so the sandwich is self-adjoint; the elements fixed by the composite anti-automorphism $\sigma = \alpha\circ\,^*$ form a closed real subspace, and the self-adjoint signed sandwiches are exactly those whose parameters lie in it, up to the identification of the sandwich map.

**Proof.** $S_{a,b}^* = S_{\alpha(a^*),\alpha(b^*)} = S_{a,b}$ by the hypothesis; the fixed set of an anti-linear involution is a closed real subspace, and the last statement is the definition of the sandwich map read on the parameters. $\square$

## The Sandwich Identity Criterion

**Proposition (the identity criterion, recalled).** In the unital case two signed sandwiches coincide,

$$
S_{c,d} = S_{a,b} \iff c^{-1}a \in Z(\mathcal{A})^\times \ \text{and}\ c^{-1}a = b\,d^{-1} ,
$$

the criterion of *The Signed Sandwich on a Topological Group*, read in the measure algebra; consequently the map $(a,b)\mapsto S_{a,b}$ is injective exactly on the pairs modulo the central relation, and the self-adjointness criterion of the corollary is exact.

**Proof.** $S_{c,d} = S_{a,b}$ means $c*\alpha(f)*d = a*\alpha(f)*b$ for all $f$; since $\alpha$ is onto this says $c^{-1}a$ commutes with every $\alpha(f)$, that is with all of $\mathcal{A}$, and equals $b d^{-1}$; the criterion follows. The parametric description of the self-adjoint sandwiches is then immediate from the adjoint formula. $\square$

## The Degenerate Cases

**Theorem (the trivial grade involution).** If $\alpha = \mathrm{id}$ then every signed sandwich is unsigned, $S_{a,b} = T_{a,b}$, and its adjoint is $T_{a^*,b^*}$; every unsigned sandwich with unitary parameters is unitary.

**Proof.** With $\alpha = \mathrm{id}$ the operator $\mathrm{A}$ is the identity, $S_{a,b} = T_{a,b}$, and the adjoint formula collapses to $(T_{a,b})^* = T_{a^*,b^*}$; the unitarity criterion is the last theorem with $\alpha = \mathrm{id}$. $\square$

**Corollary (the inner grade involution).** If $\alpha = c_z$ is inner, $S_{a,b} = T_{a*z,\,z^{-1}*b}$, and the adjoint is $(S_{a,b})^* = T_{(a*z)^*,\,(z^{-1}*b)^*}$; the signed adjoint differs from the unsigned adjoint of the transported sandwich by the transport only, and the unitarity criterion is unchanged.

**Proof.** The transport is that of *The Signed Sandwich on the Group Algebra*; the adjoint formula applied to the transported parameters gives the displayed expression, and unitarity is invariant under a transport by a fixed element because $z$ cancels. $\square$

**Remark (what the article does not do).** The adjoint of the reflection and of the signed left multiplication are the next two articles; the adjoint of a general convolution operator, its expression on $L^p$ and the involutive algebra it generates are *The Adjoint of a Convolution Operator*; the discrete version with the natural and signed bilinear forms, where the adjoint relation is $(L_a)^\dagger = L_{a^{-1}}$, is *The Signed Adjoint Sandwich on a Topological Group*, and the two forms are reconciled by the passage from the bilinear form to the Haar pairing through the involution $a\mapsto a^*$.

## Summary

With respect to the Haar pairing the elementary operators have adjoints $(L_a)^* = L_{a^*}$ (every $G$) and, in the unimodular case, $(R_b)^* = R_{b^*}$ and $\mathrm{A}^* = \mathrm{A}$; the signed sandwich $S_{a,b}(f) = a*\alpha(f)*b = L_a\mathrm{A}R_b$ therefore has adjoint $S_{\alpha(a^*),\alpha(b^*)}$, the unsigned sandwich $T_{a,b}$ has adjoint $T_{a^*,b^*}$, and the adjoint is an involution on each family, compatible with the coset decomposition $S_{a,b} = T_{a,b}\mathrm{A}$ and with the composition law. The sandwich $S_{a,b}$ is unitary exactly when $a$ and $b$ are unitary elements — nonvacuous only on a discrete group or in the measure algebra, where the point masses are unitary — and it is self-adjoint exactly when its parameters are fixed by the composite anti-automorphism $\sigma = \alpha\circ\,^*$, the sandwich identity criterion being the one recalled from the discrete theory. When the grade involution is trivial the signed family collapses to the unsigned, and when it is inner the signed adjoint is the unsigned adjoint of the transported sandwich. The adjacency with the discrete theory is the passage from the bilinear form of *The Signed Adjoint Sandwich on a Topological Group* to the Haar pairing through the involution.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{a,b}(f) = a*f*b$ | The unsigned sandwich |
| $S_{a,b}(f) = a*\alpha(f)*b = L_a\mathrm{A}R_b$ | The signed sandwich |
| $(L_a)^* = L_{a^*}$, $(R_b)^* = R_{b^*}$ | Elementary adjoints, Haar pairing |
| $\mathrm{A}^* = \mathrm{A}$ | The grade-involution operator is self-adjoint |
| $(T_{a,b})^* = T_{a^*,b^*}$ | The unsigned adjoint |
| $(S_{a,b})^* = S_{\alpha(a^*),\alpha(b^*)}$ | The signed adjoint |
| $(S_{a,b})^*S_{a,b} = 1\iff a,b$ unitary | The unitarity criterion |
| $\sigma = \alpha\circ\,^*$ | The composite anti-automorphism fixing the self-adjoint sandwiches |
| $S_{c,d} = S_{a,b}\iff c^{-1}a\in Z^\times,\ c^{-1}a = bd^{-1}$ | The sandwich identity criterion |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutions, their composites and the self-adjoint elements.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the adjoint, unitarity and the form-preserving operators.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the group von Neumann algebra and the unitarity of its operators.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, second edition, 1979), for the involution on the group algebra and the unitary elements.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the sandwich action, its adjoint and the groups it generates.
