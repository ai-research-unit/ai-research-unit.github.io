# __The Geometry of the Idempotents of $M_3(\mathbb{C})$__

## Introduction

**The idempotents of rank one form an affine bundle of rank $2$ over $\mathbb{P}^{2}$, of complex dimension $4$; the idempotents of rank $p$ form the homogeneous space $PGL_3/P(GL_p\times GL_{3-p})$, of dimension $2p(3-p)$, a fibre bundle over the Grassmannian $\operatorname{Gr}(p,3)$ whose fibre is the contractible space of complements.** For $p=1$ and $p=2$ the dimension is $4$; the two cases are exchanged by $E\mapsto I-E$. The full flag variety $GL_3/B$ has dimension $3$, and the partial flags are the Grassmannians. The gauge torus $T/\mathbb{C}^{\times}$ is the two-dimensional quotient of the diagonal torus inside the fibre of the frame bundle over the flag variety, and it rescales the nilpotents $E_{12},E_{23}$ while fixing the idempotents.

An idempotent is a solution of $E^{2}=E$; it is a projection onto its image along its kernel. The geometry of the idempotents is therefore the geometry of pairs of complementary subspaces, and the rank stratification is the stratification by the dimension of the image. The article proves the orbit description, identifies the fibres, computes the dimensions, describes the incidence relations and the flag variety, and works explicit matrices. The Peirce decomposition is *The Peirce Decomposition of $M_3(\mathbb{C})$*; the frame and the gauge are *The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$*; the topology is *The Topology of $M_3(\mathbb{C})$*.

## Idempotents and Complementary Pairs

**Definition.** An idempotent is a matrix $E\in M_3(\mathbb{C})$ with $E^{2}=E$. Its rank is the dimension of its image.

**Proposition.** Let $E$ be an idempotent of rank $p$. Then

$$
\mathbb{C}^{3}=\operatorname{im}E\oplus\ker E,
$$

and $E$ is the projection onto $\operatorname{im}E$ along $\ker E$. Conversely, every direct sum decomposition $\mathbb{C}^{3}=V\oplus W$ with $\dim V=p$ defines an idempotent $E_{V,W}$ of rank $p$ with image $V$ and kernel $W$.

**Proof.** If $v\in\operatorname{im}E\cap\ker E$, then $v=Ew$ and $Ev=0$, so $v=Ew=E^{2}w=E(Ev)=0$. If $x\in\mathbb{C}^{3}$, then $x=Ex+(x-Ex)$, with $Ex\in\operatorname{im}E$ and $E(x-Ex)=Ex-E^{2}x=0$, so $x\in\operatorname{im}E+\ker E$. The map $E_{V,W}$ is defined by $E(v+w)=v$ for $v\in V$, $w\in W$; it is linear, has image $V$, kernel $W$, and squares to itself.

**Corollary.** The idempotents of rank $p$ are in bijection with the pairs $(V,W)$ of complementary subspaces with $\dim V=p$. The bijection is $E\mapsto(\operatorname{im}E,\ker E)$.

**The trace.** An idempotent of rank $p$ has trace $p$, because the trace is the sum of the eigenvalues and the eigenvalues of an idempotent are $0$ and $1$. In particular, the rank is determined by the trace.

## The Orbits

**Theorem.** The group $GL_3(\mathbb{C})$ acts transitively on the idempotents of rank $p$ by conjugation,

$$
E\longmapsto SES^{-1},
$$

and the stabiliser of the idempotent $E_p=\operatorname{diag}(I_p,0)$ is the block diagonal subgroup

$$
P_p=\left\{\begin{pmatrix}A&0\\0&D\end{pmatrix}:A\in GL_p(\mathbb{C}),\ D\in GL_{3-p}(\mathbb{C})\right\}.
$$

Hence the variety of idempotents of rank $p$ is

$$
\mathcal{E}_p\cong GL_3(\mathbb{C})/P_p\cong PGL_3(\mathbb{C})/P(GL_p\times GL_{3-p}),
$$

of complex dimension

$$
\dim\mathcal{E}_p=9-\big(p^{2}+(3-p)^{2}\big)=2p(3-p).
$$

**Proof of transitivity.** Two idempotents of rank $p$ have images of dimension $p$ and kernels of dimension $3-p$; choose bases adapted to the decompositions $\mathbb{C}^{3}=\operatorname{im}E\oplus\ker E$ and $\mathbb{C}^{3}=\operatorname{im}F\oplus\ker F$. The change of basis maps one decomposition to the other and conjugates $E$ to $F$.

**Proof of the stabiliser.** The condition $SE_p=E_pS$ in block form $S=\begin{pmatrix}A&B\\C&D\end{pmatrix}$ gives

$$
\begin{pmatrix}A&0\\C&0\end{pmatrix}
=\begin{pmatrix}A&B\\0&0\end{pmatrix},
$$

so $B=0$ and $C=0$. The blocks $A$ and $D$ must be invertible because $S$ is invertible. The dimension is $p^{2}+(3-p)^{2}$; subtracting from $9$ gives $2p(3-p)$.

**The centre.** The scalar matrices act trivially by conjugation, so the orbit is also the quotient of $PGL_3$ by the image of $P_p$. The dimension is the same because the centre is one-dimensional and is contained in $P_p$.

**The values.** For $p=0$ and $p=3$ the orbit is a point, the zero matrix and the identity. For $p=1$ and $p=2$,

$$
\dim\mathcal{E}_1=\dim\mathcal{E}_2=2\cdot1\cdot2=4 .
$$

**The complement map.** The map $E\mapsto I-E$ is a bijection between idempotents of rank $p$ and idempotents of rank $3-p$; it exchanges image and kernel, and it is an isomorphism of varieties. So the geometry of rank two is the geometry of rank one.

## The Affine Bundle over the Grassmannian

**The projection.** For $p=1$, the map

$$
\pi:\mathcal{E}_1\longrightarrow\mathbb{P}^{2},\qquad E\longmapsto\operatorname{im}E,
$$

sends an idempotent to its image line. The fibre over a line $L$ is the set of idempotents with image $L$, equivalently the set of kernels $W$ complementary to $L$.

**Theorem.** The fibre $\pi^{-1}(L)$ is an affine space of dimension $2$, and $\mathcal{E}_1$ is an affine bundle of rank $2$ over $\mathbb{P}^{2}$.

**Proof.** Fix a line $L$. A complement $W$ to $L$ is the graph of a linear map $L\to\mathbb{C}^{3}/L$; the set of such graphs is an affine space modelled on $\operatorname{Hom}(L,\mathbb{C}^{3}/L)\cong\mathbb{C}^{2}$. The identification depends on the choice of a base complement, so the bundle is affine and not a vector bundle. The total space has dimension $2+2=4$.

**Explicit coordinates.** Choose a vector $u$ spanning $L$ and a linear functional $\varphi$ with $\varphi(u)=1$. The idempotent is

$$
E=u\varphi,
$$

and the kernel is $\ker\varphi$, a complement of $L$. The pair $(u,\varphi)$ is determined by $E$ up to the scaling $(u,\varphi)\mapsto(\lambda u,\lambda^{-1}\varphi)$, so the fibre has the two parameters of $\varphi$ modulo the normalisation $\varphi(u)=1$, which is the affine space $\mathbb{C}^{2}$.

**The rank-two case.** For $p=2$, the map $E\mapsto\ker E$ sends a rank-two idempotent to a line, and the fibre is again an affine space of dimension $2$; via $E\mapsto I-E$ this is the rank-one picture with image and kernel exchanged.

**Worked example.** Take

$$
u=\begin{pmatrix}1\\1\\0\end{pmatrix},
\qquad
\varphi=\begin{pmatrix}1&0&0\end{pmatrix},
\qquad
E=u\varphi=\begin{pmatrix}1&0&0\\1&0&0\\0&0&0\end{pmatrix}.
$$

Then $E^{2}=E$, $\operatorname{im}E=\mathbb{C}u$, and $\ker E=\ker\varphi=\{x:x_1=0\}=\operatorname{span}(e_2,e_3)$, a complement of the line $\mathbb{C}u$. The rank is $1$, the trace is $1$, and the point of $\mathbb{P}^{2}$ is $[1:1:0]$. The fibre coordinate is the functional $\varphi$ restricted to the quotient, with the normalisation $\varphi(u)=1$.

**The zero and the identity.** The idempotents of rank $0$ and $3$ are isolated: the zero matrix and the identity. The variety of all idempotents has four connected components. The rank-one and rank-two varieties are connected, and the zero and identity are points, so the total has four connected components, of dimensions $0,4,4,0$.

## Flags and Grassmannians

**The Grassmannians.** For $0\le p\le3$, the Grassmannian $\operatorname{Gr}(p,3)$ is the set of $p$-dimensional subspaces of $\mathbb{C}^{3}$. It is a compact complex manifold of dimension

$$
\dim\operatorname{Gr}(p,3)=p(3-p),
$$

with $\operatorname{Gr}(0,3)$ and $\operatorname{Gr}(3,3)$ points, and $\operatorname{Gr}(1,3)\cong\mathbb{P}^{2}\cong\operatorname{Gr}(2,3)$.

**The full flag variety.** A full flag is a chain

$$
0\subset L_1\subset L_2\subset\mathbb{C}^{3},
\qquad \dim L_1=1,\quad \dim L_2=2 .
$$

The group $GL_3(\mathbb{C})$ acts transitively on the full flags. The stabiliser of the standard flag $\langle e_1\rangle\subset\langle e_1,e_2\rangle$ is the Borel subgroup $B$ of upper triangular invertible matrices, of dimension $6$ (three diagonal and three upper entries). Hence the flag variety is

$$
\operatorname{Flags}=GL_3/B\cong PGL_3/B',
$$

of dimension $9-6=3$; $B'$ is the image of $B$ in $PGL_3$, of dimension $5$, and $8-5=3$.

**The partial flags.** A partial flag of type $(p)$ is a $p$-dimensional subspace, so the variety of partial flags of type $(p)$ is $\operatorname{Gr}(p,3)$, of dimension $p(3-p)$. A partial flag of type $(1,2)$ is a full flag: a line contained in a plane. The incidence variety

$$
\{(L,V):L\subset V\}\subset\mathbb{P}^{2}\times\mathbb{P}^{2}
$$

has dimension $3$: it is the full flag variety, and the two projections to $\mathbb{P}^{2}$ are fibrations with fibre $\mathbb{P}^{1}$.

**Proof of the incidence dimension.** Fix $L$; the planes $V$ containing $L$ form a $\mathbb{P}^{1}$, so the incidence variety has dimension $2+1=3$. Fix $V$; the lines $L\subset V$ form a $\mathbb{P}^{1}$, the same count. The two projections exhibit the flag variety as a $\mathbb{P}^{1}$-bundle over either Grassmannian.

**The incidence of idempotents.** For idempotents $E$ of rank $1$ and $F$ of rank $2$, the relation

$$
EF=FE=E
$$

says that $E$ is a subprojection of $F$: the image of $E$ is contained in the image of $F$, and the kernel of $F$ is contained in the kernel of $E$. The pair $(\operatorname{im}E,\operatorname{im}F)$ is a flag $L\subset V$. The variety of such pairs maps to the full flag variety; the map is surjective, and its fibres are the choices of the complementary kernels. The idempotent incidence is the linear realisation of the flag incidence.

**Worked example.** Let

$$
E=E_{11}=\begin{pmatrix}1&0&0\\0&0&0\\0&0&0\end{pmatrix},
\qquad
F=E_{11}+E_{22}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix}.
$$

Then $E^{2}=E$, $F^{2}=F$, and $EF=FE=E$. The images are $L=\langle e_1\rangle\subset V=\langle e_1,e_2\rangle$, and the kernels are $\ker E=\langle e_2,e_3\rangle$ and $\ker F=\langle e_3\rangle$, with $\ker F\subset\ker E$. The flag is the standard one.

**The complement example.** For

$$
E'=\begin{pmatrix}1&0&0\\1&0&0\\0&0&0\end{pmatrix},
\qquad
F'=I-E'=\begin{pmatrix}0&0&0\\-1&1&0\\0&0&1\end{pmatrix},
$$

one has $E'F'=F'E'=0$ and $E'+F'=I$. The idempotents are complementary: the image of $E'$ is the kernel of $F'$ and the kernel of $E'$ is the image of $F'$. The pair is a decomposition of the identity, not a flag incidence.

## The Gauge and the Frame Bundle

**The frame bundle.** A frame is an ordered basis $(u_1,u_2,u_3)$ of $\mathbb{C}^{3}$, that is, a matrix $S\in GL_3$ whose columns are the frame vectors. The map

$$
GL_3\longrightarrow\operatorname{Flags},\qquad
S\longmapsto\big(\langle u_1\rangle\subset\langle u_1,u_2\rangle\big),
$$

is a principal bundle with fibre the Borel $B$, of dimension $6$. The fibre over a flag is the set of frames adapted to the flag.

**The gauge torus.** Inside $B$ sits the diagonal torus

$$
T=\{\operatorname{diag}(t_1,t_2,t_3):t_i\neq0\},
$$

which rescales the frame vectors without changing the flag. The scalar matrices $\mathbb{C}^{\times}I$ act trivially on the flag and on the idempotents, so the gauge group of the frame is

$$
T/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^{2},
$$

of complex dimension $2$ and real dimension $4$. The two gauge parameters are

$$
\lambda_1=t_1/t_2,\qquad
\lambda_2=t_2/t_3 .
$$

**The action on the nilpotents.** In the frame adapted to the root $H$, the gauge acts by

$$
E_{12}\mapsto\lambda_1E_{12},\qquad
E_{23}\mapsto\lambda_2E_{23},\qquad
E_{13}\mapsto\lambda_1\lambda_2E_{13}.
$$

The product is forced by the composition: $t_1/t_3=(t_1/t_2)(t_2/t_3)$. The idempotents $P_k$ are invariant, because they are diagonal in the frame and the gauge rescales the frame vectors within their own lines. The gauge is therefore the fibre direction of the frame bundle that is invisible to the idempotents.

**The gauge as a fibre.** The fibration $GL_3\to\operatorname{Flags}$ has fibre $B$; the diagonal torus $T$ is the subgroup of the fibre that preserves the splitting of the flag into lines, and $T/\mathbb{C}^{\times}$ is the gauge torus. The gauge is not an extra symmetry of the idempotent variety: it is the ambiguity in choosing a frame over a flag, and the idempotents depend only on the flag data and the complementary kernels.

**Proof.** A diagonal matrix $t$ acts on the frame by $u_i\mapsto t_iu_i$; the flag $\langle u_1\rangle\subset\langle u_1,u_2\rangle$ is unchanged. The conjugation $tE_{ij}t^{-1}$ multiplies $E_{ij}$ by $t_i/t_j$, which gives the three rescalings. The idempotents $P_k$ have matrix units $E_{kk}$ on the diagonal, so they are fixed.

## The Geometry of the Strata

**The rank stratification.** The idempotents stratify by rank:

| Rank $p$ | Variety | Complex dimension | Fibre over $\operatorname{Gr}(p,3)$ |
|---|---|---|---|
| $0$ | point | $0$ | point |
| $1$ | affine bundle over $\mathbb{P}^{2}$ | $4$ | $\mathbb{C}^{2}$ |
| $2$ | affine bundle over $\mathbb{P}^{2}$ | $4$ | $\mathbb{C}^{2}$ |
| $3$ | point | $0$ | point |

The middle two strata are isomorphic by $E\mapsto I-E$.

**The strata are closed.** The rank is locally constant on the idempotent variety: for an idempotent, $\operatorname{rank}E=\operatorname{tr}E$, and the trace is continuous with integer values, hence constant on a connected neighbourhood. Therefore each rank stratum is open and closed in the variety of idempotents, and the four strata are its connected components.

**The tangent space.** At an idempotent $E$, the tangent space of the orbit is

$$
T_E\mathcal{E}_p=\operatorname{im}(\operatorname{ad}_E)=\{[X,E]:X\in M_3\},
$$

the set of commutators. Its dimension is $2p(3-p)$, and its orthogonal complement for the trace form is $\ker(\operatorname{ad}_{E^{*}})$, the centraliser of $E^{*}$.


**Proof.** The derivative of $SES^{-1}$ at $S=I$ in the direction $X$ is $[X,E]$. The image of $\operatorname{ad}_E$ has dimension $\dim GL_3-\dim\ker\operatorname{ad}_E=9-(p^{2}+(3-p)^{2})=2p(3-p)$, which matches the orbit dimension. The orthogonal complement of the image for the trace form is the kernel of $\operatorname{ad}_{E^{*}}$; for an idempotent, $E^{*}$ is another idempotent, and the centraliser has the same dimension.

**The normal directions.** The complement of the tangent space is the centraliser of $E^{*}$, of dimension $p^{2}+(3-p)^{2}$. The normal directions to the orbit are the ways of moving the image and the kernel independently; the fibre directions of the affine bundle are the normal directions that change the kernel while fixing the image.

**Worked dimension check.** For $p=1$, the orbit has dimension $4$ and the centraliser has dimension $1+4=5$; the sum is $9$. For $p=2$, the orbit has dimension $4$ and the centraliser has dimension $4+1=5$; the sum is $9$. For $p=0$ and $p=3$ the orbit is a point and the centraliser is all of $M_3$.

## Summary

The idempotents of rank $p$ are the projections onto a $p$-plane along a complementary $(3-p)$-plane. They form the homogeneous space

$$
\mathcal{E}_p\cong GL_3/P_p\cong PGL_3/P(GL_p\times GL_{3-p}),
\qquad
\dim\mathcal{E}_p=2p(3-p),
$$

with $P_p$ the block diagonal $GL_p\times GL_{3-p}$. For $p=1$ the variety is an affine bundle of rank $2$ over $\mathbb{P}^{2}$, of dimension $4$; the fibre over a line $L$ is the affine space of complements to $L$, isomorphic to $\mathbb{C}^{2}$ and contractible. For $p=2$ the map $E\mapsto I-E$ identifies the geometry with the rank-one case. The strata of ranks $0,1,2,3$ are the four connected components of the idempotent variety, of dimensions $0,4,4,0$. The full flag variety $GL_3/B$ has dimension $3$, and the incidence variety of a line in a plane is the same flag variety, a $\mathbb{P}^{1}$-bundle over either $\mathbb{P}^{2}$. The gauge torus $T/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^{2}$ has complex dimension $2$ and real dimension $4$; it rescales $E_{12},E_{23}$ by $\lambda_1,\lambda_2$ and $E_{13}$ by the forced product $\lambda_1\lambda_2$, while fixing the spectral idempotents $P_k$.

$$
\boxed{\ \mathcal{E}_p=GL_3/(GL_p\times GL_{3-p}),\quad \dim=2p(3-p);\quad \mathcal{E}_1\to\mathbb{P}^{2}\text{ affine } \mathbb{C}^{2}\text{-bundle};\quad \dim\mathrm{Flags}=3;\quad \dim(T/\mathbb{C}^{\times})=2.\ }
$$

| Object | Complex dimension | Real dimension |
|---|---|---|
| $\mathcal{E}_1$ | $4$ | $8$ |
| $\mathcal{E}_2$ | $4$ | $8$ |
| $\operatorname{Gr}(p,3)$ | $p(3-p)$ | $2p(3-p)$ |
| $\operatorname{Flags}$ | $3$ | $6$ |
| $T/\mathbb{C}^{\times}$ | $2$ | $4$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E$ | idempotent, $E^{2}=E$ |
| $\mathcal{E}_p$ | idempotents of rank $p$ |
| $P_p$ | block diagonal $GL_p\times GL_{3-p}$ |
| $\operatorname{Gr}(p,3)$ | Grassmannian of $p$-planes in $\mathbb{C}^{3}$ |
| $\operatorname{Flags}$ | full flag variety $GL_3/B$ |
| $T$ | diagonal torus of the frame |
| $\lambda_1,\lambda_2$ | gauge parameters $t_1/t_2$, $t_2/t_3$ |

## Further Reading

- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the Grassmannians, the flag variety and the Borel subgroup.
- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992), for the determinantal varieties and the incidence varieties.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the geometry of the Grassmannians.
- [The Peirce Decomposition of $M_3(\mathbb{C})$](the-peirce-decomposition-of-m3c.html), for the idempotents in the algebra.
- [The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-m3c.html), for the frame and the gauge parameters.
- [The Topology of $M_3(\mathbb{C})$](the-topology-of-m3c.html), for the homotopy type of the idempotent varieties.
