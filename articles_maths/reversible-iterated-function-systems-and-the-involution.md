# __Reversible Iterated Function Systems and the Involution__

## Introduction

A self-similar set can be symmetric, and the symmetry is not an accident of the drawing: it is an **involution** $R$ of the ambient space that permutes the maps of the iterated function system, $R\circ S_i=S_{\rho(i)}\circ R$ for an involutive permutation $\rho$ of the branches. Such a system is **reversible**, and $R$ is its **time-reversal involution**: on the attractor it exchanges the pieces cut by the two branches of each pair, it descends to the coding as the letterwise flip, and on the limit space of a self-similar group it commutes with the shift. Reversibility is the structure that makes the transfer operator of the limit dynamical system **self-adjoint up to the involution**: the adjoint of *The Adjoint of the Transfer Operator of the Limit Dynamical System* is computed by composing with $R$, and the reversible measure of *The Self-Similar Measure and the Involution* is the one that is fixed by the reversal. This article builds the involution.

The article defines a reversible iterated function system by the exchange relation $R\circ S_i=S_{\rho(i)}\circ R$ with $\rho$ an involution, proves that the attractor is $R$-invariant and that the coding intertwines $R$ with the letterwise flip $\tilde R(x_1x_2\cdots)=\rho(x_1)\rho(x_2)\cdots$, and proves that the inverse branches of the limit map are exchanged, $R\circ\sigma_x=\sigma_{\rho(x)}\circ R$, so that the limit dynamical system is reversible in the sense of *Time Reversal and the Transfer Operator*: the shift commutes with $R$, $R\varphi=\varphi R$. It identifies the **fixed points** $\mathrm{Fix}(R)$ — points of the ambient space with $Rx=x$ — and the **fixed tiles** $T_v$ with $\rho(v)=v$, shows that a branch that is fixed, $\rho(i)=i$, contributes a symmetry of the tile $S_i\Lambda$ and a fixed point when $R$ has one on the attractor, and computes the reversible structures of the category: the segment, where the fixed point $\tfrac12$ lies on the attractor; the middle-thirds Cantor set, where $\mathrm{Fix}(R)=\{\tfrac12\}$ meets the attractor in the empty set and the involution exchanges the cylinders without fixed points; and the Sierpiński gasket with the reflection that swaps two of the three corners.

The iterated function systems, the attractors and the open set condition are *Fractal Geometry*; the boundary, the tiles, the shift, the coding and the limit space are *Limit Spaces and Schreier Graphs* and *Self-Similar Groups*; the time-reversal involution and its effect on the transfer and the Koopman operators are *Time Reversal and the Transfer Operator* of Part III, whose discrete counterpart this article is; the transfer operator of the limit system is *The Transfer Operator of the Limit Dynamical System*, the previous article; and the reversible measure and its adjoint relation are *The Self-Similar Measure and the Involution* and *The Adjoint of the Transfer Operator of the Limit Dynamical System*, the two after it; the reversible systems of *Dynamical Systems* are the same structure in continuous time, of which this article is the discrete self-similar instance. No physics is invoked.

## Reversible Iterated Function Systems

### The Involution and the Exchange of the Branches

**Definition.** Let $S_1,\dots,S_m$ be an iterated function system on a complete metric space with attractor $\Lambda$, and let $R$ be a homeomorphism with $R^2=\mathrm{id}$. The system is **reversible** with the **time-reversal involution** $R$ if there is a permutation $\rho$ of the index set with $\rho^2=\mathrm{id}$ such that
$$
R\circ S_i=S_{\rho(i)}\circ R\qquad(i=1,\dots,m).
$$
The indices with $\rho(i)=i$ are **fixed branches**; the pairs $\{i,\rho(i)\}$ with $\rho(i)\ne i$ are **exchanged branches**. Since $R^2=\mathrm{id}$, applying the relation twice gives $S_i=S_{\rho^2(i)}$, so $\rho$ is an involution, and the fixed branches are exactly those that commute with $R$.

**Proposition (the reversibility is symmetric in the branches).** If $R\circ S_i=S_{\rho(i)}\circ R$ for all $i$, then $R\circ S_{i_1}\cdots S_{i_n}=S_{\rho(i_1)}\cdots S_{\rho(i_n)}\circ R$ for every word, and the composition is fixed precisely when the word is fixed letterwise by $\rho$.

*Proof.* Induction on the length of the word, using the exchange relation at the right of the product; the fixed case is the letterwise-fixed word, because each application of $\rho$ either changes the letter or not.

### The Invariance of the Attractor and the Coding

**Theorem (the attractor is invariant).** If the system is reversible then $R(\Lambda)=\Lambda$; conversely if $R(\Lambda)=\Lambda$ and the system satisfies the open set condition with disjoint pieces, then the system is reversible.

*Proof.* The set $R(\Lambda)=\bigcup_i R S_i(\Lambda)=\bigcup_i S_{\rho(i)}R(\Lambda)$ is a compact set satisfying the same invariance equation as $\Lambda$, so $R(\Lambda)=\Lambda$ by the uniqueness of the attractor of *Fractal Geometry*. Conversely, if $R(\Lambda)=\Lambda$ then $S_i R(\Lambda)$ and $R S_i(\Lambda)$ are two pieces of $\Lambda$ of the same scale and position, so they coincide by the disjointness, and $R S_i=S_{\rho(i)}R$ on the pieces and hence on the attractor.

**Theorem (the coding intertwines the involution).** Let $\pi:\partial\mathcal{T}\to\Lambda$ be the coding map of the iterated function system, and let $\tilde R(x_1x_2\cdots)=\rho(x_1)\rho(x_2)\cdots$ be the **letterwise flip** of the boundary. Then
$$
R\circ\pi=\pi\circ\tilde R ,
$$
so that $\tilde R$ is the coding-level form of the involution.

*Proof.* $R\pi(x\xi)=R S_x\pi(\xi)=S_{\rho(x)}R\pi(\xi)=S_{\rho(x)}\pi(\tilde R\xi)=\pi(\rho(x)\tilde R\xi)=\pi(\tilde R(x\xi))$, by the exchange relation, the induction, and the definition of the coding. The letterwise flip is the time reversal of the one-sided shift, and it commutes with the shift: $\tilde R\tau=\tau\tilde R$.

## The Limit Dynamical System and Its Reversal

### The Limit Map and Reversibility

**Definition.** Let $G\le\operatorname{Aut}(\mathcal{T})$ be a contracting self-similar group with limit space $\mathcal{J}_G$, tiles $T_v$ and limit map $\varphi$ of *The Transfer Operator of the Limit Dynamical System*. The group is **reversible** if there is an involutive automorphism of the self-similar structure exchanging the letters by a permutation $\rho$ with $\rho^2=\mathrm{id}$, that is, an involution $R$ of $\mathcal{J}_G$ with $R(T_v)=T_{\rho(v)}$ and $R\circ\sigma_x=\sigma_{\rho(x)}\circ R$ for every letter.

**Theorem (the reversal commutes with the limit map).** For a reversible self-similar group the limit map commutes with the involution,
$$
R\circ\varphi=\varphi\circ R ,
$$
the exchange of the inverse branches is $R\circ\sigma_x=\sigma_{\rho(x)}\circ R$, and the time-reversal involution conjugates the transfer operator with the permuted one: with $L_\varphi$ the transfer operator of the previous article and $P_\rho f=f\circ R$ the operator of the involution,
$$
P_\rho\,L_\varphi\,P_\rho=L_\varphi .
$$

*Proof.* On the boundary the letterwise flip commutes with the shift, so $R\varphi=\varphi R$ by the coding. The branch relation follows by taking the inverses: $(R\sigma_x)^{-1}=\sigma_x^{-1}R=\varphi|_{T_x}R$ and $(\sigma_{\rho(x)}R)^{-1}=R^{-1}\varphi|_{T_{\rho(x)}}=R\varphi|_{T_{\rho(x)}}$; the two agree because $R$ maps $T_{\rho(x)}$ to $T_x$. For the transfer operator, $P_\rho L_\varphi P_\rho f(x)=\sum_{\varphi(y)=Rx}d(y)f(Ry)=\sum_{\varphi(Ry')=Rx}d(Ry')f(Ry')=\sum_{\varphi(y')=x}d(y')f(y')$ where the change of variables $y=Ry'$ uses $\varphi R=R\varphi$ and the invariance of the local degree under $R$; this is $L_\varphi f(x)$.

**Remark (the reversibility in the sense of Part III).** The involution $R$ is the **time reversal** of *Time Reversal and the Transfer Operator* in the discrete setting: it commutes with the dynamics, it exchanges the inverse branches pairwise, and its presence is the structure under which the transfer operator has the self-adjointness of the next articles. Because the involution exchanges the branches, it is not the identity of the dynamics but an extra symmetry, and the quotient of the limit space by $R$ is the space of the reversible system.

### The Fixed Points and the Fixed Tiles

**Definition.** The **fixed points** of the involution are the points of the ambient space with $Rx=x$, a closed set $\mathrm{Fix}(R)$; the **fixed tiles** are the tiles $T_v$ with $\rho(v)=v$ letterwise, so that $R(T_v)=T_v$; and the **fixed part** of the system is the intersection $\mathrm{Fix}(R)\cap\mathcal{J}_G$ of the fixed set with the limit space.

**Theorem (the dichotomy of the reversal).** The involution either fixes a point of the attractor or exchanges the pieces without a fixed point. If $\rho(i)=i$ for some $i$ then the tile $S_i\Lambda$ is $R$-invariant and $\mathrm{Fix}(R)\cap S_i\Lambda$ contains the fixed points of $R$ in that tile, so the fixed part is nonempty exactly when some branch is fixed or some exchanged pair of tiles meets at a fixed point; if no branch is fixed and the pieces are disjoint, then the system exchanges its pieces and the fixed part is empty.

*Proof.* A fixed tile $T_v$ with $\rho(v)=v$ is carried to itself and the fixed set inside it is the fixed set of the restriction; the counting of the tiles with $\rho(v)=v$ is the counting of the words over the fixed letters of $\rho$, and the pieces are disjoint under the open set condition, so the fixed part is the union over the fixed-letter words of the fixed sets inside $T_v$; if there is no fixed letter, the words over fixed letters are empty and the fixed set meets the attractor only through the limit points of the exchanged tiles, which is empty when the pieces are separated.

## The Reversible Systems of the Category

### The Segment and the Cantor Set

**Example (the segment).** For $S_0(x)=\tfrac12x$, $S_1(x)=\tfrac12x+\tfrac12$ on the interval and $R(x)=1-x$, the exchange relation $R S_i=S_{1-i}R$ holds at every point: $R(S_0x)=1-\tfrac12x$ and $S_1(Rx)=\tfrac12(1-x)+\tfrac12=1-\tfrac12x$. The attractor is $[0,1]$, invariant under $R$, the fixed set is $\mathrm{Fix}(R)=\{\tfrac12\}$, and $\tfrac12$ is a point of the attractor: the fixed part is a single point. The letterwise flip is $\tilde R(x_1x_2\cdots)=\bar x_1\bar x_2\cdots$, and the reversible system is the limit dynamical system of the dihedral group of *Self-Similar Groups*, whose limit space is the segment.

**Example (the middle-thirds Cantor set).** For $S_0(x)=\tfrac13x$, $S_1(x)=\tfrac13x+\tfrac23$ and $R(x)=1-x$, the same exchange relation holds: $R(S_0x)=1-\tfrac13x$ and $S_1(Rx)=\tfrac13(1-x)+\tfrac23=1-\tfrac13x$. The attractor $\Lambda$ is invariant, the fixed set is again $\mathrm{Fix}(R)=\{\tfrac12\}$, but now $\tfrac12\notin\Lambda$, because $x=\tfrac12$ has the ternary expansion $x=0.111\cdots_3$, which uses the digit $1$, while the attractor carries only the digits $0$ and $2$. The involution exchanges the cylinders letterwise, $R[x_1\cdots x_n]=[\bar x_1\cdots \bar x_n]$, without fixed point, and the fixed part of the system is empty. The verification of the exchange relation at the sample points $0,\tfrac15,\tfrac7{10},\tfrac13,\tfrac12$ returns the identity to machine precision, and the fixed point $\tfrac12$ is confirmed to lie outside the attractor; the exchange of the cylinder masses is exact for the symmetric weights.

### The Sierpiński Gasket

**Example (the reflection of the gasket).** For the maps $S_i(x)=\tfrac12(x+q_i)$ of the gasket with the corners $q_0,q_1,q_2$ of an equilateral triangle, let $R$ be the reflection fixing $q_0$ and exchanging $q_1$ and $q_2$. Then $R S_0=S_0 R$ (the fixed branch) and $R S_1=S_2 R$, $R S_2=S_1 R$ (the exchanged pair), so the system is reversible with the fixed word $0$ and the exchanged pair $\{1,2\}$; the attractor is invariant, the fixed set is the median through $q_0$, and the fixed part is the segment of that median inside the gasket, which is a nonempty set of fractal dimension. The involution descends to the limit dynamical system of the group of the gasket of *Self-Similar Groups*, which is level-transitive and reversible in this sense.

## The Associated Reversible Dynamical System

**Definition.** The **associated reversible dynamical system** is the pair $(\varphi,R)$ of the limit map and its commuting involution; it is the discrete counterpart of the reversible system of *Time Reversal and the Transfer Operator*, and the orbit equivalence of $(\varphi,R)$ is the orbit equivalence of the two-sided natural extension of $\varphi$ with the involution $R$.

**Theorem (the natural extension and the reversal).** The natural extension of the limit dynamical system is the two-sided shift $\Phi(x_n)_{n\in\mathbb{Z}}=(x_{n+1})_{n\in\mathbb{Z}}$ on the set of two-sided codes, and the reversal $\hat R(x_n)=(R x_{-n})$ is a measure-preserving involution commuting with $\Phi$, whose quotient is the reversible system; the one-sided factor of $\Phi$ is $\varphi$ and the one-sided factor of $\hat R$ is $R$.

*Proof sketch.* The natural extension of a non-invertible map is the shift on the space of orbits; the reversibility of the coding means that the orbit of $R\xi$ is the reversal of the orbit of $\xi$, so the involution $\hat R$ is well defined and commutes with the shift. The quotient and the entropy are those of the reversible systems of *Ergodic Theory*; the reversible dynamical systems of Part III are the same structure with the continuous time replaced by the iteration. The reversible systems of the self-similar groups of the category are the segment, the Cantor set and the gasket, and their reversible invariants are computed in *The Self-Similar Measure and the Involution*.

**Remark (what reversibility buys).** The involution makes the analysis symmetric: the transfer operator is conjugated to itself by $P_\rho$, its eigenfunctions come in $R$-symmetric and $R$-antisymmetric families, and the spectral problem splits into the two. The decomposition is the discrete analogue of the spectral decomposition of a reversible dynamical system in *Time Reversal and the Transfer Operator*, and it is the tool of *The Adjoint of the Transfer Operator of the Limit Dynamical System*.

## Summary

A **reversible iterated function system** is one equipped with an **involution** $R$ exchanging the maps, $R S_i=S_{\rho(i)}R$ with $\rho^2=\mathrm{id}$; the attractor is $R$-invariant, the coding descends $R$ to the letterwise flip $\tilde R(x_1x_2\cdots)=\rho(x_1)\rho(x_2)\cdots$, and on the limit space of a reversible self-similar group the involution commutes with the limit map, $R\varphi=\varphi R$, and exchanges the inverse branches, $R\sigma_x=\sigma_{\rho(x)}R$, so that the transfer operator is conjugated to itself, $P_\rho L_\varphi P_\rho=L_\varphi$. The **fixed branches** $\rho(i)=i$ and the **fixed tiles** $T_v$ with $\rho(v)=v$ carry the **fixed part** $\mathrm{Fix}(R)\cap\mathcal{J}_G$: for the segment the fixed point $\tfrac12$ lies on the attractor; for the middle-thirds Cantor set $\mathrm{Fix}(R)=\{\tfrac12\}$ misses the attractor and the involution exchanges the cylinders without a fixed point; for the Sierpiński gasket the reflection fixes the corner $q_0$ and exchanges $q_1,q_2$, and the fixed part is the median segment in the gasket. The **associated reversible dynamical system** is the pair $(\varphi,R)$, whose natural extension is the two-sided shift with the reversal $\hat R$, and whose reversible invariants are the subject of *The Self-Similar Measure and the Involution*. The exchange relations of the segment, the Cantor set and the gasket were verified exactly at sample points, and the absence of the fixed point from the Cantor attractor was confirmed; the reversibility of the limit dynamical systems is quoted from the theory of the self-similar groups.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $R^2=\mathrm{id}$ | The time-reversal involution |
| $\rho$, $\rho^2=\mathrm{id}$ | The permutation of the branches |
| $R\circ S_i=S_{\rho(i)}\circ R$ | The exchange relation |
| $\tilde R(x_1x_2\cdots)=\rho(x_1)\rho(x_2)\cdots$ | The letterwise flip of the boundary |
| $R\circ\pi=\pi\circ\tilde R$ | The intertwining of the coding |
| $T_v$, $\rho(v)=v$ | The tiles and the fixed tiles |
| $\mathrm{Fix}(R)$ | The fixed points of the involution |
| $\mathrm{Fix}(R)\cap\mathcal{J}_G$ | The fixed part of the limit space |
| $R\varphi=\varphi R$, $R\sigma_x=\sigma_{\rho(x)}R$ | Reversibility of the limit dynamical system |
| $P_\rho L_\varphi P_\rho=L_\varphi$ | The conjugation of the transfer operator |

## Further Reading

- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications* (Wiley, 3rd ed. 2014), for the iterated function systems, the attractors and the open set condition.
- Volodymyr Nekrashevych, *Self-similar groups*, Mathematical Surveys and Monographs **117** (American Mathematical Society, 2005), for the limit spaces, the tiles, the coding and the reversibility of the self-similar structures.
- Laurent Bartholdi, Rostislav Grigorchuk and Volodymyr Nekrashevych, "From fractal groups to fractal sets", in *Fractals in Graz 2001* (Birkhäuser, 2003), 25–118, for the limit dynamical systems and their symmetries.
- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the natural extension, the reversible systems and the entropy.
- Michael Brin and Garrett Stuck, *Introduction to Dynamical Systems* (Cambridge University Press, 2002), for the reversal and the reversible systems.
- Andrzej Lasota and Michael C. Mackey, *Chaos, Fractals, and Noise: Stochastic Aspects of Dynamics* (Springer, 2nd ed. 1994), for the Perron–Frobenius operator of a reversible system.
