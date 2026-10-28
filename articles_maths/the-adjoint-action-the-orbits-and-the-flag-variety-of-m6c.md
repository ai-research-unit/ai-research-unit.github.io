# __The Adjoint Action, the Orbits and the Flag Variety__

## Introduction

The projective linear group $PGL_6(\mathbb{C})$ acts on $M_6(\mathbb{C})$ by conjugation,

$$
\Phi_g(A)=gAg^{-1},
\qquad
g\in GL_6(\mathbb{C}),
$$

and the action factors through the center. The orbits are the conjugacy classes, classified by the Jordan type. For a cyclic element with simple spectrum the orbit has dimension $30$ and the stabilizer is the torus

$$
(\mathbb{C}^\times)^5,
$$

so the orbit–stabilizer count is

$$
35=30+5 .
$$

The flag variety $GL_6/B$ of complete flags has dimension $15$; the Grassmannians are

$$
\operatorname{Gr}(1,6)=\mathbb{P}^5,\qquad
\dim\operatorname{Gr}(2,6)=2\cdot4=8 .
$$

The gauge is the fibre of the conjugation map over the root: the set of frames diagonalising $H$ is a torsor under the stabilizer $(\mathbb{C}^\times)^5$.

The article assumes the roots of *Roots of Unity and the Lagrange Idempotents* and the projective linear group of *The Matrix Algebra $M_6(\mathbb{C})$*. It uses the language of algebraic groups but no topology beyond the dimension counts. The Jordan decomposition is *The Element, the Coordinates and the Trace*; the spectral strata are *The Sextic and the Spectral Strata*; the Grassmannian geometry is *The Geometry of the Idempotents*.

## The Adjoint Action

### Definition

**Definition.** The **adjoint action** of $PGL_6(\mathbb{C})$ on $M_6(\mathbb{C})$ is

$$
\Phi_{\bar g}(A)=gAg^{-1},
$$

where $\bar g$ is the class of $g\in GL_6$ modulo the scalars. On the Lie algebra $\mathfrak{sl}_6$ it is the adjoint representation

$$
\operatorname{Ad}_g(X)=gXg^{-1}.
$$

**Theorem.** The action is well defined, faithful, and preserves the trace, the determinant, the characteristic polynomial and the Jordan type.

**Proof.** If $g$ is replaced by $\lambda g$, the conjugation is unchanged. The kernel of the action is the center $\mathbb{C}^\times I_6$, so the action of $PGL_6$ is faithful. Conjugation preserves the characteristic polynomial, hence the trace, the determinant and the eigenvalues; it preserves the Jordan form.

**Corollary (the infinitesimal action).** The Lie algebra action is

$$
\mathfrak{sl}_6\longrightarrow\operatorname{End}(M_6),
\qquad
X\longmapsto\operatorname{ad}_X,
\qquad
\operatorname{ad}_X(A)=[X,A].
$$

**Proof.** Differentiate $e^{tX}Ae^{-tX}$ at $t=0$.

### The Orbits

**Theorem.** Two matrices are in the same $PGL_6$ orbit if and only if they have the same Jordan type: the same eigenvalues with the same multiplicities and the same Jordan block sizes.

**Proof.** The Jordan normal form is a complete invariant of conjugacy; two matrices with the same Jordan type are conjugate, and conjugation preserves the type.

**Corollary (the orbit types).**

- The **semisimple orbits** are the conjugacy classes of diagonalizable matrices; they are parameterized by the eigenvalue multiset, an element of $\operatorname{Sym}^6(\mathbb{C})$.
- The **nilpotent orbits** are the conjugacy classes of nilpotent matrices; they are parameterized by the partitions of $6$.
- A general orbit is the product of a semisimple orbit and a nilpotent orbit in each generalized eigenspace.

**Proof.** The Jordan decomposition $A=S+N$ with $SN=NS$; the semisimple part gives the eigenvalue multiset, the nilpotent part gives a partition in each generalized eigenspace.

**Theorem (the dimension).** For any $A$,

$$
\dim(PGL_6\cdot A)=35-\dim Z_{PGL_6}(A)
=36-\dim Z_{GL_6}(A),
$$

where $Z$ is the centralizer.

**Proof.** The orbit–stabilizer theorem for the $35$-dimensional group $PGL_6$; the centralizer in $PGL_6$ is the image of the centralizer in $GL_6$, and the two dimensions differ by the one-dimensional center.

**Corollary (the cyclic orbit).** If $A$ is cyclic with simple spectrum, then

$$
Z_{GL_6}(A)\cong(\mathbb{C}^\times)^6,
\qquad
Z_{PGL_6}(A)\cong(\mathbb{C}^\times)^5,
\qquad
\dim(PGL_6\cdot A)=30 .
$$

**Proof.** The centralizer of a cyclic element is $\mathbb{C}[A]^\times$; for a simple spectrum this is the diagonal torus in the eigenbasis, of dimension $6$ in $GL_6$ and $5$ in $PGL_6$.

**Corollary (the root orbit).** The orbit of the root $H$ is the set of matrices with characteristic polynomial $t^6-1$ and simple spectrum; it has dimension $30$.

**Proof.** All such matrices are conjugate to $H$; the orbit is the fibre of the characteristic map over $t^6-1$, of dimension $30$.

### The Nilpotent Orbits

**Theorem.** The nilpotent orbits of $M_6(\mathbb{C})$ are the partitions of $6$. For a partition $\lambda$ with conjugate partition $\lambda'$,

$$
\dim\mathcal O_\lambda=36-\sum_i(\lambda_i')^2 .
$$

**Proof.** The centralizer of a nilpotent of Jordan type $\lambda$ has dimension $\sum_i(\lambda_i')^2$ (the standard dimension formula for the centralizer of a nilpotent matrix); the orbit dimension is $36$ minus that.

**Corollary (the table).**

| Partition $\lambda$ | $\lambda'$ | $\sum(\lambda_i')^2$ | $\dim\mathcal O_\lambda$ |
|---|---|---|---|
| $(6)$ | $(1^6)$ | $6$ | $30$ |
| $(5,1)$ | $(2,1^4)$ | $8$ | $28$ |
| $(4,2)$ | $(2,2,1,1)$ | $10$ | $26$ |
| $(4,1,1)$ | $(3,1,1,1)$ | $12$ | $24$ |
| $(3,3)$ | $(2,2,2)$ | $12$ | $24$ |
| $(3,2,1)$ | $(3,2,1)$ | $14$ | $22$ |
| $(3,1,1,1)$ | $(4,1,1)$ | $18$ | $18$ |
| $(2,2,2)$ | $(3,3)$ | $18$ | $18$ |
| $(2,2,1,1)$ | $(4,2)$ | $20$ | $16$ |
| $(2,1,1,1,1)$ | $(5,1)$ | $26$ | $10$ |
| $(1^6)$ | $(6)$ | $36$ | $0$ |

**Proof.** Compute the conjugate partition and the sum of squares; subtract from $36$.

**Remark (the regular nilpotent).** The principal nilpotent orbit $(6)$ has dimension $30$, the same as the regular semisimple orbit. The zero orbit $(1^6)$ has dimension $0$. The nilpotent cone is the union of the eleven orbits.

## The Stabilizer and the Count

### The Cyclic Stabilizer

**Theorem.** The stabilizer in $PGL_6$ of a cyclic element with simple spectrum is the maximal torus

$$
(\mathbb{C}^\times)^5,
$$

of dimension $5$.

**Proof.** The centralizer in $GL_6$ is the diagonal torus $(\mathbb{C}^\times)^6$; the center $\mathbb{C}^\times I_6$ is the diagonal scalar, and the quotient is $(\mathbb{C}^\times)^5$.

**Corollary (the stabilizer of the root).** The stabilizer of the root $H$ is the gauge torus

$$
(\mathbb{C}^\times)^5,
$$

the same group that rescales the simple nilpotents of *The Frame, the Simple Nilpotents and the Gauge*.

**Proof.** $H$ has simple spectrum, so its centralizer is the diagonal torus modulo the center; the gauge is the same torus.

### The Orbit–Stabilizer Count

**Theorem.** For the cyclic element,

$$
\dim PGL_6=35=\dim(PGL_6\cdot A)+\dim Z_{PGL_6}(A)=30+5 .
$$

For the same element in $GL_6$,

$$
36=30+6 .
$$

**Proof.** The orbit–stabilizer theorem; the dimensions above.

**Corollary (the flag count).** The dimensions are

$$
\dim GL_6=36,\qquad
\dim B=21,\qquad
\dim GL_6/B=15,
$$

and

$$
\dim\operatorname{Gr}(1,6)=5,\qquad
\dim\operatorname{Gr}(2,6)=8 .
$$

**Proof.** The Borel subgroup of upper triangular matrices has $6$ diagonal and $15$ off-diagonal parameters, of dimension $21$; the quotient has dimension $36-21=15$. The Grassmannian $\operatorname{Gr}(k,6)$ has dimension $k(6-k)$: $1\cdot5=5$ and $2\cdot4=8$.

### The Gauge as the Fibre

**Theorem.** The conjugation map

$$
PGL_6\longrightarrow\mathcal O_H,
\qquad
\bar g\longmapsto gHg^{-1},
$$

is a principal bundle with fibre the stabilizer $(\mathbb{C}^\times)^5$. The gauge group is the fibre over the root $H$.

**Proof.** The fibre over $H$ is the set of $\bar g$ with $gHg^{-1}=H$, that is the stabilizer. The map is surjective onto the orbit by definition, and the stabilizer acts freely on the fibres.

**Corollary (the frame picture).** The set of ordered bases in which $H$ is diagonal is a torsor under $(\mathbb{C}^\times)^6$; modulo the overall scalar, the set of projective frames is a torsor under the gauge $(\mathbb{C}^\times)^5$. Choosing a projective frame is choosing a gauge.

**Proof.** If $g_0$ diagonalizes $H$, every other diagonalizing basis is $g_0t$ with $t$ in the centralizer $(\mathbb{C}^\times)^6$; the centralizer modulo the center is the gauge.

## The Flag Variety

### The Full Flag Variety

**Definition.** A **complete flag** of $\mathbb{C}^6$ is a chain

$$
0\subset V_1\subset V_2\subset\cdots\subset V_5\subset\mathbb{C}^6,
\qquad
\dim V_i=i .
$$

The **flag variety** is

$$
\mathcal F=GL_6/B,
$$

where $B$ is the Borel subgroup of upper triangular matrices, the stabilizer of the standard flag.

**Theorem.** $\mathcal F$ is a smooth projective variety of dimension

$$
\dim\mathcal F=36-21=15=\frac{6\cdot5}{2}.
$$

**Proof.** $GL_6$ acts transitively on the complete flags (any flag is carried to the standard one by a basis adapted to the flag); the stabilizer is the Borel $B$, of dimension $21$; the quotient has dimension $15$.

**Corollary (the iterated bundle and the Plücker embedding).** The flag variety embeds in the product of the Grassmannians,

$$
\mathcal F\hookrightarrow\operatorname{Gr}(1,6)\times\operatorname{Gr}(2,6)\times\cdots\times\operatorname{Gr}(5,6),
$$

and it is an iterated projective bundle with fibres

$$
\mathbb{P}^5,\quad\mathbb{P}^4,\quad\mathbb{P}^3,\quad\mathbb{P}^2,\quad\mathbb{P}^1,
$$

so that

$$
\dim\mathcal F=5+4+3+2+1=15 .
$$

**Proof.** Choose $V_1\in\mathbb{P}^5$ (dimension $5$); then $V_2/V_1$ is a line in $\mathbb{C}^6/V_1\cong\mathbb{C}^5$, so $V_2$ varies in a $\mathbb{P}^4$ (dimension $4$); then $V_3/V_2$ varies in a $\mathbb{P}^3$ (dimension $3$); then $V_4/V_3$ in a $\mathbb{P}^2$ (dimension $2$); then $V_5/V_4$ in a $\mathbb{P}^1$ (dimension $1$). The total is $15$.

**Corollary (the eigenbasis).** An ordered eigenbasis of a cyclic element with simple spectrum determines a complete flag: the first $k$ eigenvectors span $V_k$. The flag is independent of the scaling of the eigenvectors; the scalings are the gauge.

**Proof.** The flag is the chain of spans; rescaling a vector does not change its span.

### The Grassmannians

**Definition.** The **Grassmannian** $\operatorname{Gr}(k,6)$ is the set of $k$-dimensional subspaces of $\mathbb{C}^6$.

**Theorem.**

$$
\dim\operatorname{Gr}(k,6)=k(6-k),
$$

and

$$
\operatorname{Gr}(1,6)=\mathbb{P}^5,\qquad
\dim\operatorname{Gr}(2,6)=8,\qquad
\dim\operatorname{Gr}(3,6)=9 .
$$

**Proof.** A $k$-plane is the image of a full-rank $6\times k$ matrix; the space of such matrices has dimension $6k$, the stabilizer $GL_k$ has dimension $k^2$, and the quotient has dimension $6k-k^2=k(6-k)$.

**Corollary (the idempotents).** The rank-$k$ idempotents form the homogeneous space

$$
GL_6/(GL_k\times GL_{6-k}),
$$

of dimension $2k(6-k)$. The image map to $\operatorname{Gr}(k,6)$ is a fibration with fibre the affine space of complements, of dimension $k(6-k)$.

**Proof.** An idempotent of rank $k$ is determined by its image $V$ and its kernel $W$, a complementary $k$-plane and $(6-k)$-plane. The image is a point of $\operatorname{Gr}(k,6)$; the kernel is a point of the affine space of complements to $V$ in $\mathbb{C}^6$, of dimension $k(6-k)$. The total dimension is $k(6-k)+k(6-k)=2k(6-k)$. For $k=1,2,3$ these are $10,16,18$.

**Corollary (the minimal ideals).** The minimal left ideals are parameterized by the hyperplanes of $\mathbb{C}^6$, that is by $\mathbb{P}^5$ of the dual; the minimal right ideals by the lines of $\mathbb{C}^6$, that is by $\mathbb{P}^5$.

**Proof.** This is *The Modules and the Minimal Left Ideals*: the left ideal depends on the kernel hyperplane, the right ideal on the image line.

### The Incidence

**Theorem.** The full flag variety fibres over each Grassmannian:

$$
\pi_k:\mathcal F\longrightarrow\operatorname{Gr}(k,6),
\qquad
(V_1,\dots,V_5)\longmapsto V_k,
$$

with fibre the product of the flag varieties of $V_k$ and $\mathbb{C}^6/V_k$.

**Proof.** The fibre over $V_k$ consists of the flags of $V_k$ and the flags of the quotient; the dimensions add.

**Corollary (the dimensions).** For $k=1$ the fibre has dimension $10$; for $k=2$ it has dimension $7$; for $k=3$ it has dimension $6$.

**Proof.** $\dim\mathcal F-\dim\operatorname{Gr}(k,6)$: $15-5=10$, $15-8=7$, $15-9=6$.

**Remark (the Peirce reading).** The image of a rank-$k$ idempotent is a point of $\operatorname{Gr}(k,6)$; the idempotent is a point of the total space of the complement bundle over the Grassmannian. The corners are the blocks relative to the plane and its complement; the stabilizer of the idempotent is the Levi $GL(V)\times GL(W)$, while the parabolic is the stabilizer of the image plane alone. **The Grassmannian is the base of the Peirce fibration, not the whole space of idempotents.**

## The Gauge as the Fibre over the Root

### The Bundle

**Theorem.** The map

$$
\pi:PGL_6\longrightarrow\mathcal O_H,
\qquad
\pi(\bar g)=gHg^{-1},
$$

is a principal $(\mathbb{C}^\times)^5$-bundle. The gauge group is the fibre $\pi^{-1}(H)$.

**Proof.** The fibre is the stabilizer; the action of the stabilizer on the fibre is free and transitive.

**Corollary (the dimensions).**

$$
\dim PGL_6=35=\dim\mathcal O_H+\dim(\mathbb{C}^\times)^5=30+5 .
$$

**Proof.** The dimension of a principal bundle is the sum of the base and the fibre.

### The Root

**Theorem.** The orbit $\mathcal O_H$ is the set of roots: the matrices with characteristic polynomial $t^6-1$ and simple spectrum. The fibre over $H$ is the gauge torus; the total space is the set of pairs (root, frame).

**Proof.** The roots are conjugate to $H$; the fibre is the centralizer.

**Corollary (the frame bundle).** The total space of the bundle is the set of pairs $(H',g)$ with $H'=gHg^{-1}$; the projection forgets $g$. The gauge is the choice of the frame at the root.

**Proof.** The pair is determined by $g$ modulo the stabilizer; the total space is $PGL_6$.

### The Count

**Theorem.** The three counts are

$$
35=30+5,
\qquad
36=30+6,
\qquad
15=5+4+3+2+1 .
$$

**Proof.** The first is the $PGL_6$ orbit–stabilizer count; the second the $GL_6$ count; the third the iterated bundle of the flag variety.

**Remark (the root and the flag).** The root fixes the spectrum; the orbit is the set of matrices with that spectrum; the gauge is the ambiguity of the eigenbasis; the flag is the chain of spans of the eigenbasis. **The root, the orbit, the gauge and the flag are four readings of the same eigenbasis.**

## Summary

The adjoint action of $PGL_6$ on $M_6(\mathbb{C})$ has the Jordan types as orbits. For the cyclic element with simple spectrum,

$$
\dim(PGL_6\cdot A)=30,
\qquad
Z_{PGL_6}(A)\cong(\mathbb{C}^\times)^5,
$$

and the orbit–stabilizer count is

$$
35=30+5 .
$$

The nilpotent orbits are the partitions of $6$, with dimensions $36-\sum_i(\lambda_i')^2$; the principal orbit has dimension $30$, the zero orbit $0$.

$$
\boxed{\ 35=30+5,\qquad \dim GL_6/B=15,\qquad \operatorname{Gr}(1,6)=\mathbb{P}^5,\quad \dim\operatorname{Gr}(2,6)=8 .\ }
$$

The flag variety $GL_6/B$ has dimension $15$; the Grassmannians have dimensions $k(6-k)$; the full flag fibres over each Grassmannian. The conjugation map $PGL_6\to\mathcal O_H$ is a principal bundle with fibre the gauge torus $(\mathbb{C}^\times)^5$; the gauge is the fibre over the root.

| Object | Dimension |
|---|---|
| $PGL_6$ | $35$ |
| Cyclic orbit | $30$ |
| Gauge stabilizer | $5$ |
| $GL_6$ | $36$ |
| Flag variety | $15$ |
| $\operatorname{Gr}(1,6)=\mathbb{P}^5$ | $5$ |
| $\operatorname{Gr}(2,6)$ | $8$ |
| $\operatorname{Gr}(3,6)$ | $9$ |
| Principal nilpotent orbit | $30$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi_g$ | the conjugation $A\mapsto gAg^{-1}$ |
| $\mathcal O_H$ | the orbit of the root $H$ |
| $Z_{PGL_6}(A)$ | the stabilizer of $A$ |
| $\mathcal F=GL_6/B$ | the full flag variety |
| $\operatorname{Gr}(k,6)$ | the Grassmannian of $k$-planes |
| $B$ | the Borel subgroup of upper triangular matrices |
| $\lambda'$ | the conjugate partition of a nilpotent Jordan type |

## Further Reading

- [The Matrix Algebra $M_6(\mathbb{C})$](the-matrix-algebra-m6c.html), for $PGL_6$, the derivations and the automorphisms.
- [The Element, the Coordinates and the Trace](the-element-the-coordinates-and-the-trace-of-m6c.html), for the Jordan decomposition and the Jordan type.
- [The Sextic and the Spectral Strata](the-sextic-and-the-spectral-strata-of-m6c.html), for the spectral strata and the centralizer.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge-of-m6c.html), for the gauge torus.
- [The Geometry of the Idempotents](the-geometry-of-the-idempotents-of-m6c.html), for the Grassmannian of the idempotents.
- [The Modules and the Minimal Left Ideals](the-modules-and-the-minimal-left-ideals-of-m6c.html), for the projective space of the minimal ideals.
- [The Adjoint Action and the Orbits](the-adjoint-action-and-the-orbits.html), for the general theory of conjugacy classes.
- [The Flag Variety](the-flag-variety.html), for the general theory of $GL_n/B$ and the Plücker embedding.
