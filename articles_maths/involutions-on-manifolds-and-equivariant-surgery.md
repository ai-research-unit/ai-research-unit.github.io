
# __Involutions on Manifolds and Equivariant Surgery__

## Introduction

An **involution** of a manifold is a homeomorphism $T$ with $T^2 = \mathrm{id}$, and the pair $(M,T)$ is a manifold with an action of $\mathbb{Z}/2$. This article is the first of the structural group: it treats the involution as a structure on the manifold itself — the fixed set, the quotient, the equivariant neighbourhood — and it develops the **equivariant surgery** that classifies such structures, that is, the surgery theory of the pair performed so that the involution is preserved throughout.

The two objects of the theory are the **fixed set** $F = M^{T}$ and the **quotient** $M/T$; the equivariant neighbourhood of $F$ is a product in which the involution acts by reflection on the normal factor, so that the local model is completely determined. The classification is the surgery-theoretic one: an equivariant normal map has an obstruction in a Wall group of the group ring of $\pi_1$ with the action of $\mathbb{Z}/2$, the obstruction splits into a free part and a fixed-set part, and its vanishing is the criterion for an equivariant homotopy equivalence.

**The article assumes** the homology and cohomology of a manifold, the Smith theory of periodic maps, the surgery obstruction and the elementary expansions of *The Surgery Operator* and *The Handle Operator*, all of this Part or the algebraic topology of it. It uses the linear algebra of involutions of a vector space (*Linear Spaces*) and the elementary theory of finite group actions.

**The boundaries of the article.** The involution as an operator on the homology and the interaction of the involution with the intersection form are *The Involution as an Operator on the Homology* and *The Involution on the Homology*. The general periodic map of prime order is *Periodic Maps and the Smith Theory*; the classification of involutions on surfaces is *The Classification of Involutions on Surfaces*; the cobordism of group actions is *Involutions and the Cobordism of Group Actions*. The complete Wall groups, the surgery exact sequence and the $h$- and $s$-cobordism theorems are *Cobordism and Surgery Theory*. The analytic $G$-signature theorem is *Hermitian Pairings and the Equivariant Signature*; the smooth and piecewise-linear constructions are Part III. No analysis is used.

## Locally Linear Involutions and the Fixed Set

**Definition.** An involution of a manifold $M$ is **locally linear** if every point has a neighbourhood $U$ and a homeomorphism $U\cong\mathbb{R}^n$ under which the action of $T$ becomes a linear involution of $\mathbb{R}^n$; a **linear involution** is a linear map $\tau$ with $\tau^2 = \mathrm{id}$. Every continuous involution of a topological manifold is locally linear (a theorem of finite group actions), and the hypothesis is kept explicit only to make the normal form below precise.

**Proposition (normal form of a linear involution).** Let $\tau$ be a linear involution of $\mathbb{R}^n$. Then there is a basis in which
$$
\tau = \operatorname{diag}(1,\dots,1,-1,\dots,-1),
$$
with $r$ entries $+1$ and $n-r$ entries $-1$; the fixed subspace is the $r$-dimensional $+1$-eigenspace, the normal subspace is the $(n-r)$-dimensional $-1$-eigenspace, and $r$ and $n-r$ are invariants of $\tau$.

**Proof.** A linear involution is diagonalisable with eigenvalues $\pm1$ because its minimal polynomial divides $x^2-1$, which has distinct roots over $\mathbb{R}$; the signs of the eigenvalues are the two pieces, and the dimensions are the multiplicities.

**Theorem (the fixed set is a locally flat submanifold).** Let $T$ be a locally linear involution of an $n$-manifold $M$. Then the fixed set $F = M^{T}$ is a closed locally flat submanifold of $M$, possibly empty; each connected component has a dimension $r \leq n$ that is constant on the component; and every point of $F$ has an equivariant neighbourhood
$$
F\times D^{k}\longrightarrow M, \qquad T(x,v) = (x,-v), \qquad k = n-r,
$$
the **equivariant tubular neighbourhood**, in which $F$ sits as $F\times\{0\}$ and the involution reflects the normal disc.

**Proof.** On a locally linear chart the fixed set is the fixed subspace of the linear model, a linear subspace, and the chart identifies a neighbourhood of the point with the product of the fixed subspace and the normal disc; the reflection is the action on the normal factor. The product neighbourhoods patch because the local models are the same up to the linear structure, and the constancy of $r$ along a component follows by connectedness.

**Corollary (the cases of the theory).** The involution is **free** if $F = \varnothing$ and **non-free** otherwise. For a free involution the orbit map $M\to M/T$ is a two-sheeted covering and the quotient is a closed manifold of the same dimension; for a non-free involution the quotient is an orbifold whose singular locus is the image of $F$, and the local group at a singular point is $\mathbb{Z}/2$ acting by reflection.

**Remark (the dimension of the fixed set and Smith theory).** For a mod $2$ homology sphere the Smith theory of *Periodic Maps and the Smith Theory* already forces $F$ to be a mod $2$ homology $r$-sphere with $r\leq n$ and $r\equiv n\pmod 2$ when $F$ is nonempty; the present article refines this to the statement that $F$ is a genuine submanifold with an equivariant neighbourhood, which is the input the surgery theory needs.

## The Quotient and the Orbit Map

**Definition.** The **quotient** $M/T$ is the orbit space, and the **orbit map** $\pi : M\to M/T$ is the quotient map. Its restriction to $M\setminus F$ is a free two-sheeted covering onto its image, and the image of $F$ is the **mirror locus**.

**Proposition (structure of the quotient).** Let $T$ be a locally linear involution with fixed set $F$ of codimension $k$. Then $M/T$ is a topological space which is a manifold away from the mirror locus, near which it is locally the product of the model $\mathbb{R}^{n-k}\times(\mathbb{R}^k/\pm)$; this local model is the product of a disc with the "half-disc" $\mathbb{R}^k/\pm$, a manifold with boundary when $k=1$ and a singular space otherwise. The orbit map is a finite quotient map, and the quotient of the free part is a covering.

**Proof.** The local model is the quotient of the product $F\times D^k$ of the normal form by the reflection $(x,v)\mapsto(x,-v)$, which is $F\times(D^k/\pm)$; the quotient of a disc by the antipodal involution is the cone on $\mathbb{RP}^{k-1}$, a manifold with boundary exactly when $k=1$ and a singular space in higher codimension.

**Remark (the double of the quotient).** When $k=1$ — the fixed set has codimension one, the case of a "reflection" — the quotient $M/T$ is a manifold with boundary $\pi(F)$, and $M$ is its double along the boundary. This is the topological form of the doubling of a manifold with boundary, and it is the case in which the quotient is again a manifold.

## Equivariant Homology and the Borel Construction

The equivariant invariants of the pair $(M,T)$ are the homology of the quotient and of the fixed set, glued by the equivariant homology of the action.

**Definition.** The **Borel construction** of the $\mathbb{Z}/2$-space $M$ is the quotient
$$
M_{\mathbb{Z}/2} = M\times_{\mathbb{Z}/2}E\mathbb{Z}/2 = \frac{M\times E\mathbb{Z}/2}{(x,e)\sim(Tx,t e)},
$$
where $E\mathbb{Z}/2\to B\mathbb{Z}/2 = \mathbb{RP}^\infty$ is the universal $\mathbb{Z}/2$-bundle; the **equivariant homology** is $H_*^{\mathbb{Z}/2}(M;\mathbb{Z}) = H_*(M_{\mathbb{Z}/2};\mathbb{Z})$.

**Theorem (the spectral sequence of the Borel construction).** There is a first-quadrant spectral sequence
$$
E^2_{p,q} = H_p\bigl(\mathbb{Z}/2;H_q(M;\mathbb{Z})\bigr) \Longrightarrow H_{p+q}^{\mathbb{Z}/2}(M;\mathbb{Z}),
$$
with coefficients in the module $H_q(M;\mathbb{Z})$ carrying the action of the involution. For the trivial action it specialises to $H_p(\mathbb{RP}^\infty;\mathbb{Z})\otimes H_q(M;\mathbb{Z})$, and with $\mathbb{F}_2$ coefficients to the polynomial ring $\mathbb{F}_2[x]$ tensored with the homology; the $E^\infty$ page and the edge maps recover the Smith sequences relating $H_*(M)$, $H_*(F)$ and $H_*(M/T)$.

**Proof sketch.** The spectral sequence is the Serre spectral sequence of the fibration $M\to M_{\mathbb{Z}/2}\to B\mathbb{Z}/2$, with the local coefficients given by the action of $\pi_1(B\mathbb{Z}/2) = \mathbb{Z}/2$ on $H_*(M)$. The identification of the edge maps with the Smith sequences is by comparing the Borel construction with the maps $F\times_{\mathbb{Z}/2}E\mathbb{Z}/2 = F\times B\mathbb{Z}/2$ and $(M/T)_{\mathbb{Z}/2}$, together with the relation $M/T = M_{\mathbb{Z}/2}$ for a free action. The full statements of the resulting exact sequences are *Periodic Maps and the Smith Theory*.

**Corollary (the fixed part and the quotient).** The homology of $M/T$ is the $\mathbb{Z}/2$-coinvariant or invariant part of $H_*(M)$ according to the coefficient ring, as in *The Involution as an Operator on the Homology*; the Borel construction adds to this the higher equivariant classes, whose mod $2$ reductions are the classes of the Smith sequences.

## Equivariant Surgery

**Definition.** An **equivariant surgery datum** for the involution $T$ on the $n$-manifold $M$ is an equivariant embedding
$$
S^k\times D^{n-k}\hookrightarrow M
$$
of a product carrying an involution, with a linear involution on the second factor; the **equivariant surgery** removes the image and glues the complementary product equivariantly, so that the surgered manifold $M'$ inherits an involution, and the trace $W$ inherits an involution with $W^{T}$ the equivariant trace.

**Proposition (the two kinds of datum).** The equivariant data are of two kinds: those supported on the free part of $M$, whose normal representation is a sum of copies of the sign representation, and those supported near the fixed set, whose attaching sphere lies in $F$ and whose model is $F\times$ (a linear involution of $D^k$). A surgery in the free part changes the homology as in the non-equivariant case and keeps the fixed set unchanged; a surgery near $F$ changes the fixed set itself, replacing a product in $F$ by the complementary product.

**Proof.** The normal form of the linear involution shows that the model of a handle near the fixed set is determined by the dimensions of the two eigenspaces; the effect on the fixed set is the surgery of $F$ by the restriction of the model, and away from $F$ the operation is the non-equivariant one with an equivariant framing.

**Theorem (the equivariant surgery obstruction).** Let $T$ act on a closed $n$-manifold $X$ with fundamental group $\pi = \pi_1(X)$, and let $(f,b)$ be an equivariant normal map. Then the obstruction to surgering $(f,b)$ equivariantly into an equivariant homotopy equivalence is an element
$$
\sigma^{\mathbb{Z}/2}(f,b) \in L_n\bigl(\mathbb{Z}[\pi]\otimes \mathbb{Z}[\mathbb{Z}/2]\bigr) = L_n\bigl(\mathbb{Z}[\pi\times\mathbb{Z}/2]\bigr),
$$
the Wall surgery obstruction group of the group ring of $\pi\times\mathbb{Z}/2$ with the involution $g\mapsto g^{-1}$ and the orientation character; it vanishes if and only if the equivariant normal map can be corrected by equivariant surgeries to an equivariant homotopy equivalence, for $n\geq5$.

**Proof sketch.** The obstruction is the Wall obstruction of the equivariant normal map, computed in the group ring with its anti-involution and the orientation character. The group ring splits into the trivial and the sign summands, and correspondingly the obstruction has a component on the free part — the surgery obstruction of the quotient — and a component on the fixed part — the surgery obstruction of the fixed set together with its normal data. For a free action only the first component is present. The identification of the components and the vanishing criterion are the equivariant surgery theorem; the full proofs are in the literature and in *Cobordism and Surgery Theory*.

**Proposition (the components of the obstruction).** For $n = 4k$ the obstruction is a multisignature: the ordinary signature of $X$ together with the signatures of the fixed set and of the normal representations. For $n = 4k+2$ the obstruction is an Arf-type invariant of the middle-dimensional forms, together with a fixed-set Arf invariant. For a free involution the fixed part is absent and the obstruction reduces to that of the quotient.

**Proof sketch.** The obstruction group $L_{4k}$ of a group ring with involution is detected by the signatures of the Hermitian forms over the various simple summands of the group ring, which for $\mathbb{Z}[\mathbb{Z}/2]$ are the trivial and the sign representations; the fixed-set and normal contributions are the multisignature components of the equivariant form. The details are *Hermitian Pairings and the Equivariant Signature* and *Cobordism and Surgery Theory*.

## Classification of Involutions

**Theorem (the Browder–Livesay classification, statement).** Let $T$ be an involution of a closed simply connected manifold of dimension $n\geq5$ whose fixed set is a given manifold $F$ with a given normal representation, and suppose the equivariant normal invariants are fixed. Then the equivariant surgery obstruction lives in $L_n(\mathbb{Z}[\mathbb{Z}/2])$ and its vanishing is the necessary and sufficient condition for $T$ to be equivariantly $h$-cobordant to a standard involution with the same fixed data; the group $L_n(\mathbb{Z}[\mathbb{Z}/2])$ is computed from the representation ring of $\mathbb{Z}/2$ and is detected by the multisignature for $n\equiv0\pmod4$ and by the Arf invariants for $n\equiv2\pmod4$.

**Proof sketch.** The classification is the surgery exact sequence applied to the group $\mathbb{Z}/2$; the normal invariants are the equivariant normal data, the structure set measures the ambiguity, and the obstruction group is the Wall group of the group ring. The computation of $L_n(\mathbb{Z}[\mathbb{Z}/2])$ is a calculation of the Witt groups of the summands of the group ring. The theorem in this form and its many variants for the fixed set and the normal representations are the Browder–Livesay–Sullivan surgery theory; the sources are cited below.

**Remark (rigidity).** For a free involution on a simply connected manifold of dimension at least five, the equivariant surgery reduces to the surgery of the quotient, so the free involutions with a given quotient are classified by the surgery of the quotient together with the two possible orientations; for a non-free involution the fixed-set data are additional invariants, and this is the reason the equivariant theory is strictly richer than the non-equivariant one.

## Examples

**Example (the antipodal map of the sphere).** The antipodal map $A(x) = -x$ of $S^n$ is a free involution with quotient $\mathbb{RP}^n$. The quotient is a manifold and the equivariant surgery is the ordinary surgery of $\mathbb{RP}^n$; the fixed set is empty, so the fixed part of the obstruction vanishes, and the free part is the surgery obstruction of the projective space. The classification of the free involutions with a given quotient is the classification of the two-sheeted coverings, which is *Free Involutions and Lens Spaces*.

**Example (the reflection of the sphere).** The reflection of $S^n$ in an equator has fixed set $S^{n-1}$ of codimension one and quotient the disc $D^n$, with $S^n$ the double of the disc. This is the case $k=1$ of the structure theorem, and the quotient is a manifold with boundary; the equivariant surgery is the surgery of the pair (the disc, its boundary), and the obstruction is the ordinary one of the disc.

**Example (the hyperelliptic involution of a surface).** On a closed orientable surface $S_g$ the hyperelliptic involution has $2g+2$ isolated fixed points and quotient the sphere; the fixed set is of dimension zero and the normal representation is the sign representation. The equivariant surgery of surfaces is the classification of involutions of *The Classification of Involutions on Surfaces*, and the obstruction theory of the present article specialises to the counting of the fixed points.

**Example (an involution on a four-manifold).** Let $T$ act on a closed simply connected four-manifold with fixed set a union of surfaces. The obstruction for $n=4$ is a multisignature: the signature of the four-manifold, the signatures of the fixed surfaces, and the normal contributions. The vanishing of the obstruction is the criterion for the pair to be equivariantly $h$-cobordant to a standard model, and the example is the simplest in which both the free part and the fixed part of the obstruction are nonzero.

## Summary

A locally linear involution of an $n$-manifold has a locally flat fixed set $F$ of some dimension $r\leq n$ constant on each component, with an equivariant neighbourhood $F\times D^k$ on which the involution acts by reflection on the normal disc; the involution is free when $F$ is empty and the quotient is then a closed manifold, and otherwise the quotient is an orbifold with mirror locus the image of $F$, a manifold with boundary exactly in the codimension-one case. The equivariant invariants are assembled by the Borel construction $M\times_{\mathbb{Z}/2}E\mathbb{Z}/2$, whose Serre spectral sequence has $E^2_{p,q} = H_p(\mathbb{Z}/2;H_q(M))$ and whose edge maps recover the Smith sequences relating the manifold, its quotient and its fixed set. Equivariant surgery is the surgery theory of the pair, with the obstruction in the Wall group of the group ring of $\pi\times\mathbb{Z}/2$; the group ring splits into a trivial and a sign part, so the obstruction splits into a free part, which is the obstruction of the quotient, and a fixed part, whose components are the multisignature in dimension $4k$ and the Arf-type invariants in dimension $4k+2$. The classification of involutions with given fixed data is the equivariant Browder–Livesay–Sullivan surgery, and it is strictly richer than the free case, where it reduces to the surgery of the quotient.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T$, $T^2=\mathrm{id}$ | the involution of the manifold $M$ |
| $F = M^{T}$ | the fixed set; a locally flat submanifold of dimension $r$ |
| $k = n-r$ | the codimension of the fixed set; the normal dimension |
| $F\times D^k$, $(x,v)\mapsto(x,-v)$ | the equivariant tubular neighbourhood, the normal form |
| $M/T$, $\pi : M\to M/T$ | the quotient and the orbit map; $\pi(F)$ the mirror locus |
| $M_{\mathbb{Z}/2} = M\times_{\mathbb{Z}/2}E\mathbb{Z}/2$ | the Borel construction; its homology the equivariant homology |
| $H_p(\mathbb{Z}/2;H_q(M))\Rightarrow H^{G}_{p+q}(M)$ | the Borel spectral sequence |
| $\mathbb{Z}[\mathbb{Z}/2] = \mathbb{Z}\oplus\mathbb{Z}_{\mathrm{sgn}}$ | the group ring split into the trivial and the sign summands |
| $\sigma^{\mathbb{Z}/2}(f,b)\in L_n(\mathbb{Z}[\pi\times\mathbb{Z}/2])$ | the equivariant surgery obstruction |
| multisignature, Arf invariants | the components of the obstruction in dimensions $4k$, $4k+2$ |
| $L_n(\mathbb{Z}[\mathbb{Z}/2])$ | the obstruction group for a simply connected target |

## Further Reading

- William Browder and Glen Bredon (editors), *Surgery on Simply-Connected Manifolds* (Springer, 1972), for the surgery obstruction and the simply connected theory.
- William Browder and G. Robert Livesay, "Fixed Point Free Involutions on Homotopy Spheres", *Tohoku Mathematical Journal* 25 (1973), 69–87, for the free case and the classification of free involutions.
- Karl Heinz Dovermann and Reinhard Schultz, *Equivariant Surgery Theories and Their Periodicity Properties* (Springer Lecture Notes 1443, 1990), for the equivariant surgery obstruction, its components and the multisignature.
- Karl Heinz Dovermann, "Equivariant Periodicity for Compact Group Actions", *Transactions of the American Mathematical Society* 258 (1980), 393–414, for the periodicity of the equivariant Wall groups.
- C. T. C. Wall, *Surgery on Compact Manifolds* (Academic Press, 1970), for the underlying surgery obstruction and the exact sequence.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for locally linear actions, the fixed sets and the equivariant tubular neighbourhoods.
- Michael F. Atiyah and Isadore M. Singer, "The Index of Elliptic Operators: III", *Annals of Mathematics* 87 (1968), 546–604, for the $G$-signature theorem, whose statement is *Hermitian Pairings and the Equivariant Signature*.
