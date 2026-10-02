
# __The Signed Adjoint of the Left Multiplication on a Topological Group__

## Introduction

The signed left multiplication is the one-sided operator $u\mapsto a\,\alpha(u)$ on the group algebra, and its adjoint with respect to the signed form is the signed left multiplication by the inverse: the class of one-sided signed operators is closed under the adjoint, exactly as the class of reflections is. The self-adjointness and the unitarity of the operator then carve the group into two of the sets the involution defines: the operator is self-adjoint exactly for the elements of order two and unitary exactly for the elements of the fixed subgroup, and it is an involution exactly for the elements of the inverted subgroup. This article computes the adjoint, separates the three conditions, and assembles the two-sided signed sandwich from the one-sided operator and its adjoint.

The article assumes the natural and signed forms and the adjoints of the translations and of the linear extension $A$ of the grade involution from *The Adjoint of the Left Multiplication on a Topological Group*; the adjoint of the signed sandwich, its inverse and its unitarity criterion from *The Signed Adjoint Sandwich on a Topological Group*; the signed left multiplication, its composition laws, its square and its fixed set from *The Signed Left Multiplication on a Topological Group*; and the fixed subgroup, the inverted set and the dictionary from *Involutive Topological Groups*. The Haar inner product and the adjoint of the one-sided operator under it are Part III.

Throughout, $G$ is a Hausdorff topological group, $k$ is a field of characteristic different from two, $k[G]$ is the group algebra, $\sigma$ is a continuous involution, $\alpha = \sigma\iota$ is the associated continuous involutive automorphism, $A u = \sum_g u_g\,\alpha(g)$ is its linear extension, $H = G^\alpha = I(\sigma)$ is the fixed subgroup, and the **signed left multiplication** is the operator

$$
\Lambda_a : k[G] \longrightarrow k[G] , \qquad \Lambda_a(u) = a\,\alpha(u) = (L_aA)(u) ,
$$

with the **signed right multiplication** $\Lambda^{\mathrm{R}}_b(u) = \alpha(u)b$.

## The Adjoint of the Signed Left Multiplication

**Theorem (the explicit form of the adjoint).** With respect to the signed form $B_\alpha(u,v) = \sum_g u_gv_{\alpha(g)}$,

$$
\Lambda_a^\dagger = \Lambda_{a^{-1}} , \qquad \bigl(\Lambda^{\mathrm{R}}_b\bigr)^\dagger = \Lambda^{\mathrm{R}}_{b^{-1}} ,
$$

so the adjoint of the one-sided signed operator is the one-sided signed operator of the inverse, and the adjoint operation is an involution on each of the two signed families.

**Proof.** $\Lambda_a = L_aA$, so $\Lambda_a^\dagger = A^\dagger L_a^\dagger = A\,L_{\sigma(a)}$ by the adjoints of the elementary operators. Applying this to $u$ gives $A(\sigma(a)u) = \alpha(\sigma(a))\,\alpha(u)$. Since $\alpha$ and $\iota$ commute, $\alpha\sigma = \alpha\iota\alpha = \iota\alpha^2 = \iota$, so $\alpha\sigma(a) = a^{-1}$, and the operator is $u\mapsto a^{-1}\alpha(u) = \Lambda_{a^{-1}}(u)$. The computation for the signed right multiplication is the mirror image, and the double adjoint is immediate from $\sigma^2 = \mathrm{id}$.

**Corollary (the untwisted case).** When $\alpha = \mathrm{id}$ the signed left multiplication is the left multiplication and the signed form is the natural form; the adjoint is again the left multiplication by the inverse, which is the statement of *The Adjoint of the Left Multiplication on a Topological Group* for that case.

**Proof.** The formula specialises, since $\alpha = \mathrm{id}$ makes $\Lambda_a = L_a$ and $B_\alpha = B$.

## Self-Adjointness and Unitarity

**Theorem (the three conditions).** The signed left multiplication satisfies

$$
\Lambda_a \text{ is self-adjoint} \iff a^2 = e , \qquad
\Lambda_a \text{ is unitary} \iff a \in G^\alpha = H , \qquad
\Lambda_a \text{ is an involution} \iff a \in I(\alpha) = G^\sigma .
$$

It is simultaneously unitary and self-adjoint exactly for the elements of order two in the fixed subgroup, which are the elements of $G^\alpha \cap G^\sigma$, and for those elements it is an orthogonal involution.

**Proof.** Self-adjointness: $\Lambda_a^\dagger = \Lambda_{a^{-1}}$ equals $\Lambda_a = L_aA$ exactly when $L_{a^{-1}} = L_a$, that is $a^{-1} = a$, so $a^2 = e$. Unitarity: $\Lambda_a^\dagger\Lambda_a = \Lambda_{a^{-1}}\Lambda_a = L_{a^{-1}}A\,L_aA = L_{a^{-1}}L_{\alpha(a)}A^2 = L_{a^{-1}\alpha(a)}$, which is the identity exactly when $\alpha(a) = a$, that is $a\in G^\alpha$; the other order gives $L_{a\alpha(a)^{-1}}$, with the same conclusion. Involution: $\Lambda_a^2 = L_{a\alpha(a)}$ by the composition law, which is the identity exactly when $\alpha(a) = a^{-1}$, that is $a \in I(\alpha) = G^\sigma$. The intersection of the two sets is the set of $a$ with $\alpha(a) = a$ and $\alpha(a) = a^{-1}$, hence $a^2 = e$; for such an element the operator is unitary and an involution, and an involution that is unitary is self-adjoint.

**Corollary (the two faces of the involution).** The unitary signed left multiplications form the image of the fixed subgroup $H = G^\alpha$ and are pairwise distinct; the involutive signed left multiplications form the image of the inverted set $G^\sigma = I(\alpha)$ and are distinct; the two images meet exactly in the involutions carried by the elements of order two of $H$, and the unitary family is a subgroup of the group of form-preserving operators, of which the orthogonal involutions form the elements of order two.

**Proof.** If $\Lambda_a = \Lambda_b$ then $L_{a^{-1}b} = \mathrm{id}$ by the composition law, so $a = b$; hence both parametrisations are injective and the images are the stated sets. The product of two unitary operators is unitary, and the identity is unitary, so the unitary family is a subgroup; the orthogonal involutions are its elements of order two because for an involution unitarity and self-adjointness coincide.

**Theorem (the fixed sets).** The fixed space of the signed left multiplication is the kernel of the operator $L_aA - \mathrm{id}$, spanned by the solutions of $a = x\alpha(x)^{-1}$ in the group; it is closed, and when $a\in G^\sigma$ the operator is an involution and the fixed space is a direct summand of the group algebra with orthogonal complement the other eigenspace.

**Proof.** On a group element $x$ the equation $\Lambda_a(x) = x$ is $a\alpha(x) = x$, that is $a = x\alpha(x)^{-1}$; the kernel is their span, closed by continuity. If $a\in G^\sigma$ then $\Lambda_a^2 = \mathrm{id}$, and for an involution with $2$ invertible the group algebra splits into the two eigenspaces, orthogonal for the signed form when the involution is self-adjoint, which for $a\in G^\sigma\cap G^\alpha$ is the case.

## Relation to the Signed Sandwich

**Theorem (assembling the two-sided operator).** The signed sandwich factors through the one-sided operators,

$$
\Sigma^{\alpha}_{a,b} = L_a\circ\Lambda^{\mathrm{R}}_b = \Lambda_a\circ R_{\alpha(b)} ,
$$

and its adjoint is assembled from the one-sided adjoints:

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^\dagger = R_{b^{-1}}\circ\Lambda_{a^{-1}} = \Sigma^{\alpha}_{a^{-1},b^{-1}} .
$$

**Proof.** $L_a\Lambda^{\mathrm{R}}_b(u) = L_a(\alpha(u)b) = a\alpha(u)b$ and $\Lambda_aR_{\alpha(b)}(u) = a\alpha(u\alpha(b)) = a\alpha(u)\alpha^2(b) = a\alpha(u)b$. For the adjoint, $(\Sigma^\alpha_{a,b})^\dagger = (\Lambda_aR_{\alpha(b)})^\dagger = R_{\alpha(b)}^\dagger\Lambda_a^\dagger = R_{\sigma\alpha(b)}\Lambda_{a^{-1}}$, and $\sigma\alpha = \sigma(\sigma\iota) = \iota$, so $\sigma\alpha(b) = b^{-1}$ and the adjoint is $R_{b^{-1}}\Lambda_{a^{-1}}(u) = a^{-1}\alpha(u)b^{-1} = \Sigma^\alpha_{a^{-1},b^{-1}}(u)$, consistently with *The Signed Adjoint Sandwich on a Topological Group*.

**Corollary (the sandwich from a unitary one-sided operator).** If $a\in H$ then $\Lambda_a$ is unitary and the signed sandwich $\Sigma^{\alpha}_{a,e} = \Lambda_a$ is unitary; more generally $\Sigma^{\alpha}_{a,b}$ is unitary for all $a\in H$ and all $b$ with $\alpha(b)b^{-1} = e$, that is for $b\in H$, recovering the fixed-subgroup criterion of *The Signed Adjoint Sandwich on a Topological Group* from the one-sided one.

**Proof.** The first statement is the unitarity criterion, and the second is the sandwich criterion specialised, whose second condition $\alpha(b)b^{-1} = \alpha(a)^{-1}a$ reduces to $\alpha(b)b^{-1} = e$ when $a\in H$ because then $\alpha(a) = a$.

## Summary

The signed left multiplication $\Lambda_a(u) = a\alpha(u)$ on the group algebra has adjoint $\Lambda_a^\dagger = \Lambda_{a^{-1}}$ with respect to the signed form, and the signed right multiplication has the same property; the one-sided signed families are closed under the adjoint. The operator is self-adjoint exactly for the elements of order two, unitary exactly for the elements of the fixed subgroup $H = G^\alpha$, and an involution exactly for the elements of the inverted set $G^\sigma = I(\alpha)$; the three conditions meet in the elements of order two of $H$, where the operator is an orthogonal involution. The fixed space is the kernel of $L_aA - \mathrm{id}$, spanned by the solutions of $a = x\alpha(x)^{-1}$. The two-sided signed sandwich is assembled as $\Sigma^{\alpha}_{a,b} = L_a\Lambda^{\mathrm{R}}_b = \Lambda_aR_{\alpha(b)}$, and its adjoint is assembled from the one-sided adjoints, giving again $\Sigma^{\alpha}_{a^{-1},b^{-1}}$; the unitarity criterion of the two-sided operator is recovered from the one-sided criterion, and the one-sided operator is unitary exactly on the fixed subgroup. The Haar inner product and the adjoint under it are Part III and are not used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda_a(u) = a\alpha(u) = L_aAu$ | the signed left multiplication on the group algebra |
| $\Lambda^{\mathrm{R}}_b(u) = \alpha(u)b$ | the signed right multiplication |
| $\Lambda_a^\dagger = \Lambda_{a^{-1}}$ | the adjoint with respect to the signed form |
| $a^2 = e$ | self-adjointness condition |
| $a \in G^\alpha$ | unitarity condition |
| $a \in I(\alpha) = G^\sigma$ | the involution condition |
| $\Lambda_a^2 = L_{a\alpha(a)}$ | the square of the operator |
| $G^\alpha\cap G^\sigma$ | the elements of order two in the fixed subgroup, orthogonal involutions |
| $\Sigma^{\alpha}_{a,b} = L_a\Lambda^{\mathrm{R}}_b = \Lambda_aR_{\alpha(b)}$ | the signed sandwich from the one-sided operators |
| $\sigma\alpha = \iota$ | the identity reconciling the factors |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutions, adjoints, unitarity and the operators they define.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the one-sided and two-sided signed operators and their relations.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for adjoints with respect to a form, self-adjoint and unitary operators.
- Lev S. Pontryagin, *Topological Groups* (Gordon and Breach, second edition, 1966), for the translations and their continuity in the topological setting.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, second edition, 1979), for the Haar inner product and the adjoint of a one-sided operator under it, which is Part III.
