
# __Derived Functors__

## Introduction

A half-exact functor loses information: the left exact functor $\operatorname{Hom}_R(M,-)$ turns a short exact sequence into four exact terms and then stops, and the right exact functor $-\otimes_RM$ does the same in the other direction. The loss is measured by a sequence of functors, the **derived functors**, which continue the exact sequence indefinitely and turn the failure of exactness into data. The construction is the one the previous article prepared: apply the functor not to the module but to a projective or an injective resolution, and take the homology of the resulting complex. The comparison theorem guarantees that the answer does not depend on the resolution chosen, so the construction is intrinsic.

This article develops the right derived functors of a left exact functor and the left derived functors of a right exact one, their independence of the resolution, the connecting homomorphism and the long exact sequence, the technique of dimension shifting, the characterisation of derived functors as universal delta-functors, the use of acyclic resolutions, and the elementary vanishing and additivity properties. It is the direct continuation of *Homological Algebra*.

Throughout, $\mathcal{A}$ and $\mathcal{B}$ are abelian categories, $F:\mathcal{A}\to\mathcal{B}$ is an additive functor, and the case $F=\operatorname{Hom}_R(M,-)$ or $F=-\otimes_RM$ over a commutative ring $R$ with $1 \neq 0$ is kept in view. The article assumes the complexes, resolutions, the comparison theorem and the long exact sequence of *Homological Algebra*, and the abelian-category framework of *Abelian and Grothendieck Categories*, in particular the existence of enough projectives or enough injectives. No topology and no form occurs; the words *complex*, *resolution* and *limit* are algebraic, and the applications of the theory to sheaf cohomology and to the cohomology of spaces require a site or a space and therefore belong to Part II, where they are treated in *Sheaves and Cohomology* and *Algebraic Topology*. The general composition of derived functors is stated here and its computational form, the Grothendieck spectral sequence, is developed.

## The Construction

### Right Derived Functors

**Definition.** Let $\mathcal{A}$ have enough injectives and let $F:\mathcal{A}\to\mathcal{B}$ be a covariant left exact functor. For an object $A$ of $\mathcal{A}$ choose an injective resolution $0\to A\to I^0\to I^1\to\cdots$, apply $F$, and form the cochain complex

$$
0\longrightarrow F(I^0)\xrightarrow{\ F(d^0)\ } F(I^1)\xrightarrow{\ F(d^1)\ }\cdots .
$$

The **right derived functors** of $F$ are

$$
R^nF(A)=H^n\bigl(F(I^\bullet)\bigr), \qquad n \ge 0 .
$$

**Definition.** Dually, let $\mathcal{A}$ have enough projectives and let $G:\mathcal{A}\to\mathcal{B}$ be a covariant right exact functor. For an object $A$ choose a projective resolution $P_\bullet\to A$, apply $G$, and form $G(P_\bullet)$; the **left derived functors** are

$$
L_nG(A)=H_n\bigl(G(P_\bullet)\bigr), \qquad n \ge 0 .
$$

**Proposition.** The functors $R^nF$ and $L_nG$ are well defined up to natural isomorphism: they do not depend on the choice of resolution.

*Proof.* Let $I^\bullet,J^\bullet$ be two injective resolutions of $A$. By the comparison theorem the identity of $A$ lifts to chain maps $\varphi:I^\bullet\to J^\bullet$ and $\psi:J^\bullet\to I^\bullet$, and $\psi\varphi$ and $\varphi\psi$ are homotopic to the identities. Applying the additive functor $F$ preserves the homotopies, so $F(\varphi)$ and $F(\psi)$ are mutually inverse up to homotopy, and homotopic maps induce the same map on homology. Hence $H^n(F(I^\bullet))\cong H^n(F(J^\bullet))$ canonically. The projective case is dual. $\square$

**Proposition.** $R^0F\cong F$ when $F$ is left exact, and $L_0G\cong G$ when $G$ is right exact. In particular the derived functors extend the given functor.

*Proof.* For a left exact $F$ the sequence $0\to A\to I^0\to I^1$ is exact, so applying $F$ gives the exact sequence $0\to F(A)\to F(I^0)\to F(I^1)$; therefore $H^0(F(I^\bullet))=\ker F(d^0)\cong F(A)$. Dually, right exactness of $G$ gives $G(P_1)\to G(P_0)\to G(A)\to0$ exact, so $H_0(G(P_\bullet))=G(P_0)/\operatorname{im}G(d_1)\cong G(A)$. $\square$

### Functoriality and Additivity

**Proposition.** A morphism $u:A\to A'$ induces morphisms $R^nu:R^nF(A)\to R^nF(A')$ for every $n$, making each $R^nF$ a functor; the functors are additive, and the assignment is compatible with composition. The same holds for $L_nG$.

*Proof.* By the comparison theorem, $u$ lifts to a chain map between chosen resolutions, unique up to homotopy; applying $F$ and taking homology gives $R^nu$, independent of the lift by the same homotopy argument as above. Additivity of $R^nF$ follows from additivity of $F$ on hom complexes and of homology. $\square$

**Corollary.** The functors $R^nF$ and $L_nG$ preserve finite direct sums, $R^nF(A\oplus A')\cong R^nF(A)\oplus R^nF(A')$, since they are additive.

### Acyclic Resolutions

Injective and projective resolutions are not the only ones that compute the derived functors; any resolution by acyclic objects will do, and this is often the practical way to compute.

**Definition.** An object $Q$ is **$F$-acyclic** if $R^nF(Q)=0$ for all $n>0$; dually an object $P$ is **$G$-acyclic** if $L_nG(P)=0$ for all $n>0$.

**Theorem.** Let $F$ be left exact with enough injectives and let $0\to A\to Q^0\to Q^1\to\cdots$ be a resolution of $A$ by $F$-acyclic objects. Then $R^nF(A)\cong H^n(F(Q^\bullet))$ naturally in $A$.

*Proof.* Decompose the resolution into short exact sequences $0\to A\to Q^0\to K^1\to0$, $0\to K^1\to Q^1\to K^2\to0$, and so on, and apply the long exact sequence of the next section to each. The terms $R^nF(Q^i)$ vanish for $n>0$ because the $Q^i$ are acyclic, and the exact sequences collapse to isomorphisms
$$
R^nF(A)\cong R^{n-1}F(K^1)\cong R^{n-2}F(K^2)\cong\cdots\cong R^0F(K^n)/\cdots,
$$
which identify $R^nF(A)$ with the $n$-th cohomology of $F(Q^\bullet)$. $\square$

**Example.** Every injective object is $F$-acyclic for every left exact $F$, since an injective resolution of an injective object has length zero and shortens by the splitting of $0\to I\to I\to0\to\cdots$; this recovers the definition. The useful cases are the objects that are acyclic for a particular $F$ — for example, flat modules for the tensor product, or flasque sheaves for the global sections of a sheaf in Part II.

## The Long Exact Sequence

### The Connecting Homomorphism

**Theorem.** Let $0\to A\to B\to C\to0$ be a short exact sequence in $\mathcal{A}$ and let $F$ be left exact with enough injectives. There are connecting morphisms $\delta^n:R^nF(C)\to R^{n+1}F(A)$, natural in the short exact sequence, making

$$
0\to F(A)\to F(B)\to F(C)\xrightarrow{\ \delta^0\ } R^1F(A)\to R^1F(B)\to R^1F(C)\xrightarrow{\ \delta^1\ } R^2F(A)\to\cdots
$$

exact. Dually, a right exact $G$ with enough projectives gives a long exact sequence in $L_nG$, with connecting morphisms $L_nG(C)\to L_{n-1}G(A)$.

*Proof.* Choose injective resolutions $I^\bullet\to A$ and $J^\bullet\to C$ and use the horseshoe lemma to build a resolution $K^\bullet=I^\bullet\oplus J^\bullet$ of $B$ together with a short exact sequence of complexes $0\to I^\bullet\to K^\bullet\to J^\bullet\to0$. The horseshoe construction splits in each degree, and every additive functor preserves a split exact sequence, so $0\to F(I^\bullet)\to F(K^\bullet)\to F(J^\bullet)\to0$ is again a short exact sequence of complexes. The long exact homology sequence of *Homological Algebra* applied to it is the displayed sequence, with connecting map the snake map transported through the horseshoe identifications; the left-exactness of $F$ is what identifies the degree-zero term $H^0(F(I^\bullet))$ with $F(A)$ so that the sequence begins at $F(A)$. Naturality is the naturality of the snake lemma. The dual statement follows by reversing all arrows. $\square$

**Corollary (naturality).** A map of short exact sequences induces a map of the two long exact sequences, commuting with all connecting morphisms.

**Corollary.** If $F$ is exact then $R^nF=0$ for all $n\ge1$; more generally if $F$ is left exact and $R^1F$ is effaceable — meaning it vanishes on objects that receive an epimorphism from an acyclic object — then all higher derived functors vanish.

### Dimension Shifting

The connecting morphisms allow derived functors in high degree to be computed from those in low degree.

**Corollary (dimension shifting).** Let $0\to A\to I\to A'\to0$ be short exact with $I$ injective. Then $R^nF(A')\cong R^{n+1}F(A)$ for all $n\ge1$, and the beginning of the long exact sequence is the four-term exact sequence

$$
0\to F(A)\to F(I)\to F(A')\to R^1F(A)\to0,
$$

so that $R^1F(A)\cong\operatorname{coker}(F(I)\to F(A'))$; dually, if $0\to A'\to P\to A\to0$ is short exact with $P$ projective then $L_nG(A)\cong L_{n+1}G(A')$ for all $n\ge1$ and $L_1G(A)\cong\ker(G(A')\to G(P))$.

*Proof.* In the long exact sequence of the theorem the terms $R^nF(I)$ vanish for $n\ge1$ because $I$ is injective, so the segment
$$
R^nF(I)\to R^nF(A')\xrightarrow{\delta^n}R^{n+1}F(A)\to R^{n+1}F(I)
$$
becomes $0\to R^nF(A')\xrightarrow{\cong}R^{n+1}F(A)\to0$ for $n\ge1$. For $n=0$ the same vanishing of $R^1F(I)$ gives the segment $F(A)\to F(I)\to F(A')\xrightarrow{\delta^0}R^1F(A)\to R^1F(I)=0$, which is the displayed four-term exact sequence, and $R^1F(A)$ is the cokernel of $F(I)\to F(A')$ by the exactness at $F(A')$. The projective statement is dual: the segment $0\to L_1G(A)\to G(A')\to G(P)$ identifies $L_1G(A)$ with the kernel. $\square$

**Corollary.** If $R^nF=0$ for one $n\ge1$ then $R^mF=0$ for all $m\ge n$: the vanishing of a derived functor in degree $n$ propagates upward. Dually, if $L_nG=0$ for one $n\ge1$ then $L_mG=0$ for all $m\ge n$.

## Universal Delta-Functors

### Delta-Functors

The construction of the long exact sequence suggests an axiomatic description of derived functors that does not mention resolutions.

**Definition.** A (covariant, homological) **delta-functor** from $\mathcal{A}$ to $\mathcal{B}$ consists of additive functors $T_n:\mathcal{A}\to\mathcal{B}$ for $n\ge0$ together with, for every short exact sequence $0\to A\to B\to C\to0$, connecting morphisms $\delta_n:T_n(C)\to T_{n-1}(A)$ natural in the sequence and making the long sequence $\cdots\to T_n(A)\to T_n(B)\to T_n(C)\xrightarrow{\delta_n}T_{n-1}(A)\to\cdots$ exact. A **morphism** of delta-functors is a natural transformation $T_n\to T_n'$ commuting with the $\delta$. The cohomological version has upper indices and connecting maps $\delta^n:T^n(C)\to T^{n+1}(A)$.

**Example.** The right derived functors of a left exact functor, together with the connecting morphisms constructed above, form a cohomological delta-functor. The functors $L_nG$ together with their connecting morphisms form a homological delta-functor.

### Effaceability and Universality

**Definition.** A cohomological delta-functor $T^\bullet$ is **effaceable** in degree $n>0$ if for every object $A$ there is a monomorphism $u:A\to M$ with $T^n(u)=0$; it is **universal** if every natural transformation from $T^\bullet$ to another delta-functor that is an isomorphism in degree $0$ is an isomorphism in every degree.

**Theorem.** The right derived functors of a left exact functor $F$ form a universal effaceable cohomological delta-functor with $T^0=F$; conversely, any effaceable cohomological delta-functor with $T^0=F$ that vanishes on injectives and is defined on an abelian category with enough injectives is naturally isomorphic to the right derived functors of $F$.

*Proof.* Effaceability in degree $n$ holds by embedding $A$ in an injective $M$, since $R^nF(M)=0$. For universality, let $\eta:T^\bullet\to U^\bullet$ be a morphism of delta-functors that is an isomorphism in degree $0$. One shows by induction on $n$ that $\eta$ is an isomorphism in degree $n$: embed $A$ in an injective $M$ and form $0\to A\to M\to A'\to0$; the two long exact sequences are connected by $\eta$, and the five lemma reduces the statement in degree $n$ for $A$ to the statement in degree $n-1$ for $A'$ and the known vanishing of $T^n(M)=U^n(M)=0$ for $n>0$. The converse follows because a universal delta-functor is determined by its degree-$0$ term, which is $F$. $\square$

**Corollary.** Any construction that produces an effaceable delta-functor with $T^0=F$ computes the derived functors of $F$. This is the criterion by which the derived functors of the tensor product, the group cohomology functors and the sheaf cohomology functors are identified, and it is the reason resolutions by acyclic objects suffice.

## Composition of Functors

When two left exact functors are composed, the derived functors of the composite are computed by a spectral sequence from the derived functors of the factors. The full statement and its proof lie outside this article; here the clean case is recorded, in which one functor sends injectives to acyclics.

**Theorem (Grothendieck, elementary case).** Let $F:\mathcal{A}\to\mathcal{B}$ and $G:\mathcal{B}\to\mathcal{C}$ be left exact functors between abelian categories with enough injectives. Suppose that $F$ sends injective objects of $\mathcal{A}$ to $G$-acyclic objects, that is, $R^nG(F(I))=0$ for every injective $I$ and every $n\ge1$. Then for every object $A$ of $\mathcal{A}$ there are natural isomorphisms

$$
R^n(GF)(A)\cong R^nG(FA), \qquad n\ge0 .
$$

*Proof.* Take an injective resolution $I^\bullet$ of $A$. By hypothesis each $F(I^n)$ is $G$-acyclic, so the resolution $F(I^\bullet)$ of $FA$ by $G$-acyclic objects computes $R^nG(FA)$ by the acyclic-resolution theorem. But $R^n(GF)(A)$ is by definition $H^n(GF(I^\bullet))=H^n(G(F(I^\bullet)))$, which is also $R^nG(FA)$. $\square$

**Remark.** When the hypothesis fails, the two sides are related by the Grothendieck spectral sequence $E_2^{p,q}=R^pG(R^qF(A))\Rightarrow R^{p+q}(GF)(A)$, developed. The elementary statement above is the case in which the spectral sequence collapses to its edge; the general statement is the reason the composition of derived functors is the main computational tool of the theory.

## Elementary Properties and Examples

### Exactness and Vanishing

**Proposition.** Let $F$ be left exact with enough injectives. Then $F$ is exact if and only if $R^1F=0$, if and only if $R^nF=0$ for all $n\ge1$. Dually a right exact $G$ is exact if and only if $L_1G=0$.

*Proof.* If $F$ is exact it preserves the exactness of an injective resolution, so the complex $F(I^\bullet)$ is exact in positive degrees and $R^nF=0$ for $n\ge1$. Conversely, if $R^1F=0$ then the dimension-shifting corollary gives $R^nF=0$ for all $n\ge1$, and the long exact sequence attached to a short exact sequence has $F$ exact in the middle by exactness of the sequence and the vanishing of $R^1F(A)$. The dual argument gives the statement for $G$. $\square$

**Example.** $\operatorname{Hom}_R(M,-)$ is exact if $M$ is projective, so its derived functors vanish in positive degree for projective $M$; $\operatorname{Hom}_R(P,-)$ has zero right derived functors. Dually, $\operatorname{Hom}_R(-,I)$ is exact for injective $I$, so the left exact $\operatorname{Hom}_R(-,I)$ has vanishing right derived functors in positive degree. These observations are the module-level content of the vanishing of $\operatorname{Ext}$.

**Example.** $-\otimes_RM$ is exact when $M$ is flat, so $L_n(-\otimes_RM)=0$ for $n\ge1$ when $M$ is flat. This is the homological characterisation of flatness, and it is used in the article *Flatness and Exactness* for the ideal criterion. The functor $L_n(-\otimes_RM)$ is written $\operatorname{Tor}_n^R(-,M)$, and its theory is developed.

### The Functors $\operatorname{Ext}$ and $\operatorname{Tor}$

Two cases are so important that they receive names.

**Definition.** For $R$-modules $M,N$ the **right derived functors** of $\operatorname{Hom}_R(M,-)$ are written

$$
\operatorname{Ext}_R^n(M,N)=R^n\operatorname{Hom}_R(M,-)(N),
$$

computed from an injective resolution of $N$; equivalently, since $\operatorname{Hom}_R(-,N)$ is left exact, they are the right derived functors of the contravariant functor $\operatorname{Hom}_R(-,N)$ computed from a projective resolution of $M$. The **left derived functors** of $-\otimes_RN$ are written

$$
\operatorname{Tor}_n^R(M,N)=L_n(-\otimes_RN)(M),
$$

computed from a projective resolution of $M$.

The identification of the two computations of $\operatorname{Ext}^n$, the interpretation of $\operatorname{Ext}^1$ as extension classes, the universal coefficient theorem, the Künneth formula and the theory of $\operatorname{Tor}$ for two variables are not covered here. Here the two families are introduced only as the derived functors of the two basic module functors, and their long exact sequences and vanishing properties are those of the general theory.

**Example (group cohomology).** For a group $G$ and a $G$-module $M$, the functor $M\mapsto M^G$ of invariants is left exact, and its right derived functors $H^n(G,M)$ are the group cohomology; the functor of coinvariants is right exact and its left derived functors are the group homology. The category of $G$-modules is the category of left modules over the group ring $\mathbb{Z}[G]$, an algebra object of Part I, so group cohomology is an instance of the theory of this article. The group-cohomological development is given in the companion article *Group Cohomology* of the *Groups* category, being written in the same batch.

**Example (sheaf cohomology, Part II).** For a sheaf of abelian groups on a site, the global-section functor is left exact and its right derived functors are the sheaf cohomology groups $H^n(X,\mathcal{F})$. The algebraic input is this article and *Homological Algebra*; the site, its Grothendieck topology and the geometric meaning of the cohomology are the subject of Part II, where they are treated in *Sheaves and Cohomology*; the categorical framework is supplied by *Abelian and Grothendieck Categories*.

### Base Change and Derived Functors

**Proposition.** Let $\varphi:R\to S$ be a homomorphism of commutative rings. For every $R$-module $M$ and every $S$-module $N$ there are natural isomorphisms

$$
\operatorname{Ext}_S^n(S\otimes_RM,N)\cong\operatorname{Ext}_R^n(M,\operatorname{Res}N), \qquad n\ge0,
$$

where $\operatorname{Res}N$ is $N$ regarded as an $R$-module. If in addition $S$ is flat as an $R$-module, then also

$$
\operatorname{Tor}_n^S(S\otimes_RM,N)\cong\operatorname{Tor}_n^R(M,\operatorname{Res}N), \qquad n\ge0 .
$$

*Proof.* The adjunction between extension and restriction of scalars gives a natural isomorphism of functors $\operatorname{Hom}_S(S\otimes_RM,-)\cong\operatorname{Hom}_R(M,\operatorname{Res}-)$. Restriction of scalars is exact and carries injective $S$-modules to injective $R$-modules, so an injective resolution of $N$ over $S$ restricts to an injective resolution of $\operatorname{Res}N$ over $R$ and computes the right derived functors on both sides; this gives the first family. For the second, restriction along a flat $\varphi$ makes $S\otimes_R-$ exact, so it carries a projective resolution of $M$ to a projective resolution of $S\otimes_RM$; applying $-\otimes_SN$ and using $(S\otimes_RP)\otimes_SN\cong P\otimes_R\operatorname{Res}N$ gives the isomorphism on homology. Without flatness the two Tor families are related by a spectral sequence rather than by an isomorphism. $\square$

## Summary

The right derived functors $R^nF$ of a left exact functor $F$ are computed by applying $F$ to an injective resolution of the object and taking cohomology; the left derived functors $L_nG$ of a right exact functor are dual. The comparison theorem of *Homological Algebra* makes the answer independent of the resolution, and additivity makes the derived functors additive and compatible with finite direct sums. One has $R^0F\cong F$ and $L_0G\cong G$, so the derived functors extend the original functor.

A short exact sequence produces a long exact sequence of derived functors with natural connecting morphisms, constructed from a short exact sequence of resolutions and the long exact homology sequence. The connecting morphisms yield dimension shifting, which computes a derived functor in high degree from one in low degree and propagates vanishing: if $R^nF=0$ for one $n\ge1$ then all higher ones vanish, and likewise for $L_nG$. Any resolution by $F$-acyclic objects computes $R^\bullet F$, and the derived functors are characterised as the universal effaceable delta-functor with degree-zero term $F$; a functor is exact precisely when its positive derived functors vanish.

The two basic module functors give the named families $\operatorname{Ext}_R^n(M,N)=R^n\operatorname{Hom}_R(M,-)(N)$ and $\operatorname{Tor}_n^R(M,N)=L_n(-\otimes_RN)(M)$, whose detailed theory is not covered here. The composition of two left exact functors has derived functors computed by those of the factors when the first sends injectives to acyclics, and in general by the Grothendieck spectral sequence. Every statement is algebraic; the sheaf-cohomological realisation needs a site and belongs to Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{A}$, $\mathcal{B}$ | abelian categories |
| $F$, $G$ | additive functors; $F$ left exact, $G$ right exact |
| $R^nF$ | right derived functors of a left exact functor |
| $L_nG$ | left derived functors of a right exact functor |
| $I^\bullet$, $P_\bullet$ | injective and projective resolutions |
| $\delta^n$, $\delta_n$ | connecting morphisms of the long exact sequence |
| $F$-acyclic, $G$-acyclic | object with vanishing positive derived functors |
| $T^\bullet$, $T_\bullet$ | (co)homological delta-functor |
| $\operatorname{Ext}_R^n(M,N)$ | right derived functors of $\operatorname{Hom}_R(M,-)$ |
| $\operatorname{Tor}_n^R(M,N)$ | left derived functors of $-\otimes_RN$ |
| $\operatorname{Res}N$ | restriction of scalars along $R\to S$ |
| $H^n(G,M)$ | group cohomology, an instance over $\mathbb{Z}[G]$ |





## Further Reading

- Henri Cartan and Samuel Eilenberg, *Homological Algebra* (Princeton University Press, 1956), for the construction of derived functors from resolutions.
- Alexander Grothendieck, "Sur quelques points d'algèbre homologique", *Tohoku Mathematical Journal* 9 (1957), 119–221, for the theory of abelian categories, effaceability and the spectral sequence of composed functors.
- Peter J. Hilton and Urs Stammbach, *A Course in Homological Algebra*, 2nd ed. (Springer, 1997), for delta-functors and dimension shifting.
- Saunders Mac Lane, *Homology* (Springer, 1995), for the universal property of derived functors and the comparison theorem.
- Barry Mitchell, "The full imbedding theorem", *American Journal of Mathematics* 86 (1964), 619–637, for the categorical setting of the construction.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for the long exact sequences and the elementary computations.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for derived functors, delta-functors and the Grothendieck spectral sequence.
