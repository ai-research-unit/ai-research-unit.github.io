# __Two-Sided Operators on the General Quaternionic Algebra__

## Introduction

The **two-sided operators** of the general quaternionic bilinear product $\tilde q_1 \star \tilde q_2 = \tilde q_1^{\natural}\tilde q_2$ of *Introduction to the General Quaternionic Algebra* are the products of a left and a right multiplication, with the left one carrying the conjugation of the product and the right one the plain product of the block:

$$
T_{\tilde q_3,\tilde q_4}(\tilde q) = \tilde q_3 \star \tilde q \cdot \tilde q_4 = \tilde q_3^{\natural}\tilde q\,\tilde q_4 = L_{\tilde q_3^{\natural}}R_{\tilde q_4} .
$$

They are the elementary sandwiches of the block, and their family carries the whole operator calculus of the algebra: a composition law, an adjoint for each of the two forms of the space, and the fact — the *type* of the family — that the sandwiches span every real-linear operator of $\mathbb{H}$. The left factor is the left multiplication by the conjugated parameter, $L_{\tilde q_3^{\natural}}$. This article establishes those four facts and compares them with the plain algebra of the same space, where the left multiplication does not carry the conjugation and the two laws are correspondingly different. The one-sided families are *One-Sided Operators on the General Quaternionic Algebra*, below this article in this category, and the left family with its monoid *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, above this article in this category; the forms are *The Isotropic Structure of the General Quaternionic Algebra*, above this article in this category.

**Conventions.** The elements are $\tilde q_1 = \sum_\mu q_{1\mu} e_\mu$ with the conjugation ${}^{\natural}$ negating $\vec e_x,\vec e_y,\vec e_z$; the product is $\tilde q_1 \star \tilde q_2 = \tilde q_1^{\natural}\tilde q_2$; the two forms of the space are the plain form $\langle\tilde q_1,\tilde q_2\rangle = \mathrm{Sc}(\tilde q_1\tilde q_2)$ of signature $(1,3)$ and the quaternionic form $\langle\tilde q_1,\tilde q_2\rangle_{\natural} = \mathrm{Sc}(\tilde q_1\tilde q_2^{\natural}) = \sum_\mu q_{1\mu} q_{2\mu}$ of signature $(4,0)$; a right multiplication is the plain one, $R_{\tilde q_4}(\tilde q) = \tilde q\tilde q_4$.

## The Family

**Definition.** For $\tilde q_3,\tilde q_4 \in \mathbb{H}$ the **two-sided operator** is $T_{\tilde q_3,\tilde q_4} = L_{\tilde q_3^{\natural}}R_{\tilde q_4}$, the map $\tilde q \mapsto \tilde q_3^{\natural}\tilde q\tilde q_4$. The family is $\mathcal T = \{T_{\tilde q_3,\tilde q_4}\}$.

**Theorem (the type of the family).** The family spans the whole algebra of real-linear operators, $\operatorname{span}_\mathbb{R}\mathcal T = \operatorname{End}_\mathbb{R}(\mathbb{H})$, of real dimension sixteen; every real-linear operator of $\mathbb{H}$ is a finite real combination of two-sided operators.

*Proof.* The left multiplications span a four-dimensional subspace by *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, above this article in this category, and the right multiplications span another four-dimensional subspace; the products $L_{\tilde q_3^{\natural}}R_{\tilde q_4}$ span the product of the two subspaces, and the sandwich operators of the plain algebra are known to span $\operatorname{End}_\mathbb{R}(\mathbb{H})$, since the enveloping algebra $\mathbb{H} \otimes_\mathbb{R} \mathbb{H}^{\mathrm{opp}}$ is the full matrix algebra $M_4(\mathbb{R})$. The reindexing $\tilde q_3 \mapsto \tilde q_3^{\natural}$ is a bijection, so the quaternionic sandwiches are the plain ones reindexed and span the same sixteen dimensions.

**Corollary.** The four-dimensional space $\mathbb{H}$ is simple as a module over the operator algebra $\mathcal T$: the family is all of $\operatorname{End}_\mathbb{R}(\mathbb{H})$, and a full endomorphism algebra acts faithfully.

*Proof.* The theorem gives $\mathcal T = \operatorname{End}_\mathbb{R}(\mathbb{H})$, and the endomorphism algebra of a finite-dimensional space acts faithfully on it.

## Composition

**Theorem (the composition law).** For all $\tilde q_3,\tilde q_4,\tilde q_5,\tilde q_6 \in \mathbb{H}$,

$$
T_{\tilde q_3,\tilde q_4}T_{\tilde q_5,\tilde q_6} = T_{\tilde q_5\tilde q_3,\,\tilde q_6\tilde q_4} .
$$

Both parameters are **reversed**, because both the first factor of the product and the second carry an order-reversing step: the first through the anti-automorphism ${}^{\natural}$ that the left multiplication contains, the second through the opposite algebra.

*Proof.* Apply the left side to $\tilde q$ and use the associativity of the plain product:
$$
T_{\tilde q_3,\tilde q_4}\bigl(T_{\tilde q_5,\tilde q_6}(\tilde q)\bigr) = \tilde q_3^{\natural}\bigl(\tilde q_5^{\natural}\tilde q\tilde q_6\bigr)\tilde q_4 = \bigl(\tilde q_3^{\natural}\tilde q_5^{\natural}\bigr)\tilde q\bigl(\tilde q_6\tilde q_4\bigr) = (\tilde q_5\tilde q_3)^{\natural}\,\tilde q\,(\tilde q_6\tilde q_4),
$$
which is $T_{\tilde q_5\tilde q_3,\tilde q_6\tilde q_4}(\tilde q)$.

**Proposition (when two sandwiches agree, and the zero case).** The sandwich $L_\alpha R_\beta$ is zero exactly when $\alpha = 0$ or $\beta = 0$. For **nonzero** parameter pairs, two sandwiches agree as operators exactly when the pairs differ by a single real scalar:

$$
\alpha,\beta,\alpha',\beta' \neq 0 : \quad L_{\alpha}R_{\beta} = L_{\alpha'}R_{\beta'} \iff \alpha' = \mu\alpha \text{ and } \beta' = \mu^{-1}\beta \text{ for some } \mu \in \mathbb{R}^\times .
$$

*Proof.* The equality $L_\alpha R_\beta = 0$ says $\alpha\tilde q\beta = 0$ for every $\tilde q$; at $\tilde q = e_t$ this is $\alpha\beta = 0$, and in a division algebra a product vanishes exactly when a factor does, so $\alpha = 0$ or $\beta = 0$, and conversely. Assume now all four parameters nonzero and $\alpha\tilde q\beta = \alpha'\tilde q\beta'$ for every $\tilde q$. Multiply on the left by $\alpha^{-1}$ and put $\gamma = \alpha^{-1}\alpha'$, so that $\tilde q\beta = \gamma\tilde q\beta'$ for every $\tilde q$. At $\tilde q = e_t$ this gives $\beta = \gamma\beta'$, whence $\beta' = \gamma^{-1}\beta$; substituting back gives $(\tilde q\gamma - \gamma\tilde q)\beta' = 0$ for every $\tilde q$, and since $\beta' \neq 0$ the parameter $\gamma$ is central, that is $\gamma = \mu$ real and nonzero. Therefore $\alpha' = \alpha\gamma = \mu\alpha$ and $\beta' = \mu^{-1}\beta$. Conversely, if $\alpha' = \mu\alpha$ and $\beta' = \mu^{-1}\beta$ then $L_{\alpha'}R_{\beta'} = L_{\mu\alpha}R_{\mu^{-1}\beta} = L_\alpha R_\beta$, because the scalar is central.

**Corollary (the monoid and the kernel).** The family is a monoid under composition, with identity $T_{e_t,e_t} = \mathrm{id}$; the map $(\tilde q_3,\tilde q_4) \mapsto T_{\tilde q_3,\tilde q_4}$ is a homomorphism of monoids onto the family from the product of two opposite monoids, $(\mathbb{H}^{\mathrm{opp}})^2$ with the multiplication of the parameters in both places, and its kernel — the preimage of the identity — is the one-parameter group

$$
\{(\lambda,\lambda^{-1}) : \lambda \in \mathbb{R}^\times\} \cong \mathbb{R}^\times .
$$

*Proof.* Closure is the law, and $T_{e_t,e_t}(\tilde q) = e_t^{\natural}\tilde q e_t = \tilde q$. The homomorphism reads the law as the multiplication of the parameters with both places reversed, which is the opposite law in each place. For the kernel, $T_{\tilde q_3,\tilde q_4} = \mathrm{id}$ forces $T_{\tilde q_3,\tilde q_4}$ nonzero, hence $\tilde q_3 \neq 0$ and $\tilde q_4 \neq 0$; the agree-as-operators criterion applied to the pairs $(\tilde q_3^{\natural},\tilde q_4)$ and $(e_t,e_t)$ then gives $\tilde q_3^{\natural} = \mu e_t$ and $\tilde q_4 = \mu^{-1}e_t$ with a single real $\mu \neq 0$, that is $\tilde q_3 = \mu$ and $\tilde q_4 = \mu^{-1}$ real scalars. Hence the kernel is the displayed one-parameter group. The two-element set $\{(\pm e_t,\pm e_t)\}$ is the part of it inside the integral scalars, not the whole kernel.

**Corollary (the one-parameter redundancy).** The parametrisation is not injective: $T_{\lambda\tilde q_3,\lambda^{-1}\tilde q_4} = T_{\tilde q_3,\tilde q_4}$ for every real $\lambda \neq 0$, because the scalar commutes with everything. The family is therefore a quotient of $(\mathbb{H}^{\mathrm{opp}})^2$ by the diagonal scalars, and the two-sided operators of a given parameter pair are the same operator along the two one-parameter lines of the scaling. The kernel of the previous corollary is exactly the diagonal scaling line through $(e_t,e_t)$.

**Corollary (the units).** $T_{\tilde q_3,\tilde q_4}$ is invertible exactly when $\tilde q_3 \neq 0$ and $\tilde q_4 \neq 0$, with inverse $T_{\tilde q_3^{-1},\tilde q_4^{-1}}$.

*Proof.* By the law, $T_{\tilde q_3,\tilde q_4}T_{\tilde q_3^{-1},\tilde q_4^{-1}} = T_{\tilde q_3^{-1}\tilde q_3,\tilde q_4^{-1}\tilde q_4} = T_{e_t,e_t}$; conversely an invertible two-sided operator has a nonzero value at $e_t$ on both sides, $\tilde q_3^{\natural}\tilde q_4 \neq 0$, so both parameters are nonzero. The inverses are taken in the plain algebra, where every nonzero element has one.

## The Adjoint

Each form of the space defines a transpose on the operators, and the two transposes of a sandwich are other sandwiches with the parameters conjugated and swapped.

**Theorem (the transpose for the plain form).** With respect to the plain form $\langle\tilde q_1,\tilde q_2\rangle = \mathrm{Sc}(\tilde q_1\tilde q_2)$, the transpose of a two-sided operator is

$$
T_{\tilde q_3,\tilde q_4}^{\sim} = T_{\tilde q_4^{\natural},\tilde q_3^{\natural}} = L_{\tilde q_4}R_{\tilde q_3^{\natural}} .
$$

*Proof.* The transpose is characterised by $\langle T\tilde q_1,\tilde q_2\rangle = \langle\tilde q_1,T^{\sim}\tilde q_2\rangle$. For $T = T_{\tilde q_3,\tilde q_4}$,
$$
\mathrm B\bigl(T\tilde q_1,\tilde q_2\bigr) = \mathrm{Sc}\bigl(\tilde q_3^{\natural}\tilde q_1\tilde q_4\tilde q_2\bigr) = \mathrm{Sc}\bigl(\tilde q_1\,\tilde q_4\tilde q_2\tilde q_3^{\natural}\bigr) ,
$$
by the cyclic invariance of the scalar part, and the last is $\langle\tilde q_1,\tilde q_4\tilde q_2\tilde q_3^{\natural}\rangle = \langle\tilde q_1,T_{\tilde q_4^{\natural},\tilde q_3^{\natural}}\tilde q_2\rangle$, since $(\tilde q_4^{\natural})^{\natural}\tilde q_2\tilde q_3^{\natural} = \tilde q_4\tilde q_2\tilde q_3^{\natural}$.

**Theorem (the transpose for the quaternionic form).** With respect to the quaternionic form $\langle\tilde q_1,\tilde q_2\rangle_{\natural} = \mathrm{Sc}(\tilde q_1\tilde q_2^{\natural})$ of signature $(4,0)$, the transpose of a two-sided operator is

$$
T_{\tilde q_3,\tilde q_4}^{\dagger} = T_{\tilde q_3^{\natural},\tilde q_4^{\natural}} .
$$

*Proof.* The characterisation is $\langle T\tilde q_1,\tilde q_2\rangle_{\natural} = \langle\tilde q_1,T^{\dagger}\tilde q_2\rangle_{\natural}$, and
$$
N\bigl(T\tilde q_1,\tilde q_2\bigr) = \mathrm{Sc}\bigl(\tilde q_3^{\natural}\tilde q_1\tilde q_4\tilde q_2^{\natural}\bigr) = \mathrm{Sc}\bigl(\tilde q_1\,\tilde q_4\tilde q_2^{\natural}\tilde q_3^{\natural}\bigr) = \mathrm{Sc}\bigl(\tilde q_1\,(\tilde q_3\tilde q_2\tilde q_4^{\natural})^{\natural}\bigr) ,
$$
using that $(\tilde q_3\tilde q_2\tilde q_4^{\natural})^{\natural} = \tilde q_4\tilde q_2^{\natural}\tilde q_3^{\natural}$; the last is $\langle\tilde q_1,\tilde q_3\tilde q_2\tilde q_4^{\natural}\rangle_{\natural} = \langle\tilde q_1,T_{\tilde q_3^{\natural},\tilde q_4^{\natural}}\tilde q_2\rangle_{\natural}$, since $(\tilde q_3^{\natural})^{\natural}\tilde q_2\tilde q_4^{\natural} = \tilde q_3\tilde q_2\tilde q_4^{\natural}$.

**Corollary (the two transposes and the comparison).** The plain transpose swaps the two parameters and conjugates them both, $T^{\sim}_{\tilde q_3,\tilde q_4} = T_{\tilde q_4^{\natural},\tilde q_3^{\natural}}$; the quaternionic transpose keeps the two parameters in place and conjugates them both, $T^{\dagger}_{\tilde q_3,\tilde q_4} = T_{\tilde q_3^{\natural},\tilde q_4^{\natural}}$. For a nonzero sandwich, the two transposes coincide exactly when the two parameters are proportional over $\mathbb{R}$,

$$
\tilde q_3,\tilde q_4 \neq 0 : \quad T^{\sim}_{\tilde q_3,\tilde q_4} = T^{\dagger}_{\tilde q_3,\tilde q_4} \iff \tilde q_4 \in \mathbb{R}\tilde q_3 ,
$$

which includes the diagonal case $\tilde q_3 = \tilde q_4$ but is strictly wider; and a nonzero sandwich is self-transpose for the plain form exactly when the second parameter is a real multiple of the conjugate of the first,

$$
\tilde q_3,\tilde q_4 \neq 0 : \quad T_{\tilde q_3,\tilde q_4} = T^{\sim}_{\tilde q_3,\tilde q_4} \iff \tilde q_4 \in \mathbb{R}\tilde q_3^{\natural} .
$$

The two criteria are stated for a nonzero sandwich because the zero operators $T_{0,\tilde q_4}$ and $T_{\tilde q_3,0}$ are transposed to zero and satisfy both equalities trivially, without any proportion between the parameters.

*Proof.* The transposes are the sandwiches $T_{\tilde q_4^{\natural},\tilde q_3^{\natural}}$ and $T_{\tilde q_3^{\natural},\tilde q_4^{\natural}}$ with all four parameters nonzero for a nonzero sandwich. They agree exactly when the pairs $(\tilde q_4^{\natural},\tilde q_3^{\natural})$ and $(\tilde q_3^{\natural},\tilde q_4^{\natural})$ differ by the real scalar of the agree-as-operators criterion, that is $\tilde q_3^{\natural} = \mu\tilde q_4^{\natural}$ for some $\mu \neq 0$, which is $\tilde q_3 = \mu\tilde q_4$. For the self-transpose reading, $T_{\tilde q_3,\tilde q_4} = T^{\sim}_{\tilde q_3,\tilde q_4}$ compares the pairs $(\tilde q_3^{\natural},\tilde q_4)$ and $(\tilde q_4^{\natural},\tilde q_3^{\natural})$: the criterion gives $\tilde q_4^{\natural} = \mu\tilde q_3^{\natural}$ and $\tilde q_3^{\natural} = \mu^{-1}\tilde q_4^{\natural}$, which is the single condition $\tilde q_4 = \mu\tilde q_3^{\natural}$ with a real $\mu \neq 0$.

## The Comparison with the Plain Algebra

**Proposition.** The two-sided operators of the plain algebra are the sandwiches with the direct product, $T^{(0)}_{\tilde q_3,\tilde q_4}(\tilde q) = \tilde q_3\tilde q\tilde q_4$, and they satisfy the composition law $T^{(0)}_{\tilde q_3,\tilde q_4}T^{(0)}_{\tilde q_5,\tilde q_6} = T^{(0)}_{\tilde q_3\tilde q_5,\tilde q_6\tilde q_4}$, with only the second parameter reversed. The quaternionic operators are the same sandwiches with the first parameter conjugated, $T_{\tilde q_3,\tilde q_4} = T^{(0)}_{\tilde q_3^{\natural},\tilde q_4}$, and their composition law reverses both parameters.

*Proof.* The plain law is the associativity of the plain product read twice; the quaternionic law is the theorem above, and the identification with the plain family is $\tilde q_3^{\natural}(\tilde q\tilde q_4) = T^{(0)}_{\tilde q_3^{\natural},\tilde q_4}(\tilde q)$.

| | plain algebra | quaternionic algebra |
|---|---|---|
| operator | $T^{(0)}_{\tilde q_3,\tilde q_4}(\tilde q) = \tilde q_3\tilde q\tilde q_4$ | $T_{\tilde q_3,\tilde q_4}(\tilde q) = \tilde q_3^{\natural}\tilde q\tilde q_4$ |
| composition | $T^{(0)}_{\tilde q_3,\tilde q_4}T^{(0)}_{\tilde q_5,\tilde q_6} = T^{(0)}_{\tilde q_3\tilde q_5,\tilde q_6\tilde q_4}$ | $T_{\tilde q_3,\tilde q_4}T_{\tilde q_5,\tilde q_6} = T_{\tilde q_5\tilde q_3,\tilde q_6\tilde q_4}$ |
| transpose for $\mathrm B$ | $T^{(0)\sim}_{\tilde q_3,\tilde q_4} = T^{(0)}_{\tilde q_4,\tilde q_3}$ | $T^{\sim}_{\tilde q_3,\tilde q_4} = T_{\tilde q_4^{\natural},\tilde q_3^{\natural}}$ |
| transpose for $N$ | $T^{(0)\dagger}_{\tilde q_3,\tilde q_4} = T^{(0)}_{\tilde q_3^{\natural},\tilde q_4^{\natural}}$ | $T^{\dagger}_{\tilde q_3,\tilde q_4} = T_{\tilde q_3^{\natural},\tilde q_4^{\natural}}$ |
| family | all of $\operatorname{End}_\mathbb{R}(\mathbb{H})$ | all of $\operatorname{End}_\mathbb{R}(\mathbb{H})$ |

**Corollary.** The families agree as sets of operators, $T_{\tilde q_3,\tilde q_4} = T^{(0)}_{\tilde q_3^{\natural},\tilde q_4}$, and they differ in the multiplication they carry: the plain law reverses one parameter, the quaternionic law reverses two. The difference is the anti-automorphism in the first slot of the product, and it is the same difference as between the two left-multiplication monoids (*The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, above this article in this category).

## Summary

The two-sided operators of the quaternionic product are $T_{\tilde q_3,\tilde q_4}(\tilde q) = \tilde q_3^{\natural}\tilde q\tilde q_4$, the sandwiches of the conjugated left multiplication $L_{\tilde q_3^{\natural}}$ with the plain right multiplication $R_{\tilde q_4}$. They span every real-linear operator of $\mathbb{H}$; two of them agree exactly on parameter pairs differing by a real scalar, so the family is a quotient of the parameter space by that scaling. They form a monoid with identity $T_{e_t,e_t}$ and composition law $T_{\tilde q_3,\tilde q_4}T_{\tilde q_5,\tilde q_6} = T_{\tilde q_5\tilde q_3,\tilde q_6\tilde q_4}$ reversing **both** parameters, the identity being reached exactly on the one-parameter kernel $\{(\lambda,\lambda^{-1})\}$; the invertible elements are those with both parameters nonzero, with inverse $T_{\tilde q_3^{-1},\tilde q_4^{-1}}$. The transpose for the plain form swaps and conjugates the two parameters, $T^{\sim}_{\tilde q_3,\tilde q_4} = T_{\tilde q_4^{\natural},\tilde q_3^{\natural}}$; the transpose for the quaternionic form keeps the places and conjugates, $T^{\dagger}_{\tilde q_3,\tilde q_4} = T_{\tilde q_3^{\natural},\tilde q_4^{\natural}}$; the two coincide on the real-proportional parameters, and a nonzero sandwich is plain-self-transpose exactly for $\tilde q_4 \in \mathbb{R}\tilde q_3^{\natural}$. The plain algebra has the same family of operators with the plain sandwiches, the composition law reversing one parameter, and the transpose swapping the parameters without conjugating; the whole difference is the conjugation that the first slot of the quaternionic product inserts.

## Summary of Notation

| symbol | meaning |
|---|---|
| $T_{\tilde q_3,\tilde q_4}(\tilde q) = \tilde q_3^{\natural}\tilde q\tilde q_4 = L_{\tilde q_3^{\natural}}R_{\tilde q_4}$ | the two-sided operator of the quaternionic product |
| $L_{\alpha}R_{\beta} = L_{\alpha'}R_{\beta'} \iff (\alpha',\beta') = (\mu\alpha,\mu^{-1}\beta)$ | when two sandwiches agree; the kernel is $\{(\lambda,\lambda^{-1})\}$, $\lambda \in \mathbb{R}^\times$ |
| $\mathcal T$ | the family of two-sided operators, spanning $\operatorname{End}_\mathbb{R}(\mathbb{H})$ |
| $T_{\tilde q_3,\tilde q_4}T_{\tilde q_5,\tilde q_6} = T_{\tilde q_5\tilde q_3,\tilde q_6\tilde q_4}$ | the composition law, both parameters reversed |
| $T^{\sim}_{\tilde q_3,\tilde q_4} = T_{\tilde q_4^{\natural},\tilde q_3^{\natural}}$ | the transpose for the plain form $\mathrm B$ |
| $T^{\dagger}_{\tilde q_3,\tilde q_4} = T_{\tilde q_3^{\natural},\tilde q_4^{\natural}}$ | the transpose for the quaternionic form $\langle\cdot,\cdot\rangle_{\natural}$ |
| $T^{\sim}_{\tilde q_3,\tilde q_4} = T^{\dagger}_{\tilde q_3,\tilde q_4} \iff \tilde q_4 \in \mathbb{R}\tilde q_3$ | the two transposes coincide on proportional parameters |
| $T_{\tilde q_3,\tilde q_4} = T^{\sim}_{\tilde q_3,\tilde q_4} \iff \tilde q_4 \in \mathbb{R}\tilde q_3^{\natural}$ | the plain self-transpose parameters |
| $\langle\tilde q_1,\tilde q_2\rangle = \mathrm{Sc}(\tilde q_1\tilde q_2)$ | the plain form, of signature $(1,3)$ |
| $\langle\tilde q_1,\tilde q_2\rangle_{\natural} = \mathrm{Sc}(\tilde q_1\tilde q_2^{\natural})$ | the quaternionic form, of signature $(4,0)$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the sandwich representation, the enveloping algebra and the identification of the sandwiches with the endomorphisms.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the opposite ring, the two-sided action and the anti-isomorphisms of a division algebra.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the transpose attached to a bilinear form and its behaviour under an involution.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the isometry and similarity groups of a form on a central simple algebra.
