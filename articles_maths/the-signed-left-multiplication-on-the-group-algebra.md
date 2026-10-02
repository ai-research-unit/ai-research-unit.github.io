
# __The Signed Left Multiplication on the Group Algebra__

## Introduction

The one-sided operators of the group algebra are the left and right convolutions and their mirrors, and the grade involution twists one of them: the **signed left multiplication** is the operator $f\mapsto a*\alpha(f)$, the composite of the left convolution by $a$ with the twist. It is a bounded operator, invertible when $a$ is a unit, but it is not an algebra automorphism and it is not a right or left multiplication; the family it forms is a coset of the left convolutions, its products with the unsigned left convolutions are unsigned, and the elements it fixes are the kernel of an unsigned left convolution. This article defines the operator, computes its laws, its relation to the unsigned left multiplication, its invertibility and its square, and describes the elements it fixes.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the algebra $L^1(G)$ and its norm from *The Convolution Algebra $L^1(G)$*; the convolution operators and their composition laws from *Convolution on a Group* and *The Group Algebra as an Algebra of Operators*; the grade involution $\alpha$, the operator $\mathrm{A}f = \alpha(f)$, the signed sandwich and its composition laws from *The Signed Sandwich on the Group Algebra*; the abstract signed left multiplication, its relation to the unsigned one and the elements it fixes from *The Signed Left Multiplication on a Group* (Part I) and *The Signed Left Multiplication on a Topological Group* (Part II); and the bounded operators, the operator norm and the strong topology from *Operator Algebras*. The reflections are *Reflections as Signed Two-Sided Operators on the Group Algebra*, immediately preceding; the adjoint of this operator is *The Signed Adjoint of the Left Multiplication on the Group Algebra*, in the `- * Operator Theory` group of this category; the measure algebra is *The Involution on the Measure Algebra*, later. No adjoint is used here, and nothing Fourier-analytic occurs.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$ and identity $e$; $\mathcal{A} = L^1(G)$ is the group algebra with convolution $f*g$, norm $\|f\|_1$ and unit group $\mathcal{A}^\times$; $\alpha$ is a continuous involutive automorphism, $\mathrm{A}f = \alpha(f)$ with $\mathrm{A}^2 = \mathrm{id}$; and the **signed left multiplication** by $a$ and the **signed right multiplication** by $b$ are

$$
\Lambda_a = L_a\,\mathrm{A}, \quad \Lambda_a(f) = a*\alpha(f); \qquad \Lambda^{\mathrm R}_b = \mathrm{A}\,R_b, \quad \Lambda^{\mathrm R}_b(f) = \alpha(f)*b .
$$

The unsigned left multiplication is $L_a(f) = a*f$. The set of signed left multiplications is $\Lambda(\mathcal{A}) = \{\Lambda_a : a \in \mathcal{A}\}$.

## The Signed Left Multiplication

**Definition.** For $a \in \mathcal{A}$ the **signed left multiplication** is the operator $\Lambda_a = L_a\mathrm{A}$ on $\mathcal{A}$.

**Theorem (boundedness and the norm).** $\Lambda_a$ is a bounded linear operator with

$$
\|\Lambda_a\| \leq \|a\|_1\,\|\alpha\| ,
$$

and $\|\Lambda_a\| = \|a\|_1$ when $\alpha$ is isometric, in particular for the sign character and for a group automorphism of a unimodular group. The map $a\mapsto\Lambda_a$ is linear and Lipschitz, $\|\Lambda_a - \Lambda_{a'}\|\leq\|a-a'\|_1\|\alpha\|$.

**Proof.** $\Lambda_a$ is the composite of the bounded operators $L_a$ and $\mathrm{A}$, so it is bounded with norm at most the product, and $\|L_a\| = \|a\|_1$; the isometric case is $\|\mathrm{A}\| = 1$. The Lipschitz statement is linearity together with the bound. $\square$

**Proposition (it is not an algebra homomorphism).** If $\alpha\neq\mathrm{id}$ then $\Lambda_a$ is not an algebra automorphism of $\mathcal{A}$, and it is not a left convolution; it preserves the product only in the degenerate cases $\alpha = \mathrm{id}$ or $a = 0$.

**Proof.** $\Lambda_a(f*g) = a*\alpha(f)*\alpha(g)$ and $\Lambda_a(f)*\Lambda_a(g) = a*\alpha(f)*a*\alpha(g)$; these agree for all $f, g$ exactly when $a = 0$ or $\alpha = \mathrm{id}$. Similarly $\Lambda_a = L_b$ would give $\mathrm{A} = L_{a^{-1}*b}$ when $a$ is a unit, and a left convolution is not the automorphism $\mathrm{A}$ unless $\mathrm{A} = \mathrm{id}$. $\square$

**Remark (an affine operator).** The signed left multiplication is an **affine** operator on the algebra: it is a bounded linear map that permutes the algebra without preserving its multiplication, exactly as a reflection does. Its study belongs with the operators that act on $\mathcal{A}$ as a Banach space rather than as an algebra, and the only algebraic structure it respects is the grading carried by $\mathrm{A}$.

## Composition and the Generated Family

**Proposition (the composition laws).** For all $a, b \in \mathcal{A}$,

$$
\Lambda_a\,\Lambda_b = L_{a*\alpha(b)}, \qquad L_a\,\Lambda_b = \Lambda_{a*b}, \qquad \Lambda_a\,L_b = \Lambda_{a*\alpha(b)} .
$$

Hence a product of two signed left multiplications is an unsigned left convolution, a product of an unsigned and a signed left multiplication is signed, and the sign of a product is the product of the signs.

**Proof.** $\Lambda_a\Lambda_b(f) = a*\alpha(b*\alpha(f)) = a*\alpha(b)*\alpha^2(f) = a*\alpha(b)*f = L_{a*\alpha(b)}(f)$; the second and third are the same computation with the appropriate factor unsigned, using $\alpha(f*b) = \alpha(f)*\alpha(b)$. $\square$

**Corollary (the coset and the generated group).** The signed left multiplications form the coset

$$
\Lambda(\mathcal{A}) = L(\mathcal{A})\,\mathrm{A} = \mathrm{A}\,L(\mathcal{A}),
$$

and the subgroup of $B(\mathcal{A})^\times$ generated by the invertible left convolutions and $\mathrm{A}$ is $L(\mathcal{A})^\times\sqcup L(\mathcal{A})^\times\mathrm{A}$, a subgroup of index at most two over $L(\mathcal{A})^\times$.

**Proof.** $\Lambda_a = L_a\mathrm{A}$ gives the coset, and $\mathrm{A}L_b\mathrm{A} = L_{\alpha(b)}$ gives the other description; the product of any word in the generators is an invertible left convolution or an invertible signed left multiplication, so the generated subgroup is the union, and the product law $\Lambda_a\Lambda_b = L_{a*\alpha(b)}$ gives the parity. $\square$

**Proposition (the coset is trivial exactly when the twist is).** Suppose $\mathcal{A}$ is unital, equivalently $G$ is discrete. Then $\mathrm{A}\in L(\mathcal{A})$ if and only if $\alpha = \mathrm{id}$, and consequently

$$
\Lambda(\mathcal{A}) = L(\mathcal{A}) \quad\Longleftrightarrow\quad \alpha = \mathrm{id} ;
$$

for $\alpha\neq\mathrm{id}$ the signed left multiplications are not left convolutions and the two families are disjoint.

**Proof.** If $\mathrm{A} = L_b$ then $\alpha(1) = \mathrm{A}(1) = L_b(1) = b$, and $\alpha(1) = 1$, so $b = 1$ and $\mathrm{A} = L_1 = \mathrm{id}$; the converse is the definition $\Lambda_a = L_a$ when $\alpha = \mathrm{id}$. Since $\Lambda(\mathcal{A}) = L(\mathcal{A})\mathrm{A}$ and $\mathrm{A}$ is its own inverse, $\Lambda(\mathcal{A}) = L(\mathcal{A})$ if and only if $\mathrm{A}\in L(\mathcal{A})$, giving the equivalence; the disjointness follows because the two families are the two cosets of $L(\mathcal{A})$ in the group they generate, and distinct cosets are disjoint. For a non-unital algebra the statement is read in the unitisation $\mathcal{A}^\sharp$. $\square$

## The Elements it Fixes

**Definition.** The **fixed set** of $\Lambda_a$ is

$$
\operatorname{Fix}_L(a) = \{f \in \mathcal{A} : a*\alpha(f) = f\} = \ker(\Lambda_a - \mathrm{id}) .
$$

**Theorem (the fixed set is closed and is an eigenspace of a left convolution).** $\operatorname{Fix}_L(a)$ is a closed linear subspace of $\mathcal{A}$, and

$$
\operatorname{Fix}_L(a) = \ker\bigl(L_{a*\alpha(a)} - \mathrm{id}\bigr),
$$

the $1$-eigenspace of the unsigned left convolution by $a*\alpha(a)$; it is nontrivial exactly when $1$ is an eigenvalue of $L_{a*\alpha(a)}$, and it contains $0$ but need not be a subalgebra.

**Proof.** The fixed set is the kernel of the bounded operator $\Lambda_a - \mathrm{id}$, hence closed and linear. For the identification, $f = a*\alpha(f)$ gives on applying $\alpha$ that $\alpha(f) = \alpha(a)*f$, and substituting back $f = a*\alpha(a)*f = L_{a*\alpha(a)}(f)$; conversely $L_{a*\alpha(a)}(f) = f$ gives $a*\alpha(f) = a*\alpha(a)*f = f$ after applying the same substitution, so the two kernels coincide. The fixed set is a subspace and not a subalgebra, since the product of two fixed elements is fixed only when $\alpha = \mathrm{id}$. $\square$

**Example (the inversion and the square roots).** Let $G$ be abelian and let $\alpha = \alpha_\iota$ be induced by the inversion, $\alpha(f)(x) = f(x^{-1})$ for the unimodular group $G$. On a discrete $G$ and $a = \delta_k$,

$$
\Lambda_{\delta_k}(\delta_g) = \delta_k*\delta_{g^{-1}} = \delta_{kg^{-1}},
$$

so $\operatorname{Fix}_L(\delta_k)$ is the linear span of the square roots of $k$: for $G = \mathbb{R}$ additive and $k$ arbitrary it is one-dimensional, spanned by $\delta_{k/2}$; for $G = \mathbb{Z}$ with $k$ odd it is $\{0\}$, since $k$ has no square root; on a divisible abelian group where every element has two square roots it is two-dimensional. This is the group-algebra form of the square-root example of *The Signed Left Multiplication on a Topological Group*.

**Example (the trivial grade involution).** If $\alpha = \mathrm{id}$ then $\Lambda_a = L_a$ and $\operatorname{Fix}_L(a) = \ker(L_a - \mathrm{id})$: the signed operator is the unsigned one, its fixed set is the $1$-eigenspace of left convolution by $a$, and the family is not a new one. When $a$ is a unit different from $1$ this kernel is $\{0\}$.

## Invertibility and the Square

**Theorem (invertibility).** The signed left multiplication $\Lambda_a$ is invertible exactly when $a$ is a unit, and then

$$
\Lambda_a^{-1} = \mathrm{A}\,L_{a^{-1}} = \Lambda_{\alpha(a)^{-1}} ,
$$

that is $\Lambda_a^{-1}(g) = \alpha(a^{-1}*g) = \alpha(a)^{-1}*\alpha(g)$; the inverse of a signed left multiplication is again a signed left multiplication, and the invertible signed left multiplications form a coset of the group of invertible left convolutions.

**Proof.** $\Lambda_a = L_a\mathrm{A}$ is invertible exactly when $L_a$ is, that is exactly when $a$ is a unit, and then $\Lambda_a^{-1} = \mathrm{A}^{-1}L_{a^{-1}} = \mathrm{A}L_{a^{-1}}$. For the explicit form, $\Lambda_a^{-1}(g) = \alpha(a^{-1}*g) = \alpha(a)^{-1}*\alpha(g) = \Lambda_{\alpha(a)^{-1}}(g)$, using that $\alpha$ is multiplicative and $\alpha(a^{-1}) = \alpha(a)^{-1}$. $\square$

**Proposition (the square and the involution case).** The square of the signed left multiplication is the unsigned left convolution

$$
\Lambda_a^2 = L_{a*\alpha(a)},
$$

so $\Lambda_a$ is an involution of the Banach space $\mathcal{A}$ if and only if $a*\alpha(a) = 1$, equivalently $\alpha(a) = a^{-1}$ when $a$ is a unit; the set of such units is the **inverted set** $I(\alpha) = \{u\in\mathcal{A}^\times : \alpha(u) = u^{-1}\}$, on which the associated involution of the group agrees with the grade involution.

**Proof.** $\Lambda_a^2 = L_a\mathrm{A}L_a\mathrm{A} = L_aL_{\alpha(a)}\mathrm{A}^2 = L_{a*\alpha(a)}$ by the intertwining $\mathrm{A}L_a = L_{\alpha(a)}\mathrm{A}$; a left convolution $L_c$ is the identity exactly when $c = 1$ (for $\mathcal{A}$ unital) or, in general, when $c$ is the identity of the unitisation. The identification $a*\alpha(a) = 1\iff\alpha(a) = a^{-1}$ for a unit $a$ is immediate. $\square$

**Remark (relation to the reflections).** The one-sided operator is the specialisation of the signed sandwich in which one factor is the identity, $\Lambda_a = S_{a,1} = \Sigma^\alpha_{a,1}$ when $\mathcal{A}$ is unital, and more generally $\Sigma^\alpha_{a,b} = \Lambda_aR_{\alpha(b)}$; the signed left multiplication is thus the one-sided member of the two-sided family of the category, and the reflections are the members whose two factors are inverse to each other. The carrier condition of the reflection, $u*\alpha(u)\in Z(\mathcal{A})$, is the centrality of the square factor, and it is weaker than the involution condition $a*\alpha(a) = 1$ of the present section; the two coincide when the only central element of the form $a*\alpha(a)$ arising is $1$.

## Summary

The signed left multiplication on the group algebra is $\Lambda_a(f) = a*\alpha(f) = L_a\mathrm{A}$, a bounded operator with $\|\Lambda_a\|\leq\|a\|_1\|\alpha\|$, equal to $\|a\|_1$ when $\alpha$ is isometric; it is an affine operator, not an algebra automorphism and not a left convolution unless $\alpha = \mathrm{id}$. Its composition laws are $\Lambda_a\Lambda_b = L_{a*\alpha(b)}$, $L_a\Lambda_b = \Lambda_{a*b}$ and $\Lambda_aL_b = \Lambda_{a*\alpha(b)}$, so the signed left multiplications form the coset $\Lambda(\mathcal{A}) = L(\mathcal{A})\mathrm{A} = \mathrm{A}L(\mathcal{A})$, a product of two of them is unsigned, and the generated group is $L(\mathcal{A})^\times\sqcup L(\mathcal{A})^\times\mathrm{A}$; the signed family is disjoint from the unsigned one when $\alpha\neq\mathrm{id}$. The operator is invertible exactly when $a$ is a unit, with $\Lambda_a^{-1} = \mathrm{A}L_{a^{-1}} = \Lambda_{\alpha(a)^{-1}}$, an inverse that is again signed; its square is $\Lambda_a^2 = L_{a*\alpha(a)}$, so it is an involution exactly for the units of the inverted set $I(\alpha)$, $\alpha(a) = a^{-1}$. The fixed set $\operatorname{Fix}_L(a)$ is the closed kernel of $\Lambda_a - \mathrm{id}$, equal to the $1$-eigenspace $\ker(L_{a*\alpha(a)} - \mathrm{id})$ of an unsigned left convolution; on an abelian group with the inversion as twist it is the span of the square roots of the translating element, and it may be $\{0\}$. The signed left multiplication is the one-sided specialisation of the signed sandwich, and its adjoint is *The Signed Adjoint of the Left Multiplication on the Group Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{A} = L^1(G)$, $\|f\|_1$ | The group algebra and its norm |
| $\alpha$, $\mathrm{A}f = \alpha(f)$ | Grade involution and the implementing operator |
| $\Lambda_a = L_a\mathrm{A}$, $\Lambda_a(f) = a*\alpha(f)$ | The signed left multiplication |
| $\Lambda^{\mathrm R}_b(f) = \alpha(f)*b$ | The signed right multiplication |
| $\|\Lambda_a\| \leq \|a\|_1\|\alpha\|$ | The norm bound; equality when $\alpha$ is isometric |
| $\Lambda_a\Lambda_b = L_{a*\alpha(b)}$ | Product of two signed left multiplications is unsigned |
| $\Lambda(\mathcal{A}) = L(\mathcal{A})\mathrm{A}$ | The signed left multiplications as a coset |
| $\operatorname{Fix}_L(a) = \ker(\Lambda_a - \mathrm{id}) = \ker(L_{a*\alpha(a)} - \mathrm{id})$ | The fixed set, closed |
| $\Lambda_a^{-1} = \Lambda_{\alpha(a)^{-1}}$ | The inverse, invertible iff $a$ is a unit |
| $\Lambda_a^2 = L_{a*\alpha(a)}$ | The square |
| $I(\alpha) = \{u\in\mathcal{A}^\times : \alpha(u) = u^{-1}\}$ | The inverted set, on which $\Lambda_a$ is an involution |

## Further Reading

- Lev S. Pontryagin, *Topological Groups* (Gordon and Breach, second edition, 1966), for the translation operators, the homeomorphism group and the continuous automorphisms.
- Karl H. Hofmann and Sidney A. Morris, *The Structure of Compact Groups* (De Gruyter, third edition, 2013), for operator families generated by translations and a fixed automorphism of a compact group.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutive automorphisms, their fixed and inverted elements and the affine operators they define.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the one-sided and two-sided signed operators and the reflections they realise.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, second edition, 1979), for convolution on a group algebra and the left and right multiplications.
