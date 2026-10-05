
# __The Signed Left Multiplication on an Involutive Banach Algebra__

## Introduction

The left multiplication $L_a(x) = ax$ is the operator by which an algebra acts on itself, and when the algebra carries a grade involution $\alpha$ the action can be twisted by the grading, giving the **signed left multiplication**

$$
\ell_a(x) = a\,\alpha(x) .
$$

It is the signed sandwich with right parameter $1$, $\ell_a = S_{a,1}$, and it is the model of a graded module action: a graded algebra acts on itself through $\ell_a$, and a graded module is acted on by the same operator with the argument in the module. The twist changes the action in one place, the argument, and it moves the operator into the coset $L(A)\alpha$ of the ordinary left multiplications: the product of a signed left multiplication with an unsigned one is signed, the product of two signed ones is unsigned, and the group that the two families generate together is a semidirect product of the left multiplications with the two-element group $\{\mathrm{id},\alpha\}$. This article treats the signed left multiplication on an involutive Banach algebra: it fixes the operator, proves its continuity and its bounds, computes the composition laws, identifies the fixed elements, relates the family to the unsigned left multiplications, and records the degenerate cases.

The article assumes the signed sandwich, its decomposition, its table and its inverse from *The Signed Sandwich on a Banach Algebra*; the Banach algebra, its norm, the unit group and the centre from *Topological Algebras and Banach Algebras*; the bounded operators, the operator norm and the one-sided multiplications from *Operators on a Banach Algebra*; the grade involution and the grading from *Involutive Topological Bilinear Algebras*; and the abstract signed left multiplication from *The Signed Left Multiplication on an Algebra*. The anti-automorphism involution $\sigma$ is the structure of the `- * Theory` group of this category and is not used here; the graded module action is *The Graded Action on a Module over an Involutive Banach Algebra*, and the adjoint is *The Signed Adjoint of the Left Multiplication on an Involutive Banach Algebra*, later still.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$; $A$ is a unital Banach algebra over $\mathbb{K}$ with submultiplicative norm $\lVert\cdot\rVert$, centre $Z(A)$ and unit group $A^\times$; $\alpha$ is a continuous involutive automorphism, the **grade involution**, with $\alpha^2 = \mathrm{id}$ and $\lVert\alpha\rVert < +\infty$; $L_a(x) = ax$ and $R_b(x) = xb$ are the unsigned one-sided multiplications; the **signed left multiplication** is $\ell_a = L_a\alpha = S_{a,1}$, $\ell_a(x) = a\alpha(x)$; the **signed right multiplication** is $\varrho_b = \alpha R_b = S_{1,b}$, $\varrho_b(x) = \alpha(x)b$; and $A = A^+\oplus A^-$ is the grading.

## Definition and Decomposition

**Definition.** The **signed left multiplication** with parameter $a \in A$ is the operator $\ell_a(x) = a\alpha(x)$; the **signed right multiplication** is $\varrho_b(x) = \alpha(x)b$. The unsigned left and right multiplications are $L_a$ and $R_b$.

**Proposition (factorisation, boundedness and the coset).** For all $a,b \in A$,

$$
\ell_a = L_a\circ\alpha = S_{a,1} , \qquad \varrho_b = \alpha\circ R_b = S_{1,b} ,
$$

and $\ell_a$, $\varrho_b$ are bounded linear operators with

$$
\lVert\ell_a\rVert \leq \lVert a\rVert\,\lVert\alpha\rVert , \qquad \lVert\varrho_b\rVert \leq \lVert b\rVert\,\lVert\alpha\rVert ,
$$

with equality in the isometric case $\lVert\alpha\rVert = 1$. The signed left multiplications are the coset $L(A)\circ\alpha$ of the unsigned left multiplications by the twist, and $\ell_1 = \varrho_1 = \alpha$.

**Proof.** $\ell_a(x) = a\alpha(x) = L_a(\alpha(x)) = S_{a,1}(x)$ because $S_{a,1}(x) = a\alpha(x)1$; the factorisation, boundedness and norm bound follow from those of $L_a$ and $\alpha$, and $\varrho_b$ is the mirror image. The coset description is the factorisation, and $\ell_1 = L_1\alpha = \alpha$. $\square$

## Composition and the Generated Group

**Proposition (the mixed composition laws).** For all $a,b \in A$,

$$
\ell_a L_b = \ell_{a\alpha(b)} , \qquad L_a \ell_b = \ell_{ab} , \qquad \varrho_b R_a = \varrho_{\alpha(a)b} , \qquad R_a \varrho_b = \varrho_{ba} ,
$$

so the product of a signed left multiplication with an unsigned one is signed, and the signed family is stable under composition with the unsigned family on the appropriate side.

**Proof.** $\ell_a L_b(x) = \ell_a(bx) = a\alpha(bx) = a\alpha(b)\alpha(x) = \ell_{a\alpha(b)}(x)$; $L_a\ell_b(x) = a\,b\alpha(x) = \ell_{ab}(x)$; the right-handed statements are the mirror images. $\square$

**Proposition (the signed product is unsigned).** For all $a,b \in A$,

$$
\ell_a\,\ell_b = L_{a\alpha(b)} , \qquad \varrho_b\,\varrho_a = R_{\alpha(b)a} , \qquad \ell_a\,\varrho_b = T_{a,\alpha(b)} , \qquad \varrho_b\,\ell_a = T_{\alpha(a),b} ,
$$

where $T_{p,q}(x) = pxq$ is the unsigned sandwich. Hence the product of two signed one-sided multiplications is an unsigned one-sided multiplication, and the product of a signed left and a signed right multiplication is an unsigned two-sided sandwich; the signed family is not closed under composition unless $\alpha = \mathrm{id}$.

**Proof.** $\ell_a\ell_b(x) = a\alpha(b\alpha(x)) = a\alpha(b)\alpha^2(x) = a\alpha(b)x = L_{a\alpha(b)}(x)$; $\ell_a\varrho_b(x) = a\alpha(\alpha(x)b) = a\,x\,\alpha(b) = T_{a,\alpha(b)}(x)$; the other two are the mirror images. Composition of two signed operators carries no twist on the argument, so the result is unsigned; when $\alpha = \mathrm{id}$ the signed and the unsigned families coincide. $\square$

**Theorem (the generated group).** The signed left multiplications with unit parameter are invertible with

$$
\ell_u^{-1} = \ell_{\alpha(u)^{-1}} , \qquad \varrho_v^{-1} = \varrho_{\alpha(v)^{-1}} ,
$$

and they generate, together with the unsigned left multiplications, the subgroup $\{L_a : a \in A^\times\}\cdot\{\mathrm{id},\alpha\}$ of $B(A)^\times$. The grade involution normalises the left multiplications,

$$
\alpha\,L_u\,\alpha = L_{\alpha(u)} ,
$$

so the generated group is the semidirect product $L(A^\times)\rtimes\{\mathrm{id},\alpha\}$.

**Proof.** $\ell_u\ell_{\alpha(u)^{-1}}(x) = L_{u\alpha(\alpha(u)^{-1})}(x) = L_{uu^{-1}}(x) = x$ by the signed product law, and similarly on the other side, so $\ell_u$ is invertible with the stated inverse; the same computation gives the right-handed inverse. The mixed laws show that the set generated by the $L_u$ and the $\ell_u$ is $L(A^\times)\cup L(A^\times)\alpha$, which is closed under multiplication and inversion and is the semidirect product with the two-element group $\{\mathrm{id},\alpha\}$, the action being $\alpha L_u\alpha = L_{\alpha(u)}$. $\square$

## The Fixed Elements

**Proposition (the fixed set).** For $a \in A$ the fixed set of the signed left multiplication is

$$
A^{\ell_a} = \{x \in A : a\,\alpha(x) = x\} ; \qquad \text{for a unit } a, \quad A^{\ell_a} = \{x : \alpha(x) = a^{-1}x\} .
$$

It is closed, being the equalizer of the continuous maps $\ell_a$ and $\mathrm{id}$, and it contains $0$.

**Proof.** The fixed equation is $a\alpha(x) = x$; for a unit $a$ it is equivalent to $\alpha(x) = a^{-1}x$. The set is the equalizer of two continuous maps into a Hausdorff space, hence closed, and it contains $0$ because $\ell_a$ is additive. $\square$

**Corollary (the fixed subring of the grade involution).** The signed left multiplication $\ell_1 = \alpha$ has fixed set the fixed subalgebra $A^\alpha$ of the grade involution; the unsigned left multiplication $L_1 = \mathrm{id}$ fixes all of $A$; and $A^\alpha \subseteq A^{\ell_a}$ exactly when $a$ fixes $A^\alpha$ pointwise.

**Proof.** $\ell_1 = \alpha$ has fixed set $\{x : \alpha(x) = x\} = A^\alpha$; an element $x \in A^\alpha$ satisfies $a\alpha(x) = ax$, which equals $x$ for every such $x$ exactly when $a$ fixes $A^\alpha$ pointwise. $\square$

**Remark (the fixed set as an eigenspace).** When $\alpha$ is the grade involution of a splitting of $A$ and $a$ is a unit, the fixed set is an affine eigenspace of the composite automorphism $c_a\alpha$, that is $A^{\ell_a} = A^{c_{a^{-1}}\alpha}$; it is a subspace when $a$ is fixed by $\alpha$, and otherwise it is a coset of the intersection of the two fixed spaces, which is the boundary of the present article.

## The Relation to the Unsigned Left Multiplication

**Proposition (the two families differ by the grade involution).** The signed left multiplications are the composite of the unsigned left multiplications with the grade involution,

$$
\ell_a = L_a\circ\alpha , \qquad \varrho_b = \alpha\circ R_b ,
$$

so the signed family is the coset $L(A)\alpha$ and the unsigned family is the subgroup $L(A)$ of the bounded operators. A signed and an unsigned left multiplication agree on $a$ and $u$ exactly when $\alpha$ is the identity on the range of $L_a$; for a unit this forces $\alpha = \mathrm{id}$.

**Proof.** The factorisations are the proposition above; $\ell_a = L_a$ means $a\alpha(x) = ax$ for all $x$, that is $a(\alpha(x)-x) = 0$, and for a unit $a$ this is $\alpha = \mathrm{id}$. $\square$

**Theorem (degeneracy, the inner grade involution).** Suppose $\alpha = c_z$ is the inner automorphism by a unit $z$. Then every signed left multiplication is an unsigned two-sided sandwich,

$$
\ell_a = T_{az,\,z^{-1}} , \qquad \varrho_b = T_{z,\,z^{-1}b} ,
$$

and the signed family carries no information beyond the unsigned family and the inner automorphism.

**Proof.** $\ell_a(x) = a z x z^{-1} = (az)x(z^{-1}) = T_{az,z^{-1}}(x)$, and $\varrho_b(x) = zxz^{-1}b = T_{z,z^{-1}b}(x)$. $\square$

**Remark (the boundary between the two order-two maps).** The map $\alpha$ of this article is the grade involution, an **automorphism** of order two. The **involution** in the sense of an anti-automorphism, denoted $\sigma$ in this category, is the structure of the `- * Theory` group and is not used here. On a commutative algebra the two coincide, on a non-commutative one they do not.

## The Banach Reading and Examples

**Proposition (continuity and completion).** The maps $a \mapsto \ell_a$ and $b \mapsto \varrho_b$ are bounded linear maps $A \to B(A)$ of norm at most $\lVert\alpha\rVert$, and they are isometric when $\alpha$ is isometric and $A$ is unital. They extend to the completion of $A$, and they are continuous for the norm, the strong and the weak operator topologies.

**Proof.** Linearity and the norm bound are the factorisation; for isometric $\alpha$ and $\lVert a\rVert = 1$, $\lVert\ell_a\rVert = \sup_{\lVert x\rVert\leq1}\lVert a\alpha(x)\rVert \geq \lVert a\alpha(1)\rVert = \lVert a\rVert$ when $\lVert\alpha(1)\rVert = 1$, giving equality. The extension and the continuity for the operator topologies are standard. $\square$

**Example (the matrix algebra).** Let $A = M_n(\mathbb{K})$ and $\alpha(X) = DXD^{-1}$ with $D^2 = I$; the signed left multiplication is $\ell_A(X) = A(DXD^{-1}) = (AD)X D^{-1}$, an unsigned two-sided sandwich, in accordance with the degeneracy theorem since this $\alpha$ is inner.

**Example (the superalgebra).** Let $A = A^0\oplus A^1$ be a graded Banach algebra with grade involution $\alpha$. On homogeneous $x$, $\ell_a(x) = (-1)^{\lvert x\rvert}ax$: an odd element $a$ acts on the even part by $L_a$ and on the odd part by $-L_a$, and the fixed set of $\ell_a$ for $a = 1$ is the even part $A^0$.

## Summary

On an involutive Banach algebra — a Banach algebra $A$ with a continuous grade involution $\alpha$ — the signed left multiplication is $\ell_a(x) = a\alpha(x) = L_a\alpha = S_{a,1}$, bounded with $\lVert\ell_a\rVert \leq \lVert a\rVert\lVert\alpha\rVert$, and the signed right multiplication is $\varrho_b = \alpha R_b$. The mixed laws $\ell_aL_b = \ell_{a\alpha(b)}$ and $L_a\ell_b = \ell_{ab}$ show that the signed left multiplications are the coset $L(A)\alpha$ of the unsigned ones, stable under composition with the unsigned family; the products $\ell_a\ell_b = L_{a\alpha(b)}$ and $\ell_a\varrho_b = T_{a,\alpha(b)}$ are unsigned, so the signed family is closed under inversion, $\ell_u^{-1} = \ell_{\alpha(u)^{-1}}$, but not under composition. The two families generate the semidirect product $L(A^\times)\rtimes\{\mathrm{id},\alpha\}$, with $\alpha L_u\alpha = L_{\alpha(u)}$. The fixed set of $\ell_a$ is the closed set $\{x : a\alpha(x) = x\}$, which is $A^\alpha$ for $a = 1$; when $\alpha$ is inner every signed left multiplication is an unsigned sandwich; and the operator $\alpha$ is the grade involution, an automorphism, distinct from the anti-automorphism involution $\sigma$ of the `- * Theory` group. The graded module action is *The Graded Action on a Module over an Involutive Banach Algebra*, and the adjoint is *The Signed Adjoint of the Left Multiplication on an Involutive Banach Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $\lVert\cdot\rVert$, $A^\times$, $Z(A)$ | Banach algebra, norm, units, centre |
| $\alpha$, $\lVert\alpha\rVert$ | Continuous grade involution (involutive automorphism) |
| $L_a$, $R_b$ | Unsigned left and right multiplications |
| $\ell_a = L_a\alpha = S_{a,1}$ | Signed left multiplication, $\ell_a(x)=a\alpha(x)$ |
| $\varrho_b = \alpha R_b = S_{1,b}$ | Signed right multiplication, $\varrho_b(x)=\alpha(x)b$ |
| $\ell_aL_b=\ell_{a\alpha(b)}$, $L_a\ell_b=\ell_{ab}$ | Mixed laws |
| $\ell_a\ell_b=L_{a\alpha(b)}$, $\ell_a\varrho_b=T_{a,\alpha(b)}$ | Signed products are unsigned |
| $\ell_u^{-1}=\ell_{\alpha(u)^{-1}}$ | Inverse, for $u$ a unit |
| $A^{\ell_a}=\{x:a\alpha(x)=x\}$ | Fixed set, closed |
| $\alpha L_u\alpha=L_{\alpha(u)}$ | Normalisation; group $L(A^\times)\rtimes\{\mathrm{id},\alpha\}$ |
| $\alpha=c_z\Rightarrow\ell_a=T_{az,z^{-1}}$ | Degeneracy when $\alpha$ is inner |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the left regular representation, the graded algebras and the operators of a grading.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the left and right multiplications and the bounded operators of a Banach algebra.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume I* (Cambridge University Press, 1994), for the graded Banach algebras and the automatic continuity of the automorphisms.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the graded modules and the sign rule of a grading.
- Béla Bollobás, *Linear Analysis* (Cambridge University Press, second edition, 1999), for the operator topologies and the completeness of the operator algebra.
