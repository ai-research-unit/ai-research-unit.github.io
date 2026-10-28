# __The Topology of $M_3(\mathbb{C})$__

## Introduction

**The algebra $M_3(\mathbb{C})$ is homeomorphic to $\mathbb{R}^{18}$ and is contractible; its group of units $GL_3(\mathbb{C})$ is homotopy equivalent to the compact $*$-unitary group $U(3)$, with**

$$
\pi_1(GL_3)=\mathbb{Z},\qquad
\pi_2(GL_3)=0,\qquad
\pi_3(GL_3)=\mathbb{Z}.
$$

The determinant hypersurface $\det A=0$ is star-shaped around the origin, hence contractible, and its complement is $GL_3$. The space of idempotents of rank $p$ is homotopy equivalent to the Grassmannian $\operatorname{Gr}(p,3)$; for $p=1$ and $p=2$ this is $\mathbb{P}^{2}$, with $\pi_2=\mathbb{Z}$ and Euler characteristic $3$. The full flag variety $GL_3/B$ is simply connected, of real dimension $6$, with $\pi_2=\mathbb{Z}^{2}$ and Euler characteristic $6$. The determinant line bundle over $GL_3$ is trivial, with first Chern class $0$, although the determinant map itself induces an isomorphism on $\pi_1$; the nontrivial determinant bundles live over the Grassmannians and the flag variety.

The article computes the homotopy type of the algebra and the group, the homotopy groups and the cohomology of $U(3)$, the topology of the determinant hypersurface, the homotopy type of the idempotent varieties and the flag variety, and the first Chern classes of the determinant bundles. The polar decomposition is *The Polar Decomposition of $M_3(\mathbb{C})$*; the idempotent geometry is *The Geometry of the Idempotents of $M_3(\mathbb{C})$*; the frame and the gauge are *The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$*.

## The Algebra and the Group

**Theorem (contractibility).** $M_3(\mathbb{C})\cong\mathbb{R}^{18}$ is contractible.

**Proof.** The map $H(t,A)=(1-t)A$ is a deformation retraction of $M_3$ onto the origin. The identification with $\mathbb{R}^{18}$ is the real and imaginary parts of the nine entries.

**Theorem (polar retraction).** $GL_3(\mathbb{C})$ deformation retracts onto $U(3)$.

**Proof.** Write $A=UP$ with $U\in U(3)$ and $P$ positive definite, and define

$$
H(t,A)=U P^{1-t},\qquad 0\le t\le1 .
$$

The matrix $P^{1-t}$ is positive definite for every $t$, so the path stays in $GL_3$. At $t=0$ it is $UP=A$, and at $t=1$ it is $U$. The map is continuous because the polar factors are continuous on $GL_3$.

**Corollary.** $GL_3(\mathbb{C})$ and $U(3)$ have the same homotopy groups, homology and cohomology.

**The maximal compact subgroup.** $U(3)$ is a maximal compact subgroup of $GL_3(\mathbb{C})$, and $GL_3/U(3)\cong\operatorname{Herm}_{>0}(3)\cong\mathbb{R}^{9}$ is contractible. The quotient is the symmetric space of positive definite Hermitian matrices, of real dimension $9$.

**Proof.** The polar decomposition gives the diffeomorphism $GL_3\cong U(3)\times\operatorname{Herm}_{>0}(3)$, and the positive definite cone is convex, hence contractible.

## The Homotopy Groups

**Theorem.** The homotopy groups of $GL_3(\mathbb{C})$ begin

$$
\pi_0=0,\qquad
\pi_1=\mathbb{Z},\qquad
\pi_2=0,\qquad
\pi_3=\mathbb{Z}.
$$

**Proof of $\pi_1=\mathbb{Z}$.** The determinant map

$$
\det:U(3)\longrightarrow U(1)
$$

is surjective, and its fibre over $1$ is $SU(3)$. The group $SU(3)$ is simply connected, so the long exact sequence of the fibration gives

$$
\pi_1(U(3))\cong\pi_1(U(1))=\mathbb{Z}.
$$

The generator is the loop $t\mapsto\operatorname{diag}(e^{2\pi it},1,1)$.

**Proof of $\pi_2=0$.** The group $U(3)$ is a compact Lie group, and every Lie group has vanishing $\pi_2$. Equivalently, the fibration $U(2)\to U(3)\to U(3)/U(2)\cong S^{5}$ has $\pi_2(U(2))=0$ and $\pi_2(S^{5})=0$, so the long exact sequence gives $\pi_2(U(3))=0$.

**Proof of $\pi_3=\mathbb{Z}$.** The quotient $SU(3)/SU(2)\cong S^{5}$ is $4$-connected, so the long exact sequence of the fibration $SU(2)\to SU(3)\to S^{5}$ gives $\pi_3(SU(3))\cong\pi_3(SU(2))=\pi_3(S^{3})=\mathbb{Z}$. Since $U(3)$ is $SU(3)$ times a circle up to a finite central quotient, $\pi_3(U(3))=\mathbb{Z}$.

**The stable range.** For $k<2n$ the homotopy groups $\pi_k(U(n))$ stabilise to $\pi_k(U)$. For $n=3$ the stable values begin $\pi_1=\mathbb{Z}$, $\pi_2=0$, $\pi_3=\mathbb{Z}$.

**The cohomology.** The cohomology of $U(3)$ with integer coefficients is the exterior algebra

$$
H^{*}(U(3);\mathbb{Z})=\Lambda(x_1,x_3,x_5),
$$

on generators of degrees $1$, $3$ and $5$. Its Poincaré polynomial is

$$
P_{U(3)}(t)=(1+t)(1+t^{3})(1+t^{5})
=1+t+t^{3}+t^{4}+t^{5}+t^{6}+t^{8}+t^{9}.
$$

The Euler characteristic is $P(-1)=0$, as for every compact odd-dimensional Lie group. The total Betti number is $P(1)=8$.

**Proof.** The cohomology of $U(n)$ is the exterior algebra on generators of degrees $2k-1$ for $k=1,\dots,n$; this is the standard theorem of Borel. For $n=3$ the degrees are $1,3,5$.

## The Determinant Hypersurface

**Theorem.** The hypersurface

$$
\Sigma_0=\{A\in M_3(\mathbb{C}):\det A=0\}
$$

is contractible.

**Proof.** For $A\in\Sigma_0$ and $0\le t\le1$, the matrix $(1-t)A$ is singular, because its rank is at most the rank of $A$, which is at most $2$. The map $H(t,A)=(1-t)A$ is a deformation retraction of $\Sigma_0$ onto $0$. Hence $\Sigma_0$ is contractible.

**The complement.** The complement of $\Sigma_0$ is $GL_3(\mathbb{C})$, which is homotopy equivalent to $U(3)$ and has $\pi_1=\mathbb{Z}$.

**The pair.** Both $\Sigma_0$ and $M_3$ are contractible, so the inclusion $\Sigma_0\subset M_3$ is a homotopy equivalence. The interesting topology is carried by the complement, not by the hypersurface.

**The singular locus.** Inside $\Sigma_0$, the singular locus is the variety $\Sigma_1=\{A:\operatorname{rank}A\le1\}$, of complex dimension $5$ and real dimension $10$. It is also star-shaped around $0$, hence contractible; its complement in $\Sigma_0$ is the smooth part of the hypersurface, consisting of the matrices of rank exactly $2$.

**The rank stratification.** The rank stratification

$$
M_3=\Sigma_0\sqcup GL_3,
\qquad
\Sigma_0=\Sigma_1\sqcup\{\operatorname{rank}=2\}
$$

is a stratification by locally closed sets. The open stratum $GL_3$ has $\pi_1=\mathbb{Z}$; the closed stratum $\Sigma_0$ is contractible; the singular stratum $\Sigma_1$ is contractible.

**Proof of the dimension.** The rank-one matrices form the affine cone over $\mathbb{P}^{2}\times\mathbb{P}^{2}$, of dimension $5$; the rank-zero matrix is the apex. The rank-two matrices form the smooth part of the determinant hypersurface, of complex dimension $8$.

## The Idempotent Varieties

**Theorem.** The variety $\mathcal{E}_p$ of idempotents of rank $p$ is homotopy equivalent to the Grassmannian $\operatorname{Gr}(p,3)$.

**Proof.** The map $\pi:\mathcal{E}_p\to\operatorname{Gr}(p,3)$, $E\mapsto\operatorname{im}E$, is a fibre bundle whose fibre over a $p$-plane $V$ is the affine space of complements to $V$, of dimension $p(3-p)$, hence contractible. Explicitly, let $P_V$ be the orthogonal projection onto $V=\operatorname{im}E$; it is continuous in $E$, and $P_V=E(E^{*}E)^{+}E^{*}$. The linear homotopy $E_t=(1-t)E+tP_V$ is idempotent because $EP_V=P_V$ and $P_VE=E$, so $E_t^{2}=(1-t)E+tP_V=E_t$; it contracts $\mathcal{E}_p$ onto the set of orthogonal projections, which is $\operatorname{Gr}(p,3)$.

**The values.** For $p=0$ and $p=3$ the Grassmannian is a point and the idempotent variety is a point. For $p=1$ and $p=2$,

$$
\mathcal{E}_1\simeq\mathbb{P}^{2}\simeq\mathcal{E}_2 .
$$

**The homotopy groups.** For $p=1$,

$$
\pi_1(\mathcal{E}_1)=0,\qquad
\pi_2(\mathcal{E}_1)=\mathbb{Z},\qquad
\pi_3(\mathcal{E}_1)=0,
$$

and the same holds for $p=2$.

**Proof.** The Grassmannian $\operatorname{Gr}(1,3)=\mathbb{P}^{2}$ has the cell decomposition $\mathbb{P}^{2}=S^{2}\cup e^{4}$, so $\pi_1=0$, $\pi_2=\mathbb{Z}$ and $\pi_3=0$; the last vanishing follows from the fibration $S^{1}\to S^{5}\to\mathbb{P}^{2}$ and $\pi_3(S^{5})=\pi_3(S^{1})=0$.

**The cohomology.** The cohomology of $\mathbb{P}^{2}$ is

$$
H^{*}(\mathbb{P}^{2};\mathbb{Z})=\mathbb{Z}[h]/(h^{3}),
\qquad \deg h=2,
$$

with Betti numbers $1,0,1,0,1$ and Euler characteristic $3$. The idempotent variety has the same cohomology.

**The compact models.** The idempotent variety is not compact, but it is homotopy equivalent to the Grassmannian, which is compact. The rank-one idempotents with image $L$ retract onto the orthogonal projection onto $L$, the unique idempotent with kernel $L^{\perp}$; the fibre is the affine space of complements to $L$, and the retraction contracts it to the orthogonal complement.

## The Flag Variety

**Theorem.** The full flag variety $\operatorname{Flags}=GL_3/B$ is a simply connected compact complex manifold of complex dimension $3$ and real dimension $6$, with

$$
\pi_1(\operatorname{Flags})=0,\qquad
\pi_2(\operatorname{Flags})=\mathbb{Z}^{2},\qquad
\chi(\operatorname{Flags})=6 .
$$

Its Betti numbers are $1,0,2,0,2,0,1$ in real degrees $0,1,\dots,6$.

**Proof.** The flag variety is $U(3)/T$ with $T$ the maximal torus, because $U(3)$ acts transitively on the flags and the stabiliser of the standard flag is the diagonal torus. The long exact sequence of $\pi_1(T)\to\pi_1(U(3))\to\pi_1(U(3)/T)\to\pi_0(T)$ is $\mathbb{Z}^{3}\to\mathbb{Z}\to\pi_1(\mathrm{Flags})\to0$, and the first map is the sum of the three coordinates, which is surjective; hence $\pi_1(\mathrm{Flags})=0$. The same fibration with $\pi_2(U(3))=0$ gives $\pi_2(\mathrm{Flags})\cong\ker(\mathbb{Z}^{3}\to\mathbb{Z})=\mathbb{Z}^{2}$. The Euler characteristic is the order of the Weyl group, $|S_3|=6$. The Betti numbers follow from the Schubert cell decomposition: one cell in real dimension $0$, two in dimension $2$, two in dimension $4$, and one in dimension $6$.

**The Schubert cells.** The cells are indexed by the permutations of three letters; the length of the permutation is the complex dimension of the cell. The six permutations have lengths

$$
0,\ 1,\ 1,\ 2,\ 2,\ 3,
$$

which gives the Poincaré polynomial

$$
P_{\operatorname{Flags}}(t)=1+2t^{2}+2t^{4}+t^{6},
\qquad P_{\operatorname{Flags}}(1)=6 .
$$

**The incidence bundle.** The map $\operatorname{Flags}\to\mathbb{P}^{2}$, $(L,V)\mapsto L$, is a $\mathbb{P}^{1}$-bundle, and so is the map to $\mathbb{P}^{2}$ sending $(L,V)$ to $V$. The first is the projectivisation of the tautological quotient bundle $Q=\mathbb{C}^{3}/S$, with fibre $\mathbb{P}(\mathbb{C}^{3}/L)$; the second is the projectivisation of the tautological subbundle $S$, with fibre $\mathbb{P}(V)$. The flag variety is the incidence variety of a point in a plane in $\mathbb{P}^{2}$.

**The relation to the idempotents.** The flag variety is the image of the incidence variety of pairs of idempotents $E\le F$ of ranks $1$ and $2$: the pair maps to the flag $(\operatorname{im}E,\operatorname{im}F)$. The map is surjective, and the fibres are the choices of complementary kernels. The flag variety is the compact base that records the incidence.

## The Determinant Bundles

**The determinant over $GL_3$.** The determinant is a holomorphic map

$$
\det:GL_3(\mathbb{C})\longrightarrow\mathbb{C}^{\times},
$$

and it induces an isomorphism on $\pi_1$: both groups are $\mathbb{Z}$, and the loop $\operatorname{diag}(e^{2\pi it},1,1)$ maps to $e^{2\pi it}$.

**Theorem.** The determinant line bundle $L=GL_3\times_{\det}\mathbb{C}$ associated to the character $\det$ is trivial, and its first Chern class is zero.

**Proof.** $GL_3$ is homotopy equivalent to $U(3)$, and $H^{2}(U(3);\mathbb{Z})=0$ because the cohomology is exterior on generators of degrees $1,3,5$. Line bundles on a space are classified by $H^{2}(X;\mathbb{Z})$, so every line bundle on $GL_3$ is trivial. The determinant map is nontrivial on $\pi_1$, but its associated line bundle is topologically trivial.

**The determinant over the Grassmannian.** The tautological subbundle $S$ over $\operatorname{Gr}(p,3)$ has a determinant line bundle $\det S$. For $\operatorname{Gr}(1,3)=\mathbb{P}^{2}$,

$$
\det S=\mathcal{O}(-1),
\qquad
c_1(\det S)=-h,
$$

where $h$ is the hyperplane class generating $H^{2}(\mathbb{P}^{2};\mathbb{Z})\cong\mathbb{Z}$. For $\operatorname{Gr}(2,3)$ the same formula holds with the dual convention, and $c_1$ generates $H^{2}$.

**The determinant over the flag variety.** The flag variety has a filtration of tautological bundles

$$
0\subset S_1\subset S_2\subset\mathbb{C}^{3},
\qquad \operatorname{rank}S_i=i .
$$

The line bundles $L_i=S_i/S_{i-1}$ have first Chern classes $c_1(L_i)$ that span $H^{2}(\operatorname{Flags};\mathbb{Z})\cong\mathbb{Z}^{2}$, and

$$
c_1(L_1)+c_1(L_2)+c_1(L_3)=0,
$$

because the determinant of the trivial bundle is trivial. The two simple Schubert divisor classes are $c_1(L_1)$ and $c_1(L_2)$, and $c_1(L_3)=-(c_1(L_1)+c_1(L_2))$.

**Proof.** The filtration is the tautological filtration of the flag; the quotient $L_i$ is a line bundle. The determinant of the direct sum $\bigoplus_iL_i\cong\mathbb{C}^{3}$ is trivial, so the sum of the first Chern classes is zero. The classes generate because the line bundles $L_i$ generate the Picard group of the flag variety, of rank $2$.

## Summary

The algebra $M_3(\mathbb{C})$ is $\mathbb{R}^{18}$ and is contractible. The group $GL_3(\mathbb{C})$ deformation retracts onto $U(3)$ by the polar decomposition, so the two have the same homotopy type; $\pi_1(GL_3)=\mathbb{Z}$, $\pi_2(GL_3)=0$, and $\pi_3(GL_3)=\mathbb{Z}$. The cohomology of $U(3)$ is the exterior algebra $\Lambda(x_1,x_3,x_5)$, with Poincaré polynomial $(1+t)(1+t^{3})(1+t^{5})$ and Euler characteristic $0$. The determinant hypersurface $\det A=0$ is star-shaped around the origin and contractible; its singular locus, the rank-at-most-one variety, is also contractible. The idempotent variety of rank $p$ is homotopy equivalent to $\operatorname{Gr}(p,3)$; for $p=1,2$ this is $\mathbb{P}^{2}$, with $\pi_1=0$, $\pi_2=\mathbb{Z}$, $\pi_3=0$ and Euler characteristic $3$. The full flag variety $GL_3/B\cong U(3)/T$ is simply connected, of real dimension $6$, with $\pi_2=\mathbb{Z}^{2}$, Betti numbers $1,0,2,0,2,0,1$ and Euler characteristic $6$. The determinant line bundle over $GL_3$ is trivial with $c_1=0$; over the Grassmannians the determinant of the tautological subbundle has $c_1=-h$, generating $H^{2}\cong\mathbb{Z}$; over the flag variety the three tautological quotient lines span $H^{2}\cong\mathbb{Z}^{2}$ with the relation $c_1(L_1)+c_1(L_2)+c_1(L_3)=0$.

$$
\boxed{\ M_3\simeq *,\quad GL_3\simeq U(3),\quad \pi_1=\mathbb{Z},\ \pi_2=0,\ \pi_3=\mathbb{Z},\quad \det\nolimits^{-1}(0)\simeq *,\quad \mathcal{E}_p\simeq\operatorname{Gr}(p,3),\quad \operatorname{Flags}\simeq U(3)/T,\ \chi=6.\ }
$$

| Space | Homotopy type | $\pi_1$ | $\pi_2$ | Euler characteristic |
|---|---|---|---|---|
| $M_3(\mathbb{C})$ | point | $0$ | $0$ | $1$ |
| $\det=0$ | point | $0$ | $0$ | $1$ |
| $GL_3(\mathbb{C})$ | $U(3)$ | $\mathbb{Z}$ | $0$ | $0$ |
| $\mathcal{E}_1\simeq\mathcal{E}_2$ | $\mathbb{P}^{2}$ | $0$ | $\mathbb{Z}$ | $3$ |
| $\operatorname{Flags}$ | $U(3)/T$ | $0$ | $\mathbb{Z}^{2}$ | $6$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{E}_p$ | idempotents of rank $p$ |
| $\operatorname{Gr}(p,3)$ | Grassmannian of $p$-planes |
| $\operatorname{Flags}$ | full flag variety $GL_3/B$ |
| $B$ | Borel subgroup of upper triangular matrices |
| $T$ | maximal torus of $U(3)$ |
| $S$ | tautological subbundle |
| $L_i$ | tautological quotient line $S_i/S_{i-1}$ |
| $h$ | hyperplane class of $\mathbb{P}^{2}$ |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge, 2002), for the homotopy groups, the fibrations and the cohomology of homogeneous spaces.
- Raoul Bott and Loring Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the cohomology of $U(n)$ and the flag varieties.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Grassmannians, the flag varieties and the determinant bundles.
- [The Geometry of the Idempotents of $M_3(\mathbb{C})$](the-geometry-of-the-idempotents-of-m3c.html), for the affine bundle and the flag incidence.
- [The Polar Decomposition of $M_3(\mathbb{C})$](the-polar-decomposition-of-m3c.html), for the deformation retraction onto $U(3)$.
- [The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-m3c.html), for the gauge torus.
