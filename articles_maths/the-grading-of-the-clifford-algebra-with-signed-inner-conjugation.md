# __The Grading of the Clifford Algebra with Signed Inner Conjugation__

## Introduction

The **signed inner conjugation** $\mathrm{Ad}^{\alpha}_x(y)=\alpha(x)\,y\,x^{-1}$ is not a second structure beside the inner conjugation, and the geometric layer does not need a second copy of the algebra. It is the same conjugation read on a $\mathbb{Z}/2$-graded algebra, and the grading carries the whole difference. Two facts make this precise. The first is that the sign is entirely in the grade involution, $\alpha(x)=\varepsilon_x\,x$ with $\varepsilon_x=(-1)^{k}$ on the degree-$k$ part, so the two operators agree on the even part of the algebra and differ by $-1$ on the odd part. The second, and the one that settles the question of independence, is that the composition of two signed conjugations is a signed conjugation by the product,

$$
\mathrm{Ad}^{\alpha}_x\circ\mathrm{Ad}^{\alpha}_z=\mathrm{Ad}^{\alpha}_{xz},
$$

and when $x$ and $z$ are both odd the product $xz$ is even, so the composite is an **ordinary** inner conjugation: the two minus signs cancel. What is needed is the full graded algebra $\mathrm{Cl}(V,q)=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, not the even subalgebra $\mathrm{Cl}^0$ alone, and not two independent copies of $\mathrm{Cl}^0$.

The two components play distinct roles and are tied together by the multiplication. The even part carries the spin group, the rotations and the ordinary sandwich; the odd part carries the reflections and the twist, and it is not an independent copy, because it is a single coset of the even part inside the pin group and is generated from it by multiplication by one odd unit. Two independent copies of $\mathrm{Cl}^0$ would lose the rule odd $\times$ odd $=$ even, the action of the odd elements on $V$ and the relation between the two sectors, which is exactly the structure the pin group is made of.

The Clifford algebra, its parity grading and the grade involution are from *Clifford Algebras* and *Clifford Algebras in Finite Dimensions*. The general two-sided family is *Two-Sided Operators on a Clifford Algebra*; the operator, its sign, its kernel and its action on $V$ are *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*; the one-sided factors and their conjugation form are *One-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*; the groups $\Gamma$, $\mathrm{Pin}$, $\mathrm{Spin}$, the Clifford norm, the exact sequences and Cartan–Dieudonné are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the chirality of a module and the parity of a minimal left ideal are *Pin Representations and Clifford Modules with Signed Inner Conjugation* and *Spinors as Minimal Left Ideals with Signed Inner Conjugation*. Nothing owned by those entries is re-derived. The base is a field $F$ of characteristic not $2$, with $q$ a non-degenerate quadratic form on the finite-dimensional space $V$ and $B$ its polar form.

## The Grading and the Sign

**Given.** The algebra is graded by parity, $\mathrm{Cl}(V,q)=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, with $\mathrm{Cl}^i\mathrm{Cl}^j\subseteq\mathrm{Cl}^{i+j}$, the exponent read modulo two:

$$
\text{even}\cdot\text{even}=\text{even},\quad
\text{even}\cdot\text{odd}=\text{odd},\quad
\text{odd}\cdot\text{even}=\text{odd},\quad
\text{odd}\cdot\text{odd}=\text{even}.
$$

The grade involution $\alpha$ fixes the even part and negates the odd part, so on a homogeneous element of degree $k$ one has $\alpha(x)=\varepsilon_x\,x$ with $\varepsilon_x=(-1)^{k}$.

**Proposition (the sign is the parity).** $\mathrm{Ad}^{\alpha}_x=\varepsilon_x\,\mathrm{Ad}_x$ for every homogeneous unit $x$. Hence the two operators agree on the even part of the algebra and differ by $-1$ on the odd part, and both preserve the parity grading.

*Proof.* The grade involution is a central scalar on each homogeneous component, $\alpha(x)=\varepsilon_xx$ with $\varepsilon_x$ central; substituting into the definition of the signed inner conjugation gives the first claim, and the second is the parity preservation of $\mathrm{Ad}^{\alpha}_x$ and of $\mathrm{Ad}_x$. This is the parity-sign proposition of *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*.

**Remark.** The signs belong to the components, not to the operators: the even part is the fixed locus of $\alpha$, where no sign can appear, and the odd part is the locus on which $\alpha$ is $-1$, where the sign must appear. Every statement of this article is that one table read at some level.

## The Composition of Two Signed Conjugations

**Proposition (cancellation).** For units $x,z$ one has

$$
\mathrm{Ad}^{\alpha}_x\circ\mathrm{Ad}^{\alpha}_z=\mathrm{Ad}^{\alpha}_{xz},
$$

and if $x$ and $z$ are both odd then $xz$ is even, hence $\mathrm{Ad}^{\alpha}_{xz}=\mathrm{Ad}_{xz}$. **The composite of two signed conjugations is an ordinary inner conjugation.**

*Proof.* The composition law is the one of the family; for the second statement, the product of two odd elements is even by the grading table, and on an even element the grade involution is the identity, so the signed and the ordinary member coincide.

**The parity table of the composites.** Writing $\varepsilon_x,\varepsilon_z\in\{\pm1\}$ for the parities, $\mathrm{Ad}^{\alpha}_x\mathrm{Ad}^{\alpha}_z=\varepsilon_x\varepsilon_z\,\mathrm{Ad}_{xz}$, so the composite is signed exactly when one of the two elements is odd and the other even, and ordinary exactly when the two have the same parity.

| $x$ | $z$ | $xz$ | composite |
|---|---|---|---|
| even | even | even | ordinary, $\mathrm{Ad}_{xz}$ |
| even | odd | odd | signed, $-\mathrm{Ad}_{xz}$ |
| odd | even | odd | signed, $-\mathrm{Ad}_{xz}$ |
| odd | odd | even | ordinary, $\mathrm{Ad}_{xz}$ |

**Corollary (the square of an odd sign is ordinary).** If $x$ is odd then $x^{2}$ is even and

$$
\bigl(\mathrm{Ad}^{\alpha}_x\bigr)^{2}=\mathrm{Ad}^{\alpha}_{x^{2}}=\mathrm{Ad}_{x^{2}} .
$$

So a signed conjugation by an odd element is never an involution of the signed kind: its square has forgotten the sign.

**Corollary (one odd operator generates the odd family).** Fix an odd unit $u$. Every odd unit is $x=us$ with $s=u^{-1}x$ even, hence

$$
\mathrm{Ad}^{\alpha}_x=\mathrm{Ad}^{\alpha}_u\circ\mathrm{Ad}^{\alpha}_s .
$$

So the whole family of signed conjugations is generated by the ordinary conjugations together with the single signed conjugation by $u$. There is no second independent family: the odd part contributes one operator and its products with the even operators.

**Remark.** The corollary is the operator form of the statement that one graded structure suffices. The group of induced maps is generated by the images of the even units and one odd image, and in the language of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* the corresponding group-theoretic fact is that the odd part of the pin group is a coset, which is the next section.

## The Odd Part of Pin is a Coset, Not a Subgroup

**Proposition.** Let $\Gamma(V,q)$ be the Clifford group and let $\Gamma^0=\Gamma(V,q)\cap\mathrm{Cl}^0$ and $\Gamma^1=\Gamma(V,q)\cap\mathrm{Cl}^1$ be its even and odd parts. Then $\Gamma^0$ is a subgroup of index at most two, and if $\Gamma^1$ is non-empty it is a single coset,

$$
\Gamma^1=x\,\Gamma^0=\Gamma^0x,\qquad x\in\Gamma^1 \text{ any}.
$$

The same statements hold for $\mathrm{Pin}(V,q)$ and for $\mathrm{Spin}(V,q)=\mathrm{Pin}(V,q)\cap\mathrm{Cl}^0$.

*Proof.* The even part is closed under multiplication and inversion because the grading is multiplicative and the inverse of an even element is even; it is a subgroup. If $x$ is odd and $s$ even then $xs$ and $sx$ are odd, so $x\Gamma^0\subseteq\Gamma^1$ and $\Gamma^0x\subseteq\Gamma^1$; conversely an odd $y$ is $y=x\,(x^{-1}y)$ with $x^{-1}y$ even, giving $\Gamma^1\subseteq x\Gamma^0$ and similarly on the other side. The statements for the pin group are the restrictions to the norm-one slice, and the spin group is its even part.

**Corollary (the two minuses cancel, at the level of the group).** The product of two odd elements of $\mathrm{Pin}$ lies in $\mathrm{Spin}$; the product of an odd and an even element is odd. So the odd part is stable under multiplication by $\mathrm{Spin}$ but not closed under multiplication by itself, and

$$
\mathrm{Pin}(V,q)=\mathrm{Spin}(V,q)\ \sqcup\ (\text{odd coset}),\qquad \mathrm{Pin}/\mathrm{Spin}\cong\mathbb{Z}/2
$$

whenever the odd part is non-empty, which over $\mathbb{R}$ always holds since the norm of a vector $N(u)=-q(u)$ takes the value $\pm1$ after rescaling. The odd part is therefore a coset, and it is the coset that carries the reflections; a second group is not needed to describe them.

**Corollary (the images of the two components).** Let $x\in\Gamma(V,q)$ and let $k$ be the parity of $x$. Writing $x$ as a product of $k$ vectors gives $\mathrm{Ad}^{\alpha}_x$ as a product of $k$ reflections, so

$$
\det\mathrm{Ad}^{\alpha}_x=(-1)^{k}=\varepsilon_x ,
$$

and the even part of the group maps into $SO(V,q)$ while the odd part maps into its complement. The reflection $\rho_u=\mathrm{Ad}^{\alpha}_u$ is the image of an odd element, and it is the composite of two odd images that lands back in $SO$.

*Proof.* The group is generated by the non-isotropic vectors it contains; for a vector $u$ the operator $\mathrm{Ad}^{\alpha}_u$ is the reflection $\rho_u$, of determinant $-1$; the determinant is multiplicative, so a product of $k$ reflections has determinant $(-1)^{k}$. The parity statement follows.

## The Two Components as Even Modules

The odd part is not a second algebra, and the precise sense in which the algebra looks like "two copies" is a module-theoretic one.

**Proposition.** Let $e\in V$ with $q(e)\neq0$, so that $e$ is an odd unit. Then left multiplication by $e$ maps the even part onto the odd part and the odd part onto the even part, and the Clifford algebra is a free left module of rank two over its even subalgebra,

$$
\mathrm{Cl}(V,q)=\mathrm{Cl}^0\oplus\mathrm{Cl}^1=\mathrm{Cl}^0\cdot 1\ \oplus\ \mathrm{Cl}^0\cdot e ,
$$

with basis $\{1,e\}$. Right multiplication by $e$ is an isomorphism of left $\mathrm{Cl}^0$-modules $\mathrm{Cl}^0\to\mathrm{Cl}^1$.

*Proof.* Multiplication by an odd element shifts the parity, $e\,\mathrm{Cl}^i\subseteq\mathrm{Cl}^{i+1}$; it is a bijection because $e$ is invertible, with inverse left multiplication by $e^{-1}$, so $e\,\mathrm{Cl}^0=\mathrm{Cl}^1$ and $e\,\mathrm{Cl}^1=\mathrm{Cl}^0$. Every element is $x=x_0+x_1$ with $x_i\in\mathrm{Cl}^i$, and $x_1=(x_1e^{-1})e$ with $x_1e^{-1}\in\mathrm{Cl}^0$, so $\mathrm{Cl}^1\subseteq\mathrm{Cl}^0e$ and the sum is direct on parity; hence $\{1,e\}$ is a basis over $\mathrm{Cl}^0$. For the last statement, right multiplication $y\mapsto ye$ is $\mathrm{Cl}^0$-linear on the left, $(ay)e=a(ye)$, and carries $\mathrm{Cl}^0$ bijectively onto $\mathrm{Cl}^1$.

**Remark (the copies are not independent).** The two summands are isomorphic as modules over the even subalgebra, but the isomorphism is multiplication by the odd unit $e$, and the multiplication of the two summands with each other is not the multiplication of two independent copies: it is the graded multiplication, with odd $\times$ odd $=$ even. The decomposition records that the algebra is a rank-two module over its even part, not that the two components can be separated.

**Corollary (the same on the module of the representation).** Let $S$ be a Clifford module with its parity splitting $S=S^0\oplus S^1$, and let $I$ be a minimal left ideal with its splitting $I=I^0\oplus I^1$ of *Spinors as Minimal Left Ideals with Signed Inner Conjugation*. Then the even part of the algebra preserves each summand and the odd part interchanges the two, in both cases. This is the chirality statement of *Pin Representations and Clifford Modules with Signed Inner Conjugation*, seen on the two examples.

## Why Two Independent Copies Fail

Suppose one tried to replace the graded algebra by two independent copies $A,B\cong\mathrm{Cl}^0$ and to build the pin group as the disjoint union $A\sqcup B$. Each of the structures that the geometric layer uses is then lost.

- **The multiplication rule.** In the graded algebra the product of two odd elements is even, and it is an element of the algebra; in two copies the product of two elements of $B$ has nowhere to live, and the group law of $\mathrm{Pin}$, which mixes the components by the rule odd $\cdot$ odd $\in\mathrm{Spin}$, cannot be stated.
- **The action on $V$.** The reflection $\rho_u=\mathrm{Ad}^{\alpha}_u$ needs the odd element $u$ and the twist $\alpha$ in the left factor; an element of an independent copy $B$ has no action on $V$ and no relation to $\alpha$.
- **The twist itself.** The grade involution is defined by the degree, that is by the position of an element in the two components; without the grading there is no $\alpha$, and therefore no distinction between the inner conjugation and the signed one.
- **The relation between the sectors.** $\mathrm{Pin}/\mathrm{Spin}\cong\mathbb{Z}/2$ says that the odd part is a coset, that is, that every odd element is the product of the fixed odd unit $u$ with an element of $\mathrm{Spin}$; a disjoint union of two copies has no such relation and no quotient.

**Remark (one graded algebra).** The correct structure is a single $\mathbb{Z}/2$-graded algebra — a superalgebra — with the grading part of the structure and not a piece of notation: $\mathrm{Cl}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$ and $\mathrm{Cl}^i\mathrm{Cl}^j\subseteq\mathrm{Cl}^{i+j}$. The pin group is the group of invertible elements of norm $\pm1$ in this algebra, its even subgroup is the spin group, and the odd part is a coset. In the language of physics the even elements are bosonic, the odd ones fermionic, the grading is the fermion parity, and a structure that mixes the two components is stated with the grading built in; without the grading the mixing cannot even be written. The biquaternion case of that reading, where the ambient algebra is the Dirac algebra, the twist is the conjugation by the volume element and the supercharge is an odd generator, is *The Graded Algebra, Fermion Parity and the Two Sectors with Signed Inner Conjugation in Biquaternionic Form* and *The Superalgebra Reading and the Odd Extension with Signed Inner Conjugation in Biquaternionic Form* in the physics corpus.

### The Parity Grading Against the Multi-vector Refinement

The parity grading is the coarsest one, and it is the one this article uses. The finer **multi-vector decomposition** $\mathrm{Cl}=\bigoplus_k\mathrm{Cl}^k$ is also standard, and it is worth recording why the two are not on the same footing.

- **The parity grading is intrinsic.** The grade involution $\alpha$ is an algebra automorphism defined by the parity alone, with no extra data; every algebra automorphism of $\mathrm{Cl}$ that comes from an isometry of $V$ preserves it, and it is the grading of every Clifford algebra at once.
- **The multi-vector refinement depends on a frame.** A $\mathbb{Z}$-grading of $\mathrm{Cl}$ into degrees is fixed by a choice of an orthonormal basis of $V$, hence by an orthogonal decomposition of $V$ into lines; the parity involution is the comparison $\text{even}/\text{odd}$ of **any** such decomposition, and it is the part that survives the choice. A different decomposition of $V$ need not preserve a given finer grading.

The consequence, noted by Fauser in the paper this pair of articles draws from, is that "the $\mathbb{Z}_n$-grading used to define multi-vectors is not a feature of Clifford algebra" and that "different $\mathbb{Z}_n$-gradings can produce quite different spinor modules". The multi-vector degree is therefore a convention attached to a frame, while the parity is structure; the signed inner conjugation, whose whole difference from the inner one is the parity sign $\varepsilon_x$, is built on the intrinsic grading and is for that reason canonical.

**Remark (the corpus's grade decomposition).** The corpus also uses the finer grading — the grade decomposition of the geometric product in *The Geometric Product and the Grade Decomposition*, and the Clifford algebra's grading in *Clifford Algebras in Finite Dimensions* — and there the parity is the reduction of the grade modulo two. The two readings coexist: this article's parity is the canonical half of the fine grading, and the fine grading is recovered from it together with the frame. The point recorded here is only that the half is intrinsic and the fine grading is not, which is why the sign of the signed inner conjugation can be defined for every Clifford algebra without mentioning a frame.

## The Two Maps Compared

The two operators come from the same group and differ only by the parity sign, and the sign acquires a global effect on the determinant because the parity of the dimension enters.

**Proposition.** For $x\in\Gamma(V,q)$ of parity $k$, $\det\mathrm{Ad}^{\alpha}_x=\varepsilon_x$, while

$$
\det\mathrm{Ad}_x=(\varepsilon_x)^{n+1}=
\begin{cases}
\varepsilon_x, & n \text{ even},\\[2pt]
+1, & n \text{ odd},
\end{cases}
\qquad n=\dim V .
$$

Hence for $n$ even the inner conjugation and the signed inner conjugation reach the same two cosets of $SO(V,q)$ in $O(V,q)$, and for $n$ odd the inner conjugation maps the whole Clifford group into $SO(V,q)$ and misses every improper isometry, while the signed inner conjugation still reaches them all.

*Proof.* $\mathrm{Ad}_x=\varepsilon_x\mathrm{Ad}^{\alpha}_x$ by the parity-sign proposition, so on an $n$-dimensional space $\det\mathrm{Ad}_x=(\varepsilon_x)^{n}\det\mathrm{Ad}^{\alpha}_x=(\varepsilon_x)^{n+1}$, and the previous section gives $\det\mathrm{Ad}^{\alpha}_x=\varepsilon_x$.

**Remark.** In odd dimension the inner conjugation therefore does not merely have too large a kernel; its image is proper in $O(V,q)$, and no inner conjugation is an improper isometry. The signed version is the one whose image is the full orthogonal group, and its kernel on the pin group is $\{\pm1\}$; both statements are the reason the geometric layer is built on the signed member.

## Worked Cases

### Two Odd Steps Give an Ordinary Step

In $\mathrm{Cl}_{0,3}(\mathbb{R})$ with $e_j^{2}=-1$, let $u=e_1$ and $w=e_2$, both odd. Then

$$
\mathrm{Ad}^{\alpha}_{e_1}=\rho_{e_1},\qquad \mathrm{Ad}^{\alpha}_{e_2}=\rho_{e_2},
$$

and the composite is

$$
\mathrm{Ad}^{\alpha}_{e_1}\circ\mathrm{Ad}^{\alpha}_{e_2}=\mathrm{Ad}^{\alpha}_{e_1e_2}=\mathrm{Ad}_{e_1e_2},
$$

the last equality because $e_1e_2$ is even. The element $e_1e_2$ has norm one and acts by

$$
\mathrm{Ad}_{e_1e_2}(e_1)=-e_1,\qquad \mathrm{Ad}_{e_1e_2}(e_2)=-e_2,\qquad \mathrm{Ad}_{e_1e_2}(e_3)=e_3 ,
$$

the half-turn of the plane $\mathrm{span}(e_1,e_2)$, of determinant $+1$. Two signed reflections, each of determinant $-1$, have composed into one ordinary rotation: this is the cancellation of the two minus signs, computed.

### The Central Odd Element

In the same algebra the volume element $\omega=e_1e_2e_3$ is odd, central and satisfies $\omega^{2}=1$, and its norm is $N(\omega)=\omega\bar\omega=\omega^{2}=1$, so $\omega\in\mathrm{Pin}$. Its two images are

$$
\mathrm{Ad}_{\omega}=\mathrm{id},\qquad \mathrm{Ad}^{\alpha}_{\omega}=-\mathrm{id},
$$

by the parity-sign proposition, and $-\mathrm{id}$ has determinant $(-1)^{3}=-1$, an improper isometry, in agreement with $\varepsilon_\omega=-1$ and with the odd part mapping into the complement of $SO$. Under the inner conjugation the odd element $\omega$ is the identity, which is the failure recorded in *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*; under the signed inner conjugation it is the nontrivial element of the odd coset. The two statements are the same parity sign.

### The Rank-Two Decomposition

In $\mathrm{Cl}_{0,3}(\mathbb{R})$ the even part is $\mathrm{Cl}^0=\mathrm{span}\{1,e_2e_3,e_3e_1,e_1e_2\}$, of dimension four, and with $e=e_1$ one has

$$
\mathrm{Cl}^1=\mathrm{span}\{e_1,e_1e_2e_3,e_2,e_3\}=\mathrm{Cl}^0e_1=\mathrm{Cl}^0e ,
$$

so the algebra is free of rank two over $\mathrm{Cl}^0$ with basis $\{1,e_1\}$, and right multiplication by $e_1$ is the isomorphism $\mathrm{Cl}^0\to\mathrm{Cl}^1$ of left $\mathrm{Cl}^0$-modules. The odd component is thus obtained from the even one by one multiplication, which is the precise sense in which it is not an independent copy.

## Summary

The **signed inner conjugation** is not an independent structure beside the inner conjugation; it is the same conjugation on the graded algebra $\mathrm{Cl}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, differing from it by the parity sign $\varepsilon_x=(-1)^{k}$, so that the two agree on the even part and differ on the odd part. The composition law

$$
\mathrm{Ad}^{\alpha}_x\circ\mathrm{Ad}^{\alpha}_z=\mathrm{Ad}^{\alpha}_{xz}
$$

gives the cancellation that settles the question: for $x$ and $z$ both odd the product $xz$ is even, so the composite is the **ordinary** inner conjugation $\mathrm{Ad}_{xz}$; the composite is signed exactly when the two elements have opposite parities. Consequently the square of a signed conjugation by an odd element is ordinary, and the whole family is generated by the ordinary conjugations together with the signed conjugation by any single odd unit.

The group-theoretic form of the same fact is that the odd part of the pin group is a **coset**, $\mathrm{Pin}=\mathrm{Spin}\sqcup(\text{odd coset})$ and $\mathrm{Pin}/\mathrm{Spin}\cong\mathbb{Z}/2$ whenever it is non-empty: the product of two odd elements is even, the odd part is not a subgroup, and the reflections are carried by that coset. The algebra is a free rank-two module over its even subalgebra with basis $\{1,e\}$ for an odd unit $e$, and right multiplication by $e$ identifies the two components as left $\mathrm{Cl}^0$-modules — so the two components are isomorphic but not independent, the identification being multiplication by an odd element. Two independent copies of $\mathrm{Cl}^0$ would lose the rule odd $\times$ odd $=$ even, the action of the odd elements on $V$, the twist and the relation between the sectors; one $\mathbb{Z}/2$-graded algebra, with the grading as part of the structure, suffices.

Finally, the parity sign has a global effect on the images: $\det\mathrm{Ad}^{\alpha}_x=\varepsilon_x$, while $\det\mathrm{Ad}_x=(\varepsilon_x)^{n+1}$, which is $\varepsilon_x$ for even $n$ and $+1$ for odd $n$. In odd dimension the inner conjugation maps the whole Clifford group into $SO(V,q)$ and misses every improper isometry, whereas the signed inner conjugation reaches all of $O(V,q)$; in even dimension the two reach the same two cosets, and it is the kernel, $\{\pm1\}$ against a larger group, that distinguishes them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Cl}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$ | Parity grading, the structure the geometric layer needs |
| $\mathrm{Cl}^i\mathrm{Cl}^j\subseteq\mathrm{Cl}^{i+j}$ | Multiplicativity of the grading; odd $\cdot$ odd $=$ even |
| $\alpha(x)=\varepsilon_xx$, $\varepsilon_x=(-1)^{k}$ | Grade involution, the parity sign |
| $\mathrm{Ad}^{\alpha}_x=\varepsilon_x\mathrm{Ad}_x$ | Signed inner conjugation against the inner conjugation |
| $\mathrm{Ad}^{\alpha}_x\mathrm{Ad}^{\alpha}_z=\mathrm{Ad}^{\alpha}_{xz}$ | Composition law; ordinary composite for two odd elements |
| $(\mathrm{Ad}^{\alpha}_x)^{2}=\mathrm{Ad}_{x^{2}}$ | Square of an odd sign |
| $\Gamma^0$, $\Gamma^1$, $\mathrm{Pin}=\mathrm{Spin}\sqcup(\text{odd coset})$ | The even subgroup and the odd coset |
| $\mathrm{Pin}/\mathrm{Spin}\cong\mathbb{Z}/2$ | The quotient, when the odd part is non-empty |
| $\det\mathrm{Ad}^{\alpha}_x=\varepsilon_x$ | Parity of the reflection length |
| $\det\mathrm{Ad}_x=(\varepsilon_x)^{n+1}$ | $\varepsilon_x$ for even $n$, $+1$ for odd $n$ |
| $\mathrm{Cl}=\mathrm{Cl}^0\oplus\mathrm{Cl}^0e$, $e$ odd unit | Free rank-two module over the even subalgebra, basis $\{1,e\}$ |
| $R_e:\mathrm{Cl}^0\to\mathrm{Cl}^1$ | Isomorphism of left $\mathrm{Cl}^0$-modules, the two components identified |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the parity grading, the pin and spin groups and the parity of an odd element.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the two conjugations of a graded algebra, their determinants and their images in the orthogonal group.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the chirality splitting of the spinor module and the action of the odd part upon it.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the graded structure of a Clifford algebra and its intrinsic involutions.
- Nicolas Bourbaki, *Algèbre*, Chapitre 9, *Formes sesquilinéaires et formes quadratiques* (Hermann, 1959), for the Clifford algebra as a graded algebra over its even part and the structure of its group of units.
- Bertfried Fauser, "On the equivalence of Daviau's space Clifford algebraic, Hestenes' and Parra's formulations of (real) Dirac theory," arXiv:hep-th/9908200, 1999, §3–4, for the observation that the $\mathbb{Z}_n$-grading used to define multi-vectors is not a feature of Clifford algebra and that different $\mathbb{Z}_n$-gradings can produce different spinor modules; the source of the subsection on the parity grading against the multi-vector refinement.
