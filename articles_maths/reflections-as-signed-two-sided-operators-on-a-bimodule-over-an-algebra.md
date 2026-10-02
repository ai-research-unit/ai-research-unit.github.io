
# __Reflections as Signed Two-Sided Operators on a Bimodule over an Algebra__

## Introduction

A reflection of a graded bimodule is a two-sided operator of order two whose middle factor carries the grade involution. *The Signed Sandwich on a Bimodule over an Algebra* defined the operator $r_u=S^{\alpha}_{u,u^{-1}}$ and found that its square is the inner conjugation by $u\alpha(u)$; this article reads the construction backwards. Given an operator of order two that is built from a unit and the grade involution, which unit realises it, and when is the operator genuinely an involution? The answer pairs the reflections with the **elements acting by an involution**, that is, the units $u$ with $u\alpha(u)$ in the centralizer of the bimodule, and it fails in two ways: when $u\alpha(u)$ is not in that centralizer the operator has infinite order, and when the bimodule is not faithful different units realise the same reflection.

The article assumes the graded bimodule of *The Signed Sandwich on a Bimodule over an Algebra*, and the operator layer of *Left and Right Multiplication of a Module* and *Module Endomorphisms*. The signed operators built from the involution of the elements and from the adjoint belong to the `* Operator Theory` group and do not occur here. The article stays inside Part I: no distance, norm, form or limit, and *reflection* means an operator of order two without any geometric reading. Throughout, $A$ is a unital associative $R$-algebra with a grade involution $\alpha$, ${}_A M_A$ is a graded $(A,A)$-bimodule, $C_A(M)=\{w \in A : wx=xw \text{ for all } x \in M\}$ is the centralizer of the bimodule, and $r_u=S^{\alpha}_{u,u^{-1}}$.

## Reflections and the Signed Sandwich

### Definition

**Definition.** Let $u \in A^{\times}$. The **signed inner conjugation** by $u$ is the operator

$$
r_u=S^{\alpha}_{u,u^{-1}} : M \to M, \qquad r_u(x)=u\,\alpha(x)\,u^{-1}.
$$

A **reflection** of the graded bimodule is a signed two-sided operator $r_u$ that is an involution, $r_u^{2}=\mathrm{id}_M$.

**Proposition.** The signed inner conjugations are invertible, with

$$
r_u^{-1}=r_{\alpha(u)^{-1}}=r_{\alpha(u^{-1})},
$$

and they satisfy the product rule

$$
r_u\,r_v=\operatorname{conj}_{u\alpha(v)} \qquad (u,v \in A^{\times}),
$$

where $\operatorname{conj}_w(x)=wxw^{-1}$. The product of two reflections is therefore an inner conjugation, and it is a reflection only when it can be rewritten in the form $r_w$; in general the reflections are not closed under composition.

*Proof.* The inverse is the corollary on invertibility of *The Signed Sandwich on a Bimodule over an Algebra*. For the product, the composition law gives $r_ur_v=S_{u\alpha(v),\,\alpha(v^{-1})u^{-1}}$; since $\alpha(v^{-1})=\alpha(v)^{-1}$ the second parameter is $\alpha(v)^{-1}u^{-1}=(u\alpha(v))^{-1}$, so the composite is the unsigned diagonal sandwich $S_{w,w^{-1}}$ with $w=u\alpha(v)$, that is $\operatorname{conj}_w$. A reflection as a set of operators is the image of $A^{\times}$ under $u\mapsto r_u$, which need not be a subgroup. $\square$

### The criterion

**Theorem.** For $u \in A^{\times}$ the operator $r_u$ is a reflection if and only if $u\alpha(u) \in C_A(M)$:

$$
r_u^{2}=\operatorname{conj}_{u\alpha(u)}=\mathrm{id}_M \iff u\,\alpha(u) \in C_A(M).
$$

When the condition holds, $r_u$ is the inner automorphism $\operatorname{conj}_{u\alpha(u)}$ of order two; when it fails, $r_u$ is not a reflection, its order being whatever the order of the coset of $u\alpha(u)$ in $A^{\times}/C_A(M)^{\times}$ is.

*Proof.* The square is $\operatorname{conj}_{u\alpha(u)}$ by the proposition, and an inner conjugation is the identity exactly when the conjugating element commutes with every element of $M$, which is the definition of $C_A(M)$. If the condition fails, the square is a nontrivial inner conjugation, so $r_u$ is not of order two and is not a reflection. Its order may be finite or infinite: $\operatorname{conj}_w^{k}=\operatorname{conj}_{w^{k}}$ is the identity exactly when $w^{k} \in C_A(M)$, and a unit outside $C_A(M)$ may still have a power inside it. $\square$

The theorem names the units that realise reflections.

**Definition.** A unit $u \in A^{\times}$ **acts by an involution** when the signed inner conjugation $r_u$ is an involution, that is, when $u\alpha(u) \in C_A(M)$.

Thus the reflections are exactly the operators $r_u$ with $u$ acting by an involution, and the correspondence to be studied is between the reflections and the cosets of these units.

### The special case $u\alpha(u)=1$

**Proposition.** If $u\alpha(u)=1$, that is $\alpha(u)=u^{-1}$, then $u$ acts by an involution and

$$
r_u(x)=u\,\alpha(x)\,u^{-1}=u\,\alpha(x)\,\alpha(u)=u\,\alpha(xu).
$$

*Proof.* $\alpha(u)=u^{-1}$ gives $u\alpha(u)=1 \in C_A(M)$, so the criterion holds; the displayed rewriting uses $u^{-1}=\alpha(u)$ and the automorphism property $\alpha(a)\alpha(b)=\alpha(ab)$. $\square$

The elements with $\alpha(u)=u^{-1}$ are the **$\alpha$-antisymmetric** units; they always act by an involution, and they form a subgroup of $A^{\times}$ when the centre contains a suitable element, as the examples show.

## The Correspondence

### The map from units to reflections

**Theorem.** For units $u,v \in A^{\times}$,

$$
r_u=r_v \iff v^{-1}u \in C_A(M).
$$

Consequently the map $u \mapsto r_u$ is constant on the right cosets of the subgroup $C_A(M)^{\times}=C_A(M)\cap A^{\times}$ and separates distinct cosets; its image is the set of reflections, and the criterion "$u$ acts by an involution" depends only on the coset.

*Proof.* $r_u=r_v$ says $u\alpha(x)u^{-1}=v\alpha(x)v^{-1}$ for all $x$, that is $w\alpha(x)w^{-1}=\alpha(x)$ with $w=v^{-1}u$, that is $w\alpha(x)=\alpha(x)w$ for all $x$. Since $\alpha$ is bijective on $M$ this says $wy=yw$ for all $y \in M$, which is $w \in C_A(M)$. The subgroup statement is the proposition below, and the dependence on the coset is the proposition after it. $\square$

**Proposition.** $C_A(M)$ is a subalgebra of $A$ containing $Z(A)$, and $C_A(M)^{\times}$ is a subgroup of $A^{\times}$.

*Proof.* $C_A(M)$ is closed under addition, multiplication and the scalars, and contains the centre because central elements commute with everything. If $w \in C_A(M)$ is a unit then $w^{-1}x=w^{-1}xww^{-1}=w^{-1}wxw^{-1}=xw^{-1}$ for all $x$, so $w^{-1} \in C_A(M)$; hence the units of $C_A(M)$ form a subgroup of $A^{\times}$. $\square$

**Proposition.** If $u$ acts by an involution and $c \in C_A(M)^{\times}$, then $uc$ acts by an involution and $r_{uc}=r_u$.

*Proof.* $r_{uc}=r_u$ by the theorem, since $u^{-1}(uc)=c \in C_A(M)$; and the criterion is a property of the operator $r_u$, so it holds at $uc$ as well. $\square$

### The quotient description

The correspondence is therefore a bijection of sets

$$
\{u \in A^{\times} : u\alpha(u) \in C_A(M)\} \big/ C_A(M)^{\times} \;\longleftrightarrow\; \{\text{reflections of } M\},
$$

sending the coset of $u$ to $r_u$. For a faithful bimodule $C_A(M)=Z(A)$ and the correspondence is between reflections and the cosets of $Z(A)^{\times}$ in the units that act by an involution.

**Corollary (the faithful case).** If $M$ is faithful over $A$, then $r_u=r_v$ exactly when $v^{-1}u \in Z(A)$, and $r_u$ is a reflection exactly when $u\alpha(u) \in Z(A)$.

*Proof.* $C_A(M)=Z(A)$ when $M$ is faithful, by the definition of the centralizer. $\square$

### The elements of order two

**Proposition.** Suppose $\alpha(u)=u$ and $u^{2} \in C_A(M)$. Then $u$ acts by an involution and $r_u=\operatorname{conj}_u$. In particular every involution $u$ of $A$ with $u^{2}=1$ that commutes with the action on $M$ realises a reflection.

*Proof.* $u\alpha(u)=u^{2} \in C_A(M)$; and $r_u(x)=u\alpha(x)u^{-1}=uxu^{-1}$ because $\alpha(u)=u$, so $r_u=\operatorname{conj}_u$, whose square is $\operatorname{conj}_{u^{2}}=\mathrm{id}$. $\square$

## The Degenerate Cases

### Failure of the involution property

The first failure is the non-involutive operator.

**Proposition.** If $u\alpha(u) \notin C_A(M)$ then $r_u$ is not a reflection: its square is the nontrivial inner conjugation $\operatorname{conj}_{u\alpha(u)}$, so $r_u^{2}\neq\mathrm{id}_M$. Its order is the order of the class of $u\alpha(u)$ in $A^{\times}/C_A(M)^{\times}$ and may be finite or infinite.

*Proof.* Immediate from the criterion and the computation of the powers of $\operatorname{conj}_w$, namely $\operatorname{conj}_w^{k}=\operatorname{conj}_{w^{k}}$. $\square$

**Example.** Let $A=M_2(k)$ with $\alpha=\mathrm{id}$, $M=A$, and $u=E_{12}+I$. Then $u^{2}=I+2E_{12}\notin Z(A)=C_A(M)$, so $r_u=\operatorname{conj}_u$ has $r_u^{2}=\operatorname{conj}_{u^{2}}\neq\mathrm{id}$: the operator has infinite order and the unit does not act by an involution.

### Failure of uniqueness

The second failure is the non-faithful module.

**Proposition.** If $C_A(M) \supsetneq Z(A)$ — for instance when $M$ is not faithful, or when the action of $A$ on $M$ factors through a quotient with a larger centre — then there are units $u \neq v$ with $r_u=r_v$: the element is not recoverable from the reflection.

*Proof.* Take $v=uc$ with $c \in C_A(M)^{\times}$, $c \neq 1$. Then $v \neq u$ but $r_v=r_u$ by the theorem. $\square$

**Example.** Let $A=M_2(k)$ act on $M=k^2$ through the quotient $k$ — that is, $A$ acts by scalars through an algebra homomorphism $A \to k$ — so that every element of $M_2(k)$ acts as a scalar and $C_A(M)$ is the whole algebra. Then every unit of $A$ realises the same signed inner conjugation on $M$, and the correspondence collapses: the reflection is one operator and the class of realising units is all of $A^{\times}$.

### The trivial grade involution

**Proposition.** If $\alpha=\mathrm{id}$ then the criterion is $u^{2} \in C_A(M)$, the correspondence sends $u$ to $\operatorname{conj}_u$, and the reflections are the inner conjugations by units with $u^{2} \in C_A(M)$.

*Proof.* $u\alpha(u)=u^{2}$ and $r_u(x)=uxu^{-1}$ when $\alpha=\mathrm{id}$. $\square$

### The trivial action of the grade involution

**Proposition.** If $\alpha$ fixes every element of $M$ then $r_u=\operatorname{conj}_u$ for every $u$, whatever $\alpha$ does on $A$; the signed and the unsigned inner conjugations coincide, and the criterion reduces to $u^{2} \in C_A(M)$.

*Proof.* $\alpha(x)=x$ for $x \in M$, so $r_u(x)=uxu^{-1}$, and $u\alpha(u)$ acts on $M$ as $u^{2}$. $\square$

## Examples

**(a) The regular bimodule.** For $M={}_A A_A$ the bimodule is faithful and $C_A(M)=Z(A)$; the reflections are the $r_u$ with $u\alpha(u) \in Z(A)$, and $r_u=r_v$ exactly when $v^{-1}u \in Z(A)$. This is the criterion of the ring-level article, now read as a statement about cosets.

**(b) The matrix algebra with an even/odd grading.** For $A=M_2(k)$, $J=\operatorname{diag}(1,-1)$, $\alpha(X)=JXJ^{-1}$, and $M=A$, the unit $u=E_{12}+E_{21}$ has $\alpha(u)=-u$ and $u^{2}=I$, so $u\alpha(u)=-I \in Z(A)$ and $r_u$ is a reflection; the units $-u$ and $u$ realise the same reflection because $(-u)^{-1}u=-I \in Z(A)$.

**(c) The antisymmetric units.** For $A=\mathbb{H}$ with the grade involution $\alpha$ given by quaternion conjugation, a pure imaginary unit $u$ satisfies $\alpha(u)=-u$ and $u^{2}=-1$, so $u\alpha(u)=-u^{2}=1$ is central and every such unit acts by an involution: $r_u(x)=u\alpha(x)u^{-1}$ is a reflection. The correspondence is a bijection from the units of $\mathbb{H}$ modulo $\mathbb{R}^{\times}$ onto these reflections.

**(d) A non-faithful module.** For $A=M_n(k)$ acting on $k$ through a character $A \to k$, $C_A(M)=A$, and all units realise the same reflection; the correspondence is maximally degenerate.

## Summary

For a graded bimodule ${}_A M_A$ with grade involution $\alpha$, the signed inner conjugation by a unit $u$ is $r_u(x)=u\alpha(x)u^{-1}$, with $r_u^{-1}=r_{\alpha(u)^{-1}}$ and $r_ur_v=\operatorname{conj}_{u\alpha(v)}$. It is a reflection exactly when $u\alpha(u)$ lies in the centralizer $C_A(M)$ of the bimodule, and the units with this property are the units that act by an involution; the elements with $\alpha(u)=u^{-1}$ are the basic examples. The map $u\mapsto r_u$ is constant on the right cosets of $C_A(M)^{\times}$ and separates distinct cosets, so the reflections correspond bijectively to the cosets of $C_A(M)^{\times}$ in the set of units acting by an involution; for a faithful bimodule the centralizer is the centre $Z(A)$. Two degenerations occur: a unit with $u\alpha(u) \notin C_A(M)$ gives an operator of infinite order and no reflection, and a non-faithful bimodule makes the centralizer larger than the centre, so distinct units realise the same reflection and the element cannot be recovered from the operator. When $\alpha=\mathrm{id}$ or when $\alpha$ fixes the module, the signed conjugations reduce to the ordinary ones and the criterion is $u^{2} \in C_A(M)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | unital associative $R$-algebra with grade involution $\alpha$ |
| ${}_A M_A$ | graded $(A,A)$-bimodule |
| $\alpha$ | grade involution, $\alpha^{2}=\mathrm{id}$, compatible with the bimodule |
| $r_u=S^{\alpha}_{u,u^{-1}}$ | signed inner conjugation by a unit, $x\mapsto u\alpha(x)u^{-1}$ |
| $r_u^{2}=\operatorname{conj}_{u\alpha(u)}$ | the square is an inner conjugation |
| $C_A(M)$ | centralizer of the bimodule, $\{w : wx=xw \text{ for all } x\}$ |
| $C_A(M)^{\times}$ | the units of $C_A(M)$, a subgroup of $A^{\times}$ |
| $u$ acts by an involution | $u\alpha(u) \in C_A(M)$, equivalently $r_u$ is a reflection |
| $r_ur_v=\operatorname{conj}_{u\alpha(v)}$ | product of two signed inner conjugations |
| $Z(A)$ | the centre of $A$, equal to $C_A(M)$ for a faithful $M$ |
| $\alpha(u)=u^{-1}$ | the antisymmetric units, always acting by an involution |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for order-two automorphisms and the two-sided operators they define.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the sandwich action, the reflections and the criterion for an order-two operator.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, second edition, 2001), for inner conjugations and reflections in a graded algebra.
- T. Y. Lam, *Lectures on Modules and Rings* (Springer, 1999), for centralizers of a module and the units that act trivially on it.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for automorphisms of order two and the group they generate with the inner automorphisms.
