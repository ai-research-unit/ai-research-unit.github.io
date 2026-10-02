# __The Gysin Sequence of a Two-Fold Covering__

## Introduction

A two-fold covering $p : X\to B$ is a sphere bundle with fibre $S^0$, and like every sphere bundle it carries a long exact sequence — the **Gysin sequence** — relating the cohomology of the base, the cohomology of the total space, the transfer and a single class of the base, the **Euler class**. For a two-fold covering the sequence is especially transparent: the fibre has dimension zero, no suspension intervenes, and the Euler class is a degree-one class $e \in H^1(B;\mathbb{F}_2)$ that classifies the cover, so that the sequence reads the cohomology of the cover from the cohomology of the base and one class. The Euler class is the obstruction to a section, it vanishes exactly for the trivial cover, and the Gysin sequence is the exact sequence

$$
\cdots \to H^{n-1}(B;\mathbb{F}_2) \xrightarrow{\ \smile e\ } H^{n}(B;\mathbb{F}_2) \xrightarrow{\ p^*\ } H^{n}(X;\mathbb{F}_2) \xrightarrow{\ \tau\ } H^{n}(B;\mathbb{F}_2) \xrightarrow{\ \smile e\ } H^{n+1}(B;\mathbb{F}_2) \to \cdots
$$

in which the pullback, the transfer and the cup product with the Euler class are the successive maps.

The article develops the sequence. It identifies the two-fold covering with the double cover of a real line bundle, defines the Euler class and proves that it classifies the cover and vanishes exactly for the trivial one, states the Gysin sequence in cohomology with its exactness, states the dual sequence in homology with the cap product and the transfer, describes the splitting of the sequence and the transfer's role, and computes the examples of the spheres, the projective spaces, the torus and the surfaces. The general Gysin sequence of a sphere bundle and its proof from the Serre spectral sequence are those of *The Leray–Serre Spectral Sequence*; the transfer, its composition identities and its compatibility with the Euler class are those of *The Transfer and the Involution*, which precedes this article; the Euler class as the first Stiefel–Whitney class of a line bundle and the classifying spaces are those of *Vector Bundles and Characteristic Classes* and *Two-Fold Coverings and the Borel Construction*; and the cup and cap products are those of *Cup and Cap Products*. Nothing analytic and nothing geometric is used: the article is the algebra of a double cover and its classifying class.

Throughout, $p : X \to B$ is a two-fold covering of connected spaces, $\sigma$ is the deck transformation, and $e \in H^1(B;\mathbb{F}_2)$ is the Euler class; the main statements are with $\mathbb{F}_2$ coefficients, where the double cover is automatically oriented because $\mathbb{F}_2$ has no sign, and the integer-coefficient form with the twisted local system $\tilde{\mathbb Z}$ is cited at the end. The transfer is written $\tau$, in cohomology as a map $H^n(X;\mathbb{F}_2)\to H^n(B;\mathbb{F}_2)$ and in homology as a map $H_n(B;\mathbb{F}_2)\to H_n(X;\mathbb{F}_2)$. The cap product is $\cap$ and the coefficient field is $\mathbb{F}_2 = \mathbb{Z}/2$ unless stated.

## The Euler Class and the Classification

### The Line Bundle of the Double Cover

**Definition.** Let $p : X\to B$ be a two-fold covering. The deck transformation $\sigma$ acts on the product $X\times\mathbb{R}$ by $\sigma\cdot(x,t) = (\sigma x,-t)$, and the quotient

$$
L = X\times_{\mathbb{Z}/2}\mathbb{R} = \frac{X\times\mathbb{R}}{(x,t)\sim(\sigma x,-t)}
$$

is a real line bundle over $B$, the **line bundle of the double cover**; its unit sphere bundle is the double cover $X\to B$ and its unit disk bundle is the total space of the associated disk bundle.

**Proposition.** The assignment from two-fold coverings of $B$ to real line bundles over $B$ is a bijection on isomorphism classes, and the composite of the double cover with the projection to the line bundle is the sphere bundle of $L$; the cover is trivial exactly when $L$ is trivial.

*Proof.* A line bundle is the quotient of its sphere bundle by the antipodal action of the deck transformation, and conversely the associated line bundle of a double cover is the bundle displayed; the two constructions are inverse on isomorphism classes and preserve triviality. $\square$

### The Euler Class

**Definition.** The **Euler class** of the two-fold covering is the first Stiefel–Whitney class of its line bundle,

$$
e = w_1(L) \in H^1(B;\mathbb{F}_2),
$$

that is the class that classifies $L$, equivalently the class with $p^*e = 0$ that generates the kernel of the pullback $p^* : H^1(B;\mathbb{F}_2)\to H^1(X;\mathbb{F}_2)$.

**Theorem.** The Euler class satisfies $p^*e = 0$, and it is the obstruction to a section of the covering: the covering has a continuous section if and only if $e = 0$, and then and only then is it the trivial covering $B\sqcup B\to B$. The class $e$ is the image of the classifying map $B\to\mathbb{RP}^{\infty}$ of the double cover under the isomorphism $H^1(B;\mathbb{F}_2)\cong[B,\mathbb{RP}^{\infty}]$.

*Proof.* The pullback of the class of the line bundle to the total space of the sphere bundle vanishes because the tautological line over a point of the sphere bundle is trivialised by the point; the section statement is the splitting principle for the $\mathbb{Z}/2$-bundle, a section splitting the cover; and the classification of line bundles and of double covers by $H^1$ is the standard one. $\square$

### The Classification

**Theorem.** The Euler class is a bijection between the isomorphism classes of two-fold coverings of $B$ and the group $H^1(B;\mathbb{F}_2)$:

$$
\{\text{two-fold coverings of } B\}/\cong \;\longleftrightarrow\; H^1(B;\mathbb{F}_2), \qquad p \mapsto e(p),
$$

under which the trivial covering corresponds to $0$ and the connected coverings correspond to the nonzero classes; the deck transformation of the cover with class $e$ is recovered as the action of $\mathbb{Z}/2$ on the fibre of $L$.

*Proof.* The bijection between line bundles and $H^1$ with $\mathbb{F}_2$ coefficients follows from the classification of rank-one bundles by their transition functions and the identification $\mathrm{Vect}^1(B;\mathbb{F}_2)\cong H^1(B;\mathbb{F}_2)$ of *Vector Bundles and Characteristic Classes*; composing with the bijection of the first section gives the statement. $\square$

## The Gysin Sequence

### The Statement

**Theorem (Gysin sequence).** Let $p : X\to B$ be a two-fold covering with Euler class $e$, and let $\tau$ be the transfer. Then there is a long exact sequence of $\mathbb{F}_2$-vector spaces, natural for maps of two-fold coverings,

$$
\cdots \to H^{n-1}(B) \xrightarrow{\ \smile e\ } H^{n}(B) \xrightarrow{\ p^*\ } H^{n}(X) \xrightarrow{\ \tau\ } H^{n}(B) \xrightarrow{\ \smile e\ } H^{n+1}(B) \to \cdots ,
$$

the **Gysin sequence** of the covering; in it $\smile e$ is the cup product with the Euler class, $p^*$ the pullback, and $\tau$ the transfer. The composite of two successive maps is zero, $\tau\circ p^* = 0$ and $e\smile\tau = 0$, and the sequence is exact at every term.

*Proof.* The sequence is the Gysin sequence of the sphere bundle $S^0\to X\to B$ with fibre $S^0$; for such a bundle the Serre spectral sequence of the fibration has only two relevant columns and the only differential is the transgression, whose identification with the cup product by the Euler class is the standard computation, and the resulting long exact sequence is the Gysin sequence of *The Leray–Serre Spectral Sequence*. The vanishing of the two composites and the exactness are the two exactness statements of the sequence. $\square$

### The Identities and the Transfer

**Theorem.** The transfer in the Gysin sequence is characterised by the identities

$$
\tau \circ p^* = 0, \qquad \tau(\alpha \smile p^*\beta) = \tau(\alpha)\smile\beta, \qquad \tau(p^*\beta)= (\deg p)\beta = 0,
$$

for $\alpha \in H^*(X)$, $\beta \in H^*(B)$; the middle identity is the projection formula, and the last is the vanishing because the degree of the covering is $2$, which is zero in $\mathbb{F}_2$. These identities, together with the exactness, determine the transfer as the connecting homomorphism of the sequence, and they are the cohomological form of the identities of *The Transfer and the Involution*.

*Proof.* The projection formula is the naturality of the transfer under the cup product, and the vanishing of $\tau p^*$ is the composition $\tau p^* = 2$ computed in $\mathbb{F}_2$; the identification with the connecting homomorphism follows because a map with exactly these two properties and the exactness is the connecting map of the long exact sequence, by the standard uniqueness of the connecting homomorphism. $\square$

### The Homology Form

**Theorem.** Dualising the cohomology sequence, and using that $\mathbb{F}_2$ is a field, gives the **homology Gysin sequence**

$$
\cdots \to H_n(B) \xrightarrow{\ \cap\, e\ } H_{n-1}(B) \xrightarrow{\ \tau\ } H_{n-1}(X) \xrightarrow{\ p_*\ } H_{n-1}(B) \xrightarrow{\ \cap\, e\ } H_{n-2}(B) \to \cdots ,
$$

in which $\cap\,e$ is the cap product with the Euler class, $\tau$ is the homology transfer and $p_*$ is the pushforward; the transfer and the pushforward satisfy $\tau p_* = 1+\sigma_*$ and $p_*\tau = 0$, and the sequence is exact. In the homology sequence the transfer runs in the direction of the covering, from the base to the total space, dual to the cohomological transfer, and the cap product is the connecting map.

*Proof.* Dualise the cohomology sequence term by term with $\mathbb{F}_2$ coefficients, identifying $H^n = (H_n)^*$ by the universal coefficient theorem of *Cohomology and the Universal Coefficient Theorem*; the dual of the cup product with $e$ is the cap product with $e$, the dual of the pullback is the pushforward and the dual of the transfer is the homology transfer, and exactness is preserved by duality over a field. The two composition identities are the duals of the cohomological ones and the identities of *The Transfer and the Involution*. $\square$

## The Splitting and the Involutive Structure

### The Sequence as a Module over the Group Ring

**Theorem.** The involution $\sigma$ acts on $H^*(X)$, and the Gysin sequence is a sequence of modules over the group ring $\mathbb{F}_2[\mathbb{Z}/2] = \mathbb{F}_2[\sigma]/(\sigma^2-1)$; the transfer lands in the invariants, $\sigma\tau = \tau$, and the pushforward lands in the coinvariants, $p_*\sigma = p_*$. The sequence splits as a sequence of vector spaces, but not naturally: the obstruction to a natural splitting is the Euler class, and the sequence of $\mathbb{F}_2[\sigma]$-modules is the algebraic content of the double cover.

*Proof.* The action of $\sigma$ on the cohomology of the cover is a module structure, the transfer and the pushforward are equivariant in the stated sense by the identities of *The Transfer and the Involution*, and the exactness gives the module sequence; the non-naturality of the splitting is measured by the extension class, which is the Euler class. $\square$

### The Split Case

**Theorem.** If the Euler class vanishes the covering is trivial, $X\cong B\sqcup B$, the transfer is the projection onto the first copy, and the Gysin sequence splits: $H^*(X)\cong H^*(B)\oplus H^*(B)$ with the two copies exchanged by the deck transformation. Conversely, if the sequence splits naturally with $H^*(X)\cong H^*(B)\oplus H^*(B)$ as modules, then $e=0$.

*Proof.* For the trivial covering the transfer and the pullback are the two projections and the inclusion of the two copies, and the sequence is the short exact sequence $0\to H^*(B)\to H^*(B)\oplus H^*(B)\to H^*(B)\to 0$; conversely the natural splitting exhibits $p^*$ as a split injection, so the connecting map $\smile e$ is zero on the image of the transfer and the exactness forces $e=0$. $\square$

## Integer Coefficients and the Orientation

### The Local System of the Covering

**Definition.** The **orientation local system** of the two-fold covering is the local system $\mathbb{Z}^{tw}$ on $B$ whose fibre is $\mathbb{Z}$ and whose monodromy along a loop is multiplication by $+1$ or $-1$ according to whether the loop lifts to a closed or an open path in the cover; its mod 2 reduction is the constant system $\mathbb{F}_2$, and the covering is orientable in the sense of the local system exactly when the monodromy is trivial, which happens exactly for the trivial cover.

**Theorem.** With integer coefficients the Gysin sequence holds with the orientation local system in the $\smile e$ and $\tau$ terms,

$$
\cdots \to H^{n}(B;\mathbb{Z}^{tw}) \xrightarrow{\ \smile e\ } H^{n+1}(B;\mathbb{Z}) \xrightarrow{\ p^*\ } H^{n+1}(X;\mathbb{Z}) \xrightarrow{\ \tau\ } H^{n+1}(B;\mathbb{Z}^{tw}) \to \cdots ,
$$

so that the coefficients change along the sequence according to the monodromy; the mod 2 sequence of the article is the reduction of this one, where the local system becomes constant because $\mathbb{F}_2$ has no sign, and the untwisted integer sequence holds only for the trivial cover. The discrepancy between the integer and the mod 2 forms is exactly the orientation of the covering.

*Proof.* The Serre spectral sequence of the $S^0$-bundle has local coefficients $H^*(S^0)$ twisted by the monodromy, which is the stated local system; reducing modulo two makes the monodromy trivial and gives the constant sequence. $\square$

## The Euler Class as an Obstruction

### The Obstruction-Theoretic Reading

**Theorem.** The Euler class is the primary obstruction to a section of the covering: $e \in H^1(B;\mathbb{F}_2) = H^1(B;\pi_0(S^0))$ is the obstruction class, and the covering has a continuous section if and only if $e=0$, if and only if the covering is trivial. This is the case of the obstruction theory of *Equivariant Obstruction Theory* with the fibre $S^0$ and the trivial coefficient system over the base, the group being trivial in the base direction.

*Proof.* The section problem for the $S^0$-bundle is the extension problem over the 1-skeleton with coefficients $\pi_0(S^0)=\mathbb{Z}/2$, and the primary obstruction is the Euler class by the identification of the obstruction cocycle with the classifying class of the bundle; the vanishing of the primary obstruction is the existence of a section for a bundle whose fibre is discrete. $\square$

### The Kernel and the Connectivity

**Corollary.** The kernel of the pullback in degree one is generated by the Euler class,

$$
\ker\bigl(p^* : H^1(B;\mathbb{F}_2) \to H^1(X;\mathbb{F}_2)\bigr) = \langle e \rangle ,
$$

so the covering is connected if and only if $e \neq 0$; for a connected base the total space is connected exactly when the covering is non-trivial, and the trivial covering has two components exchanged by the deck transformation.

*Proof.* The exactness of the Gysin sequence at $H^1(B)$ gives the kernel as the image of $\smile e : H^0(B)\to H^1(B)$, which is the span of $e$ because $H^0(B;\mathbb{F}_2)=\mathbb{F}_2$; a two-fold cover is connected exactly when it is non-trivial. $\square$

## Examples

**Example (the spheres and the projective spaces).** For the antipodal covering $S^n\to\mathbb{RP}^n$ the Euler class is the generator $x\in H^1(\mathbb{RP}^n;\mathbb{F}_2)$ and the Gysin sequence reads

$$
0 \to H^0(B) \xrightarrow{\ \smile x\ } H^1(B) \xrightarrow{\ p^*\ } H^1(S^n)=0 \to \cdots
$$

for $n \geq 2$, with the case $n=1$ the degree-two covering of the circle treated in the last example; for $1 \leq k \leq n$ the map $\smile x : H^{k-1}(B)\to H^k(B)$ is an isomorphism: for $k<n$ the target $H^k(S^n)$ of $p^*$ vanishes, and for $k=n$ it is the vanishing of $p^*$ on the top class that makes $\smile x$ onto and hence an isomorphism; the sequence is consistent with, and reconstructs, $H^*(\mathbb{RP}^n;\mathbb{F}_2) = \mathbb{F}_2[x]/(x^{n+1})$, with $e = x$. In the top degree the exactness reads $H^{n-1}(B)\xrightarrow{\smile x}H^n(B)\xrightarrow{p^*}H^n(S^n)\xrightarrow{\tau}H^n(B)\xrightarrow{\smile x}H^{n+1}(B)=0$, so the pullback vanishes in degree $n$ and the transfer is an isomorphism there: the projection has degree two, and over $\mathbb{F}_2$ the pullback on the top class is the multiplication by two, which is zero, while the exactness forces the transfer to be the other isomorphism.

**Example (the torus and the Klein bottle).** For the double cover $T^2\to K$ of the Klein bottle $K$ by the torus, the Euler class is the nonzero class of $H^1(K;\mathbb{F}_2)=\mathbb{F}_2$ and the Gysin sequence computes the mod 2 cohomology of the torus from that of the Klein bottle, the transfer recording the two sheets; the deck transformation reverses the orientation of the fibre, so the integer statement needs the twisted local system while the mod 2 statement is unchanged. For the double cover of the torus by the torus, obtained by squaring one coordinate, the Euler class is a generator of $H^1(T^2;\mathbb{F}_2)=\mathbb{F}_2^2$ and the sequence computes the mod 2 cohomology of the cover from that of the base.

**Example (the circle).** For the covering $S^1\to S^1$, $z\mapsto z^2$, the Euler class is the generator of $H^1(S^1;\mathbb{F}_2)$, the map $\smile e : H^0(B)\to H^1(B)$ is an isomorphism, and the sequence reads $H^0(B)\xrightarrow{\cong}H^1(B)\xrightarrow{0}H^1(X)\xrightarrow{\cong}H^1(B)\to 0$; the pullback is zero in degree one because the map has degree two and two is zero in $\mathbb{F}_2$, and the transfer is an isomorphism there. The example exhibits both the vanishing $\tau p^* = 2 = 0$ and the failure of the sequence to split naturally.

**Remark (the sphere bundles of higher rank).** The sequence here is the case of the sphere bundle of a line bundle, where the Euler class is the first Stiefel–Whitney class; for the sphere bundle of a vector bundle of higher rank the same construction gives the Gysin sequence with the Euler class the top Stiefel–Whitney class, the transfer the pushforward along the fibre, and the same identities $\tau p^*=0$ and $e\smile\tau=0$. The presentation with the transfer as the connecting homomorphism is the one that generalises, and the exactness is the general form of the Euler-class identity of *The Transfer and the Involution*.

**Remark (the connection with the fixed set).** For a non-free involution the Euler class of the normal directions to the fixed set plays the role of the Euler class of the cover of the free part: the identity $r\tau=e\smile(-)$ of *The Transfer and the Involution* is the local form of the Gysin exactness, and the two statements combine into the description of the fixed set as the singular locus of the quotient in *The Cohomology of an Orbit Space*. The integer form of the same exactness, with the coefficient system twisted by the orientation of the cover, is the subject of *Cohomology and the Universal Coefficient Theorem*.

**Remark (the oriented cover).** When the cover is oriented and integral coefficients are used, the Euler class carries the twist of the orientation, the Gysin sequence is the same exactness with the local system of the orientation, and the mod 2 sequence is its reduction; the passage between the two is the one treated in *Cohomology and the Universal Coefficient Theorem*.

## Summary

The two-fold covering $p : X\to B$ is the sphere bundle of a real line bundle $L$, and its Euler class is the first Stiefel–Whitney class $e = w_1(L)\in H^1(B;\mathbb{F}_2)$; the class satisfies $p^*e=0$, it classifies the cover, and it vanishes exactly when the cover is trivial. The Gysin sequence is the long exact sequence

$$
\cdots \to H^{n-1}(B)\xrightarrow{\smile e}H^n(B)\xrightarrow{p^*}H^n(X)\xrightarrow{\tau}H^n(B)\xrightarrow{\smile e}H^{n+1}(B)\to\cdots,
$$

with $p^*$ the pullback, $\tau$ the transfer and $\smile e$ the cup product with the Euler class; its dual is the homology sequence with the cap product $\cap\,e$ as the connecting map and the transfer and the pushforward in the dual directions, and $\tau p^*=0$, $e\smile\tau=0$, $\tau p_*=1+\sigma_*$, $p_*\tau=0$. The sequence is one of modules over $\mathbb{F}_2[\sigma]$, it splits as vector spaces but not naturally, the obstruction to the natural splitting being the Euler class, and it splits naturally exactly for the trivial cover; the transfer is the connecting homomorphism characterised by the projection formula and the vanishing $\tau p^*=0$. The computations for the antipodal covers of the spheres give $H^*(\mathbb{RP}^n;\mathbb{F}_2)=\mathbb{F}_2[x]/(x^{n+1})$, and the examples of the torus and the circle exhibit the two faces of the transfer. The general Gysin sequence of a sphere bundle is that of *The Leray–Serre Spectral Sequence*, the transfer and its identities are those of *The Transfer and the Involution*, and the integer form with the twisted local system belongs to the cohomology with local coefficients of *Cohomology and the Universal Coefficient Theorem*. Nothing analytic and nothing geometric was used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $p : X\to B$ | Two-fold covering; $\sigma$ the deck transformation |
| $L = X\times_{\mathbb{Z}/2}\mathbb{R}$ | Line bundle of the covering; $X$ is its sphere bundle |
| $e = w_1(L)\in H^1(B;\mathbb{F}_2)$ | Euler class; the cover is classified by $e$ |
| $p^*e = 0$ | The pullback of the Euler class vanishes |
| $\smile e : H^n(B)\to H^{n+1}(B)$ | Cup product with the Euler class; a successive map of the Gysin sequence |
| $p^* : H^n(B)\to H^n(X)$ | Pullback of the covering |
| $\tau : H^n(X)\to H^n(B)$ | Cohomological transfer, degree zero |
| $\cdots\to H^{n-1}(B)\xrightarrow{\smile e}H^n(B)\xrightarrow{p^*}H^n(X)\xrightarrow{\tau}H^n(B)\to\cdots$ | Gysin sequence (cohomology) |
| $\cap\,e : H_n(B)\to H_{n-1}(B)$ | Cap product; connecting map of the homology Gysin sequence |
| $\tau : H_n(B)\to H_n(X)$, $p_* : H_n(X)\to H_n(B)$ | Homology transfer and pushforward |
| $\tau p^*=0$, $e\smile\tau=0$, $\tau p_*=1+\sigma_*$, $p_*\tau=0$ | The identities of the sequence |
| $H^1(B;\mathbb{F}_2)\cong\{\text{two-fold covers}\}$ | Classification by the Euler class |

## Further Reading

- Norman Steenrod, *The Topology of Fibre Bundles* (Princeton University Press, 1951), for the Gysin sequence, the Euler class and the transfer.
- Edwin H. Spanier, *Algebraic Topology* (McGraw–Hill, 1966), for the Gysin sequence, the transfer and the Euler class of a line bundle.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the double covers, the Euler class and the cohomology of the projective spaces.
- John W. Milnor and James D. Stasheff, *Characteristic Classes* (Annals of Mathematics Studies 76, 1974), for the Euler class, the Stiefel–Whitney classes and the Gysin sequence.
- John McCleary, *A User's Guide to Spectral Sequences* (Cambridge University Press, 2nd ed. 2001), for the Serre spectral sequence of a sphere bundle and the identification of the transgression with the Euler class.
- Glen E. Bredon, *Topology and Geometry* (Springer, 1993), for the Gysin sequence and the cohomology with local coefficients of a covering.
