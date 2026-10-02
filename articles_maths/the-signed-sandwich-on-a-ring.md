
# __The Signed Sandwich on a Ring__

## Introduction

A two-sided operator on a ring dresses one element between a left and a right factor: for $a, b \in A$ the **unsigned sandwich** is
$S_{a,b}(x) = axb$. When the ring carries an automorphism $\alpha$ of order two — the **grade involution** — the sandwich can be twisted in the middle, and the **signed sandwich** is $S^{\alpha}_{a,b}(x) = a\,\alpha(x)\,b$. The twist is a single substitution of $\alpha(x)$ for $x$, and it is the operator form of the parity sign that the graded algebras carry: an element of odd degree changes sign under $\alpha$, and the sandwich records that sign in the middle factor.

This article defines the two sandwiches, computes how each is built from the one-sided multiplications of *Left and Right Multiplication in a Ring*, and shows the exact relation between them: $S^{\alpha}_{a,b} = S_{a,b}\circ\alpha$, so the signed sandwich is the unsigned one precomposed with the grade involution, and the two coincide when $\alpha = \mathrm{id}$. It then specialises to the **reflections**, the signed sandwiches $S^{\alpha}_{u,u^{-1}}$ by a unit, and determines when such an operator is an involution: exactly when $u\,\alpha(u)$ is central.

The article assumes a ring with a grade involution. No involution of the elements is used; the involution $\sigma$ of a ring and the dagger built from it belong to the `* Theory` and `* Operator Theory` groups of this category, and the Hermitian sandwich, which pairs an element with its dagger, is the corresponding object there. The article stays inside Part I: no distance, norm, form or measure occurs, and the "reflection" is defined algebraically as an operator of order two, without any geometric reading. Throughout, $A$ is a ring with $1 \neq 0$, not assumed commutative; $\alpha$ is a **grade involution** of $A$, that is, an automorphism with $\alpha^2 = \mathrm{id}$; and $L_a$, $R_b$ are the one-sided multiplications.

## The Unsigned Sandwich

### Definition and the two-sided reading

**Definition.** For $a, b \in A$ the **unsigned sandwich** with parameters $a$ and $b$ is the additive map

$$
S_{a,b} : A \to A, \qquad S_{a,b}(x) = a\,x\,b .
$$

It is the composite $S_{a,b} = L_a \circ R_b = R_b \circ L_a$ of a left multiplication by $a$ and a right multiplication by $b$, and it is **additive** because the multiplications are, while it is **quadratic** in its parameters: it is linear in neither $a$ nor $b$ alone when $A$ is noncommutative, since $S_{aa',b}(x) = a a' x b = S_{a,b}(a'xb)$.

**Proposition.** For all $a, b, c, d \in A$,

$$
S_{a,b} \circ S_{c,d} = S_{ac,\,db}, \qquad S_{a,b}(1) = ab .
$$

The vanishing of the operator is the two-sided condition $S_{a,b} = 0 \iff aAb = 0$, and its kernel is the additive subgroup $\ker S_{a,b} = \{x : axb = 0\}$, which is not in general an ideal.

**Proof.** Composition and the value at the unit are immediate from associativity and the definition. $S_{a,b} = 0$ says $a x b = 0$ for every $x$, which is the two-sided condition $aAb = 0$; the kernel is the definition. In a noncommutative ring the single product $ab$ does not control the operator: in $M_2(k)$ take $a = E_{11}$ and $b = E_{22}$, so that $ab = 0$, yet $aE_{12}b = E_{12} \neq 0$ and $S_{a,b} \neq 0$.

### The generated operators

The unsigned sandwiches are exactly the products of one left and one right multiplication, and the composition law $S_{a,b}S_{c,d} = S_{ac,db}$ exhibits them as a monoid isomorphic to $A \times A^{\mathrm{op}}$ acting on $A$.

**Proposition.** The sandwiches form a submonoid of $\operatorname{End}(A)$ under composition, with identity $S_{1,1} = \mathrm{id}$, and $S_{a,b}$ is invertible exactly when $a$ and $b$ are units, in which case

$$
S_{a,b}^{-1} = S_{a^{-1},\,b^{-1}} .
$$

**Proof.** The composition law is closure, and $S_{1,1}(x) = x$. For invertibility, $S_{a,b}S_{a^{-1},b^{-1}} = S_{1,1} = S_{a^{-1},b^{-1}}S_{a,b}$ when $a, b$ are units; conversely if $S_{a,b}$ is invertible then $S_{a,b}(A) = aAb = A$, which forces $a$ and $b$ to be units (take $1$ in the image: $a x_1 b = 1 = a x_2 b$ gives left and right inverses).

**Remark.** The diagonal sandwich $S_{u,u^{-1}}$ with $u$ a unit is the **inner conjugation** $\operatorname{conj}_u(x) = uxu^{-1}$ of *Inner Automorphisms of a Ring*, and the composition law reads $\operatorname{conj}_u\operatorname{conj}_v = \operatorname{conj}_{uv}$. The non-diagonal sandwiches, with $b \neq a^{-1}$, are the general two-sided operators and are not automorphisms.

## The Grade Involution

### Definition

**Definition.** A **grade involution** of $A$ is an automorphism $\alpha \in \operatorname{Aut}(A)$ with $\alpha^2 = \mathrm{id}$; it is the **trivial** grade involution when $\alpha = \mathrm{id}$. The pair $(A, \alpha)$ is a **graded ring** in the sense of a $\mathbb{Z}/2$-graded ring, the decomposition being

$$
A = A_{\bar 0} \oplus A_{\bar 1}, \qquad A_{\bar 0} = \{x : \alpha(x) = x\}, \quad A_{\bar 1} = \{x : \alpha(x) = -x\},
$$

the **even** and **odd** parts, defined whenever $2$ is invertible in $A$.

**Proposition.** The even part $A_{\bar 0}$ is a subring and the odd part $A_{\bar 1}$ is an $A_{\bar 0}$-bimodule; the product of two odd elements is even, and $\alpha(xy) = \alpha(x)\alpha(y)$ is the multiplicativity that makes $A$ a $\mathbb{Z}/2$-graded ring: $A_i A_j \subseteq A_{i+j}$.

**Proof.** $\alpha(x\pm y) = \alpha(x)\pm\alpha(y)$ and $\alpha(xy) = \alpha(x)\alpha(y)$, so a product of two elements of signs $\pm$ has sign the product; the even part is closed under multiplication and contains $1$, and the odd part is closed under inversion and under multiplication by even elements.

**Remark (the two order-two maps).** A grade involution $\alpha$ **preserves** the product; an involution $\sigma$ of the elements, the subject of the `* Theory` group, **reverses** it. On a commutative ring the two notions coincide, on a noncommutative ring they do not, and the signed operators of this group are built from $\alpha$ alone. The composite $\delta = \sigma\circ\alpha$ of the two is the dagger, and it belongs to the `* Operator Theory` group.

### Conjugation by the grade involution

**Proposition.** For all $a, b \in A$,

$$
\alpha\,L_a\,\alpha^{-1} = L_{\alpha(a)}, \qquad \alpha\,R_b\,\alpha^{-1} = R_{\alpha(b)}, \qquad \alpha\,S_{a,b}\,\alpha^{-1} = S_{\alpha(a),\alpha(b)} .
$$

**Proof.** $\alpha(L_a(\alpha^{-1}(x))) = \alpha(a\,\alpha^{-1}(x)) = \alpha(a)x = L_{\alpha(a)}(x)$; the right case is the mirror, and the sandwich case is the two together.

**Corollary.** The grade involution acts on the monoid of sandwiches by the simultaneous substitution $a \mapsto \alpha(a)$, $b \mapsto \alpha(b)$; it fixes the sandwich $S_{a,b}$ exactly when $\alpha(a) = a$ and $\alpha(b) = b$, that is, when both parameters are even.

## The Signed Sandwich

### Definition and the relation to the unsigned one

**Definition.** For $a, b \in A$ the **signed sandwich** is

$$
S^{\alpha}_{a,b} : A \to A, \qquad S^{\alpha}_{a,b}(x) = a\,\alpha(x)\,b .
$$

It is the composite $S^{\alpha}_{a,b} = L_a \circ R_b \circ \alpha = S_{a,b}\circ\alpha$ of the unsigned sandwich with the grade involution, and it is additive.

**Theorem (the signed sandwich is the unsigned sandwich at $\alpha$).** For all $a, b \in A$,

$$
S^{\alpha}_{a,b} = S_{a,b} \circ \alpha, \qquad\text{and}\qquad S^{\alpha}_{a,b} = \alpha \circ S_{\alpha^{-1}(a),\alpha^{-1}(b)} .
$$

In particular the two sandwiches coincide exactly when $\alpha = \mathrm{id}$, and $S^{\alpha}_{a,b}(x) = S_{a,b}(\alpha(x))$ for every $x$.

**Proof.** $S_{a,b}(\alpha(x)) = a\alpha(x)b = S^{\alpha}_{a,b}(x)$, which is the first identity. For the second, $\alpha(S_{\alpha^{-1}(a),\alpha^{-1}(b)}(x)) = \alpha(\alpha^{-1}(a)\,x\,\alpha^{-1}(b)) = a\,\alpha(x)\,b$.

**Corollary (linearity in the parameters up to the sign).** The signed sandwich is linear in $a$ and in $b$ as additive maps, $S^{\alpha}_{a+a',b} = S^{\alpha}_{a,b} + S^{\alpha}_{a',b}$, and it is $\alpha$-twisted in the **middle** argument: it is additive there, and it is the unsigned sandwich that carries the twist, not the parameters.

### Composition

**Proposition.** For all $a, b, c, d \in A$,

$$
S^{\alpha}_{a,b} \circ S^{\alpha}_{c,d} = S^{\alpha}_{a\,\alpha(c),\; b\,\alpha(d)} .
$$

**Proof.** Using $S^{\alpha}_{c,d} = S_{c,d}\alpha$ and the commutation $\alpha S_{c,d} = S_{\alpha(c),\alpha(d)}\alpha$ of the previous section, the composite is $S_{a,b}\alpha S_{c,d}\alpha = S_{a,b}S_{\alpha(c),\alpha(d)}\alpha^2 = S_{a\alpha(c),\,b\alpha(d)}$, and this is $S^{\alpha}_{a\alpha(c),b\alpha(d)}$ by the definition.

**Corollary.** The signed sandwiches form a submonoid of $\operatorname{End}(A)$, with identity $S^{\alpha}_{1,1} = \alpha$. The monoid law is not the sandwich law of the unsigned case: the composite of $S^{\alpha}_{a,b}$ and $S^{\alpha}_{c,d}$ inserts $\alpha$ into the parameters, which is the operator form of the sign rule the grading imposes.

**Proposition (the diagonal case).** For a unit $u$,

$$
S^{\alpha}_{u,u^{-1}}(x) = u\,\alpha(x)\,u^{-1},
$$

the **signed inner conjugation** by $u$, and

$$
\bigl(S^{\alpha}_{u,u^{-1}}\bigr)^2 = S^{\alpha}_{u\alpha(u),\,u^{-1}\alpha(u^{-1})} = \operatorname{conj}_{u\alpha(u)} .
$$

**Proof.** The first display is the definition with $b=u^{-1}$. The square follows from the composition law: $S^{\alpha}_{u,u^{-1}}\circ S^{\alpha}_{u,u^{-1}} = S^{\alpha}_{u\alpha(u),\,u^{-1}\alpha(u^{-1})}$, and $u^{-1}\alpha(u^{-1}) = (u\alpha(u))^{-1}$ because $\alpha(u^{-1}) = \alpha(u)^{-1}$, so the composite is the inner conjugation by $u\alpha(u)$.

## Reflections Realised by the Signed Sandwich

### Definition and the involutive case

**Definition.** A **reflection** of the graded ring $(A,\alpha)$ is a signed two-sided operator $r_u = S^{\alpha}_{u,u^{-1}}$ by a unit $u$; it is a genuine reflection, that is, an operator of order two, exactly when $r_u^2 = \mathrm{id}$.

**Theorem.** Let $u \in A^\times$. The signed inner conjugation $r_u$ is an involution if and only if $u\,\alpha(u)$ is central; it is then the inner automorphism $\operatorname{conj}_{u\alpha(u)}$ of order two, and it can be written

$$
r_u(x) = u\,\alpha(x)\,u^{-1}, \qquad r_u^2(x) = x \iff u\,\alpha(u) \in Z(A).
$$

**Proof.** By the composition computation, $r_u^2 = \operatorname{conj}_{u\alpha(u)}$, and an inner conjugation is the identity exactly when the conjugating element is central. When $u\alpha(u)$ is central, $r_u^2 = \mathrm{id}$ is automatic since $\operatorname{conj}_{u\alpha(u)}(x) = x$. Conversely if $r_u^2 = \mathrm{id}$ then $u\alpha(u) x = x\, u\alpha(u)$ for all $x$, so $u\alpha(u)$ is central.

**Corollary.** If $u$ is fixed by $\alpha$ ($\alpha(u) = u$), then $u\alpha(u) = u^2$ and the reflection is an involution exactly when $u^2$ is central; if $u$ is negated by $\alpha$ ($\alpha(u) = -u$) and $2$ is invertible, then $u\alpha(u) = -u^2$, again central exactly when $u^2$ is central. In particular, if $u^2 \in Z(A)$, then $r_u$ is an involution whichever parity $u$ has.

### Examples

**(a) The trivial grade involution.** If $\alpha = \mathrm{id}$, then $S^{\alpha}_{a,b} = S_{a,b}$ and $r_u = \operatorname{conj}_u$; here $r_u^2 = \operatorname{conj}_{u^2}$, which is the identity exactly when $u^2 \in Z(A)$, the same criterion as in the general case with $\alpha(u) = u$.

**(b) The matrix ring with an even/odd grading.** Let $A = M_2(k)$ and let $\alpha$ be the automorphism $X \mapsto JXJ^{-1}$ with $J = \operatorname{diag}(1,-1)$, so that $\alpha^2 = \mathrm{id}$ and the even part is the diagonal matrices and the odd part the off-diagonal ones. For the unit $u = E_{12} + E_{21}$ one has $\alpha(u) = -u$, so $u\alpha(u) = -u^2$; and $u^2 = E_{11} + E_{22} = I$ is central, so $u\alpha(u) = -I$ is central and $r_u$ is an involution. Explicitly $r_u(x) = u\alpha(x)u^{-1}$, and since $u^{-1} = u$ and $\alpha(u)=-u$, one computes $r_u^2(x) = u\alpha(u)x(u\alpha(u))^{-1} = (-I)x(-I)^{-1} = x$.

**(c) A degenerate case.** Let $A = M_2(k)$ with $\alpha = \mathrm{id}$ and let $u = E_{12} + I$. Then $\alpha(u) = u$ and $u^2 = I + 2E_{12}$, which is not central, so $r_u = \operatorname{conj}_u$ has $r_u^2 = \operatorname{conj}_{u^2} \neq \mathrm{id}$: the operator is an automorphism of infinite order, not a reflection. The failure is exactly the non-centrality of $u\alpha(u)$, and it is the degenerate case the menu records.

## Summary

For a ring $A$ with a grade involution $\alpha$, the **unsigned sandwich** is $S_{a,b}(x) = axb = L_aR_b$, with composition $S_{a,b}S_{c,d} = S_{ac,db}$ and inverses $S_{a^{-1},b^{-1}}$ on the units, and the **signed sandwich** is $S^{\alpha}_{a,b}(x) = a\alpha(x)b$. The two are related by $S^{\alpha}_{a,b} = S_{a,b}\circ\alpha$, so the signed sandwich is the unsigned one at the grade-involution of its argument, and they coincide exactly when $\alpha = \mathrm{id}$. The signed sandwiches compose as $S^{\alpha}_{a,b}S^{\alpha}_{c,d} = S^{\alpha}_{a\alpha(c),b\alpha(d)}$, a monoid law with identity $\alpha$ that inserts the grade involution into the parameters, which is the sign rule of the grading.

The diagonal signed sandwich $r_u = S^{\alpha}_{u,u^{-1}}$ is the signed inner conjugation $x \mapsto u\alpha(x)u^{-1}$, and its square is the inner conjugation by $u\alpha(u)$. It is therefore an involution, a **reflection**, exactly when $u\,\alpha(u)$ is central; this covers the case $u^2 \in Z(A)$ for either parity of $u$, and it fails in the degenerate case of a non-central $u\alpha(u)$, where the operator is an automorphism of infinite order. No involution of the elements, no dagger and no form occurs; the Hermitian sandwich, in which the right factor is the dagger of the left, is the corresponding construction of the `* Operator Theory` group of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | Ring with $1 \neq 0$, not assumed commutative |
| $\alpha$ | Grade involution, an automorphism with $\alpha^2 = \mathrm{id}$ |
| $S_{a,b}(x) = axb$ | Unsigned sandwich, the two-sided operator $L_aR_b$ |
| $S^{\alpha}_{a,b}(x) = a\alpha(x)b$ | Signed sandwich |
| $S^{\alpha}_{a,b} = S_{a,b}\circ\alpha$ | The signed sandwich is the unsigned one at $\alpha$ |
| $S_{a,b}S_{c,d} = S_{ac,db}$ | Composition of unsigned sandwiches |
| $S^{\alpha}_{a,b}S^{\alpha}_{c,d} = S^{\alpha}_{a\alpha(c),b\alpha(d)}$ | Composition of signed sandwiches |
| $r_u = S^{\alpha}_{u,u^{-1}}(x) = u\alpha(x)u^{-1}$ | Reflection, signed inner conjugation by a unit |
| $r_u^2 = \operatorname{conj}_{u\alpha(u)}$ | A reflection is an involution iff $u\alpha(u) \in Z(A)$ |
| $A_{\bar 0}, A_{\bar 1}$ | Even and odd parts of the grading by $\alpha$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for derivations, automorphisms of order two and the grading an involution of order two defines.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for involutions of a ring, the grade involution and the two-sided operators built from them.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the sandwich action and the reflections it realises.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the graded structure of a Clifford algebra and the parity sign carried by its involutions.
