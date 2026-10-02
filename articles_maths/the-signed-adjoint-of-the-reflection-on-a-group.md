
# __The Signed Adjoint of the Reflection on a Group__

## Introduction

A reflection of a graded group is a signed conjugation that is an involution, and its adjoint under the natural pairing is again a signed conjugation, with parameter the inverse of the twisted element. The self-adjointness is then automatic for the reflections and fails exactly for the signed conjugations that are not involutions, which is to say for the degenerate case in which the product $a\alpha(a)$ is not central. This article gives the adjoint, proves the equivalence of self-adjointness with the reflection property, and isolates the degenerate case. It is the fifth article of the `* Operator Theory` group; the reflections and the criterion $a\alpha(a)\in Z(G)$ are from *Reflections as Signed Two-Sided Operators on a Group*, the adjoint of the signed sandwich from *The Signed Adjoint Sandwich on a Group*, and the pairing from *Involutions on the Operator Layer*.

Throughout, $(G,\alpha)$ is a group with an involutive automorphism $\alpha$, a **signed conjugation** is the operator $\Sigma^{\alpha}_{a,a^{-1}}$, and a **reflection** is a signed conjugation that is an involution; the criterion of *Reflections as Signed Two-Sided Operators on a Group* is that $\Sigma^{\alpha}_{a,a^{-1}}$ is an involution, equivalently a reflection, if and only if $a\,\alpha(a)\in Z(G)$.

## The Adjoint of a Reflection

**Theorem (the adjoint is a reflection).** For every $a\in G$,

$$
\bigl(\Sigma^{\alpha}_{a,a^{-1}}\bigr)^{*}=\Sigma^{\alpha}_{\alpha(a)^{-1},\ \alpha(a)}=\Sigma^{\alpha}_{\alpha(a)^{-1},\,(\alpha(a)^{-1})^{-1}},
$$

which is the signed conjugation with parameter $\alpha(a)^{-1}$. Hence the adjoint of a reflection is a reflection, and the reflections are closed under the adjoint.

**Proof.** The adjoint formula of *The Signed Adjoint Sandwich on a Group* gives $\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}=\Sigma^{\alpha}_{\alpha(a)^{-1},\alpha(b)^{-1}}$; with $b=a^{-1}$ this is $\Sigma^{\alpha}_{\alpha(a)^{-1},\alpha(a^{-1})^{-1}}=\Sigma^{\alpha}_{\alpha(a)^{-1},\alpha(a)}$, since $\alpha(a^{-1})=\alpha(a)^{-1}$ and its inverse is $\alpha(a)$. The result is the signed conjugation with parameter $\alpha(a)^{-1}$, whose second parameter is $(\alpha(a)^{-1})^{-1}=\alpha(a)$. Every reflection has this form, because $\alpha(a)^{-1}=b$ for the parameter $b=\alpha^{-1}(a^{-1})=\alpha(a^{-1})$, so the adjoint of a reflection is a reflection.

**Corollary (the adjoint involution on the reflections).** The adjoint acts on the set of reflections by $\Sigma^{\alpha}_{a,a^{-1}}\mapsto\Sigma^{\alpha}_{\alpha(a)^{-1},\alpha(a)}$, an involution of that set; it fixes a reflection exactly when the reflection is self-adjoint.

**Proof.** The displayed map is the restriction of the adjoint, which is an involution of the operator algebra; a fixed point of the restriction is exactly a self-adjoint reflection.

**Proposition (the adjoint respects the coset description).** Since a signed conjugation depends only on the class of $a$ modulo the centre, $\Sigma^{\alpha}_{a,a^{-1}}=\Sigma^{\alpha}_{az^{-1},za^{-1}}$ for $z\in Z(G)$, the adjoint operation on the reflections descends to the set of cosets $aZ(G)$, where it is the assignment $aZ(G)\mapsto\alpha(a)^{-1}Z(G)$.

**Proof.** The dependence on the class is the equality criterion of *The Signed Adjoint Sandwich on a Group* specialised to $b=a^{-1}$; the adjoint of a reflection has parameter $\alpha(a)^{-1}$, and the class of the parameter is determined by the class of $a$.

## Self-Adjointness

**Theorem (a signed conjugation is self-adjoint if and only if it is a reflection).** For every $a\in G$,

$$
\Sigma^{\alpha}_{a,a^{-1}}\text{ is self-adjoint}
\quad\Longleftrightarrow\quad
a\,\alpha(a)\in Z(G)
\quad\Longleftrightarrow\quad
\Sigma^{\alpha}_{a,a^{-1}}\text{ is a reflection}.
$$

Hence every reflection is self-adjoint, and the signed conjugations that are not reflections are exactly the signed conjugations that are not self-adjoint.

**Proof.** Self-adjointness is the equality $\Sigma^{\alpha}_{a,a^{-1}}=\Sigma^{\alpha}_{\alpha(a)^{-1},\alpha(a)}$, which by the equality criterion of *The Signed Adjoint Sandwich on a Group* is the existence of $z\in Z(G)$ with $\alpha(a)^{-1}=a z^{-1}$ and $\alpha(a)=z a^{-1}$. The first relation gives $z=\alpha(a)a$, and the second gives the same, since $\alpha(a)=za^{-1}$ is $z=\alpha(a)a$. So self-adjointness is exactly the centrality of $\alpha(a)a$, and $\alpha(a)a$ is central if and only if $a\alpha(a)$ is, because the two are conjugate: $a\,\alpha(a)=a\,(\alpha(a)a)\,a^{-1}$. The centrality of $a\alpha(a)$ is the reflection criterion of *Reflections as Signed Two-Sided Operators on a Group*, which completes the equivalence. The final sentence restates it.

**Corollary (the failure in the degenerate case).** In the degenerate case $a\alpha(a)\notin Z(G)$ the signed conjugation $\Sigma^{\alpha}_{a,a^{-1}}$ is not an involution and is not self-adjoint; the two failures coincide, and there is no signed conjugation that is one and not the other.

**Proof.** The equivalence of the theorem is the coincidence: a signed conjugation is an involution iff $a\alpha(a)\in Z(G)$ iff it is self-adjoint.

**Remark (the reading of the theorem).** The theorem says that on the level of adjoints the reflection property is not an extra condition: the operators whose adjoint is themselves are exactly the reflections, so the adjoint operation selects the reflections among the signed conjugations. This is the operator-level counterpart of the fact that the fixed points of the inversion are the elements of order at most two, and it is the reason the reflections are read as the self-adjoint signed two-sided operators.

## The Degenerate Case and the Examples

**Example (the abelian case).** If $G$ is abelian then every $a\alpha(a)$ is central, so every signed conjugation is a reflection and every one is self-adjoint. By *Reflections as Signed Two-Sided Operators on a Group*, on an abelian group all the signed conjugations coincide with the grade involution $\alpha$, and $\alpha$ is self-adjoint by *The Group Inversion as an Adjoint*; the two statements agree.

**Example (the Klein four group).** Let $G=V_4$ with the involutive automorphism $\alpha$ swapping the two generators. The group is abelian, so all four signed conjugations are reflections; they are self-adjoint, and the adjoint operation on them is the identity on the two-element set of distinct signed conjugations.

**Example (the dihedral group).** Let $G=D_4=\langle r,s\mid r^{4}=s^{2}=e,\ srs=r^{-1}\rangle$ with $\alpha=c_s$ the conjugation by the reflection $s$, an involutive automorphism. For $a=r$ one has $\alpha(r)=r^{-1}$ and $a\alpha(r)=r\cdot r^{-1}=e$, central, so $\Sigma^{\alpha}_{r,r^{-1}}$ is a reflection and is self-adjoint. For $a=s$ one has $\alpha(s)=s$ and $a\alpha(a)=s^{2}=e$, again a reflection. The degenerate case does not occur here, because the conjugations by $s$ invert $r$ and fix $s$.

**Example (a genuine degeneracy).** Take $G=S_3$ and $\alpha$ an involutive automorphism, for instance the conjugation by the transposition $t=(1\,2)$. For $a=(2\,3)$ one computes $\alpha(a)=(1\,3)$ and $a\alpha(a)=(2\,3)(1\,3)=(1\,2\,3)$, of order three, which is not central; so $\Sigma^{\alpha}_{a,a^{-1}}$ is not an involution and is not self-adjoint, and the adjoint of the signed conjugation with parameter $(2\,3)$ is the signed conjugation with parameter $\alpha(a)^{-1}=(1\,3)$.

**Remark (the two failures are one).** The article has exhibited three things that could fail separately and that in fact fail together: the signed conjugation may fail to be an involution, it may fail to be a reflection, and it may fail to be self-adjoint. The theorem shows that for the signed conjugations these are the same failure, governed by the single condition $a\alpha(a)\in Z(G)$; the reason is that the involution property, the reflection property and the self-adjointness all reduce to the same centrality of $a\alpha(a)$.

## Summary

The adjoint of the signed conjugation with parameter $a$ is the signed conjugation with parameter $\alpha(a)^{-1}$, so the adjoint of a reflection is a reflection and the reflections are closed under the adjoint operation, which acts on their cosets by $aZ(G)\mapsto\alpha(a)^{-1}Z(G)$. A signed conjugation is **self-adjoint if and only if it is a reflection**, both conditions being equivalent to $a\alpha(a)\in Z(G)$; hence every reflection is self-adjoint and the signed conjugations that are not self-adjoint are exactly the ones that are not involutions, the degenerate case. The abelian case, the Klein four group with the swap and the dihedral group with the conjugation by a reflection are all non-degenerate, and the first genuinely degenerate instance is the symmetric group on three letters with a non-trivial involutive automorphism.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Sigma^{\alpha}_{a,a^{-1}}$ | a signed conjugation |
| reflection | a signed conjugation that is an involution |
| $\bigl(\Sigma^{\alpha}_{a,a^{-1}}\bigr)^{*}=\Sigma^{\alpha}_{\alpha(a)^{-1},\alpha(a)}$ | the adjoint of a signed conjugation |
| $a\alpha(a)\in Z(G)$ | the reflection and self-adjointness criterion |
| $aZ(G)\mapsto\alpha(a)^{-1}Z(G)$ | the adjoint action on the cosets |
| degenerate case | $a\alpha(a)\notin Z(G)$, neither a reflection nor self-adjoint |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for reflections, involutions and the self-adjoint elements.
- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, fourth edition, 1995), for the symmetric and dihedral groups and their conjugations.
- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, second edition, 1996), for centrality and conjugacy in the small groups.
- I. Martin Isaacs, *Finite Group Theory* (American Mathematical Society, Graduate Studies in Mathematics 92, 2008), for automorphisms of order two and their fixed-point conditions.
