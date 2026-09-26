
# __Spectral Sequences__

## Introduction

A spectral sequence is a bookkeeping device for the homology of an object that carries a filtration. It replaces a single unknown graded group by a succession of approximations, each an algebraic invariant of the previous one, converging to the graded pieces of the answer. The device is forced on us whenever two homological constructions are composed: the derived functors of a composite functor, the homology of a double complex, the homology of a filtered complex. In each case the spectral sequence computes the answer from a sequence of successive approximations, and the first page is built from data that can be read off directly — the homology of the filtration quotients, or the iterated derived functors of the two factors.

This article develops filtered complexes and their spectral sequences, the pages and differentials, the convergence of a spectral sequence to the homology of the filtered complex, the spectral sequences of a double complex and of a composite of functors, the five-term exact sequence and the edge homomorphisms, and the algebraic applications: the Künneth and base-change spectral sequences and the Lyndon–Hochschild–Serre spectral sequence of a group extension. It follows *Ext and Tor*, whose balance theorems and Künneth theorem it completes, and it supplies the computational tool that other articles use.

Throughout, $R$ is a commutative ring with identity $1\neq0$ and complexes are complexes of $R$-modules unless a general abelian category is named; the theory is algebraic and is stated for an abelian category with enough injectives or enough projectives where resolutions are needed. No distance, norm, open set or completion occurs; the word *convergence* has its purely algebraic meaning, that the successive pages stabilise and the stable terms are the graded pieces of a filtered graded group. The Leray–Serre spectral sequence of a fibration, the spectral sequence of a sheaf and the Atiyah–Hirzebruch spectral sequence all require a space or a site, and they belong to Part II, where they are treated in *Algebraic Topology* and *Sheaves and Cohomology*; the algebraic theory of this article is what those applications use.

## Filtrations and Their Spectral Sequences

### Filtrations of Complexes

**Definition.** A **(decreasing) filtration** of a graded object or a complex $C$ is a family of subobjects $F_pC$ for $p \in \mathbb{Z}$ with $F_{p+1}C\subseteq F_pC$ and with $F_pC_n$ defined for all $p,n$. It is **exhaustive** if $\bigcup_pF_pC=C$ and **separated** if $\bigcap_pF_pC=0$; it is **bounded below** if for each $n$ there is $p_0$ with $F_{p_0}C_n=C_n$, **bounded above** if for each $n$ there is $p_1$ with $F_{p_1}C_n=0$, and **bounded** if it is both, so that for each $n$ only finitely many of the graded pieces $\operatorname{gr}_pC_n$ are nonzero. The associated graded object is $\operatorname{gr}_pC=F_pC/F_{p+1}C$.

A filtration of a complex is a filtration by subcomplexes, so that the quotient $F_pC/F_{p+1}C$ is again a complex and its homology is defined.

**Definition.** For a filtered complex $(C,F)$ the **spectral sequence of the filtration** has, for $r\ge0$,

$$
E^0_{p,q}=F_pC_{p+q}/F_{p+1}C_{p+q}, \qquad E^1_{p,q}=H_{p+q}\bigl(F_pC/F_{p+1}C\bigr),
$$

and for $r\ge1$ the terms $E^r_{p,q}$ are obtained from $E^{r-1}$ by taking homology with respect to a differential $d^{r-1}$ of bidegree $(-r+1,r-2)$; the term $E^{r+1}$ is the homology of $E^r$ with respect to $d^r$. The bidegree convention is fixed so that the differential of $E^r$ has total degree $-1$,
$d^r:E^r_{p,q}\to E^r_{p-r,q+r-1}$ in homological indexing, and dually in cohomological indexing.

**Remark.** The construction is that of an **exact couple**: a pair of objects $D,E$ with maps $i:D\to D$, $j:D\to E$, $k:E\to D$ forming an exact triangle, and the derived couple obtained by replacing $D$ by $k^{-1}(\operatorname{im}i)/j(\ker i)$ and $E$ by $\ker i/j(\ker i)$. The exact couple of a filtered complex has $D$ the homology of the filtration stages and $E$ the homology of the quotients; iterating the derived couple gives the pages. It is the cleanest proof that the pages exist and that $d^2=0$, but it is not needed for the computations below and is not developed further here.

**Example.** For the filtration of a complex by the degree filtration $F_pC=C$ for $p\le0$, $F_pC=0$ for $p>0$, the spectral sequence has $E^1=E^0$ equal to the homology of the complex in the only column; it converges to the homology of the complex.

### Convergence

**Definition.** A spectral sequence $(E^r,d^r)$ **converges** to a filtered graded object $H$ if for every $(p,q)$ the terms $E^r_{p,q}$ are independent of $r$ for large $r$, with stable value $E^\infty_{p,q}$, and $E^\infty_{p,q}\cong F_pH_{p+q}/F_{p+1}H_{p+q}$ for a filtration of $H$; one writes $E^2_{p,q}\Rightarrow H_{p+q}$.

**Theorem.** Let $(C,F)$ be a filtered complex whose filtration is exhaustive, separated and bounded. Then the spectral sequence of the filtration converges to the homology of $C$: for every $n$,

$$
E^\infty_{p,q}\cong\frac{F_pH_{p+q}(C)}{F_{p+1}H_{p+q}(C)},
$$

and the filtration of $H_n(C)$ induced by $F$ has the indicated graded pieces.

*Proof.* The filtration restricts to filtrations of the cycles and the boundaries, $F_pZ_n=Z_n\cap F_pC_n$ and $F_pB_n=B_n\cap F_pC_n$, and the first page is
$$
E^1_{p,q}=H_{p+q}\bigl(F_pC/F_{p+1}C\bigr)\cong\frac{F_pZ_{p+q}}{F_pB_{p+q}+F_{p+1}Z_{p+q}} .
$$
The differentials of the pages are induced by the boundary of $C$, and the stable terms satisfy
$$
E^\infty_{p,q}\cong\frac{F_pH_{p+q}(C)}{F_{p+1}H_{p+q}(C)}, \qquad F_pH_n(C)=\frac{F_pZ_n+B_n}{B_n} .
$$
Boundedness makes the filtrations of each $Z_n$, $B_n$ and $H_n$ finite, so the successive quotients stabilise after finitely many pages and the limit is attained. $\square$

**Definition.** A spectral sequence **degenerates at the $E^r$-page** if $d^s=0$ for all $s\ge r$, so that $E^r\cong E^\infty$ and the successive pages are unchanged. In that case $E^r_{p,q}\cong F_pH_{p+q}/F_{p+1}H_{p+q}$ for all $(p,q)$, and the homology is determined by the $E^r$-page up to extension problems.

**Remark.** A spectral sequence computes the graded pieces of a filtered homology, not the homology itself. The remaining ambiguity is the **extension problem**: reconstructing $H_n$ from the successive quotients $E^\infty_{p,q}$ with $p+q=n$. When the filtration has only two nontrivial steps this is a short exact sequence; when it has more, additional data are needed. The explicit computations below are chosen so that the extension problem is solvable, either by degeneracy or by a complementary argument.

## The Spectral Sequence of a Double Complex

### Statement

**Theorem.** Let $C_{\bullet\bullet}$ be a double complex with commuting horizontal and vertical differentials and total complex $\operatorname{Tot}(C)$. If for each $n$ only finitely many $C_{p,q}$ with $p+q=n$ are nonzero, then there are two spectral sequences converging to the homology of the total complex,

$$
{}^IE^2_{p,q}=H^{\mathrm{h}}_p H^{\mathrm{v}}_q(C)\Longrightarrow H_{p+q}\bigl(\operatorname{Tot}C\bigr), \qquad {}^{II}E^2_{p,q}=H^{\mathrm{v}}_q H^{\mathrm{h}}_p(C)\Longrightarrow H_{p+q}\bigl(\operatorname{Tot}C\bigr),
$$

where $H^{\mathrm{h}}$ and $H^{\mathrm{v}}$ denote homology with respect to the horizontal and the vertical differentials.

*Proof.* Filter $\operatorname{Tot}(C)$ by the column degree, $F_p\operatorname{Tot}(C)_n=\bigoplus_{p'\ge p}C_{p',n-p'}$, so that the filtration is exhaustive, separated and bounded under the finiteness hypothesis. The $E^0$-page has $E^0_{p,q}=C_{p,q}$, and the differential $d^0$ is the vertical differential up to a sign; hence $E^1_{p,q}=H^{\mathrm{v}}_q(C_{p,\bullet})$ and $E^2_{p,q}=H^{\mathrm{h}}_pH^{\mathrm{v}}_q(C)$, by the sign rule that makes the total differential square to zero. The convergence is the theorem on filtered complexes. The second spectral sequence is obtained from the filtration by rows. $\square$

**Proposition.** If the columns of the double complex are exact, then $E^1_{p,q}=H^{\mathrm{v}}_q(C_{p,\bullet})=0$ for all $(p,q)$ and the spectral sequence collapses, so the total complex is exact; dually, exactness of the rows kills the second spectral sequence and forces $H_n(\operatorname{Tot}C)=0$ for all $n$.

*Proof.* If the columns are exact then $H^{\mathrm{v}}_q(C_{p,\bullet})=0$ for all $p,q$, so $E^1=0$ and hence $E^\infty=0$, which forces $H_n(\operatorname{Tot}C)=0$ for all $n$. The row statement is the same argument applied to the transposed double complex. $\square$

### Applications to Balance and Künneth

**Example (balance of Tor).** Let $P_\bullet\to M$ and $Q_\bullet\to N$ be projective resolutions over $R$ and form the double complex $P_p\otimes_RQ_q$. Its rows and columns are exact in positive degrees because the $P_p$ and $Q_q$ are flat, and the two spectral sequences give $H_n(\operatorname{Tot}(P\otimes Q))\cong\operatorname{Tor}_n^R(M,N)$ in two ways, one computing $\operatorname{Tor}_n^R(M,N)$ from the resolution of $M$ and the other from the resolution of $N$. This proves the symmetry of Tor stated in *Ext and Tor*. The same computation with $\operatorname{Hom}_R(P_p,I^q)$ in place of the tensor product, for an injective resolution $I^\bullet$ of $N$, proves the balance of the two computations of $\operatorname{Ext}$.

**Example (Künneth spectral sequence).** For complexes of flat modules $C_\bullet,D_\bullet$ with $C_\bullet$ bounded below there is a spectral sequence

$$
E^2_{p,q}=\bigoplus_{p'+q'=q}\operatorname{Tor}_p^R\bigl(H_{p'}(C),H_{q'}(D)\bigr)\Longrightarrow H_{p+q}(C\otimes_RD),
$$

obtained from the double complex $C_p\otimes_RD_q$. Over a principal ideal domain $\operatorname{Tor}_p=0$ for $p\ge2$, so only the columns $p=0$ and $p=1$ are nonzero and the sequence degenerates at the $E^2$-page, giving the Künneth short exact sequence of *Ext and Tor*, whose unnatural splitting makes the spectral sequence the cleaner statement.

## The Spectral Sequence of a Composite of Functors

### Statement

**Theorem (Grothendieck).** Let $\mathcal{A},\mathcal{B},\mathcal{C}$ be abelian categories with enough injectives, let $F:\mathcal{A}\to\mathcal{B}$ and $G:\mathcal{B}\to\mathcal{C}$ be left exact covariant functors, and suppose that $F$ carries injective objects of $\mathcal{A}$ to $G$-acyclic objects of $\mathcal{B}$. Then for every object $A$ of $\mathcal{A}$ there is a first-quadrant spectral sequence

$$
E_2^{p,q}=R^pG\bigl(R^qF(A)\bigr)\Longrightarrow R^{p+q}(GF)(A),
$$

natural in $A$, with differentials $d^r:E^r_{p,q}\to E^r_{p+r,q-r+1}$.

*Proof.* Take an injective resolution $A\to I^\bullet$ and apply the Cartan–Eilenberg resolution of the complex $F(I^\bullet)$ by injectives, then apply $G$; the result is a double complex whose two spectral sequences are as follows. In one direction the $q$-variable computes the derived functors of $F$ and the $p$-variable applies $G$ to injectives, giving $E_2^{p,q}=R^pG(R^qF(A))$; in the other direction $E_2^{p,q}=0$ for $q\neq0$, because each $F(I^q)$ is $G$-acyclic, so that sequence collapses and the abutment is $R^{p+q}(GF)(A)$. The hypothesis on injectives is exactly what makes the second direction degenerate. $\square$

**Corollary (five-term exact sequence).** Under the hypotheses, for every object $A$ there is an exact sequence

$$
0\to R^1G(FA)\to R^1(GF)(A)\to G\bigl(R^1F(A)\bigr)\xrightarrow{\ d_2^{0,1}\ } R^2G(FA)\to R^2(GF)(A),
$$

obtained from the low-degree terms of the spectral sequence together with the edge homomorphisms.

*Proof.* The sequence is the exact sequence of the terms $E_2^{0,0},E_2^{1,0},E_2^{0,1},E_2^{2,0},E_2^{1,1}$ of the spectral sequence, using the identifications $E_2^{p,0}=R^pG(FA)$ and $E_2^{0,q}=G(R^qF(A))$ and the convergence to $R^{p+q}(GF)(A)$. Exactness is the general exactness of the low-degree part of a first-quadrant spectral sequence. $\square$

### Edge Homomorphisms

**Definition.** For a first-quadrant spectral sequence converging to $H$, the **edge homomorphisms** are the natural maps

$$
E^2_{p,0}\twoheadrightarrow E^\infty_{p,0}\hookrightarrow F_pH_p/F_{p+1}H_p\hookrightarrow H_p, \qquad H_p\twoheadrightarrow F_0H_p/F_1H_p\hookrightarrow E^\infty_{0,p}\hookrightarrow E^2_{0,p},
$$

obtained from the inclusions and projections of the filtration. They are the comparison maps between the abutment and the two edges of the spectral sequence.

**Example.** In the Grothendieck spectral sequence the edge homomorphisms give the natural maps $R^pG(FA)\to R^p(GF)(A)$ and $R^p(GF)(A)\to G(R^pF(A))$; the five-term exact sequence is the statement that they fit into an exact sequence.

## Algebraic Examples

### The Base-Change Spectral Sequence

**Theorem.** Let $\varphi:R\to S$ be a homomorphism of commutative rings, let $M$ be an $R$-module and $N$ an $S$-module. There is a first-quadrant spectral sequence

$$
E_2^{p,q}=\operatorname{Tor}_p^S\bigl(\operatorname{Tor}_q^R(S,M),N\bigr)\Longrightarrow\operatorname{Tor}_{p+q}^R(M,\operatorname{Res}N),
$$

where $\operatorname{Res}N$ is $N$ regarded as an $R$-module. When $S$ is flat over $R$ the terms $\operatorname{Tor}_q^R(S,M)$ vanish for $q\ge1$ and the spectral sequence degenerates to the isomorphism $\operatorname{Tor}_n^S(S\otimes_RM,N)\cong\operatorname{Tor}_n^R(M,\operatorname{Res}N)$ of *Derived Functors*.

*Proof.* Apply the Grothendieck spectral sequence to the composite of the right exact functors $M\mapsto S\otimes_RM$ and $-\otimes_SN$, using left derived functors in place of right; equivalently, apply the spectral sequence of the double complex obtained from resolutions of $M$ over $R$ and of $N$ over $S$. The degeneration in the flat case is the vanishing of the higher Tor over $R$ of the flat module $S$. $\square$

### The Lyndon–Hochschild–Serre Spectral Sequence

**Theorem.** Let $N$ be a normal subgroup of a group $G$, let $M$ be a $G$-module over $\mathbb{Z}$, and regard $M$ as an $N$-module by restriction. There is a first-quadrant spectral sequence

$$
E_2^{p,q}=H^p\bigl(G/N,H^q(N,M)\bigr)\Longrightarrow H^{p+q}(G,M),
$$

where the coefficient system $H^q(N,M)$ for $G/N$ comes from the conjugation action of $G$ on $N$.

*Proof.* The functor of $G$-invariants is the composite of the functors of $N$-invariants and of $(G/N)$-invariants: $M^G=(M^N)^{G/N}$. Both are left exact, and the functor $M\mapsto M^N$ carries injective $\mathbb{Z}[G]$-modules to injective $\mathbb{Z}[G/N]$-modules, because restriction along $G\to G/N$ has an exact left adjoint and preserves the relevant classes; the Grothendieck spectral sequence applied to this composite, with the identification $H^n(G,M)=\operatorname{Ext}^n_{\mathbb{Z}[G]}(\mathbb{Z},M)$ of *Ext and Tor*, is the displayed spectral sequence. The action of $G/N$ on $H^q(N,M)$ is the one induced by conjugation. $\square$

**Example.** For the trivial coefficient module $M=\mathbb{Z}$ the five-term exact sequence of the theorem becomes the inflation–restriction exact sequence relating $H^1(G/N,\mathbb{Z})$, $H^1(G,\mathbb{Z})$, $H^1(N,\mathbb{Z})^{G/N}$, $H^2(G/N,\mathbb{Z})$ and $H^2(G,\mathbb{Z})$.

### Composites in Practice

The Grothendieck spectral sequence is the source of most of the spectral sequences in algebra. Three instances are worth recording: the **base-change** sequence above, for a change of ring; the **Künneth** sequence, for the tensor product of complexes and the composite of the tensor and homology functors; and the **change-of-rings** sequence for group cohomology. In each case the $E^2$-page is built from two known families and the differentials assemble them into the answer. The geometric instances — the Leray spectral sequence of a map of spaces, the Leray–Serre spectral sequence of a fibration, the Atiyah–Hirzebruch spectral sequence of a generalised cohomology theory, and the spectral sequence of a filtered complex of sheaves on a site — require a space or a site and are developed in Part II, in *Algebraic Topology* and *Sheaves and Cohomology*. The algebraic theory of this article is the input to those constructions, and their statements are deferred there explicitly.

## Degeneration and Practical Computation

### Recognising Degeneration

**Proposition.** A first-quadrant spectral sequence $(E^r)$ with $E^2_{p,q}=0$ for all $q>0$ degenerates at $E^2$, and $H_n\cong E^2_{n,0}$. Similarly, if $E^2_{p,q}=0$ for all $p>0$ then it degenerates at $E^2$ and $H_n\cong E^2_{0,n}$. More generally, if the differentials must land in a vanishing region, they vanish and the sequence degenerates.

*Proof.* The differential on $E^2$ maps $E^2_{p,q}\to E^2_{p+2,q-1}$; if $q=0$ the target is zero in the first case, and if $p=0$ the source is zero in the second. Inductively the same vanishing kills every higher differential on the surviving region. $\square$

**Theorem.** If a first-quadrant spectral sequence converges to $H$ and $E^2_{p,q}=0$ for all $q\neq0$, then the edge homomorphism $E^2_{p,0}\to H_p$ is an isomorphism for every $p$, and the filtration of $H_p$ has a single nontrivial step.

*Proof.* The only nonzero column contributes in each total degree, so $F_pH_p/F_{p+1}H_p=E^\infty_{p,0}=E^2_{p,0}$ and all other graded pieces vanish; the edge map is the composite of the projection and the inclusion, which are inverse to the identifications. $\square$

### The Extension Problem in Low Degree

**Proposition.** For a first-quadrant spectral sequence converging to $H$ whose differentials vanish from $E^3$ onward, so that $E^\infty=H(E^2,d_2)$, the low-degree terms fit into the exact sequence

$$
0\to E^2_{1,0}\to H_1\to E^2_{0,1}\xrightarrow{\ d_2^{0,1}\ } E^2_{2,0}\to H_2 ,
$$

the last map having kernel the image of $d_2^{0,1}$; the map $H_2\to E^2_{0,2}$ induced by the filtration has image $\ker d_2^{0,2}$, and the kernel of that map is the next filtration step, which contains the image of $E^2_{2,0}$ and equals it exactly when the stable term $E^\infty_{1,1}$ vanishes.

*Proof.* Convergence gives the filtration steps $F_1H_1/F_2H_1=E^\infty_{1,0}=E^2_{1,0}$, $F_0H_1/F_1H_1=E^\infty_{0,1}=\ker d_2^{0,1}$ and $F_0H_2/F_1H_2=E^\infty_{0,2}=\ker d_2^{0,2}$, while $E^\infty_{2,0}=E^2_{2,0}/\operatorname{im}d_2^{0,1}$ is the smallest step of the filtration of $H_2$; assembling the successive quotients gives the displayed exactness. $\square$

**Proposition.** If only the two columns $p=0$ and $p=1$ of a first-quadrant spectral sequence are nonzero, then every differential vanishes, $E^\infty=E^2$, and for every $n$ there is a short exact sequence

$$
0\to E^2_{1,n-1}\to H_n\to E^2_{0,n}\to0 ,
$$

so the extension problem in degree $n$ is the extension of $E^2_{0,n}$ by $E^2_{1,n-1}$. This is the situation of the Künneth spectral sequence of a tensor product over a principal ideal domain, where $\operatorname{Tor}_p$ vanishes for $p\ge2$ and only the columns $p=0,1$ survive.

*Proof.* The differential $d^r$ changes the column by $r$, so $d^r=0$ for $r\ge2$ when only the columns $0$ and $1$ are present; the only differential that may be nonzero is $d^1$, and it is absorbed into the passage from $E^1$ to $E^2$, so that $E^\infty=E^2$. The filtration of $H_n$ is then the two-step filtration $0\subseteq F_1H_n\subseteq H_n$ with graded pieces $E^\infty_{1,n-1}=E^2_{1,n-1}$ and $E^\infty_{0,n}=E^2_{0,n}$, which is the displayed short exact sequence. $\square$

## Summary

A filtration of a complex produces a spectral sequence whose zeroth page consists of the filtration quotients, whose first page is the homology of those quotients, and whose successive pages are obtained by taking homology with respect to differentials of increasing bidegree. If the filtration is exhaustive, separated and bounded, the spectral sequence converges to the homology of the complex: the stable terms $E^\infty_{p,q}$ are the graded pieces of a filtration of $H_{p+q}$, and the reconstruction of the homology itself from those graded pieces is the extension problem. Degeneration at a finite page removes the problem; the low-degree terms of any first-quadrant sequence give edge homomorphisms and a five-term exact sequence.

A double complex with commuting differentials and finitely many nonzero entries in each total degree has two spectral sequences, one computing the horizontal homology of the vertical, the other the vertical homology of the horizontal, both converging to the homology of the total complex. This is the computation that proves the balance of Ext and Tor and yields the Künneth spectral sequence. The Grothendieck spectral sequence of a composite of left exact functors has $E_2^{p,q}=R^pG(R^qF(A))$ and converges to $R^{p+q}(GF)(A)$ when $F$ carries injectives to $G$-acyclics, and the base-change and Lyndon–Hochschild–Serre spectral sequences are its two principal algebraic instances.

Every statement is algebraic. The spectral sequences attached to spaces, fibrations and sheaves require the topology of Part II and are developed there in *Algebraic Topology* and *Sheaves and Cohomology*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F_pC$ | filtration of a complex or graded object |
| $\operatorname{gr}_pC=F_pC/F_{p+1}C$ | associated graded object |
| $E^r_{p,q}$, $d^r$ | page and differential, $d^r:E^r_{p,q}\to E^r_{p-r,q+r-1}$ |
| $E^\infty_{p,q}$ | stable term of a convergent spectral sequence |
| $E^2_{p,q}\Rightarrow H_{p+q}$ | convergence to a filtered graded group |
| $\operatorname{Tot}(C)$ | total complex of a double complex $C_{p,q}$ |
| $H^{\mathrm{h}}$, $H^{\mathrm{v}}$ | horizontal and vertical homology |
| $R^pG(R^qF(A))$ | $E_2$-page of the Grothendieck spectral sequence |
| $d_2^{0,1}$ | differential appearing in the five-term exact sequence |
| $\operatorname{Tor}_p^R$, $R^pG$ | derived functors entering the examples |
| $R$ | commutative ring with $1\neq0$; $\varphi:R\to S$ a change of rings |





## Further Reading

- Henri Cartan and Samuel Eilenberg, *Homological Algebra* (Princeton University Press, 1956), for the spectral sequence of a filtered complex and of a double complex.
- Alexander Grothendieck, "Sur quelques points d'algèbre homologique", *Tohoku Mathematical Journal* 9 (1957), 119–221, for the spectral sequence of a composite of functors.
- Peter J. Hilton and Urs Stammbach, *A Course in Homological Algebra*, 2nd ed. (Springer, 1997), for exact couples, convergence and the five-term exact sequence.
- Saunders Mac Lane, *Homology* (Springer, 1995), for the spectral sequence of a filtered complex and its convergence.
- John McCleary, *A User's Guide to Spectral Sequences*, 2nd ed. (Cambridge University Press, 2001), for the working calculus of the pages and the classical examples.
- Barry Mitchell, "The full imbedding theorem", *American Journal of Mathematics* 86 (1964), 619–637, for spectral sequences in abelian categories.
- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for the Lyndon–Hochschild–Serre spectral sequence.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for exact couples, the Grothendieck spectral sequence and the Künneth spectral sequence.
