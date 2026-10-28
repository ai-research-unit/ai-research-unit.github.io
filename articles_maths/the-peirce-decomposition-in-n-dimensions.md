# __The Peirce Decomposition in $n$ Dimensions__

## Introduction

A complete family of $n$ orthogonal idempotents cuts the algebra $M_{n}(\mathbb{C})$ into $n^{2}$ lines, one for each ordered pair of members of the family. Each line is the set of elements that one idempotent selects on the left and another on the right, and the product of two lines is either zero or a third line. This is the **Peirce decomposition** of the algebra relative to the family.

The article states the decomposition for arbitrary $n$, proves that the components are lines and gives the multiplication rule. It then treats the case in which the family comes from a root of $1$, that is, from an element $H$ with $H^{n}=I$ and simple spectrum. It assumes the matrix algebra and its idempotents, and nothing else.

The article stops at the decomposition. It chooses no basis, defines no coordinates and calls no element a spinor. The basis is *The Peirce Basis in $n$ Dimensions*, and the coordinates and spinors are *Spinors as Peirce Coordinates in $n$ Dimensions*. 

## The Family

**Definition.** A family $P_{1},\dots,P_{n}$ of elements of $M_{n}(\mathbb{C})$ is **complete, orthogonal and idempotent** when

$$
P_{k}^{2}=P_{k},\qquad P_{k}P_{l}=0\ (k\ne l),\qquad \sum_{k=1}^{n}P_{k}=I .
$$

The order of the members is not part of the definition; the subscripts are labels.

**Lemma.** In $M_{n}(\mathbb{C})$ each member of a complete orthogonal family of $n$ idempotents has rank one.

**Proof.** Let $V_{k}=\operatorname{im}P_{k}$. If $\sum_{k}v_{k}=0$ with $v_{k}\in V_{k}$, applying $P_{l}$ gives $v_{l}=0$, so the sum $V_{1}+\cdots+V_{n}$ is direct. Hence

$$
n=\operatorname{rk}I=\sum_{k=1}^{n}\operatorname{rk}P_{k},
$$

and every term is at least $1$ because $P_{k}\ne0$. So every term is $1$.

**The family is not canonical.** The algebra alone carries no preferred family; a family is data. Different families give different decompositions of the same algebra.

## The Peirce Lines

**Definition.** For $k,l\in\{1,\dots,n\}$ the **Peirce line** $A_{kl}$ is

$$
A_{kl}=P_{k}M_{n}(\mathbb{C})P_{l}=\{P_{k}XP_{l}:X\in M_{n}(\mathbb{C})\}.
$$

**Theorem.** Each $A_{kl}$ is a one-dimensional complex subspace, and

$$
M_{n}(\mathbb{C})=\bigoplus_{k,l=1}^{n}A_{kl}.
$$

**Proof.** Choose $u_{k}$ spanning $V_{k}$ and a linear form $\ell_{k}$ with $\ell_{k}(u_{l})=\delta_{kl}$. The projection $P_{k}$ has image $V_{k}$ and kernel $\bigoplus_{l\ne k}V_{l}$, so $P_{k}=u_{k}\ell_{k}$. For any $X$,

$$
P_{k}XP_{l}=u_{k}\ell_{k}Xu_{l}\ell_{l}=\ell_{k}(Xu_{l})\,u_{k}\ell_{l},
$$

which lies in the complex line spanned by $u_{k}\ell_{l}$. The line is attained, because

$$
P_{k}(u_{k}\ell_{l})P_{l}=u_{k}\ell_{l}.
$$

So $A_{kl}=\mathbb{C}\,u_{k}\ell_{l}$.

Every $X$ satisfies

$$
X=\Big(\sum_{k}P_{k}\Big)X\Big(\sum_{l}P_{l}\Big)=\sum_{k,l}P_{k}XP_{l},
$$

so the lines span. If $\sum_{k,l}X_{kl}=0$ with $X_{kl}\in A_{kl}$, then multiplying on the left by $P_{k}$ and on the right by $P_{l}$ gives $X_{kl}=0$. The sum is direct.

**The diagonal lines are canonical.** $A_{kk}=\mathbb{C}P_{k}$, spanned by the idempotent itself. The off-diagonal lines have no distinguished element: the theorem exhibits one, $u_{k}\ell_{l}$, but the choice of $u_{k}$ and of $\ell_{l}$ was a choice.

## The Multiplication Rule

**Theorem.** For all $k,l,p,q$,

$$
A_{kl}A_{pq}\subseteq\delta_{lp}A_{kq}.
$$

**Proof.** For $X,Y\in M_{n}(\mathbb{C})$,

$$
(P_{k}XP_{l})(P_{p}YP_{q})=P_{k}X(P_{l}P_{p})YP_{q}=\delta_{lp}\,P_{k}XY P_{q},
$$

which lies in $A_{kq}$ when $l=p$ and is zero otherwise.

In words: the second index of the first factor must equal the first index of the second, and the product then runs from the first index of the first factor to the second index of the second.

**Corollary.** An off-diagonal line is square-zero, $A_{kl}^{2}=0$ for $k\ne l$. No element of an off-diagonal line is idempotent. The idempotents of the decomposition lie on the diagonal, and on the diagonal the only idempotents are $0$ and $P_{k}$.

## The Peirce Table

The $n^{2}$ lines are collected in the **Peirce table**, the $n\times n$ array whose entry in row $k$ and column $l$ is $A_{kl}$. The diagonal entries are the canonical lines $\mathbb{C}P_{k}$. The off-diagonal entries are the mixed lines. The table is the multiplication table of the algebra read line by line.

The array is not symmetric: $A_{kl}$ and $A_{lk}$ are different lines, exchanged by the transpose and, when the family is Hermitian, by the star. The diagonal is fixed by both.

## The Family from a Root of $1$

**The root.** Let $H\in M_{n}(\mathbb{C})$ satisfy $H^{n}=I$ and have $n$ distinct eigenvalues. Since $x^{n}-1$ has the distinct roots $\zeta^{0},\dots,\zeta^{n-1}$, with $\zeta=e^{2\pi i/n}$, the eigenvalues of $H$ are those roots, each once. Write

$$
P_{k}=\frac{1}{n}\sum_{j=0}^{n-1}\zeta^{-(k-1)j}H^{j},\qquad k=1,\dots,n .
$$

**Proposition.** The $P_{k}$ are idempotent, orthogonal and complete, each of rank one, and

$$
H=\sum_{k=1}^{n}\zeta^{k-1}P_{k}.
$$

**Proof.** On the eigenvalue $\zeta^{m}$ the polynomial $\frac1n\sum_{j}\zeta^{-(k-1)j}x^{j}$ takes the value $\delta_{m,k-1}$, so $P_{k}$ is the spectral projector of the eigenvalue $\zeta^{k-1}$. Distinct eigenvalues give orthogonal projectors, and their sum is the identity. The spectrum is simple, so each rank is one. The reconstruction of $H$ is the spectral theorem.

The family is then the spectral family of $H$. In a basis $v_{1},\dots,v_{n}$ with $Hv_{k}=\zeta^{k-1}v_{k}$ and $\ell_{l}(v_{k})=\delta_{kl}$,

$$
P_{k}=v_{k}\ell_{k},\qquad A_{kl}=\mathbb{C}\,v_{k}\ell_{l}.
$$

So the Peirce line $A_{kl}$ is the space of maps that send the $l$-th eigenline into the $k$-th and vanish on the other eigenlines, and the decomposition is the algebra's copy of the spectral decomposition of $H$.

**Without simple spectrum.** If $H^{n}=I$ but an eigenvalue is repeated, the same formula gives a complete orthogonal family, but $\operatorname{rk}P_{k}$ is the multiplicity of $\zeta^{k-1}$. The decomposition is then coarse: a component $A_{kl}$ has dimension $\operatorname{rk}P_{k}\operatorname{rk}P_{l}$, and is a line only when both multiplicities are one. The family is maximal, and the decomposition fine, exactly when the spectrum is simple.

**The case $n=2$.** A root of $1$ is an element $H$ with $H^{2}=I$. If $H\ne\pm I$, then

$$
P_{+}=\frac{I+H}{2},\qquad P_{-}=\frac{I-H}{2},
$$

and the algebra splits into the four lines $A_{++},A_{+-},A_{-+},A_{--}$.

**The case $n=3$.** With $H$ the cyclic shift satisfying $Hv_{k}=\omega^{k-1}v_{k}$ and $\omega=e^{2\pi i/3}$, the eigenvectors are $v_{1}=(1,1,1)/\sqrt3$, $v_{2}=(1,\omega,\omega^{2})/\sqrt3$ and $v_{3}=(1,\omega^{2},\omega)/\sqrt3$, and $A_{kl}=\mathbb{C}\,v_{k}v_{l}^{*}$.

## The Root Does Not Give the Basis

The root fixes the family, and therefore the decomposition. It fixes no vector in an off-diagonal line. The diagonal lines have canonical vectors, the idempotents $P_{k}$. The mixed lines do not: the element $v_{k}\ell_{l}$ depends on the normalisation of $v_{k}$ and of $\ell_{l}$, and the normalisation is a choice.

**The eigenlines are not the Peirce lines.** The eigenlines of $H$ are lines in $\mathbb{C}^{n}$. The Peirce lines are lines in $M_{n}(\mathbb{C})$. The line $A_{kl}$ is the space of maps from the $l$-th eigenline to the $k$-th, so it is attached to a pair of eigenlines and is not one of them. The spectral decomposition of the element and the Peirce decomposition of the algebra are two different decompositions, related by $A_{kl}=\mathbb{C}\,v_{k}\ell_{l}$.

**A root is not needed.** Any $n$ lines $L_{1},\dots,L_{n}$ in direct sum, with $L_{1}\oplus\cdots\oplus L_{n}=\mathbb{C}^{n}$, give the idempotents $P_{k}$ of projection onto $L_{k}$ along the other lines, hence a complete family and a Peirce decomposition. The root is a convenient source of such a family, and it adds an ordering by the eigenvalues; it is not part of the Peirce structure.

## What the Decomposition Does Not Give

The decomposition gives the lines and their multiplication. It gives no element in an off-diagonal line, no multiplication table with numerical entries, no coordinates and no spinor. The diagonal is canonical; the mixed lines are not. The choice of one element per line, its freedom and its dimension count are *The Peirce Basis in $n$ Dimensions*. The coordinates of an element and the rows of the coordinate array are *Spinors as Peirce Coordinates in $n$ Dimensions*.

## Summary

A complete family of $n$ idempotents in $M_{n}(\mathbb{C})$ has rank one at each member, and it decomposes the algebra into the $n^{2}$ lines $A_{kl}=P_{k}M_{n}P_{l}$. The product rule is $A_{kl}A_{pq}\subseteq\delta_{lp}A_{kq}$, so the off-diagonal lines are square-zero and the idempotents lie on the diagonal. The decomposition is canonical given the family, and the family is not canonical. A root $H$ with $H^{n}=I$ and simple spectrum supplies a family through its Lagrange projectors, and then $A_{kl}=\mathbb{C}\,v_{k}\ell_{l}$; the root fixes the lines and no element inside the mixed ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_{k}$ | A member of the complete orthogonal family |
| $V_{k}=\operatorname{im}P_{k}$ | The line of the $k$-th idempotent |
| $A_{kl}=P_{k}M_{n}P_{l}$ | The Peirce line, left index first |
| $u_{k}$, $\ell_{k}$ | A vector spanning $V_{k}$ and its dual form |
| $H$ | A root of $1$, $H^{n}=I$ |
| $\zeta=e^{2\pi i/n}$ | The primitive $n$-th root of unity |
| $v_{k}$ | An eigenvector of $H$ with eigenvalue $\zeta^{k-1}$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and its multiplication rule.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for idempotents, ranks and spectral projectors.
- [Roots of Unity and the Lagrange Idempotents of $M_n(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-mnc.html), for the projectors used in §*The Family from a Root of $1$*.
- [The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$](the-peirce-decomposition-and-the-corner-recursion-mnc.html), for the coarse splits and the corner recursion.
- [The Peirce Basis in $n$ Dimensions](the-peirce-basis-in-n-dimensions.html), for the choice of one element per line.
- [Spinors as Peirce Coordinates in $n$ Dimensions](spinors-as-peirce-coordinates-in-n-dimensions.html), for the rows of the coordinate array.
