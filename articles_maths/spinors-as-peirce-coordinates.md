# __Spinors as Peirce Coordinates__

## Introduction

A spinor is not a column of a matrix, and it is not every irreducible Peirce carrier. It is a coordinate vector on a subspace that one idempotent singles out inside an algebra, **when that subspace carries the spin-$\tfrac12$ weight of the frame root**. The idempotent fixes the subspace, its companion corner supplies the extra coordinate directions, and the diagonal corner supplies the coefficients. This article states that definition in a general finite-dimensional algebra, proves when the subspace is irreducible, identifies the weight condition that makes it a spinor space, and separates the algebraic object from the pictures that a matrix model provides.

The subspace is the **Peirce carrier**

$$
C(e)=Ae=eAe\oplus fAe,
\qquad f=1_A-e,
$$

of an idempotent $e$. The diagonal corner $D=eAe$ is the algebra of coefficients; the companion corner $fAe$ is square-zero and its elements are the companion nilpotents. If $(\nu_1,\dots,\nu_s)$ generates $fAe$ over $D$, every element of $C(e)$ is written

$$
\xi=d_0+\nu_1d_1+\dots+\nu_sd_s,
\qquad d_i\in D,
$$

and the spinor is the list $(d_0;d_1,\dots,d_s)$. The number of entries is $1+s$.

Four results organise the article. First, a spinor is an element of a Peirce carrier that also satisfies a weight condition: the half-root acts with weights $\tfrac12$ and $-\tfrac12$, each once. Second, semisimplicity of the algebra is exactly what makes the carrier irreducible: in a semisimple algebra a primitive idempotent gives an irreducible carrier, while the upper triangular algebra $T_2$ has a primitive idempotent with a reducible carrier. Third, the weight condition is restrictive: in $M_N(k)$ with the standard frame it holds only for $N=2$, so the column of $M_N$ is a spinor space only in the biquaternion case; for $N>2$ the column is the spin-$(N-1)/2$ carrier of the Peirce chain. Fourth, the column of a matrix model is one picture of the carrier, not its definition, and the number of coordinates $1+s$ is not the spin.

**Setting.** Throughout, $k$ is a field, $A$ is a finite-dimensional unital associative $k$-algebra with $1_A\neq0$, and $e\in A$ is an idempotent with $f=1_A-e$. The corners and the companion count are those of *Peirce Coordinates and Companion Nilpotents*: $A_{st}=e_sAe_t$, $D=A_{++}=eAe$, and $s$ is the least number of generators of $A_{-+}=fAe$ over $D$. The primitive idempotents are those of *Primitive Idempotents and Minimal Left Ideals*; the module-theoretic comparison, used only for the theorem below, is *Modules over an Algebra* and *Simple and Semisimple Modules*. No form, no involution, no matrix model and no module theory is used in the definition.

## The Carrier

**Definition.** The **Peirce carrier** of $e$ is $C(e)=Ae=\{\,x\in A:xe=x\,\}$. Its **diagonal part** is $D=eAe$ and its **companion part** is $fAe$.

**Proposition.** $C(e)=D\oplus fAe$, and left multiplication by any $a\in A$ maps $C(e)$ into itself.

*Proof.* This is *Peirce Coordinates and Companion Nilpotents*, §*The Carrier and Its Coordinates*: the Peirce expansion of $x\in Ae$ has only the corners with right index $+$, and $(ax)e=a(xe)=ax$.

**Definition.** A **companion frame** of $e$ is a family $(\nu_1,\dots,\nu_s)$ of elements of $fAe$ that generates $fAe$ over $D$ with $s$ minimal. The **coordinate vector** of $\xi\in C(e)$ is the list $(d_0;d_1,\dots,d_s)$ of the expansion above; it is unique when the companion family is a $D$-basis.

**Proposition.** If $D$ is a division ring, then $fAe$ is free over $D$, the companion frame is a basis, and $C(e)\cong D^{1+s}$.

*Proof.* Every module over a division ring is free. The expansion is unique by the direct sum $D\oplus fAe$.

**Example (the biquaternion).** For $A=\mathbb{B}$, $e=\tilde\Pi_+$, $f=\tilde\Pi_-$, one has $D=\mathbb{C}\tilde\Pi_+\cong\mathbb{C}$, $s=1$, and

$$
C(\tilde\Pi_+)=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_y\cong\mathbb{C}^2 .
$$

The two coordinates are the coefficient of the idempotent and the coefficient of the companion nilpotent. The other idempotent gives $C(\tilde\Pi_-)=\mathbb{C}\vec\Upsilon_x\oplus\mathbb{C}\tilde\Pi_-$, a second carrier with the same structure. The two are different subspaces of the algebra and the same two-dimensional complex space up to isomorphism.

## The Definition of a Spinor

**Definition.** Let $e$ be an idempotent with $h=2e-1_A$, and let $C(e)=Ae$ be its Peirce carrier. A **spinor** of the frame $e$ is an element of $C(e)$ when the half-root $\tfrac12h$ acts on $C(e)$ by left multiplication with the weight string

$$
\tfrac12,\ -\tfrac12,
$$

each weight occurring once over $D=eAe$; that is, $C(e)=L_+\oplus L_-$ with $hx=\pm x$ for $x\in L_\pm$. A **spinor frame** is the pair of $e$ and a companion frame $(\nu_1,\dots,\nu_s)$; in that frame the spinor is its coordinate vector $(d_0;d_1,\dots,d_s)\in D^{1+s}$.

When the weight condition fails, $C(e)$ is a **Peirce carrier** and its coordinate vector is a Peirce coordinate, not a spinor. The definition has four ingredients: an idempotent, the subspace it fixes on the right, the companion corner that completes it, and the weight condition on the half-root. The last condition supplies the spin-$\tfrac12$ structure; irreducibility alone does not.

**Theorem (the matrix case).** Let $A=M_N(k)$ and $e=E_{11}$. Then $C(e)$ is a spinor space exactly when $N=2$.

*Proof.* The carrier is the first column, $C(e)=\operatorname{span}\{E_{11},\dots,E_{N1}\}$, and $h=2E_{11}-I_N$ acts by $hE_{11}=E_{11}$ and $hE_{k1}=-E_{k1}$ for $k\ge2$. The half-root therefore has the weight $+\tfrac12$ once and $-\tfrac12$ with multiplicity $N-1$. The weight string is $(+\tfrac12,-\tfrac12)$ exactly when $N=2$.

**Corollary.** In a semisimple algebra with a primitive idempotent of a simple component $M_N(D)$, the carrier is a spinor space exactly when $N=2$. The biquaternion is the case $N=2$, $D=\mathbb{C}$.

**Remark (why the whole carrier, not one corner).** The diagonal corner $D$ alone is not the spinor space. In $M_2(k)$ with $e=E_{11}$, $D=kE_{11}$ is a single coefficient, and the spinor also needs the companion direction $E_{21}$; without it there is no second coordinate. The companion corner alone is not the spinor space either: its elements are nilpotents, and a nilpotent is a direction, not a state. The spinor is an element of their sum, with one diagonal coordinate and $s$ companion coordinates.

**Remark (coordinates over $D$, not over $k$).** The entries of the coordinate vector are elements of $D=eAe$, not scalars. When $D$ is a division ring, this is a vector of $1+s$ entries over a division ring, and $1+s$ is its dimension over $D$. When $D$ is a matrix algebra, an entry is itself a matrix; the coordinate vector is a block vector, and $1+s$ counts blocks, not scalars.

## Irreducibility

**Proposition.** If $C(e)$ is irreducible under left multiplication, then $e$ is primitive and $D=eAe$ is a division ring.

*Proof.* If $e=e_1+e_2$ with $e_1,e_2$ nonzero orthogonal idempotents, then $Ae=Ae_1\oplus Ae_2$ is a nontrivial decomposition into left-invariant subspaces, against irreducibility. An $A$-endomorphism $\varphi$ of $Ae$ satisfies $\varphi(x)=\varphi(xe)=x\varphi(e)$, with $\varphi(e)\in Ae$ and $e\varphi(e)=\varphi(e)e=\varphi(e)$, so $\varphi$ is the right multiplication by an element of $D=eAe$; conversely every such right multiplication is $A$-linear. Hence $\operatorname{End}_A(C(e))\cong D^{\mathrm{opp}}$, and the endomorphism ring of an irreducible module is a division ring by Schur's lemma. So $D$ is a division ring.

**Theorem.** Let $A$ be semisimple and $e$ primitive. Then $C(e)$ is irreducible under left multiplication.

*Proof.* In a semisimple algebra the primitive idempotent $e$ has $D=eAe$ a division ring and $Ae$ a simple left module; this is the equivalence proved in *Primitive Idempotents and Minimal Left Ideals*, §*The equivalence*, and the simplicity is exactly the absence of a proper nonzero left-invariant subspace.

**Example (the theorem fails without semisimplicity).** Let $A=T_2(k)$ be the upper triangular algebra and $e=E_{22}$. Then $e$ is primitive and $D=eAe=kE_{22}$ is a division ring, but

$$
C(e)=kE_{12}\oplus kE_{22},
$$

and $kE_{12}$ is a proper left-invariant subspace: $E_{11}E_{12}=E_{12}$, $E_{22}E_{12}=0$ and $E_{12}^2=0$. So $C(e)$ is reducible. Primitiveness and a division corner do not suffice; semisimplicity is the missing hypothesis.

**Example (the dual numbers).** In $A=k[\varepsilon]$, the identity $e=1_A$ is primitive, $D=A$ is not a division ring, and $C(e)=A$ contains the invariant subspace $k\varepsilon$. The carrier is reducible. The companion corner is zero, so the reducibility is entirely in the diagonal part.

**Corollary.** In a semisimple algebra, the idempotents whose carriers are irreducible are exactly the primitive idempotents. The spinor carriers are the further subset selected by the weight condition: the primitive idempotents of a simple component $M_N(D)$ with $N=2$.

## What the Definition Is Not

**It is not a corner.** The space $A_{++}$ is the coefficient algebra, and a general element of it is a matrix of labels. The spinor uses $A_{++}$ for its first coordinate and $A_{-+}$ for the rest; neither corner alone is the carrier.

**It is not a column.** A column appears when the algebra is written as $M_N(k)$ and the carrier is read on the first column of the matrix. That picture requires a basis of $A$ and the identification $A\cong M_N(k)$; it is not available in a general algebra. The column is the image of $C(e)$ under one model, not the object.

**It is not defined by minimality.** The carrier is defined by the idempotent before any minimality is mentioned. The closure of $C(e)$ under left multiplication is a consequence of the product rule, and its minimality is a theorem about semisimple algebras, proved in *Primitive Idempotents and Minimal Left Ideals*. The order is: idempotent, carrier, coordinates, weight. Irreducibility is a theorem about the carrier; it is not the spinor condition, and the irreducible carrier of $M_3$ with $e=E_{11}$ is the counterexample.

**The number of coordinates is not the spin.** A carrier of dimension $N$ over $k$ is not a spin-$N$ object. The spin is a weight of a frame root on the carrier, and it requires an $\mathfrak{sl}_2$ triple that the idempotent alone does not supply; the weight condition above is the part of that triple that the half-root supplies. That is the subject of *The Weight of a Frame Root and the Spin Quantum Number*.

## Examples

| algebra | idempotent | $D$ | $s$ | carrier | irreducible? | spinor? |
|---|---|---|---|---|---|---|
| $\mathbb{B}=M_2(\mathbb{C})$ | $\tilde\Pi_+$ | $\mathbb{C}$ | $1$ | $\mathbb{C}^2$ | yes | yes |
| $M_2(k)$ | $E_{11}$ | $k$ | $1$ | $k^2$ | yes | yes |
| $M_3(k)$ | $E_{11}$ | $k$ | $2$ | $k^3$ | yes | no |
| $M_N(k)$ | $E_{11}$ | $k$ | $N-1$ | $k^N$ | yes | no, $N>2$ |
| $M_N(k)$ | $E_{11}+E_{22}$, $N\ge3$ | $M_2(k)$ | $\lceil N/2\rceil-1$ | two-column block | no | no |
| $\mathbb{H}$ | $1_A$ | $\mathbb{H}$ | $0$ | $\mathbb{H}$ | yes | no |
| $T_2(k)$ | $E_{11}$ | $k$ | $0$ | $k$ | yes | no |
| $T_2(k)$ | $E_{22}$ | $k$ | $1$ | $k^2$ | no | no |
| $k[\varepsilon]$ | $1_A$ | $k[\varepsilon]$ | $0$ | $k[\varepsilon]$ | no | no |

The matrix algebra with a primitive idempotent is the model case: $C(e)$ is the first column, of dimension $N$ over $k$, and the companion frame is $E_{21},\dots,E_{N1}$. The biquaternion is the only matrix case in which the column is a spinor space: $N=2$, the column has two entries, and the half-root has weights $\pm\tfrac12$. For $N>2$ the column is the carrier of the spin-$(N-1)/2$ Peirce chain, so its $N$ entries are Peirce coordinates, not spinor coordinates. The quaternions are the case $s=0$: the carrier is the algebra itself, of dimension one over $\mathbb{H}$, and the half-root has the single weight $+\tfrac12$, so the carrier is not a spinor space.

**The Clifford case.** For the complex Clifford algebra the structure depends on the parity of $N$. For $N=2m$ even,

$$
\mathrm{Cl}_{2m}(\mathbb{C})\cong M_{2^m}(\mathbb{C}),
$$

with one simple component and a primitive idempotent of $D\cong\mathbb{C}$, $s=2^m-1$, and carrier dimension $2^m$. For $N=2m+1$ odd,

$$
\mathrm{Cl}_{2m+1}(\mathbb{C})\cong M_{2^m}(\mathbb{C})\oplus M_{2^m}(\mathbb{C}),
$$

with two simple components, the two chiralities; a primitive idempotent of either component has $D\cong\mathbb{C}$, $s=2^m-1$, and carrier dimension $2^m$. In both cases the number of companion nilpotents and the number of spinor coordinates are the same datum:

| $N$ | Clifford algebra | $m$ | $s$ | spinor dimension |
|---|---|---|---|---|
| $2$ | $M_2(\mathbb{C})$ | $1$ | $1$ | $2$ |
| $3$ | $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ | $1$ | $1$ | $2$ |
| $4$ | $M_4(\mathbb{C})$ | $2$ | $3$ | $4$ |
| $5$ | $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$ | $2$ | $3$ | $4$ |
| $6$ | $M_8(\mathbb{C})$ | $3$ | $7$ | $8$ |
| $8$ | $M_{16}(\mathbb{C})$ | $4$ | $15$ | $16$ |

**The Clifford reading.** In this table "spinor dimension" is the dimension of the Clifford module carried by the Peirce ideal, not a claim that the half-root alone supplies the weights $\pm\tfrac12$. The Clifford spin structure is the action of the bivectors. At $N=2$ the Peirce root and the Clifford vector agree, and the two-dimensional ideal is the spin-$\tfrac12$ module. At $N=4$ the four-dimensional ideal is the Dirac module; under the volume element it splits into two two-dimensional half-spin modules of spin $\tfrac12$. The Peirce carrier is the module; the bivector action is what makes it a spinor representation.

## Summary

A spinor is an element of the Peirce carrier $C(e)=Ae=eAe\oplus fAe$ of an idempotent $e$ when the half-root $\tfrac12h$, with $h=2e-1_A$, acts on $C(e)$ by left multiplication with the weights $+\tfrac12$ and $-\tfrac12$, each once over $D$. In coordinates over $D=eAe$ it is the vector $(d_0;d_1,\dots,d_s)$ with one diagonal entry and one entry for each of the $s$ companion directions. The definition uses an idempotent, a subspace, a square-zero corner and the weight condition; it does not use a matrix model or a column.

In a semisimple algebra the primitive idempotents are exactly the idempotents with irreducible carriers, and $D$ is a division ring, so the carrier is $D^{1+s}$. Without semisimplicity the equivalence fails: the upper triangular algebra has a primitive idempotent with a reducible carrier. Irreducibility is not the spinor condition; the weight string is. In $M_N(k)$ with a primitive idempotent, $s=N-1$ and the carrier has $N$ coordinates. The weight condition holds only for $N=2$, so the biquaternion is the only matrix case in which those coordinates are spinor coordinates; for $N>2$ the carrier is the spin-$(N-1)/2$ module and the coordinates are Peirce coordinates.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | A field |
| $A$ | A finite-dimensional unital associative $k$-algebra |
| $e$ | An idempotent, $e^2=e$ |
| $f$ | The complement $1_A-e$ |
| $h=2e-1_A$ | The frame root |
| $D=eAe$ | The diagonal corner, the coefficient algebra |
| $fAe$ | The companion corner, square-zero |
| $s$ | The least number of generators of $fAe$ over $D$ |
| $C(e)=Ae$ | The Peirce carrier |
| $(\nu_1,\dots,\nu_s)$ | A companion frame |
| $(d_0;d_1,\dots,d_s)$ | The coordinates of a spinor |
| $\tfrac12h$ with weights $\pm\tfrac12$ | The condition that makes $C(e)$ a spinor space |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the corner algebras.
- Yurij A. Drozd and Vladimir V. Kirichenko, *Finite Dimensional Algebras* (Springer, 1994), for primitive idempotents and the local corners.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for the module-theoretic reading of the carrier.
- The corpus articles *Peirce Coordinates and Companion Nilpotents*, for the coordinate theory, and *The Weight of a Frame Root and the Spin Quantum Number*, for the passage from the carrier to the spin.
