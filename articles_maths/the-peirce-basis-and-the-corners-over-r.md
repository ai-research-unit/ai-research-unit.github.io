# __The Peirce Basis and the Corners over $\mathbb{R}$__

## Introduction

**A real frame cuts $M_{n}(\mathbb{R})$ into $n^{2}$ real corners, the corners multiply by the matrix-unit table, and the residual freedom is conjugation by an invertible real matrix, so the frame variety has dimension $n^{2}-n$.**

The article states the corners, proves that they sum directly to the algebra, states the products $E_{ij}E_{kl}=\delta_{jk}E_{il}$, defines a system of matrix units over $\mathbb{R}$, reads the corners as joint eigenspaces of two commuting families of operators, and computes the real gauge. Frames of equal ranks are conjugate by $\mathrm{GL}_{n}(\mathbb{R})$, the stabiliser is the diagonal subgroup $D$, and the frame variety is $\mathrm{GL}_{n}(\mathbb{R})/D$, of dimension $n^{2}-n$. It assumes *The Peirce Basis in $n$ Dimensions*, which runs the same list over $\mathbb{C}$, and defers the symmetric half of the corners to *The Peirce Decomposition of $\operatorname{Sym}_n$ as a Jordan Algebra*.

## The Frame

**A frame is an ordered family of orthogonal idempotents summing to the identity.**

$$
P_{k}P_{l}=\delta_{kl}P_{k},\qquad \sum_{k=1}^{n}P_{k}=\mathrm{I}.
$$

The rank $r_{k}=\operatorname{rk}P_{k}$ is part of the data and $\sum_{k}r_{k}=n$. The frame is **complete** when every $r_{k}=1$, and the standard frame is $F_{k}=E_{kk}$.

**The subspaces $V_{k}=\operatorname{im}P_{k}$ are independent and sum to $\mathbb{R}^{n}$.** The idempotent $P_{k}$ is the identity on $V_{k}$ and kills the other $V_{l}$, so $\mathbb{R}^{n}=\bigoplus_{k}V_{k}$ with $\dim V_{k}=r_{k}$. A frame is the same datum as a decomposition of $\mathbb{R}^{n}$ into ordered real subspaces of dimensions $r_{k}$.

## The Corners

**A corner is the space of maps from one subspace of the frame to another.**

$$
A_{kl}=P_{k}M_{n}(\mathbb{R})P_{l}=\{P_{k}XP_{l}:X\in M_{n}(\mathbb{R})\}.
$$

**Proposition.** $\dim A_{kl}=r_{k}r_{l}$, the corners are independent, and

$$
M_{n}(\mathbb{R})=\bigoplus_{k,l=1}^{n}A_{kl},\qquad \sum_{k,l}r_{k}r_{l}=\Big(\sum_{k}r_{k}\Big)^{2}=n^{2}.
$$

*Proof.* As a space of maps, $A_{kl}=\operatorname{Hom}(V_{l},V_{k})$, so its dimension is $r_{k}r_{l}$. Expanding the identity on both sides of $X$,

$$
X=\Big(\sum_{k}P_{k}\Big)X\Big(\sum_{l}P_{l}\Big)=\sum_{k,l}P_{k}XP_{l},
$$

gives the sum. For independence, multiply $\sum_{k,l}X_{kl}=0$ on the left by $P_{i}$ and on the right by $P_{j}$; every term dies except $X_{ij}$.

**The diagonal corner is the endomorphism algebra of its subspace.** $A_{kk}=\operatorname{End}(V_{k})$ has dimension $r_{k}^{2}$, and the off-diagonal corner is the space of maps $V_{l}\to V_{k}$, of dimension $r_{k}r_{l}$. At a complete frame all $n^{2}$ corners have dimension one.

## The Multiplication Table

**The product of the corner $(k,l)$ with the corner $(p,q)$ lands in the corner $(k,q)$, and only when $l=p$.** From $P_{l}P_{p}=\delta_{lp}P_{l}$,

$$
A_{kl}A_{pq}\subseteq\delta_{lp}A_{kq}.
$$

**One nonzero element per corner gives the table of the matrix units.** For a complete frame and $E_{kl}\in A_{kl}$ nonzero, the rule is

$$
E_{ij}E_{kl}=\delta_{jk}E_{il},
$$

which is the table of the elementary matrices read in the frame. It forces $E_{kk}=P_{k}$: the diagonal element is $c_{k}P_{k}$, and the rule with all indices equal gives $c_{k}^{2}=c_{k}$, hence $c_{k}=1$.

**A complete real frame realises the table with real rank-one matrices.** Let $v_{k}\in V_{k}$ be nonzero and let $\ell_{k}$ be the real form with $\ell_{k}(v_{l})=\delta_{kl}$. Then $E_{kl}=v_{k}\ell_{l}$ is real, lies in $A_{kl}$, and

$$
E_{kl}E_{pq}=v_{k}\ell_{l}(v_{p})\ell_{q}=\delta_{lp}E_{kq},\qquad E_{kk}=P_{k}.
$$

The $v_{k}$ are a real basis of $\mathbb{R}^{n}$ and the $\ell_{k}$ its real dual basis.

## Systems of Matrix Units

**A system of $n\times n$ matrix units over $\mathbb{R}$ is a family $E_{ij}\in M_{n}(\mathbb{R})$ with that table and diagonal sum the identity.**

$$
E_{ij}E_{kl}=\delta_{jk}E_{il},\qquad \sum_{k=1}^{n}E_{kk}=\mathrm{I}.
$$

**Proposition.** Such a family is a basis of the algebra, its diagonal members are the idempotents of a frame, and $E_{ij}\mapsto$ elementary array is an isomorphism of algebras.

*Proof.* The table gives $E_{kk}^{2}=E_{kk}$ and $E_{kk}E_{ll}=0$ for $k\ne l$, so the $E_{kk}$ are a frame, and the second condition makes it sum to the identity. The products span the algebra by the table and $\mathrm{I}=\sum_{k}E_{kk}$; by the corner decomposition of that frame each corner is the line spanned by $E_{kl}$, so the $n^{2}$ elements are independent. The assignment $E_{ij}\mapsto$ elementary array is linear and bijective, and both sides obey the same table, so it is multiplicative.

**Every system of units is conjugate to the standard one.** The $E_{kk}$ have rank one and are mutually orthogonal, so $\mathbb{R}^{n}=\bigoplus_{k}\operatorname{im}E_{kk}$. For $v_{k}\in\operatorname{im}E_{kk}$ nonzero, the real matrix $S$ with columns $v_{k}$ is invertible, and $S^{-1}E_{ij}S$ sends $v_{j}$ to $v_{i}$ and kills the other $v_{m}$, hence is the elementary array. The conjugating matrix is unique up to the diagonal subgroup.

## The Two Peirce Operators

**The corners are the joint eigenspaces of two commuting families of operators.**

$$
L_{k}(X)=P_{k}X,\qquad R_{k}(X)=XP_{k}.
$$

**Proposition.** The $2n$ operators commute, and

$$
A_{kl}=\{X:L_{k}X=X,\ R_{l}X=X,\ L_{i}X=R_{j}X=0\ \text{for}\ i\ne k,\ j\ne l\}.
$$

*Proof.* $L_{k}L_{i}=\delta_{ki}L_{k}$ and $L_{k}R_{j}=R_{j}L_{k}$, so the family commutes. The displayed conditions say $P_{k}XP_{l}=X$, which leaves exactly the $r_{k}r_{l}$ entries that define the corner.

**The eigenvalues are the real numbers $0$ and $1$.** Each $L_{k}$ and $R_{k}$ is $\mathbb{R}$-linear with spectrum $\{0,1\}$, so the joint eigenspaces of a real frame are real subspaces, and no complex number enters the cut.

## The Real Gauge

**Two frames with the same rank vector differ by conjugation by an invertible real matrix.** There is $S\in\mathrm{GL}_{n}(\mathbb{R})$ with

$$
P'_{k}=SP_{k}S^{-1},\qquad k=1,\dots,n .
$$

*Proof.* Take a real basis adapted to $P$, with the first $r_{1}$ vectors in $V_{1}$, the next $r_{2}$ in $V_{2}$, and so on, and a real basis $v'_{m}$ adapted to $P'$ in the same way. The matrix $S$ with $Sv_{m}=v'_{m}$ is real and invertible, and it carries $V_{k}$ isomorphically to $V'_{k}$; such a map conjugates the projection onto $V_{k}$ into the projection onto $V'_{k}$.

**The group acting is $\mathrm{GL}_{n}(\mathbb{R})$, not $\mathrm{GL}_{n}(\mathbb{C})$.** Both bases above are real, so $S$ is real. A complex $S$ that carries the standard frame to a real frame is real up to a diagonal factor: the $k$-th idempotent is sent to the projection onto the line spanned by the $k$-th column, so that column is a complex multiple of a real vector, and $S=A\operatorname{diag}(u_{1},\dots,u_{n})$ with $A$ real and all $u_{k}\ne0$. Diagonal matrices act trivially on the standard frame, so the complex matrices producing a given real frame are the real ones times the diagonal ones.

**The stabiliser is the diagonal subgroup.** If $S$ commutes with every $E_{kk}$, comparing entries in $SE_{kk}=E_{kk}S$ gives $S_{ij}=0$ for $i\ne j$. Hence

$$
D=\{\operatorname{diag}(t_{1},\dots,t_{n}):t_{k}\in\mathbb{R}^{\times}\},
$$

of dimension $n$.

**The gauge acts on the units by ratios.** Conjugation sends $E_{kl}=v_{k}\ell_{l}$ to $(Sv_{k})(\ell_{l}S^{-1})$; for diagonal $S$ with entries $t_{k}$,

$$
E_{kl}\longmapsto t_{k}t_{l}^{-1}E_{kl},
$$

and the idempotents $E_{kk}$ are fixed.

## The Frame Variety

**The complete frames form the homogeneous space $\mathrm{GL}_{n}(\mathbb{R})/D$, of dimension $n^{2}-n$.** The map $S\mapsto(SE_{11}S^{-1},\dots,SE_{nn}S^{-1})$ is surjective by the conjugation theorem and has fibres the right cosets of $D$, so

$$
\dim(\text{frames})=n^{2}-n,\qquad n^{2}=\underbrace{(n^{2}-n)}_{\text{frames}}+\underbrace{n}_{\dim D}.
$$

**At $n=3$ the dimension is $6$.** The numbers are $9-3=6$. A frame is a decomposition of $\mathbb{R}^{3}$ into three lines, which costs $3\cdot 2=6$ parameters. Over $\mathbb{C}$ the same quotient has complex dimension $n^{2}-n$, hence real dimension $2(n^{2}-n)$: the real variety has half that, and the factor two is the passage from $\mathbb{R}$ to $\mathbb{C}$ in the group.

**The tangent space confirms the count.** With $S=\mathrm{I}+\epsilon X$ the frame moves by $P_{k}(\epsilon)=\mathrm{I}+\epsilon[X,P_{k}]$, so the tangent space at the standard frame is spanned by the commutators $[X,E_{kk}]$. That span has dimension $6$ at $n=3$ and $12$ at $n=4$, and the kernel of $X\mapsto([X,E_{kk}])_{k}$ is the diagonal matrices.

## The Real Content: Simultaneous Diagonalisation

**A frame of real idempotents exists exactly when the idempotents are simultaneously diagonalisable over $\mathbb{R}$.** For commuting real idempotents $P_{k}$ with $\sum_{k}P_{k}=\mathrm{I}$ and ranks $r_{k}$ there is $S\in\mathrm{GL}_{n}(\mathbb{R})$ with

$$
S^{-1}P_{k}S=\operatorname{diag}(\underbrace{1,\dots,1}_{r_{k}},\underbrace{0,\dots,0}_{n-r_{k}})
$$

in block position $k$. This is the adapted-basis argument again: the images $V_{k}$ are independent and sum to $\mathbb{R}^{n}$, and a real basis chosen block by block diagonalises all the $P_{k}$ at once.

**The diagonalising matrix is real because the eigenvalues are real.** The real content is not commutativity, which holds over $\mathbb{C}$ too, but the fact that the eigenvalues are the real numbers $0$ and $1$. For distinct real $\lambda_{k}$ the combination $H=\sum_{k}\lambda_{k}P_{k}$ has eigenvalues $\lambda_{k}$; every eigenvector of $H$ is an eigenvector of every $P_{k}$, and the eigenvectors of a real matrix with distinct real eigenvalues are real.

**The ranks are arbitrary and they are the only invariant.** For every composition $n=r_{1}+\cdots+r_{n}$ with $r_{k}\ge1$, a real invertible $S$ and the diagonal blocks $\Delta_{k}$ give the frame $P_{k}=S\Delta_{k}S^{-1}$. Two frames are conjugate by $\mathrm{GL}_{n}(\mathbb{R})$ exactly when their rank vectors agree.

**The frame comes from a real basis.** The unit $E_{kl}=v_{k}\ell_{l}$ is a real matrix only if $v_{k}$ and $\ell_{l}$ are real, and a real frame supplies them, since each $\operatorname{im}P_{k}$ is a real line. No real frame needs complex vectors in its Peirce basis.

**A frame need not be symmetric.** The corner $A_{kl}=\operatorname{Hom}(V_{l},V_{k})$ requires real subspaces only. The frames fixed by the transpose, with $P_{k}^{\mathsf T}=P_{k}$, are treated in *The Peirce Decomposition and the Two Halves over $\mathbb{R}$*.

## Summary

A frame of $M_{n}(\mathbb{R})$ is an ordered family of orthogonal real idempotents summing to the identity, equivalently a decomposition of $\mathbb{R}^{n}$ into ordered real subspaces $V_{k}$ of ranks $r_{k}$. The corners $A_{kl}=P_{k}M_{n}(\mathbb{R})P_{l}=\operatorname{Hom}(V_{l},V_{k})$ have dimension $r_{k}r_{l}$, sum directly to the algebra, and multiply by $A_{kl}A_{pq}\subseteq\delta_{lp}A_{kq}$; a system of matrix units is one real element $E_{kl}$ per corner with $E_{ij}E_{kl}=\delta_{jk}E_{il}$ and $\sum_{k}E_{kk}=\mathrm{I}$, and it is a basis of the algebra. The corners are the joint eigenspaces of the Peirce operators $L_{k}(X)=P_{k}X$ and $R_{k}(X)=XP_{k}$, with eigenvalues $0$ and $1$. Frames of equal ranks are conjugate by $\mathrm{GL}_{n}(\mathbb{R})$, with stabiliser the diagonal group $D$ of dimension $n$, so the frame variety is $\mathrm{GL}_{n}(\mathbb{R})/D$ of real dimension $n^{2}-n$; at $n=3$ that is $9-3=6$, half the real dimension $12$ of the complex frame space. The real content is that a frame of real idempotents exists exactly when the idempotents are simultaneously diagonalisable over $\mathbb{R}$, which holds because the eigenvalues are real; then the ranks are arbitrary and the units come from a real basis.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_{k}$ | The $k$-th idempotent of the frame |
| $V_{k}=\operatorname{im}P_{k}$ | The real subspace of the $k$-th idempotent |
| $r_{k}=\operatorname{rk}P_{k}$ | The rank, with $\sum_{k}r_{k}=n$ |
| $A_{kl}=P_{k}M_{n}(\mathbb{R})P_{l}$ | The corner, isomorphic to $\operatorname{Hom}(V_{l},V_{k})$ |
| $E_{kl}$ | The chosen element of $A_{kl}$ |
| $L_{k},R_{k}$ | The Peirce operators $X\mapsto P_{k}X$ and $X\mapsto XP_{k}$ |
| $D$ | The diagonal subgroup of $\mathrm{GL}_{n}(\mathbb{R})$ |
| $\mathrm{GL}_{n}(\mathbb{R})/D$ | The frame variety, of dimension $n^{2}-n$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for Peirce corners, systems of matrix units and their uniqueness up to conjugation.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for idempotents, adapted bases and simultaneous diagonalisation over $\mathbb{R}$.
- [The Peirce Basis in $n$ Dimensions](the-peirce-basis-in-n-dimensions.html), for the complex version of the same table and the gauge on the units.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the matrix units and the transpose over $\mathbb{R}$.
- [The Peirce Decomposition of $\operatorname{Sym}_n$ as a Jordan Algebra](the-peirce-decomposition-of-sym-n-r-as-a-jordan-algebra.html), for the symmetric half of the corners.
- [The Frame, the Simple Nilpotents and the Real Gauge of $M_n(\mathbb{R})$](the-frame-the-simple-nilpotents-and-the-real-gauge-of-mnr.html), for the nilpotents attached to a frame.
