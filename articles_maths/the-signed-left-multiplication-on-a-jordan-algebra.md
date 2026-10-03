# __The Signed Left Multiplication on a Jordan Algebra__

## Introduction

The one-sided multiplication of a Jordan algebra is the operator $L_a(x) = a \bullet x$ of *The Left and Right Multiplication Operators on a Jordan Algebra*; on a special Jordan algebra $J = A^+$ it is the symmetrisation $\tfrac12(\ell_a+\rho_a)$ of the two associative one-sided multiplications $\ell_a(x) = ax$ and $\rho_a(x) = xa$ of the ambient algebra $A$. When $A$ carries a grade involution $\alpha$, each of the associative one-sided multiplications admits a **signed** version, in which the argument is replaced by $\alpha(x)$: the **signed left multiplication** is

$$
\ell^{\alpha}_a : J \to J, \qquad \ell^{\alpha}_a(x) = a\,\alpha(x) ,
$$

and the signed right multiplication is $\rho^{\alpha}_a(x) = \alpha(x)\,a$. The signed one-sided actions combine with the unsigned ones to give the signed sandwich of *The Signed Sandwich on a Jordan Algebra*, $S^{\alpha}_{a,b} = \rho_b\ell^{\alpha}_a = \ell_a\rho^{\alpha}_b$, a product of one unsigned and one signed one-sided action.

The article defines the signed one-sided actions on the underlying module of a special graded Jordan algebra, relates them to the unsigned ones by $\ell^{\alpha}_a = \ell_a\circ\alpha$ and $\rho^{\alpha}_a = \rho_a\circ\alpha$, and records that the signed sandwich is their product with an **unsigned** partner, $S^{\alpha}_{a,b} = \rho_b\ell^{\alpha}_a = \ell_a\rho^{\alpha}_b$, and determines their **homogeneity**: the signed left multiplication by $a$ shifts the parity by the parity of $a$, so it is a graded operator of degree $|a|$ and not a degree-preserving one; this is the sign rule the grading imposes on the one-sided layer, and it is the precise difference from the unsigned left multiplication, which preserves the degree. The article then computes the **elements fixed** by the signed left multiplication: on even elements the equation is $ax = x$, on odd elements it is $ax = -x$, so the fixed space is the even part of the eigenvalue-one space of $\ell_a$ together with the odd part of its eigenvalue-minus-one space; in particular the signed left multiplication by the unit $1$ fixes exactly the even part $A_{\bar 0}$. The symmetrisation of the two signed one-sided actions is the quadratic representation twisted by $\alpha$, $\tfrac12(\ell^{\alpha}_a\rho^{\alpha}_a + \rho^{\alpha}_a\ell^{\alpha}_a) = U_a\circ\alpha$, which is where the signed left multiplication meets the structure group.

The article assumes *The Left and Right Multiplication Operators on a Jordan Algebra* for $L_a$, $U_a$ and the quadratic representation, *Left and Right Multiplication in a Ring* for $\ell_a$ and $\rho_a$, *The Signed Sandwich on a Jordan Algebra* for the signed sandwich and the grade involution, and *Jordan Algebras* for the special algebra $A^+$. The adjoint of the signed left multiplication with respect to the pairing of the category is *The Signed Adjoint of the Left Multiplication on a Jordan Algebra*, in the `* Operator Theory` group; the `*` involution of the elements is not used here. Throughout, $A$ is an associative unital $R$-algebra, $J = A^+$ is the special Jordan algebra with the halved product, and $\alpha$ is a grade involution of $A$. No form, norm, distance or geometric reflection occurs.

## The Unsigned One-Sided Actions

### The Associative Multiplications

For $a \in A$ the **associative left multiplication** and **right multiplication** are the $R$-linear maps

$$
\ell_a : A \to A, \quad \ell_a(x) = ax , \qquad \rho_a : A \to A, \quad \rho_a(x) = xa ,
$$

the one-sided multiplications of *Left and Right Multiplication in a Ring*. They are the operators whose products are the sandwiches, $S_{a,b} = \ell_a\rho_b$, with the composition laws $\ell_a\ell_b = \ell_{ab}$ and $\rho_a\rho_b = \rho_{ba}$ of that article.

### The Jordan Left Multiplication as a Symmetrisation

The Jordan left multiplication of $J = A^+$ is

$$
L_a = \tfrac12\bigl(\ell_a + \rho_a\bigr), \qquad L_a(x) = a \bullet x = \tfrac12(ax + xa) ,
$$

as in *The Left and Right Multiplication Operators on a Jordan Algebra*. The two associative one-sided actions therefore do not separately descend to the Jordan structure; only their symmetrisation does, and this is the same phenomenon as the collapse $L_a = R_a$ of the two Jordan one-sided multiplications: the Jordan structure retains the symmetric part and discards the difference $\tfrac12(\ell_a-\rho_a) = \tfrac12\operatorname{ad}_a$.

**Proposition.** The correspondence $a \mapsto L_a = \tfrac12(\ell_a+\rho_a)$ is injective when $A$ has no nonzero element annihilating $A$ on both sides, and it is additive; the map is an $R$-linear isomorphism onto its image, and it is not multiplicative in $a$ unless $A$ is commutative.

*Proof.* Additivity is clear. If $\tfrac12(\ell_a+\rho_a) = 0$ then $ax+xa = 0$ for all $x$; multiplying by $x$ on the appropriate side or specialising to $x = 1$ gives $a = 0$ when $A$ is unital with $2$ invertible or when the two-sided annihilator is zero. The failure of multiplicativity is the failure of the associativity of $\circ$: $L_aL_b \ne L_{a\bullet b}$ unless $A$ is commutative, as in *The Left and Right Multiplication Operators on a Jordan Algebra*. $\square$

## The Signed One-Sided Actions

### Definition

**Definition.** For $a \in J$ the **signed left multiplication** and the **signed right multiplication** are the $R$-linear maps on the module $J$

$$
\ell^{\alpha}_a : J \to J, \quad \ell^{\alpha}_a(x) = a\,\alpha(x) , \qquad
\rho^{\alpha}_a : J \to J, \quad \rho^{\alpha}_a(x) = \alpha(x)\,a .
$$

They are linear in the parameter $a$ and additive in $x$, and they are the operators composing to the signed sandwich: $S^{\alpha}_{a,b} = \ell^{\alpha}_a\rho^{\alpha}_b$, since $\rho^{\alpha}_b(x) = \alpha(x)b$ and $\ell^{\alpha}_a(\alpha(x)b) = a\,\alpha(\alpha(x)b) = a\,x\,\alpha(b)$, which is $S_{a,\alpha(b)}$ and agrees with the definition $S^{\alpha}_{a,b}(x) = a\alpha(x)b$ exactly when the middle factor is read correctly, namely $S^{\alpha}_{a,b} = \ell^{\alpha}_a\circ\rho^{\alpha}_{\alpha(b)}$. This identication is recorded as a proposition below.

### Relation to the Unsigned Action

**Theorem.** For every $a \in J$,

$$
\ell^{\alpha}_a = \ell_a\circ\alpha , \qquad \rho^{\alpha}_a = \rho_a\circ\alpha ,
$$

and the signed actions are obtained from the unsigned ones by precomposition with the grade involution.

*Proof.* $\ell_a(\alpha(x)) = a\alpha(x) = \ell^{\alpha}_a(x)$; the right case is identical. $\square$

**Corollary.** The signed left multiplication is the unsigned left multiplication read at the twisted argument, and the two coincide exactly when $\alpha = \mathrm{id}$; in particular $\ell^{\alpha}_1 = \alpha$ is the grade involution itself, while $\ell_1 = \mathrm{id}$.

**Proposition (composition with the signed sandwich).** For all $a, b \in J$,

$$
S^{\alpha}_{a,b} = \rho_b\circ\ell^{\alpha}_a = \ell_a\circ\rho^{\alpha}_b ,
$$

so the signed sandwich is the product of one **unsigned** and one **signed** one-sided action, in either order; the product of two signed actions is instead $\ell^{\alpha}_a\rho^{\alpha}_b(x) = a\,x\,\alpha(b) = S_{a,\alpha(b)}(x)$, an unsigned sandwich at the twisted right parameter.

*Proof.* $\rho_b(\ell^{\alpha}_a(x)) = \rho_b(a\alpha(x)) = a\alpha(x)b = S^{\alpha}_{a,b}(x)$; the second expression is identical. For the last identity, $\rho^{\alpha}_b(x) = \alpha(x)b$ and $\ell^{\alpha}_a(\alpha(x)b) = a\alpha(\alpha(x)b) = ax\alpha(b) = S_{a,\alpha(b)}(x)$. $\square$

### Homogeneity and the Sign Rule

**Theorem (the sign rule).** Let $A = A_{\bar 0}\oplus A_{\bar 1}$ be the grading by $\alpha$ and let $a$ be homogeneous of parity $|a| \in \{0,1\}$. Then

$$
\ell^{\alpha}_a(A_{\bar i}) \subseteq A_{\overline{i+|a|}} , \qquad \rho^{\alpha}_a(A_{\bar i}) \subseteq A_{\overline{i+|a|}} ,
$$

so that the signed one-sided actions are **graded operators of degree $|a|$**: they preserve the degree when $a$ is even and exchange the even and odd parts when $a$ is odd.

*Proof.* For $x \in A_{\bar i}$ one has $\alpha(x) = (-1)^i x$, so $\ell^{\alpha}_a(x) = (-1)^i ax$, and the parity of $ax$ is $|a|+i$ because $A$ is graded. The right case is identical. $\square$

**Corollary.** The unsigned left multiplication preserves the degree, because it is the symmetrisation of the two degree-preserving actions $\ell_a$ and $\rho_a$; the signed left multiplication shifts the degree by the parity of $a$. The sign rule is the parity factor $(-1)^i$ that the twist inserts, and it is the reason the signed one-sided action cannot be an operator of the Jordan structure when $a$ is odd: a Jordan operator must preserve the degree, while $\ell^{\alpha}_a$ with $a$ odd exchanges the two parts.

## The Elements Fixed

### The Fixed Space

**Theorem.** The elements fixed by the signed left multiplication are

$$
\{x \in J : \ell^{\alpha}_a(x) = x\} = \{x \in A_{\bar 0} : ax = x\} \oplus \{x \in A_{\bar 1} : ax = -x\} ;
$$

that is, the intersection of the even part with the eigenvalue-one space of the left multiplication $\ell_a$, together with the intersection of the odd part with its eigenvalue-minus-one space.

*Proof.* Write $x = x_0 + x_1$ with $x_i \in A_{\bar i}$. Then $\ell^{\alpha}_a(x) = a\alpha(x_0) + a\alpha(x_1) = ax_0 - ax_1$, and the equation $ax_0 - ax_1 = x_0 + x_1$ decouples by parity into $ax_0 = x_0$ and $-ax_1 = x_1$. $\square$

**Corollary (the case $a = 1$).** The signed left multiplication by the unit is the grade involution itself, $\ell^{\alpha}_1 = \alpha$, and its fixed space is exactly the even part $A_{\bar 0}$, which is the subalgebra of $J$; the odd part $A_{\bar 1}$ is the eigenvalue-minus-one space.

**Corollary (the case of a central unit).** If $a$ is a unit with $a^2 = 1$ or, more generally, if the equation $a\alpha(x) = x$ decouples as $ax = x$ on the even part and $ax = -x$ on the odd part, the fixed space is the kernel of $\ell_a - \mathrm{id}$ on $A_{\bar 0}$ together with the kernel of $\ell_a + \mathrm{id}$ on $A_{\bar 1}$. The case $a = 1$ gives the even part.

**Example.** Let $A = k[x]/(x^2)$, $\alpha = \mathrm{id}$ and $a = x$, so that $\ell^{\alpha}_x = \ell_x$ and the fixed elements satisfy $xy = y$, that is $(x-1)y = 0$; since $x-1$ is a unit of $A$, the fixed space is $0$. For the coordinatewise algebra $A = k^n$ with the involution negating the last coordinate and $a = 1$, the fixed space is the span of the first $n-1$ standard idempotents, the even part.

### The Symmetrisation and the Structure Group

**Proposition.** For $a \in J$,

$$
\ell_a\circ\rho^{\alpha}_a = \rho_a\circ\ell^{\alpha}_a = U_a\circ\alpha ,
$$

where $U_a$ is the quadratic representation of *The Left and Right Multiplication Operators on a Jordan Algebra* and $U_a\circ\alpha$ is the symmetrised signed sandwich of *The Signed Sandwich on a Jordan Algebra* with equal parameters; the product is that of one **unsigned** and one **signed** one-sided action.

*Proof.* $\ell_a(\rho^{\alpha}_a(x)) = \ell_a(\alpha(x)a) = a\alpha(x)a = U_a(\alpha(x))$, and $\rho_a(\ell^{\alpha}_a(x)) = \rho_a(a\alpha(x)) = a\alpha(x)a$, the same operator. Reading $U_a(\alpha(x))$ as $(U_a\circ\alpha)(x)$ gives the statement. $\square$

**Corollary.** The product of an unsigned and a signed one-sided action is the twist of the quadratic representation, which lies in the multiplication algebra; the signed one-sided actions themselves do not. The signed left multiplication is therefore the one-parameter operator from which the tied two-parameter operators of the group $\operatorname{Mult}(J)$ are rebuilt, and its adjoint — the object of *The Signed Adjoint of the Left Multiplication on a Jordan Algebra* — is the operator that carries the pairing through the action.

## Summary

On a special graded Jordan algebra $J = A^+$ the **signed left multiplication** is $\ell^{\alpha}_a(x) = a\alpha(x)$ and the signed right multiplication is $\rho^{\alpha}_a(x) = \alpha(x)a$; they are the unsigned associative multiplications precomposed with the grade involution, $\ell^{\alpha}_a = \ell_a\circ\alpha$, $\rho^{\alpha}_a = \rho_a\circ\alpha$, and they compose to the signed sandwich. Their **sign rule** is the parity shift: $\ell^{\alpha}_a$ maps the graded part $i$ to the part $\overline{i+|a|}$, so it preserves the degree for even $a$ and exchanges the parts for odd $a$, whereas the unsigned Jordan left multiplication $L_a = \tfrac12(\ell_a+\rho_a)$ always preserves the degree. The **fixed elements** of $\ell^{\alpha}_a$ are the even solutions of $ax=x$ together with the odd solutions of $ax=-x$; for $a=1$ the signed left multiplication is the grade involution and the fixed space is the even part $A_{\bar 0}$. The product of an unsigned and a signed one-sided action is $U_a\circ\alpha$, the twisted quadratic representation. No form, norm or geometric reflection occurs; the adjoint is deferred to the `* Operator Theory` group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J = A^+$ | Special Jordan algebra with halved product |
| $\alpha$ | Grade involution, $\alpha^2=\mathrm{id}$ |
| $A_{\bar 0}, A_{\bar 1}$ | Even and odd parts |
| $\ell_a(x) = ax$, $\rho_a(x) = xa$ | Associative one-sided multiplications |
| $L_a = \tfrac12(\ell_a+\rho_a)$ | Jordan left multiplication |
| $\ell^{\alpha}_a(x) = a\alpha(x)$ | Signed left multiplication |
| $\rho^{\alpha}_a(x) = \alpha(x)a$ | Signed right multiplication |
| $\ell^{\alpha}_a = \ell_a\circ\alpha$ | Relation to the unsigned action |
| $\ell^{\alpha}_a(A_{\bar i})\subseteq A_{\overline{i+|a|}}$ | The sign rule (degree shift) |
| $\{x : \ell^{\alpha}_a x = x\}$ | Fixed space, decoupled by parity |
| $U_a\circ\alpha = \tfrac12(\ell^{\alpha}_a\rho^{\alpha}_a+\rho^{\alpha}_a\ell^{\alpha}_a)$ | Symmetrisation |
| $S^{\alpha}_{a,b}$ | Signed sandwich (Article 7) |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the one-sided multiplications, the quadratic representation and the structure group of a Jordan algebra.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the special Jordan algebra, its one-sided actions and the structure group.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the grade involution and the graded operators built from it.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for one-sided multiplications and their symmetrisations.
- Ottmar Loos, *Symmetric Spaces I: General Theory* (Benjamin, 1969), for the graded one-sided actions and the structure group in the algebraic setting.
