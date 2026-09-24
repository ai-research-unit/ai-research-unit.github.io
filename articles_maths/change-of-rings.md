
# __Change of Rings__

## Introduction

A homomorphism of algebras relates the module categories of its source and its target, and the three functors that do the relating — **restriction**, **extension** and **coextension of scalars** — form an adjoint triple. Restriction forgets the larger algebra, extension changes the scalars along the homomorphism, and coextension forms a hom module; the two adjunctions between them are Frobenius reciprocity in the abstract form used throughout representation theory. The purpose of this article is to develop the triple, to identify exactly when extension preserves exactness (the flatness condition), and to record the behaviour of flatness under change of rings over a noncommutative base.

The conventions are those of *Modules over an Algebra*: $R$ is a commutative ring with identity, $A$ and $B$ are unital associative $R$-algebras, and $\varphi: A \to B$ is a unital $R$-algebra homomorphism. A left $A$-module is written ${}_A M$ and a right $A$-module $M_A$. The balanced product and the tensor–hom adjunction are those of the companion article *The Balanced Product over an Algebra*; the flatness theory of the commutative case is in *Modules* §13, and the present treatment is the noncommutative generalisation. Morita equivalence, with which flatness is compatible, is treated in *Morita Equivalence*.

The plan is as follows. Restriction of scalars is defined first, because it is the simplest and is always exact. Extension and coextension are then constructed from the bimodule structure that $\varphi$ induces on $B$, and the two adjunctions are read off from the tensor–hom adjunction. The middle sections treat base change of algebras and the special case of a quotient. Flatness over a noncommutative ring is defined and its one-sided character is explained, and the article closes with the change-of-rings theorems for flatness and with the group-algebra case, where extension and coextension are induction and coinduction.

## Restriction of Scalars

### Definition

Let $\varphi: A \to B$ be a unital $R$-algebra homomorphism. Every left $B$-module $N$ becomes a left $A$-module by

$$
a \cdot n = \varphi(a) n, \qquad a \in A,\ n \in N.
$$

The axioms follow immediately from the homomorphism properties of $\varphi$: $\varphi(a+a')=\varphi(a)+\varphi(a')$, $\varphi(aa')=\varphi(a)\varphi(a')$, $\varphi(1_A)=1_B$, and the $B$-module axioms. The resulting functor

$$
\operatorname{Res}_\varphi : \operatorname{Mod}(B) \longrightarrow \operatorname{Mod}(A)
$$

is **restriction of scalars**. It fixes the underlying abelian group and the maps, so it is faithful and injective on hom-sets:

$$
\operatorname{Hom}_B(N,N') \subseteq \operatorname{Hom}_A(\operatorname{Res}_\varphi N, \operatorname{Res}_\varphi N'), \qquad \operatorname{Res}_\varphi \text{ on morphisms is the identity inclusion.}
$$

The inclusion can be strict: $B$-linear maps are $A$-linear, since $f(\varphi(a)n)=\varphi(a)f(n)$, but not conversely.

### Exactness and preservation

**Proposition.** Restriction of scalars is exact: every short exact sequence in $\operatorname{Mod}(B)$ remains short exact in $\operatorname{Mod}(A)$.

*Proof.* The underlying groups and maps are unchanged, and exactness is a property of the underlying groups and maps alone. $\square$

Restriction also preserves direct sums, products and limits, since these are computed on the underlying modules. It does not in general preserve free modules or projective modules: the $A$-module $\operatorname{Res}_\varphi B$ is $B$ with the $A$-action through $\varphi$, and this is projective over $A$ only when $B$ happens to be projective as a left $A$-module. For the quotient homomorphism $A \to A/I$ it is $A/I$, which is projective over $A$ only when $I$ is a direct summand. Restriction preserves injective modules exactly when extension of scalars is exact, that is, when $B$ is flat as a right $A$-module: for an injective $B$-module $I$ the functor $\operatorname{Hom}_B(-,I)$ is exact, and $\operatorname{Hom}_A(-,\operatorname{Res}_\varphi I)\cong\operatorname{Hom}_B(B\otimes_A-,I)$, so it is exact whenever $B\otimes_A-$ is; dually, restriction preserves projectives exactly when $B$ is projective as a left $A$-module, the condition that the right adjoint $\operatorname{Hom}_A(B,-)$ be exact. If $A$ is semisimple then every $A$-module is projective and flat, so both conditions hold automatically.

## Extension of Scalars

### Definition

The homomorphism $\varphi$ makes $B$ a $(B,A)$-bimodule: the left action is multiplication in $B$, and the right action is

$$
b \cdot a = b\,\varphi(a), \qquad b \in B,\ a \in A.
$$

The bimodule axioms hold because $\varphi$ is a unital homomorphism. For a left $A$-module $M$, the balanced product

$$
\varphi_!(M)=B\otimes_A M
$$

is a left $B$-module by *The Balanced Product over an Algebra*, and the assignment is functorial:

$$
\varphi_! = B \otimes_A - : \operatorname{Mod}(A) \longrightarrow \operatorname{Mod}(B).
$$

This is **extension of scalars** along $\varphi$. Its elements are finite sums $\sum_i b_i\otimes m_i$, with the relations of the balanced product, and $b(b'\otimes m)=(bb')\otimes m$.

### Elementary properties

**Proposition.** Extension of scalars is right exact and preserves direct sums and free modules:

$$
B\otimes_A A \cong B, \qquad B\otimes_A A^n \cong B^n, \qquad B\otimes_A \Bigl(\bigoplus_i M_i\Bigr)\cong\bigoplus_i (B\otimes_A M_i).
$$

It preserves projective modules, and it carries the regular module ${}_A A$ to the regular module ${}_B B$.

*Proof.* Right exactness and preservation of direct sums are the corresponding properties of the balanced product from *The Balanced Product over an Algebra*. For free modules, $B\otimes_A A^n\cong (B\otimes_A A)^n\cong B^n$ by the unit isomorphism $B\otimes_A A\cong B$. A projective $A$-module is a direct summand of a free $A$-module $A^n$; applying the right exact functor $B\otimes_A-$ to the split sequence gives a split sequence exhibiting $B\otimes_A P$ as a direct summand of $B^n$, hence projective. $\square$

In general $B\otimes_A-$ is not left exact, and it is exact precisely when $B$ is flat as a right $A$-module, which is the subject of §Flatness and Change of Rings.

## Coextension of Scalars

### Definition

The homomorphism $\varphi$ also makes $B$ an $(A,B)$-bimodule: the left action is

$$
a \cdot b = \varphi(a) b, \qquad a \in A,\ b \in B,
$$

and the right action is multiplication in $B$. For a left $A$-module $N$, the abelian group

$$
\varphi_*(N)=\operatorname{Hom}_A(B,N)
$$

carries a left $B$-module structure

$$
(b \cdot f)(b')=f(b'b), \qquad b,b' \in B,\ f \in \operatorname{Hom}_A(B,N),
$$

which is a left action because $(bb')\cdot f=b\cdot(b'\cdot f)$, as the computation $f(b''(bb'))=f((b''b)b')$ shows. The resulting functor

$$
\varphi_*=\operatorname{Hom}_A(B,-) : \operatorname{Mod}(A) \longrightarrow \operatorname{Mod}(B)
$$

is **coextension of scalars**. It is left exact, being a hom functor, and it preserves limits and injectives.

### An inner description

When $\varphi$ is injective and $B$ is a free $A$-module, coextension has a more familiar shape. The $A$-linear maps $B\to N$ are determined by their values on an $A$-basis of $B$, and the $B$-action is by left multiplication of the argument. For the group algebra $A=F[H]\to F[G]=B$ this gives coinduction, and for the quotient $A\to A/I$ it gives the $I$-torsion submodule, both treated below.

## The Adjoint Triple

The three functors are linked by two adjunctions, both special cases of the tensor–hom adjunction of *The Balanced Product over an Algebra*.

**Theorem.** For a unital algebra homomorphism $\varphi: A \to B$ there are natural isomorphisms

$$
\operatorname{Hom}_B(\varphi_! M, N) \cong \operatorname{Hom}_A(M, \operatorname{Res}_\varphi N),
$$

$$
\operatorname{Hom}_B(N', \varphi_* N) \cong \operatorname{Hom}_A(\operatorname{Res}_\varphi N', N),
$$

for ${}_A M$, ${}_B N$, ${}_B N'$. Equivalently, there is an adjoint triple

$$
\varphi_! \dashv \operatorname{Res}_\varphi \dashv \varphi_*.
$$

*Proof.* The first isomorphism is the tensor–hom adjunction applied to the $(B,A)$-bimodule $B$, with $\operatorname{Hom}_B(B,N)\cong \operatorname{Res}_\varphi N$. The second is the same adjunction applied to the $(A,B)$-bimodule $B$, giving $\operatorname{Hom}_B(N',\operatorname{Hom}_A(B,N))\cong\operatorname{Hom}_A(B\otimes_B N',N)\cong\operatorname{Hom}_A(\operatorname{Res}_\varphi N',N)$. Both are natural in all variables. $\square$

**Corollary (Frobenius reciprocity).** With $M \in \operatorname{Mod}(A)$ and $N \in \operatorname{Mod}(B)$,

$$
\operatorname{Hom}_B(\varphi_! M, N) \cong \operatorname{Hom}_A(M, \operatorname{Res}_\varphi N).
$$

Taking dimensions over a field gives the classical multiplicity form: the multiplicity of a simple $B$-module $N$ in the extension of a simple $A$-module $M$ equals the multiplicity of $M$ in the restriction of $N$. This is the statement used constantly in the representation theory of groups and Lie algebras, and it is purely a consequence of the adjunction.

The adjoint triple has the usual formal consequences. Since $\varphi_!$ is a left adjoint it preserves colimits and is right exact; since $\operatorname{Res}_\varphi$ has both adjoints it preserves limits and colimits (both left and right exact, as observed directly); and since $\varphi_*$ is a right adjoint it preserves limits and is left exact. Moreover $\operatorname{Res}_\varphi$ preserves injectives exactly when the extension functor $B\otimes_A-$ is exact, and preserves projectives exactly when the coextension functor $\operatorname{Hom}_A(B,-)$ is exact, by the two adjunctions of §The Adjoint Triple.

## Base Change and the Quotient Case

### Base change of algebras

Let $R \to S$ be a homomorphism of commutative rings, let $A$ be an $R$-algebra, and put

$$
A_S=A\otimes_R S,
$$

the **base change** of $A$ to $S$. It is an $S$-algebra with multiplication $(a\otimes s)(a'\otimes s')=aa'\otimes ss'$, and there is a canonical $R$-algebra homomorphism $A\to A_S$, $a\mapsto a\otimes 1_S$. Applying the triple to this homomorphism gives, for a left $A$-module $M$,

$$
\operatorname{Res} M = M \text{ as an } R\text{-module}, \qquad \varphi_! M=A_S\otimes_A M \cong M\otimes_R S,
$$

the **complexification** or base change of $M$, and $\varphi_* M=\operatorname{Hom}_A(A_S,M)$. The most important case for this category is $R=\mathbb{R}$, $S=\mathbb{C}$, $A=\mathbb{H}$: then

$$
\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}=\mathbb{B},
$$

the biquaternion algebra, and extension of scalars carries real $\mathbb{H}$-modules to complex $\mathbb{B}$-modules. Since $\mathbb{B}\cong M_2(\mathbb{C})$ is Morita equivalent to $\mathbb{C}$, the complexified representation theory is the module theory of $\mathbb{C}$, a reduction used.

### The quotient homomorphism

Let $I \subseteq A$ be a two-sided ideal and let $\varphi: A \to A/I$ be the quotient map.

- **Restriction** is inflation: an $A/I$-module is an $A$-module on which $I$ acts by zero.
- **Extension** is $\varphi_! M=(A/I)\otimes_A M \cong M/IM$, by the right exactness and the relation $I\otimes_A M$ mapping onto $IM$. This is the largest quotient of $M$ on which $I$ acts trivially, and it is the standard tool for Nakayama's lemma of *Simple and Semisimple Modules*.
- **Coextension** is $\varphi_* N=\operatorname{Hom}_A(A/I,N)\cong\{n \in N : In=0\}$, the $I$-torsion submodule of $N$. Indeed an $A$-linear map $A/I\to N$ is determined by the image $n$ of $1$, and kills $I$ precisely when $In=0$.

For the Jacobson radical $I=J(A)$, extension is $M/J(A)M$ and restriction identifies the simple $A$-modules with the simple $A/J(A)$-modules, by *Simple and Semisimple Modules*.

## Flatness over Noncommutative Rings

### Definition

A right $A$-module $M$ is **flat** if the functor

$$
M\otimes_A - : \operatorname{Mod}(A) \longrightarrow \operatorname{Ab}
$$

is exact. Equivalently, $\operatorname{Tor}_1^A(M,N)=0$ for every left $A$-module $N$. A left $A$-module $N$ is flat if $-\otimes_A N$ is exact on right $A$-modules. The two notions are the two halves of the tensor product, and for a bimodule they may differ.

**Theorem.** Every projective module is flat. Consequently every free module is flat.

*Proof.* Free modules are flat because $A\otimes_A-\cong\mathrm{id}$ is exact, and a direct sum of flat modules is flat because $-\otimes_A-$ commutes with direct sums. A projective module is a direct summand of a free module, and a direct summand of a flat module is flat: if $M=P\oplus Q$ is flat and $L\to L'$ is injective, then $L\otimes_A P\to L'\otimes_A P$ is a direct summand of the injective map $L\otimes_A M\to L'\otimes_A M$, and a direct summand of an injective map is injective. $\square$

The converse is false in general: over a commutative ring the flat module $\mathbb{Q}$ over $\mathbb{Z}$ is not projective, and over a noncommutative ring flatness is again weaker than projectivity. Over a left perfect ring, and in particular over a finite-dimensional algebra, flat left modules are projective; this is a standard theorem of Bass and is cited rather than proved here.

### One-sidedness

Flatness over a noncommutative ring is a genuinely one-sided condition. To define the flatness of a bimodule ${}_B M_A$ one may ask whether $M\otimes_A-$ is exact, or whether $-\otimes_B M$ is exact, and the two questions are independent. Free modules and projective modules are flat on the side on which they act, but there exist bimodules flat as left modules and not as right modules; the standard examples and the fully faithful treatment are in the sources cited below. For a commutative ring the distinction disappears, and the flatness of *Modules* §13 is recovered.

### Localisation, Tor and purity

For a commutative ring $R$ and a multiplicative set $S$, the localisation $R\to S^{-1}R$ is flat as an $R$-module, so extension of scalars along it is exact; this is the commutative model of the phenomenon. Over a noncommutative ring one has the corresponding Ore localisations, whose flatness requires an Ore condition. The obstruction to flatness for a right $A$-module $M$ is measured by the groups $\operatorname{Tor}_i^A(M,-)$, of which the first vanishing is equivalent to flatness. A short exact sequence $0\to L\to M\to N\to0$ of left $A$-modules is **pure** when it remains exact after tensoring with every right $A$-module $M'$, that is, when the map $M'\otimes_A L\to M'\otimes_A M$ is injective for every $M'$. A sequence whose quotient $N$ is flat is pure, because $\operatorname{Tor}_1^A(M',N)=0$ forces the connecting map of the long exact sequence to vanish; the converse fails, since a split sequence is pure while its quotient need not be flat, as the split sequence $0\to\mathbb{Z}\to\mathbb{Z}\oplus\mathbb{Z}/2\mathbb{Z}\to\mathbb{Z}/2\mathbb{Z}\to0$ shows.

## Flatness and Change of Rings

The central result of the article is that flatness of the bimodule ${}_B B_A$ is exactly what makes extension of scalars exact, and that flatness of modules is inherited along a flat change of rings.

**Theorem.** Let $\varphi: A\to B$ be a unital algebra homomorphism. Then the following are equivalent.

1. Extension of scalars $B\otimes_A-$ is exact.
2. $B$ is flat as a right $A$-module.

*Proof.* Extension is the functor $B\otimes_A-$ applied to left $A$-modules, which is exact precisely when the right $A$-module $B$ is flat, by the definition of flatness. $\square$

**Theorem.** Let $\varphi: A\to B$ be a unital algebra homomorphism such that $B$ is flat as a right $A$-module, and let $N$ be a flat left $B$-module. Then $\operatorname{Res}_\varphi N$ is a flat left $A$-module.

*Proof.* Let $X$ be a right $A$-module. By associativity of the balanced product of *The Balanced Product over an Algebra*, applied to the right $A$-module $X$, the $(A,B)$-bimodule $B$ (through $\varphi$; its left $A$-action is $a\cdot b=\varphi(a)b$, and its right $B$-action is multiplication in $B$, the right $A$-module structure entering only through the flatness hypothesis) and the left $B$-module $N$,

$$
X\otimes_A \operatorname{Res}_\varphi N \cong (X\otimes_A B)\otimes_B N.
$$

The functor $X\mapsto X\otimes_A B$ is exact on right $A$-modules because $B$ is flat as a right $A$-module, and $-\otimes_B N$ is exact because $N$ is a flat left $B$-module; the composite is exact, so $\operatorname{Res}_\varphi N$ is flat. $\square$

Two further compatibility facts are immediate from the adjoint triple.

- Extension of scalars preserves projectives, by the proposition of §Extension of Scalars; it preserves flatness too, since for a right $B$-module $N'$ one has $N'\otimes_B(B\otimes_A M)\cong\operatorname{Res}_\varphi N'\otimes_A M$, so the functor $N'\mapsto N'\otimes_B(B\otimes_A M)$ is the composite of restriction, which is the identity on underlying groups and homomorphisms, with $-\otimes_A M$, and is therefore exact whenever $M$ is flat as a left $A$-module.
- Flatness and projectivity are Morita invariants, by *Morita Equivalence*, so they are unchanged under the extension along a Morita equivalence.

## Examples

**(a) The identity.** For $\varphi=\mathrm{id}_A$ the triple is $A\otimes_A-\cong\mathrm{id}$, restriction is the identity, and coextension is $\operatorname{Hom}_A(A,-)\cong\mathrm{id}$; all three coincide, and both adjunctions are the identity adjunction.

**(b) Inclusion of a subalgebra.** For an inclusion $A\hookrightarrow B$, restriction forgets the action of the elements of $B\setminus A$; extension is $B\otimes_A-$; coextension is $\operatorname{Hom}_A(B,-)$. When $B$ is free of rank $r$ as an $A$-module on each side, with basis $b_1,\dots,b_r$, the underlying $A$-modules of $\varphi_!M$ and $\varphi_*M$ agree: both are direct sums of $r$ copies of $M$, because $B\otimes_A M\cong A^r\otimes_A M\cong M^r$ on the right and a homomorphism out of the free left $A$-module $B$ is determined by the images of the basis, so that $\operatorname{Hom}_A(B,M)\cong M^r$. The $B$-module structures need not coincide, however, and the question whether extension and coextension are isomorphic is a genuine one; the group-algebra case, where a finite index makes them isomorphic, is example (e).

**(c) Quotients.** For $A\to A/I$ the three functors are inflation, $M\mapsto M/IM$, and $N\mapsto\{n : In=0\}$, as in §Base Change and the Quotient Case. Nakayama's lemma is the statement that $M/IM=M$ forces $M=0$ when $I\subseteq J(A)$ and $M$ is finitely generated.

**(d) Base change.** For $R\to S$ commutative and $A$ an $R$-algebra, extension along $A\to A\otimes_R S$ is $M\mapsto M\otimes_R S$; for $R\hookrightarrow S$ and $S$ flat over $R$, the extension is exact, and flatness is inherited by the base-changed module. For $R=\mathbb{R}\to\mathbb{C}$ and $A=\mathbb{H}$, this complexifies $\mathbb{H}$-modules to $\mathbb{B}$-modules, and for $A=\mathbb{H}$ itself $\mathbb{H}\otimes_\mathbb{R}\mathbb{C}=\mathbb{B}\cong M_2(\mathbb{C})$.

**(e) Group algebras and Frobenius reciprocity.** Let $H\leq G$ be finite groups, let $F$ be a field and let $\varphi: F[H]\to F[G]$ be the inclusion. Then

$$
\varphi_! V=F[G]\otimes_{F[H]}V=\operatorname{Ind}_H^G V, \qquad \varphi_* W=\operatorname{Hom}_{F[H]}(F[G],W)=\operatorname{Coind}_H^G W,
$$

and the adjunction $\varphi_!\dashv\operatorname{Res}$ is **Frobenius reciprocity**:

$$
\operatorname{Hom}_{F[G]}(\operatorname{Ind}_H^G V, W) \cong \operatorname{Hom}_{F[H]}(V, \operatorname{Res}_H^G W).
$$

Because $F[G]$ is free of rank $[G:H]$ over $F[H]$ on both sides, induction and coinduction are naturally isomorphic, and the rank formula gives $\dim_F \operatorname{Ind}_H^G V=[G:H]\dim_F V$. Restriction is exact always. The representation-theoretic content is developed.

**(f) The quaternion algebra over the reals.** The inclusion $\mathbb{R}\hookrightarrow\mathbb{H}$ makes $\mathbb{H}$ a free $\mathbb{R}$-module, hence flat, so every restriction of an $\mathbb{H}$-module to $\mathbb{R}$ is flat, and extension $\mathbb{H}\otimes_\mathbb{R}-$ is exact. For $\mathbb{R}\hookrightarrow\mathbb{C}$ and $A=\mathbb{H}$, the extension is $\mathbb{B}\cong M_2(\mathbb{C})$, Morita equivalent to $\mathbb{C}$; the functor $\operatorname{Mod}(\mathbb{H})\to\operatorname{Mod}(\mathbb{B})$ is exact, and its target has a single simple module, the defining module $S=\mathbb{C}^2$.

## Summary

A unital algebra homomorphism $\varphi: A\to B$ induces an adjoint triple $\varphi_!\dashv\operatorname{Res}_\varphi\dashv\varphi_*$ between $\operatorname{Mod}(A)$ and $\operatorname{Mod}(B)$. Restriction of scalars is the identity on underlying abelian groups and homomorphisms, is faithful, injective on hom-sets, exact, and preserves limits; it preserves injectives exactly when $B$ is flat as a right $A$-module, equivalently when extension of scalars is exact; it sends a $B$-module $N$ to the $A$-module with $a\cdot n=\varphi(a)n$. Extension of scalars is $\varphi_! M=B\otimes_A M$, where $B$ is the $(B,A)$-bimodule induced by $\varphi$; it is right exact, preserves direct sums, free modules, the regular module and projective modules, and by Frobenius reciprocity $\operatorname{Hom}_B(\varphi_!M,N)\cong\operatorname{Hom}_A(M,\operatorname{Res}N)$. Coextension of scalars is $\varphi_* N=\operatorname{Hom}_A(B,N)$ with $(b\cdot f)(b')=f(b'b)$, where $B$ is the $(A,B)$-bimodule induced by $\varphi$; it is left exact and satisfies $\operatorname{Hom}_B(N',\varphi_*N)\cong\operatorname{Hom}_A(\operatorname{Res}N',N)$. The two adjunctions are the tensor–hom adjunction applied to the two bimodule structures on $B$.

Extension is exact exactly when $B$ is flat as a right $A$-module. Flatness over a noncommutative ring means exactness of the relevant one-sided tensor functor, and it is a genuinely one-sided condition for bimodules; projective modules and free modules are flat, the converse fails, and over a left perfect ring, in particular a finite-dimensional algebra, flat left modules are projective. Flatness is inherited along a flat change of rings: if $B$ is flat as a right $A$-module and $N$ is a flat left $B$-module, then $\operatorname{Res}_\varphi N$ is a flat left $A$-module, by the associativity identity $X\otimes_A\operatorname{Res}_\varphi N\cong(X\otimes_A B)\otimes_B N$. The examples are the identity, inclusions of subalgebras, quotient maps (where extension is $M\mapsto M/IM$ and coextension is the $I$-torsion), base change of algebras (including the complexification $\mathbb{H}\to\mathbb{B}$), and the group-algebra case, where extension and coextension are induction and coinduction and the first adjunction is Frobenius reciprocity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity, the base ring |
| $A$, $B$ | unital associative $R$-algebras |
| $\varphi : A \to B$ | unital $R$-algebra homomorphism |
| $\operatorname{Res}_\varphi$ | restriction of scalars $\operatorname{Mod}(B)\to\operatorname{Mod}(A)$ |
| $\varphi_! = B\otimes_A -$ | extension of scalars $\operatorname{Mod}(A)\to\operatorname{Mod}(B)$ |
| $\varphi_* = \operatorname{Hom}_A(B,-)$ | coextension of scalars $\operatorname{Mod}(A)\to\operatorname{Mod}(B)$ |
| $\varphi_! \dashv \operatorname{Res}_\varphi \dashv \varphi_*$ | the adjoint triple |
| $M/IM$ | $\varphi_!M$ for the quotient map $A\to A/I$ |
| $\{n : In=0\}$ | $\varphi_*N$ for the quotient map $A\to A/I$ |
| $A_S=A\otimes_R S$ | base change of an $R$-algebra to an $S$-algebra |
| $M\otimes_R S$ | base change of a module |
| $\operatorname{Tor}_i^A(M,N)$ | derived functors of the balanced product |
| $\operatorname{Ind}_H^G V=F[G]\otimes_{F[H]}V$ | induction, extension along $F[H]\to F[G]$ |
| $\operatorname{Coind}_H^G W=\operatorname{Hom}_{F[H]}(F[G],W)$ | coinduction |
| $J(A)$ | Jacobson radical |
| $\mathbb{H}$, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | quaternions, biquaternions |
| $S=\mathbb{C}^2$ | defining module of $\mathbb{B}$ |



## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for restriction, extension and coextension of scalars and their adjunctions.
- Hyman Bass, *Algebraic K-Theory* (Benjamin, 1968), for perfect rings and the theorem that flat left modules over them are projective.
- Nicolas Bourbaki, *Algebra I* (Springer, 1989), for change of rings, flatness and the tensor–hom adjunction.
- Henri Cartan and Samuel Eilenberg, *Homological Algebra* (Princeton, 1956), for Tor, flatness and purity.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Wiley, 1962), for induction, coinduction and Frobenius reciprocity.
- I. Martin Isaacs, *Character Theory of Finite Groups* (Academic Press, 1976), for Frobenius reciprocity and induced modules in the group-algebra setting.
- T. Y. Lam, *Lectures on Modules and Rings* (Springer, 1999), for flatness over noncommutative rings, one-sided flatness, and the theorems of Bass.
- Bo Stenström, *Rings of Quotients* (Springer, 1975), for one-sided localisation and flatness.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge, 1994), for Tor, flatness and change of rings.
