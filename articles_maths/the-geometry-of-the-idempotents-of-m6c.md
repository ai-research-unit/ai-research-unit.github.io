# __The Geometry of the Idempotents of $M_6(\mathbb{C})$__

## Introduction

An idempotent of $M_6(\mathbb{C})$ is a matrix $E$ with

$$
E^2=E.
$$

It is a projector: $V=\operatorname{im}E\oplus\ker E$, and $E$ is the projection onto its image along its kernel. The rank-$p$ idempotents form a smooth variety

$$
\mathcal E_p=\{E:E^2=E,\ \operatorname{rank}E=p\},
$$

of complex dimension

$$
\dim\mathcal E_p=2p(6-p).
$$

For $p=1$ the variety is an affine bundle of rank $5$ over $\mathbb{P}^5$, of dimension $10$; for general $p$ it is the homogeneous space

$$
\mathcal E_p\cong PGL_6/P(GL_p\times GL_{6-p}),
$$

a fibre bundle over $\operatorname{Gr}(p,6)$ with the contractible fibre of complements. The full flag variety $GL_6/B$ has dimension $15$; the partial flags and their incidence relations organise the idempotents, and the gauge is the fibre of the frame bundle.

The article assumes the Grassmannians and the orbit–stabilizer count of *The Adjoint Action, the Orbits and the Flag Variety of $M_6(\mathbb{C})$* and the Peirce decomposition of *The Peirce Decomposition of $M_6(\mathbb{C})$*. It uses the elementary geometry of homogeneous spaces. The idempotents of the biquaternion algebra are *Square Roots of One and the Idempotents of the Biquaternion Algebra*; the spectral geometry is *The Sextic and the Spectral Strata of $M_6(\mathbb{C})$*.

## The Idempotents

### Definition and Rank

**Definition.** An **idempotent** is $E\in M_6(\mathbb{C})$ with $E^2=E$. Its **rank** is the dimension of its image.

**Theorem.** If $E^2=E$, then

$$
V=\operatorname{im}E\oplus\ker E,
\qquad
E|_{\operatorname{im}E}=I,\quad
E|_{\ker E}=0,
$$

and the rank is the trace. Conversely, every direct sum decomposition $V=U\oplus W$ defines the idempotent $E$ with image $U$ and kernel $W$.

**Proof.** For $v\in V$, $v=Ev+(v-Ev)$; $Ev\in\operatorname{im}E$ and $v-Ev\in\ker E$ because $E(v-Ev)=Ev-E^2v=0$. The intersection is zero: if $Ev=0$ and $Ev=v$, then $v=0$. On the image, $E(Ev)=E^2v=Ev$; on the kernel, $E=0$. The trace is the sum of the eigenvalues, which are $1$ on the image and $0$ on the kernel.

**Corollary (the eigenvalues).** The eigenvalues of an idempotent are $0$ and $1$; the rank is the multiplicity of $1$.

**Proof.** The minimal polynomial divides $t^2-t=t(t-1)$.

### The Rank-One Idempotents

**Theorem.** A rank-one idempotent is

$$
E=u\varphi,
\qquad
\varphi(u)=1,
$$

with $u\in\mathbb{C}^6$ and $\varphi\in(\mathbb{C}^6)^*$. Its image is the line $\mathbb{C}u$, and its kernel is the hyperplane $\ker\varphi$.

**Proof.** A rank-one matrix is $u\varphi$; $E^2=u\varphi(u)\varphi=\varphi(u)E$, so $E^2=E$ iff $\varphi(u)=1$. The image is $\mathbb{C}u$; the kernel is $\ker\varphi$.

**Theorem (the affine bundle).** The rank-one idempotents form an affine bundle of rank $5$ over $\mathbb{P}^5$:

$$
\pi:\mathcal E_1\longrightarrow\mathbb{P}^5,
\qquad
E\longmapsto\operatorname{im}E .
$$

The fibre over the line $L$ is the affine space of complements $H$ to $L$ in $\mathbb{C}^6$, of dimension $5$. Hence

$$
\dim\mathcal E_1=5+5=10 .
$$

**Proof.** The image of a rank-one idempotent is a line, so the map is well defined and surjective. The fibre over $L$ is the set of kernels $H$ complementary to $L$, equivalently the set of splittings $V=L\oplus H$. The set of complements to $L$ is an affine space modelled on $\operatorname{Hom}(V/L,L)$, of dimension $5$. The total dimension is the sum.

**Corollary (the affine structure).** Choose a line $L$ and a complement $H_0$. Every other complement is the graph of a linear map $L\to H_0$; the affine coordinates are the $5$ parameters of that map.

**Proof.** A complement $H$ transverse to $L$ is the graph of a unique linear map $L\to H_0$; the graph is a $5$-dimensional affine space.

**Corollary (the explicit form).** In a basis with $L=\mathbb{C}e_1$ and $H_0=\langle e_2,\dots,e_6\rangle$, the rank-one idempotents with image $L$ are

$$
E=\begin{pmatrix}1&a_2&\cdots&a_6\\0&0&\cdots&0\\\vdots&\vdots&&\vdots\\0&0&\cdots&0\end{pmatrix},
\qquad
(a_2,\dots,a_6)\in\mathbb{C}^5 .
$$

**Proof.** $E=e_1\varphi$ with $\varphi(e_1)=1$ and $\varphi(e_j)=a_j$; the matrix is the row $(1,a_2,\dots,a_6)$ in the first row.

### The Rank-$p$ Idempotents

**Theorem.** The rank-$p$ idempotents form the homogeneous space

$$
\mathcal E_p\cong PGL_6/P(GL_p\times GL_{6-p}),
$$

of complex dimension

$$
\dim\mathcal E_p=2p(6-p).
$$

**Proof.** $PGL_6$ acts transitively on rank-$p$ idempotents: every such idempotent is conjugate to $E_p=\operatorname{diag}(I_p,0)$. The stabilizer of $E_p$ is the image in $PGL_6$ of the block-diagonal $GL_p\times GL_{6-p}$, of dimension $p^2+(6-p)^2-1$. The orbit dimension is

$$
35-\bigl(p^2+(6-p)^2-1\bigr)=36-p^2-(6-p)^2=2p(6-p).
$$

**Corollary (the table).**

| $p$ | $2p(6-p)$ | Description |
|---|---|---|
| $0$ | $0$ | the zero idempotent |
| $1$ | $10$ | affine bundle over $\mathbb{P}^5$ |
| $2$ | $16$ | affine bundle over $\operatorname{Gr}(2,6)$ |
| $3$ | $18$ | affine bundle over $\operatorname{Gr}(3,6)$ |
| $4$ | $16$ | affine bundle over $\operatorname{Gr}(4,6)$ |
| $5$ | $10$ | affine bundle over $\operatorname{Gr}(5,6)=\mathbb{P}^5$ |
| $6$ | $0$ | the identity |

**Proof.** Substitute $p$ in $2p(6-p)$.

**Theorem (the bundle over the Grassmannian).** The image map

$$
\pi_p:\mathcal E_p\longrightarrow\operatorname{Gr}(p,6),
\qquad
E\longmapsto\operatorname{im}E
$$

is a fibre bundle with fibre the affine space of complements, of dimension $p(6-p)$. Hence

$$
\dim\mathcal E_p=p(6-p)+p(6-p)=2p(6-p).
$$

**Proof.** The image is a $p$-plane; the kernel is a complementary $(6-p)$-plane. The set of complements to a fixed $p$-plane is an affine space modelled on $\operatorname{Hom}(\mathbb{C}^6/V_p,V_p)$, of dimension $p(6-p)$. The total dimension is the sum.

**Corollary (the contractible fibre).** The fibre is an affine space, hence contractible; the variety $\mathcal E_p$ is homotopy equivalent to the Grassmannian $\operatorname{Gr}(p,6)$.

**Proof.** A fibre bundle with contractible fibre has the homotopy type of the base.

**Remark (the two descriptions).** The homogeneous-space description $PGL_6/P(GL_p\times GL_{6-p})$ and the affine-bundle description over $\operatorname{Gr}(p,6)$ are the same variety: the base is the image Grassmannian, the fibre is the complement, and the structure group is the affine general linear group of the complement.

## The Flag Variety

### The Full Flag Variety

**Definition.** A **complete flag** is a chain

$$
0\subset V_1\subset V_2\subset\cdots\subset V_5\subset\mathbb{C}^6,
\qquad
\dim V_i=i .
$$

The **full flag variety** is

$$
\mathcal F=GL_6/B,
$$

where $B$ is the Borel subgroup of upper triangular matrices.

**Theorem.** $\mathcal F$ is a smooth projective variety of dimension

$$
\dim\mathcal F=36-21=15 .
$$

**Proof.** $GL_6$ acts transitively on complete flags; the stabilizer of the standard flag is $B$, of dimension $21$ (six diagonal and fifteen upper off-diagonal parameters); the quotient has dimension $15$.

**Corollary (the iterated bundle).** The flag variety is an iterated projective bundle with fibres

$$
\mathbb{P}^5,\ \mathbb{P}^4,\ \mathbb{P}^3,\ \mathbb{P}^2,\ \mathbb{P}^1,
$$

and

$$
15=5+4+3+2+1 .
$$

**Proof.** Choose $V_1$ in $\mathbb{P}^5$; then $V_2/V_1$ in $\mathbb{P}^4$; then $V_3/V_2$ in $\mathbb{P}^3$; then $V_4/V_3$ in $\mathbb{P}^2$; then $V_5/V_4$ in $\mathbb{P}^1$.

### The Partial Flags

**Definition.** A **partial flag of type $(p_1,\dots,p_k)$** is a chain

$$
0\subset V_{p_1}\subset\cdots\subset V_{p_k}\subset\mathbb{C}^6,
\qquad
\dim V_{p_i}=p_i .
$$

**Theorem.** The partial flag variety of type $(p)$ is the Grassmannian

$$
\mathcal F_{(p)}=\operatorname{Gr}(p,6),
\qquad
\dim=p(6-p).
$$

For the type $(p,q)$ with $p<q$, the dimension is

$$
\dim\mathcal F_{(p,q)}=p(6-p)+(q-p)(6-q).
$$

**Proof.** Choose $V_p$ (dimension $p(6-p)$); then $V_q/V_p$ is a $(q-p)$-plane in $\mathbb{C}^6/V_p\cong\mathbb{C}^{6-p}$, of dimension $(q-p)(6-p-(q-p))=(q-p)(6-q)$.

**Corollary (the table).**

| Type | Dimension |
|---|---|
| $(1)$ | $5$ |
| $(2)$ | $8$ |
| $(3)$ | $9$ |
| $(1,2)$ | $5+4=9$ |
| $(2,4)$ | $8+2\cdot2=12$ |
| $(1,3)$ | $5+2\cdot3=11$ |
| $(1,2,3)$ | $5+4+3=12$ |
| $(1,2,3,4,5)$ | $15$ |

**Proof.** Apply the formula.

### The Incidence

**Theorem.** The full flag variety fibres over every partial flag variety:

$$
\pi_{p_1,\dots,p_k}:\mathcal F\longrightarrow\mathcal F_{(p_1,\dots,p_k)},
$$

with fibre the product of the flag varieties of the successive quotients.

**Proof.** A complete flag projects to its subspaces of the prescribed dimensions; the fibre consists of the flags refining the partial flag.

**Corollary (the rank-$p$ idempotent and the flag).** A rank-$p$ idempotent determines the two-step partial flag

$$
0\subset\operatorname{im}E\subset\mathbb{C}^6,
$$

but not a complete flag; the complete flag requires the further splitting of the image and the kernel. The fibre of $\mathcal F\to\operatorname{Gr}(p,6)$ over the image is the product of the full flag varieties of the $p$-plane and the $(6-p)$-quotient, of dimension

$$
\frac{p(p-1)}2+\frac{(6-p)(5-p)}2 .
$$

**Proof.** The image and the quotient are the two blocks of the idempotent; a complete flag refining $0\subset\operatorname{im}E\subset V$ is a flag of the image times a flag of the quotient.

**Remark (idempotent versus flag).** An idempotent of rank $p$ is more than its image: it also chooses the kernel, a complement. **The Grassmannian records the image; the idempotent records the splitting; the flag records the refinement.**

## The Gauge and the Frame Bundle

### The Frame Bundle

**Definition.** A **frame** of $\mathbb{C}^6$ is an ordered basis $(v_1,\dots,v_6)$. The **frame bundle** over the flag variety is

$$
\pi:GL_6\longrightarrow GL_6/B=\mathcal F,
$$

sending a frame to the flag of its coordinate spans.

**Theorem.** $\pi$ is a principal $B$-bundle: the fibre over a flag is the Borel subgroup $B$ of dimension $21$.

**Proof.** Two frames give the same flag iff they differ by an upper triangular change of basis, that is by an element of $B$.

**Corollary (the gauge).** The **gauge** is the maximal torus of $B$ modulo the center,

$$
(\mathbb{C}^\times)^5,
$$

of dimension $5$. It acts on the frame by rescaling the basis vectors.

**Proof.** The diagonal torus of $GL_6$ is $(\mathbb{C}^\times)^6$; modulo the center $\mathbb{C}^\times I_6$ it is $(\mathbb{C}^\times)^5$. The rescaling of the frame preserves the flag.

### The Gauge as the Fibre

**Theorem.** Over the root $H$, the eigenframe bundle is a principal $(\mathbb{C}^\times)^6$-bundle; modulo the overall scale it is a principal $(\mathbb{C}^\times)^5$-bundle, and the gauge is its fibre.

**Proof.** The eigenbases of $H$ are the frames in which $H$ is diagonal; two such frames differ by independent rescalings, the torus $(\mathbb{C}^\times)^6$. The overall scale acts trivially on the projective frame, so the gauge is $(\mathbb{C}^\times)^6/\mathbb{C}^\times\cong(\mathbb{C}^\times)^5$.

**Corollary (the dimensions).**

$$
\dim GL_6=36=\dim\mathcal F+\dim B=15+21,
\qquad
\dim B=21=15+6 .
$$

The Borel has dimension $21$; its maximal torus has dimension $6$; the unipotent radical has dimension $15$; the gauge is the torus modulo the center, of dimension $5$.

**Proof.** The Borel is the semidirect product of the torus (dimension $6$) and the unipotent radical (dimension $15$); the flag variety has dimension $15$.

**Remark (the three fibres).** The frame bundle over the flag variety has fibre the Borel ($21$); the eigenframe bundle over the root has fibre the torus ($6$, or $5$ projectively); the idempotent bundle over the Grassmannian has fibre the affine space of complements ($p(6-p)$). **The gauge is the torus fibre; the flag fibre is the Borel; the idempotent fibre is the complement.**

## Summary

The rank-$p$ idempotents form the smooth variety

$$
\mathcal E_p\cong PGL_6/P(GL_p\times GL_{6-p}),
\qquad
\dim_{\mathbb{C}}\mathcal E_p=2p(6-p),
$$

an affine bundle over the Grassmannian $\operatorname{Gr}(p,6)$ with fibre the contractible affine space of complements, of dimension $p(6-p)$.

$$
\boxed{\ \dim\mathcal E_1=10=5+5,\qquad \dim\mathcal E_p=2p(6-p),\qquad \dim GL_6/B=15 .\ }
$$

For $p=1$ the variety is an affine bundle of rank $5$ over $\mathbb{P}^5$; for $p=3$ it has dimension $18$; for $p=6$ it is the single identity.

The full flag variety $GL_6/B$ has dimension $15$, with the iterated bundle $5+4+3+2+1$. The partial flags are the Grassmannians and their incidences; an idempotent determines the two-step flag of its image, and the complete flag refines it. The gauge $(\mathbb{C}^\times)^5$ is the fibre of the frame bundle over the root; the Borel is the fibre over the flag.

| Object | Dimension |
|---|---|
| $\mathcal E_1$ | $10$ |
| $\mathcal E_2$ | $16$ |
| $\mathcal E_3$ | $18$ |
| $\mathcal E_p$ | $2p(6-p)$ |
| $\operatorname{Gr}(p,6)$ | $p(6-p)$ |
| Full flag variety | $15$ |
| Borel $B$ | $21$ |
| Gauge $(\mathbb{C}^\times)^5$ | $5$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal E_p$ | the rank-$p$ idempotents |
| $P(GL_p\times GL_{6-p})$ | the projective Levi stabilizer |
| $\operatorname{Gr}(p,6)$ | the Grassmannian of $p$-planes |
| $\mathcal F=GL_6/B$ | the full flag variety |
| $\mathcal F_{(p_1,\dots,p_k)}$ | the partial flag variety |
| $B$ | the Borel subgroup of upper triangular matrices |

## Further Reading

- [The Adjoint Action, the Orbits and the Flag Variety of $M_6(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m6c.html), for the orbit–stabilizer count and the Grassmannians.
- [The Peirce Decomposition of $M_6(\mathbb{C})$](the-peirce-decomposition-of-m6c.html), for the corners of an idempotent.
- [The Rank-Two and Rank-Three Splits of $M_6(\mathbb{C})$](the-rank-two-and-rank-three-splits-of-m6c.html), for the rank-two and rank-three idempotents.
- [The Modules and the Minimal Left Ideals of $M_6(\mathbb{C})$](the-modules-and-the-minimal-left-ideals-of-m6c.html), for the projective space of the minimal ideals.
- [The Frame, the Simple Nilpotents and the Gauge of $M_6(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-m6c.html), for the gauge torus.
- [Grassmannians and Stiefel Manifolds](grassmannians-and-stiefel-manifolds.html), for the general theory of $\operatorname{Gr}(p,n)$.
- [Flag Manifolds](flag-manifolds.html), for the general theory of $GL_n/B$ and the incidence.
- [Idempotents](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the rank-one case.
