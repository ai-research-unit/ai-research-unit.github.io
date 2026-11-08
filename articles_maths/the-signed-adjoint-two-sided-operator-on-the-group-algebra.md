
# __The Signed Adjoint Two-Sided Operator on the Group Algebra__

## Introduction

The signed two-sided operator is the two-sided operator $f\mapsto a*\alpha(f)*b$, built from the two convolutions and the grade involution, and its adjoint with respect to the Haar pairing is another signed two-sided operator, with both parameters carried through the composite of the grade involution and the involution of the algebra. The adjoint turns out to be an involution on the family of signed two-sided operators, compatible with their coset structure and their composition law, and the comparison of the adjoint with the inverse gives the unitarity condition: a signed two-sided operator is unitary exactly when both its parameters are unitary elements of the algebra, which on the group algebra forces the group to be discrete or the reading to be taken in the measure algebra. The elements fixed by the composite involution give self-adjoint two-sided operators. This article computes the adjoint, states the unitarity and self-adjointness criteria, and records the degenerate cases.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the group algebra, its involution and the regular representation from *The Convolution Algebra $L^1(G)$*, *The Group Algebra as an Involutive Algebra*, *The Group Algebra as an Algebra of Operators* and *The Left and Right Regular Representation*; the grade involution $\alpha$, the operator $\mathrm{A}f = \alpha(f)$, the signed and unsigned two-sided operators, their composition laws, their inverses and the signed conjugations from *The Signed Two-Sided Operator on the Group Algebra*; the signed left multiplication from *The Signed Left Multiplication on the Group Algebra*; the adjoints of the elementary operators, $(L_a)^* = L_{a^*}$, $(R_b)^* = R_{b^*}$, $\mathrm{A}^* = \mathrm{A}$, from *Hermitian Operators on a Group Algebra* and *Unitary Representations and the Adjoint*, immediately preceding; the involution on the measure algebra from *The Involution on the Measure Algebra*; and the bounded operators and the adjoint from *Operator Algebras*. The signed adjoint of the reflection and of the left multiplication are *The Signed Adjoint of the Reflection on the Group Algebra* and *The Signed Adjoint of the Left Multiplication on the Group Algebra*, next; the adjoint of a convolution operator on its own terms is *The Adjoint of a Convolution Operator*, the last article of this group; the discrete version, with the natural and signed bilinear forms, is *The Signed Adjoint Two-Sided Operator on a Topological Group*.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$; $\mathcal{A} = L^1(G)$ carries the involution $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ and the **Haar pairing** $\langle f,h\rangle = \int_G f\overline{h}\,dx$; $\alpha$ is a **grade involution**, a continuous involutive automorphism of the Banach algebra $\mathcal{A}$ (a sign character or a measure-preserving group automorphism), $\mathrm{A}f = \alpha(f)$, and the **unsigned** and **signed two-sided operators** are

$$
L_{a}R_{b}, \quad L_{a}R_{b}(f) = a*f*b ; \qquad \mathcal{T}_{a,b} = L_a\mathrm{A}R_b, \quad \mathcal{T}_{a,b}(f) = a*\alpha(f)*b .
$$

The adjoint is taken with respect to the Haar pairing; the right-handed identities are stated in the **unimodular** case, the left-handed ones hold for every $G$.

## The Adjoints of the Elementary Operators

**Theorem (recalled).** With respect to the Haar pairing,

$$
(L_a)^* = L_{a^*}\ \ (\text{every } G), \qquad (R_b)^* = R_{b^*}, \qquad \mathrm{A}^* = \mathrm{A}\ \ (\text{unimodular } G),
$$

and the adjoint is an anti-linear involution, $(ST)^* = T^*S^*$, $(T^*)^* = T$.

**Proof.** These are the computations of *Hermitian Operators on a Group Algebra*, obtained from the unitary representation $\lambda$ for the left identity and from the right regular representation in the unimodular case for the right identity; the operator identities are general.

**Corollary (the inversion in the parameter).** $a^{**} = a$ and $(a^{-1})^* = (a^*)^{-1}$, so the adjoint of an elementary operator is the elementary operator of the involuted parameter; for a point mass $\delta_x$ on a discrete group, $\delta_x^* = \delta_{x^{-1}}$ and $(L_{\delta_x})^* = L_{\delta_{x^{-1}}}$.

**Proof.** $(a^{-1})^* = (a^*)^{-1}$ is the anti-automorphism law applied to $a*a^{-1} = 1$; the point-mass statement is the discrete case of $a^*$.

## The Adjoint of the Signed Two-Sided Operator

**Theorem (the explicit form of the adjoint).** With respect to the Haar pairing, in the unimodular case,

$$
\boxed{\;\bigl(L_{a}R_{b}\bigr)^* = L_{a^*}R_{\,b^*} , \qquad \bigl(\mathcal{T}_{a,b}\bigr)^* = \mathcal{T}_{\alpha(a^*),\,\alpha(b^*)}\;} ,
$$

and the adjoint operation is an involution on each family, $\bigl((\mathcal{T}_{a,b})^*\bigr)^* = \mathcal{T}_{a,b}$.

**Proof.** By the anti-automorphism property and the elementary adjoints, $(\mathcal{T}_{a,b})^* = (L_a\mathrm{A}R_b)^* = R_b^*\mathrm{A}^*L_a^* = R_{b^*}\mathrm{A}L_{a^*}$. Now $\mathrm{A}L_c = L_{\alpha(c)}\mathrm{A}$ and $R_d\mathrm{A} = \mathrm{A}R_{\alpha^{-1}(d)} = \mathrm{A}R_{\alpha(d)}$, so $R_{b^*}\mathrm{A}L_{a^*} = L_{\alpha(a^*)}\mathrm{A}R_{\alpha(b^*)} = \mathcal{T}_{\alpha(a^*),\alpha(b^*)}$. The unsigned formula is the case $\alpha = \mathrm{id}$ read off the same computation, and the double adjoint uses $\alpha^2 = \mathrm{id}$ and $a^{**} = a$.

**Corollary (compatibility with the coset structure and the composition law).** The adjoint carries the signed two-sided operators to the signed two-sided operators and the unsigned to the unsigned, and it is compatible with the composition law of *The Signed Two-Sided Operator on the Group Algebra*,

$$
\boxed{\;\bigl(\mathcal{T}_{c,d}\mathcal{T}_{a,b}\bigr)^* = \mathcal{T}_{a,b}^*\,\mathcal{T}_{c,d}^* , \qquad \mathcal{T}_{a,b}^* = L_{a}R_{b}^*\,\mathrm{A} = \mathcal{T}_{\alpha(a^*),\alpha(b^*)}\;} ,
$$

and it respects the coset decomposition $\mathcal{T}_{a,b} = L_{a}R_{b}\mathrm{A}$, carrying $\mathrm{A}$ to itself.

**Proof.** The first identity is the anti-automorphism property of the adjoint applied to the composition; the second is the decomposition $\mathcal{T}_{a,b}^* = (L_{a}R_{b}\mathrm{A})^* = \mathrm{A}^*L_{a}R_{b}^* = \mathrm{A}L_{a^*}R_{b^*}$ and the intertwining relations; the coset statement is immediate from $\mathrm{A}^* = \mathrm{A}$.

## The Unitarity Condition

**Definition.** A signed two-sided operator is **unitary** when $\mathcal{T}_{a,b}^*\mathcal{T}_{a,b} = 1$ and $\mathcal{T}_{a,b}\mathcal{T}_{a,b}^* = 1$; equivalently when it preserves the Haar pairing, $\langle \mathcal{T}_{a,b}f,\mathcal{T}_{a,b}h\rangle = \langle f,h\rangle$ for all $f,h$.

**Theorem (the unitarity criterion).** In the unital case (in particular for a discrete group, or in the measure algebra $M(G)$) the signed two-sided operator $\mathcal{T}_{a,b}$ is unitary if and only if both parameters are unitary elements of $\mathcal{A}$,

$$
\boxed{\;\mathcal{T}_{a,b}^*\mathcal{T}_{a,b} = \mathcal{T}_{a,b}\mathcal{T}_{a,b}^* = 1 \iff a^*\!*a = a*\!a^* = 1 \ \text{and}\ b^*\!*b = b*\!b^* = 1\;} .
$$

On the group algebra $L^1(G)$ of a non-discrete group there are no unitary elements, so no signed two-sided operator is unitary there; the unitarity condition is nonvacuous exactly on a discrete group or in the measure algebra, where the point masses are unitary.

**Proof.** By the composition law, $\mathcal{T}_{\alpha(a^*),\alpha(b^*)}\mathcal{T}_{a,b} = L_{\alpha(a^*)*\alpha(a)}R_{\,\alpha(b)*\alpha(b^*)}$ and $\mathcal{T}_{a,b}\mathcal{T}_{\alpha(a^*),\alpha(b^*)} = L_{a*a^*}R_{\,b^*\!*b}$; the identity criterion for unsigned two-sided operators, $L_{c}R_{d} = 1$ iff $c = d = 1$ in the unital case, gives $\alpha(a^*\!*a) = 1$ and $\alpha(b*\!b^*) = 1$ for the first product and $a*a^* = 1$, $b^*\!*b = 1$ for the second. Applying $\alpha^{-1}$ and combining, the condition is that $a$ and $b$ be unitary. The absence of unitary elements on a non-discrete $L^1(G)$ is *The Group Algebra as an Involutive Algebra*.

**Corollary (the fixed elements give self-adjoint two-sided operators).** If $\alpha(a^*) = a$ and $\alpha(b^*) = b$, then $\mathcal{T}_{a,b}^* = \mathcal{T}_{a,b}$, so the two-sided operator is self-adjoint; the elements fixed by the composite anti-automorphism $\sigma = \alpha\circ\,{}^{*}$ form a closed real subspace, and the self-adjoint signed two-sided operators are exactly those whose parameters lie in it, up to the identification of the two-sided map.

**Proof.** $\mathcal{T}_{a,b}^* = \mathcal{T}_{\alpha(a^*),\alpha(b^*)} = \mathcal{T}_{a,b}$ by the hypothesis; the fixed set of an anti-linear involution is a closed real subspace, and the last statement is the definition of the two-sided map read on the parameters.

## The Two-Sided Identity Criterion

**Proposition (the identity criterion, recalled).** In the unital case two signed two-sided operators coincide,

$$
\mathcal{T}_{c,d} = \mathcal{T}_{a,b} \iff c^{-1}a \in Z(\mathcal{A})^\times \ \text{and}\ c^{-1}a = b\,d^{-1} ,
$$

the criterion of *The Signed Two-Sided Operator on a Topological Group*, read in the measure algebra; consequently the map $(a,b)\mapsto \mathcal{T}_{a,b}$ is injective exactly on the pairs modulo the central relation, and the self-adjointness criterion of the corollary is exact.

**Proof.** $\mathcal{T}_{c,d} = \mathcal{T}_{a,b}$ means $c*\alpha(f)*d = a*\alpha(f)*b$ for all $f$; since $\alpha$ is onto this says $c^{-1}a$ commutes with every $\alpha(f)$, that is with all of $\mathcal{A}$, and equals $b d^{-1}$; the criterion follows. The parametric description of the self-adjoint two-sided operators is then immediate from the adjoint formula.

## The Degenerate Cases

**Theorem (the trivial grade involution).** If $\alpha = \mathrm{id}$ then every signed two-sided operator is unsigned, $\mathcal{T}_{a,b} = L_{a}R_{b}$, and its adjoint is $L_{a^*}R_{b^*}$; every unsigned two-sided operator with unitary parameters is unitary.

**Proof.** With $\alpha = \mathrm{id}$ the operator $\mathrm{A}$ is the identity, $\mathcal{T}_{a,b} = L_{a}R_{b}$, and the adjoint formula collapses to $(L_{a}R_{b})^* = L_{a^*}R_{b^*}$; the unitarity criterion is the last theorem with $\alpha = \mathrm{id}$.

**Corollary (the inner grade involution).** If $\alpha = c_z$ is inner, $\mathcal{T}_{a,b} = L_{a*z}R_{\,z^{-1}*b}$, and the adjoint is $(\mathcal{T}_{a,b})^* = L_{(a*z)^*}R_{\,(z^{-1}*b)^*}$; the signed adjoint differs from the unsigned adjoint of the two-sided operator transported by the transport only, and the unitarity criterion is unchanged.

**Proof.** The transport is that of *The Signed Two-Sided Operator on the Group Algebra*; the adjoint formula applied to the transported parameters gives the displayed expression, and unitarity is invariant under a transport by a fixed element because $z$ cancels.

**Remark (what the article does not do).** The adjoint of the reflection and of the signed left multiplication are the next two articles; the adjoint of a general convolution operator, its expression on $L^{n}$ and the involutive algebra it generates are *The Adjoint of a Convolution Operator*; the discrete version with the natural and signed bilinear forms, where the adjoint relation is $(L_a)^\dagger = L_{a^{-1}}$, is *The Signed Adjoint Two-Sided Operator on a Topological Group*, and the two forms are reconciled by the passage from the bilinear form to the Haar pairing through the involution $a\mapsto a^*$.

## Summary

With respect to the Haar pairing the elementary operators have adjoints $(L_a)^* = L_{a^*}$ (every $G$) and, in the unimodular case, $(R_b)^* = R_{b^*}$ and $\mathrm{A}^* = \mathrm{A}$; the signed two-sided operator $\mathcal{T}_{a,b}(f) = a*\alpha(f)*b = L_a\mathrm{A}R_b$ therefore has adjoint $\mathcal{T}_{\alpha(a^*),\alpha(b^*)}$, the unsigned two-sided operator $L_{a}R_{b}$ has adjoint $L_{a^*}R_{b^*}$, and the adjoint is an involution on each family, compatible with the coset decomposition $\mathcal{T}_{a,b} = L_{a}R_{b}\mathrm{A}$ and with the composition law. The two-sided operator $\mathcal{T}_{a,b}$ is unitary exactly when $a$ and $b$ are unitary elements — nonvacuous only on a discrete group or in the measure algebra, where the point masses are unitary — and it is self-adjoint exactly when its parameters are fixed by the composite anti-automorphism $\sigma = \alpha\circ\,{}^{*}$, the two-sided identity criterion being the one recalled from the discrete theory. When the grade involution is trivial the signed family collapses to the unsigned, and when it is inner the signed adjoint is the unsigned adjoint of the transported two-sided operator. The adjacency with the discrete theory is the passage from the bilinear form of *The Signed Adjoint Two-Sided Operator on a Topological Group* to the Haar pairing through the involution.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{a}R_{b}(f) = a*f*b$ | The unsigned two-sided operator |
| $\mathcal{T}_{a,b}(f) = a*\alpha(f)*b = L_a\mathrm{A}R_b$ | The signed two-sided operator |
| $(L_a)^* = L_{a^*}$, $(R_b)^* = R_{b^*}$ | Elementary adjoints, Haar pairing |
| $\mathrm{A}^* = \mathrm{A}$ | The grade-involution operator is self-adjoint |
| $(L_{a}R_{b})^* = L_{a^*}R_{b^*}$ | The unsigned adjoint |
| $(\mathcal{T}_{a,b})^* = \mathcal{T}_{\alpha(a^*),\alpha(b^*)}$ | The signed adjoint |
| $(\mathcal{T}_{a,b})^*\mathcal{T}_{a,b} = 1\iff a,b$ unitary | The unitarity criterion |
| $\sigma = \alpha\circ\,{}^{*}$ | The composite anti-automorphism fixing the self-adjoint two-sided operators |
| $\mathcal{T}_{c,d} = \mathcal{T}_{a,b}\iff c^{-1}a\in Z^\times,\ c^{-1}a = bd^{-1}$ | The two-sided identity criterion |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutions, their composites and the self-adjoint elements.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the adjoint, unitarity and the form-preserving operators.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the group von Neumann algebra and the unitarity of its operators.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, second edition, 1979), for the involution on the group algebra and the unitary elements.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the two-sided action, its adjoint and the groups it generates.
