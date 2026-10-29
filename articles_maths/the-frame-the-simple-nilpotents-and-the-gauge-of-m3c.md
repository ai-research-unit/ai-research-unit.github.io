# __The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$__

## Introduction

A frame of $M_{3}(\mathbb{C})$ is a basis of the algebra by nine matrix units $E_{ij}$ with $E_{ij}E_{kl}=\delta_{jk}E_{il}$ and $\sum_{i}E_{ii}=I$. The diagonal units are three idempotents; the off-diagonal units are six nilpotents, of which two are the **simple** ones and the remaining four are their products and the products of the opposite pair. The frame is the matrix-unit form of the Peirce decomposition, and it is the object on which the gauge acts.

This article constructs the frame from a basis of $\mathbb{C}^{3}$, proves the multiplication table, isolates the two simple nilpotents $E_{12},E_{23}$ and the composite $E_{13}=E_{12}E_{23}$, and computes the gauge group. The gauge rescales the off-diagonal units by $E_{ij}\mapsto(t_{i}/t_{j})E_{ij}$; it fixes every idempotent, and its group is $(\mathbb{C}^{\times})^{2}$, the maximal torus of $PGL_{3}(\mathbb{C})$. The rescaling of the two simple nilpotents by $\lambda_{1}$ and $\lambda_{2}$ forces the composite to be rescaled by $\lambda_{1}\lambda_{2}$: there is no third independent scalar.

**The idempotents do not depend on the gauge parameter.** The symbols $\lambda_{1},\lambda_{2}$ below are gauge parameters of the nilpotents; they never multiply an idempotent. A statement that an idempotent depends on $\lambda$ is a confusion of the gauge with the frame.

The article assumes the algebra and its matrix units of *The Matrix Algebra $M_{3}(\mathbb{C})$*, the Peirce decomposition of *The Peirce Decomposition of $M_{3}(\mathbb{C})$*, and the root of *Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$*. The two-parameter gauge is developed further in *The Two-Parameter Gauge of $M_3(\mathbb{C})$*; the modules built on the idempotents are *The Modules and the Minimal Left Ideals of $M_3(\mathbb{C})$*.

## The Frame from a Basis

**Definition.** A **frame** of $M_{3}(\mathbb{C})$ is a family $(E_{ij})_{i,j=1}^{3}$ of elements with

$$
E_{ij}E_{kl}=\delta_{jk}E_{il},\qquad \sum_{i=1}^{3}E_{ii}=I,\qquad E_{ii}\neq0 .
$$

The frame is **normalized** by the second condition; the first alone gives $E_{ii}^{2}=E_{ii}$, $E_{ii}E_{jj}=0$ for $i\neq j$, and $E_{ij}^{2}=0$ for $i\neq j$.

**Theorem (the frame from a basis).** Let $(v_{1},v_{2},v_{3})$ be a basis of $\mathbb{C}^{3}$ and let $(v_{1}^{\vee},v_{2}^{\vee},v_{3}^{\vee})$ be the dual basis, $v_{j}^{\vee}(v_{k})=\delta_{jk}$. Put

$$
E_{ij}=v_{i}v_{j}^{\vee}.
$$

Then $(E_{ij})$ is a frame. Conversely every frame is of this form for a basis unique up to a common scalar.

**Proof.** The product is

$$
(v_{i}v_{j}^{\vee})(v_{k}v_{l}^{\vee})=v_{i}\,v_{j}^{\vee}(v_{k})\,v_{l}^{\vee}=\delta_{jk}\,v_{i}v_{l}^{\vee}=\delta_{jk}E_{il},
$$

which is the matrix-unit rule. The diagonal elements are idempotent, $E_{ii}^{2}=v_{i}v_{i}^{\vee}v_{i}v_{i}^{\vee}=v_{i}v_{i}^{\vee}=E_{ii}$, and pairwise orthogonal, $E_{ii}E_{jj}=v_{i}\delta_{ij}v_{j}^{\vee}=\delta_{ij}E_{ii}$. The sum is the resolution of the identity,

$$
\sum_{i}v_{i}v_{i}^{\vee}=I,
$$

because both sides act as the identity on each basis vector $v_{k}$.

Conversely, let $(E_{ij})$ be a frame. The diagonal $E_{ii}$ is a rank-one idempotent, so its image is a line $L_{i}$; the three lines are independent because $\sum E_{ii}=I$, and they are the coordinate lines of a basis. Choose $v_{i}\in L_{i}$ with $E_{ii}v_{i}=v_{i}$. The off-diagonal $E_{ij}$ maps $L_{j}$ to $L_{i}$ and is nonzero; write $E_{ij}=v_{i}\varphi_{j}$ with $\varphi_{j}$ a linear functional. The relation $E_{ij}E_{jk}=E_{ik}$ gives $v_{i}\varphi_{j}(v_{j})\varphi_{k}=v_{i}\varphi_{k}$, hence $\varphi_{j}(v_{j})=1$, and $E_{ij}E_{kj}=0$ for $i\neq k$ gives $\varphi_{j}(v_{k})=0$ for $k\neq j$. So $\varphi_{j}=v_{j}^{\vee}$ and $E_{ij}=v_{i}v_{j}^{\vee}$. A second basis $v_{i}'$ giving the same frame satisfies $v_{i}'v_{j}'^{\vee}=v_{i}v_{j}^{\vee}$ for all $i,j$; taking $i=j$ gives $v_{i}'=s_{i}v_{i}$, and taking $i\neq j$ gives $s_{i}s_{j}^{-1}=1$, so all $s_{i}$ are equal. The basis is unique up to a common scalar.

**Corollary.** The frames of $M_{3}(\mathbb{C})$ form the homogeneous space

$$
\{\text{frames}\}\cong GL_{3}(\mathbb{C})/\mathbb{C}^{\times}I\cong PGL_{3}(\mathbb{C}),
$$

of complex dimension $9-1=8$.

**Proof.** A basis is a point of $GL_{3}$; the frame depends on the basis only through its class modulo a common scalar, by the theorem. The action is free, so the quotient has dimension $9-1=8$.

**The diagonal frame and the root.** Given a frame, the three diagonal idempotents $P_{i}=E_{ii}$ are a complete orthogonal family, and

$$
H=\sum_{i=1}^{3}\zeta_{i}E_{ii}
$$

is a root with simple spectrum, by *Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$*. Conversely, a root $H$ gives its three Lagrange idempotents $P_{i}$, and a frame with $E_{ii}=P_{i}$ is a choice of the six off-diagonal units. The root and the frame are therefore related by

$$
\{\text{frames}\}\longrightarrow\{\text{roots}\},\qquad (E_{ij})\longmapsto\sum_{i}\zeta_{i}E_{ii},
$$

and the fibre is the gauge of §*The Gauge* below.

**The standard frame.** For the standard basis $v_{i}=e_{i}$ the frame is the standard matrix-unit frame $E_{ij}$, with $E_{ii}=\operatorname{diag}(0,\dots,1,\dots,0)$. Its root is $H_{0}=\operatorname{diag}(1,\omega,\omega^{2})$.

## The Simple Nilpotents and the Composite

**Definition.** In a frame, the **simple nilpotents** are the two adjacent off-diagonal units

$$
N_{1}=E_{12},\qquad N_{2}=E_{23}.
$$

They are square-zero,

$$
N_{1}^{2}=E_{12}E_{12}=0,\qquad N_{2}^{2}=E_{23}E_{23}=0,
$$

and their only nonzero product is the **composite**

$$
N_{1}N_{2}=E_{12}E_{23}=E_{13}.
$$

The opposite pair $E_{21},E_{32}$ has the composite $E_{31}=E_{32}E_{21}$.

**Proposition.** The algebra generated by $N_{1}$ and $N_{2}$ is the three-dimensional nilpotent algebra

$$
\mathfrak{n}_{+}=\operatorname{span}\{E_{12},E_{23},E_{13}\},
\qquad
\mathfrak{n}_{+}^{2}=\mathbb{C}E_{13},\qquad
\mathfrak{n}_{+}^{3}=0,
$$

and $E_{13}$ is not an independent generator: it is the product $N_{1}N_{2}$.

**Proof.** The products of the two generators are $N_{1}^{2}=0$, $N_{2}^{2}=0$, $N_{1}N_{2}=E_{13}$ and $N_{2}N_{1}=E_{23}E_{12}=0$, because $E_{23}E_{12}=\delta_{31}E_{22}=0$. Every word in $N_{1},N_{2}$ of length at least two is therefore either $E_{13}$ or zero, and the span of $N_{1},N_{2},E_{13}$ is closed under multiplication. The product $E_{13}E_{13}=0$ and $E_{13}N_{1}=E_{13}E_{12}=0$, $N_{2}E_{13}=E_{23}E_{13}=0$, so the square of the span is $\mathbb{C}E_{13}$ and its cube is zero.

**The composite is forced.** The relation $E_{13}=E_{12}E_{23}$ is a consequence of the frame, not a choice. If the two simple nilpotents are rescaled by $\lambda_{1}$ and $\lambda_{2}$,

$$
E_{12}'=\lambda_{1}E_{12},\qquad E_{23}'=\lambda_{2}E_{23},
$$

then the composite is rescaled by the product,

$$
E_{13}'=E_{12}'E_{23}'=\lambda_{1}\lambda_{2}E_{13}.
$$

There is no independent scalar on $E_{13}$: the third scalar is the product of the first two. This is the cocycle of §*The Gauge*.

**The two simple nilpotents are the simple root vectors.** In the basis of the root, $E_{12}$ and $E_{23}$ are the root vectors of the two simple roots of $\mathfrak{sl}_{3}$, and $E_{13}$ is the root vector of the highest root, whose weight is the sum of the two simple weights. The composite is therefore the highest-root vector, and its gauge weight is the product $\lambda_{1}\lambda_{2}$ of the two simple weights. The lower triangular pair $E_{21},E_{32}$ carries the negative roots, with the composite $E_{31}=E_{32}E_{21}$.

**Explicit matrices.** The standard simple nilpotents and their composite are

$$
N_{1}=\begin{pmatrix}0&1&0\\0&0&0\\0&0&0\end{pmatrix},\qquad
N_{2}=\begin{pmatrix}0&0&0\\0&0&1\\0&0&0\end{pmatrix},\qquad
N_{1}N_{2}=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix}=E_{13}.
$$

The products are checked directly: $N_{1}^{2}=N_{2}^{2}=0$, $N_{1}N_{2}=E_{13}$, $N_{2}N_{1}=0$. The algebra $\mathfrak{n}_{+}$ is the strictly upper triangular algebra, of dimension three; its cube is zero.

## The Gauge

**Definition.** Let $t_{1},t_{2},t_{3}\in\mathbb{C}^{\times}$ and let $D=\operatorname{diag}(t_{1},t_{2},t_{3})$. The **gauge transformation** of the frame is

$$
E_{ij}\longmapsto E_{ij}'=D E_{ij}D^{-1}=\frac{t_{i}}{t_{j}}E_{ij}.
$$

The diagonal units are fixed, $E_{ii}'=E_{ii}$; the off-diagonal units are rescaled by the ratios $t_{i}/t_{j}$.

**Proposition.** The gauge transformation preserves the frame. It fixes every idempotent $E_{ii}$, the root $H=\sum_{i}\zeta_{i}E_{ii}$, the spectrum, the trace, the determinant and the characteristic polynomial of every element. It acts on the Peirce coordinates by

$$
\alpha_{ij}\longmapsto\frac{t_{j}}{t_{i}}\alpha_{ij}.
$$

**Proof.** For the frame, $(D E_{ij}D^{-1})(D E_{kl}D^{-1})=D E_{ij}E_{kl}D^{-1}=\delta_{jk}D E_{il}D^{-1}$; the sum of the diagonal units is $D I D^{-1}=I$. The diagonal units are fixed because $D E_{ii}D^{-1}=(t_{i}/t_{i})E_{ii}=E_{ii}$. The root is a linear combination of the diagonal units, so it is fixed, and so are its spectrum and the polynomial invariants of every element, since conjugation by $D$ preserves the trace and the determinant. If $A=\sum\alpha_{ij}E_{ij}=\sum\alpha_{ij}'E_{ij}'$, then $\alpha_{ij}'E_{ij}'=\alpha_{ij}E_{ij}$ gives $\alpha_{ij}'=\alpha_{ij}(t_{j}/t_{i})$.

**The gauge group is $(\mathbb{C}^{\times})^{2}$.** The parameters $t_{1},t_{2},t_{3}$ and $ct_{1},ct_{2},ct_{3}$ give the same ratios, so the common scalar acts trivially and the effective group is

$$
(\mathbb{C}^{\times})^{3}/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^{2},
$$

of complex dimension two. Its two coordinates are the ratios

$$
\lambda_{1}=\frac{t_{1}}{t_{2}},\qquad \lambda_{2}=\frac{t_{2}}{t_{3}},
\qquad
\frac{t_{1}}{t_{3}}=\lambda_{1}\lambda_{2}.
$$

In particular the simple nilpotents transform by

$$
E_{12}\longmapsto\lambda_{1}E_{12},\qquad
E_{23}\longmapsto\lambda_{2}E_{23},\qquad
E_{13}\longmapsto\lambda_{1}\lambda_{2}E_{13}.
$$

**Worked example.** Take $\lambda_{1}=2$ and $\lambda_{2}=3$. The gauge parameters can be chosen as $t_{1}=6$, $t_{2}=3$, $t_{3}=1$, since $6/3=2$ and $3/1=3$. Then

$$
D=\begin{pmatrix}6&0&0\\0&3&0\\0&0&1\end{pmatrix},
\qquad
D E_{12}D^{-1}=2E_{12},\quad
D E_{23}D^{-1}=3E_{23},\quad
D E_{13}D^{-1}=6E_{13}.
$$

The diagonal idempotents are unchanged:

$$
D E_{11}D^{-1}=E_{11},\qquad
D E_{22}D^{-1}=E_{22},\qquad
D E_{33}D^{-1}=E_{33},
$$

and the root $H_{0}=\operatorname{diag}(1,\omega,\omega^{2})$ is unchanged. The composite is rescaled by $2\cdot3=6$, not by an independent number.

**The cocycle that forbids a third scalar.** Suppose that a rescaling $E_{ij}\mapsto\lambda_{ij}E_{ij}$ with $\lambda_{ij}\in\mathbb{C}^{\times}$ preserves the frame. Then for all $i,j,k$,

$$
\lambda_{ij}\lambda_{jk}=\lambda_{ik},\qquad \lambda_{ii}=1,\qquad \lambda_{ji}=\lambda_{ij}^{-1}.
$$

**Proposition.** Every solution is of the form $\lambda_{ij}=t_{i}/t_{j}$ for some $t_{i}\in\mathbb{C}^{\times}$, and the solutions form a group isomorphic to $(\mathbb{C}^{\times})^{2}$.

**Proof.** Put $t_{i}=\lambda_{i1}$, with the index $1$ fixed. The cocycle gives $\lambda_{ij}=\lambda_{i1}\lambda_{1j}=t_{i}\lambda_{j1}^{-1}=t_{i}/t_{j}$, using $\lambda_{1j}=\lambda_{j1}^{-1}$. Conversely every assignment $t_{i}/t_{j}$ satisfies the three relations. Two assignments $t_{i}$ and $ct_{i}$ give the same $\lambda$, so the parameter space is $(\mathbb{C}^{\times})^{3}/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^{2}$.

**Corollary.** If $\lambda_{1}$ is put on $E_{12}$ and $\lambda_{2}$ on $E_{23}$, then the scalar on $E_{13}$ is forced to be $\lambda_{1}\lambda_{2}$. A third independent scalar $\lambda_{3}$ on $E_{13}$ is incompatible with the frame unless $\lambda_{3}=\lambda_{1}\lambda_{2}$. The only freedom is the two-parameter torus, and the composite carries the product of the two simple weights.

## The Count $8=6+2$

**The frame has eight complex parameters, the root six, and the gauge two.**

**Theorem.** The map

$$
\pi:\{\text{frames}\}\longrightarrow\{\text{roots with simple spectrum}\},\qquad
(E_{ij})\longmapsto H=\sum_{i}\zeta_{i}E_{ii},
$$

is surjective, and its fibre over every root is a torsor under the gauge group $(\mathbb{C}^{\times})^{2}$. Consequently

$$
\dim_{\mathbb{C}}\{\text{frames}\}=8=6+2=\dim_{\mathbb{C}}\{\text{roots}\}+\dim_{\mathbb{C}}(\mathbb{C}^{\times})^{2}.
$$

**Proof.** The map is well defined by §*The Frame from a Basis*: the diagonal units of a frame are a complete orthogonal family, and the root built from them has simple spectrum. It is surjective because a root gives its three Lagrange idempotents $P_{i}$, and a frame with $E_{ii}=P_{i}$ exists: choose nonzero $E_{ij}\in A_{ij}$ normalized by $E_{ij}E_{ji}=P_{i}$; the Peirce pairing of *The Peirce Decomposition of $M_{3}(\mathbb{C})$* makes the choice possible, and the matrix-unit table makes it a frame.

The fibre over $H$ consists of the frames with the same diagonal units. The Peirce lines $A_{ij}=P_{i}M_{3}P_{j}$ are one-dimensional, so a frame over $H$ is the choice of a nonzero $E_{ij}\in A_{ij}$ for each $i\neq j$, normalized by $E_{ij}E_{ji}=P_{i}$. The gauge $E_{ij}\mapsto(t_{i}/t_{j})E_{ij}$ acts on these choices, and it acts simply transitively: given two frames $E_{ij}$ and $E_{ij}'$ with the same diagonal, $E_{ij}'=\mu_{ij}E_{ij}$ with $\mu_{ij}\in\mathbb{C}^{\times}$; the matrix-unit table forces $\mu_{ij}\mu_{jk}=\mu_{ik}$ and $\mu_{ji}=\mu_{ij}^{-1}$, so by the cocycle proposition $\mu_{ij}=t_{i}/t_{j}$ for a unique class of $t$ modulo common scalar. The fibre is therefore a $(\mathbb{C}^{\times})^{2}$-torsor, of dimension two.

The dimensions are the orbit dimension $6$ of *Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$* and the torus dimension $2$; the total is the frame dimension $8$ of §*The Frame from a Basis*. The two counts agree, and the agreement is the content of the theorem.

**The three counts of the same eight.**

- **Frames.** $PGL_{3}$ has dimension $8$.
- **Root plus gauge.** The root orbit $PGL_{3}/T$ has dimension $6$; the torus $T$ has dimension $2$; $6+2=8$.
- **Basis plus gauge.** A basis of $\mathbb{C}^{3}$ has $9$ parameters; the common scalar of the frame removes $1$, leaving the $8$ parameters of the frame. Of these, the $2$ independent scalings of the gauge are the fibre over the root, leaving the $6$ parameters of the root orbit.

The gauge is not a redundancy of the root: it is the fibre of the frame over the root, and it is the freedom of the off-diagonal units at fixed idempotents.

## The Maximal Torus of $PGL_{3}$

**The gauge group is the maximal torus of the projective linear group.**

The diagonal matrices of $GL_{3}$ form a maximal torus $T_{GL}\cong(\mathbb{C}^{\times})^{3}$. Its image in $PGL_{3}=GL_{3}/\mathbb{C}^{\times}I$ is

$$
T=T_{GL}/(T_{GL}\cap\mathbb{C}^{\times}I)\cong(\mathbb{C}^{\times})^{3}/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^{2},
$$

which is a maximal torus of $PGL_{3}$, of dimension two. The gauge of §*The Gauge* is exactly this torus acting by conjugation on the frame; the root vectors $E_{ij}$ are the weight vectors, of weights $t_{i}/t_{j}$, and the simple nilpotents $E_{12},E_{23}$ carry the two simple roots. The composite $E_{13}$ carries the highest root, the sum of the two simple roots in the character lattice.

**The root system.** The weights $t_{i}/t_{j}$ for $i\neq j$ are the six roots of $A_{2}$, and the two simple ones are $\alpha_{1}=t_{1}/t_{2}$ and $\alpha_{2}=t_{2}/t_{3}$; the highest root is $\alpha_{1}\alpha_{2}=t_{1}/t_{3}$. The gauge parameters $\lambda_{1},\lambda_{2}$ are the values of the two simple roots, and the composite weight is their product. The root system is the classical $A_{2}$ of $PGL_{3}$; the frame is a point of the group, and the gauge is the torus that fixes the root.

**The comparison with the biquaternion case.** For $n=2$ the frame has two diagonal idempotents and two off-diagonal units $E_{12},E_{21}$; the gauge is

$$
E_{12}\longmapsto\mu E_{12},\qquad E_{21}\longmapsto\mu^{-1}E_{21},
$$

with one parameter $\mu\in\mathbb{C}^{\times}$. The torus is $(\mathbb{C}^{\times})^{2}/\mathbb{C}^{\times}\cong\mathbb{C}^{\times}$, of dimension one. The $M_{3}$ case has two simple nilpotents and two parameters; the composite is forced. The extra datum that the older literature calls the second root of the two-dimensional frame is a point of this one-parameter gauge: it fixes the relative scale of $E_{12}$ and $E_{21}$, and it is not a second primitive idempotent. The pattern is $(\mathbb{C}^{\times})^{n-1}$ for $M_{n}(\mathbb{C})$: one parameter for the biquaternion algebra $M_{2}(\mathbb{C})$, two for $M_{3}(\mathbb{C})$, and $n-1$ in general.

## Summary

A frame is a basis of $M_{3}(\mathbb{C})$ by matrix units. It is the same data as a basis of $\mathbb{C}^{3}$ up to a common scalar, so the frames form $PGL_{3}(\mathbb{C})$, of complex dimension $8$:

$$
\boxed{\;\{\text{frames}\}\cong PGL_{3}(\mathbb{C}),\qquad \dim_{\mathbb{C}}=8.\;}
$$

The diagonal units are three idempotents; the simple nilpotents are

$$
N_{1}=E_{12},\qquad N_{2}=E_{23},\qquad N_{1}^{2}=N_{2}^{2}=0,\qquad N_{1}N_{2}=E_{13}.
$$

The composite $E_{13}$ is the product of the two simple nilpotents, not an independent generator.

The gauge is

$$
E_{ij}\longmapsto\frac{t_{i}}{t_{j}}E_{ij},\qquad t_{i}\in\mathbb{C}^{\times},
$$

with group $(\mathbb{C}^{\times})^{3}/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^{2}$. It fixes every idempotent, the root, the spectrum and the polynomial invariants. The two simple rescalings $\lambda_{1},\lambda_{2}$ force the composite rescaling $\lambda_{1}\lambda_{2}$; the cocycle $\lambda_{ij}\lambda_{jk}=\lambda_{ik}$ has only the solutions $\lambda_{ij}=t_{i}/t_{j}$, and there is no third independent scalar.

| Quantity | Value for $M_{3}(\mathbb{C})$ |
|---|---|
| Frame dimension | $8$ |
| Root orbit dimension | $6$ |
| Gauge torus dimension | $2$ |
| Simple nilpotents | $E_{12},E_{23}$ |
| Composite | $E_{13}=E_{12}E_{23}$ |
| Gauge parameters | $\lambda_{1},\lambda_{2}$ with $\lambda_{3}=\lambda_{1}\lambda_{2}$ |
| $\dim$ of the maximal torus of $PGL_{3}$ | $2$ |

The count $8=6+2$ is the orbit-stabiliser count for the action of $PGL_{3}$ on the root: the root is the orbit, the gauge is the stabiliser.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E_{ij}$ | the matrix units of a frame |
| $v_{i}^{\vee}$ | the dual basis functional, $v_{j}^{\vee}(v_{k})=\delta_{jk}$ |
| $N_{1}=E_{12}$, $N_{2}=E_{23}$ | the simple nilpotents |
| $\mathfrak{n}_{+}$ | the nilpotent algebra $\operatorname{span}\{E_{12},E_{23},E_{13}\}$ |
| $t_{i}$ | gauge parameters, $t_{i}\in\mathbb{C}^{\times}$ |
| $\lambda_{1}=t_{1}/t_{2}$, $\lambda_{2}=t_{2}/t_{3}$ | the two gauge parameters on the simple nilpotents |
| $T$ | the maximal torus $(\mathbb{C}^{\times})^{2}$ of $PGL_{3}$ |
| $\alpha_{1}=t_{1}/t_{2}$, $\alpha_{2}=t_{2}/t_{3}$ | the simple roots of $A_{2}$ |

## Further Reading

- [The Peirce Decomposition of $M_3(\mathbb{C})$](the-peirce-decomposition-of-m3c.html), for the nine lines and the coarse split.
- [Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m3c.html), for the root $H$ and its idempotents.
- [The Two-Parameter Gauge of $M_3(\mathbb{C})$](the-two-parameter-gauge-of-m3c.html), for the gauge read on the coherence entries and the comparison with the single $\lambda$ of $\mathbb{B}$.
- [The Matrix Algebra $M_3(\mathbb{C})$](the-matrix-algebra-m3c.html), for the matrix units and the projective group.
- [Matrix Algebras](matrix-algebras.html), for the matrix-unit table.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the two-dimensional frame and its single $\mu$.
- [Root Systems and Classification](root-systems-and-classification.html), for the root system $A_{2}$ and the maximal torus.
- [The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-mnc.html), for the general construction at order $n$.
