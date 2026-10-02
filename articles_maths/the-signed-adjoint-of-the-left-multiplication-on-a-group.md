
# __The Signed Adjoint of the Left Multiplication on a Group__

## Introduction

The signed left multiplication $x\mapsto a\,\alpha(x)$ is the one-sided operator built from the left translation and the grade involution, and its adjoint under the natural pairing is again a signed left multiplication, with parameter $\alpha(a)^{-1}$. The adjoint operation therefore acts on the set of signed left multiplications as an involution of the index set, and that involution is exactly the group involution $\sigma=\iota\alpha$ associated with $\alpha$; the self-adjoint signed left multiplications are those indexed by the fixed elements of $\sigma$. This article gives the adjoint, proves that the index assignment is an involution-preserving bijection, and records the relation to the signed sandwich. It is the sixth article of the `* Operator Theory` group; the signed left multiplication and its composition law are from *The Signed Left Multiplication on a Group*, the pairing and adjoint from *Involutions on the Operator Layer*, and the signed sandwich from *The Signed Adjoint Sandwich on a Group*.

Throughout, $(G,\alpha)$ is a group with an involutive automorphism $\alpha$, $\sigma=\iota\alpha$ is the associated involution of $G$, $\ell^{\alpha}_a(x)=a\,\alpha(x)=\Sigma^{\alpha}_{a,e}$ is the signed left multiplication, and the adjoint is taken with respect to the orthonormal pairing $\langle g,h\rangle=\delta_{g,h}$.

## The Adjoint

**Theorem (the adjoint of a signed left multiplication).** For every $a\in G$,

$$
\bigl(\ell^{\alpha}_a\bigr)^{*}=\Sigma^{\alpha}_{\alpha(a)^{-1},\,e}=\ell^{\alpha}_{\alpha(a)^{-1}}=\ell^{\alpha}_{\alpha(a^{-1})}.
$$

Hence the adjoint of a signed left multiplication is a signed left multiplication, and the set $\{\ell^{\alpha}_a:a\in G\}$ is closed under the adjoint.

**Proof.** The signed left multiplication is the signed sandwich with second parameter $e$, so the adjoint formula of *The Signed Adjoint Sandwich on a Group* gives $\bigl(\ell^{\alpha}_a\bigr)^{*}=\Sigma^{\alpha}_{\alpha(a)^{-1},\alpha(e)^{-1}}=\Sigma^{\alpha}_{\alpha(a)^{-1},e}$, because $\alpha(e)=e$. The last equality is $\alpha(a^{-1})=\alpha(a)^{-1}$.

**Corollary (the adjoint inverts the index through the involution).** The assignment $a\mapsto\alpha(a)^{-1}$ is an involution of the set $G$, and the adjoint on the signed left multiplications is that assignment on the indices:

$$
a\mapsto\alpha(a)^{-1},
\qquad
a\mapsto\alpha(a)^{-1}\mapsto\alpha\bigl(\alpha(a)^{-1}\bigr)^{-1}=a .
$$

It is the anti-automorphism $\sigma=\iota\alpha=\alpha\iota$ of *Involutive Groups*, read on the index set.

**Proof.** The double application returns $a$ because $\alpha^{2}=\mathrm{id}$, so the assignment is an involution of the set $G$. And $\alpha(a)^{-1}=\iota(\alpha(a))=\sigma(a)$; so the assignment is the group involution $\sigma$, which is an anti-automorphism of order two.

**Proposition (the index map is a bijection).** The map $a\mapsto\ell^{\alpha}_a$ is a bijection from $G$ onto the set of signed left multiplications; it intertwines the involution $\sigma$ of $G$ with the adjoint, and it carries the fixed set $G^{\sigma}$ onto the set of self-adjoint signed left multiplications.

**Proof.** Injectivity: $\ell^{\alpha}_a=\ell^{\alpha}_b$ means $a\alpha(x)=b\alpha(x)$ for all $x$, and evaluating at $x=e$ gives $a=b$; surjectivity is the definition of the set. The intertwining is the theorem read as $\ell^{\alpha}_{\sigma(a)}=(\ell^{\alpha}_a)^{*}$. The fixed set statement is the definition of a fixed point of $\sigma$ together with the same equation.

## Self-Adjointness and Unitarity

**Theorem (the self-adjoint signed left multiplications).** $\ell^{\alpha}_a$ is self-adjoint if and only if $\alpha(a)=a^{-1}$, equivalently if and only if $a\alpha(a)=e$, equivalently if and only if $a$ is fixed by the involution $\sigma=\iota\alpha$. Hence the self-adjoint signed left multiplications are indexed exactly by the fixed set $G^{\sigma}$ of $\sigma$.

**Proof.** Self-adjointness is $\ell^{\alpha}_a=\ell^{\alpha}_{\alpha(a)^{-1}}$, and the index map is injective, so the condition is $a=\alpha(a)^{-1}$, that is $\alpha(a)=a^{-1}$. Applying $\iota$ gives $\sigma(a)=a$. The fixed set of $\sigma$ is precisely $\{a:\alpha(a)=a^{-1}\}$ by the identity $G^{\sigma}=I(\alpha)$ of *Involutions and the Fixed-Point Subgroup*.

**Proposition (unitarity).** Every signed left multiplication is unitary: $\bigl(\ell^{\alpha}_a\bigr)^{*}\ell^{\alpha}_a=\mathrm{id}=\ell^{\alpha}_a\bigl(\ell^{\alpha}_a\bigr)^{*}$.

**Proof.** It is the signed sandwich with second parameter $e$, and every signed sandwich is unitary by *The Signed Adjoint Sandwich on a Group*. Directly, $\ell^{\alpha}_a\ell^{\alpha}_{\alpha(a)^{-1}}=L_{a\,\alpha(\alpha(a)^{-1})}=L_{aa^{-1}}=\mathrm{id}$ by the composition law of *The Signed Left Multiplication on a Group* and $\alpha^{2}=\mathrm{id}$.

**Example (the fixed and inverted elements).** On the cyclic group $C_6$ with $\alpha=\iota$ the involution $\sigma=\iota\alpha=\mathrm{id}$ has fixed set all of $C_6$, so every signed left multiplication is self-adjoint; on $S_3$ with the conjugation by a transposition, the fixed set of $\sigma=\iota\alpha$ is the inverted set $I(\alpha)$ of the conjugation, which has four elements $\{e,(1\,2),(1\,2\,3),(1\,3\,2)\}$, and exactly four of the six signed left multiplications are self-adjoint.

**Remark (the contrast with the unsigned case).** The unsigned left multiplication satisfies $(L_a)^{*}=L_{a^{-1}}$, indexed by the inversion $\iota$; the signed one satisfies $(\ell^{\alpha}_a)^{*}=\ell^{\alpha}_{\alpha(a)^{-1}}$, indexed by $\sigma=\iota\alpha$. The insertion of the grade involution therefore replaces the inversion by the involution $\sigma$ on the index set, and the self-adjoint unsigned left multiplications are indexed by the elements of order at most two whereas the self-adjoint signed ones are indexed by the fixed set of $\sigma$. The two agree exactly when $\alpha=\mathrm{id}$.

## The Relation to the Signed Sandwich

**Proposition (the adjoint of the signed sandwich factors through the signed left multiplication).** For every $a,b\in G$,

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}=\bigl(\ell^{\alpha}_a\bigr)^{*}\circ(R_b)^{*}=\ell^{\alpha}_{\alpha(a)^{-1}}\circ R_{b^{-1}}.
$$

**Proof.** The factorisation $\Sigma^{\alpha}_{a,b}=R_b\circ\ell^{\alpha}_a$ is from *The Signed Adjoint Sandwich on a Group*; the adjoint of a product reverses the order, and the adjoints of the two factors are the theorem above and $(R_b)^{*}=R_{b^{-1}}$.

**Corollary (the two-sided adjoint from the one-sided one).** The adjoint of the signed sandwich is determined by the adjoint of the signed left multiplication and the adjoint of the right translation; iterating, the adjoint of any word in the operators $\ell^{\alpha}_a$ and $R_b$ is the reversed word in the adjoints, and it remains in the algebra generated by the signed left multiplications and the right translations.

**Proof.** The adjoint is an anti-involution of the operator algebra, so it reverses words; the generators are mapped to generators by the theorem and by $(R_b)^{*}=R_{b^{-1}}$.

**Remark (no $*$-representation).** The map $a\mapsto\ell^{\alpha}_a$ is not a homomorphism, its composition law being $\ell^{\alpha}_a\ell^{\alpha}_b=L_{a\alpha(b)}$ of *The Signed Left Multiplication on a Group*; so the signed left multiplications do not form a $*$-representation of $G$. What they form is a set indexed by $G$ and closed under the adjoint, on which the adjoint acts as the involution $\sigma$ of the index set. The $*$-representation statement belongs to the unsigned left regular representation of *The Adjoint of the Left Multiplication on a Group*.

## Summary

The adjoint of the signed left multiplication is the signed left multiplication with index sent through the involution,

$$
\bigl(\ell^{\alpha}_a\bigr)^{*}=\ell^{\alpha}_{\alpha(a)^{-1}}=\ell^{\alpha}_{\sigma(a)},
\qquad \sigma=\iota\alpha,
$$

so the set $\{\ell^{\alpha}_a\}$ is closed under the adjoint and the index map $a\mapsto\ell^{\alpha}_a$ is a bijection intertwining $\sigma$ with the adjoint. The **self-adjoint** signed left multiplications are those with $\alpha(a)=a^{-1}$, that is those indexed by the fixed set $G^{\sigma}=I(\alpha)$ of the involution $\sigma$; the unsigned case is recovered at $\alpha=\mathrm{id}$, where $\sigma=\iota$ and the self-adjoint signed left multiplications are indexed by the $2$-torsion. Every signed left multiplication is **unitary**, being the signed sandwich with second parameter $e$.

The adjoint of the general signed sandwich factors through the signed left multiplication, $\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}=\ell^{\alpha}_{\alpha(a)^{-1}}\circ R_{b^{-1}}$, so the two-sided adjoint is built from the one-sided adjoint and the adjoint of the right translation. The signed left multiplications do not form a $*$-representation, their composition law being that of *The Signed Left Multiplication on a Group*; they form a set indexed by $G$ on which the adjoint is the involution $\sigma$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\ell^{\alpha}_a(x)=a\,\alpha(x)$ | the signed left multiplication |
| $\bigl(\ell^{\alpha}_a\bigr)^{*}=\ell^{\alpha}_{\alpha(a)^{-1}}$ | the adjoint |
| $\sigma=\iota\alpha=\alpha\iota$ | the involution of the index set |
| self-adjoint $\iff\alpha(a)=a^{-1}$ | indexed by the fixed set $G^{\sigma}=I(\alpha)$ |
| $\bigl(\ell^{\alpha}_a\bigr)^{*}\ell^{\alpha}_a=\mathrm{id}$ | unitarity |
| $\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}=\ell^{\alpha}_{\alpha(a)^{-1}}R_{b^{-1}}$ | the adjoint of the sandwich |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutions on a group, adjoints and the unitary elements.
- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, fourth edition, 1995), for the left regular representation and the involutions of the small groups.
- Marshall Hall, *The Theory of Groups* (Macmillan, 1959), for the regular representation and its matrices.
- I. Martin Isaacs, *Finite Group Theory* (American Mathematical Society, Graduate Studies in Mathematics 92, 2008), for automorphisms of order two, their fixed and inverted sets.
