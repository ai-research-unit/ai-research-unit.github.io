# __The Spin Chain and the Adjoint Decomposition of $M_3(\mathbb{C})$__

## Introduction

The algebra $M_{3}(\mathbb{C})$ carries a copy of $\mathfrak{su}_{2}$ inside $\mathfrak{gl}_{3}$, and the defining space $\mathbb{C}^{3}$ is, under this copy, the spin-one module $\operatorname{Sym}^{2}(\mathbb{C}^{2})$. The three standard basis vectors are the three weights $1,0,-1$, the raising operator moves along the chain with the coefficients $\sqrt2,\sqrt2$, and the algebra itself, read as a module for the same $\mathfrak{su}_{2}$, splits into three irreducible summands of dimensions $1,3,5$.

This article states the $\mathfrak{su}_{2}$, proves the commutation relations, identifies the carrier, computes the ladder, and proves the decomposition

$$
M_{3}(\mathbb{C})\cong V_{0}\oplus V_{1}\oplus V_{2}=1+3+5
$$

by exhibiting one highest-weight vector for each summand and checking that their submodules fill the algebra. The trace line is the $1$; the $3$ is isomorphic to the carrier; the $5$ is the spin-two summand. The decomposition of the traceless part, the adjoint of $PGL_{3}$, is $3+5$; the extra $1$ is the trace, which is the centre of $\mathfrak{gl}_{3}$.

**The carrier is not a Peirce line.** The Peirce lines of *The Peirce Decomposition of $M_{3}(\mathbb{C})$* are one-dimensional subspaces of the algebra. The carrier is the three-dimensional minimal left ideal $M_{3}P_{k}\cong\mathbb{C}^{3}$, a module over the algebra. The spin chain runs through the carrier, not through a list of Peirce elements. For $n=3$ the carrier has spin one; only the biquaternion case $n=2$ has a spinorial carrier.

The article assumes the matrix units and the trace of *The Matrix Algebra $M_{3}(\mathbb{C})$*, and the frame of *The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$*. The triplet is developed on its own in *The Triplet: Spin One and the Adjoint $1+3+5$ of $M_3(\mathbb{C})$*.

## The Copy of $\mathfrak{su}_{2}$

**Definition.** Let

$$
J_{3}=\begin{pmatrix}1&0&0\\0&0&0\\0&0&-1\end{pmatrix},
\qquad
J_{+}=\sqrt2\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}=\sqrt2(E_{12}+E_{23}),
$$

$$
J_{-}=\sqrt2\begin{pmatrix}0&0&0\\1&0&0\\0&1&0\end{pmatrix}=\sqrt2(E_{21}+E_{32}).
$$

The indices are $1,2,3$, and the matrix units are those of the standard frame.

**Theorem.** The three matrices satisfy

$$
[J_{3},J_{+}]=J_{+},\qquad [J_{3},J_{-}]=-J_{-},\qquad [J_{+},J_{-}]=2J_{3},
$$

and they span a three-dimensional Lie algebra isomorphic to $\mathfrak{su}_{2}$ over $\mathbb{C}$, equivalently to $\mathfrak{sl}_{2}(\mathbb{C})$.

**Proof.** The first two brackets are read on the matrix units: $[J_{3},E_{12}]=(1-0)E_{12}=E_{12}$ and $[J_{3},E_{23}]=(0-(-1))E_{23}=E_{23}$, so $[J_{3},J_{+}]=J_{+}$; similarly $[J_{3},E_{21}]=-E_{21}$ and $[J_{3},E_{32}]=-E_{32}$, so $[J_{3},J_{-}]=-J_{-}$. For the third,

$$
[J_{+},J_{-}]=2\bigl([E_{12},E_{21}]+[E_{12},E_{32}]+[E_{23},E_{21}]+[E_{23},E_{32}]\bigr).
$$

The four brackets are $E_{11}-E_{22}$, $0$, $0$, $E_{22}-E_{33}$, so the sum is $2(E_{11}-E_{33})=2J_{3}$. The three elements are linearly independent and close under the bracket, and the relations are the standard presentation of $\mathfrak{sl}_{2}$; the real form with $J_{3}$ Hermitian and $J_{+}^{*}=J_{-}$ is $\mathfrak{su}_{2}$.

**The matrices are Hermitian and skew-Hermitian in the right combination.** $J_{3}$ is Hermitian, $J_{+}^{*}=J_{-}$, and $J_{\pm}$ are neither Hermitian nor skew-Hermitian; the real combinations $J_{1}=\tfrac12(J_{+}+J_{-})$ and $J_{2}=\tfrac{1}{2i}(J_{+}-J_{-})$ are Hermitian, and $iJ_{1},iJ_{2},iJ_{3}$ are the skew-Hermitian generators of $\mathfrak{su}_{2}$. The complex span is $\mathfrak{sl}_{2}(\mathbb{C})$.

**The compact form.** The three matrices

$$
iJ_{3},\qquad \tfrac{i}{2}(J_{+}+J_{-}),\qquad \tfrac{1}{2}(J_{+}-J_{-})
$$

are skew-Hermitian, and their brackets are the brackets of $\mathfrak{su}_{2}$ with the conventional normalisation. The article uses the complexified generators $J_{3},J_{\pm}$ because the weights are then integers and the matrices are real.

## The Carrier and the Spin Chain

**The carrier is $\mathbb{C}^{3}$ with the standard basis.** Write $e_{1},e_{2},e_{3}$ for the standard basis, with indices chosen so that

$$
J_{3}e_{1}=e_{1},\qquad J_{3}e_{2}=0,\qquad J_{3}e_{3}=-e_{3}.
$$

**Proposition (the ladder).** The raising and lowering operators act by

$$
J_{+}e_{1}=0,\qquad J_{+}e_{2}=\sqrt2\,e_{1},\qquad J_{+}e_{3}=\sqrt2\,e_{2},
$$

$$
J_{-}e_{1}=\sqrt2\,e_{2},\qquad J_{-}e_{2}=\sqrt2\,e_{3},\qquad J_{-}e_{3}=0.
$$

**Proof.** The matrix $J_{+}=\sqrt2(E_{12}+E_{23})$ sends $e_{2}$ to $\sqrt2e_{1}$ and $e_{3}$ to $\sqrt2e_{2}$, and kills $e_{1}$; the matrix $J_{-}=\sqrt2(E_{21}+E_{32})$ sends $e_{1}$ to $\sqrt2e_{2}$ and $e_{2}$ to $\sqrt2e_{3}$, and kills $e_{3}$.

**The chain.** The vectors are the weights of a spin-one module:

$$
e_{1}=|1,1\rangle,\qquad e_{2}=|1,0\rangle,\qquad e_{3}=|1,-1\rangle,
$$

and the ladder coefficients are

$$
J_{+}|1,0\rangle=\sqrt2\,|1,1\rangle,\qquad
J_{+}|1,-1\rangle=\sqrt2\,|1,0\rangle,
$$

$$
J_{-}|1,1\rangle=\sqrt2\,|1,0\rangle,\qquad
J_{-}|1,0\rangle=\sqrt2\,|1,-1\rangle.
$$

The two coefficients are the same, $\sqrt2$, because the spin is one; the general coefficient is $\sqrt{j(j+1)-m(m\pm1)}$, which at $j=1$ takes the values $\sqrt2$ at both steps. The chain has length three and ends at the highest weight $e_{1}$ and the lowest weight $e_{3}$.

**The identification with $\operatorname{Sym}^{2}(\mathbb{C}^{2})$.** Let $x,y$ be a basis of $\mathbb{C}^{2}$ and put

$$
e_{1}=x^{2},\qquad e_{2}=\sqrt2\,xy,\qquad e_{3}=y^{2}.
$$

Then the operators

$$
J_{3}=\tfrac12(x\partial_{x}-y\partial_{y}),\qquad J_{+}=x\partial_{y},\qquad J_{-}=y\partial_{x}
$$

act by

$$
J_{3}x^{2}=x^{2},\quad J_{3}(\sqrt2xy)=0,\quad J_{3}y^{2}=-y^{2},
$$

$$
J_{+}x^{2}=0,\quad J_{+}(\sqrt2xy)=\sqrt2x^{2},\quad J_{+}y^{2}=2xy=\sqrt2(\sqrt2xy),
$$

$$
J_{-}x^{2}=2xy=\sqrt2(\sqrt2xy),\quad J_{-}(\sqrt2xy)=\sqrt2y^{2},\quad J_{-}y^{2}=0.
$$

So the identification is an isomorphism of $\mathfrak{sl}_{2}$-modules,

$$
\mathbb{C}^{3}\cong\operatorname{Sym}^{2}(\mathbb{C}^{2}),
$$

and the carrier is the **spin-one** module. The factor $\sqrt2$ in $e_{2}$ is exactly what makes the ladder coefficients $\sqrt2$ in both directions; without it the identification would carry the coefficients $2$ and $1$ instead.

**The Peirce chain.** In the standard frame the three Peirce idempotents are $E_{11},E_{22},E_{33}$, and their images are the three lines $\mathbb{C}e_{1},\mathbb{C}e_{2},\mathbb{C}e_{3}$. The weights of the three lines are $1,0,-1$, the same as the weights of the carrier basis. The **spin chain** is the chain of the three image lines, read with the raising operator: $e_{1}\leftarrow e_{2}\leftarrow e_{3}$ under $J_{+}$, with the coefficients $\sqrt2,\sqrt2$. The chain is read on the carrier, not on the idempotents: the adjoint action sends $E_{22}$ to $\sqrt2(E_{12}-E_{23})$, not to $E_{11}$, and only the images of the idempotents in the minimal left ideal form the weight chain. In the standard frame the three image lines are the coordinate lines; in a general frame they are the eigenspaces of $H$, and the raising operator is the same $J_{+}$ transported by the frame.

## The Adjoint Decomposition

**Theorem (the decomposition $1+3+5$).** As a module for the $\mathfrak{su}_{2}$ of §*The Copy of $\mathfrak{su}_{2}$*, the algebra splits as

$$
\boxed{\;M_{3}(\mathbb{C})\cong V_{0}\oplus V_{1}\oplus V_{2},\qquad
\dim V_{0}=1,\quad\dim V_{1}=3,\quad\dim V_{2}=5.\;}
$$

The summand $V_{0}$ is the trace line $\mathbb{C}I$; $V_{1}$ is isomorphic to the carrier $\mathbb{C}^{3}$; $V_{2}$ is the spin-two summand. The traceless part is

$$
\mathfrak{sl}_{3}(\mathbb{C})\cong V_{1}\oplus V_{2}=3+5,
$$

the adjoint of $PGL_{3}(\mathbb{C})$.

**Proof by weight multiplicities.** The operator $\operatorname{ad}_{J_{3}}$ acts on the matrix unit $E_{ij}$ by the difference of the weights:

$$
\operatorname{ad}_{J_{3}}(E_{ij})=(J_{3})_{ii}E_{ij}-E_{ij}(J_{3})_{jj}=(\delta_{i1}-\delta_{i3}-\delta_{j1}+\delta_{j3})E_{ij}.
$$

The weights and their multiplicities are therefore

| Weight $m$ | Matrix units | Multiplicity |
|---|---|---|
| $2$ | $E_{13}$ | $1$ |
| $1$ | $E_{12},E_{23}$ | $2$ |
| $0$ | $E_{11},E_{22},E_{33}$ | $3$ |
| $-1$ | $E_{21},E_{32}$ | $2$ |
| $-2$ | $E_{31}$ | $1$ |

The character of $M_{3}$ is

$$
t^{2}+2t+3+2t^{-1}+t^{-2}.
$$

The irreducible characters of $\mathfrak{sl}_{2}$ of dimensions $5,3,1$ are

$$
\chi_{2}=t^{2}+t+1+t^{-1}+t^{-2},\qquad
\chi_{1}=t+1+t^{-1},\qquad
\chi_{0}=1,
$$

and their sum is exactly the character of $M_{3}$. A finite-dimensional $\mathfrak{sl}_{2}$-module is determined up to isomorphism by its character, so the decomposition, if it exists, is the one displayed, with one summand for each highest weight $0,1,2$.

**Proof by highest-weight vectors.** Existence is exhibited. The three vectors

$$
v_{2}=E_{13},\qquad v_{1}=E_{12}+E_{23},\qquad v_{0}=I
$$

are annihilated by $J_{+}$:

$$
[J_{+},E_{13}]=0,\qquad [J_{+},E_{12}+E_{23}]=0,\qquad [J_{+},I]=0.
$$

The first is the highest-root vector: $E_{13}$ has weight $2$, and the raising operator would give weight $3$, which does not occur. The second has weight $1$; the individual commutators are $[J_{+},E_{12}]=-\sqrt2\,E_{13}$ and $[J_{+},E_{23}]=\sqrt2\,E_{13}$, which cancel in the sum. The third is central.

The submodule generated by $v_{2}$ has the five vectors

$$
u_{2}=E_{13},\qquad
u_{1}=\frac{E_{23}-E_{12}}{\sqrt2},\qquad
u_{0}=\frac{E_{11}-2E_{22}+E_{33}}{\sqrt6},\qquad
u_{-1}=\frac{E_{21}-E_{32}}{\sqrt2},\qquad
u_{-2}=E_{31},
$$

with

$$
J_{-}u_{2}=2u_{1},\quad
J_{-}u_{1}=\sqrt6\,u_{0},\quad
J_{-}u_{0}=\sqrt6\,u_{-1},\quad
J_{-}u_{-1}=2u_{-2},\quad
J_{-}u_{-2}=0,
$$

and the reverse coefficients for $J_{+}$. The vectors are orthonormal for the trace form $\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)$, and they span a five-dimensional irreducible module of highest weight $2$.

The submodule generated by $v_{1}$ has the three vectors

$$
w_{1}=\frac{E_{12}+E_{23}}{\sqrt2},\qquad
w_{0}=\frac{E_{33}-E_{11}}{\sqrt2},\qquad
w_{-1}=-\frac{E_{21}+E_{32}}{\sqrt2},
$$

with

$$
J_{-}w_{1}=\sqrt2\,w_{0},\qquad J_{-}w_{0}=\sqrt2\,w_{-1},\qquad J_{-}w_{-1}=0,
$$

and the reverse coefficients for $J_{+}$. They are orthonormal for the trace form and span a three-dimensional irreducible module of highest weight $1$.

The trace line is spanned by $I/\sqrt3$, of weight $0$, and is one-dimensional. The three submodules are pairwise orthogonal for the trace form and have dimensions $5+3+1=9$, so their sum is the whole algebra. The decomposition is complete.

**The explicit matrices of the $5$.** In the standard matrix units the five vectors are

$$
u_{2}=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix},\qquad
u_{1}=\frac{1}{\sqrt2}\begin{pmatrix}0&-1&0\\0&0&1\\0&0&0\end{pmatrix},\qquad
u_{0}=\frac{1}{\sqrt6}\begin{pmatrix}1&0&0\\0&-2&0\\0&0&1\end{pmatrix},
$$

$$
u_{-1}=\frac{1}{\sqrt2}\begin{pmatrix}0&0&0\\1&0&0\\0&-1&0\end{pmatrix},\qquad
u_{-2}=\begin{pmatrix}0&0&0\\0&0&0\\1&0&0\end{pmatrix}.
$$

The five matrices are traceless; the Cartan element $u_{0}$ is Hermitian, and $u_{-1}=-u_{1}^{*}$, while $u_{2}$ and $u_{-2}$ are adjoint to each other. They are the spin-two multiplet. The three matrices of the $3$ are

$$
w_{1}=\frac{1}{\sqrt2}\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix},\qquad
w_{0}=\frac{1}{\sqrt2}\begin{pmatrix}-1&0&0\\0&0&0\\0&0&1\end{pmatrix},\qquad
w_{-1}=-\frac{1}{\sqrt2}\begin{pmatrix}0&0&0\\1&0&0\\0&1&0\end{pmatrix}.
$$

The trace line is $I/\sqrt3$. The nine matrices

$$
u_{2},u_{1},u_{0},u_{-1},u_{-2},w_{1},w_{0},w_{-1},I/\sqrt3
$$

are an orthonormal basis of $M_{3}(\mathbb{C})$ for the trace form. This is the explicit form of the decomposition $1+3+5$.

**The $3$ is isomorphic to the carrier.** The map

$$
\mathbb{C}^{3}\longrightarrow V_{1},\qquad
e_{1}\longmapsto w_{1},\quad e_{2}\longmapsto w_{0},\quad e_{3}\longmapsto w_{-1},
$$

is an isomorphism of $\mathfrak{sl}_{2}$-modules: it sends the ladder $J_{+}e_{2}=\sqrt2e_{1}$ to $J_{+}w_{0}=\sqrt2w_{1}$, and the other steps likewise. The $3$ of the adjoint is isomorphic to the carrier of the spin chain, and the $5$ is the spin-two module $\operatorname{Sym}^{4}(\mathbb{C}^{2})$. The $1$ is the trace, which the adjoint of $PGL_{3}$ removes.

**The weights on the Peirce chain.** Value the index $1$ as weight $1$, the index $2$ as weight $0$ and the index $3$ as weight $-1$. The standard Peirce line $A_{ij}=\mathbb{C}E_{ij}$ then has weight $w_{i}-w_{j}$, and the nine lines carry the weights

| | $j=1$ $(1)$ | $j=2$ $(0)$ | $j=3$ $(-1)$ |
|---|---|---|---|
| $i=1$ $(1)$ | $0$ | $1$ | $2$ |
| $i=2$ $(0)$ | $-1$ | $0$ | $1$ |
| $i=3$ $(-1)$ | $-2$ | $-1$ | $0$ |

The highest weight is $2$, on $A_{13}$; the weight $1$ occurs twice, on $A_{12}$ and $A_{23}$; the weight $0$ three times, on the diagonal; the weights $-1$ and $-2$ are the opposites. The diagonal chain $A_{11},A_{22},A_{33}$ carries the weights $1,0,-1$, the same as the carrier, and the two lines $A_{12},A_{23}$ of weight $1$ are the highest-weight line of the $3$.

## The Comparison with the Spinorial Case

**For $n=2$ the carrier is two-dimensional and spinorial; for $n=3$ it is three-dimensional and spin one.**

In $M_{2}(\mathbb{C})$, with

$$
J_{3}=\tfrac12\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
J_{+}=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
J_{-}=\begin{pmatrix}0&0\\1&0\end{pmatrix},
$$

the defining space $\mathbb{C}^{2}$ is the spin-$\tfrac12$ module, with weights $\pm\tfrac12$ and ladder coefficient $1$. The algebra itself is

$$
M_{2}(\mathbb{C})\cong V_{0}\oplus V_{1}=1+3,
$$

the trace line and the adjoint $\mathfrak{sl}_{2}$. The biquaternion algebra is $M_{2}(\mathbb{C})$, and its spinor is the two-dimensional carrier; the adjoint is the three-dimensional vector.

In $M_{3}(\mathbb{C})$ the carrier is $\mathbb{C}^{3}=\operatorname{Sym}^{2}(\mathbb{C}^{2})$, the weights are $1,0,-1$, and the ladder coefficients are $\sqrt2,\sqrt2$. The adjoint is $1+3+5$. **There is no half-integer weight in the $M_{3}$ decomposition**: every weight of $\operatorname{ad}_{J_{3}}$ is an integer, and every irreducible summand has odd dimension. The half-integer weights occur only in the two-dimensional carrier of the biquaternion case; this is the precise sense in which the biquaternion algebra is the spinorial case and $M_{3}(\mathbb{C})$ is not.

**The spin is the weight of the Peirce chain.** The highest weight of the carrier is $1$, so the spin is $1$. The highest weight of the $5$ is $2$, so its spin is $2$; the highest weight of the $3$ is $1$, so its spin is $1$; the trace has spin $0$. The three spins $0,1,2$ are the three summands $1,3,5$, and the dimensions are $2j+1$.

## Summary

The algebra $M_{3}(\mathbb{C})$ contains the copy of $\mathfrak{su}_{2}$ generated by

$$
J_{3}=\operatorname{diag}(1,0,-1),\qquad
J_{+}=\sqrt2(E_{12}+E_{23}),\qquad
J_{-}=\sqrt2(E_{21}+E_{32}),
$$

with $[J_{3},J_{\pm}]=\pm J_{\pm}$ and $[J_{+},J_{-}]=2J_{3}$. The carrier is

$$
\mathbb{C}^{3}=\operatorname{Sym}^{2}(\mathbb{C}^{2}),\qquad
e_{1}=x^{2},\quad e_{2}=\sqrt2xy,\quad e_{3}=y^{2},
$$

of spin one, with ladder coefficients $\sqrt2,\sqrt2$. The adjoint decomposition is

$$
\boxed{\;M_{3}(\mathbb{C})=V_{0}\oplus V_{1}\oplus V_{2}=1+3+5,\qquad
\mathfrak{sl}_{3}(\mathbb{C})=3+5.\;}
$$

The $1$ is the trace line, the $3$ is the spin-one summand isomorphic to the carrier, and the $5$ is the spin-two summand. The weights of the algebra are $2,1,0,-1,-2$ with multiplicities $1,2,3,2,1$; there is no half-integer weight. The spinorial case is the biquaternion algebra $M_{2}(\mathbb{C})$, where the carrier is $\mathbb{C}^{2}$ of spin $\tfrac12$.

| Quantity | Value for $M_{3}(\mathbb{C})$ |
|---|---|
| Carrier | $\mathbb{C}^{3}=\operatorname{Sym}^{2}(\mathbb{C}^{2})$ |
| Spin | $1$ |
| Ladder coefficients | $\sqrt2,\sqrt2$ |
| Adjoint of $\mathfrak{gl}_{3}$ | $1+3+5$ |
| Adjoint of $\mathfrak{sl}_{3}$ | $3+5$ |
| Weight multiplicities | $1,2,3,2,1$ |
| Half-integer weights | none |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J_{3}$ | $\operatorname{diag}(1,0,-1)$, the Cartan generator |
| $J_{+},J_{-}$ | the raising and lowering operators, $\sqrt2(E_{12}+E_{23})$, $\sqrt2(E_{21}+E_{32})$ |
| $e_{1},e_{2},e_{3}$ | the carrier basis, weights $1,0,-1$ |
| $V_{j}$ | the irreducible module of spin $j$ and dimension $2j+1$ |
| $u_{m}$ | the orthonormal basis of $V_{2}$, weight $m$ |
| $w_{m}$ | the orthonormal basis of $V_{1}$, weight $m$ |
| $\chi_{j}$ | the character of $V_{j}$ |

## Further Reading

- [The Triplet: Spin One and the Adjoint $1+3+5$ of $M_3(\mathbb{C})$](the-triplet-spin-one-and-the-adjoint-of-m3c.html), for the triplet read on its own.
- [The Peirce Decomposition of $M_3(\mathbb{C})$](the-peirce-decomposition-of-m3c.html), for the Peirce lines and the carrier.
- [The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-m3c.html), for the matrix units.
- [The Matrix Algebra $M_3(\mathbb{C})$](the-matrix-algebra-m3c.html), for the trace and the matrix units.
- [Representations of Lie Algebras](representations-of-lie-algebras.html), for the highest-weight classification used in the proof.
- [The Spin of a Biquaternion](the-spin-of-a-biquaternion.html), for the spinorial case $n=2$.
- [Root Systems and Classification](root-systems-and-classification.html), for the root system $A_{2}$.
- [The Spin Chain and the Adjoint Decomposition of $M_n(\mathbb{C})$](the-spin-chain-and-the-adjoint-decomposition-mnc.html), for the general construction at order $n$.
