# __Two-Sided Operators on the General Quaternionic Algebra of Quaternions__

## Introduction

The **two-sided operators** of the general quaternionic bilinear product $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$ of *Introduction to the General Quaternionic Algebra of Quaternions* are the products of a left and a right multiplication, with the left one carrying the conjugation of the product and the right one the plain product of the block:

$$
T_{\tilde a,\tilde b}(\tilde q) = \tilde a \star \tilde q \cdot \tilde b = \tilde a^{\natural}\tilde q\,\tilde b = L_{\tilde a^{\natural}}R_{\tilde b} .
$$

They are the elementary sandwiches of the block, and their family carries the whole operator calculus of the algebra: a composition law, an adjoint for each of the two forms of the space, and the fact — the *type* of the family — that the sandwiches span every real-linear operator of $\mathbb{H}$. The left factor is the left multiplication by the conjugated parameter, $L_{\tilde a^{\natural}}$. This article establishes those four facts and compares them with the plain algebra of the same space, where the left multiplication does not carry the conjugation and the two laws are correspondingly different. The one-sided families are *One-Sided Operators on the General Quaternionic Algebra of Quaternions*, below this article in this category, and the left family with its monoid *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, above this article in this category; the forms are *The Isotropic Structure of the General Quaternionic Algebra*, above this article in this category.

**Conventions.** The elements are $\tilde p = \sum_\mu p_\mu e_\mu$ with the conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$; the product is $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$; the two forms of the space are the plain form $\mathrm B(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q)$ of signature $(1,3)$ and the quaternionic form $N(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q^{\natural}) = \sum_\mu p_\mu q_\mu$ of signature $(4,0)$; a right multiplication is the plain one, $R_{\tilde b}(\tilde q) = \tilde q\tilde b$.

## The Family

**Definition.** For $\tilde a,\tilde b \in \mathbb{H}$ the **two-sided operator** is $T_{\tilde a,\tilde b} = L_{\tilde a^{\natural}}R_{\tilde b}$, the map $\tilde q \mapsto \tilde a^{\natural}\tilde q\tilde b$. The family is $\mathcal T = \{T_{\tilde a,\tilde b}\}$.

**Theorem (the type of the family).** The family spans the whole algebra of real-linear operators, $\operatorname{span}_\mathbb{R}\mathcal T = \operatorname{End}_\mathbb{R}(\mathbb{H})$, of real dimension sixteen; every real-linear operator of $\mathbb{H}$ is a finite real combination of two-sided operators.

*Proof.* The left multiplications span a four-dimensional subspace by *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, above this article in this category, and the right multiplications span another four-dimensional subspace; the products $L_{\tilde a^{\natural}}R_{\tilde b}$ span the product of the two subspaces, and the sandwich operators of the plain algebra are known to span $\operatorname{End}_\mathbb{R}(\mathbb{H})$, since the enveloping algebra $\mathbb{H} \otimes_\mathbb{R} \mathbb{H}^{\mathrm{op}}$ is the full matrix algebra $M_4(\mathbb{R})$. The reindexing $\tilde a \mapsto \tilde a^{\natural}$ is a bijection, so the quaternionic sandwiches are the plain ones reindexed and span the same sixteen dimensions.

**Corollary.** The four-dimensional space $\mathbb{H}$ is simple as a module over the operator algebra $\mathcal T$: the family is all of $\operatorname{End}_\mathbb{R}(\mathbb{H})$, and a full endomorphism algebra acts faithfully.

*Proof.* The theorem gives $\mathcal T = \operatorname{End}_\mathbb{R}(\mathbb{H})$, and the endomorphism algebra of a finite-dimensional space acts faithfully on it.

## Composition

**Theorem (the composition law).** For all $\tilde a,\tilde b,\tilde c,\tilde d \in \mathbb{H}$,

$$
T_{\tilde a,\tilde b}T_{\tilde c,\tilde d} = T_{\tilde c\tilde a,\,\tilde d\tilde b} .
$$

Both parameters are **reversed**, because both the first factor of the product and the second carry an order-reversing step: the first through the anti-automorphism ${}^{\natural}$ that the left multiplication contains, the second through the opposite algebra.

*Proof.* Apply the left side to $\tilde q$ and use the associativity of the plain product:
$$
T_{\tilde a,\tilde b}\bigl(T_{\tilde c,\tilde d}(\tilde q)\bigr) = \tilde a^{\natural}\bigl(\tilde c^{\natural}\tilde q\tilde d\bigr)\tilde b = \bigl(\tilde a^{\natural}\tilde c^{\natural}\bigr)\tilde q\bigl(\tilde d\tilde b\bigr) = (\tilde c\tilde a)^{\natural}\,\tilde q\,(\tilde d\tilde b),
$$
which is $T_{\tilde c\tilde a,\tilde d\tilde b}(\tilde q)$.

**Proposition (when two sandwiches agree, and the zero case).** The sandwich $L_\alpha R_\beta$ is zero exactly when $\alpha = 0$ or $\beta = 0$. For **nonzero** parameter pairs, two sandwiches agree as operators exactly when the pairs differ by a single real scalar:

$$
\alpha,\beta,\alpha',\beta' \neq 0 : \quad L_{\alpha}R_{\beta} = L_{\alpha'}R_{\beta'} \iff \alpha' = \mu\alpha \text{ and } \beta' = \mu^{-1}\beta \text{ for some } \mu \in \mathbb{R}^\times .
$$

*Proof.* The equality $L_\alpha R_\beta = 0$ says $\alpha\tilde q\beta = 0$ for every $\tilde q$; at $\tilde q = e_0$ this is $\alpha\beta = 0$, and in a division algebra a product vanishes exactly when a factor does, so $\alpha = 0$ or $\beta = 0$, and conversely. Assume now all four parameters nonzero and $\alpha\tilde q\beta = \alpha'\tilde q\beta'$ for every $\tilde q$. Multiply on the left by $\alpha^{-1}$ and put $\gamma = \alpha^{-1}\alpha'$, so that $\tilde q\beta = \gamma\tilde q\beta'$ for every $\tilde q$. At $\tilde q = e_0$ this gives $\beta = \gamma\beta'$, whence $\beta' = \gamma^{-1}\beta$; substituting back gives $(\tilde q\gamma - \gamma\tilde q)\beta' = 0$ for every $\tilde q$, and since $\beta' \neq 0$ the parameter $\gamma$ is central, that is $\gamma = \mu$ real and nonzero. Therefore $\alpha' = \alpha\gamma = \mu\alpha$ and $\beta' = \mu^{-1}\beta$. Conversely, if $\alpha' = \mu\alpha$ and $\beta' = \mu^{-1}\beta$ then $L_{\alpha'}R_{\beta'} = L_{\mu\alpha}R_{\mu^{-1}\beta} = L_\alpha R_\beta$, because the scalar is central.

**Corollary (the monoid and the kernel).** The family is a monoid under composition, with identity $T_{e_0,e_0} = \mathrm{id}$; the map $(\tilde a,\tilde b) \mapsto T_{\tilde a,\tilde b}$ is a homomorphism of monoids onto the family from the product of two opposite monoids, $(\mathbb{H}^{\mathrm{op}})^2$ with the multiplication of the parameters in both places, and its kernel — the preimage of the identity — is the one-parameter group

$$
\{(\lambda,\lambda^{-1}) : \lambda \in \mathbb{R}^\times\} \cong \mathbb{R}^\times .
$$

*Proof.* Closure is the law, and $T_{e_0,e_0}(\tilde q) = e_0^{\natural}\tilde q e_0 = \tilde q$. The homomorphism reads the law as the multiplication of the parameters with both places reversed, which is the opposite law in each place. For the kernel, $T_{\tilde a,\tilde b} = \mathrm{id}$ forces $T_{\tilde a,\tilde b}$ nonzero, hence $\tilde a \neq 0$ and $\tilde b \neq 0$; the agree-as-operators criterion applied to the pairs $(\tilde a^{\natural},\tilde b)$ and $(e_0,e_0)$ then gives $\tilde a^{\natural} = \mu e_0$ and $\tilde b = \mu^{-1}e_0$ with a single real $\mu \neq 0$, that is $\tilde a = \mu$ and $\tilde b = \mu^{-1}$ real scalars. Hence the kernel is the displayed one-parameter group. The two-element set $\{(\pm e_0,\pm e_0)\}$ is the part of it inside the integral scalars, not the whole kernel.

**Corollary (the one-parameter redundancy).** The parametrisation is not injective: $T_{\lambda\tilde a,\lambda^{-1}\tilde b} = T_{\tilde a,\tilde b}$ for every real $\lambda \neq 0$, because the scalar commutes with everything. The family is therefore a quotient of $(\mathbb{H}^{\mathrm{op}})^2$ by the diagonal scalars, and the two-sided operators of a given parameter pair are the same operator along the two one-parameter lines of the scaling. The kernel of the previous corollary is exactly the diagonal scaling line through $(e_0,e_0)$.

**Corollary (the units).** $T_{\tilde a,\tilde b}$ is invertible exactly when $\tilde a \neq 0$ and $\tilde b \neq 0$, with inverse $T_{\tilde a^{-1},\tilde b^{-1}}$.

*Proof.* By the law, $T_{\tilde a,\tilde b}T_{\tilde a^{-1},\tilde b^{-1}} = T_{\tilde a^{-1}\tilde a,\tilde b^{-1}\tilde b} = T_{e_0,e_0}$; conversely an invertible two-sided operator has a nonzero value at $e_0$ on both sides, $\tilde a^{\natural}\tilde b \neq 0$, so both parameters are nonzero. The inverses are taken in the plain algebra, where every nonzero element has one.

## The Adjoint

Each form of the space defines a transpose on the operators, and the two transposes of a sandwich are other sandwiches with the parameters conjugated and swapped.

**Theorem (the transpose for the plain form).** With respect to the plain form $\mathrm B(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q)$, the transpose of a two-sided operator is

$$
T_{\tilde a,\tilde b}^{\sim} = T_{\tilde b^{\natural},\tilde a^{\natural}} = L_{\tilde b}R_{\tilde a^{\natural}} .
$$

*Proof.* The transpose is characterised by $\mathrm B(T\tilde p,\tilde q) = \mathrm B(\tilde p,T^{\sim}\tilde q)$. For $T = T_{\tilde a,\tilde b}$,
$$
\mathrm B\bigl(T\tilde p,\tilde q\bigr) = \mathrm{Sc}\bigl(\tilde a^{\natural}\tilde p\tilde b\tilde q\bigr) = \mathrm{Sc}\bigl(\tilde p\,\tilde b\tilde q\tilde a^{\natural}\bigr) ,
$$
by the cyclic invariance of the scalar part, and the last is $\mathrm B(\tilde p, \tilde b\tilde q\tilde a^{\natural}) = \mathrm B(\tilde p, T_{\tilde b^{\natural},\tilde a^{\natural}}\tilde q)$, since $(\tilde b^{\natural})^{\natural}\tilde q\tilde a^{\natural} = \tilde b\tilde q\tilde a^{\natural}$.

**Theorem (the transpose for the quaternionic form).** With respect to the quaternionic form $N(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q^{\natural})$ of signature $(4,0)$, the transpose of a two-sided operator is

$$
T_{\tilde a,\tilde b}^{\dagger} = T_{\tilde a^{\natural},\tilde b^{\natural}} .
$$

*Proof.* The characterisation is $N(T\tilde p,\tilde q) = N(\tilde p,T^{\dagger}\tilde q)$, and
$$
N\bigl(T\tilde p,\tilde q\bigr) = \mathrm{Sc}\bigl(\tilde a^{\natural}\tilde p\tilde b\tilde q^{\natural}\bigr) = \mathrm{Sc}\bigl(\tilde p\,\tilde b\tilde q^{\natural}\tilde a^{\natural}\bigr) = \mathrm{Sc}\bigl(\tilde p\,(\tilde a\tilde q\tilde b^{\natural})^{\natural}\bigr) ,
$$
using that $(\tilde a\tilde q\tilde b^{\natural})^{\natural} = \tilde b\tilde q^{\natural}\tilde a^{\natural}$; the last is $N(\tilde p, \tilde a\tilde q\tilde b^{\natural}) = N(\tilde p, T_{\tilde a^{\natural},\tilde b^{\natural}}\tilde q)$, since $(\tilde a^{\natural})^{\natural}\tilde q\tilde b^{\natural} = \tilde a\tilde q\tilde b^{\natural}$.

**Corollary (the two transposes and the comparison).** The plain transpose swaps the two parameters and conjugates them both, $T^{\sim}_{\tilde a,\tilde b} = T_{\tilde b^{\natural},\tilde a^{\natural}}$; the quaternionic transpose keeps the two parameters in place and conjugates them both, $T^{\dagger}_{\tilde a,\tilde b} = T_{\tilde a^{\natural},\tilde b^{\natural}}$. For a nonzero sandwich, the two transposes coincide exactly when the two parameters are proportional over $\mathbb{R}$,

$$
\tilde a,\tilde b \neq 0 : \quad T^{\sim}_{\tilde a,\tilde b} = T^{\dagger}_{\tilde a,\tilde b} \iff \tilde b \in \mathbb{R}\tilde a ,
$$

which includes the diagonal case $\tilde a = \tilde b$ but is strictly wider; and a nonzero sandwich is self-transpose for the plain form exactly when the second parameter is a real multiple of the conjugate of the first,

$$
\tilde a,\tilde b \neq 0 : \quad T_{\tilde a,\tilde b} = T^{\sim}_{\tilde a,\tilde b} \iff \tilde b \in \mathbb{R}\tilde a^{\natural} .
$$

The two criteria are stated for a nonzero sandwich because the zero operators $T_{0,\tilde b}$ and $T_{\tilde a,0}$ are transposed to zero and satisfy both equalities trivially, without any proportion between the parameters.

*Proof.* The transposes are the sandwiches $T_{\tilde b^{\natural},\tilde a^{\natural}}$ and $T_{\tilde a^{\natural},\tilde b^{\natural}}$ with all four parameters nonzero for a nonzero sandwich. They agree exactly when the pairs $(\tilde b^{\natural},\tilde a^{\natural})$ and $(\tilde a^{\natural},\tilde b^{\natural})$ differ by the real scalar of the agree-as-operators criterion, that is $\tilde a^{\natural} = \mu\tilde b^{\natural}$ for some $\mu \neq 0$, which is $\tilde a = \mu\tilde b$. For the self-transpose reading, $T_{\tilde a,\tilde b} = T^{\sim}_{\tilde a,\tilde b}$ compares the pairs $(\tilde a^{\natural},\tilde b)$ and $(\tilde b^{\natural},\tilde a^{\natural})$: the criterion gives $\tilde b^{\natural} = \mu\tilde a^{\natural}$ and $\tilde a^{\natural} = \mu^{-1}\tilde b^{\natural}$, which is the single condition $\tilde b = \mu\tilde a^{\natural}$ with a real $\mu \neq 0$.

## The Comparison with the Plain Algebra

**Proposition.** The two-sided operators of the plain algebra are the sandwiches with the direct product, $T^{(0)}_{\tilde a,\tilde b}(\tilde q) = \tilde a\tilde q\tilde b$, and they satisfy the composition law $T^{(0)}_{\tilde a,\tilde b}T^{(0)}_{\tilde c,\tilde d} = T^{(0)}_{\tilde a\tilde c,\tilde d\tilde b}$, with only the second parameter reversed. The quaternionic operators are the same sandwiches with the first parameter conjugated, $T_{\tilde a,\tilde b} = T^{(0)}_{\tilde a^{\natural},\tilde b}$, and their composition law reverses both parameters.

*Proof.* The plain law is the associativity of the plain product read twice; the quaternionic law is the theorem above, and the identification with the plain family is $\tilde a^{\natural}(\tilde q\tilde b) = T^{(0)}_{\tilde a^{\natural},\tilde b}(\tilde q)$.

| | plain algebra | quaternionic algebra |
|---|---|---|
| operator | $T^{(0)}_{\tilde a,\tilde b}(\tilde q) = \tilde a\tilde q\tilde b$ | $T_{\tilde a,\tilde b}(\tilde q) = \tilde a^{\natural}\tilde q\tilde b$ |
| composition | $T^{(0)}_{\tilde a,\tilde b}T^{(0)}_{\tilde c,\tilde d} = T^{(0)}_{\tilde a\tilde c,\tilde d\tilde b}$ | $T_{\tilde a,\tilde b}T_{\tilde c,\tilde d} = T_{\tilde c\tilde a,\tilde d\tilde b}$ |
| transpose for $\mathrm B$ | $T^{(0)\sim}_{\tilde a,\tilde b} = T^{(0)}_{\tilde b,\tilde a}$ | $T^{\sim}_{\tilde a,\tilde b} = T_{\tilde b^{\natural},\tilde a^{\natural}}$ |
| transpose for $N$ | $T^{(0)\dagger}_{\tilde a,\tilde b} = T^{(0)}_{\tilde a^{\natural},\tilde b^{\natural}}$ | $T^{\dagger}_{\tilde a,\tilde b} = T_{\tilde a^{\natural},\tilde b^{\natural}}$ |
| family | all of $\operatorname{End}_\mathbb{R}(\mathbb{H})$ | all of $\operatorname{End}_\mathbb{R}(\mathbb{H})$ |

**Corollary.** The families agree as sets of operators, $T_{\tilde a,\tilde b} = T^{(0)}_{\tilde a^{\natural},\tilde b}$, and they differ in the multiplication they carry: the plain law reverses one parameter, the quaternionic law reverses two. The difference is the anti-automorphism in the first slot of the product, and it is the same difference as between the two left-multiplication monoids (*The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, above this article in this category).

## Summary

The two-sided operators of the quaternionic product are $T_{\tilde a,\tilde b}(\tilde q) = \tilde a^{\natural}\tilde q\tilde b$, the sandwiches of the conjugated left multiplication $L_{\tilde a^{\natural}}$ with the plain right multiplication $R_{\tilde b}$. They span every real-linear operator of $\mathbb{H}$; two of them agree exactly on parameter pairs differing by a real scalar, so the family is a quotient of the parameter space by that scaling. They form a monoid with identity $T_{e_0,e_0}$ and composition law $T_{\tilde a,\tilde b}T_{\tilde c,\tilde d} = T_{\tilde c\tilde a,\tilde d\tilde b}$ reversing **both** parameters, the identity being reached exactly on the one-parameter kernel $\{(\lambda,\lambda^{-1})\}$; the invertible elements are those with both parameters nonzero, with inverse $T_{\tilde a^{-1},\tilde b^{-1}}$. The transpose for the plain form swaps and conjugates the two parameters, $T^{\sim}_{\tilde a,\tilde b} = T_{\tilde b^{\natural},\tilde a^{\natural}}$; the transpose for the quaternionic form keeps the places and conjugates, $T^{\dagger}_{\tilde a,\tilde b} = T_{\tilde a^{\natural},\tilde b^{\natural}}$; the two coincide on the real-proportional parameters, and a nonzero sandwich is plain-self-transpose exactly for $\tilde b \in \mathbb{R}\tilde a^{\natural}$. The plain algebra has the same family of operators with the plain sandwiches, the composition law reversing one parameter, and the transpose swapping the parameters without conjugating; the whole difference is the conjugation that the first slot of the quaternionic product inserts.

## Summary of Notation

| symbol | meaning |
|---|---|
| $T_{\tilde a,\tilde b}(\tilde q) = \tilde a^{\natural}\tilde q\tilde b = L_{\tilde a^{\natural}}R_{\tilde b}$ | the two-sided operator of the quaternionic product |
| $L_{\alpha}R_{\beta} = L_{\alpha'}R_{\beta'} \iff (\alpha',\beta') = (\mu\alpha,\mu^{-1}\beta)$ | when two sandwiches agree; the kernel is $\{(\lambda,\lambda^{-1})\}$, $\lambda \in \mathbb{R}^\times$ |
| $\mathcal T$ | the family of two-sided operators, spanning $\operatorname{End}_\mathbb{R}(\mathbb{H})$ |
| $T_{\tilde a,\tilde b}T_{\tilde c,\tilde d} = T_{\tilde c\tilde a,\tilde d\tilde b}$ | the composition law, both parameters reversed |
| $T^{\sim}_{\tilde a,\tilde b} = T_{\tilde b^{\natural},\tilde a^{\natural}}$ | the transpose for the plain form $\mathrm B$ |
| $T^{\dagger}_{\tilde a,\tilde b} = T_{\tilde a^{\natural},\tilde b^{\natural}}$ | the transpose for the quaternionic form $N$ |
| $T^{\sim}_{\tilde a,\tilde b} = T^{\dagger}_{\tilde a,\tilde b} \iff \tilde b \in \mathbb{R}\tilde a$ | the two transposes coincide on proportional parameters |
| $T_{\tilde a,\tilde b} = T^{\sim}_{\tilde a,\tilde b} \iff \tilde b \in \mathbb{R}\tilde a^{\natural}$ | the plain self-transpose parameters |
| $\mathrm B(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q)$ | the plain form, of signature $(1,3)$ |
| $N(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q^{\natural})$ | the quaternionic form, of signature $(4,0)$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the sandwich representation, the enveloping algebra and the identification of the sandwiches with the endomorphisms.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the opposite ring, the two-sided action and the anti-isomorphisms of a division algebra.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the transpose attached to a bilinear form and its behaviour under an involution.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the isometry and similarity groups of a form on a central simple algebra.
