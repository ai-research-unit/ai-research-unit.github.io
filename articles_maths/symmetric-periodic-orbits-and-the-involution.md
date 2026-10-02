# __Symmetric Periodic Orbits and the Involution__

## Introduction

A **symmetric periodic orbit** is a periodic orbit that is carried to itself by the involution, and the involution turns the search for it and the spectral study of it into a half-dimensional problem. For a **reversible** map, with reversor $R$, a periodic orbit is symmetric when $R(\mathcal{O})=\mathcal{O}$ — equivalently it meets the fixed set $\mathrm{Fix}(R)$ — and then the orbit contains a point $p$ with $T^n p=p$ and $p\in\mathrm{Fix}(R)$, so the periodic condition is imposed on the lower-dimensional fixed set instead of on the whole phase space; the derivative of the return then satisfies $DR(p)\,D(T^n)(p)\,DR(p)=D(T^{-n})(p)$, so the spectrum of the monodromy is invariant under $\lambda\mapsto\lambda^{-1}$ and the multipliers of a symmetric orbit occur in reciprocal pairs. For an **equivariant** map, with commuting involution $\sigma$, a periodic orbit is symmetric when it lies in $\mathrm{Fix}(\sigma)$ or when $\sigma$ acts on it by the half-shift; the derivative of the return commutes with $D\sigma$, so the multipliers split into the isotypic blocks of the involution at a symmetric point. In both cases the involution is the operator that halves the problem, and the existence theory of the symmetric orbits — the Poincaré–Birkhoff theorem and the reversible twist theory of Birkhoff, Moser and collaborators — is the classical body of results the reduction makes available.

The article treats the symmetric periodic orbits and the operator form of the reduction. It defines the symmetric orbit for the two kinds of involution, states the reduction of the period condition to the fixed set, and explains why the search is half-dimensional; it states the **Poincaré–Birkhoff theorem** for an area-preserving twist map of the annulus and the reversible refinement, with the one-dimensional intermediate-value argument that produces the symmetric orbits; it derives the **operator form** of the symmetry: the conjugacy of the monodromy to its inverse for a reversor and its commutation with the involution for an equivariant symmetry, the reciprocal multiplier pairs and the isotypic multiplicity; and it closes with the examples — the symmetric periodic orbits of the standard map, of the reversible Hénon-type families, and of the doubling map — and with the Lefschetz and index count of the symmetric orbits.

The reversible symmetries, the fixed sets, the product-of-involutions structure and the symmetric orbit structure are those of *Reversible Dynamical Systems and Time-Reversal Symmetry*; the commuting involutions, the fixed-point subspaces and the isotypic decomposition are those of *Equivariant Dynamics under an Involution*, immediately preceding; the periodic orbits, the return maps, the Floquet multipliers and the linearisation are those of *Smooth Dynamical Systems*; the twist maps, the annulus and the rotation number are those of *Topological Dynamics* and of *Billiards and Related Systems*; the symplectic structures and the canonical maps are those of *Lagrangian and Hamiltonian Systems*. The operator-theoretic form of the involution is *Reversible Operators and the Involution*, in the `- * Operator Theory` group; the KAM continuation of the symmetric curves is *Reversible Systems and the KAM Theorem*, later in this category; and the equivariant existence theory is *Equivariant Bifurcation Theory*.

No physics is invoked.

## Symmetric Periodic Orbits

### The Two Kinds of Symmetry

**Definition.** Let $T$ be invertible with involution.

1. If $R$ is a **reversor**, $RTR=T^{-1}$, a periodic orbit $\mathcal{O}$ of $T$ is **$R$-symmetric** (or simply symmetric) if $R(\mathcal{O})=\mathcal{O}$; equivalently, by the orbit structure of the reversible theory, if $\mathcal{O}$ contains a point of $\mathrm{Fix}(R)$.
2. If $\sigma$ is an **equivariant symmetry**, $\sigma T=T\sigma$, a periodic orbit $\mathcal{O}$ of period $n$ is **$\sigma$-symmetric** if $\sigma(\mathcal{O})=\mathcal{O}$; by the orbit structure of the equivariant theory, this happens exactly when $\mathcal{O}\subseteq\mathrm{Fix}(\sigma)$, or when $\sigma$ acts on $\mathcal{O}$ by the shift by $n/2$ with $n$ even.

**Theorem (reduction to the fixed set).** (i) For a reversor $R$, a periodic orbit of period dividing $2n$ is symmetric if and only if it is the orbit of a point $p\in\mathrm{Fix}(R)$ with $T^{n}p=p$; the symmetric periodic orbits of period dividing $2n$ are therefore in bijection with the fixed points of the restricted map $T^n|_{\mathrm{Fix}(R)}$. (ii) For an equivariant $\sigma$, the symmetric periodic orbits that lie in $\mathrm{Fix}(\sigma)$ are the periodic orbits of the restricted map $T|_{\mathrm{Fix}(\sigma)}$.

*Proof.* The reductions are the symmetric orbit theorems of the two preceding articles: for the reversor, $p\in\mathrm{Fix}(R)$ and $T^np=p$ give an $R$-invariant orbit, and conversely an $R$-invariant orbit contains a symmetric point whose forward image at the half-period is again symmetric; for the equivariant involution, the points of $\mathrm{Fix}(\sigma)$ are carried to points of $\mathrm{Fix}(\sigma)$ by every power of $T$. The bijection is then the restriction of the period condition.

**Remark (the dimension halving).** For a reversor with a fixed set of dimension $\dim M-k$, the reduction solves $T^n p=p$ on a $(\dim M-k)$-dimensional set rather than on the $\dim M$-dimensional manifold; the numerical search for a symmetric periodic orbit is therefore a root-finding problem of half the dimension in the typical case $k=\dim M/2$, and this is the "symmetric periodic orbit" method of the area-preserving theory. The same comment applies to a fixed-point subspace of the equivariant involution.

## Existence: the Poincaré–Birkhoff Theory

**Theorem (Poincaré–Birkhoff, quoted).** Let $T$ be an area-preserving homeomorphism of the closed annulus $\mathbb{A}=S^1\times[0,1]$ that is a **twist map**: $T$ is the identity on the boundary in the sense that the boundary components are invariant and their rotation numbers $\rho_0<\rho_1$ differ. Then for every rational number $p/q$ with $\rho_0<p/q<\rho_1$ there are at least two periodic orbits of period $q$ whose rotation number is $p/q$; in particular, when the boundary rotation numbers straddle $0$, the map has at least two fixed points. The orbits are found as the intersections of the boundary of a Birkhoff annulus with its image, and the proof of the fixed-point case is the Poincaré last geometric theorem.

*Proof (sketch).* The proof is the Birkhoff argument: one lifts $T$ to the strip and considers, for each rotation number, the set of points whose orbit crosses a fundamental domain; the twist condition makes the image of the "translated graph" of the lift cross the original graph, and the topological crossing of the two graphs, together with the area-preserving property, forces at least two intersections, each an orbit of the required period. The complete argument, the rotation number of a homeomorphism of the annulus and the theory of the Birkhoff annulus are standard, and the details are those of *Topological Dynamics* and of the area-preserving theory.

**Theorem (the reversible refinement, quoted).** Let $T$ be a reversible area-preserving twist map of the annulus, with reversor $R$ whose fixed set is a finite union of **symmetry lines** meeting the annulus. Then the symmetric periodic orbits are found by a one-dimensional argument: on each symmetry line the return map restricted to the line is a monotone or a fold map, and its fixed points, which are the intersections of the line with its images, are the symmetric periodic orbits; the Poincaré–Birkhoff theorem may then be proved for the reversible twist maps by counting the intersections along the symmetry lines, and the symmetric orbits exist whenever the twist and the boundary rotation numbers force a crossing.

*Proof.* Quoted as the reversible version of the Poincaré–Birkhoff theory (Birkhoff, Moser and collaborators). The reduction is the one-dimensional fixed-point equation of the first theorem: on a symmetry line the map $T^n|_{\mathrm{Fix}(R)}$ is an interval map, and the intermediate value theorem applied to $T^n(q)-q$ supplies the roots when the two ends of a symmetry line are displaced in opposite directions under $T^n$.

**Remark (the symmetric orbits as the organising skeleton).** The symmetric periodic orbits are the points where the reversible dynamics meets its own symmetry line, and they organise the invariant curves: a symmetric periodic orbit is typically trapped between two symmetric invariant curves, and the destruction of the curves in the reversible KAM theory is accompanied by the continuing existence of the symmetric orbits. This is what makes the reversible theory numerically stable, and it is the content of *Reversible Systems and the KAM Theorem*, later in this category.

## The Operator Form of the Involution

### The Monodromy of a Symmetric Orbit

**Theorem (reversor: the multipliers are reciprocal).** Let $R$ be a reversor of $T$, let $p\in\mathrm{Fix}(R)$, and let $M=D(T^n)(p)$ be the derivative of the return. Then

$$
DR(p)\,M\,DR(p)=M^{-1}, \qquad DR(p)^2=I,
$$

so $M$ is conjugate to its inverse by the linear involution $DR(p)$; consequently the spectrum of $M$ is invariant under $\lambda\mapsto\lambda^{-1}$, and the Floquet multipliers of the symmetric periodic orbit occur in reciprocal pairs, $\lambda$ and $1/\lambda$, with the unit circle mapped to itself.

*Proof.* Differentiating the identity $R T^n R=T^{-n}$ at the fixed point $p$ and using $R(p)=p$ and the chain rule gives $DR(p)\,D(T^n)(Rp)\,DR(p)=D(T^{-n})(p)$; since $Rp=p$ and $D(T^{-n})(p)=D(T^n)(p)^{-1}=M^{-1}$, the displayed identity follows. If $Mv=\lambda v$ then $M(DR(p)v)=\lambda^{-1}DR(p)v$, so the spectrum is closed under inversion.

**Theorem (equivariant involution: the multipliers are isotypic).** Let $\sigma$ be an equivariant involution of $T$, let $p\in\mathrm{Fix}(\sigma)$, and let $M=D(T^n)(p)$. Then

$$
M\,D\sigma(p)=D\sigma(p)\,M ,
$$

so $M$ preserves the isotypic decomposition of $T_pM$ and splits into the blocks on the $+1$ and the $-1$ eigenspaces of $D\sigma(p)$; the multipliers of the symmetric orbit split accordingly, and a symmetric orbit whose fixed point has a non-free $\mathbb{Z}/2$-action on its tangent space has a forced multiplicity in the corresponding block.

*Proof.* Differentiating $\sigma T^n=T^n\sigma$ at $p$ and using $D\sigma(\sigma p)=D\sigma(p)$ with $\sigma p=p$ gives $D\sigma(p)M=MD\sigma(p)$; the block decomposition is then the isotypic theorem of *Equivariant Dynamics under an Involution*.

**Example (an elliptic and a hyperbolic pair, recomputed).** For the reversible planar family $f(x,y)=(y,y^2-x)$ with $R(x,y)=(y,x)$, the origin is a symmetric fixed point and its monodromy is $Df(0,0)=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, with the eigenvalues $\pm i$ forming the reciprocal pair $i,1/i=-i$ and producing a rotation of the linearised dynamics; for the odd-parameter family $f(x,y)=(y,\,y^3-3y-x)$ with $g$ odd, the symmetric period-two orbit $\{(1,-1),(-1,1)\}$ has the monodromy $Df^2(1,-1)=-I$ up to $O(10^{-12})$, with the double eigenvalue $-1$, again reciprocal because $-1=(-1)^{-1}$. Both matrices were computed in plain Python from the branch formula and reproduce the reciprocal-pair theorem.

### The Fixed-Point Index and the Lefschetz Number

**Definition.** For a fixed point $p$ of a smooth map with $I-DT(p)$ invertible the **fixed-point index** is $\operatorname{sign}\det(I-DT(p))$, and the **Lefschetz number** of a map of a compact manifold is $L(T)=\sum_i(-1)^i\operatorname{tr}(T^*|_{H^i})$; the fixed points of a nondegenerate map are counted with the index by the Lefschetz formula, $\sum_{Tp=p}\operatorname{sign}\det(I-DT(p))=L(T)$ when all the fixed points are nondegenerate.

**Theorem (the symmetric index).** The symmetric periodic orbits of period dividing $n$ of a reversible map are the fixed points of the restricted map $T^n|_{\mathrm{Fix}(R)}$, counted by the index of the restricted map; the index of a symmetric fixed point is the product of the two indices of the blocks of the monodromy under the splitting $\lambda,1/\lambda$, and the Lefschetz number of the restriction computes the number of symmetric orbits in each period. The same statement holds for the equivariant involution with the restricted map $T|_{\mathrm{Fix}(\sigma)}$.

*Proof.* The reduction theorem identifies the symmetric periodic orbits with the fixed points of the restriction; the index statement is the multiplicativity of the sign of the determinant under the reciprocal-pair factorisation of the characteristic polynomial of a symmetric monodromy, $\det(I-\lambda^{-1}M)$ pairing the reciprocal eigenvalues; and the Lefschetz formula applied to the restricted map counts them.

## The Examples

**Example (the standard map).** The standard map $S(\theta,I)=(\theta+I+k\sin\theta,\,I+k\sin\theta)$ is reversible with $R(\theta,I)=(-\theta,I+k\sin\theta)$, whose fixed set is the two **symmetry lines** $\theta=0$ and $\theta=\pi$; the symmetric periodic orbits are the intersections of these lines with their images under the powers of $S$, and the reversible Poincaré–Birkhoff theory produces the two symmetric orbits of each admissible rotation number. At the fixed point $(\pi,0)$, which is symmetric for the reversor and fixed by the central involution $\Sigma$, the monodromy $DS(\pi,0)$ has determinant $1$ and trace $2-k$, so the eigenvalues are a reciprocal pair $\lambda,\lambda^{-1}$; for $0<k<4$ the trace lies in $(-2,2)$ and the pair is complex conjugate on the unit circle, so the point is elliptic, while for $k>4$ the pair is real and reciprocal and the point is hyperbolic. At $k=4$ the trace is $-2$ and the eigenvalue $-1$ has multiplicity two, the reversible analogue of a period-doubling threshold, where the orbit loses its linear stability in a symmetry-breaking. The identities $R^2=\mathrm{id}$, $RSR=S^{-1}$ and the commutation with $\Sigma$ were verified numerically in the two preceding articles.

**Example (the doubling map and its symmetric orbits).** For $T x=2x\bmod1$ and the equivariant involution $\sigma x=-x$, the fixed set is $\{0,\tfrac12\}$ and $T$ maps both points to $0$; the $\sigma$-symmetric periodic orbits are the periodic orbits contained in the two-point fixed set, that is, the fixed point $0$. The doubling map has no other symmetric periodic orbit, whereas it has many periodic orbits in general, so the symmetric ones are a thin subset — the generic situation: the symmetric periodic orbits are a controlled subset of all the periodic orbits, and the involution organises them without producing them all.

**Example (an index count).** For the reversible family $f(x,y)=(y,y^2-x)$ the origin is a symmetric fixed point with $Df=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ and $\det(I-Df)=\det\begin{pmatrix}1&-1\\1&1\end{pmatrix}=2>0$, so the index is $+1$; the point $(2,2)$ is also a symmetric fixed point, with $Df(2,2)=\begin{pmatrix}0&1\\-1&4\end{pmatrix}$ and the real reciprocal pair $2\pm\sqrt3$ of multipliers. The indices add to the Lefschetz number of the restriction, which counts the symmetric fixed points; the computation is the elementary one of the reciprocal-pair theorem and requires no numerics beyond the two-by-two determinant.

## Summary

A **symmetric periodic orbit** is a periodic orbit carried to itself by the involution. For a **reversor** $R$, $RTR=T^{-1}$, the orbit is symmetric exactly when it contains a point $p\in\mathrm{Fix}(R)$ with $T^np=p$, so the period condition is imposed on the fixed set — the **reduction to the fixed set** — and the symmetric orbits of period dividing $2n$ are the fixed points of $T^n|_{\mathrm{Fix}(R)}$; for an **equivariant** involution $\sigma$, the symmetric orbits lie in $\mathrm{Fix}(\sigma)$ or are shifted by $n/2$. Existence is supplied by the **Poincaré–Birkhoff theorem**: an area-preserving twist map of the annulus has at least two periodic orbits of each admissible rotation number, and its reversible refinement produces the symmetric orbits through the one-dimensional fixed-point equation on the **symmetry lines**. The **operator form** of the symmetry is the statement about the monodromy $M=D(T^n)(p)$: a reversor conjugates it to its inverse, $DR(p)MDR(p)=M^{-1}$, so the Floquet multipliers of a symmetric orbit come in reciprocal pairs $\lambda,1/\lambda$ (verified for the reversible families: $\pm i$ at the symmetric fixed point, $-1$ double at the symmetric period-two orbit); an equivariant involution commutes with it, $MD\sigma(p)=D\sigma(p)M$, so the multipliers split into the isotypic blocks and the non-free action forces multiplicities. The **fixed-point index** and the **Lefschetz number** of the restricted map count the symmetric orbits, the index factorising a symmetric fixed point into its reciprocal pair. The examples are the standard map, whose symmetric orbits lie on the symmetry lines $\theta=0,\pi$ and whose symmetric fixed point $(\pi,0)$ is elliptic for $k<4$ and degenerate at $k=4$, and the doubling map, whose only $\sigma$-symmetric periodic orbit is the fixed point $0$. The KAM continuation of the symmetric orbits is *Reversible Systems and the KAM Theorem*, the operator involution is *Reversible Operators and the Involution*, and the equivariant existence theory is *Equivariant Bifurcation Theory*, all later in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $\sigma$ | Reversor ($RTR=T^{-1}$); equivariant involution ($\sigma T=T\sigma$) |
| $\mathrm{Fix}(R)$, $\mathrm{Fix}(\sigma)$ | Fixed sets; the symmetry lines in the planar reversible case |
| $p$, $T^np=p$ | Symmetric periodic point and its period condition |
| $\mathcal{O}$, $R(\mathcal{O})=\mathcal{O}$ | Periodic orbit and its symmetry |
| $M=D(T^n)(p)$ | Monodromy (derivative of the return) at a symmetric point |
| $DR(p)MDR(p)=M^{-1}$ | Reciprocity of the multipliers for a reversor |
| $MD\sigma(p)=D\sigma(p)M$ | Isotypic block structure for an equivariant involution |
| $\lambda,1/\lambda$ | Reciprocal Floquet multipliers |
| $\rho_0,\rho_1$ | Boundary rotation numbers of a twist map |
| $\operatorname{sign}\det(I-DT(p))$, $L(T)$ | Fixed-point index and Lefschetz number |

## Further Reading

- George D. Birkhoff, "Proof of Poincaré's geometric theorem", *Transactions of the American Mathematical Society* 14 (1913), 14–22, and "On the periodic motions of dynamical systems", *Acta Mathematica* 50 (1927), 359–379, for the twist theorem.
- Henri Poincaré, "Sur un théorème de géométrie", *Rendiconti del Circolo Matematico di Palermo* 33 (1912), 375–407, for the last geometric theorem.
- John Moser, "On invariant curves of area-preserving mappings of an annulus", *Nachrichten der Akademie der Wissenschaften in Göttingen* (1962), 1–20, and *Stable and Random Motions in Dynamical Systems* (Princeton University Press, 1973), for the twist theory and the reversible periodic orbits.
- Michael B. Sevryuk, *Reversible Systems* (Springer Lecture Notes in Mathematics 1211, 1986), for the reversible Poincaré–Birkhoff and KAM theory.
- John A. G. Roberts and G. R. W. Quispel, "Chaos and time-reversal symmetry", *Physics Reports* 216 (1992), 63–177, for the symmetric orbits in reversible systems.
- Michel Hénon, "Numerical study of quadratic area-preserving mappings", *Quarterly of Applied Mathematics* 27 (1969), 291–312, for the numerical symmetric orbits.
- Anatole Katok and Boris Hasselblatt, *Introduction to the Modern Theory of Dynamical Systems* (Cambridge University Press, 1995), for the rotation number, the annulus and the twist theorem.
- Solomon Lefschetz, *Topology* (American Mathematical Society, 1930), for the fixed-point index and the Lefschetz number.
