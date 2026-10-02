
# __The Adjoint of the Sandwich on a Bimodule over an Algebra__

## Introduction

The two-sided operator of a bimodule is the sandwich $S_{a,b}(x)=axb$, a left multiplication followed by a right one. This article computes its adjoint. The answer is that the adjoint acts on the parameters by the involution: $(S_{a,b})^{*}=S_{\sigma(a),\sigma(b)}$. The involution of the algebra and the involution of the module's endomorphism ring are therefore the same operation seen in two coordinates, and the self-adjoint and unitary sandwiches are read off immediately.

The article is the first of the `* Operator Theory` group of this category. It assumes the bimodule and sandwich of *The Signed Sandwich on a Bimodule over an Algebra* (in its unsigned, ungraded form), the one-sided multiplications of *Left and Right Multiplication of a Module*, the pairing and adjoint of *The Adjoint of a Module Homomorphism*, and the involution on the endomorphism ring of *The Involution on the Endomorphism Ring of a Module*. The signed version of the same computation, in which the grade involution is inserted in the middle, is *The Signed Adjoint Sandwich on a Bimodule over an Algebra*. The article stays inside Part I: no distance, norm, form with a norm, topology or limit. Throughout, $R$ is a commutative ring with $1 \neq 0$ in which $2$ is invertible, $(A,\sigma)$ is an involutive $R$-algebra, ${}_A M_A$ is an $(A,A)$-bimodule carrying a non-degenerate reflexive $\sigma$-sesquilinear pairing $\langle\cdot,\cdot\rangle$, $L_a$ and $R_b$ are the one-sided multiplications, and $S_{a,b}=L_aR_b=R_bL_a$.

## The Bimodule Pairing

### The balanced sesquilinear pairing

For the adjoints of both one-sided multiplications to exist, the pairing must be compatible with both actions.

**Definition.** A **balanced $\sigma$-sesquilinear pairing** on the bimodule ${}_A M_A$ is a $\sigma$-sesquilinear pairing that is additionally compatible with the right action:

$$
\langle am,n\rangle=\langle m,\sigma(a)n\rangle, \qquad \langle mb,n\rangle=\langle m,n\sigma(b)\rangle \qquad (a,b \in A,\ m,n \in M).
$$

The two identities are equivalent when the pairing is non-degenerate and reflexive; the first says the pairing is balanced on the left, the second on the right.

The compatibility is the bimodule form of the sesquilinear identity of *The Adjoint of a Module Homomorphism*: a pairing on a bimodule that only sees the left action would have no reason to be compatible with the right one, and the balanced condition is exactly what makes the sandwich adjoint computable.

### The adjoints of the one-sided multiplications

**Proposition.** For all $a,b \in A$, when the adjoints exist,

$$
(L_a)^{*}=L_{\sigma(a)}, \qquad (R_b)^{*}=R_{\sigma(b)} .
$$

*Proof.* The first is the computation of *The Adjoint of a Module Homomorphism*. For the second, $\langle R_b(m),n\rangle=\langle mb,n\rangle=\langle m,n\sigma(b)\rangle=\langle m,R_{\sigma(b)}(n)\rangle$, so $R_{\sigma(b)}$ represents the functional and is the adjoint by uniqueness. $\square$

Both one-sided multiplications therefore have adjoints obtained by applying the involution to the parameter, and this is the key to the sandwich.

## The Adjoint of the Sandwich

### The main computation

**Theorem.** For all $a,b \in A$,

$$
(S_{a,b})^{*}=S_{\sigma(a),\,\sigma(b)} .
$$

*Proof.* Since $S_{a,b}=L_aR_b$ and the adjoint is anti-multiplicative, $(S_{a,b})^{*}=(R_b)^{*}(L_a)^{*}=R_{\sigma(b)}L_{\sigma(a)}$. The two one-sided multiplications commute, so $R_{\sigma(b)}L_{\sigma(a)}=L_{\sigma(a)}R_{\sigma(b)}=S_{\sigma(a),\sigma(b)}$. $\square$

The parameters are transformed by $\sigma$ in place; equivalently, $(S_{a,b})^{*}=S_{\sigma(a),\sigma(b)}$ says that the diagram

$$
(a,b) \xrightarrow{\ (\sigma,\sigma)\ } (\sigma(a),\sigma(b)), \qquad S_{a,b} \xrightarrow{\ {}^{*}\ } S_{\sigma(a),\sigma(b)}
$$

commutes: applying the pair $(\sigma,\sigma)$ to the parameters and applying the operator involution to the sandwich are the same operation. This is the precise sense in which the involution of the bimodule is compatible with the involution of the algebra.

### Self-adjoint and skew-adjoint sandwiches

**Corollary.** Suppose the sandwich map $(a,b)\mapsto S_{a,b}$ is injective. Then

$$
(S_{a,b})^{*}=S_{a,b} \iff \sigma(a)=a,\ \sigma(b)=b, \qquad (S_{a,b})^{*}=-S_{a,b} \iff \sigma(a)=-a,\ \sigma(b)=-b .
$$

Thus the self-adjoint sandwiches are exactly those with both parameters symmetric, and the skew-adjoint sandwiches those with both parameters antisymmetric.

*Proof.* $S_{\sigma(a),\sigma(b)}=S_{a,b}$ is $\sigma(a)=a$ and $\sigma(b)=b$ by injectivity; the skew case is the same with a sign, and the signs of the two parameters must agree because $S_{a,b}$ is linear in each parameter. $\square$

### Unitary sandwiches

**Theorem.** If $a$ and $b$ are unitary elements of $A$, then $S_{a,b}$ is unitary:

$$
\sigma(a)a=a\sigma(a)=1 \text{ and } \sigma(b)b=b\sigma(b)=1 \implies (S_{a,b})^{*}S_{a,b}=S_{a,b}(S_{a,b})^{*}=\mathrm{id} .
$$

Conversely, for the regular bimodule with the regular pairing and an injective sandwich map, a unitary sandwich has unitary parameters.

*Proof.* By the composition law $S_{x,y}S_{u,v}=S_{xu,vy}$ of the sandwich,

$$
(S_{a,b})^{*}S_{a,b}=S_{\sigma(a)a,\,b\sigma(b)}, \qquad S_{a,b}(S_{a,b})^{*}=S_{a\sigma(a),\,\sigma(b)b},
$$

and these are $\mathrm{id}=S_{1,1}$ when $a,b$ are unitary. The converse is the same equalities read backwards. $\square$

The unitary sandwiches are the two-sided operators that preserve the pairing, in agreement with the isometry characterisation of *The Involution on the Endomorphism Ring of a Module*; the condition on the parameters is that each be unitary in the algebra, and the two sides of the sandwich are independent.

## Kernel, Image and the Paired Complement

**Corollary.** For all $a,b$, when the pairing is perfect,

$$
\ker (S_{a,b})^{*}=(\operatorname{im}S_{a,b})^{\mathrm{c}}, \qquad \operatorname{im}(S_{a,b})^{*}={}^{\mathrm{c}}(\ker S_{a,b}),
$$

and the adjoint preserves the lengths of the kernel, the image and the cokernel.

*Proof.* These are the general kernel and image identities of *The Adjoint of a Module Homomorphism*, applied to $S_{a,b}$. $\square$

The complement of the image of a sandwich is the set of $n$ killed by all $axb$, that is $(\operatorname{im}S_{a,b})^{\mathrm{c}}=\{n : \langle aMb,n\rangle=0\}$.

## The Sandwich Involution and the Parameter Involution

### The involution on the two-sided operators

**Proposition.** Let $T$ be the $R$-submodule of $E=\operatorname{End}_A(M)$ spanned by the sandwiches $S_{a,b}$. Then $T$ is stable under the involution ${}^{*}$ of $E$, and the induced map on $T$ is the map $S_{a,b}\mapsto S_{\sigma(a),\sigma(b)}$.

*Proof.* The adjoint of a sum is the sum of the adjoints, and the adjoint of a sandwich is again a sandwich by the theorem; hence $T$ is stable. $\square$

So the sandwich span is not merely a submodule of $E$ but an **involutive subalgebra** when it is closed under products: it contains the identity and the involution. In the case of the regular bimodule it is all of $E$, and the involution it carries is $\sigma$.

### Compatibility with the representation

**Proposition.** The map $A\otimes_R A^{\mathrm{op}}\to E$, $a\otimes b\mapsto S_{a,b}$ of *Left and Right Multiplication of a Module*, is compatible with the involutions: the involution $\sigma\otimes\sigma$ on the source and the involution ${}^{*}$ on the target satisfy

$$
(a\otimes b)^{*} \longmapsto (S_{a,b})^{*}=S_{\sigma(a),\sigma(b)} .
$$

*Proof.* Immediate from the theorem and the definition of the map. $\square$

Consequently the image of the algebra of two-sided operators is an involutive quotient of $A\otimes_RA^{\mathrm{op}}$ with the involution $\sigma\otimes\sigma$; the kernel of the map is an involutive ideal.

## Degenerate Cases

### A pairing that is not balanced

**Proposition.** If the pairing is compatible with the left action but not with the right, then $(L_a)^{*}=L_{\sigma(a)}$ but $R_b$ need not have an adjoint of the form $R_{\sigma(b)}$; the formula $(S_{a,b})^{*}=S_{\sigma(a),\sigma(b)}$ may fail, and the adjoint of $S_{a,b}$, when it exists, is an operator that is not a sandwich.

*Proof.* The right-adjoint computation used the balanced identity $\langle mb,n\rangle=\langle m,n\sigma(b)\rangle$; without it the functional $n\mapsto\langle mb,n\rangle$ need not be represented by a right multiplication. $\square$

### A non-faithful module

**Proposition.** If the sandwich map is not injective — for instance when the bimodule is not faithful and $S_{a,b}=S_{a',b'}$ for distinct parameters — then the self-adjointness and unitarity criteria are criteria on the operators, not on the parameters: the parameters of a self-adjoint sandwich are determined only up to the kernel of the sandwich map.

*Proof.* $S_{a,b}$ depends only on the image of $(a,b)$ in the quotient by the kernel, and the adjoint depends only on the operator, so the criteria lift to the quotient. $\square$

### The degenerate pairing of the trivial module

**Proposition.** If $M=0$ then every sandwich is $0$, the pairing is vacuous, and the involution on $E=0$ is the identity: the construction degenerates and every statement above is void.

*Proof.* Immediate. $\square$

## Examples

**(a) The regular bimodule.** For $M={}_A A_A$ with the balanced pairing $\langle m,n\rangle=\sigma(m)n$, the adjoint of $S_{a,b}$ is $S_{\sigma(a),\sigma(b)}$; the sandwich span is all of $E\cong A^{\mathrm{op}}$ when $A$ is a division ring, and the involution is $\sigma$.

**(b) Matrix algebras.** For $A=M_n(\mathbb{C})$ with $\sigma$ the conjugate transpose and $M=A$ the regular bimodule, $S_{A,B}(X)=AXB$ and $(S_{A,B})^{*}=S_{A^{*},B^{*}}$ with $A^{*}=\overline{A}^{\mathsf{T}}$; self-adjoint sandwiches are those with $A,B$ hermitian.

**(c) The group algebra of a finite group.** For $A=R[G]$ with $\sigma(g)=g^{-1}$ extended $R$-linearly, the sandwich by group elements is $S_{g,h}(x)=gxh^{-1}$; the adjoint is $S_{g^{-1},h}$: the inverse in the group plays the role of $\sigma$ on the parameters.

**(d) A pairing that is not balanced.** For $M=A$ with the pairing $\langle m,n\rangle=\tau(m)n$ for a linear functional $\tau$ that is not $\sigma$-stable, the right action is not adjointable by right multiplication and the theorem fails.

## Summary

On an $(A,A)$-bimodule with a non-degenerate reflexive balanced $\sigma$-sesquilinear pairing, the adjoints of the one-sided multiplications are $(L_a)^{*}=L_{\sigma(a)}$ and $(R_b)^{*}=R_{\sigma(b)}$, and the adjoint of the sandwich is $(S_{a,b})^{*}=S_{\sigma(a),\sigma(b)}$. The sandwich parameters are transformed by the involution of the algebra, and the operator involution of the endomorphism ring is the same operation in operator coordinates; the span of the sandwiches is an involutive submodule of $E$, and the map $A\otimes_RA^{\mathrm{op}}\to E$ is compatible with $\sigma\otimes\sigma$. The self-adjoint sandwiches are those with both parameters symmetric, the skew-adjoint those with both parameters antisymmetric, and the unitary sandwiches are the isometries; they are exactly the sandwiches with unitary parameters when the sandwich map is injective. The general kernel, image and length statements for the adjoint apply, so $\ker(S_{a,b})^{*}=(\operatorname{im}S_{a,b})^{\mathrm{c}}$ and the lengths of the kernel, image and cokernel are preserved. The construction fails when the pairing is not balanced on the right and degenerates when the module is not faithful or is zero. The signed version, with the grade involution in the middle, is *The Signed Adjoint Sandwich on a Bimodule over an Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $(A,\sigma)$ | base ring, involutive $R$-algebra |
| ${}_A M_A$ | $(A,A)$-bimodule with balanced σ-sesquilinear pairing |
| $\langle\cdot,\cdot\rangle$ | the pairing, $\langle am,n\rangle=\langle m,\sigma(a)n\rangle$ and $\langle mb,n\rangle=\langle m,n\sigma(b)\rangle$ |
| $L_a$, $R_b$ | left and right multiplications |
| $S_{a,b}=L_aR_b$ | the sandwich, $S_{a,b}(x)=axb$ |
| $S_{x,y}S_{u,v}=S_{xu,vy}$ | composition of sandwiches |
| $(S_{a,b})^{*}=S_{\sigma(a),\sigma(b)}$ | the adjoint of the sandwich |
| $\operatorname{im}(S_{a,b})^{\mathrm{c}}$ | paired complement of the image |
| $A\otimes_RA^{\mathrm{op}}\to E$ | the sandwich representation, compatible with $\sigma\otimes\sigma$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for bimodules, sesquilinear forms and adjoints.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for bimodules and the adjoint of a two-sided multiplication.
- Israel N. Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for involutions and the balanced forms they act on.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for hermitian forms over a bimodule and the operators they adjoint.
- T. Y. Lam, *Lectures on Modules and Rings* (Springer, 1999), for two-sided multiplications, their kernels and their adjoints.
