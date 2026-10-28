# __The Geometry of the Idempotents__

## Introduction

**The idempotents of rank $p$ in $M_4(\mathbb{C})$ form the homogeneous space $PGL_4/P(GL_p\times GL_{4-p})$, of complex dimension $2p(4-p)$; for $p=1$ this is an affine bundle of rank $3$ over $\mathbb{P}^3$, of dimension $6$.** The fibre over a $p$-plane is the affine space of complements, which is contractible; the idempotents of rank $p$ are therefore homotopy equivalent to the Grassmannian $\operatorname{Gr}(p,4)$. The full flag variety $GL_4/B$ has dimension $6$; the partial flags and their incidence relations organise the complements, and the gauge torus is the fibre of the frame bundle over the root orbit.

The article describes the rank-one idempotents and their affine bundle, the general rank-$p$ homogeneous space, the tangent space and the rank stratification, the relation to the flag variety and the Grassmannians, and the gauge.

The Peirce decomposition is *The Peirce Decomposition*; the rank-two split is *The Rank-Two Split*; the root and the gauge are *The Frame, the Simple Nilpotents and the Gauge*; the adjoint action and the flag variety are *The Adjoint Action, the Orbits and the Flag Variety*; the topology is *The Topology of $M_4(\mathbb{C})$*.

## Rank-One Idempotents

**Definition.** An **idempotent** is a matrix $P$ with

$$
P^2=P.
$$

Its **rank** is the dimension of its image. A rank-one idempotent has the form

$$
P=u\,\varphi,\qquad
\varphi(u)=1,
$$

where $u\in\mathbb{C}^4$ is a nonzero vector and $\varphi\in(\mathbb{C}^4)^*$ is a linear form with $\varphi(u)=1$. The image is the line $L=\mathbb{C}u$, and the kernel is the hyperplane $H=\ker\varphi$, which does not contain $u$.

**The affine bundle.** The map

$$
\pi:\{P:\operatorname{rank}P=1,\ P^2=P\}\longrightarrow\mathbb{P}^3,
\qquad
P\longmapsto\operatorname{im}P,
$$

sends a rank-one idempotent to its image line. The fibre over a line $L$ is

$$
\pi^{-1}(L)=\{\varphi\in L^*:\varphi(u)=1\},
$$

an affine space of dimension $3$: the linear forms on $L$ with value $1$ on $u$. The total space is an **affine bundle of rank $3$** over $\mathbb{P}^3$, of complex dimension

$$
3+3=6.
$$

**The chart.** In the frame where $u=e_1$, a rank-one idempotent with image the first coordinate line is

$$
P=E_{11}+aE_{12}+bE_{13}+cE_{14}
=\begin{pmatrix}
1&a&b&c\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
\qquad a,b,c\in\mathbb{C}.
$$

Indeed $P^2=P$, the image is $\mathbb{C}e_1$, and the kernel is

$$
x_1+ax_2+bx_3+cx_4=0.
$$

The three coordinates $(a,b,c)$ are the fibre coordinates over the line $[e_1]$. The transition functions between charts are affine, because the condition $\varphi(u)=1$ is affine in the frame.

**The fibre is not a vector space.** The fibre over $L$ is an affine space, not a vector space: there is no canonical origin. The **orthogonal projection** onto $L$,

$$
P_L=u(u^*u)^{-1}u^*,
$$

is a distinguished point of the fibre, the point where the kernel is $L^\perp$. It gives a global section of the affine bundle and identifies the fibre with the vector space $L^\perp$-valued forms; the section depends on the Hermitian metric.

**The orthogonal idempotents.** The idempotents with $P^*=P$ are the orthogonal projections. A rank-one orthogonal projection is determined by its image line, so the orthogonal rank-one idempotents form the Grassmannian

$$
\operatorname{Gr}(1,4)=\mathbb{P}^3,
$$

of dimension $3$. They are the zero section of the affine bundle; the general rank-one idempotents have a nonzero complement coordinate.

## Rank-$p$ Idempotents

**The homogeneous space.** Let $P$ be an idempotent of rank $p$. The image $U=\operatorname{im}P$ and the kernel $W=\ker P$ are complementary:

$$
\mathbb{C}^4=U\oplus W,\qquad
\dim U=p,\quad \dim W=4-p.
$$

Conversely, every direct sum decomposition determines a unique idempotent, the projection onto $U$ along $W$. The group $GL_4$ acts transitively on the rank-$p$ idempotents by conjugation, and the stabiliser of $P$ is the block-diagonal group

$$
GL_p\times GL_{4-p}
=\left\{\begin{pmatrix}A&0\\0&D\end{pmatrix}:A\in GL_p,\ D\in GL_{4-p}\right\}.
$$

In the projective group the stabiliser is its image

$$
P(GL_p\times GL_{4-p})=(GL_p\times GL_{4-p})/\mathbb{C}^\times I.
$$

Hence the rank-$p$ idempotents form the homogeneous space

$$
\mathcal{I}_p=PGL_4/P(GL_p\times GL_{4-p}),
$$

of complex dimension

$$
\dim\mathcal{I}_p=15-\bigl(p^2+(4-p)^2-1\bigr)
=16-p^2-(4-p)^2
=2p(4-p).
$$

The values are

$$
p=0:\ 0,\qquad
p=1:\ 6,\qquad
p=2:\ 8,\qquad
p=3:\ 6,\qquad
p=4:\ 0.
$$

**The bundle over the Grassmannian.** The projection

$$
\pi:\mathcal{I}_p\longrightarrow\operatorname{Gr}(p,4),\qquad
P\longmapsto\operatorname{im}P,
$$

is a fibre bundle. The fibre over a $p$-plane $U$ is the affine space of complements $W$ to $U$, equivalently the affine space of linear maps

$$
B:W\longrightarrow U,
$$

the graphs of which are the complements. The fibre has dimension

$$
p(4-p),
$$

and the total dimension is

$$
p(4-p)+p(4-p)=2p(4-p).
$$

The fibre is contractible, so the total space $\mathcal{I}_p$ is homotopy equivalent to $\operatorname{Gr}(p,4)$.

**The chart.** In a decomposition $\mathbb{C}^4=U\oplus W$ with $U$ spanned by the first $p$ coordinates, every idempotent with image $U$ has the block form

$$
P=\begin{pmatrix}I_p&B\\0&0\end{pmatrix},
\qquad
B\in\operatorname{Hom}(W,U)\cong\mathbb{C}^{p\times(4-p)}.
$$

The square is $P$ because the lower-left block is zero and the upper-left block is the identity; the kernel is the graph of $-B$ in $W$. The matrix $B$ is the fibre coordinate; the orthogonal projection is $B=0$.

**The orthogonal idempotents.** The self-adjoint idempotents of rank $p$ are the orthogonal projections, determined by their image $p$-plane. They form the Grassmannian

$$
\operatorname{Gr}(p,4),\qquad
\dim=p(4-p),
$$

the zero section of the affine bundle. The general idempotents have the complement coordinate $B\ne0$; the affine bundle is the total space, and the Grassmannian is the compact skeleton.

**The rank-one case.** For $p=1$,

$$
\mathcal{I}_1\longrightarrow\mathbb{P}^3
$$

is the affine bundle of rank $3$ of the previous section; for $p=3$ it is the dual affine bundle over $\mathbb{P}^3$; for $p=2$ it is the affine bundle of rank $4$ over $\operatorname{Gr}(2,4)$, of dimension $8$.

## The Tangent Space

**The tangent space at $P$.** Differentiate the equation $P(t)^2=P(t)$ at $t=0$:

$$
X P+P X=X,
$$

where $X=\dot P(0)$. The tangent space of the idempotent variety at $P$ is therefore

$$
T_P\mathcal{I}_p=\{X\in M_4:XP+PX=X\}.
$$

**The Peirce form.** In the decomposition $\mathbb{C}^4=U\oplus W$, write

$$
P=\begin{pmatrix}I_p&B\\0&0\end{pmatrix},
\qquad
X=\begin{pmatrix}X_{11}&X_{12}\\X_{21}&X_{22}\end{pmatrix},
\qquad B:W\to U .
$$

The condition $XP+PX=X$ is equivalent to

$$
X_{11}=-BX_{21},\qquad X_{22}=X_{21}B,
$$

with $X_{12}:W\to U$ and $X_{21}:U\to W$ free. Hence

$$
\dim T_P\mathcal{I}_p=p(4-p)+p(4-p)=2p(4-p).
$$

Equivalently, in the Peirce decomposition of $P$, the tangent space is $PMQ\oplus QMP$, the two off-diagonal corners. The diagonal Peirce corners $PMP\oplus QMQ$ are the normal directions for the trace form. At the orthogonal projection $B=0$ the coordinate blocks and the Peirce corners coincide, and the tangent space is the off-diagonal block space.

**Smoothness.** Each rank-$p$ stratum is a homogeneous space $PGL_4/P$, so it is smooth, and the tangent space has the expected dimension. The rank is locally constant on the idempotent variety, because $\operatorname{rank}P=\operatorname{tr}P$ is continuous and integer-valued; the strata are therefore open and closed, and there is no closure order between different ranks.

## The Rank Stratification

**The strata.** The idempotents split by rank:

$$
\mathcal{I}=\bigsqcup_{p=0}^{4}\mathcal{I}_p,
\qquad
\mathcal{I}_p=\{P:P^2=P,\ \operatorname{rank}P=p\}.
$$

The strata are the orbits of $PGL_4$; the rank is the only invariant, because every rank-$p$ idempotent is conjugate to $\operatorname{diag}(I_p,0)$.

**The strata are clopen.** The rank of an idempotent is its trace, $\operatorname{rank}P=\operatorname{tr}P$, which is continuous and integer-valued on the idempotent variety. Hence each $\mathcal{I}_p$ is both open and closed, and the closure of $\mathcal{I}_p$ is $\mathcal{I}_p$ itself:

$$
\overline{\mathcal{I}_p}=\mathcal{I}_p.
$$

The variety is the disjoint union of the five connected components $\mathcal{I}_0,\dots,\mathcal{I}_4$. The zero idempotent and the identity are isolated points; the rank-one and rank-three strata are six-dimensional; the rank-two stratum is eight-dimensional. There is no closure order between different ranks: a limit of rank-$p$ idempotents has rank $p$.

**The rank-two case.** The rank-two idempotents have dimension $8$; the orthogonal ones form $\operatorname{Gr}(2,4)$ of dimension $4$. In the standard frame the two chiral idempotents $P_+$ and $P_-$ of *The Two Chiralities* are two particular orthogonal rank-two idempotents, points of the Grassmannian, not components. For a general root they are non-Hermitian projections and correspond to transverse pairs of planes, not to points of $\operatorname{Gr}(2,4)$. The general rank-two idempotent has a nonzero mass block; the Peirce table is *The Rank-Two Split*.

**The decomposition.** The rank-$p$ idempotent gives the Peirce corners

$$
p^2+p(4-p)+(4-p)p+(4-p)^2=16,
$$

with dimensions

$$
p^2,\quad p(4-p),\quad (4-p)p,\quad (4-p)^2.
$$

For $p=1$: $1+3+3+9$; for $p=2$: $4+4+4+4$; for $p=3$: $9+3+3+1$. The geometry of the idempotent is the geometry of its Peirce corners.

## The Flag Variety and the Partial Flags

**The full flag variety.** A **full flag** is a chain

$$
0=F_0\subset F_1\subset F_2\subset F_3\subset F_4=\mathbb{C}^4,
\qquad
\dim F_k=k.
$$

The flag variety is

$$
\mathcal{F}=GL_4/B,
$$

where $B$ is the Borel subgroup of upper triangular matrices. Its dimension is

$$
\dim\mathcal{F}=16-10=6.
$$

The flag variety is smooth, projective and simply connected.

**The Grassmannians.** The Grassmannian $\operatorname{Gr}(p,4)$ is the space of $p$-planes; its dimension is

$$
\dim\operatorname{Gr}(p,4)=p(4-p).
$$

In particular,

$$
\operatorname{Gr}(1,4)=\mathbb{P}^3,\quad
\operatorname{Gr}(2,4),\quad \dim4,\quad
\operatorname{Gr}(3,4)=\mathbb{P}^3 .
$$

**The idempotents are transverse pairs, not flags.** A rank-$p$ idempotent is a pair $(U,W)$ with

$$
U\oplus W=\mathbb{C}^4,\qquad \dim U=p,
$$

a **transverse** pair. A partial flag of type $(p,4-p)$ is a **nested** pair

$$
U\subset W,\qquad \dim U=p,\quad \dim W=4-p,
$$

which is a different object. The idempotent variety is the open subset of $\operatorname{Gr}(p,4)\times\operatorname{Gr}(4-p,4)$ where $U\cap W=0$, of dimension $2p(4-p)$; the partial flag variety is the closed incidence subset where $U\subset W$, of dimension $p(4-p)+(4-2p)p$ for $p\le2$. The two are different: the idempotent variety is affine and noncompact, while the partial flag variety is projective and compact. The product of Grassmannians is a compactification of the idempotent variety; the partial flag variety is a different closed subvariety of the product.

**The incidence relations.** The partial flag variety of type $(p,q)$ with $p<q$ is

$$
\mathcal{F}_{p,q}=\{(U,V):U\subset V,\ \dim U=p,\ \dim V=q\},
$$

of dimension

$$
p(4-p)+(q-p)(4-q).
$$

The full flag maps to it with fibres the product of the full flag varieties of the subquotients $U$, $V/U$ and $\mathbb{C}^4/V$. The standard incidence correspondences are the projections to the two Grassmannians; the fibres are Grassmannians of the subquotients. These are the nested-flag analogues of the transverse-pair bundle of the idempotents.

**The gauge as the fibre of the frame bundle.** The projection

$$
GL_4\longrightarrow\mathbb{P}^3,\qquad
S\longmapsto S e_1,
$$

is a principal bundle with fibre the parabolic stabiliser of the line. The maximal torus $T\cong(\mathbb{C}^\times)^3$ of $PGL_4$ is the gauge torus; the frame bundle over the root orbit,

$$
PGL_4\longrightarrow PGL_4/T,
$$

has fibre $T$, and the gauge is that fibre. The count is

$$
\underbrace{15}_{\text{frame group}}
=
\underbrace{12}_{\text{root orbit}}
+
\underbrace{3}_{\text{gauge}}.
$$

The idempotents $E_{ii}$ of a frame are the coordinate projections; the gauge rescales the frame and acts on the off-diagonal nilpotents, while the diagonal idempotents are invariant.

## The Biquaternion Case

**At $n=2$ the idempotents are simpler.** The rank-one idempotents of $M_2(\mathbb{C})$ form

$$
PGL_2/P(GL_1\times GL_1),
$$

of dimension

$$
2\cdot1\cdot1=2,
$$

an affine bundle of rank $1$ over $\mathbb{P}^1$. In a chart,

$$
P=\begin{pmatrix}1&a\\0&0\end{pmatrix},
\qquad a\in\mathbb{C},
$$

the image is the first coordinate line, and the kernel is the line $x_1+ax_2=0$. The orthogonal rank-one idempotents form $\mathbb{P}^1$.

**The rank-two case.** The identity is the only rank-two idempotent; the zero matrix is the only rank-zero idempotent. The rank-one idempotents are the two-dimensional family; the coarse Peirce corners are $1+1+1+1$.

**The comparison.** The full algebra has the affine bundles of ranks $3,4,3$ over $\mathbb{P}^3,\operatorname{Gr}(2,4),\mathbb{P}^3$; the biquaternion algebra has the affine bundle of rank $1$ over $\mathbb{P}^1$. The pattern is the same: the idempotents of rank $p$ form the affine bundle of complements over $\operatorname{Gr}(p,n)$, of dimension $2p(n-p)$.

## Summary

The idempotents of rank $p$ in $M_4(\mathbb{C})$ form the homogeneous space

$$
\mathcal{I}_p=PGL_4/P(GL_p\times GL_{4-p}),
\qquad
\dim_\mathbb{C}\mathcal{I}_p=2p(4-p).
$$

For $p=1$ this is an affine bundle of rank $3$ over $\mathbb{P}^3$, of dimension $6$; for $p=2$ it is an affine bundle of rank $4$ over $\operatorname{Gr}(2,4)$, of dimension $8$; for $p=3$ it is the dual affine bundle over $\mathbb{P}^3$, of dimension $6$. The fibre over a $p$-plane is the affine space of complements, of dimension $p(4-p)$, contractible; the orthogonal projections form the zero section $\operatorname{Gr}(p,4)$, and $\mathcal{I}_p$ is homotopy equivalent to $\operatorname{Gr}(p,4)$. The tangent space at $P$ is the sum of the two off-diagonal Peirce corners $\{X:XP+PX=X\}$, of dimension $2p(4-p)$; the rank strata are clopen components, with $\overline{\mathcal{I}_p}=\mathcal{I}_p$ because $\operatorname{rank}P=\operatorname{tr}P$ is locally constant. The full flag variety $GL_4/B$ has dimension $6$ and is simply connected; the idempotents are transverse pairs of a $p$-plane and a $(4-p)$-plane, not nested flags. The gauge torus $T\cong(\mathbb{C}^\times)^3$ is the fibre of the frame bundle over the root orbit, and $15=12+3$.

$$
\boxed{\ \dim_\mathbb{C}\mathcal{I}_p=2p(4-p),\quad \mathcal{I}_1\to\mathbb{P}^3\ \text{affine rank }3,\quad \mathcal{I}_p\simeq\operatorname{Gr}(p,4),\quad \dim_\mathbb{C}\mathcal{F}=6. }
$$

| Object | Complex dimension |
|---|---|
| $\mathcal{I}_0$ | $0$ |
| $\mathcal{I}_1$ | $6$ |
| $\mathcal{I}_2$ | $8$ |
| $\mathcal{I}_3$ | $6$ |
| $\mathcal{I}_4$ | $0$ |
| $\operatorname{Gr}(p,4)$ | $p(4-p)$ |
| Full flag variety | $6$ |
| Gauge torus | $3$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{I}_p$ | the idempotents of rank $p$ |
| $P(GL_p\times GL_{4-p})$ | the projective parabolic stabiliser, with Levi $GL_p\times GL_{4-p}$ |
| $\operatorname{Gr}(p,4)$ | the Grassmannian of $p$-planes |
| $\mathcal{F}=GL_4/B$ | the full flag variety |
| $T$ | the gauge torus |
| $B$ | the complement coordinate of an idempotent |

## Further Reading

- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the Grassmannians, the flag variety and the incidence relations.
- James E. Humphreys, *Linear Algebraic Groups* (Springer, 1975), for homogeneous spaces, parabolic subgroups and flag varieties.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for idempotents and Peirce decompositions.
- [The Peirce Decomposition](the-peirce-decomposition-of-m4c.html), for the corners of an idempotent.
- [The Rank-Two Split](the-rank-two-split-of-m4c.html), for the rank-two Peirce table.
- [The Adjoint Action, the Orbits and the Flag Variety](the-adjoint-action-the-orbits-and-the-flag-variety-of-m4c.html), for the orbits and the flag variety.
- [The Topology of $M_4(\mathbb{C})$](the-topology-of-m4c.html), for the homotopy equivalence $\mathcal{I}_p\simeq\operatorname{Gr}(p,4)$.
