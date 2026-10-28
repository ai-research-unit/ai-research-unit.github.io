# __The Frame, the Simple Nilpotents and the Gauge of $M_6(\mathbb{C})$__

## Introduction

A root gives six lines; a frame gives a vector in each line. The passage from the root to the frame is the passage from the projective basis to the basis, and its only freedom is a scale in each of the five simple directions. This article fixes the frame, the matrix units it carries, the five simple nilpotents, the composites they generate, and the five-parameter gauge that rescales them. The count is

$$
\underbrace{30}_{\text{root}}+\underbrace{5}_{\text{gauge}}=\underbrace{35}_{\text{frame}}=\dim PGL_6 .
$$

The article assumes the root and its six Lagrange projectors of *Roots of Unity and the Lagrange Idempotents of $M_6(\mathbb{C})$*. It uses the algebra $M_6(\mathbb{C})$ of *The Matrix Algebra $M_6(\mathbb{C})$* and nothing else: no form, no norm, no topology. The Peirce decomposition by the frame is *The Peirce Decomposition of $M_6(\mathbb{C})$*; the spin chain built on the frame is *The Spin Chain and the Adjoint Decomposition of $M_6(\mathbb{C})$*; the geometry of the frames is *The Geometry of the Idempotents of $M_6(\mathbb{C})$*.

**The gauge is a gauge of the nilpotents.** It rescales $E_{12},\dots,E_{56}$, one parameter for each, and it fixes every idempotent. There are five parameters, not six: the sixth is the overall scale, and the product rule removes it. The cocycle that removes it is §*The Cocycle*.

## The Frame

### Definition

**Definition.** A **frame** of $\mathbb{C}^6$ is an ordered basis $(v_1,\dots,v_6)$, read up to a single overall nonzero scalar:

$$
(v_1,\dots,v_6)\sim(tv_1,\dots,tv_6),\qquad t\in\mathbb{C}^\times .
$$

The frame is written $F=(v_1,\dots,v_6)$, and the class of $F$ in the projective space of bases is the object.

**Proposition.** The set of frames is $PGL_6(\mathbb{C})$, of complex dimension $35$.

**Proof.** A basis is an invertible matrix $B$ whose columns are the $v_i$; the equivalence is $B\sim tB$, so the set of frames is $GL_6(\mathbb{C})/\mathbb{C}^\times=PGL_6(\mathbb{C})$. The dimension is $36-1=35$.

**Definition.** The **dual frame** is the basis $v_1^{\vee},\dots,v_6^{\vee}$ of the dual space defined by $v_j^{\vee}(v_k)=\delta_{jk}$. The **matrix units** of the frame are

$$
E_{ij}=v_iv_j^{\vee},\qquad i,j=1,\dots,6 .
$$

As linear maps, $E_{ij}$ sends $v_j$ to $v_i$ and every other $v_k$ to zero.

**Proposition (the matrix-unit rule).** For all $i,j,k,l$,

$$
E_{ij}E_{kl}=\delta_{jk}E_{il}.
$$

**Proof.** $E_{ij}E_{kl}=v_iv_j^{\vee}v_kv_l^{\vee}=v_i\delta_{jk}v_l^{\vee}=\delta_{jk}E_{il}$.

**Corollary.** The thirty-six matrix units are a basis of $M_6(\mathbb{C})$, the diagonal units $E_{ii}$ are idempotents, the off-diagonal units $E_{ij}$ ($i\neq j$) are square-zero, and

$$
\sum_{i=1}^{6}E_{ii}=I_6,\qquad
E_{ii}E_{jj}=\delta_{ij}E_{ii}.
$$

**Proof.** The rule gives $E_{ii}^2=E_{ii}$ and $E_{ij}^2=\delta_{ji}E_{ij}=0$ for $i\neq j$. The sum $\sum_iE_{ii}$ fixes every $v_j$, hence is the identity. The units are linearly independent because their values on the six vectors are the six matrix units of the standard basis after the identification $v_i\mapsto e_i$.

### The Root of a Frame

**Definition.** The **root of the frame** is

$$
H_F=\sum_{i=1}^{6}\zeta_iE_{ii},
$$

with $\zeta_i=\zeta^{i-1}$ the six sixth roots of unity.

**Proposition.** $H_F$ is a root in the sense of *Roots of Unity and the Lagrange Idempotents of $M_6(\mathbb{C})$*: $H_F^6=I_6$, its eigenvalues are the six roots, each with multiplicity one, and its Lagrange projectors are the diagonal units $E_{ii}$.

**Proof.** In the frame, $H_F$ is the diagonal matrix $\operatorname{diag}(\zeta_1,\dots,\zeta_6)$. It has the six distinct sixth roots on the diagonal, so it is a root and its eigenspaces are the six frame lines. The Lagrange projector of $\zeta_i$ is the coordinate projector $E_{ii}$.

**Corollary.** The frame is a root together with one nonzero vector in each of its six lines. The root is the frame modulo the scales; the scales are the gauge.

**Proof.** The root determines the six lines $V_i=\mathbb{C}v_i$ but no vector inside them. A frame determines the lines and a vector in each. Two frames with the same root differ by $v_i\mapsto t_iv_i$, which is the gauge below.

### The Coordinates

**Definition.** The **coordinates** of $A\in M_6(\mathbb{C})$ in the frame are the thirty-six numbers $a_{ij}$ defined by

$$
A=\sum_{i,j=1}^{6}a_{ij}E_{ij}.
$$

The matrix $(a_{ij})$ is the matrix of $A$ in the basis $(v_1,\dots,v_6)$: the $j$-th column gives the coordinates of $Av_j$.

**Proposition (the coordinate rule for the product).**

$$
(AB)_{ij}=\sum_{k=1}^{6}a_{ik}b_{kj}.
$$

**Proof.** Multiply the two sums and use $E_{ik}E_{kj}=E_{ij}$ and $E_{ik}E_{lj}=0$ for $l\neq k$.

The frame is therefore exactly a choice of coordinates in which the product is the ordinary matrix product, and the root is the diagonal matrix of the sixth roots. **The frame is not an extra structure on the algebra; it is a basis of the algebra adapted to the root.**

## The Simple Nilpotents

### Definition

**Definition.** The **simple nilpotents** of the frame are the five matrix units

$$
E_{12},\ E_{23},\ E_{34},\ E_{45},\ E_{56}.
$$

The name is that of the simple roots of the root system $A_5$: $E_{i,i+1}$ is the root vector of the simple root $\alpha_i$, and the five of them are the simple directions of the flag. It is not a classification of nilpotents: every nonzero nilpotent of $M_6(\mathbb{C})$ is conjugate to $E_{12}$.

**Proposition.** Each simple nilpotent is square-zero and of rank one:

$$
E_{i,i+1}^2=0,\qquad \operatorname{rank}E_{i,i+1}=1,\qquad E_{i,i+1}\neq0 .
$$

**Proof.** The square is $\delta_{i+1,i}E_{i,i+1}=0$. The rank is one because the image is the line $\mathbb{C}v_i$ and the kernel is the hyperplane spanned by the other five vectors. The unit is nonzero because it sends $v_{i+1}$ to $v_i\neq0$.

### The Composites

**Theorem.** For $i<j$,

$$
E_{ij}=E_{i,i+1}E_{i+1,i+2}\cdots E_{j-1,j}.
$$

For $i>j$ the same formula with the reversed chain gives $E_{ij}$; for $i=j$ the empty product is $E_{ii}$.

**Proof.** Apply the matrix-unit rule successively:

$$
E_{i,i+1}E_{i+1,i+2}=E_{i,i+2},\qquad
E_{i,i+2}E_{i+2,i+3}=E_{i,i+3},
$$

and so on. Each intermediate product is a matrix unit because the inner indices match, and the chain telescopes to $E_{ij}$.

**Corollary.** The five simple nilpotents generate, as an algebra without unit, the fifteen-dimensional algebra of strictly upper triangular matrices; with the six diagonal units they generate the twenty-one-dimensional upper triangular subalgebra; and adding the five negative simple units $E_{21},\dots,E_{65}$ generates all of $M_6(\mathbb{C})$.

**Proof.** The composites $E_{ij}$ with $i<j$ are the fifteen positive-root vectors and are obtained from the simple ones by the theorem; their span is the strictly upper triangular algebra. Adding the $E_{ii}$ gives the diagonal, hence the upper triangular subalgebra. The lower triangular units are the products of the negative simple units, obtained by the same telescoping with the indices reversed, and the upper, lower and diagonal units together span all thirty-six coordinates.

### The Positive and the Negative Units

**Proposition.** The off-diagonal units split into the fifteen positive ones $E_{ij}$ with $i<j$ and the fifteen negative ones with $i>j$. Each is nilpotent of index two, and the two sets are exchanged by the transpose in the frame.

**Proof.** $E_{ij}^2=\delta_{ji}E_{ij}=0$ whenever $i\neq j$. The transpose of $v_iv_j^{\vee}$ is $v_jv_i^{\vee}=E_{ji}$.

**Remark.** The words *simple* and *composite* refer to the length of the chain from $i$ to $j$: the simple ones have length one, the composites have length $j-i\ge2$. The algebra has five simple nilpotents and ten composite ones in the positive set, and the same numbers in the negative set.

## The Gauge

### The Action on the Frame

**Definition.** A **gauge** is a tuple

$$
\lambda=(\lambda_1,\dots,\lambda_5)\in(\mathbb{C}^\times)^5 .
$$

It acts on the frame by independent rescalings

$$
v_i\longmapsto t_iv_i,
\qquad
\lambda_i=\frac{t_i}{t_{i+1}},
$$

where $(t_1,\dots,t_6)\in(\mathbb{C}^\times)^6$ is any lift of $\lambda$; the lift is unique up to a common factor, which acts trivially on the projective frame.

**Proposition (the action on the units).** Under the gauge,

$$
E_{ij}\longmapsto\frac{t_i}{t_j}E_{ij},
\qquad
E_{i,i+1}\longmapsto\lambda_iE_{i,i+1},
\qquad
E_{ii}\longmapsto E_{ii}.
$$

**Proof.** $(t_iv_i)(t_jv_j)^{\vee}=t_iv_i\,t_j^{-1}v_j^{\vee}=(t_i/t_j)E_{ij}$. For $j=i+1$ the ratio is $\lambda_i$; for $j=i$ it is $1$.

**Corollary (the gauge rescales the nilpotents and fixes the idempotents).** The five parameters $\lambda_1,\dots,\lambda_5$ act one on each simple nilpotent, and the idempotents $E_{11},\dots,E_{66}$ are fixed. There is no parameter attached to an idempotent.

**Corollary (the action on the composites).** The composite $E_{ij}$ with $i<j$ is rescaled by the product of the simple parameters along the chain:

$$
E_{ij}\longmapsto\lambda_i\lambda_{i+1}\cdots\lambda_{j-1}E_{ij}.
$$

**Proof.** Apply the proposition to each factor of the theorem and multiply the ratios; the product telescopes to $t_i/t_j$.

### The Gauge as Conjugation

**Proposition.** The gauge is the conjugation by the diagonal matrix $G=\operatorname{diag}(t_1,\dots,t_6)$:

$$
E_{ij}\longmapsto GE_{ij}G^{-1}=\frac{t_i}{t_j}E_{ij}.
$$

**Proof.** $G(v_iv_j^{\vee})G^{-1}=(t_iv_i)(t_j^{-1}v_j^{\vee})=(t_i/t_j)E_{ij}$.

**Corollary.** The gauge is an inner automorphism of $M_6(\mathbb{C})$. It fixes the root $H_F$, fixes every idempotent $E_{ii}$, and acts freely on the frame and on the tuple of simple nilpotents.

**Proof.** Conjugation by an invertible matrix is an algebra automorphism. The root $H_F=\sum_i\zeta_iE_{ii}$ is a linear combination of the fixed idempotents, hence fixed. The tuple $(E_{12},\dots,E_{56})$ is rescaled by $(\lambda_1,\dots,\lambda_5)$, so no nonidentity gauge fixes the whole tuple; the frame is rescaled by the $t_i$, so no nonidentity gauge fixes it either.

**Remark.** The gauge is therefore not a change of the algebra and not a change of the root. It is a change of the frame inside the root, and its effect on the matrix of an element is the conjugation

$$
A=\sum a_{ij}E_{ij}\longmapsto GAG^{-1}=\sum\frac{t_i}{t_j}a_{ij}E_{ij}.
$$

The eigenvalues of $A$ are unchanged, the idempotents are unchanged, and only the off-diagonal coordinates move. **This is why the parameter of the gauge belongs to the nilpotent and not to the idempotent.**

### The Cocycle

**Theorem (the cocycle).** Let $c_{ij}\in\mathbb{C}^\times$ be scalars attached to the matrix units $E_{ij}$, and suppose that the rescaled units $c_{ij}E_{ij}$ satisfy the same multiplication rule,

$$
(c_{ij}E_{ij})(c_{jk}E_{jk})=c_{ik}E_{ik}
\qquad\text{for all }i,j,k .
$$

Then there are $t_1,\dots,t_6\in\mathbb{C}^\times$ with

$$
c_{ij}=\frac{t_i}{t_j}
\qquad\text{for all }i,j .
$$

The assignment is unique up to a common factor of the $t_i$, so the group of such rescalings is $(\mathbb{C}^\times)^6/\mathbb{C}^\times\cong(\mathbb{C}^\times)^5$.

**Proof.** The condition is $c_{ij}c_{jk}=c_{ik}$. Setting $j=i$ gives $c_{ii}c_{ik}=c_{ik}$, hence $c_{ii}=1$, since $c_{ik}\neq0$; similarly $c_{jj}=1$. Setting $k=j$ gives $c_{ij}c_{jj}=c_{ij}$, which is consistent. Now fix the index $1$ and put $t_i=c_{i1}$. Then

$$
c_{ij}=c_{i1}c_{1j}=\frac{c_{i1}}{c_{j1}}=\frac{t_i}{t_j},
$$

using $c_{j1}c_{1j}=c_{jj}=1$. The common factor is the only freedom: $t_i\mapsto st_i$ leaves every ratio unchanged.

**Corollary (no sixth parameter, and none on the idempotents).** The gauge has exactly five parameters. A parameter attached to the sixth direction is the overall scale and acts trivially; a parameter attached to an idempotent $E_{ii}$ is forced to $1$ by $c_{ii}=c_{ij}c_{ji}=1$.

**Proof.** The diagonal units are fixed by the cocycle, and the six scales $t_i$ enter only through the five ratios $t_i/t_{i+1}$; the common scale is the kernel of the map $(t_i)\mapsto(t_i/t_{i+1})$.

**Remark (why the composites are not independent).** The ten composite positive units have no gauge parameters of their own: once the five simple ones are fixed, the composite $E_{ij}$ is rescaled by the product along the chain. This is the content of §*The Action on the Composites*, and it is the reason the gauge is five-dimensional rather than fifteen- or thirty-six-dimensional. The cocycle is the algebraic statement that the gauge is a **one-cocycle of the flag**, a coboundary of the chain $1\to2\to\cdots\to6$.

### A Worked Gauge

**Example.** Take the standard frame $v_i=e_i$ and the gauge

$$
\lambda=(2,3,5,7,11).
$$

Choose the lift $t_1=1$, so that

$$
t_2=\tfrac12,\qquad
t_3=\tfrac16,\qquad
t_4=\tfrac1{30},\qquad
t_5=\tfrac1{210},\qquad
t_6=\tfrac1{2310}.
$$

Then

$$
E_{12}\mapsto2E_{12},\quad
E_{23}\mapsto3E_{23},\quad
E_{34}\mapsto5E_{34},\quad
E_{45}\mapsto7E_{45},\quad
E_{56}\mapsto11E_{56},
$$

and the composite $E_{16}$ is rescaled by

$$
\frac{t_1}{t_6}=2310=2\cdot3\cdot5\cdot7\cdot11 .
$$

The diagonal units are unchanged, and the matrix of the gauge is

$$
G=\operatorname{diag}\!\left(1,\tfrac12,\tfrac16,\tfrac1{30},\tfrac1{210},\tfrac1{2310}\right).
$$

For the element $A=\sum_{i,j}a_{ij}E_{ij}$, the gauge sends $a_{ij}$ to $(t_i/t_j)a_{ij}$: the entry $a_{16}$ is multiplied by $2310$, the entry $a_{61}$ by $1/2310$, and the diagonal entries are fixed.

**Remark.** The example exhibits the whole content of the gauge in one line: five independent rescalings of the simple nilpotents, the composites determined by the product, the idempotents fixed.

## The Count

### The Root and the Gauge

**Theorem.** The frame set is the total space of a principal bundle

$$
T\longrightarrow PGL_6\longrightarrow PGL_6/T,
$$

where $T\cong(\mathbb{C}^\times)^5$ is the gauge torus and $PGL_6/T$ is the root set. In particular

$$
\dim PGL_6=35=30+5=\dim(PGL_6/T)+\dim T .
$$

**Proof.** A frame is a point of $PGL_6$. The map to the root is the map to the decomposition into six lines, whose fibre is the torus of independent rescalings modulo the overall scale, of dimension five. The root set is $PGL_6/T$ by *Roots of Unity and the Lagrange Idempotents of $M_6(\mathbb{C})$*, of dimension $30$. The dimensions add along the fibration.

### The Three Counts

The same number is reached by three routes.

| Route | First datum | Dimension | Second datum | Dimension | Total |
|---|---|---|---|---|---|
| root and gauge | root, $PGL_6/T$ | $30$ | gauge, $T$ | $5$ | $35$ |
| frame | ordered projective basis | $35$ | — | — | $35$ |
| group | $PGL_6$ | $35$ | — | — | $35$ |

**Proof.** The three rows count the same set: a frame is a root together with a gauge, an ordered projective basis, and a point of $PGL_6$. The first row is the fibration; the second is the definition; the third is the identification of the frame set with $PGL_6$.

**Remark (the count of the nilpotents).** The five simple nilpotents carry the five gauge parameters. The ten composites carry the ten products, and the fifteen negative units carry the reciprocals. The total number of off-diagonal units is thirty, but only the five simple ones are independent under the gauge. **The gauge is the Cartan torus of the flag, and its dimension is the rank of $A_5$, which is five.**

## Summary

A frame of $\mathbb{C}^6$ is an ordered projective basis, that is a point of $PGL_6$ of dimension $35$. It carries thirty-six matrix units $E_{ij}=v_iv_j^{\vee}$ with $E_{ij}E_{kl}=\delta_{jk}E_{il}$, six idempotents $E_{ii}$ and thirty nilpotents $E_{ij}$, $i\neq j$.

The five simple nilpotents $E_{12},\dots,E_{56}$ generate the fifteen positive units by the composites

$$
E_{ij}=E_{i,i+1}E_{i+1,i+2}\cdots E_{j-1,j},
\qquad i<j.
$$

The gauge is the torus $(\mathbb{C}^\times)^5$ acting by $E_{ij}\mapsto(t_i/t_j)E_{ij}$; it rescales the simple nilpotents by $\lambda_i=t_i/t_{i+1}$, the composites by the products, and fixes every idempotent.

$$
\boxed{\ \text{The frame is the root plus the gauge: }35=30+5.\ }
$$

The cocycle $c_{ij}c_{jk}=c_{ik}$ forces $c_{ij}=t_i/t_j$ and $c_{ii}=1$: no sixth parameter, no parameter on an idempotent.

| Object | Count | Data |
|---|---|---|
| Frame | $35$ | ordered projective basis, $PGL_6$ |
| Root | $30$ | six lines, $PGL_6/T$ |
| Gauge | $5$ | $\lambda_1,\dots,\lambda_5$, the torus $T$ |
| Simple nilpotents | $5$ | $E_{12},\dots,E_{56}$ |
| Composites | $10$ | $E_{ij}$, $i<j$, $j-i\ge2$ |
| Idempotents | $6$ | $E_{ii}$, fixed by the gauge |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F=(v_1,\dots,v_6)$ | a frame, an ordered basis up to overall scale |
| $v_j^{\vee}$ | the dual basis, $v_j^{\vee}(v_k)=\delta_{jk}$ |
| $E_{ij}=v_iv_j^{\vee}$ | the matrix units, $E_{ij}E_{kl}=\delta_{jk}E_{il}$ |
| $H_F=\sum_i\zeta_iE_{ii}$ | the root of the frame |
| $a_{ij}$ | the coordinates of $A$ in the frame |
| $E_{i,i+1}$ | the five simple nilpotents |
| $\lambda_i=t_i/t_{i+1}$ | the gauge parameters, $i=1,\dots,5$ |
| $G=\operatorname{diag}(t_1,\dots,t_6)$ | the gauge transformation |
| $T\cong(\mathbb{C}^\times)^5$ | the gauge torus |
| $c_{ij}$ | a scalar attached to $E_{ij}$, with $c_{ij}c_{jk}=c_{ik}$ |

## Further Reading

- [Roots of Unity and the Lagrange Idempotents of $M_6(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m6c.html), for the root and the six lines.
- [The Peirce Decomposition of $M_6(\mathbb{C})$](the-peirce-decomposition-of-m6c.html), for the corners and the matrix units.
- [The Spin Chain and the Adjoint Decomposition of $M_6(\mathbb{C})$](the-spin-chain-and-the-adjoint-decomposition-of-m6c.html), for the principal $\mathfrak{su}_2$ generated by the simple nilpotents.
- [The Matrix Algebra $M_6(\mathbb{C})$](the-matrix-algebra-m6c.html), for the algebra, the trace, the determinant and $PGL_6$.
- [The Geometry of the Idempotents of $M_6(\mathbb{C})$](the-geometry-of-the-idempotents-of-m6c.html), for the frame bundle over the variety of decompositions.
- [Flag Manifolds](flag-manifolds.html), for the flag variety and its principal bundles.
- [Primitive Idempotents and Minimal Left Ideals](primitive-idempotents-and-minimal-left-ideals.html), for the matrix units and the ideals they generate.
- James E. Humphreys, *Linear Algebraic Groups* (Springer, 1975), for the root systems, the simple roots and the maximal torus.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the flag variety and the Borel subgroup.
- [The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-mnc.html), for the general construction at order $n$.
