# __The Adjoint Action, the Orbits and the Flag Variety of $M_3(\mathbb{C})$__

## Introduction

**The projective group $PGL_3(\mathbb{C})$ acts on $M_3(\mathbb{C})$ by conjugation, and its orbits are the conjugacy classes, classified by the Jordan type.** The orbit of a regular element, with three distinct eigenvalues, has dimension $6$, and its stabiliser is the maximal torus $(\mathbb{C}^{\times})^{2}$, of dimension $2$; the count is $8=6+2$. The orbit of a scalar is a point, with stabiliser the whole group. The nilpotent orbits are the zero orbit, the minimal orbit of dimension $4$ and the principal orbit of dimension $6$. The full flag variety $GL_3/B$ has dimension $3$; the Grassmannians $\operatorname{Gr}(1,3)=\mathbb{P}^{2}$ and $\operatorname{Gr}(2,3)$ have dimension $2$; the gauge torus is the fibre of the frame bundle over the root orbit.

The article defines the action, classifies the orbits by the Jordan type and computes their dimensions by the orbit–stabiliser theorem, treats the regular elements and the gauge, describes the nilpotent orbits and their closures, and identifies the flag variety and the Grassmannians as the natural quotients of the group. Every dimension is computed twice: from the centraliser and from the geometry of the flags.

The Jordan form is *Spectral Theory and the Spectral Projectors of $M_3(\mathbb{C})$*; the spectral strata by root multiplicity are *The Cubic, the Discriminant and the Spectral Strata of $M_3(\mathbb{C})$*; the root and its gauge are *The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$*; the geometry of the idempotents is *The Geometry of the Idempotents of $M_3(\mathbb{C})$*; the topology is *The Topology of $M_3(\mathbb{C})$*.

## The Conjugation Action

**Definition.** The group $GL_3(\mathbb{C})$ acts on $M_3(\mathbb{C})$ by

$$
S\cdot A=SAS^{-1}.
$$

The scalar matrices act trivially, because $\lambda I$ commutes with every $A$; so the action factors through

$$
PGL_3(\mathbb{C})=GL_3(\mathbb{C})/\mathbb{C}^{\times}I\cong SL_3(\mathbb{C})/\mu_3,
$$

of complex dimension $8$.

**Proposition.** The action is algebraic, and the orbit of $A$ is its conjugacy class

$$
\mathcal{O}(A)=\{SAS^{-1}:S\in GL_3\}.
$$

**Proof.** The map $(S,A)\mapsto SAS^{-1}$ is a morphism of affine varieties, because the entries of $SAS^{-1}$ are rational functions with denominator $\det S$, which is nowhere zero on $GL_3$. The orbit is the image of the morphism $S\mapsto SAS^{-1}$, and the stabiliser is a closed subgroup; the orbit is therefore a locally closed subvariety, smooth because it is a homogeneous space.

**The invariants.** The characteristic polynomial, and hence the trace, the second elementary symmetric function and the determinant, is constant on an orbit:

$$
\chi_{SAS^{-1}}(t)=\det(tI-SAS^{-1})=\det(S(tI-A)S^{-1})=\chi_A(t).
$$

The converse holds in the following sense: two matrices with the same Jordan form are conjugate, and the Jordan form is determined by the characteristic polynomial together with the ranks of the powers $A-\lambda I$. So the orbits are exactly the Jordan types.

**The tangent space.** The differential of the orbit map at the identity is $X\mapsto [X,A]=XA-AX$, so the tangent space at $A$ is the image of $\operatorname{ad}_A$,

$$
T_A\mathcal{O}(A)=\{[X,A]:X\in M_3\},
$$

of dimension $9-\dim Z(A)$, where $Z(A)$ is the centraliser. In the projective group the same image is obtained, because the scalars act trivially; the dimension is $8-(\dim Z(A)-1)=9-\dim Z(A)$.

**Worked example.** Take

$$
A=\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix}.
$$

Its trace is $15$, and its characteristic polynomial is

$$
\chi_A(t)=t^{3}-15t^{2}-18t,
$$

with eigenvalues $0$ and $(15\pm\sqrt{297})/2$, three distinct numbers. The centraliser is the algebra $\mathbb{C}[A]$, of dimension $3$, so the orbit has dimension $9-3=6$ and the stabiliser in $PGL_3$ has dimension $8-6=2$. The stabiliser is the torus of matrices that are diagonal in the eigenbasis of $A$.

## The Jordan Types

**The classification.** Two matrices are conjugate exactly when they have the same Jordan form. For $3\times3$ matrices the possible Jordan types are the following, listed by the partition of the size and the coincidences of the eigenvalues.

| Jordan type | Partition | $\dim Z(A)$ | $\dim\mathcal{O}$ in $PGL_3$ |
|---|---|---|---|
| scalar $aI$ | $1+1+1$ with one eigenvalue | $9$ | $0$ |
| semisimple, two eigenvalues | $2+1$ | $5$ | $4$ |
| semisimple, three eigenvalues | $1+1+1$ | $3$ | $6$ |
| one $2$-block and one $1$-block, distinct eigenvalues | $2+1$ | $3$ | $6$ |
| one $3$-block | $3$ | $3$ | $6$ |
| nilpotent $E_{12}$ | $2+1$ | $5$ | $4$ |
| principal nilpotent | $3$ | $3$ | $6$ |
| zero | $1+1+1$ | $9$ | $0$ |

The semisimple type with two eigenvalues and the nilpotent type $E_{12}$ share the partition $2+1$ and the centraliser dimension $5$; they are different orbits of the same dimension. The scalar and the zero matrix are the two closed orbits, each a single point.

**Theorem.** The orbit of $A$ has dimension $9-\dim Z(A)$, where

$$
\dim Z(A)=\sum_{i,j}\min(d_i,d_j)
$$

summed over the pairs of Jordan blocks of $A$ with the same eigenvalue, $d_i$ the block sizes. In $PGL_3$ the dimension is the same number, because the centre is one-dimensional and is contained in every centraliser.

**Proof.** The orbit–stabiliser theorem for the algebraic group action gives $\dim\mathcal{O}=\dim GL_3-\dim Z(A)=9-\dim Z(A)$; in the projective group, $\dim PGL_3-\dim(Z(A)/\mathbb{C}^{\times}I)=8-(\dim Z(A)-1)=9-\dim Z(A)$. The centraliser dimension is computed block by block: a matrix commuting with a Jordan block of size $d$ is Toeplitz on that block, and a block mapping a block of size $d_i$ to a block of size $d_j$ is determined by $\min(d_i,d_j)$ parameters. Blocks with different eigenvalues do not interact.

**The closures.** The closure of an orbit is a union of orbits, and the order is the degeneration order of the Jordan type. The scalar orbit is closed, and so is the zero orbit. The orbit of the semisimple type with two eigenvalues contains, in its closure, the scalar orbit: degenerate the difference of the two eigenvalues to zero. The orbit of the type $2+1$ with distinct eigenvalues contains the nilpotent $E_{12}$ orbit and the scalar orbit. The principal nilpotent orbit contains the minimal nilpotent orbit and the zero orbit in its closure; its closure is the whole nilpotent cone.

**Worked example: the minimal nilpotent orbit.** Let $N=E_{12}$. The equation $XN=NX$ leaves the five entries

$$
Z(N)=\left\{\begin{pmatrix}a&b&c\\0&a&0\\0&d&e\end{pmatrix}\right\},
$$

of dimension $5$. The orbit has dimension $9-5=4$. It is the set of rank-one nilpotent matrices, equivalently the set of matrices $u\varphi$ with $\varphi(u)=0$ and $u\neq0$. The parameters are $u\in\mathbb{C}^{3}\smallsetminus\{0\}$ (three dimensions) and $\varphi\in u^{\perp}$ (two dimensions), modulo the scaling $(u,\varphi)\mapsto(\lambda u,\lambda^{-1}\varphi)$ (one dimension), so the dimension is $3+2-1=4$. Projectively the orbit is the incidence variety of pairs $([u],[\varphi])$ with $u\in\ker\varphi$, of dimension $3$; the orbit is the affine cone over it.

**Worked example: the principal nilpotent orbit.** Let $N=E_{12}+E_{23}$. The centraliser is the algebra of polynomials in $N$,

$$
Z(N)=\{aI+bN+cN^{2}\},
$$

of dimension $3$, so the orbit has dimension $6$. The orbit is the set of nilpotent matrices with a single Jordan block. The two nilpotent orbits have dimensions $4$ and $6$, and their closures meet only at $0$.

## The Regular Elements

**Definition.** An element $A\in M_3$ is **regular** when its minimal polynomial has degree $3$, equivalently when its centraliser has dimension $3$, equivalently when it is cyclic: there is a vector $v$ with $v,Av,A^{2}v$ a basis.

**Theorem.** For a regular element the centraliser is the algebra $\mathbb{C}[A]$, of dimension $3$, and the orbit has dimension $6$. The stabiliser in $PGL_3$ is the maximal torus of the frame, of dimension $2$ when the eigenvalues are distinct.

**Proof.** If $A$ is cyclic with cyclic vector $v$, any $X$ commuting with $A$ is determined by $Xv$, because $X(A^{k}v)=A^{k}Xv$. The centraliser is the image of $\mathbb{C}[t]\to M_3$, $t\mapsto A$, which is three-dimensional because the minimal polynomial has degree $3$ and $I,A,A^{2}$ are independent. The orbit has dimension $9-3=6$. The stabiliser in $PGL_3$ is the image of $\mathbb{C}[A]^{\times}$, which is the torus $(\mathbb{C}^{\times})^{3}/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^{2}$ when $A$ has three distinct eigenvalues. For the regular nilpotent the units are $a I+bN+cN^{2}$ with $a\neq0$, a three-dimensional group whose image in $PGL_3$ is two-dimensional.

**The regular semisimple case.** When the three eigenvalues are distinct, the centraliser is the diagonal torus in the eigenbasis, and the stabiliser in $PGL_3$ is $(\mathbb{C}^{\times})^{2}$. The orbit is the set of matrices with the given characteristic polynomial and simple spectrum; it is the complement of the discriminant hypersurface inside the affine hypersurface $\{\chi_A=\chi\}$, of dimension $6$.

**The gauge.** The root $H$, with $H^{3}=I$ and simple spectrum, is a regular semisimple element. Its orbit is the set of roots, of dimension $6$, and its stabiliser is the gauge torus $T\cong(\mathbb{C}^{\times})^{2}$. The frame bundle

$$
PGL_3\longrightarrow PGL_3/T\cong X,\qquad [S]\longmapsto SHS^{-1},
$$

has fibre $T$ over the root, and the gauge is the fibre. This is the orbit–stabiliser count $8=6+2$ of *The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$*, read as a principal bundle.

**Worked example.** For $H=\operatorname{diag}(1,\omega,\omega^{2})$ the stabiliser in $GL_3$ is the diagonal torus $(\mathbb{C}^{\times})^{3}$, of dimension $3$; in $PGL_3$ it is the image, of dimension $2$. The orbit is $GL_3/T$, of dimension $6$, and the map $S\mapsto SHS^{-1}$ is the quotient map. The fibre over $H$ is the set of $S$ that commute with $H$, which is $T$ itself.

## The Nilpotent Orbits

**The nilpotent cone.** The nilpotent elements are those with all eigenvalues zero, equivalently $\chi_A(t)=t^{3}$, equivalently

$$
\operatorname{tr}A=\operatorname{tr}A^{2}=\det A=0.
$$

These are three polynomial equations, and the cone has dimension $9-3=6$. It is the zero set of the three coefficients of the characteristic polynomial, and it is irreducible, because it is the closure of the conjugacy class of a principal nilpotent.

**The orbits.** The nilpotent orbits are the zero orbit $\{0\}$, of dimension $0$; the minimal orbit, the rank-one nilpotent matrices, of dimension $4$; and the principal orbit, the rank-two nilpotent matrices, of dimension $6$. There are exactly three, because the nilpotent Jordan types in size $3$ are the partitions $1+1+1$, $2+1$ and $3$.

**Proof.** A nilpotent matrix has a Jordan form with blocks of size at most $3$ and eigenvalue $0$; the partitions of $3$ are the three listed. The dimensions are computed from the centralisers: $9$, $5$ and $3$. The rank-one nilpotents are exactly the matrices $u\varphi$ with $\varphi(u)=0$ and $u\neq0$; the rank-two nilpotents are the matrices whose cube is zero but whose square is not.

**The closure order.** The zero orbit lies in the closure of both nonzero orbits. The minimal orbit lies in the closure of the principal orbit: a principal nilpotent degenerates, along a parameter, to a rank-one nilpotent. The principal orbit does not lie in the closure of the minimal one, by dimension. So

$$
\{0\}\subset\overline{\mathcal{O}}_{\min}\subset\overline{\mathcal{O}}_{\mathrm{princ}},
$$

and the nilpotent cone is the union of the three orbits.

**The principal orbit and the carrier.** A principal nilpotent $N$ has a cyclic vector $v$ with $v,Nv,N^{2}v$ a basis; the triple is the **Jordan chain**. The chain is the carrier $\mathbb{C}^{3}$ read with the action of $N$, and the raising operator of *The Triplet: Spin One and the Adjoint $1+3+5$* is read in this basis. The principal orbit is the open dense orbit in the nilpotent cone, and its dimension $6$ is the dimension of the cone.

**Worked example.** For $N=E_{12}+E_{23}$ the vector $e_{1}$ is cyclic: $e_{1},Ne_{1}=e_{2},N^{2}e_{1}=e_{3}$ is the standard basis. The centraliser is $\{aI+bN+cN^{2}\}$, of dimension $3$. The orbit has dimension $6$ and is the set of nilpotents of rank two, an open dense subset of the nilpotent cone.

## The Flag Variety

**The Borel subgroup.** The **Borel subgroup** $B\subset GL_3$ is the group of invertible upper triangular matrices,

$$
B=\left\{\begin{pmatrix}b_{11}&b_{12}&b_{13}\\0&b_{22}&b_{23}\\0&0&b_{33}\end{pmatrix}:b_{ii}\neq0\right\},
$$

of dimension $6$: three diagonal parameters and three upper entries.

**The full flag variety.** The quotient $\mathcal{F}=GL_3/B$ is the **full flag variety**, the set of flags

$$
0\subset L_1\subset L_2\subset\mathbb{C}^{3},
\qquad
\dim L_1=1,\quad\dim L_2=2.
$$

Its dimension is

$$
\dim\mathcal{F}=9-6=3,
$$

and in the projective group it is $PGL_3/B'$ with $\dim B'=5$, again of dimension $3$.

**Proof.** $GL_3$ acts transitively on the flags: any flag can be carried to the standard flag $\langle e_{1}\rangle\subset\langle e_{1},e_{2}\rangle$ by a change of basis. The stabiliser of the standard flag is the group of upper triangular matrices, because such a matrix preserves $\langle e_{1}\rangle$ exactly when its first column is a multiple of $e_{1}$, and preserves $\langle e_{1},e_{2}\rangle$ exactly when its third column has zero entries in the first two rows. The quotient is therefore the flag variety, and the dimension is $9-6=3$.

**The Grassmannians.** The partial flag varieties are the quotients by the parabolic subgroups: $\operatorname{Gr}(1,3)=GL_3/P_1=\mathbb{P}^{2}$, of dimension $2$; $\operatorname{Gr}(2,3)=GL_3/P_2$, the dual projective plane, of dimension $2$; and $\mathcal{F}=GL_3/B$, of dimension $3$. The two Grassmannians are isomorphic, because a line in $\mathbb{C}^{3}$ is the same as a plane in the dual, but they are distinct as quotients: $P_1$ is the stabiliser of a line, $P_2$ the stabiliser of a plane. The incidence variety

$$
\{(L,\Pi):L\subset\Pi\}\subset\mathbb{P}^{2}\times\mathbb{P}^{2}
$$

has dimension $3$: it is the full flag variety, and the two projections to $\mathbb{P}^{2}$ are the forgetful maps.

**The fibration.** The map $\mathcal{F}\to\operatorname{Gr}(1,3)$ forgets the plane and keeps the line; its fibre over $L$ is the projective line $\mathbb{P}(\mathbb{C}^{3}/L)\cong\mathbb{P}^{1}$, of dimension $1$. The dimension count is $2+1=3$. Similarly, the map to $\operatorname{Gr}(2,3)$ forgets the line and keeps the plane, with fibre $\mathbb{P}^{1}$.

**The root orbit and the flag.** A root $H$ with simple spectrum determines an ordered triple of eigenlines $(\ell_{1},\ell_{2},\ell_{3})$, hence the flag $\ell_{1}\subset\ell_{1}\oplus\ell_{2}$. The map from the root orbit $PGL_3/T$ to $\mathcal{F}=PGL_3/B$ is the quotient by the Borel subgroup, with fibre $B/T$ of dimension $5-2=3$. The dimension count is $6=3+3$, the same count as $X\to U\to\mathcal{F}$ of *Roots of Unity and the Lagrange Idempotents of $M_3(\mathbb{C})$*, where $U$ is the unordered triple of lines.

## The Orbit–Stabiliser Count

**The theorem.** For an algebraic group $G$ acting on a variety with stabiliser $G_x$,

$$
\dim G=\dim\mathcal{O}(x)+\dim G_x .
$$

For $G=PGL_3$, of dimension $8$, the count for the regular semisimple orbit is

$$
8=6+2,
$$

with $\mathcal{O}$ the root orbit and $G_x=T$ the gauge torus. For the scalar orbit it is $8=0+8$; for the semisimple type $2+1$ it is $8=4+4$; for the principal nilpotent it is $8=6+2$; for the minimal nilpotent it is $8=4+4$.

**The gauge as the fibre.** The count $8=6+2$ says that the frame bundle $PGL_3\to X$ has fibre the torus $T$. The gauge group of *The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$* is exactly this fibre, and the two gauge parameters $\lambda_{1},\lambda_{2}$ are coordinates on it. The composite nilpotent $E_{13}$ carries the product $\lambda_{1}\lambda_{2}$ because the fibre is a group: the product in $T$ is the product of the two weights.

**The dimensions in one table.**

| Space | Group | Stabiliser | Dimension |
|---|---|---|---|
| $M_3$ | $PGL_3$ | — | $9$ |
| regular orbit | $PGL_3$ | $T$ | $6$ |
| semisimple $2+1$ orbit | $PGL_3$ | $GL_2\times GL_1/\mathbb{C}^{\times}$ | $4$ |
| principal nilpotent orbit | $PGL_3$ | $\mathbb{C}^{\times}\ltimes\mathbb{C}^{2}$ | $6$ |
| minimal nilpotent orbit | $PGL_3$ | $P_{2}$ | $4$ |
| full flag variety | $PGL_3$ | $B$ | $3$ |
| $\operatorname{Gr}(1,3)$ | $PGL_3$ | $P_{1}$ | $2$ |
| $\operatorname{Gr}(2,3)$ | $PGL_3$ | $P_{2}$ | $2$ |

The full flag variety has dimension $3$ and the principal nilpotent orbit dimension $6$. The coincidence $6=3+3$ is the fibration of the flag over the projective plane with fibre a projective line.

## Worked Example: Conjugation and Invariants

Take

$$
A=\begin{pmatrix}2&1&0\\0&2&1\\0&0&3\end{pmatrix},
\qquad
\chi_{A}(t)=(t-2)^{2}(t-3)=t^{3}-7t^{2}+16t-12 .
$$

The trace is $7$, the second coefficient is $16$, the determinant is $12$. The eigenvalues are $2$ (with a $2$-block) and $3$ (with a $1$-block); the centraliser consists of the upper Toeplitz block on the $2$-block, two parameters, and the scalar on the $1$-block, one parameter, so $\dim Z(A)=3$. The orbit has dimension $9-3=6$, and the stabiliser in $PGL_3$ has dimension $2$.

Conjugate by the diagonal matrix $S=\operatorname{diag}(1,2,1)$. Then

$$
SAS^{-1}=\begin{pmatrix}2&\tfrac12&0\\0&2&2\\0&0&3\end{pmatrix},
$$

because $(SAS^{-1})_{ij}=s_{i}a_{ij}s_{j}^{-1}$. The off-diagonal entries have moved, while

$$
\operatorname{tr}(SAS^{-1})=2+2+3=7,\qquad
\det(SAS^{-1})=2\cdot2\cdot3=12,
$$

and the characteristic polynomial is unchanged. This is the concrete form of the invariance: the entries are not conjugacy invariants, the coefficients of the cubic are.

## Summary

$PGL_3(\mathbb{C})$ acts on $M_3(\mathbb{C})$ by conjugation, of dimension $8$, and the orbits are the conjugacy classes, classified by the Jordan type. The regular semisimple orbit has dimension $6$ and stabiliser the maximal torus $(\mathbb{C}^{\times})^{2}$, so $8=6+2$; the gauge is the fibre of the frame bundle over the root orbit. The semisimple type $2+1$ and the minimal nilpotent orbit have dimension $4$; the scalar orbit has dimension $0$; the principal nilpotent orbit has dimension $6$. The nilpotent cone has dimension $6$ and three orbits, of dimensions $0,4,6$. The full flag variety $GL_3/B$ has dimension $3$, the Grassmannians $\operatorname{Gr}(1,3)=\mathbb{P}^{2}$ and $\operatorname{Gr}(2,3)$ have dimension $2$, and the flag is an incidence variety fibred over either Grassmannian with fibre $\mathbb{P}^{1}$. The root orbit maps to the flag variety with fibre $B/T$ of dimension $3$, and the dimension count $6=3+3$ is the orbit–stabiliser count read on the flag.

$$
\boxed{\ \dim PGL_3=8;\quad \dim\mathcal{O}_{\mathrm{reg}}=6,\ \operatorname{Stab}=T,\ 8=6+2;\quad \dim\mathcal{F}=3;\quad \dim\operatorname{Gr}(1,3)=\dim\operatorname{Gr}(2,3)=2.\ }
$$

| Orbit | Dimension | Stabiliser dimension |
|---|---|---|
| scalar | $0$ | $8$ |
| semisimple $2+1$ | $4$ | $4$ |
| regular semisimple | $6$ | $2$ |
| nilpotent $E_{12}$ | $4$ | $4$ |
| principal nilpotent | $6$ | $2$ |
| zero | $0$ | $8$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{O}(A)$ | the conjugacy class of $A$ |
| $Z(A)$ | the centraliser of $A$ |
| $B$ | the Borel subgroup of upper triangular matrices |
| $\mathcal{F}=GL_3/B$ | the full flag variety |
| $\operatorname{Gr}(p,3)$ | the Grassmannian of $p$-planes |
| $T$ | the maximal torus, the gauge |
| $\mathcal{N}$ | the nilpotent cone |

## Further Reading

- James E. Humphreys, *Linear Algebraic Groups* (Springer, 1975), for the Borel subgroup, the flag variety and the orbit–stabiliser theorem.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the Jordan form and the centraliser of a matrix.
- David Collingwood and William McGovern, *Nilpotent Orbits in Semisimple Lie Algebras* (Van Nostrand Reinhold, 1993), for the nilpotent orbits and their closures.
- [The Cubic, the Discriminant and the Spectral Strata of $M_3(\mathbb{C})$](the-cubic-the-discriminant-and-the-spectral-strata-of-m3c.html), for the spectral strata.
- [The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-m3c.html), for the gauge torus.
- [The Geometry of the Idempotents of $M_3(\mathbb{C})$](the-geometry-of-the-idempotents-of-m3c.html), for the idempotent varieties and the flag variety.
- [The Topology of $M_3(\mathbb{C})$](the-topology-of-m3c.html), for the homotopy type of the flag variety.
