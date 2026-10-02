
# __The Signed Adjoint Sandwich on a Topological Group__

## Introduction

The signed sandwich is the two-sided operator $u\mapsto a\,\alpha(u)\,b$ built from the multiplication and the grade involution, and its adjoint is taken with respect to the signed form of the category, the natural form twisted by the grade involution. The adjoint turns out to be the signed sandwich with both parameters inverted, and the comparison of the adjoint with the inverse produces the unitarity condition: a signed sandwich is unitary exactly when a certain product is central, and the sandwiches whose parameters lie in the fixed subgroup of the grade involution are always unitary and form a subgroup. This is the operator-theoretic counterpart of the reflection theory, since the signed conjugations are the signed sandwiches with the second parameter the inverse of the first.

The article assumes the natural and signed forms, the adjoints of the left and right multiplications and of the linear extension $A$ of the grade involution from *The Adjoint of the Left Multiplication on a Topological Group*; the signed sandwich, its factorisation, its composition laws, its inverse and the signed conjugation from *The Signed Sandwich on a Topological Group*; and the continuous involution, the associated involutive automorphism and the fixed subgroup from *Involutive Topological Groups*. The reflection read as an operator and its own adjoint occupy *The Signed Adjoint of the Reflection on a Topological Group*; the Haar pairing and the adjoint of a convolution operator under it are Part III.

Throughout, $G$ is a Hausdorff topological group, $k$ is a field, $k[G]$ is the group algebra with basis $G$, $\sigma$ is a continuous involution, $\alpha = \sigma\iota$ is the associated continuous involutive automorphism, $A u = \sum_g u_g\,\alpha(g)$ is its linear extension, and the **signed sandwich** is the operator

$$
\Sigma^{\alpha}_{a,b} : k[G] \longrightarrow k[G] , \qquad \Sigma^{\alpha}_{a,b}(u) = a\,\alpha(u)\,b = (L_aR_bA)(u) .
$$

## The Adjoints of the Elementary Operators

**Theorem (recalled).** With respect to the signed form $B_\alpha(u,v) = \sum_g u_gv_{\alpha(g)}$ the translations and the linear extension of the involution satisfy

$$
(L_a)^\dagger = L_{\sigma(a)} , \qquad (R_b)^\dagger = R_{\sigma(b)} , \qquad A^\dagger = A , \qquad (ST)^\dagger = T^\dagger S^\dagger .
$$

**Proof.** These are the adjoint computations of *The Adjoint of the Left Multiplication on a Topological Group*, and the anti-automorphism property of the adjoint with respect to a bilinear form.

**Corollary (the inversion in the parameter).** $\sigma(a) = \alpha(a)^{-1} = \alpha(a^{-1})$ for every $a$, so the signed adjoint of a translation is the translation by the image of the element under the involution, and the operator $A$ implementing the grade involution is self-adjoint.

## The Adjoint of the Signed Sandwich

**Theorem (the explicit form of the adjoint).** With respect to the signed form,

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^\dagger = \Sigma^{\alpha}_{a^{-1},\,b^{-1}} .
$$

Equivalently, the adjoint of $u\mapsto a\alpha(u)b$ is $u\mapsto a^{-1}\alpha(u)b^{-1}$, and the adjoint operation is an involution on the set of signed sandwiches: $((\Sigma^{\alpha}_{a,b})^\dagger)^\dagger = \Sigma^{\alpha}_{a,b}$.

**Proof.** By the composition and the anti-automorphism property, $(\Sigma^\alpha_{a,b})^\dagger = (L_aR_bA)^\dagger = A^\dagger R_b^\dagger L_a^\dagger = A\,R_{\sigma(b)}\,L_{\sigma(a)}$. Applying this to $u$ gives $A(\sigma(a)\,u\,\sigma(b)) = \alpha(\sigma(a))\,\alpha(u)\,\alpha(\sigma(b))$. Since $\alpha$ and $\iota$ commute, $\alpha\sigma = \alpha\iota\alpha = \iota\alpha^2 = \iota$, so $\alpha\sigma(a) = a^{-1}$ and $\alpha\sigma(b) = b^{-1}$; hence the adjoint is $u\mapsto a^{-1}\alpha(u)b^{-1}$, which is $\Sigma^\alpha_{a^{-1},b^{-1}}$. The double adjoint is immediate from $\sigma^2 = \mathrm{id}$.

**Corollary (the adjoint respects the coset structure).** The adjoint carries the unsigned sandwiches to the unsigned sandwiches and the signed ones to the signed ones, and it is compatible with the composition law of *The Signed Sandwich on a Topological Group*:

$$
\bigl(\Sigma^{\alpha}_{c,d}\circ\Sigma^{\alpha}_{a,b}\bigr)^\dagger = \bigl(\Sigma^{\alpha}_{a,b}\bigr)^\dagger\circ\bigl(\Sigma^{\alpha}_{c,d}\bigr)^\dagger = \Sigma^{\alpha}_{a^{-1}\alpha(d^{-1}),\,\alpha(c^{-1})b^{-1}} .
$$

**Proof.** Apply the composition law $\Sigma^\alpha_{c,d}\Sigma^\alpha_{a,b} = \Sigma_{c\alpha(a),\alpha(b)d}$ and then the adjoint formula; alternatively use the anti-automorphism property directly.

## The Unitarity Condition

**Definition.** A signed sandwich is **unitary** when its adjoint is its inverse, $\Sigma^\alpha_{a,b}{}^\dagger\Sigma^\alpha_{a,b} = \mathrm{id}$ and $\Sigma^\alpha_{a,b}\Sigma^\alpha_{a,b}{}^\dagger = \mathrm{id}$; equivalently when it preserves the signed form, $B_\alpha(\Sigma^\alpha_{a,b}u,\Sigma^\alpha_{a,b}v) = B_\alpha(u,v)$ for all $u,v$.

**Theorem (the inverse and the criterion).** The inverse of the signed sandwich is $\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{-1} = \Sigma^{\alpha}_{\sigma(a),\,\sigma(b)}$, and the identity criterion for signed sandwiches is

$$
\Sigma^{\alpha}_{c,d} = \Sigma^{\alpha}_{c',d'} \iff c'^{-1}c \in Z(G) \ \text{and}\ c'^{-1}c = d'd^{-1} .
$$

Consequently $\Sigma^{\alpha}_{a,b}$ is unitary if and only if

$$
a^{-1}\alpha(a) \in Z(G) \qquad\text{and}\qquad \alpha(b)\,b^{-1} = \alpha(a)^{-1}a .
$$

**Proof.** Inverse: $\Sigma^\alpha_{a,b} = L_aR_bA$ has inverse $A^{-1}R_{b^{-1}}L_{a^{-1}} = A R_{b^{-1}}L_{a^{-1}}$, and applying it to $u$ gives $\alpha(a^{-1}ub^{-1}) = \alpha(a)^{-1}\alpha(u)\alpha(b)^{-1} = \sigma(a)\alpha(u)\sigma(b) = \Sigma^\alpha_{\sigma(a),\sigma(b)}(u)$. Identity criterion: $\Sigma^\alpha_{c,d} = \Sigma^\alpha_{c',d'}$ exactly when $c'^{-1}c\,\alpha(u) = \alpha(u)\,d'd^{-1}$ for all $u$, and since $\alpha$ is onto this says $c'^{-1}c$ is central and equal to $d'd^{-1}$. Unitarity: $\Sigma^\alpha_{a,b}{}^\dagger\Sigma^\alpha_{a,b} = \Sigma^\alpha_{a^{-1},b^{-1}}\Sigma^\alpha_{a,b} = \Sigma_{a^{-1}\alpha(a),\,\alpha(b)b^{-1}}$ by the composition law, and this is the identity exactly when $c = a^{-1}\alpha(a)$ is central and $c = d^{-1}$ with $d = \alpha(b)b^{-1}$, which is the stated condition; the second half of the unitarity is the mirror computation $\Sigma^\alpha_{a,b}\Sigma^\alpha_{a^{-1},b^{-1}} = \Sigma_{a\alpha(a)^{-1},\,\alpha(b)^{-1}b}$.

**Corollary (the fixed subgroup gives unitary sandwiches).** If $a, b \in G^\alpha$, the fixed subgroup of the grade involution, then $\Sigma^{\alpha}_{a,b}$ is unitary; the unitary signed sandwiches with both parameters in $G^\alpha$ form a subgroup of the group of form-preserving operators, and it is the image of $G^\alpha\times G^\alpha$ under the sandwich map.

**Proof.** For $a \in G^\alpha$ one has $\alpha(a) = a$, so $a^{-1}\alpha(a) = e$ is central, and for $b \in G^\alpha$ one has $\alpha(b)b^{-1} = e$, so the criterion is satisfied. The set $G^\alpha\times G^\alpha$ is a group and the sandwich map is a homomorphism there because $\alpha$ is the identity on it, so the image is a subgroup of the unitary group.

**Corollary (the trivial grade involution).** If $\alpha = \mathrm{id}$ then every signed sandwich is an unsigned sandwich and every one of them is unitary with respect to the natural form, its adjoint being its inverse $\Sigma_{a^{-1},b^{-1}}$.

**Proof.** For $\alpha = \mathrm{id}$ the criterion reads $a^{-1}a = e$ central and $b b^{-1} = e$, both automatic; the adjoint formula and the inverse formula coincide.

## The Reflection Read as a Signed Sandwich

**Definition.** The **signed conjugation** by $a$ is the signed sandwich $\rho_a = \Sigma^{\alpha}_{a,a^{-1}}$.

**Theorem.** With respect to the signed form,

$$
\rho_a^\dagger = \rho_{a^{-1}} = \Sigma^{\alpha}_{a^{-1},\,a} ,
$$

the signed conjugation is self-adjoint if and only if $a^2 \in Z(G)$, and it is unitary if and only if $a^{-1}\alpha(a) \in Z(G)$. When $\rho_a$ is a reflection — that is, when $a\alpha(a) \in Z(G)$ — the two conditions are equivalent, and the reflection is then an orthogonal involution of the group algebra.

**Proof.** The adjoint formula with $b = a^{-1}$ gives $\Sigma^\alpha_{a^{-1},(a^{-1})^{-1}} = \Sigma^\alpha_{a^{-1},a} = \rho_{a^{-1}}$. Self-adjointness: $\rho_a = \rho_{a^{-1}}$ exactly when $a^{-1}\in aZ(G)$, that is $a^2 \in Z(G)$, by the coset criterion for reflections. Unitarity: in the general criterion with $b = a^{-1}$ one has $d = \alpha(b)b^{-1} = \alpha(a)^{-1}a = c^{-1}$ for $c = a^{-1}\alpha(a)$, so the second condition is automatic and the first, $c$ central, is the stated one. If $a\alpha(a)$ is central, then $\alpha(a) \in a^{-1}Z(G)$, and $a^{-1}\alpha(a) \in a^{-2}Z(G)$ is central exactly when $a^2$ is central, so the two conditions coincide; an involution that is unitary is self-adjoint and conversely, because $\rho_a^2 = \mathrm{id}$ gives $\rho_a^\dagger = \rho_a^{-1} = \rho_a$.

**Corollary (the degenerate case).** If $a\alpha(a)$ is not central then $\rho_a$ is not an involution, the two conditions separate, and the signed conjugation is self-adjoint without being unitary or unitary without being self-adjoint; the reflection correspondence collapses exactly as *Reflections as Signed Two-Sided Operators on a Topological Group* records.

**Proof.** The square of $\rho_a$ is the inner conjugation $c_{a\alpha(a)}$, which is not the identity when $a\alpha(a)$ is not central, so $\rho_a^{-1}$ is not $\rho_a$; the two conditions $a^2\in Z(G)$ and $a^{-1}\alpha(a)\in Z(G)$ are independent when $a\alpha(a)$ is not central, and examples of each kind occur already in the finite groups computed for that article.

## Summary

With respect to the signed form of the category, the signed sandwich $\Sigma^{\alpha}_{a,b}(u) = a\alpha(u)b$ has adjoint $\Sigma^{\alpha}_{a^{-1},b^{-1}}$, the signed sandwich with both parameters inverted, and the adjoint operation is an involution on the sandwich family compatible with its coset structure and its composition law. The inverse is $\Sigma^{\alpha}_{\sigma(a),\sigma(b)}$, and comparing the two gives the unitarity condition: $\Sigma^{\alpha}_{a,b}$ is unitary exactly when $a^{-1}\alpha(a)$ is central and $\alpha(b)b^{-1} = \alpha(a)^{-1}a$. The sandwiches with both parameters in the fixed subgroup $G^\alpha$ are unitary and form a subgroup, and when the grade involution is the identity every signed sandwich is unsigned and unitary. The signed conjugation $\rho_a = \Sigma^{\alpha}_{a,a^{-1}}$ has adjoint $\rho_{a^{-1}}$, is self-adjoint exactly when $a^2$ is central, and is unitary exactly when $a^{-1}\alpha(a)$ is central; for a genuine reflection the two conditions coincide, and otherwise they separate, which is the operator form of the degeneracy of the reflection correspondence.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B_\alpha(u,v) = \sum_g u_gv_{\alpha(g)}$ | the signed form |
| $\Sigma^{\alpha}_{a,b}(u) = a\alpha(u)b = L_aR_bAu$ | the signed sandwich on the group algebra |
| $(\Sigma^{\alpha}_{a,b})^\dagger = \Sigma^{\alpha}_{a^{-1},b^{-1}}$ | the explicit form of the adjoint |
| $(\Sigma^{\alpha}_{a,b})^{-1} = \Sigma^{\alpha}_{\sigma(a),\sigma(b)}$ | the inverse |
| $\Sigma^\alpha_{c,d} = \Sigma^\alpha_{c',d'} \iff c'^{-1}c\in Z(G),\ c'^{-1}c = d'd^{-1}$ | the identity criterion |
| $a^{-1}\alpha(a)\in Z(G)$, $\alpha(b)b^{-1} = \alpha(a)^{-1}a$ | the unitarity condition |
| $a, b \in G^\alpha \implies$ unitary | the fixed subgroup gives unitary sandwiches |
| $\rho_a = \Sigma^{\alpha}_{a,a^{-1}}$ | the signed conjugation |
| $\rho_a^\dagger = \rho_{a^{-1}}$ | its adjoint |
| $a^2\in Z(G)$ | self-adjointness of $\rho_a$ |
| $a^{-1}\alpha(a)\in Z(G)$ | unitarity of $\rho_a$ |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutions, forms, hermitian forms and the unitary group they define.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for bilinear forms, their twists, adjoints and isometries.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the sandwich action, its adjoint and the orthogonal and unitary groups it generates.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, second edition, 2001), for the sandwich operator and the reflection it produces.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, second edition, 1979), for the adjoint of a convolution operator, which is Part III and is not used here.
