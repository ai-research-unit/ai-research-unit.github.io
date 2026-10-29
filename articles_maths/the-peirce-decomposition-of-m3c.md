# __The Peirce Decomposition of $M_3(\mathbb{C})$__

## Introduction

Three orthogonal rank-one idempotents cut $M_3(\mathbb{C})$ into $9$ lines, one for each ordered pair. This article states the cut for an arbitrary complete family, proves that the lines are one-dimensional and sum directly, and gives the multiplication rule. It then specialises to the family of a root $H$ with $H^{3}=I$ and simple spectrum.

The article is the family-level part of the trilogy. *The Peirce Basis of $M_3(\mathbb{C})$* chooses one element in each line and computes the gauge; *Spinors as Peirce Coordinates in $M_3(\mathbb{C})$* reads the columns of the array. The root and its projectors are *Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$*; the flag and the adjoint orbits are *The Adjoint Action, the Orbits and the Flag Variety of $M_3(\mathbb{C})$*.

## The Family

**Definition.** A family $P_1,\dots,P_3$ in $M_3(\mathbb{C})$ is **complete, orthogonal and idempotent** when the members are nonzero and

$$
P_k^{2}=P_k,\qquad P_kP_l=0\ (k\ne l),\qquad \sum_{k=1}^{3}P_k=I .
$$

The order of the labels is part of the data; the unordered set is not the family.

**Lemma.** Each member of a complete orthogonal family of 3 nonzero idempotents in $M_3(\mathbb{C})$ has rank one.

**Proof.** Let $V_k=\operatorname{im}P_k$. If $\sum_kv_k=0$ with $v_k\in V_k$, applying $P_l$ gives $v_l=0$, so the sum $V_1+\cdots+V_3$ is direct and

$$
3=\operatorname{rk}I=\sum_{k=1}^{3}\operatorname{rk}P_k .
$$

Every term is at least $1$ because $P_k\ne0$, so every term is $1$.

**The family is not canonical.** The algebra carries no preferred family. Different families give different cuts of the same algebra.

## The Lines

**Definition.** For $k,l\in\{1,\dots,3\}$ the **Peirce line** is

$$
A_{kl}=P_kM_3(\mathbb{C})P_l=\{P_kXP_l:X\in M_3(\mathbb{C})\}.
$$

**Theorem.** Each $A_{kl}$ is a complex line, and

$$
M_3(\mathbb{C})=\bigoplus_{k,l=1}^{3}A_{kl}.
$$

**Proof.** Choose $u_k$ spanning $V_k$ and a form $\ell_k$ with $\ell_k(u_l)=\delta_{kl}$. Then $P_k=u_k\ell_k$, so for every $X$,

$$
P_kXP_l=u_k\,\ell_k(Xu_l)\,\ell_l\in\mathbb{C}\,u_k\ell_l,
$$

and the line is attained because $P_k(u_k\ell_l)P_l=u_k\ell_l$. The sum covers the algebra by inserting $I=\sum_kP_k$ on both sides of $X$, and it is direct because multiplying $\sum X_{kl}=0$ by $P_k$ on the left and $P_l$ on the right leaves $X_{kl}=0$. 

## The Multiplication Rule

**Theorem.** For all indices,

$$
A_{kl}A_{pq}\subseteq\delta_{lp}A_{kq}.
$$

**Proof.** $(P_kXP_l)(P_pYP_q)=P_kX(P_lP_p)YP_q=\delta_{lp}P_kXYP_q$.

The right index of the first factor must equal the left index of the second. The off-diagonal lines are square-zero and contain no idempotent; the idempotents of the cut are the $P_k$ on the diagonal.

## The Root

Let $H\in M_3(\mathbb{C})$ satisfy $H^{3}=I$ and have simple spectrum. Its eigenvalues are the Three roots of unity, and with $\omega=e^{2\pi i/3}$ they are $1,\omega,\dots,\omega^{2}$. The Lagrange projectors are

$$
P_k=\frac{1}{3}\sum_{j=0}^{3-1}\omega^{-(k-1)j}H^{j},\qquad k=1,\dots,3,
$$

and $H=\sum_k\omega^{k-1}P_k$. In the eigenbasis,

$$
H=\operatorname{diag}(1,\omega,\dots,\omega^{2}),\qquad P_k=E_{kk},
$$

so the Peirce lines are the matrix units $A_{kl}=\mathbb{C}E_{kl}$. In any other basis, with $v_k$ the eigenvector of $\omega^{k-1}$ and $\ell_l$ the dual form,

$$
E_{kl}=v_k\ell_l,\qquad v_k=\frac{1}{\sqrt{3}}\bigl(1,\omega^{k-1},\omega^{2(k-1)},\dots,\omega^{(3-1)(k-1)}\bigr)^{T}.
$$

The matrix $F=[v_1|\cdots|v_3]$ is the Fourier matrix, unitary, and $F^{*}HF$ is diagonal.

**The root fixes the lines and no element inside a mixed one.** The diagonal line has the canonical vector $P_k$. The mixed line $\mathbb{C}v_k\ell_l$ depends on the normalisation of $v_k$ and $\ell_l$; that choice is the subject of the next article.

## Dimensions and the Case

The cut has $9$ lines. The family space, the set of ordered $3$-tuples of lines summing to $\mathbb{C}^{3}$, has dimension $3^{2}-3=6$; the gauge has dimension $3-1=2$; the frame space has dimension $3^{2}-1=8$. These numbers are computed in *The Peirce Basis of $M_3(\mathbb{C})$*.

For $n=3$ the order of $H$ is $3$, so no power of $H$ is an involution. A grading that commutes with the family is $\operatorname{Ad}_S$ with $S=\operatorname{diag}(\sigma_1,\sigma_2,\sigma_3)$ and $\sigma_k=\pm1$; its sign pattern has $p$ plus signs and $3-p$ minus signs. The balanced split does not exist. The possible splits are $1+2$, and each depends on the choice of $S$. The decomposition itself supplies no chirality.

**The coarse split.** A single rank-one idempotent and its complement split the algebra into four corners of dimensions $1+2+2+4$, and the diagonal corners are $\mathbb{C}$ and $M_2(\mathbb{C})$. The fine cut refines it: the corner $PMQ$ is the sum of the lines $A_{1l}$ with $l\ne1$, and the other two corners are the same sums on the other side. The rank-$p$ version is *The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$*.

**Example.** For $u=(1,\dots,1)$ and $P=uu^{\mathsf T}/n$, the corner $PMQ$ consists of matrices whose rows are equal and sum to zero, and $QMP$ consists of matrices whose columns are equal and sum to zero, with $PAP=(\sigma(A)/n)P$ and $\sigma(A)=\sum_{i,j}A_{ij}$.

**The adjoint.** The chain of the frame acts on the traceless part, and

$$
\mathfrak{sl}_3(\mathbb{C})=3\oplus5
$$

as a direct sum of irreducible $\mathfrak{sl}_2$-spaces of dimensions $3,5,\dots,5$. The column $\mathbb{C}^{3}$ has highest weight $2$. Both statements are the standard $\mathfrak{sl}_2$ computation on the column; they are recorded here because the number of lines and the number of components must agree with them.

## What the Cut Does Not Give

The cut gives the lines and their product. It gives no element in a mixed line, no basis, no gauge and no coordinate. The diagonal is canonical; the mixed lines are not. The selection of one element per line and its freedom are *The Peirce Basis of $M_3(\mathbb{C})$*. The coordinate columns and their reading as spinors are *Spinors as Peirce Coordinates in $M_3(\mathbb{C})$*.

## Summary

A complete family of $3$ nonzero idempotents in $M_3(\mathbb{C})$ has rank one at each member and cuts the algebra into the $9$ lines $A_{kl}=P_kM_3P_l$. The rule is $A_{kl}A_{pq}\subseteq\delta_{lp}A_{kq}$, so the off-diagonal lines are square-zero and the idempotents lie on the diagonal. A root $H^{3}=I$ with simple spectrum supplies the family through its Lagrange projectors, and then $A_{kl}=\mathbb{C}v_k\ell_l$. The cut is canonical given the family; the family is not canonical; no element of a mixed line is selected.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_k$ | A member of the complete family |
| $V_k=\operatorname{im}P_k$ | Its line in $\mathbb{C}^{3}$ |
| $A_{kl}=P_kM_3P_l$ | The Peirce line |
| $v_k,\ell_k$ | An eigenvector of $H$ and its dual form |
| $H$ | A root, $H^{3}=I$ with simple spectrum |
| $\omega$ | The root of unity, $\omega=e^{2\pi i/3}$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and its rule.
- [The Matrix Algebra $M_3(\mathbb{C})$](the-matrix-algebra-m3c.html), for the algebra and its matrix units.
- [Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m3c.html), for the projectors of the root.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_3(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m3c.html), for the flag and the orbits.
- [The Peirce Basis of $M_3(\mathbb{C})$](the-peirce-basis-of-m3c.html), for the selection of the units and the gauge.
- [Spinors as Peirce Coordinates in $M_3(\mathbb{C})$](spinors-as-peirce-coordinates-in-m3c.html), for the columns of the array.
