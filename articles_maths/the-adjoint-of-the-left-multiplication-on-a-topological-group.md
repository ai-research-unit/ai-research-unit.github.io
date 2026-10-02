
# __The Adjoint of the Left Multiplication on a Topological Group__

## Introduction

An adjoint is taken with respect to a form, and the form of this category is the pairing between the functions on the group and its group algebra. This article computes the adjoint of the left multiplication with respect to that pairing and then with respect to its twisting by the grade involution. The first computation returns the left multiplication by the inverse, which is the operator form of the statement that inversion is the adjoint; the second returns the left multiplication by the image of the element under the involution, which is the precise sense in which the left regular representation is a `*`-representation. The agreement of the involution on the elements with the adjoint on the operators is proved and not assumed, as the contract of the group requires.

The article assumes the group algebra, the natural pairing and the translation operators from *Operators on a Topological Group* and *Convolution on a Topological Group*; the continuous involution, the associated involutive automorphism $\alpha = \sigma\iota$, the fixed and inverted subgroups and the dictionary from *Involutive Topological Groups*; and the continuity of the translations from *Topological Groups*. The Haar pairing and the adjoint of a convolution operator under it are *The Adjoint of a Convolution Operator* in Part III, and are named only.

Throughout, $G$ is a Hausdorff topological group with identity $e$, $k$ is a field, $k[G]$ is the group algebra with basis $G$ and finitely supported elements, $\sigma$ is a continuous involution, $\alpha = \sigma\iota$ is the associated continuous involutive automorphism, and $A$ is the linear extension of $\alpha$ to $k[G]$, $A u = \sum_g u_g\,\alpha(g)$.

## The Natural Form and the Untwisted Adjoint

**Definition.** The **natural form** of the category is the symmetric bilinear form

$$
B : k[G]\times k[G] \longrightarrow k, \qquad B(u,v) = \sum_{g\in G} u_g\,v_g ,
$$

the form making the group elements an orthonormal basis. It is the algebraic shadow of the pairing between the continuous functions and the group algebra, $B(u,v) = \langle f_v, u\rangle$ with $f_v(g) = v_g$ on the finite support of $v$.

**Theorem (the adjoint is the inverse).** On $k[G]$ the left and right multiplications satisfy

$$
(L_a)^\dagger = L_{a^{-1}} , \qquad (R_b)^\dagger = R_{b^{-1}} ,
$$

with respect to the natural form, where $L_a u = au$ and $R_b u = ub$.

**Proof.** $(L_au)_k = u_{a^{-1}k}$, so $B(L_au,v) = \sum_g u_{a^{-1}g}v_g = \sum_h u_h v_{ah}$ on setting $h = a^{-1}g$. If $T$ is the adjoint then $B(u,Tv) = \sum_h u_h(Tv)_h$, so $(Tv)_h = v_{ah}$, that is $(Tv)_h = (L_{a^{-1}}v)_h$. The computation for $R_b$ is the mirror image, using $(R_bu)_k = u_{kb^{-1}}$.

**Corollary (the inversion as the adjoint).** The adjoint operation is an anti-automorphism of the algebra of operators, $(ST)^\dagger = T^\dagger S^\dagger$, and the assignment $a\mapsto L_a$ converts the inversion into the adjoint: the adjoint of the left regular operator of $a$ is the left regular operator of $a^{-1}$. The map $u\mapsto\sum_g u_g\,g^{-1}$, the linear extension $I$ of the inversion, is a form-preserving self-adjoint anti-automorphism of $k[G]$, and it exchanges the two regular representations,

$$
(L_a)^\dagger = I\,R_a\,I = L_{a^{-1}} , \qquad (R_b)^\dagger = I\,L_b\,I = R_{b^{-1}} .
$$

**Proof.** The anti-automorphism property is general for adjoints with respect to a bilinear form. The inversion operator satisfies $B(Iu,Iv) = B(u,v)$ and $B(Iu,v) = B(u,Iv)$, so it is an isometry and self-adjoint; $\alpha = \mathrm{id}$ here, so $\sigma = \iota$. Since $I$ is an anti-automorphism, $I L_a I = R_{a^{-1}}$ and $I R_b I = L_{b^{-1}}$, which together with the theorem gives the displayed identities.

## The Signed Form

**Definition.** Let $(G,\alpha)$ be a graded topological group. The **signed form** is the symmetric bilinear form

$$
B_\alpha : k[G]\times k[G] \longrightarrow k, \qquad B_\alpha(u,v) = \sum_{g\in G} u_g\,v_{\alpha(g)} ,
$$

the natural form twisted by the grade involution; it reduces to $B$ when $\alpha = \mathrm{id}$.

**Theorem (the adjoints with respect to the signed form).** On $k[G]$,

$$
(L_a)^\dagger = L_{\sigma(a)} , \qquad (R_b)^\dagger = R_{\sigma(b)} , \qquad A^\dagger = A .
$$

**Proof.** $(L_au)_k = u_{a^{-1}k}$, so $B_\alpha(L_au,v) = \sum_g u_{a^{-1}g}v_{\alpha(g)} = \sum_h u_h v_{\alpha(a)\alpha(h)}$ on setting $h = a^{-1}g$ and using that $\alpha$ is an automorphism. If $T$ is the adjoint then $(Tv)_{\alpha(h)} = v_{\alpha(a)\alpha(h)}$, so $(Tv)_k = v_{\alpha(a)k}$ on writing $k = \alpha(h)$; since $(L_cv)_k = v_{c^{-1}k}$ and $\alpha(a)^{-1} = \alpha(a^{-1}) = \sigma(a)$, this is $L_{\sigma(a)}$. The computation for $R_b$ gives $(R_b)^\dagger = R_{\alpha(b)^{-1}} = R_{\sigma(b)}$, and for $A$ one has $(Au)_k = u_{\alpha^{-1}(k)}$, whence $B_\alpha(Au,v) = \sum_h u_h v_h$, which identifies the adjoint with $A$.

**Remark (the two adjoints).** The untwisted adjoint of $L_a$ is $L_{a^{-1}}$ and the signed adjoint is $L_{\sigma(a)}$; the two are the same computation with the two forms, and they are reconciled by $\sigma(a) = \alpha(a)^{-1}$, so the passage from one to the other is the twisting of the form by $\alpha$.

## Compatibility with the Involution

**Theorem (the left regular representation is a `*`-representation).** With respect to the signed form the assignment $a\mapsto L_a$ satisfies

$$
(L_a)^\dagger = L_{\sigma(a)} , \qquad (L_aL_b)^\dagger = L_b^\dagger L_a^\dagger , \qquad (L_a^\dagger)^\dagger = L_a ,
$$

so the involution on the elements of $G$ agrees with the adjoint on the operators: the left regular representation is a `*`-representation of the involutive group algebra, and it extends to a `*`-representation of the semidirect product $G\rtimes_\alpha C_2$ on the same space.

**Proof.** The first identity is the theorem above, the second is the general anti-automorphism property of the adjoint, and the third uses $\sigma^2 = \mathrm{id}$. The agreement is exactly the statement that the representation carries the involution to the adjoint; the extension is the action of the generator of the extension by the operator $A$, which is self-adjoint and satisfies $A L_a A = L_{\alpha(a)}$, the relation required for a representation of the semidirect product.

**Corollary (the right regular representation).** $(R_b)^\dagger = R_{\sigma(b)}$ and the two representations commute with the same involution; the operator $A$ intertwines the two, $A L_a A = L_{\alpha(a)}$ and $A R_b A = R_{\alpha(b)}$, so it is a `*`-isomorphism between the left regular representation and its twist.

**Proof.** The identities are the theorem and the definition of $A$; the intertwining is the multiplicativity of $\alpha$.

**Corollary (the degenerate cases).** If $\sigma = \iota$, so that $\alpha = \mathrm{id}$, the signed form is the natural form and the adjoint of $L_a$ is $L_{a^{-1}}$; if the involution is inner, the adjoint differs from the untwisted adjoint by the inner automorphism of the conjugating element; and if $G$ is abelian then $L_a = R_a$ and the left multiplication is self-adjoint exactly when $\sigma(a) = a$, that is for $a \in G^\sigma$.

**Proof.** The first statement is the specialisation $\alpha = \mathrm{id}$. For an inner involution one has $\sigma(a) = za z^{-1}$ up to the conventions of *The Signed Sandwich on a Topological Group*, so the signed adjoint is the conjugate of the untwisted one. On an abelian group $L_a = R_a$ and $L_{\sigma(a)} = L_a$ exactly when $\sigma(a) = a$.

## Continuity

**Theorem (the adjoint is continuous).** Let $T : k[G]\to k[G]$ be a continuous operator with an adjoint with respect to the natural or the signed form. If $T$ is a finite linear combination of translations then $T^\dagger$ is continuous, and the assignment

$$
G \longrightarrow \operatorname{End}_k(k[G]) , \qquad a \mapsto L_a^\dagger = L_{\sigma(a)} ,
$$

is continuous for the discrete topology on $k[G]$, being the composite of the continuous parametrisation $a\mapsto L_a$ of *The Signed Left Multiplication on a Topological Group* with the involution.

**Proof.** A finite linear combination of the translations is continuous, and its adjoint is a finite linear combination of the adjoints $L_{\sigma(a)}$, again continuous. The parametrisation $a\mapsto L_{\sigma(a)}$ is the composite of $\sigma$, a homeomorphism, with the continuous $a\mapsto L_a$.

## Summary

The natural form $B(u,v) = \sum_g u_gv_g$ on the group algebra gives the untwisted adjoints $(L_a)^\dagger = L_{a^{-1}}$ and $(R_b)^\dagger = R_{b^{-1}}$, which is the operator form of the statement that the inversion is the adjoint; the signed form $B_\alpha(u,v) = \sum_g u_gv_{\alpha(g)}$, the natural form twisted by the grade involution, gives $(L_a)^\dagger = L_{\sigma(a)}$, $(R_b)^\dagger = R_{\sigma(b)}$ and $A^\dagger = A$ for the linear extension $A$ of $\alpha$. The two adjoints are reconciled by $\sigma(a) = \alpha(a)^{-1}$, so the passage from the untwisted to the signed adjoint is the twisting of the form by the grade involution. With respect to the signed form the left regular representation is a `*`-representation: the involution on the elements agrees with the adjoint on the operators, and the representation extends to the semidirect product $G\rtimes_\alpha C_2$ with the generator acting by the self-adjoint operator $A$. The right regular representation carries the same involution, the two representations are intertwined by $A$, and in the degenerate cases — the involution the inversion, the involution inner, the group abelian — the formula specialises as recorded. The adjoints of finite linear combinations of translations are continuous, and the map $a\mapsto L_a^\dagger$ is continuous. The Haar pairing and the adjoint of a convolution operator under it are Part III and are not used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k[G]$ | the group algebra of finitely supported functions |
| $B(u,v) = \sum_g u_gv_g$ | the natural form, the group elements an orthonormal basis |
| $(L_a)^\dagger = L_{a^{-1}}$ | the untwisted adjoint of the left multiplication |
| $(R_b)^\dagger = R_{b^{-1}}$ | the untwisted adjoint of the right multiplication |
| $B_\alpha(u,v) = \sum_g u_gv_{\alpha(g)}$ | the signed form, the natural form twisted by $\alpha$ |
| $(L_a)^\dagger = L_{\sigma(a)}$ | the signed adjoint of the left multiplication |
| $(R_b)^\dagger = R_{\sigma(b)}$ | the signed adjoint of the right multiplication |
| $A u = \sum_g u_g\alpha(g)$ | the linear extension of $\alpha$, self-adjoint |
| $\sigma(a) = \alpha(a)^{-1}$ | the reconciliation of the two adjoints |
| `*`-representation | the agreement of the involution with the adjoint, proved here |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutions, their adjoints and the `*`-representations they define.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Wiley, 1962), for the adjoint with respect to a bilinear form and the structure of an algebra with involution.
- Lev S. Pontryagin, *Topological Groups* (Gordon and Breach, second edition, 1966), for the translations and their continuity.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for bilinear forms, their twists and the adjoint of a linear map.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, second edition, 1979), for the passage from the algebraic adjoint of the group algebra to the adjoint of a convolution operator, which is Part III.
