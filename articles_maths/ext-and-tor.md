
# __Ext and Tor__

## Introduction

The two functors that the corpus uses most are the derived functors of the two basic functors of module theory: $\operatorname{Hom}_R(-,-)$ and $-\otimes_R-$. The right derived functors of $\operatorname{Hom}$ are the **Ext** functors, and the left derived functors of the tensor product are the **Tor** functors. They measure the failure of these two functors to be exact, they are the input to the universal coefficient and Künneth theorems, and they are the algebra behind group cohomology, Hochschild homology and sheaf cohomology. $\operatorname{Ext}^1$ in particular has a second, entirely different description — the classes of extensions of one module by another, with the Baer sum as group law — and the coincidence of the two descriptions is the deepest elementary fact about Ext.

This article develops $\operatorname{Ext}_R^n(M,N)$ and $\operatorname{Tor}_n^R(M,N)$: the two ways of computing each, their long exact sequences in each variable, the extension interpretation of $\operatorname{Ext}^1$ and the Yoneda description of the higher groups, the relation of $\operatorname{Tor}_1$ and $\operatorname{Tor}$ to torsion and to flatness, the universal coefficient theorem, and the identifications with group cohomology and, in Part II, with sheaf cohomology. It follows *Derived Functors* directly, and it uses the resolutions, comparison theorem and long exact sequences of *Homological Algebra*.

Throughout, $R$ is a commutative ring with identity $1\neq0$ and $M,N$ are $R$-modules; statements that need no commutativity are marked, and there the side of the modules is stated. The article is algebraic: no distance, norm, open set or completion occurs, and the sheaf-cohomological realisation of the theory is deferred to Part II, where it is treated in *Sheaves and Cohomology*. The spectral sequences that compute the derived functors of composites are developed and are only named here.

## Ext

### The Two Definitions

**Definition.** Let $M,N$ be $R$-modules. Choose a projective resolution $P_\bullet\to M$ and form the cochain complex

$$
0\longrightarrow\operatorname{Hom}_R(P_0,N)\xrightarrow{\ d^0\ }\operatorname{Hom}_R(P_1,N)\xrightarrow{\ d^1\ }\operatorname{Hom}_R(P_2,N)\longrightarrow\cdots,
$$

with $d^n$ induced by precomposition with the differential $P_{n+1}\to P_n$. The **Ext groups** are

$$
\operatorname{Ext}_R^n(M,N)=H^n\bigl(\operatorname{Hom}_R(P_\bullet,N)\bigr), \qquad n\ge0 .
$$

Equivalently, since $\operatorname{Hom}_R(M,-)$ is left exact, $\operatorname{Ext}_R^n(M,N)=R^n\operatorname{Hom}_R(M,-)(N)$, computed from an injective resolution of $N$.

**Theorem (balance).** The two computations agree: if $P_\bullet\to M$ is a projective resolution and $N\to I^\bullet$ an injective resolution, then $H^n(\operatorname{Hom}_R(P_\bullet,N))\cong H^n(\operatorname{Hom}_R(M,I^\bullet))$ naturally in $M$ and $N$.

*Proof (in outline).* The double complex with entries $\operatorname{Hom}_R(P_p,I^q)$ has two differentials, one induced by $P_\bullet$ and one by $I^\bullet$, and they anticommute. The two spectral sequences of the double complex have $E_2^{p,q}=0$ for $q\neq0$ in one case and for $p\neq0$ in the other, because $P_p$ is projective and $I^q$ injective; both sequences therefore collapse, and their common abutment computes both sides. The degenerate case of the argument can also be run directly by the comparison theorem, comparing two resolutions of $M$. $\square$

The proof is the first place the spectral-sequence machinery is needed; it is carried out, and the balance statement is quoted here.

**Proposition.** $\operatorname{Ext}_R^0(M,N)\cong\operatorname{Hom}_R(M,N)$. The groups $\operatorname{Ext}_R^n(M,N)$ are additive functors of $N$ and, in the contravariant sense, of $M$; they vanish for $n\ge1$ whenever $M$ is projective or $N$ is injective.

*Proof.* $H^0=\ker d^0$ is $\operatorname{Hom}_R(M,N)$ because a map $P_0\to N$ killed by precomposition with $P_1\to P_0$ factors through the cokernel $M$ of $P_1\to P_0$. If $M$ is projective, $P_\bullet=M$ in degree $0$ and the complex is concentrated in degree $0$. If $N$ is injective, $\operatorname{Hom}_R(-,N)$ is exact and takes the exact resolution to an exact complex. $\square$

### The Long Exact Sequences

**Theorem.** A short exact sequence $0\to N'\to N\to N''\to0$ of $R$-modules yields a long exact sequence

$$
0\to\operatorname{Hom}_R(M,N')\to\operatorname{Hom}_R(M,N)\to\operatorname{Hom}_R(M,N'')\xrightarrow{\ \delta^0\ }\operatorname{Ext}_R^1(M,N')\to\cdots\to\operatorname{Ext}_R^n(M,N'')\xrightarrow{\ \delta^n\ }\operatorname{Ext}_R^{n+1}(M,N')\to\cdots,
$$

natural in the sequence. A short exact sequence $0\to M'\to M\to M''\to0$ yields a long exact sequence in the first variable, with the variance reversed,

$$
0\to\operatorname{Hom}_R(M'',N)\to\operatorname{Hom}_R(M,N)\to\operatorname{Hom}_R(M',N)\xrightarrow{\ \delta^0\ }\operatorname{Ext}_R^1(M'',N)\to\cdots,
$$

natural in the sequence.

*Proof.* The first is the long exact sequence of the left exact functor $\operatorname{Hom}_R(M,-)$ applied to the injective resolution, from *Derived Functors*. For the second, apply the contravariant left exact functor $\operatorname{Hom}_R(-,N)$ to a projective resolution of $M''$, or equivalently resolve the sequence by the horseshoe lemma and apply $\operatorname{Hom}_R(-,N)$; the connecting maps come from the snake lemma and the long exact homology sequence. $\square$

**Corollary.** The functors $\operatorname{Ext}_R^n(M,-)$ vanish for $n\ge1$ if and only if $M$ is projective, and $\operatorname{Ext}_R^n(-,N)$ vanish for $n\ge1$ if and only if $N$ is injective.

*Proof.* If $M$ is projective the first statement is the proposition above. Conversely, if $\operatorname{Ext}_R^1(M,-)=0$ then applying the long exact sequence to a surjection $P\to M$ with $P$ projective gives exactness of $\operatorname{Hom}_R(M,-)$ on the relevant short exact sequence, hence a lift of the identity of $M$ to $P$, so $M$ is a direct summand of $P$ and projective. The argument for injectives is dual. $\square$

### Ext$^1$ and Extensions

**Definition.** An **extension** of $M$ by $N$ is a short exact sequence $\xi:0\to N\to E\to M\to0$. Two extensions are **equivalent** if there is an isomorphism $E\to E'$ making the diagram commute, that is, restricting to the identity on $N$ and inducing the identity on $M$. The set of equivalence classes is written $\operatorname{Ext}^1_R(M,N)_{\mathrm{ext}}$.

**Definition (Baer sum).** Given extensions $\xi:0\to N\to E\to M\to0$ and $\eta:0\to N\to E'\to M\to0$, form the pullback of $E\to M$ and $E'\to M$, the extension $0\to N\oplus N\to E\times_ME'\to M\to0$, and then push forward along the subtraction map $N\oplus N\to N$, $(n,n')\mapsto n-n'$. The result is the **Baer sum** $\xi+\eta$, and it makes $\operatorname{Ext}^1_R(M,N)_{\mathrm{ext}}$ an abelian group with the split extension $0\to N\to N\oplus M\to M\to0$ as zero.

**Theorem.** There is a natural isomorphism of abelian groups $\operatorname{Ext}_R^1(M,N)\cong\operatorname{Ext}^1_R(M,N)_{\mathrm{ext}}$. The class $0$ corresponds to the split extension.

*Proof (in outline).* Given an extension $0\to N\to E\xrightarrow{\pi}M\to0$, choose a projective resolution and lift the identity of $M$ to a chain map into the complex $0\to N\to E\to0$ concentrated in degrees $2,1,0$; the failure of the lift to be a chain map in degree one is a cocycle in $\operatorname{Hom}_R(P_1,N)$, and its class does not depend on the lift. Conversely, a class $[c]\in\operatorname{Ext}^1_R(M,N)$ with $c\in\operatorname{Hom}_R(P_1,N)$ defines an extension as the cokernel of $P_1\to P_0\oplus N$, $x\mapsto(d_1x,cx)$, which is exact at the middle because of the cocycle condition. The two constructions are inverse, and the Baer sum agrees with addition of cohomology classes. $\square$

**Theorem (Yoneda).** For $n\ge1$ the group $\operatorname{Ext}_R^n(M,N)$ is naturally isomorphic to the group of equivalence classes of **$n$-fold extensions**, that is, exact sequences

$$
0\to N\to E_{n-1}\to E_{n-2}\to\cdots\to E_0\to M\to0,
$$

under a suitable equivalence relation, with the Baer-sum addition. For $n=1$ this reduces to the previous theorem.

*Proof.* The verification is that the Yoneda product of extensions composes with the connecting homomorphisms and that a projective resolution is a universal $n$-fold extension; the details are the standard Yoneda theory. $\square$

**Example.** $\operatorname{Ext}_{\mathbb{Z}}^1(\mathbb{Z}/n\mathbb{Z},A)\cong A/nA$ for every abelian group $A$: apply $\operatorname{Hom}_{\mathbb{Z}}(-,A)$ to the free resolution $0\to\mathbb{Z}\xrightarrow{\cdot n}\mathbb{Z}\to\mathbb{Z}/n\mathbb{Z}\to0$, giving the complex $0\to A\xrightarrow{\cdot n}A\to0$ concentrated in degrees $1,0$, whose $H^1$ is $A/nA$. For $A=\mathbb{Z}/m\mathbb{Z}$ this is $\mathbb{Z}/\gcd(m,n)\mathbb{Z}$. The extension interpretation recovers the fact that the nonsplit extensions of $\mathbb{Z}/n\mathbb{Z}$ by itself correspond to the elements of $\mathbb{Z}/n\mathbb{Z}$.

**Example.** Over a field $F$ every module is free, hence projective and injective, so $\operatorname{Ext}_F^n(M,N)=0$ for all $n\ge1$ and all vector spaces $M,N$; all short exact sequences of vector spaces split. The functor $\operatorname{Hom}_F(M,-)$ is exact.

## Tor

### Definition and Symmetry

**Definition.** Let $M,N$ be $R$-modules. Choose a projective resolution $P_\bullet\to M$ and form

$$
\operatorname{Tor}_n^R(M,N)=H_n\bigl(P_\bullet\otimes_RN\bigr), \qquad n\ge0 .
$$

Since $-\otimes_RN$ is right exact, $\operatorname{Tor}_n^R(M,N)=L_n(-\otimes_RN)(M)$ in the notation of *Derived Functors*.

**Theorem (balance).** $\operatorname{Tor}_n^R(M,N)\cong\operatorname{Tor}_n^R(N,M)$ naturally in $M$ and $N$; both are computed by resolving either variable.

*Proof.* Resolving $M$ by projectives and $N$ by projectives and forming the double complex $P_\bullet\otimes_RQ_\bullet$ gives two spectral sequences, both collapsing because projectives are flat; their common abutment is the total complex of $P_\bullet\otimes_RQ_\bullet$, whose homology computes both sides. The direct argument uses the comparison theorem and the flatness of projectives. $\square$

**Proposition.** $\operatorname{Tor}_0^R(M,N)\cong M\otimes_RN$, and $\operatorname{Tor}_n^R(M,N)=0$ for $n\ge1$ whenever $M$ or $N$ is flat; in particular $\operatorname{Tor}_n^R(M,N)=0$ whenever $M$ or $N$ is projective, and over a field every $\operatorname{Tor}_n$ with $n\ge1$ vanishes.

*Proof.* $\operatorname{Tor}_0=M\otimes_RN$ because the tensor product is right exact and the resolution is exact. If $M$ is flat, the functor $-\otimes_RN$ is exact and the complex $P_\bullet\otimes_RN$ is exact in positive degrees. Flatness of $N$ means $M\otimes_R-$ is exact, and the symmetry of Tor reduces this to the previous case. $\square$

**Corollary.** $M$ is flat if and only if $\operatorname{Tor}_1^R(M,N)=0$ for every $N$, equivalently if and only if $\operatorname{Tor}_n^R(M,N)=0$ for every $n\ge1$ and every $N$. This is the homological characterisation of flatness.

**Theorem.** A short exact sequence $0\to N'\to N\to N''\to0$ yields a long exact sequence

$$
\cdots\to\operatorname{Tor}_n^R(M,N')\to\operatorname{Tor}_n^R(M,N)\to\operatorname{Tor}_n^R(M,N'')\xrightarrow{\ \partial_n\ }\operatorname{Tor}_{n-1}^R(M,N')\to\cdots\to M\otimes_RN''\to0,
$$

natural in the sequence; a short exact sequence in $M$ gives the analogous sequence, and by symmetry the two agree.

*Proof.* Apply the functor $-\otimes_RN$ to a short exact sequence of projective resolutions produced by the horseshoe lemma and take the long exact homology sequence, as in *Derived Functors*. $\square$

### Tor and Torsion

**Theorem.** Over a principal ideal domain $R$, every module has a free resolution of length one and

$$
\operatorname{Tor}_0^R(M,N)=M\otimes_RN, \qquad \operatorname{Tor}_1^R(M,N)=\operatorname{Tor}(M,N), \qquad \operatorname{Tor}_n^R(M,N)=0 \ \ (n\ge2),
$$

where $\operatorname{Tor}(M,N)=\operatorname{Tor}_1^R(M,N)$ is the **torsion product**, computed from any free presentation $0\to K\to F\to M\to0$ as the kernel of $K\otimes_RN\to F\otimes_RN$. For $R=\mathbb{Z}$ and $M=\mathbb{Z}/m\mathbb{Z}$ one has $\operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/m\mathbb{Z},N)\cong\{n\in N:mn=0\}$.

*Proof.* Write $0\to K\to F\to M\to0$ with $F$ free, so $K$ is free because $R$ is a principal ideal domain; then $\operatorname{Tor}_n^R(M,N)=0$ for $n\ge2$, since the resolution has length one, and $\operatorname{Tor}_1^R(M,N)=\ker(K\otimes_RN\to F\otimes_RN)$. This kernel is the **torsion product** $\operatorname{Tor}(M,N)$. For $M=\mathbb{Z}/m\mathbb{Z}$ the resolution $0\to\mathbb{Z}\xrightarrow{\cdot m}\mathbb{Z}\to M\to0$ gives $\operatorname{Tor}_1=\ker(m:N\to N)$. $\square$

**Example.** $\operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/m\mathbb{Z},\mathbb{Z}/n\mathbb{Z})\cong\mathbb{Z}/\gcd(m,n)\mathbb{Z}$, from the resolution above with $N=\mathbb{Z}/n\mathbb{Z}$. The symmetry of Tor expresses the symmetry of the gcd.

**Example.** For a flat module the torsion product vanishes: $\operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Q},\mathbb{Z}/n\mathbb{Z})=0$ because $\mathbb{Q}$ is flat over $\mathbb{Z}$, and $\operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Q},\mathbb{Q})=0$. Localisation is flat in general, so $\operatorname{Tor}_n^R(S^{-1}R,N)=0$ for $n\ge1$.

## The Universal Coefficient Theorem

### Statement

For a complex of free modules the cohomology with coefficients is computed by the homology and the Ext groups; this is the universal coefficient theorem, and it is the standard application of the two functors.

**Theorem (universal coefficients, cohomology).** Let $C_\bullet$ be a chain complex of free modules over a principal ideal domain $R$, and let $N$ be an $R$-module. For every $n$ there is a natural short exact sequence

$$
0\longrightarrow\operatorname{Ext}_R^1(H_{n-1}(C_\bullet),N)\longrightarrow H^n(\operatorname{Hom}_R(C_\bullet,N))\longrightarrow\operatorname{Hom}_R(H_n(C_\bullet),N)\longrightarrow0,
$$

which splits, though not naturally.

**Theorem (universal coefficients, homology).** With the same hypotheses, for every $n$ there is a natural short exact sequence

$$
0\longrightarrow H_n(C_\bullet)\otimes_RN\longrightarrow H_n(C_\bullet\otimes_RN)\longrightarrow\operatorname{Tor}_1^R(H_{n-1}(C_\bullet),N)\longrightarrow0,
$$

which splits, though not naturally.

*Proof (of the homology form).* Filter the complex $C_\bullet$ by its cycles. The short exact sequences $0\to Z_n\to C_n\to B_{n-1}\to0$ and $0\to B_n\to Z_n\to H_n\to0$ are short exact sequences of complexes; applying $-\otimes_RN$ and using that $C_n$ is free, hence flat, gives the connecting maps and identifies the two ends. The Ext form is dual, with $\operatorname{Hom}_R(-,N)$ in place of $-\otimes_RN$ and the freeness of $C_n$ making $\operatorname{Hom}_R(C_n,-)$ exact. The splitting uses that the middle term is free, or more generally that the end terms are; it is not natural because the identification of the splitting depends on a choice of free presentation of the homology. $\square$

**Corollary.** If $R$ is a principal ideal domain and $H_{n-1}(C_\bullet)$ is free, then $H^n(\operatorname{Hom}_R(C_\bullet,N))\cong\operatorname{Hom}_R(H_n(C_\bullet),N)$ and $H_n(C_\bullet\otimes_RN)\cong H_n(C_\bullet)\otimes_RN$. Over a field the Ext and Tor terms always vanish and both theorems are the statement that (co)homology commutes with coefficients.

**Example.** For $R=\mathbb{Z}$, $C_\bullet$ the singular chain complex of a space — a fortiori having free chain groups — the theorem expresses the cohomology with coefficients in $N$ through the integral homology and an Ext term; this is the algebraic statement, and the topological reading belongs to Part II, where it is treated in *Algebraic Topology*.

### The Künneth Formula

**Theorem (Künneth, algebraic form).** Let $R$ be a principal ideal domain and let $C_\bullet,D_\bullet$ be chain complexes of free $R$-modules with $C_\bullet$ bounded below. For every $n$ there is a natural short exact sequence

$$
0\longrightarrow\bigoplus_{p+q=n}H_p(C_\bullet)\otimes_RH_q(D_\bullet)\longrightarrow H_n(C_\bullet\otimes_RD_\bullet)\longrightarrow\bigoplus_{p+q=n-1}\operatorname{Tor}_1^R(H_p(C_\bullet),H_q(D_\bullet))\longrightarrow0,
$$

which splits, though not naturally.

*Pro.* Filter the tensor product complex by the degree of $C$, or apply the spectral sequence of the bicomplex $C_p\otimes_RD_q$; over a principal ideal domain the two rows of the $E^2$-page are the displayed terms and the spectral sequence has only two nonzero rows, so it degenerates to the short exact sequence. The derivation by the spectral sequence is carried out, and the direct proof uses the universal coefficient theorem. $\square$

**Remark.** The Künneth sequence is the reason $\operatorname{Tor}_1$ occurs in the computation of the homology of a product; the topological instance of the formula needs spaces and belongs to Part II. The algebraic form above is stated for chain complexes of modules, as here.

## Relations to Group Cohomology and Sheaf Cohomology

### Group Cohomology as Ext

**Proposition.** Let $G$ be a group and let $M$ be a $G$-module, that is, a module over the group ring $\mathbb{Z}[G]$. Then there are natural isomorphisms

$$
H^n(G,M)\cong\operatorname{Ext}_{\mathbb{Z}[G]}^n(\mathbb{Z},M), \qquad n\ge0,
$$

where $\mathbb{Z}$ is the trivial $G$-module. The group homology is $\operatorname{Tor}_n^{\mathbb{Z}[G]}(\mathbb{Z},M)$.

*Proof.* The functor of invariants $M\mapsto M^G$ is naturally isomorphic to $\operatorname{Hom}_{\mathbb{Z}[G]}(\mathbb{Z},M)$, and the functor of coinvariants to $\mathbb{Z}\otimes_{\mathbb{Z}[G]}M$. The statement is the definition of group cohomology as the right derived functors of invariants, together with the identification of that functor with $\operatorname{Hom}_{\mathbb{Z}[G]}(\mathbb{Z},-)$. $\square$

**Example.** The augmentation ideal of $\mathbb{Z}[G]$ and the standard bar resolution give the usual cocycle description of $H^n(G,M)$, and $\operatorname{Ext}_{\mathbb{Z}[G]}^1(\mathbb{Z},M)$ classifies the extensions of $\mathbb{Z}$ by $M$, that is, the extensions of groups $1\to M\to E\to G\to1$ with abelian kernel; this is the group-theoretic face of the extension interpretation of $\operatorname{Ext}^1$. The development belongs to the companion article *Group Cohomology* of the *Groups* category, being written in the same batch.

### Sheaf Cohomology and the Deferred Statement

**Remark.** For a sheaf of abelian groups on a site the global-section functor is left exact, and the sheaf cohomology $H^n(X,\mathcal{F})$ is by definition its $n$-th right derived functor; the identification of the resulting groups with a derived functor of $\operatorname{Hom}$ in the category of sheaves is the same balance statement proved above in the module case, carried out in a Grothendieck category with enough injectives. The sheaf-theoretic version needs a site and a topology, and it belongs to Part II, where it is treated in *Sheaves and Cohomology*; the categorical framework is supplied by *Abelian and Grothendieck Categories*. This article develops the algebraic functors and states the comparison in categorical terms only.

### Additivity and Vanishing: a Summary of Computations

**Proposition.** Let $R$ be a commutative ring and let $M,N$ be $R$-modules.

(i) $\operatorname{Ext}_R^0(M,N)=\operatorname{Hom}_R(M,N)$ and $\operatorname{Tor}_0^R(M,N)=M\otimes_RN$.

(ii) $\operatorname{Ext}_R^n$ and $\operatorname{Tor}_n^R$ commute with finite direct sums in each variable.

(iii) For $R$ a principal ideal domain, $\operatorname{Ext}_R^n=0$ and $\operatorname{Tor}_n^R=0$ for $n\ge2$, and $\operatorname{Ext}_R^1(M,N)$ and $\operatorname{Tor}_1^R(M,N)$ are the torsion computed above.

(iv) If $R$ is a field, all groups with $n\ge1$ vanish.

*Proof.* (i) and (ii) are the propositions of this article and the additivity of derived functors. (iii) follows from the length-one free resolution over a principal ideal domain. (iv) is the projectivity of every module over a field. $\square$

## Summary

For $R$-modules $M,N$, $\operatorname{Ext}_R^n(M,N)$ is the right derived functor of $\operatorname{Hom}_R(M,-)$ evaluated at $N$, equivalently the cohomology of $\operatorname{Hom}_R(P_\bullet,N)$ for a projective resolution of $M$; the two computations agree by the balance theorem, whose proof needs the double complex and is completed. $\operatorname{Ext}^0=\operatorname{Hom}$, the functors vanish in positive degree when either argument is projective or injective in the appropriate slot, and they carry two long exact sequences, one in each variable. $\operatorname{Ext}^1_R(M,N)$ classifies the extensions of $M$ by $N$ under the Baer sum, and $\operatorname{Ext}^n_R(M,N)$ classifies the $n$-fold extensions.

$\operatorname{Tor}_n^R(M,N)$ is the left derived functor of $-\otimes_RN$ evaluated at $M$, equivalently the homology of $P_\bullet\otimes_RN$; it is symmetric in the two variables, $\operatorname{Tor}_0=M\otimes_RN$, it vanishes in positive degree when either variable is flat, and flatness is exactly the vanishing of $\operatorname{Tor}_1$ against every module. Over a principal ideal domain only $\operatorname{Tor}_1$ survives and it is the torsion product, with $\operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/m,\mathbb{Z}/n)=\mathbb{Z}/\gcd(m,n)\mathbb{Z}$.

The universal coefficient theorems express the (co)homology of a complex of free modules with coefficients through the integral (co)homology together with an Ext or a Tor term, splitting but not naturally; the Künneth theorem is the same computation for the tensor product of two complexes. Group cohomology is $\operatorname{Ext}^n_{\mathbb{Z}[G]}(\mathbb{Z},-)$, sheaf cohomology is the same construction in a Grothendieck category of sheaves and belongs to Part II, and the spectral sequences that compute the derived functors of composites are not covered here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Ext}_R^n(M,N)$ | right derived functors of $\operatorname{Hom}_R(M,-)$ at $N$ |
| $\operatorname{Tor}_n^R(M,N)$ | left derived functors of $-\otimes_RN$ at $M$ |
| $P_\bullet\to M$ | projective resolution of $M$ |
| $N\to I^\bullet$ | injective resolution of $N$ |
| $\delta^n$, $\partial_n$ | connecting morphisms of the Ext and Tor long exact sequences |
| $\operatorname{Ext}^1_R(M,N)_{\mathrm{ext}}$ | extension classes of $M$ by $N$ |
| $E\times_ME'$ | pullback used in the Baer sum |
| $\operatorname{Tor}(M,N)$ | torsion product over a principal ideal domain |
| $\operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/m,\mathbb{Z}/n)=\mathbb{Z}/\gcd(m,n)\mathbb{Z}$ | the standard computation |
| $H^n(G,M)$ | group cohomology, $=\operatorname{Ext}^n_{\mathbb{Z}[G]}(\mathbb{Z},M)$ |
| $R$ | commutative ring with $1\neq0$; a principal ideal domain where stated |





## Further Reading

- Henri Cartan and Samuel Eilenberg, *Homological Algebra* (Princeton University Press, 1956), for Ext, Tor, the balance of the two computations and the universal coefficient theorems.
- David Eisenbud, *Commutative Algebra with a View Toward Algebraic Geometry* (Springer, 1995), for Ext, Tor, the Koszul complex and computations over regular rings.
- Peter J. Hilton and Urs Stammbach, *A Course in Homological Algebra*, 2nd ed. (Springer, 1997), for the extension interpretation of $\operatorname{Ext}^1$ and the Yoneda product.
- Saunders Mac Lane, *Homology* (Springer, 1995), for Ext, Tor, the universal coefficient theorem and the Künneth formula.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for the long exact sequences and the computations over a principal ideal domain.
- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for group cohomology as Ext over the group ring.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for Ext, Tor, the balance theorem and the Künneth spectral sequence.
