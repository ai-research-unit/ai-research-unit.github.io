# __The Modules and the Minimal Left Ideals of $M_3(\mathbb{C})$__

## Introduction

The algebra $M_{3}(\mathbb{C})$ acts on $\mathbb{C}^{3}$ by matrix multiplication. The action is the defining representation, and the space $\mathbb{C}^{3}$ is the **carrier** of the spin chain. The same representation can be read as a minimal left ideal of the algebra: the column space
$$
M_{3}P_{1}=\{AP_{1}:A\in M_{3}\},\qquad P_{1}=E_{11},
$$
is a left $M_{3}$-module isomorphic to $\mathbb{C}^{3}$. Its dual is the minimal right ideal $P_{1}M_{3}$, the row space, and the algebra itself is the tensor product of the two:
$$
M_{3}(\mathbb{C})\cong\mathbb{C}^{3}\otimes(\mathbb{C}^{3})^{*}.
$$
The article proves these statements, describes the Peirce carrier
$$
C(P)=PMP\oplus PMQ
$$
of a rank-one idempotent $P$, and identifies the module that carries the spin chain.

The article is the module-theoretic companion of *The Peirce Decomposition of $M_{3}(\mathbb{C})$* and *The Triplet: Spin One and the Adjoint $1+3+5$ of $M_3(\mathbb{C})$*. The Peirce decomposition is a decomposition of the algebra into lines; the present article is about the modules over the algebra, which are different objects. In particular, a minimal left ideal is a three-dimensional module, not a one-dimensional Peirce line, and it is not a spinor. For $n=3$ the carrier is the spin-one module $\mathbb{C}^{3}=\operatorname{Sym}^{2}(\mathbb{C}^{2})$; only the case $n=2$ has a two-dimensional spinorial module. The distinction is stated once here and used throughout the category.

The construction is root-first. The idempotents $P_{1},P_{2},P_{3}$ are those of *Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$*; the frame $E_{ij}$ and the gauge are those of *The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$* and *The Two-Parameter Gauge of $M_3(\mathbb{C})$*.

## The Minimal Left Ideal

**Definition.** For the idempotent $P_{1}=E_{11}$, the **minimal left ideal** is
$$
M_{3}P_{1}=\{AP_{1}:A\in M_{3}(\mathbb{C})\}.
$$

**Proposition.** $M_{3}P_{1}$ is a left ideal of dimension three. As a left $M_{3}$-module it is simple, and it is isomorphic to $\mathbb{C}^{3}$ with the defining action.

**Proof.** For $A,B\in M_{3}$, $(AB)P_{1}=A(BP_{1})\in M_{3}P_{1}$, so it is a left ideal. The product $AP_{1}$ is the matrix whose first column is the first column of $A$ and whose other columns are zero; the map $A\mapsto AP_{1}$ therefore has image the space of matrices with only the first column nonzero, of dimension three, with basis
$$
E_{11},E_{21},E_{31}.
$$
The left action on this space is the action on the first column: if $v=(v_{1},v_{2},v_{3})^{\mathsf T}$ is the first column, then
$$
A\left(\sum_{i}v_{i}E_{i1}\right)=\sum_{i}(Av)_{i}E_{i1}.
$$
So $M_{3}P_{1}\cong\mathbb{C}^{3}$ as a left module.

For simplicity, let $x=\sum_{i}v_{i}E_{i1}\neq0$. Some $v_{i}\neq0$. Then
$$
E_{1i}x=v_{i}E_{11},
$$
so $E_{11}=(1/v_{i})E_{1i}x\in M_{3}x$. Hence $M_{3}P_{1}=M_{3}E_{11}\subseteq M_{3}x$, and the reverse inclusion is clear; every nonzero element generates the whole module. So the module is simple.

**The annihilator.** The annihilator of $P_{1}$ is
$$
\operatorname{Ann}(P_{1})=\{A:AP_{1}=0\}=\{A:\text{the first column of }A\text{ is zero}\},
$$
of dimension six. The quotient $M_{3}/\operatorname{Ann}(P_{1})$ is the column space, of dimension three, and it is the simple module.

**The endomorphism algebra.** Every $M_{3}$-linear endomorphism of $M_{3}P_{1}$ is right multiplication by an element of $P_{1}M_{3}P_{1}=\mathbb{C}P_{1}$, so
$$
\operatorname{End}_{M_{3}}(M_{3}P_{1})\cong\mathbb{C}.
$$
This is Schur's lemma for the simple module: the endomorphism algebra is a division algebra over $\mathbb{C}$, hence $\mathbb{C}$ itself.

**The explicit column.** A vector $v=(1,2,3)^{\mathsf T}$ corresponds to the matrix
$$
V=\sum_{i=1}^{3}v_{i}E_{i1}
=\begin{pmatrix}1&0&0\\2&0&0\\3&0&0\end{pmatrix}.
$$
The left action of $A$ is the matrix product $AV$, whose first column is $Av$ and whose other columns are zero. The module is the column, and the matrix $V$ is the column written as a matrix with the other columns zero.

## The Right Ideal and the Dual

**Definition.** The **minimal right ideal** is
$$
P_{1}M_{3}=\{P_{1}A:A\in M_{3}(\mathbb{C})\}.
$$

**Proposition.** $P_{1}M_{3}$ is a right ideal of dimension three, with basis
$$
E_{11},E_{12},E_{13}.
$$
It is the row space: $P_{1}A$ is the matrix whose first row is the first row of $A$ and whose other rows are zero. As a right $M_{3}$-module it is simple, and it is the dual of the left module $M_{3}P_{1}$.

**Proof.** The right ideal property is $(P_{1}A)B=P_{1}(AB)\in P_{1}M_{3}$. The product $P_{1}A$ has only the first row nonzero, and the basis is $E_{11},E_{12},E_{13}$. The pairing
$$
M_{3}P_{1}\times P_{1}M_{3}\longrightarrow\mathbb{C},\qquad (x,y)\longmapsto\operatorname{tr}(xy),
$$
is nondegenerate: for $x=\sum_{i}v_{i}E_{i1}$ and $y=\sum_{j}w_{j}E_{1j}$,
$$
xy=\sum_{i,j}v_{i}w_{j}E_{ij},\qquad \operatorname{tr}(xy)=\sum_{i}v_{i}w_{i},
$$
which is the standard dot product of the column $v$ and the row $w$. The pairing is left-linear in $x$ and right-linear in $y$, and it identifies $P_{1}M_{3}$ with the dual of $M_{3}P_{1}$.

**The row as a functional.** A row $w=(w_{1},w_{2},w_{3})$ is the linear functional $v\mapsto\sum_{i}w_{i}v_{i}$ on the column. The right action of $A$ on the row is the dual action: $(wA)(v)=w(Av)$. The row module is the contragredient representation of the column module. For $\mathfrak{sl}_{2}$ the spin-one module is self-dual, so the row and the column are isomorphic as modules; the isomorphism is not canonical.

**The transpose.** The transpose identifies the column with the row:
$$
(M_{3}P_{1})^{\mathsf T}=P_{1}M_{3},\qquad \left(\sum_{i}v_{i}E_{i1}\right)^{\mathsf T}=\sum_{i}v_{i}E_{1i}.
$$
The transpose is an isomorphism of vector spaces, but it reverses the multiplication: $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$. It is not an isomorphism of left modules unless the algebra is commutative. The duality is the correct module statement; the transpose is a convenient coordinate identification.

## The Tensor Product

**Theorem.**
$$
M_{3}(\mathbb{C})\cong\mathbb{C}^{3}\otimes(\mathbb{C}^{3})^{*}
$$
as a bimodule, with
$$
E_{ij}\longleftrightarrow e_{i}\otimes e_{j}^{*},
$$
where $e_{1},e_{2},e_{3}$ is the standard basis of the column and $e_{1}^{*},e_{2}^{*},e_{3}^{*}$ is the dual basis of the row.

**Proof.** The nine elementary tensors $e_{i}\otimes e_{j}^{*}$ are a basis of the tensor product, which has dimension $3\cdot3=9$; the map sends them to the nine matrix units, which are a basis of $M_{3}$. The product is
$$
(e_{i}\otimes e_{j}^{*})(e_{k}\otimes e_{l}^{*})
=\delta_{jk}\,e_{i}\otimes e_{l}^{*},
$$
which is the matrix-unit product $E_{ij}E_{kl}=\delta_{jk}E_{il}$. The left action of $M_{3}$ is on the first factor, and the right action is on the second; the two actions commute, and the tensor product is the bimodule of endomorphisms of the column.

**The trace and the identity.** Under the isomorphism,
$$
I=\sum_{i}e_{i}\otimes e_{i}^{*},\qquad
\operatorname{tr}(e_{i}\otimes e_{j}^{*})=\delta_{ij}.
$$
The trace is the contraction of the two factors; the identity is the invariant tensor of the pair of dual spaces. The determinant is the top exterior power; the algebra is the full endomorphism algebra of a three-dimensional space.

**The Peirce decomposition in the tensor picture.** The idempotent $P_{k}=E_{kk}$ is $e_{k}\otimes e_{k}^{*}$, the projection onto the $k$-th line. The Peirce line $A_{kl}=\mathbb{C}E_{kl}$ is the line $\mathbb{C}e_{k}\otimes e_{l}^{*}$, of dimension one. The left ideal $M_{3}P_{k}$ is $\mathbb{C}^{3}\otimes e_{k}^{*}$, a copy of the column; the right ideal $P_{k}M_{3}$ is $e_{k}\otimes(\mathbb{C}^{3})^{*}$, a copy of the row. The nine Peirce lines are the nine lines of the tensor product, not nine modules.

## The Minimal Left Ideals and the Non-Canonical Exchange

**The three minimal left ideals.** For $k=1,2,3$ the space
$$
M_{3}P_{k}=\{AP_{k}:A\in M_{3}\}
$$
is a minimal left ideal, isomorphic to $\mathbb{C}^{3}$. The isomorphism is the projection onto the $k$-th column:
$$
M_{3}P_{k}\longrightarrow\mathbb{C}^{3},\qquad \sum_{i}v_{i}E_{ik}\longmapsto (v_{1},v_{2},v_{3})^{\mathsf T}.
$$
The three modules are isomorphic, but the isomorphisms depend on the choice of the column; there is no canonical identification of the $k$-th column with the $l$-th column.

**The exchange.** For $k\neq l$, right multiplication by $E_{kl}$ maps $M_{3}P_{k}$ to $M_{3}P_{l}$:
$$
xE_{kl}\in M_{3}P_{k}E_{kl}=M_{3}P_{l},
$$
because $P_{k}E_{kl}=E_{kl}=E_{kl}P_{l}$. The inverse is right multiplication by $E_{lk}$:
$$
xE_{kl}E_{lk}=xP_{k}=x.
$$
So $E_{kl}$ gives an isomorphism of left modules
$$
M_{3}P_{k}\longrightarrow M_{3}P_{l},\qquad x\longmapsto xE_{kl}.
$$

**The exchange is not canonical.** The matrix unit $E_{kl}$ is determined only up to the gauge
$$
E_{kl}\longmapsto \frac{t_{k}}{t_{l}}E_{kl},
$$
as in *The Two-Parameter Gauge of $M_3(\mathbb{C})$*. The isomorphism is multiplied by the scalar $t_{k}/t_{l}$, so the set of isomorphisms $M_{3}P_{k}\to M_{3}P_{l}$ is a torsor under $\mathbb{C}^{\times}$. The choice of an isomorphism is a choice of normalized frame, not a canonical structure of the algebra. The three minimal left ideals are isomorphic, but not canonically isomorphic.

**The general minimal left ideal.** Every minimal left ideal of $M_{3}$ is of the form $M_{3}Q$ for a rank-one idempotent $Q$. Every rank-one idempotent is conjugate to $P_{1}$: if $Q$ has image the line $\mathbb{C}v$ and kernel a plane, choose $g\in GL_{3}$ with $g e_{1}=v$ and $g$ mapping the standard plane to the kernel; then $Q=gP_{1}g^{-1}$. The map
$$
M_{3}P_{1}\longrightarrow M_{3}Q,\qquad x\longmapsto xg
$$
is an isomorphism of left modules, with inverse $y\mapsto yg^{-1}$. The choice of $g$ is a choice of basis adapted to $Q$; different choices differ by the stabilizer of $P_{1}$, the diagonal torus, and the isomorphism is again non-canonical.

## The Peirce Carrier

**Definition.** Let $P$ be a rank-one idempotent and $Q=I-P$. The **Peirce carrier** is
$$
C(P)=PMP\oplus PMQ.
$$

**Proposition.** $\dim_{\mathbb{C}}C(P)=1+2=3$, and $C(P)=PM_{3}$ is the minimal right ideal generated by $P$. Its dual is the minimal left ideal $M_{3}P=PMP\oplus QMP$, also of dimension $1+2=3$. The two are isomorphic as vector spaces and dual as modules.

**Proof.** The corner $PMP$ is one-dimensional, because $P$ has rank one; the corner $PMQ$ is two-dimensional, because $Q$ has rank two and $P$ has rank one. Their sum is $PM(P+Q)=PM$, the right ideal generated by $P$. The left ideal $M_{3}P=(P+Q)MP=PMP\oplus QMP$ has the same dimensions, $1+2$. The pairing
$$
M_{3}P\times PM_{3}\longrightarrow\mathbb{C},\qquad (x,y)\longmapsto\operatorname{tr}(xy),
$$
is nondegenerate, so the right carrier is the dual of the left carrier.

**The Peirce coordinates of the carrier.** For $P=P_{1}$, the carrier $P_{1}M_{3}$ is the row space, with basis $E_{11},E_{12},E_{13}$: one diagonal coordinate and two mixed coordinates. The left carrier $M_{3}P_{1}$ is the column space, with basis $E_{11},E_{21},E_{31}$: one diagonal coordinate and two mixed coordinates. The scalar coordinate is the $PMP$ line; the two mixed coordinates are the $PMQ$ or $QMP$ plane. The carrier is the module, not the Peirce line: the line is one-dimensional, the carrier is three-dimensional.

**The carrier of a rank-one idempotent is the simple module.** For every rank-one $P$, $C(P)=PM_{3}\cong\mathbb{C}^{3}$ as a right module, and $M_{3}P\cong\mathbb{C}^{3}$ as a left module. The isomorphism depends on $P$ and on the frame; the dimension and the module structure do not. The Peirce carrier of the menu is the right module $PM_{3}$; the left module $M_{3}P$ is its dual. The spin chain of the next section is carried by the left module $M_{3}P_{1}$; the right module gives the same representation up to the duality, which is an isomorphism for the spin-one module.

**The rank-two case.** For a rank-two idempotent $P$, the corner $PMP$ has dimension four and $PMQ$ has dimension two, so $PM_{3}$ has dimension six; it is not a minimal ideal. The minimal left ideals are the modules $M_{3}P_{k}$ of the rank-one idempotents, of dimension three. The rank-two carrier is the direct sum of two minimal modules, not a simple module.

## The Module as the Carrier of the Spin Chain

**The module.** The left module $M_{3}P_{1}\cong\mathbb{C}^{3}$ is the carrier of the defining representation. The principal $\mathfrak{sl}_{2}$ of *The Spin Chain and the Adjoint Decomposition of $M_3(\mathbb{C})$* acts on it by left multiplication:
$$
A\cdot v=Av,\qquad A\in\mathfrak{sl}_{2},\quad v\in\mathbb{C}^{3}.
$$
With the standard basis $e_{1},e_{2},e_{3}$ and the operators
$$
J_{3}=\operatorname{diag}(1,0,-1),\qquad J_{+}=\sqrt2(E_{12}+E_{23}),\qquad J_{-}=\sqrt2(E_{21}+E_{32}),
$$
the module has weights $1,0,-1$ and ladder coefficients $\sqrt2$:
$$
J_{+}e_{2}=\sqrt2 e_{1},\quad J_{+}e_{3}=\sqrt2 e_{2},\quad
J_{-}e_{1}=\sqrt2 e_{2},\quad J_{-}e_{2}=\sqrt2 e_{3}.
$$
It is the spin-one module $\operatorname{Sym}^{2}(\mathbb{C}^{2})$, of dimension $3=2\cdot1+1$.

**The identification with the symmetric square.** Let $x,y$ be a basis of $\mathbb{C}^{2}$ and put
$$
e_{1}=x^{2},\qquad e_{2}=\sqrt2\,xy,\qquad e_{3}=y^{2}.
$$
Then $J_{3}=\tfrac12(x\partial_{x}-y\partial_{y})$, $J_{+}=x\partial_{y}$, $J_{-}=y\partial_{x}$, and the actions above are the actions on the symmetric square. The carrier is the spin-one module; it is not a spinor.

**The Peirce carrier and the spin chain.** The left carrier $M_{3}P_{1}$ is the column; the right carrier $P_{1}M_{3}$ is the row. The spin chain can be read on either, because the spin-one module is self-dual. The right module carries the contragredient action, whose weights are the negatives; the two readings are isomorphic because the spin-one representation is self-dual, but the isomorphism is not the transpose: the transpose reverses the multiplication, $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$, and is not an intertwiner of the two actions. The isomorphism is the duality pairing, and it is not canonical. The article uses the left module for the spin chain and the right module for the Peirce carrier, and states the duality rather than identifying them canonically.

**No spinors for $n=3$.** The carrier is three-dimensional and carries spin one. A spinor would be a two-dimensional module, and $M_{3}(\mathbb{C})$ has no two-dimensional simple module: its simple module is $\mathbb{C}^{3}$, of dimension three. The two-dimensional spinorial module exists only for $M_{2}(\mathbb{C})$, where the minimal left ideal is $\mathbb{C}^{2}$ and the Peirce decomposition has four lines. For $n=3$ the Peirce lines are one-dimensional subspaces of the algebra, the minimal left ideal is a three-dimensional module, and neither is a spinor. The word **spinor** is reserved for the $n=2$ case; the carrier of the $n=3$ spin chain is the spin-one module.

**The Peirce line is not a module.** The Peirce line $A_{kl}=\mathbb{C}E_{kl}$ is a one-dimensional subspace of the algebra. It is not closed under the left action of $M_{3}$: $E_{21}E_{11}=E_{21}$ and $E_{31}E_{11}=E_{31}$, so the left action sends the line $A_{11}$ into $A_{21}$ and $A_{31}$; the left ideal it generates is the whole first column $M_{3}E_{11}$, of dimension three, not the line. The line is a Peirce summand of the algebra, not a submodule of the defining representation. The confusion between a Peirce line and a spinor is the confusion between a one-dimensional subspace of the algebra and a minimal module; the two have different dimensions and different actions.

## Summary

The minimal left ideal is
$$
\boxed{\;M_{3}P_{1}=\{AP_{1}:A\in M_{3}\}\cong\mathbb{C}^{3},\qquad \dim_{\mathbb{C}}=3,\;}
$$
the column space, with basis $E_{11},E_{21},E_{31}$. It is simple as a left module. Its dual is the minimal right ideal
$$
P_{1}M_{3}=\{P_{1}A:A\in M_{3}\}\cong(\mathbb{C}^{3})^{*},
$$
the row space, with basis $E_{11},E_{12},E_{13}$; the pairing is $(x,y)\mapsto\operatorname{tr}(xy)$.

The algebra is the tensor product
$$
\boxed{\;M_{3}(\mathbb{C})\cong\mathbb{C}^{3}\otimes(\mathbb{C}^{3})^{*},\qquad E_{ij}\leftrightarrow e_{i}\otimes e_{j}^{*}.\;}
$$
The Peirce line $A_{kl}$ is the line $\mathbb{C}e_{k}\otimes e_{l}^{*}$; the left ideal $M_{3}P_{k}$ is $\mathbb{C}^{3}\otimes e_{k}^{*}$; the right ideal $P_{k}M_{3}$ is $e_{k}\otimes(\mathbb{C}^{3})^{*}$.

The three minimal left ideals $M_{3}P_{k}$ are isomorphic, but not canonically: the exchange $x\mapsto xE_{kl}$ is defined up to the gauge $E_{kl}\mapsto(t_{k}/t_{l})E_{kl}$, a $\mathbb{C}^{\times}$-torsor.

The Peirce carrier of a rank-one idempotent $P$ is
$$
C(P)=PMP\oplus PMQ,\qquad \dim_{\mathbb{C}}=1+2=3,
$$
the minimal right ideal $PM_{3}$; its dual is the left ideal $M_{3}P=PMP\oplus QMP$, also of dimension $1+2=3$.

The carrier of the spin chain is $M_{3}P_{1}\cong\mathbb{C}^{3}$, with weights $1,0,-1$ and ladder coefficients $\sqrt2$; it is the spin-one module $\operatorname{Sym}^{2}(\mathbb{C}^{2})$. There are no spinors for $n=3$: the simple module is three-dimensional, and only $n=2$ has a two-dimensional spinorial module.

| Quantity | Value for $M_{3}(\mathbb{C})$ |
|---|---|
| Simple left module | $\mathbb{C}^{3}$ |
| Dimension of a minimal left ideal | $3$ |
| Dimension of a minimal right ideal | $3$ |
| Peirce carrier of a rank-one $P$ | $1+2=3$ |
| Number of minimal left ideals in a complete frame | $3$ |
| Spin of the carrier | $1$ |
| Spinors for $n=3$ | none |
| Algebra as a bimodule | $\mathbb{C}^{3}\otimes(\mathbb{C}^{3})^{*}$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_{3}P_{1}$ | the minimal left ideal, the column, $\cong\mathbb{C}^{3}$ |
| $P_{1}M_{3}$ | the minimal right ideal, the row, $\cong(\mathbb{C}^{3})^{*}$ |
| $C(P)=PMP\oplus PMQ$ | the Peirce carrier of a rank-one idempotent |
| $M_{3}P=PMP\oplus QMP$ | the dual left carrier |
| $E_{ij}\leftrightarrow e_{i}\otimes e_{j}^{*}$ | the tensor decomposition of the algebra |
| $E_{kl}$ | the non-canonical exchange $M_{3}P_{k}\to M_{3}P_{l}$ |
| $\operatorname{Sym}^{2}(\mathbb{C}^{2})$ | the spin-one carrier |
| $J_{3},J_{\pm}$ | the principal $\mathfrak{sl}_{2}$ |

## Further Reading

- [The Peirce Decomposition of $M_3(\mathbb{C})$](the-peirce-decomposition-of-m3c.html), for the nine lines and the coarse corners.
- [The Triplet: Spin One and the Adjoint $1+3+5$ of $M_3(\mathbb{C})$](the-triplet-spin-one-and-the-adjoint-of-m3c.html), for the spin-one summand and the nilpotent triplet.
- [The Spin Chain and the Adjoint Decomposition of $M_3(\mathbb{C})$](the-spin-chain-and-the-adjoint-decomposition-of-m3c.html), for the weights and the ladder.
- [The Matrix Algebra $M_3(\mathbb{C})$](the-matrix-algebra-m3c.html), for the matrix units and the tensor product.
- [The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-m3c.html), for the normalized frame and the exchange.
- [The Two-Parameter Gauge of $M_3(\mathbb{C})$](the-two-parameter-gauge-of-m3c.html), for the $\mathbb{C}^{\times}$-torsor of the exchange.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the $n=2$ case and the spinorial module.
- [Modules over an Algebra](modules-over-an-algebra.html), for the general theory of modules and simple modules.
