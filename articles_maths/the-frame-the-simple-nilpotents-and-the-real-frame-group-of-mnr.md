# __The Frame, the Simple Nilpotents and the Real Frame Group of $M_n(\mathbb{R})$__

## Introduction

**A complete real frame carries a family of simple nilpotents $N=\sum_{k}c_{k}E_{k,k+1}$ with all $c_{k}\ne0$, and over $\mathbb{R}$ the coefficients live in $(n-1)$ copies of $\mathbb{R}^{\times}$, which is a space with $2^{n-1}$ components.**

The article defines the frame, defines the simple nilpotents relative to it, proves that such an $N$ is nilpotent of index $n$ and rank $n-1$, computes the real frame group of the frames, $\mathrm{GL}_{n}(\mathbb{R})$ with stabiliser the diagonal torus of dimension $n$, shows that the simple nilpotents over a fixed frame form a torus of dimension $n-1$ with $2^{n-1}$ components, shows that the fixing the frame $N$ is the one-dimensional group of scalars, and proves that every regular real nilpotent is conjugate to the shift $E_{12}+\cdots+E_{n-1,n}$. It assumes *The Peirce Basis and the Corners over $\mathbb{R}$* for the frame and its matrix units, and it complements *The Frame, the Simple Nilpotents and the Frame Group of $M_n(\mathbb{C})$*, where the same counts are complex.

## The Frame

**A frame is a complete family of orthogonal idempotents summing to the identity.**

$$
P_{k}P_{l}=\delta_{kl}P_{k},\qquad \sum_{k=1}^{n}P_{k}=\mathrm{I},\qquad \operatorname{rk}P_{k}=1 .
$$

Each $P_{k}$ projects onto a line $V_{k}$, the lines are independent, and $\mathbb{R}^{n}=V_{1}\oplus\cdots\oplus V_{n}$. The standard frame is $F_{k}=E_{kk}$, with $V_{k}$ the $k$-th coordinate line.

**A frame is the same datum as a real basis, taken up to scale.** A choice of nonzero $v_{k}\in V_{k}$ gives a real basis, and a different choice replaces $v_{k}$ by $t_{k}v_{k}$ with $t_{k}\ne0$; the frame is unchanged. So a frame is a basis modulo the diagonal scaling group $(\mathbb{R}^{\times})^{n}$.

**The frame carries a system of matrix units.** With $\ell_{k}$ the dual form on the lines, $E_{kl}=v_{k}\ell_{l}$ obeys $E_{ij}E_{kl}=\delta_{jk}E_{il}$ and $\sum_{k}E_{kk}=\mathrm{I}$, and $E_{kk}=P_{k}$. In this basis the elements $E_{kl}$ are the elementary arrays.

## The Simple Nilpotents

**A simple nilpotent relative to the frame is an element whose only nonzero Peirce components lie on the first superdiagonal, all of them nonzero.**

$$
N=\sum_{k=1}^{n-1}c_{k}E_{k,k+1},\qquad c_{k}\in\mathbb{R}^{\times}.
$$

In the Peirce coordinates of the frame this says $N=\sum_{k}N_{k,k+1}$ with $N_{k,k+1}\in A_{k,k+1}$ and $N_{k,k+1}\ne0$; in the adapted basis $N$ is the array with $c_{k}$ in position $(k,k+1)$ and zeros elsewhere.

**Proposition.** Such an $N$ satisfies

$$
N^{j}=\sum_{k=1}^{n-j}\Big(\prod_{i=0}^{j-1}c_{k+i}\Big)E_{k,k+j}\quad (1\le j\le n-1),\qquad N^{n}=0,
$$

so $N$ is nilpotent of index $n$, of rank $n-1$, and $\operatorname{rk}N^{j}=n-j$.

*Proof.* The power $N^{j}$ selects chains of $j$ consecutive superdiagonal steps, hence the entries on the $j$-th superdiagonal with the products of the $c$'s. Every product is nonzero, so $N^{j}\ne0$ for $j\le n-1$, and no chain of $n$ steps exists, so $N^{n}=0$. The array $N^{j}$ has $n-j$ nonzero entries, one per row, hence rank $n-j$.

**A simple nilpotent has the characteristic polynomial $x^{n}$.** All its eigenvalues are $0$, its trace is $0$, and its rank is $n-1$, so it is a single Jordan block of size $n$ over $\mathbb{R}$.

**The chain of images is the frame reversed.** The powers give

$$
\operatorname{im}N^{j}=\operatorname{span}(v_{1},\dots,v_{n-j}),\qquad \ker N^{j}=\operatorname{span}(v_{1},\dots,v_{j}),
$$

so $N$ moves each line of the frame one step, and the flag it defines is the frame read backwards.

## The Relations with the Idempotents

**The simple nilpotent is characterised by its Peirce relations with the frame.** The corner rule gives

$$
E_{kk}N=NE_{k+1,k+1}\quad (k=1,\dots,n-1),\qquad E_{kk}N=0\ \text{for}\ k=n,\qquad NE_{11}=0 ,
$$

and, conversely, an element satisfying these relations and lying in the sum of the corners $A_{k,k+1}$ is of the form above.

*Proof.* Multiply $N=\sum_{j}c_{j}E_{j,j+1}$ on the left by $E_{kk}$ and on the right by $E_{k+1,k+1}$; the table $E_{kk}E_{j,j+1}=\delta_{kj}E_{j,j+1}$ and $E_{j,j+1}E_{k+1,k+1}=\delta_{j,k}E_{j,j+1}$ leaves $c_{k}E_{k,k+1}$ on both sides.

**The relations say that $N$ shifts the frame and kills the ends.** $N$ maps $V_{k+1}$ to $V_{k}$ for $k\le n-1$, and it kills $V_{1}$; so $N$ is a chain map of the frame into itself, decreasing the index by one.

**The coefficients are the frame dependent data.** A different choice of the vectors $v_{k}$ changes the units by $E_{kl}\mapsto t_{k}t_{l}^{-1}E_{kl}$ and hence

$$
c_{k}\longmapsto \frac{t_{k}}{t_{k+1}}c_{k},
$$

so the individual numbers $c_{k}$ are not attached to the frame; only their orbit under the diagonal group is.

## The Real Frame Group of the Frames

**Conjugation by $\mathrm{GL}_{n}(\mathbb{R})$ acts transitively on the frames.** For two frames there is $S\in\mathrm{GL}_{n}(\mathbb{R})$ with $P'_{k}=SP_{k}S^{-1}$ for all $k$, built from two real bases adapted to the frames.

**The stabiliser of the standard frame is the diagonal subgroup.**

$$
D=\{\operatorname{diag}(t_{1},\dots,t_{n}):t_{k}\in\mathbb{R}^{\times}\}\cong(\mathbb{R}^{\times})^{n},
$$

of dimension $n$. The quotient is the variety of frames,

$$
\text{frames}=\mathrm{GL}_{n}(\mathbb{R})/D,\qquad \dim=n^{2}-n .
$$

**The group is real and not complex.** The conjugating matrix is real because both adapted bases are real; a complex matrix carrying the standard frame to a real frame is real up to a diagonal factor, and the diagonal factor acts trivially.

**The counts at $n=3$ and $n=4$.** At $n=3$ the frame variety has dimension $9-3=6$; at $n=4$ it has dimension $16-4=12$. The diagonal torus has dimension $n$ in both cases, and the two numbers add to $n^{2}$, the dimension of the group.

## The Torus of Simple Nilpotents

**Over a fixed frame the simple nilpotents form $(n-1)$ copies of $\mathbb{R}^{\times}$.**

$$
\mathcal{N}(P)=\Big\{\sum_{k=1}^{n-1}c_{k}E_{k,k+1}:c_{k}\in\mathbb{R}^{\times}\Big\}\cong(\mathbb{R}^{\times})^{n-1},
$$

of real dimension $n-1$.

**The space has $2^{n-1}$ connected components.** Each factor $\mathbb{R}^{\times}$ has two components, the positive and the negative reals, so a connected component is labelled by the signs of the $n-1$ coefficients:

$$
\varepsilon=(\operatorname{sgn}c_{1},\dots,\operatorname{sgn}c_{n-1})\in\{\pm1\}^{n-1}.
$$

Two simple nilpotents lie in the same component exactly when all their coefficients have the same signs.

**The diagonal frame group acts transitively on the whole torus.** The group $D$ acts by $c_{k}\mapsto t_{k}t_{k+1}^{-1}c_{k}$, and the map $D\to(\mathbb{R}^{\times})^{n-1}$, $t\mapsto(t_{1}t_{2}^{-1},\dots,t_{n-1}t_{n}^{-1})$, is surjective: given the ratios, choose $t_{1}$ and then $t_{k+1}=t_{k}(t_{k}t_{k+1}^{-1})^{-1}$. So all $2^{n-1}$ sign classes lie in one orbit of the frame-preserving frame group, and the components are a topological fact about $\mathbb{R}^{\times}$, not a dynamical one.

**The count is the orbit–stabiliser count inside $D$.** The stabiliser is computed in the next section and has dimension $1$, so

$$
\dim D=n=\underbrace{(n-1)}_{\text{simple nilpotents}}+\underbrace{1}_{\text{stabiliser}}.
$$

## The Frame Group that Fixes the Nilpotent

**The frame transformations fixing a simple nilpotent are the scalar matrices.**

$$
\{S\in D:SN=NS\}=\{t\,\mathrm{I}:t\in\mathbb{R}^{\times}\},
$$

a group of dimension $1$, with $2$ components.

*Proof.* Write $S=\operatorname{diag}(t_{1},\dots,t_{n})$ and compare the $(k,k+1)$ entries of $SN$ and $NS$: they are $t_{k}c_{k}$ and $t_{k+1}c_{k}$, so equality for all $k$ gives $t_{k}=t_{k+1}$, since $c_{k}\ne0$. Hence all $t_{k}$ are equal.

**The scalars act trivially on the frame and on the Peirce coordinates.** A scalar matrix commutes with every element of the algebra, so it fixes the frame, the units and the nilpotent; the one-dimensional group is the kernel of the action and not a genuine symmetry of the data.

**A negative scalar acts trivially on the nilpotent and on the units.** It fixes every $E_{kl}$, since $t_{k}t_{l}^{-1}=1$, and changes the vectors $v_{k}$ by a common sign, which is invisible in the frame.

## The Canonical Form

**The shift $N_{0}=E_{12}+E_{23}+\cdots+E_{n-1,n}$ is the simple nilpotent with all $c_{k}=1$.**

$$
N_{0}=\begin{pmatrix}0&1& & \\ &0&1& \\ & & \ddots&1\\ & & &0\end{pmatrix}.
$$

**Theorem.** Every regular nilpotent of $M_{n}(\mathbb{R})$, that is, every real matrix with characteristic polynomial $x^{n}$ and rank $n-1$, is conjugate over $\mathbb{R}$ to $N_{0}$.

*Proof.* Let $N$ be such a matrix. Such a vector exists: if $N^{n-1}=0$ then every Jordan block has size at most $n-1$, so there are at least two blocks and the rank is at most $n-2$. The vectors $v,Nv,\dots,N^{n-1}v$ are independent: a relation of least degree would give $N^{m}v\in\operatorname{span}(v,\dots,N^{m-1}v)$, hence $N^{n-1}v=0$. In the reversed basis $N^{n-1}v,\dots,Nv,v$ the matrix of $N$ is the shift, so with $S$ the matrix of that basis,

$$
S^{-1}NS=N_{0}.
$$

The basis is real because $N$ and $v$ are real, so the conjugating matrix is in $\mathrm{GL}_{n}(\mathbb{R})$.

**The canonical form is the statement that the frame's nilpotent has no moduli over $\mathbb{R}$.** Every regular nilpotent has a real Jordan form with one block, and one block of size $n$ is the shift. The simple nilpotents of a fixed frame are the shifts of that frame, and the frame group carries any one of them to any other, so the coefficients $c_{k}$ are pure frame group.

**The theorem does not hold with a fixed frame.** A regular nilpotent carries its own frame, the flag $\operatorname{im}N^{n-1}\subset\cdots\subset\operatorname{im}N\subset\mathbb{R}^{n}$ refined by lines, and that frame is what the conjugating matrix must respect; the freedom is the $n$-dimensional diagonal torus, and the $n-1$ coefficients are its coordinates.

## The Checks at $n=3$ and $n=4$

**The characteristic polynomial of a random regular nilpotent is $x^{n}$.** Building $N=SN_{0}S^{-1}$ with $S$ a random real matrix with integer entries in a small range, the characteristic polynomial computed with numpy is $x^{3}$ at $n=3$ and $x^{4}$ at $n=4$, and the rank is $n-1$ in every trial. Building $N$ directly as $\sum_{k}c_{k}E_{k,k+1}$ with random nonzero $c_{k}$ gives the same answers.

**The powers behave as predicted.** At $n=4$ with all $c_{k}=1$ the ranks of $N^{0},N^{1},N^{2},N^{3},N^{4}$ are $4,3,2,1,0$, which is the sequence $n-j$; and $N^{4}=0$ while $N^{3}\ne0$.

**The dimension count closes at every $n$.** The frame variety has dimension $n^{2}-n$, the nilpotent torus over a frame has dimension $n-1$, and the diagonal stabiliser has dimension $n$; the identity $n^{2}-n+(n-1)+1=n^{2}$ is the dimension of $\mathrm{GL}_{n}(\mathbb{R})$.

## Summary

A frame of $M_{n}(\mathbb{R})$ is a complete family of orthogonal rank-one idempotents summing to $\mathrm{I}$, equivalently a real basis taken up to diagonal scaling. Relative to a frame with matrix units $E_{kl}$, a simple nilpotent is $N=\sum_{k=1}^{n-1}c_{k}E_{k,k+1}$ with all $c_{k}\ne0$; it obeys $E_{kk}N=NE_{k+1,k+1}$, has powers with entries on the successive superdiagonals, is nilpotent of index $n$, and has rank $n-1$, hence characteristic polynomial $x^{n}$. The real frame group is conjugation by $\mathrm{GL}_{n}(\mathbb{R})$, which acts transitively on the frames with stabiliser the diagonal torus $D\cong(\mathbb{R}^{\times})^{n}$ of dimension $n$, so the frame variety has dimension $n^{2}-n$: $6$ at $n=3$ and $12$ at $n=4$. Over a fixed frame the simple nilpotents form $(\mathbb{R}^{\times})^{n-1}$, of dimension $n-1$ and with $2^{n-1}$ components labelled by the signs of the coefficients, and the diagonal frame group acts transitively on that torus. The fixing the frame a simple nilpotent is the group of scalar matrices, of dimension $1$ and with $2$ components, so $n=(n-1)+1$ inside $D$. The canonical form is the shift $E_{12}+\cdots+E_{n-1,n}$, and every real regular nilpotent is conjugate to it, with a real conjugating matrix built from the Krylov basis $v,Nv,\dots,N^{n-1}v$; this is confirmed at $n=3$ and $n=4$ by the characteristic polynomial $x^{n}$ and the rank $n-1$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_{k}$, $V_{k}$ | The idempotents of the frame and their lines |
| $E_{kl}$ | The matrix unit $v_{k}\ell_{l}$ of the frame |
| $N=\sum_{k}c_{k}E_{k,k+1}$ | A simple nilpotent, with $c_{k}\in\mathbb{R}^{\times}$ |
| $D\cong(\mathbb{R}^{\times})^{n}$ | The diagonal stabiliser of the standard frame |
| $\mathcal{N}(P)\cong(\mathbb{R}^{\times})^{n-1}$ | The simple nilpotents over the frame $P$ |
| $\mathrm{GL}_{n}(\mathbb{R})/D$ | The frame variety, of dimension $n^{2}-n$ |
| $N_{0}=E_{12}+\cdots+E_{n-1,n}$ | The shift, canonical form of a regular nilpotent |
| $v,Nv,\dots,N^{n-1}v$ | The Krylov basis of a regular nilpotent |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for frames, matrix units and the conjugation that carries one frame to another.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for nilpotent matrices, Jordan forms over $\mathbb{R}$ and the Krylov basis.
- James E. Humphreys, *Linear Algebraic Groups* (Springer, 1975), for the diagonal torus, homogeneous spaces and the orbit–stabiliser count.
- [The Peirce Basis and the Corners over $\mathbb{R}$](the-peirce-basis-and-the-corners-over-r.html), for the corners and the frame that the simple nilpotents use.
- [The Frame, the Simple Nilpotents and the Frame Group of $M_n(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-frame-group-of-mnc.html), for the complex version of the same construction.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the matrix units and the transpose over $\mathbb{R}$.
