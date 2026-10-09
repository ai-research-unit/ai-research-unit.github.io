
# __The Signed Left Multiplication on a Module over an Algebra__

## Introduction

The signed sandwich of *The Signed Sandwich on a Bimodule over an Algebra* is built from two one-sided operators; this article isolates the left one. For an algebra $A$ with a grade involution $\alpha$ acting compatibly on a module $M$, the **signed left multiplication** by $a$ is the operator $L^{\alpha}_a(m)=a\,\alpha(m)$. It is the unsigned left multiplication of *Left and Right Multiplication of a Module* with the grade involution inserted before the action, and it is the operator that carries the parity sign of the grading.

The article defines the signed left multiplication, relates it to its unsigned sibling, computes the composition of the two families, and determines the elements fixed by a signed left multiplication. The signed sandwich itself is treated in *The Signed Sandwich on a Bimodule over an Algebra*, and the corresponding right-handed operator is obtained from the same construction on the opposite algebra. The involution of the elements $\sigma$ and the adjoint belong to the `* Theory` and `* Operator Theory` groups and do not occur here. The article stays inside Part I: no distance, norm, form or limit, and the word *reflection* names an operator of order two. Throughout, $R$ is a commutative ring with $1 \neq 0$, $A$ is a unital associative $R$-algebra with grade involution $\alpha$, $M$ is a graded left $A$-module, $L_a(m)=am$ is the unsigned left multiplication, and $L^{\alpha}_a=L_a\circ\alpha$.

## The Signed Left Multiplication

### Definition

**Definition.** A **graded left $A$-module** is a left $A$-module $M$ with an additive map, written $\alpha$, such that

$$
\alpha^{2}=\mathrm{id}, \qquad \alpha(am)=\alpha(a)\,\alpha(m) \qquad (a \in A,\ m \in M).
$$

When $2$ is invertible, $M=M_{\bar0}\oplus M_{\bar1}$ with $M_{\bar0}=\{m : \alpha(m)=m\}$ and $M_{\bar1}=\{m : \alpha(m)=-m\}$.

**Definition.** For $a \in A$ the **signed left multiplication** by $a$ is

$$
L^{\alpha}_a : M \to M, \qquad L^{\alpha}_a(m)=a\,\alpha(m).
$$

**Proposition.** $L^{\alpha}_a \in \operatorname{End}_R(M)$ and $L^{\alpha}_a=L_a\circ\alpha=\alpha\circ L_{\alpha^{-1}(a)}$.

*Proof.* It is the composite of the two $R$-linear maps $L_a$ and $\alpha$; the second identity is $\alpha(L_{\alpha^{-1}(a)}(m))=\alpha(\alpha^{-1}(a)\,m)=a\,\alpha(m)$. $\square$

The map $a \mapsto L^{\alpha}_a$ is $R$-linear and additive in $a$, but it is **not** multiplicative: the composition of two of them is computed below, and it returns an unsigned left multiplication.

### Relation to the unsigned left multiplication

**Theorem.** For all $a \in A$,

$$
L^{\alpha}_a=L_a\circ\alpha, \qquad L^{\alpha}_a=\alpha\circ L_{\alpha^{-1}(a)}, \qquad L^{\alpha}_a\circ\alpha=L_a, \qquad \alpha\circ L^{\alpha}_a=L_{\alpha(a)}\circ\alpha .
$$

In particular $L^{\alpha}_a=L_a$ for all $a$ exactly when $\alpha=\mathrm{id}$ on $M$, and $L^{\alpha}_1=\alpha$.

*Proof.* The first two displays are the proposition. For the third, $L^{\alpha}_a(\alpha(m))=a\,\alpha(\alpha(m))=am=L_a(m)$. For the fourth, $\alpha(L^{\alpha}_a(m))=\alpha(a\alpha(m))=\alpha(a)m=L_{\alpha(a)}(m)$; composing with $\alpha$ gives the displayed identity. Setting $a=1$ gives $L^{\alpha}_1=\alpha$. $\square$

Thus the signed left multiplication is the unsigned one at the grade involution of its argument, and the two families differ by the single operator $\alpha$: the signed family is $\{L_a\alpha\}$ and the unsigned family is $\{L_a\}$.

### Kernel, image and invertibility

**Proposition.** For every $a \in A$,

$$
\ker L^{\alpha}_a=\alpha(\ker L_a), \qquad \operatorname{im} L^{\alpha}_a=aM, \qquad L^{\alpha}_a=0 \iff aM=0 .
$$

Consequently $L^{\alpha}_a$ is injective exactly when $L_a$ is, it is surjective exactly when $L_a$ is, and it is invertible exactly when $a$ acts invertibly on $M$.

*Proof.* $L^{\alpha}_a(m)=0$ says $\alpha(m) \in \ker L_a$, that is $m \in \alpha(\ker L_a)$ because $\alpha$ is an involution. The image is $a\alpha(M)=aM$. The last clauses follow because $\alpha$ is a bijection, and $L_a$ is invertible exactly when $am=0 \Rightarrow m=0$ and $aM=M$. $\square$

The signed and the unsigned left multiplication of the same element have the same image but conjugate kernels.

## The Graded Composition Rule

### The four general products

The composition of the signed and the unsigned left multiplications follows the parity of the twist, exactly as for the sandwiches.

**Theorem.** For all $a,b \in A$,

$$
L_a\circ L_b=L_{ab}, \qquad L^{\alpha}_a\circ L_b=L^{\alpha}_{a\alpha(b)},
$$

$$
L_a\circ L^{\alpha}_b=L^{\alpha}_{ab}, \qquad L^{\alpha}_a\circ L^{\alpha}_b=L_{a\alpha(b)}.
$$

Thus a product of two left multiplications of the same parity is unsigned and a product of two of opposite parity is signed: the family $\{L_a\}\cup\{L^{\alpha}_a\}$ is a monoid graded by $\mathbb{Z}/2$, the unsigned operators even and the signed operators odd.

*Proof.* The first is the homomorphism property of $L$. For the second, $L^{\alpha}_a(L_b(m))=a\,\alpha(bm)=a\alpha(b)\alpha(m)=L^{\alpha}_{a\alpha(b)}(m)$. For the third, $L_a(L^{\alpha}_b(m))=a\,b\,\alpha(m)=L^{\alpha}_{ab}(m)$. For the fourth, $L^{\alpha}_a(L^{\alpha}_b(m))=a\,\alpha(b\alpha(m))=a\,\alpha(b)\,m=L_{a\alpha(b)}(m)$, the two grade involutions cancelling. $\square$

**Corollary.** The signed left multiplications are closed under composition with the unsigned ones to the extent the rule permits: the product of an even number of signed operators is unsigned, and the operator $\alpha=L^{\alpha}_1$ is the odd generator.

*Proof.* Iterate the four rules; the parity of the number of signed factors determines the parity of the product. $\square$

### The generated algebra

The two families generate a single algebra, and the rule above identifies it as a crossed product.

**Proposition.** Let $C$ be the $R$-subalgebra of $\operatorname{End}_R(M)$ generated by the operators $L_a$ and $L^{\alpha}_a$, $a \in A$. Then $C$ is generated by $L_A$ and $\alpha$, and the map

$$
A \rtimes \mathbb{Z}/2 \to C, \qquad a \otimes \epsilon \mapsto L_a\alpha^{\epsilon},
$$

is a surjective homomorphism of $R$-algebras, where $A\rtimes\mathbb{Z}/2$ is the crossed product with multiplication $(a,\epsilon)(b,\eta)=(a\,\alpha^{\epsilon}(b),\,\epsilon+\eta)$.

*Proof.* $L^{\alpha}_a=L_a\alpha$, so $L_A$ and $\alpha$ generate everything; the crossed-product multiplication is designed so that $(a,\epsilon)\mapsto L_a\alpha^{\epsilon}$ respects it: $\alpha L_b\alpha^{-1}=L_{\alpha(b)}$, which is the twist in $(a,\epsilon)(b,\eta)$. $\square$

The crossed product, its multiplication and its relation to the grading are the subject of *Crossed Products*, named here and not developed.

### Reflections among the signed left multiplications

**Proposition.** For every $a \in A$,

$$
\bigl(L^{\alpha}_a\bigr)^{2}=L_{a\alpha(a)} .
$$

Consequently $L^{\alpha}_a$ is an involution if and only if $a\alpha(a)$ acts as the identity on $M$, that is, $a\alpha(a)-1 \in \operatorname{Ann}_A(M)$; for a faithful module this says $a\alpha(a)=1$.

*Proof.* $L^{\alpha}_a(L^{\alpha}_a(m))=a\,\alpha(a\alpha(m))=a\,\alpha(a)\,m=L_{a\alpha(a)}(m)$. $\square$

The result is the one-sided case of the reflection criterion of the sandwich articles: a signed one-sided operator is an involution exactly when the product $a\alpha(a)$ is absorbed by the annihilator.

## The Elements Fixed by a Signed Left Multiplication

### The fixed set

**Definition.** For $a \in A$ the **fixed set** of $L^{\alpha}_a$ is

$$
\operatorname{Fix}(L^{\alpha}_a)=\{m \in M : a\,\alpha(m)=m\}.
$$

It is the set of elements the signed operator leaves unchanged; it is not in general a submodule, because $L^{\alpha}_a$ is not in general $A$-linear.

**Proposition.** For $a \in A$, $\operatorname{Fix}(L^{\alpha}_a)$ is the set of solutions of the $\alpha$-twisted equation $a\alpha(m)=m$. In particular

$$
\operatorname{Fix}(L^{\alpha}_1)=\operatorname{Fix}(\alpha)=M_{\bar0},
$$

the even part of the module, and if $a \in \operatorname{Ann}_A(M)$ then $\operatorname{Fix}(L^{\alpha}_a)=\{0\}$.

*Proof.* The first is the definition; $L^{\alpha}_1=\alpha$ gives the second; and $aM=0$ turns $a\alpha(m)=m$ into $m=0$. $\square$

### The even case

When $a$ is fixed by the grade involution, the signed left multiplication commutes with it and preserves the two parts of the module, and the fixed set splits.

**Theorem.** Let $2$ be invertible and let $a \in A$ with $\alpha(a)=a$. Then $L^{\alpha}_a$ commutes with $\alpha$, hence preserves $M_{\bar0}$ and $M_{\bar1}$, and

$$
\operatorname{Fix}(L^{\alpha}_a)=\{m_0 \in M_{\bar0} : am_0=m_0\} \oplus \{m_1 \in M_{\bar1} : am_1=-m_1\}.
$$

For a unit $a$ this is the sum of the $1$-eigenspace of $L_a$ on $M_{\bar0}$ and the $(-1)$-eigenspace of $L_a$ on $M_{\bar1}$.

*Proof.* If $\alpha(a)=a$ then $L^{\alpha}_a\alpha=\alpha L^{\alpha}_a$ by the fourth relation, so $L^{\alpha}_a$ preserves the eigenspaces of $\alpha$. Write $m=m_0+m_1$; then $a\alpha(m)=a m_0-a m_1$, and the equation $a\alpha(m)=m$ reads $a m_0-a m_1=m_0+m_1$, which by the directness of $M_{\bar0}\oplus M_{\bar1}$ is the pair of equations $am_0=m_0$ and $am_1=-m_1$. $\square$

### The general case

For a general $a$ the fixed set is a single $\alpha$-twisted condition, and the two equations mix.

**Proposition.** For arbitrary $a \in A$, a fixed element $m$ of $L^{\alpha}_a$ satisfies $\alpha(m)=a^{-1}m$ when $a$ acts invertibly; conversely an $m$ with $\alpha(m)=a^{-1}m$ is fixed. If in addition $\alpha(a)=a^{-1}$, such an $m$ has $\alpha^{2}(m)=\alpha(a^{-1})\alpha(m)=\alpha(a)^{-1}\alpha(m)=a\,\alpha(m)=m$, so the condition is consistent with $\alpha^{2}=\mathrm{id}$.

*Proof.* The first two clauses restate $a\alpha(m)=m$. For the last, apply $\alpha$ to $\alpha(m)=a^{-1}m$: $m=\alpha(a^{-1})\alpha(m)=\alpha(a)^{-1}\alpha(m)$, so with $\alpha(a)=a^{-1}$ one has $m=a\,\alpha(m)$, which is the fixed-point equation again. $\square$

In the antisymmetric case $\alpha(a)=a^{-1}$ the fixed set of $L^{\alpha}_a$ is the set of elements whose $\alpha$-image is $a^{-1}m$; this is the one-sided counterpart of the antisymmetric units of *Reflections as Signed Two-Sided Operators on a Bimodule over an Algebra*.

## Examples

**(a) The trivial grade involution.** If $\alpha=\mathrm{id}$ then $L^{\alpha}_a=L_a$, the composition rule is the homomorphism property, and $\operatorname{Fix}(L^{\alpha}_a)=\{m : am=m\}$.

**(b) The regular module.** For $M={}_A A$ with the grade involution of $A$, $L^{\alpha}_a(b)=a\alpha(b)$, and $L^{\alpha}_1=\alpha$ has fixed set $A_{\bar0}$, the even part of the algebra; $(L^{\alpha}_a)^{2}=L_{a\alpha(a)}$, so the signed left multiplications of order two are those with $a\alpha(a)=1$, that is, the antisymmetric units of $A$.

**(c) The matrix algebra with an even/odd grading.** For $A=M_2(k)$, $J=\operatorname{diag}(1,-1)$, $\alpha(X)=JXJ^{-1}$, and $M=A$: the even part is the diagonal matrices and the odd part the off-diagonal ones. For the even element $a=\operatorname{diag}(\lambda,\mu)$ the fixed set of $L^{\alpha}_a$ is the sum of the diagonal matrices fixed by $\lambda,\mu$ and the off-diagonal matrices satisfying $am=-m$; for the odd element $a=E_{12}+E_{21}$ the equations mix the two parts, as the general proposition describes.

**(d) The quaternions.** For $A=\mathbb{H}$ with $\alpha$ the quaternion conjugation and $M=\mathbb{H}$, the even part is $\mathbb{R}$ and the odd part the pure imaginary quaternions; for $a=1$ the fixed set of $L^{\alpha}_1=\alpha$ is $\mathbb{R}$, and for a pure imaginary unit $a$ one has $\alpha(a)=-a=a^{-1}$, so the fixed set is $\{m : \alpha(m)=-am\}$, the elements on which the two conjugations agree.

## Summary

For a graded left $A$-module $M$ over an algebra with grade involution $\alpha$, the signed left multiplication is $L^{\alpha}_a(m)=a\alpha(m)=L_a\alpha=\alpha L_{\alpha^{-1}(a)}$, and it differs from the unsigned one by the grade involution; $L^{\alpha}_1=\alpha$. Its kernel is $\alpha(\ker L_a)$, its image is $aM$, and it is invertible exactly when $a$ acts invertibly. The compositions are graded: $L_aL_b=L_{ab}$ and $L^{\alpha}_aL^{\alpha}_b=L_{a\alpha(b)}$ are unsigned, while $L^{\alpha}_aL_b=L^{\alpha}_{a\alpha(b)}$ and $L_aL^{\alpha}_b=L^{\alpha}_{ab}$ are signed; the algebra generated by the two families is the image of the crossed product $A\rtimes\mathbb{Z}/2$. The square of a signed left multiplication is $(L^{\alpha}_a)^{2}=L_{a\alpha(a)}$, so it is an involution exactly when $a\alpha(a)$ acts as the identity. The fixed set $\operatorname{Fix}(L^{\alpha}_a)=\{m : a\alpha(m)=m\}$ is the even part for $a=1$, it splits into the $1$- and $(-1)$-eigenspaces of $L_a$ on the two parts when $a$ is even, and it is the $\alpha$-twisted eigenspace with eigenvalue $a^{-1}$ when $a$ is a unit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | unital associative $R$-algebra with grade involution $\alpha$ |
| $M$ | graded left $A$-module |
| $\alpha$ | grade involution, $\alpha^{2}=\mathrm{id}$, with $\alpha(am)=\alpha(a)\alpha(m)$ |
| $M_{\bar0}, M_{\bar1}$ | even and odd parts of $M$ |
| $L_a(m)=am$ | unsigned left multiplication |
| $L^{\alpha}_a(m)=a\alpha(m)$ | signed left multiplication, $=L_a\alpha=\alpha L_{\alpha^{-1}(a)}$ |
| $L^{\alpha}_1=\alpha$ | the grade involution as a signed left multiplication |
| $L^{\alpha}_aL^{\alpha}_b=L_{a\alpha(b)}$ | composition of two signed left multiplications is unsigned |
| $(L^{\alpha}_a)^{2}=L_{a\alpha(a)}$ | reflection criterion for a signed left multiplication |
| $\operatorname{Fix}(L^{\alpha}_a)$ | $\{m : a\alpha(m)=m\}$, the fixed set |
| $\operatorname{Ann}_A(M)$ | the annihilator of $M$ |
| $A\rtimes\mathbb{Z}/2$ | the crossed product generated by $A$ and the grading |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for order-two automorphisms and the grading they define.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for order-two maps and the operators built from them.
- T. Y. Lam, *Lectures on Modules and Rings* (Springer, 1999), for the annihilator, kernels of multiplications and crossed products of modules.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for one-sided operators in a graded algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, second edition, 2001), for the parity action on a Clifford module.
