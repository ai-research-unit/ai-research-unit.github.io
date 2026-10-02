
# __Modules over an Involutive Algebra__

## Introduction

An involution of an algebra is an anti-automorphism of order two, and it acts on the module category by twisting: a left module $M$ becomes another left module $M^{\sigma}$ whose action is the original one composed with $\sigma$. This article defines the twisted module, shows that the twisting is an involution of the category, and identifies the involution it induces on the endomorphisms of a module — the first place where the involution of the algebra reaches the operators.

The article opens the `* Theory` group of this category. It assumes the involutive algebra of *Involutive Linear Algebras* (in Part I), the module theory of *Modules over an Algebra*, and the operator layer of *Left and Right Multiplication of a Module*, *Module Endomorphisms* and *The Endomorphism Algebra of a Module*. The pairing, the adjoint and the involution on the full endomorphism ring of a module are the subjects of the two articles that follow, *The Adjoint of a Module Homomorphism* and *The Involution on the Endomorphism Ring of a Module*; here the involution is induced by $\sigma$ alone, on a free module, and the general case is named as needing a pairing. The article stays inside Part I: no distance, norm, form or limit occurs. Throughout, $R$ is a commutative ring with $1 \neq 0$, $A$ is a unital associative $R$-algebra with an involution $\sigma$, $M$ and $N$ are left $A$-modules, and $L_a$ is the left multiplication of *Left and Right Multiplication of a Module*.

## Involutions and Twisted Modules

### The involution of the algebra

**Definition.** An **involution** of $A$ is an $R$-linear map $\sigma : A \to A$ with

$$
\sigma^{2}=\mathrm{id}, \qquad \sigma(ab)=\sigma(b)\,\sigma(a) \qquad (a,b \in A);
$$

the pair $(A,\sigma)$ is an **involutive algebra**.

The definition, the elementary properties and the examples are those of *Involutive Linear Algebras*; only the following are used. The involution fixes the unit, $\sigma(1)=1$; it preserves invertibility, $\sigma(a)^{-1}=\sigma(a^{-1})$, so it acts on $A^{\times}$; and it is an involution of the opposite algebra $A^{\mathrm{op}}$ as well, since for the opposite product $a \cdot_{\mathrm{op}} b=ba$ one has $\sigma(a \cdot_{\mathrm{op}} b)=\sigma(ba)=\sigma(a)\sigma(b)=\sigma(b) \cdot_{\mathrm{op}} \sigma(a)$.

### The twisted module

**Definition.** Let $M$ be a left $A$-module. The **twisted module** $M^{\sigma}$ is the same additive group $M$ with the action

$$
a \cdot_{\sigma} m = \sigma(a)\,m \qquad (a \in A,\ m \in M).
$$

**Proposition.** $M^{\sigma}$ is a left $A$-module.

*Proof.* Distributivity and the unit are inherited from $M$. For associativity, $(ab) \cdot_{\sigma} m=\sigma(ab)m=\sigma(b)\sigma(a)m$, while $a \cdot_{\sigma}(b \cdot_{\sigma} m)=a \cdot_{\sigma}(\sigma(b)m)=\sigma(a)\sigma(b)m$; the two agree because $\sigma$ is an anti-automorphism. $\square$

The underlying $R$-module of $M^{\sigma}$ is that of $M$; only the action is changed, and it is changed by $\sigma$.

### Twisting is an involution of the category

**Proposition.** The assignment $M \mapsto M^{\sigma}$, with a homomorphism $f : M \to N$ sent to the same map $f : M^{\sigma} \to N^{\sigma}$, is an endofunctor of the category of left $A$-modules, and

$$
(M^{\sigma})^{\sigma}=M \qquad (M \text{ a left } A\text{-module}),
$$

so the functor is an equivalence of categories and an involution up to the identity.

*Proof.* A map $f : M \to N$ that is $A$-linear is $A$-linear for the twisted actions: $f(a \cdot_{\sigma} m)=f(\sigma(a)m)=\sigma(a)f(m)=a \cdot_{\sigma} f(m)$. Identities and composites are unchanged, so the assignment is a functor; and the action of $M^{\sigma}$ twisted again is $a \cdot_{\sigma\cdot_{\sigma}} m=\sigma(\sigma(a))m=am$, so twisting twice returns the original action. $\square$

**Corollary.** Twisting preserves and reflects the elementary properties of a module: it preserves submodules, quotients, direct sums, free modules and finitely generated modules, and it carries a simple module to a simple module.

*Proof.* The two categories are equal as categories through an invertible functor that is the identity on the underlying additive groups; all these properties are preserved under such an equivalence. $\square$

Twisting is the categorical meaning of the involution: it is a symmetry of the module category of order two.

## The Induced Involution on the Endomorphisms

### The twisted endomorphism ring

**Proposition.** For every left $A$-module $M$ the identity on maps is an isomorphism of $R$-algebras

$$
\operatorname{End}_A(M) \xrightarrow{\ \sim\ } \operatorname{End}_A(M^{\sigma}), \qquad f \longmapsto f .
$$

*Proof.* The map is additive and preserves composition and the identity; it is bijective because $M$ and $M^{\sigma}$ have the same underlying set and the same notion of $A$-linear map, as the preceding proposition shows. $\square$

So the endomorphism ring cannot distinguish a module from its twist; the twist is invisible to the operators, and this is why an involution on the endomorphisms needs an extra structure, which is a pairing, supplied in the articles that follow.

### The regular module

For the regular module the induced involution is $\sigma$ itself.

**Proposition.** Under the identification $\operatorname{End}_A({}_A A)\cong A^{\mathrm{op}}$ of *Automorphisms of Modules over an Algebra*, the involution $\sigma$ of $A$ is an involution of $A^{\mathrm{op}}$, and the corresponding map on $\operatorname{End}_A({}_A A)$ carries the right multiplication $R_a$ to $R_{\sigma(a)}$.

*Proof.* $\sigma$ is an involution of $A^{\mathrm{op}}$ by the observations above, and the isomorphism $A^{\mathrm{op}}\to\operatorname{End}_A(A)$ sends $a$ to $R_a$, so it carries $\sigma$ to $R_a \mapsto R_{\sigma(a)}$. $\square$

This is the base case: the involution of the algebra is the involution induced on the endomorphism ring of the regular module.

### The free module

For a free module the induced involution is $\sigma$ applied entrywise and combined with transposition.

**Theorem.** Let $n \geq 1$ and identify $\operatorname{End}_A({}_A A^n)\cong M_n(A^{\mathrm{op}})$ by the right multiplication $f(v)=vX$ of *The Endomorphism Algebra of a Module*. Then the map

$$
\Theta : M_n(A^{\mathrm{op}}) \to M_n(A^{\mathrm{op}}), \qquad \Theta(X)_{ij}=\sigma(X_{ji}),
$$

is an involution of the $R$-algebra $M_n(A^{\mathrm{op}})$, and it is the unique map that applies $\sigma$ to each entry and transposes the matrix.

*Proof.* Additivity and $R$-linearity are entrywise. For the product, using $(XY)_{ij}=\sum_k X_{ik} \cdot_{\mathrm{op}} Y_{kj}=\sum_k Y_{kj}X_{ik}$, one has

$$
\Theta(XY)_{ij}=\sigma\!\left(\sum_k Y_{ki}X_{jk}\right)=\sum_k \sigma(X_{jk})\sigma(Y_{ki})=\sum_k \Theta(X)_{kj}\cdot_{\mathrm{op}}\Theta(Y)_{ik}=(\Theta(Y)\Theta(X))_{ij},
$$

so $\Theta(XY)=\Theta(Y)\Theta(X)$: it is an anti-automorphism. It has order two because $\Theta^{2}(X)_{ij}=\sigma(\Theta(X)_{ji})=\sigma(\sigma(X_{ij}))=X_{ij}$. Hence $\Theta$ is an involution. Uniqueness is clear from the formula. $\square$

**Corollary.** The involution of the algebra $A$ induces an involution of the endomorphism ring of every free module, and on the regular module this is $\sigma$ itself, recovering the proposition above at $n=1$.

*Proof.* $n=1$ gives $\Theta(X)_{11}=\sigma(X_{11})$ on $M_1(A^{\mathrm{op}})=A^{\mathrm{op}}$, which is $\sigma$. $\square$

### Dependence on the basis

**Proposition.** The involution $\Theta$ of a free module depends on the chosen basis: if $P \in M_n(A^{\mathrm{op}})$ is the change-of-basis matrix from the standard basis to another basis, the induced involution for the second basis is $X \mapsto P\,\Theta(P^{-1}XP)\,P^{-1}$, an involution conjugate to $\Theta$ by the inner automorphism of $P$.

*Proof.* Change of basis is an isomorphism of $\operatorname{End}_A(A^n)$ sending an endomorphism of matrix $X$ to $P^{-1}XP$ for a suitable $P$, and conjugation transports a map on the matrix ring; carrying $\Theta$ through gives the displayed formula, which is an involution because conjugation by $P$ is an algebra automorphism. $\square$

Thus for a free module the involution induced by $\sigma$ is determined up to conjugation by a change of basis; the canonical choice is the one that applies $\sigma$ entrywise and transposes.

## Self-Conjugate Modules

### Conjugacy and its operators

**Definition.** A module $M$ is **self-conjugate** when $M \cong M^{\sigma}$.

**Proposition.** If $u : M \to M^{\sigma}$ is an isomorphism, then the composite

$$
\operatorname{End}_A(M) \xrightarrow{\ \sim\ } \operatorname{End}_A(M^{\sigma}) \xrightarrow{\ f \mapsto u^{-1}fu\ } \operatorname{End}_A(M)
$$

is a unital $R$-algebra automorphism of $\operatorname{End}_A(M)$, namely the inner automorphism by $u$; it is an involution exactly when $u^{2}$ is central in $\operatorname{End}_A(M)$, and it need not be an involution in general.

*Proof.* A self-conjugacy $u$ is in particular an element of the ring $\operatorname{End}_R(M)$, and conjugation by it is an algebra automorphism; its square is conjugation by $u^{2}$, which is the identity when $u^{2}$ is central, and not otherwise. $\square$

This shows why the general module does not by itself carry an induced involution: the only involution produced by a self-conjugacy is inner, and inner automorphisms do not see the involution of the algebra. A pairing is the missing datum, and it is introduced in the next articles.

### What a pairing will supply

The next article defines the **adjoint** of a homomorphism with respect to a pairing and uses it to build the involution on the endomorphism ring of a module; the one after that studies that involution, its self-adjoint part and its unitary group. The free-module involution $\Theta$ of this article is the model these constructions generalise, and the basis-independent description of $\Theta$ is exactly the adjoint with respect to the standard pairing on $A^n$.

## Examples

**(a) The transpose involution.** Let $A=M_n(R)$ with $\sigma(X)=X^{\mathrm{T}}$. For the regular module, $\operatorname{End}_A(A)\cong A^{\mathrm{op}}$, and $\sigma$ is the transpose on $A^{\mathrm{op}}$; for the free module $A^m$ the induced involution $\Theta$ is the usual transpose combined with $\sigma$ entrywise.

**(b) The trivial involution.** If $A$ is commutative and $\sigma=\mathrm{id}$, then $M^{\sigma}=M$ for every module and $\Theta$ is the transpose of matrices over $A$. The twisting functor is the identity.

**(c) The quaternions.** For $A=\mathbb{H}$ and $\sigma$ the quaternion conjugation, the regular module has $\operatorname{End}_A(\mathbb{H})\cong\mathbb{H}^{\mathrm{op}}\cong\mathbb{H}$ with involution $\sigma$, and the free module $\mathbb{H}^m$ has the conjugate-transpose involution on matrices over $\mathbb{H}^{\mathrm{op}}$.

**(d) Matrix algebras with the conjugate transpose.** Let $A=M_n(\mathbb{C})$ with $\sigma(X)=\overline{X}^{\mathrm{T}}$. Then $\sigma$ is an involution of $A$ and of $A^{\mathrm{op}}$; the induced involution on the endomorphism ring of the regular module is the conjugate transpose, and the unitary group of the algebra, defined in the involutive-algebra theory, is the classical unitary group $U(n)$.

**(e) The biquaternions.** For $A=\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with the involution $\sigma$ obtained from conjugation on $\mathbb{C}$ and on $\mathbb{H}$, the induced involution on $\operatorname{End}_{\mathbb{B}}(\mathbb{B})\cong\mathbb{B}^{\mathrm{op}}$ is $\sigma$, and the unitary elements of $\mathbb{B}$ are the units fixed by the corresponding adjoint of the regular module.

## Summary

An algebra with an involution $\sigma$ acts on the module category by twisting, $a \cdot_{\sigma} m=\sigma(a)m$; the twisted module $M^{\sigma}$ is a left $A$-module, twisting is an endofunctor that is an involution up to the identity, and it preserves and reflects submodules, quotients, direct sums, freeness, finite generation and simplicity. The endomorphism ring of $M$ is canonically isomorphic to that of $M^{\sigma}$ by the identity on maps, so the twisting alone does not produce an involution on the operators. The involution of the algebra is induced on the endomorphism ring of the regular module as $\sigma$ itself, under $\operatorname{End}_A(A)\cong A^{\mathrm{op}}$, and on the free module $A^n$ as the transpose-entrywise involution $\Theta(X)_{ij}=\sigma(X_{ji})$ on $M_n(A^{\mathrm{op}})$; this $\Theta$ is determined up to conjugation by a change of basis, and it is the model for the general construction. A general module carries an induced involution only when a pairing is present, and the self-conjugacy of a module produces merely an inner automorphism, which does not see the algebra involution; the pairing, the adjoint and the involution it induces on the endomorphism ring are the subjects of the two articles that follow.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity, the base ring |
| $A$ | unital associative $R$-algebra |
| $\sigma$ | involution of $A$: $\sigma^{2}=\mathrm{id}$, $\sigma(ab)=\sigma(b)\sigma(a)$ |
| $A^{\mathrm{op}}$ | opposite algebra, product $a \cdot_{\mathrm{op}} b=ba$ |
| $M$, $N$ | left $A$-modules |
| $M^{\sigma}$ | twisted module, action $a \cdot_{\sigma} m=\sigma(a)m$ |
| $f : M \to N$ | a homomorphism, also a homomorphism $M^{\sigma} \to N^{\sigma}$ |
| $\operatorname{End}_A(M) \cong \operatorname{End}_A(M^{\sigma})$ | identity on maps, an isomorphism of $R$-algebras |
| $\Theta(X)_{ij}=\sigma(X_{ji})$ | induced involution on $M_n(A^{\mathrm{op}})$ |
| $R_a$ | right multiplication, an endomorphism of ${}_A A$ |
| $u : M \to M^{\sigma}$ | a self-conjugacy, giving an inner automorphism |
| $\operatorname{End}_R(M)$ | all $R$-linear endomorphisms |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for involutions, opposite algebras and matrix algebras.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for the transpose and the opposite matrix ring.
- Israel N. Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for involutions of rings and their induced maps on matrix rings.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for the opposite algebra and involutions on matrix rings.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for involutions of the first and second kind and their behaviour under matrix extensions.
