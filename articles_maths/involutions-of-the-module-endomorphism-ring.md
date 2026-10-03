
# __Involutions of the Module Endomorphism Ring__

## Introduction

An involution of the endomorphism ring of a module is an anti-automorphism of order two, and the basic example is the adjoint with respect to a pairing. This article describes the involutions the ring $E=\operatorname{End}_A(M)$ can carry, the action of the units by conjugation on them, the fixed part of an involution — the self-adjoint operators, a Jordan algebra — and the extent to which an involution is determined by its pairing.

The article is the third of the `* Operator Theory` group of this category. It assumes the endomorphism algebra of *The Endomorphism Algebra of a Module*, the involution from a pairing of *The Involution on the Endomorphism Ring of a Module*, and the operator classes of *Module Operators with an Involution*. The classification of the involutions of a matrix algebra over a field by their symmetry type, and the hermitian forms that realise them, belong to *Hermitian Forms over an Involution Ring* and to Part II; here the involutions are described, related to pairings and sorted by their fixed parts, and the full classification is named as the next step. The article stays inside Part I: no distance, norm, positivity, topology or limit. Throughout, $R$ is a commutative ring with $1 \neq 0$ in which $2$ is invertible, $A$ is a unital associative $R$-algebra, $M$ is a left $A$-module, and $E=\operatorname{End}_A(M)$.

## Involutions of the Endomorphism Ring

### Definition and first examples

**Definition.** An **involution** of $E$ is an $R$-linear map $\theta : E \to E$ with

$$
\theta^{2}=\mathrm{id}, \qquad \theta(fg)=\theta(g)\theta(f) \qquad (f,g \in E),
$$

that is, an $R$-linear anti-automorphism of order two. The pair $(E,\theta)$ is an involutive $R$-algebra.

**Proposition.** Each of the following is an involution of the appropriate ring.

**(a)** The **identity** $\theta=\mathrm{id}$ on every commutative $E$; its fixed part is all of $E$.

**(b)** The **transpose** $\theta(X)=X^{\mathsf{T}}$ on $E=M_n(B)$ with the entrywise product, when $B$ is commutative; its fixed part is the symmetric matrices.

**(c)** The **adjoint from a pairing**, $\theta(f)=f^{*}$ on $E=\operatorname{End}_A(M)$, for $M$ with a non-degenerate reflexive $\sigma$-sesquilinear pairing, when $\sigma=\mathrm{id}$ so that the adjoint is $R$-linear (see the next section for the general case).

*Proof.* Direct verification in each case; the transpose is an anti-automorphism over a commutative coefficient ring because $(XY)^{\mathsf{T}}=Y^{\mathsf{T}}X^{\mathsf{T}}$. $\square$

For the adjoint of a $\sigma$-sesquilinear pairing the map $f \mapsto f^{*}$ is $R$-linear and anti-multiplicative, but it is an involution *of the $R$-algebra $E$* only in the sense of an involutive algebra whose base involution is $\sigma$; the kind is discussed below.

### Conjugation and isomorphism

**Definition.** Two involutions $\theta$ and $\theta'$ of $E$ are **isomorphic** when there is an $R$-algebra automorphism $\varphi$ of $E$ with

$$
\theta'=\varphi\,\theta\,\varphi^{-1}.
$$

The group $E^{\times}$ acts on the set of involutions by **inner conjugation**,

$$
(\operatorname{Ad}_u\theta)(f)=u\,\theta(f)\,u^{-1} \qquad (u \in E^{\times}),
$$

and the involutions in one orbit are inner-isomorphic.

**Proposition.** The action of $E^{\times}$ on the set of involutions is an action of the group on a set; its orbits are the inner-conjugacy classes, and $\theta$ is isomorphic to $\theta'$ exactly when $\theta'$ is in the orbit of $\theta$ under the full automorphism group $\operatorname{Aut}_{R\text{-alg}}(E)$.

*Proof.* $\operatorname{Ad}_u\operatorname{Ad}_v=\operatorname{Ad}_{uv}$ and $\operatorname{Ad}_1=\mathrm{id}$; the characterisation of isomorphism is the definition. $\square$

**Proposition.** Inner conjugation preserves the fixed part up to the conjugating automorphism: $\operatorname{Fix}(\operatorname{Ad}_u\theta)=u\operatorname{Fix}(\theta)u^{-1}$.

*Proof.* $f$ is fixed by $\operatorname{Ad}_u\theta$ exactly when $u\theta(f)u^{-1}=f$, that is $\theta(f)=u^{-1}fu$, which says $u^{-1}fu \in \operatorname{Fix}(\theta)$. $\square$

So isomorphic involutions have fixed parts of the same size, which is the first invariant that separates them.

## The Involution from a Pairing

### The construction recalled

**Proposition.** Let $\langle\cdot,\cdot\rangle$ be a non-degenerate reflexive $\sigma$-sesquilinear pairing on $M$ for which the adjoint of every endomorphism exists. Then $f \mapsto f^{*}$ is an involution of $E$ in the sense of an $R$-linear anti-automorphism of order two, and $\operatorname{Fix}({}^{*})=\operatorname{Sym}(M)$ is the set of self-adjoint operators.

*Proof.* This is *The Involution on the Endomorphism Ring of a Module*. $\square$

**Definition.** An involution of $E$ that arises this way is a **pairing involution**, and the pairing is a **realising pairing**.

The identity involution of a commutative $E$ is not a pairing involution in general, because a pairing involution has fixed part the self-adjoint operators of a non-degenerate form, which is a proper part of $E$ as soon as $M \neq 0$ and the form is non-zero; the identity involution fixes everything.

### The map from pairings to involutions

**Proposition.** The assignment $\{$pairings$\} \to \{$involutions$\}$ is:

**(i)** unchanged when the pairing is multiplied by a unit $\lambda \in R$;

**(ii)** unchanged under a change of basis;

**(iii)** not injective: two distinct pairings can induce the same involution;

**(iv)** not constant: two pairings can induce non-isomorphic involutions.

*Proof.* (i) and (ii) are the canonicality statement of *The Involution on the Endomorphism Ring of a Module*. (iii) holds because scaling is a nontrivial change of pairing leaving the involution fixed. (iv) is the example below. $\square$

**Example.** On $M=k^2$ the standard symmetric pairing has Gram matrix $I$ and induces the transpose, with fixed part of dimension $3$; the alternating pairing has Gram matrix $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ and induces $T\mapsto J^{-1}T^{\mathsf{T}}J$, whose fixed part is the scalars, of dimension $1$. The two fixed parts have different dimensions, hence the two involutions are not isomorphic and the map is not constant.

### The fixed part

**Theorem.** Let $\theta$ be a pairing involution. Then

$$
\operatorname{Fix}(\theta)=\operatorname{Sym}(M)
$$

is an $R$-submodule closed under the Jordan product $f\bullet g=\frac12(fg+gf)$ and under the square, and containing the identity. It is a unital special Jordan subalgebra of $E$.

*Proof.* This is *Module Operators with an Involution*. $\square$

**Proposition.** The fixed part satisfies $E=\operatorname{Fix}(\theta)\oplus\operatorname{Fix}(-\theta)$, where $-\theta$ is the involution $f \mapsto -\theta(f)$ and its fixed part is $\operatorname{Skew}(M)$; hence the involution is recovered from its fixed part together with the skew part. Two involutions with the same fixed part are equal when $2$ is invertible.

*Proof.* For every $f$, the decomposition $f=\frac12(f+\theta f)+\frac12(f-\theta f)$ exhibits $E$ as the sum of the two fixed parts, and the intersection is zero because $2$ is invertible; if two additive maps of order two have the same fixed part then they agree, since $f+\theta f=2f$ determines $\theta f=f$ on the fixed part and $\theta f=-f$ on the other summand. $\square$

Thus an involution of $E$ is exactly a direct-sum decomposition $E=P\oplus Q$ with $1 \in P$ and the property of being an anti-automorphism, encoded by the projections $\frac12(\mathrm{id}\pm\theta)$.

### The self-adjoint squares and the pairing

**Proposition.** For a pairing involution and $f \in E$ the operators $f^{*}f$ and $ff^{*}$ are self-adjoint, and $f$ is unitary exactly when both are the identity. Hence the fixed part determines the unitary group, $U(M)=\{f : f^{*}f=ff^{*}=\mathrm{id}\}$, but different involutions can have isomorphic — even equal-dimensional — fixed parts and different unitary groups.

*Proof.* The self-adjointness and the unitary characterisation are *Module Operators with an Involution*; the last clause is a warning, since the unitary group is defined by the involution and not by the isomorphism class of the fixed part alone. $\square$

## The Identity and the Exchange

### Two extreme involutions

The notion of an involution is wider than the notion of an adjoint of a pairing, and the simplest way to exhibit two inequivalent involutions is to look at a commutative endomorphism ring.

**Proposition.** On $E=F\times F$ with the componentwise product, the **identity** $\mathrm{id}$ and the **exchange** $\theta(x,y)=(y,x)$ are involutions. Their fixed parts are $E$ and the diagonal $\Delta=\{(x,x)\}\cong F$, of dimensions $2$ and $1$, so the two involutions are not isomorphic.

*Proof.* Both maps are $F$-linear anti-automorphisms of order two, because the product is componentwise and commutative. The fixed parts are read off, and an isomorphism of involutions carries the fixed part of one onto the fixed part of the other, so it preserves its dimension. $\square$

### The classification problem

**Definition.** An involution $\theta$ of $E$ is **adjointable** when there is a non-degenerate reflexive pairing on $M$ whose adjoint involution is $\theta$. Every pairing involution is adjointable by definition, and the map from pairings to involutions is described in the section above.

**Proposition.** Adjointability is not an isomorphism invariant at first sight, and the fixed part alone does not decide it: two involutions with fixed parts of the same dimension may be realised by pairings or not, and an involution isomorphic to an adjointable one is adjointable because an algebra automorphism carries a pairing to a pairing.

*Proof.* The last clause is the definition of isomorphism of involutions transported through the adjoint; the first is the warning that neither the fixed-part dimension nor the kind determines adjointability without further structure. $\square$

The general question — which involutions of an endomorphism ring are adjointable, and how many inequivalent pairings realise a given one — is the classification problem of the involutions of a ring acting on a module. Over a field it becomes the classification of bilinear and sesquilinear forms up to equivalence, which is *Hermitian Forms over an Involution Ring* and Part II, and it is not solved here; the identity and the exchange above show that the class of involutions is strictly larger than the class of pairing involutions whenever a pairing realisation does not exist.

## The Kind and the Centre

### The induced involution on the centre

**Proposition.** Every involution $\theta$ of $E$ restricts to an involution, in fact an automorphism of order two, of the centre $Z(E)$; the involution is of the **first kind** when this restriction is the identity and of the **second kind** otherwise.

*Proof.* For $z \in Z(E)$ and $f \in E$, $\theta(z)f=\theta(z)\theta(\theta^{-1}(f))=\theta(\theta^{-1}(f)\,z)=\theta(z\,\theta^{-1}(f))=f\,\theta(z)$, where the second equality uses $\theta(a)\theta(b)=\theta(ba)$ and the third the centrality of $z$; hence $\theta(z)$ is central. So $\theta$ maps $Z(E)$ into itself, and it is an anti-automorphism of order two of the commutative ring $Z(E)$, that is an automorphism of order two. $\square$

**Corollary.** A pairing involution induced by $\sigma$ restricts to $\sigma$ on the scalars, so it is of the first kind exactly when $\sigma$ fixes the centre of $E$, which for the regular module means $\sigma$ fixes $Z(A)$.

*Proof.* Combine the proposition with the identification of the involution on the regular module. $\square$

### The centre and the isomorphism type

**Proposition.** Isomorphic involutions induce conjugate automorphisms of the centre; consequently the first-kind and second-kind classes are isomorphism invariants, and within one kind the fixed part of the centre is an invariant.

*Proof.* An isomorphism $\varphi$ carries $Z(E)$ into $Z(E)$ and intertwines the two restrictions. $\square$

## Examples

**(a) The matrix algebra.** On $E=M_n(F)$ over a field, the transpose is the pairing involution of the standard symmetric form, with fixed part of dimension $n(n+1)/2$, while the symplectic involution of the standard alternating form has fixed part of dimension $1$ for $n=2$; the two fixed parts have different dimensions for $n \geq 2$, so the corresponding involutions are non-isomorphic.

**(b) The regular module.** For $M={}_A A$ the pairing involution is $\sigma$ on $E\cong A^{\mathrm{op}}$, of the second kind exactly when $\sigma$ moves $Z(A)$.

**(c) A commutative endomorphism ring.** For $E=F\times F$ the identity and the exchange are two non-isomorphic involutions: the identity has fixed part of dimension $2$ and is of the first kind, while the exchange has fixed part of dimension $1$ and is of the second kind, since it swaps the two central idempotents.

**(d) The quaternions.** For $E=\mathbb{H}^{\mathrm{op}}\cong\mathbb{H}$ with the conjugation involution, the fixed part is $\mathbb{R}$, the involution is of the first kind, and the unitary group is the three-sphere of unit quaternions.

## Summary

An involution of $E=\operatorname{End}_A(M)$ is an $R$-linear anti-automorphism of order two; the identity, the transpose of a matrix ring and the adjoint of a pairing are the basic examples. The units act by inner conjugation and the automorphism group by conjugation, and isomorphic involutions have fixed parts of the same size. The involution induced by a non-degenerate reflexive pairing has fixed part the self-adjoint operators, a unital special Jordan subalgebra closed under the Jordan product $\frac12(fg+gf)$, and $E$ is the direct sum of the fixed part and the fixed part of $-\theta$, the skew-adjoint operators, when $2$ is invertible; an involution is determined by its fixed part. The map from pairings to involutions is unchanged by scaling and by change of basis, is not injective and is not constant: on $k^2$ the symmetric and the alternating form give fixed parts of dimensions $3$ and $1$, hence non-isomorphic involutions. The identity and the exchange involutions of $F\times F$ have fixed parts of dimensions $2$ and $1$ and are of the first and second kind respectively; deciding which involutions are adjointable, and by which pairings, is the classification problem, which over a field is the theory of forms and is deferred. Every involution restricts to an involution of the centre, and the first- or second-kind dichotomy is an isomorphism invariant. The classification of the adjointable involutions and of the pairings realising them is the theory of hermitian forms, *Hermitian Forms over an Involution Ring*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E=\operatorname{End}_A(M)$ | the endomorphism ring of the module |
| $\theta$ | an involution of $E$, $R$-linear, order two, anti-multiplicative |
| $\operatorname{Fix}(\theta)$ | the fixed part, $\{f : \theta(f)=f\}$ |
| $\operatorname{Ad}_u\theta$ | inner conjugation, $f\mapsto u\theta(f)u^{-1}$ |
| $f^{*}$ | the adjoint of a pairing, a pairing involution |
| $\operatorname{Sym}(M)$, $\operatorname{Skew}(M)$ | fixed parts of ${}^{*}$ and of $-{}^{*}$ |
| first kind, second kind | the restriction of $\theta$ to $Z(E)$ is the identity or not |
| $J$ | the Gram matrix of the alternating form on $k^2$ |
| adjointable | arising as the adjoint of a non-degenerate reflexive pairing |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for involutions, forms and the unitary groups they define.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for involutions of matrix rings and the transpose.
- Israel N. Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for involutions of rings, their kinds and their fixed parts.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the classification of involutions and the forms realising them.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for ring involutions, their first and second kinds, and examples.
