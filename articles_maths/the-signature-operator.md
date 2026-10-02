
# __The Signature Operator__

## Introduction

The signature of a closed oriented manifold of dimension $4k$ is the signature of the intersection form on its middle cohomology: the integer $b_{+}-b_{-}$ formed from the numbers of positive and negative eigenvalues of the pairing $\langle u\cup v,[M]\rangle$. The signature is a topological invariant, and the **signature operator** exhibits it as the index of a differential operator built from a chosen metric — the operator $D=d+d^{*}$ on the differential forms, read with the grading that the metric supplies. The operator is the geometric form of the intersection form: the intersection pairing of the middle cohomology is its restriction to the harmonic forms, and the signature is the index of its positive half.

This article defines the operator, identifies its square with the Hodge Laplacian, and states the signature theorem, that the index of the operator equals $\int_M L(M)$ for the Hirzebruch $L$-genus. The operator itself is an object of the geometry: it is assembled from the exterior derivative $d$, the codifferential $d^{*}$ and the Hodge star, all of which depend on the chosen Riemannian metric, and a change of metric changes the operator. That its index does not change is the content of the theorem, and it is the theorem that makes the operator a topological instrument.

The prerequisites are *Differential Forms and Stokes' Theorem* for the exterior algebra of forms, the exterior derivative and Stokes' theorem; *Riemannian Geometry* and *Curvature and Geodesics* for the metric, its volume form and its Laplace–Beltrami operator; *The Volume Element, Duality and the Hodge Star* and the Part I article *The Hodge Star and the Real Structure of the Exterior Algebra* for the star and its square; *Characteristic Classes* for the Pontryagin classes and the $L$-class; and *The Atiyah–Singer Index Theorem and K-Theory* for the general theorem of which the signature theorem is a case. The Hodge Laplacian and the harmonic forms are the subject of *The Hodge Laplacian*, written beside this article, and are cited rather than developed; the heat-kernel proof of the index theorem is cited there and in *The Atiyah–Singer Index Theorem and K-Theory*. Nothing physical is invoked, and no structure belonging to a later category is used.

## The Hodge Star and the Inner Product

### The Star on a Riemannian Manifold

Let $(M,g)$ be a closed oriented Riemannian manifold of dimension $n$, with volume form $\mathrm{vol}_g$ and with $\Omega^{k}(M)$ the smooth complexified $k$-forms. The metric extends to the exterior algebra and, with the orientation, defines the **Hodge star**

$$
\star:\Omega^{k}(M)\longrightarrow\Omega^{n-k}(M),\qquad
\alpha\wedge\star\beta=\langle\alpha,\beta\rangle\,\mathrm{vol}_g ,
$$

where $\langle\cdot,\cdot\rangle$ is the metric on forms; the star is $\mathbb{C}$-linear, and it satisfies

$$
\star^2=(-1)^{k(n-k)}\,\mathrm{id}\quad\text{on }\Omega^{k}(M),
$$

the square computed in *The Hodge Star and the Real Structure of the Exterior Algebra* and *The Volume Element, Duality and the Hodge Star*. The **$L^{2}$ inner product** on forms is

$$
(\alpha,\beta)=\int_M\alpha\wedge\star\bar\beta ,
$$

a positive definite Hermitian form on $\Omega^{k}(M)$; the completion in it is the Hilbert space $L^{2}\Omega^{k}(M)$, and the star is a unitary map up to sign. The metric is a **chosen** object, and the star, the inner product and every operator below change with it.

### The Chirality of an Even-Dimensional Manifold

**Definition.** Let $n=2m$ be even and let $\tau$ be the operator that acts on $\Omega^{k}(M)$ by

$$
\tau\,\omega=i^{\,k(k-1)+m}\,\star\omega .
$$

It is the normalized volume element of the Clifford algebra of the exterior bundle; it is parallel and unitary, and one computes

$$
\tau^2=\mathrm{id},\qquad
\tau\,d\,\tau^{-1}=-d^{*},\qquad
\tau(d+d^{*})\tau^{-1}=-(d+d^{*}) .
$$

**Proof sketch.** The square uses $\star^2=(-1)^{k(n-k)}$ and the identity $i^{k(k-1)+m}i^{(n-k)(n-k-1)+m}(-1)^{k(n-k)}=1$. The conjugation of $d$ is the standard Hodge identity $\star d\star^{-1}=\pm d^{*}$, and the phase $i^{k(k-1)+m}$ is chosen so that the sign is $-1$; the third identity is the sum of the first two with the adjoint identity that follows from it. $\square$

The operator $\tau$ is the **chirality** or **grading**, and it splits the complexified forms into the two eigenspaces

$$
\Omega^{+}(M)=\{\omega:\tau\omega=\omega\},\qquad
\Omega^{-}(M)=\{\omega:\tau\omega=-\omega\} .
$$

Since $\tau$ maps $\Omega^{k}$ to $\Omega^{n-k}$, the splitting is not by degree. On the **middle forms** of a manifold of dimension $4k$ the phase is $i^{(2k)(2k-1)+2k}=i^{4k^2}=1$, so there $\tau=\star$, which is an involution there because $\star^2=(-1)^{2k\cdot2k}=1$; the eigenspaces are the **self-dual** and **anti-self-dual** middle forms of dimension $\tfrac12\dim\Omega^{2k}$, which are real and orthogonal.

## The Signature Operator

**Definition.** The **de Rham operator** of $(M,g)$ is

$$
D=d+d^{*}:\Omega^{\bullet}(M)\longrightarrow\Omega^{\bullet}(M),
$$

the sum of the exterior derivative and its formal adjoint; if the metric is understood, $D$ is the **signature operator** of the orientation.

**Theorem.** The operator $D$ is formally self-adjoint, $D^{*}=D$, elliptic, and it is **odd** for the chirality, $D\Omega^{+}\subseteq\Omega^{-}$ and $D\Omega^{-}\subseteq\Omega^{+}$; on a closed manifold it therefore splits into a pair of mutually adjoint operators

$$
D^{+}:\Omega^{+}(M)\longrightarrow\Omega^{-}(M),\qquad
(D^{+})^{*}=D^{-} .
$$

**Proof.** The adjointness of $d$ and $d^{*}$ gives $D^{*}=d^{*}+d=D$. The symbol of $D$ at a covector $\xi$ is $\sigma(\xi)=i(\varepsilon(\xi)+\iota(\xi))$, the Clifford multiplication by $\xi$, which is invertible for $\xi\neq0$ because its square is $|\xi|^2$; hence $D$ is elliptic. The oddness is the identity $\tau D\tau^{-1}=-D$ of the preceding section, which says $D\Omega^{\pm}\subseteq\Omega^{\mp}$. $\square$

**Remark.** The operator $D$ is assembled from the three metric objects of the article: the exterior derivative, the codifferential and the chirality, the codifferential being $d^{*}=-\tau d\tau^{-1}$ and the chirality being the star times a phase. A change of metric changes $d^{*}$, hence $D$, and the operator is a genuine geometric object and not a topological one. Its kernel and cokernel, however, are governed by the Hodge theorem and are finite-dimensional.

## The Square is the Hodge Laplacian

**Theorem.** The square of the signature operator is the **Hodge Laplacian**

$$
D^{2}=dd^{*}+d^{*}d=\Delta ,
$$

the operator whose kernel is the space $\mathcal{H}^{k}(M)$ of **harmonic $k$-forms**.

**Proof.** Expand $(d+d^{*})^2=dd^{*}+d^{*}d+ d^2+(d^{*})^2$; the last two vanish, $d^2=0$ being the defining property of the exterior derivative and $(d^{*})^2=0$ its adjoint. $\square$

**Corollary (the harmonic representatives).** On a closed manifold $\Delta$ is self-adjoint and elliptic with a discrete spectrum of nonnegative eigenvalues, and the **Hodge theorem** identifies its kernel with the de Rham cohomology,

$$
\mathcal{H}^{k}(M)\cong H^{k}_{dR}(M;\mathbb{C}),\qquad \dim\mathcal{H}^{k}(M)=b_{k}(M),
$$

so the kernel of $D$ on $k$-forms is the space of harmonic representatives of the cohomology. The Hodge decomposition, the identification of the harmonic forms and the spectral properties of $\Delta$ are the content of *The Hodge Laplacian*.

**Corollary (the middle splitting).** For a manifold of dimension $4k$ the chirality acts on the harmonic middle forms by the Hodge star, so the space $\mathcal{H}^{2k}(M)$ splits as

$$
\mathcal{H}^{2k}(M)=\mathcal{H}^{2k}_{+}(M)\oplus\mathcal{H}^{2k}_{-}(M),
$$

the self-dual and anti-self-dual harmonic forms, of dimensions $b_{+}$ and $b_{-}$, the numbers of positive and negative eigenvalues of the intersection form on $H^{2k}(M;\mathbb{R})$; the intersection form is the restriction of the pairing $\langle u\cup v,[M]\rangle$, and on the harmonic forms it is represented by the integral $\int_M u\wedge v$.

## The Signature Theorem

**Theorem (Hirzebruch's signature theorem).** Let $M$ be a closed oriented manifold of dimension $4k$ and let $D^{+}:\Omega^{+}\to\Omega^{-}$ be the positive half of its signature operator. Then the analytic index of $D^{+}$ is the signature of $M$:

$$
\operatorname{ind}D^{+}=\dim\ker D^{+}-\dim\operatorname{coker}D^{+}=b_{+}-b_{-}=\sigma(M) .
$$

Combined with the Atiyah–Singer index theorem, the index is the characteristic number

$$
\sigma(M)=\int_M L(TM),
$$

where $L(TM)$ is the **Hirzebruch $L$-genus** of the tangent bundle, the genus with the first terms

$$
L=1+\frac{p_1}{3}+\frac{7p_2-p_1^2}{45}+\cdots
$$

in the Pontryagin classes $p_i$ of $TM$.

**Proof sketch.** A harmonic form is closed and coclosed and represents its cohomology class, and the index of $D^{+}$ is the trace of the chirality on the kernel, $\operatorname{ind}D^{+}=\operatorname{tr}(\tau\mid\ker D)$, because $\ker D^{\pm}$ are the $\pm1$ eigenspaces of $\tau$ on $\ker D=\mathcal{H}^{\bullet}(M)$. On the middle degree the chirality is the Hodge star, so its trace on $\mathcal{H}^{2k}(M)$ is the signature $b_{+}-b_{-}$ of the intersection form; on a pair $\mathcal{H}^{j}(M)\oplus\mathcal{H}^{n-j}(M)$ with $j\neq n-j$ the chirality maps $\Omega^{j}$ to $\Omega^{n-j}$ and exchanges the two summands, so its trace there is $0$ and the non-middle harmonic forms cancel in the index. Hence $\operatorname{ind}D^{+}=b_{+}-b_{-}$. The identification of the index with $\int_ML(TM)$ is the Atiyah–Singer theorem in the case of the symbol of $d+d^{*}$, the symbol class being the Thom class whose Chern character is the $L$-class; the theorem and its heat-kernel proof are stated in *The Atiyah–Singer Index Theorem and K-Theory*. $\square$

**Remark.** The theorem is the sharp form of the observation that the operator depends on the metric but its index does not: the signature is read off the chosen metric through the operator, and the answer is a topological invariant of the manifold. The same operator on the even and odd forms, graded by the total degree instead of the chirality, has index the Euler characteristic, $\operatorname{ind}(d+d^{*})=b_{0}-b_{1}+b_{2}-\cdots=\chi(M)$; the signature and the Euler characteristic are the two characteristic numbers that the de Rham complex yields, computed by the $L$-class and the Euler class respectively.

## The Operator in Low Dimensions

### Dimension Four

**Example (the four-sphere).** For $S^4$ the middle cohomology $H^{2}(S^4;\mathbb{R})$ vanishes and the signature is $0$; consistently, $p_1(TS^4)=0$, so $\int_{S^4}L=0$. The signature operator has no harmonic middle forms and its index vanishes.

**Example (the complex projective plane).** For $\mathbb{CP}^2$ the cohomology is $\mathbb{R}$ in degrees $0,2,4$, so $b_2=1$ and the intersection form on $H^{2}$ is the $1\times1$ matrix $(1)$, of signature $1$. The first Pontryagin class evaluates as $p_1[\mathbb{CP}^2]=3$, so $L_1=p_1/3$ gives $\sigma(\mathbb{CP}^2)=1$, in agreement.

**Example (the product of two spheres).** For $S^{2}\times S^{2}$ the middle cohomology has rank two, spanned by the two sphere classes with intersection matrix
$$
\begin{pmatrix}0&1\\1&0\end{pmatrix},
$$
whose eigenvalues are $1$ and $-1$ and whose signature is $0$; the first Pontryagin class is a torsion-free class with $p_1[S^2\times S^2]=0$, and $\int L=0$ again.

**Example (a $K3$ surface).** For a $K3$ surface the middle cohomology has rank $22$, with $b_{+}=3$ and $b_{-}=19$, so the signature is
$$
\sigma(K3)=3-19=-16 ;
$$
the first Pontryagin number is $p_1[K3]=-48$, and $L_1=p_1/3$ gives $\int L=-16$, in agreement. The signature of a $K3$ surface is the standard negative value against which the signature theorem is checked, and the intersection form is the even unimodular form of rank $22$ and signature $-16$.

### Spheres and Complex Projective Spaces

**Example.** For the sphere $S^{4k}$ the middle cohomology vanishes and the signature is $0$ for $k\geq1$; the signature operator's index is therefore $0$, and the $L$-genus of the sphere is $0$. For the complex projective space $\mathbb{CP}^{2k}$ the middle cohomology is one-dimensional and the signature is $1$; the total $L$-genus evaluates to $1$, which is the Todd genus of $\mathbb{CP}^{2k}$, in agreement with the fact that the signature and the holomorphic Euler characteristic coincide there.

**Example (dimension congruent to two).** For a closed oriented manifold of dimension $n\equiv2\pmod4$ the middle intersection form is alternating, its signature is $0$, and the $L$-genus has no term in the top degree; the signature operator still exists and is elliptic, and its index vanishes. The signature is a nontrivial invariant only in dimensions divisible by four, which is why the signature theorem is stated there.

## Summary

The **signature operator** of a closed oriented Riemannian manifold of even dimension $n=2m$ is $D=d+d^{*}$, the sum of the exterior derivative and its formal adjoint, read with the chirality $\tau=i^{k(k-1)+m}\star$, which is an involution with $\tau^2=\mathrm{id}$ and $\tau D\tau^{-1}=-D$. The operator is self-adjoint and elliptic, it is odd for the chirality, and its square is the **Hodge Laplacian**, $D^2=dd^{*}+d^{*}d=\Delta$, whose kernel is the space of harmonic forms and is isomorphic to the de Rham cohomology. On the middle forms of a $4k$-manifold the chirality is the Hodge star, and the harmonic middle forms split into the self-dual and anti-self-dual parts of dimensions $b_{+}$ and $b_{-}$.

The positive half $D^{+}:\Omega^{+}\to\Omega^{-}$ has index $b_{+}-b_{-}=\sigma(M)$, and the Atiyah–Singer theorem identifies this **signature** with the characteristic number $\int_M L(TM)$ of the Hirzebruch $L$-genus, whose first terms are $1+p_1/3+(7p_2-p_1^2)/45+\cdots$. The operator is assembled from the chosen metric — the star, the codifferential and the volume form all depend on it — while its index is a topological invariant, and the signature theorem is the statement of that independence. The graded operator on the even and odd forms instead has index the Euler characteristic. The examples are $S^4$, $\mathbb{CP}^2$ and $S^{2}\times S^{2}$ in dimension four and the $K3$ surface, whose signature is $-16$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(M,g)$, $n$, $\mathrm{vol}_g$ | Closed oriented Riemannian manifold, dimension, volume form |
| $\Omega^{k}(M)$, $\Omega^{\pm}(M)$ | Complexified $k$-forms, the two chirality eigenspaces |
| $\langle\alpha,\beta\rangle$ | Metric on forms; $(\alpha,\beta)=\int_M\alpha\wedge\star\bar\beta$ |
| $\star$ | Hodge star, $\star^2=(-1)^{k(n-k)}$ on $\Omega^{k}$ |
| $\tau=i^{k(k-1)+m}\star$ | Chirality, $\tau^2=\mathrm{id}$, $\tau D\tau^{-1}=-D$, $n=2m$ |
| $d$, $d^{*}=-\tau d\tau^{-1}$ | Exterior derivative, codifferential (formal adjoint) |
| $D=d+d^{*}$ | Signature operator; $D^{+}:\Omega^{+}\to\Omega^{-}$ |
| $\Delta=dd^{*}+d^{*}d=D^2$ | Hodge Laplacian |
| $\mathcal{H}^{k}(M)\cong H^{k}_{dR}(M)$ | Harmonic forms, de Rham cohomology, $b_k$ |
| $b_{\pm}$, $\sigma(M)=b_{+}-b_{-}$ | Dimensions of the self-dual and anti-self-dual harmonic middle forms, signature |
| $L(TM)=1+p_1/3+\cdots$ | Hirzebruch $L$-genus; $\sigma(M)=\int_ML(TM)$ |
| $\chi(M)=\operatorname{ind}(d+d^{*})$ | Euler characteristic as the index of the total-degree grading |

## Further Reading

- Friedrich Hirzebruch, *Topological Methods in Algebraic Geometry*, Classics in Mathematics (Springer, 1995), for the signature theorem, the $L$-genus and the multiplicative sequences.
- Michael F. Atiyah and Isadore M. Singer, "The index of elliptic operators I, III," *Annals of Mathematics* **87** (1968), 484–530 and 546–604, for the index of the signature operator and its characteristic-number form.
- Michael F. Atiyah and Raoul Bott, "A Lefschetz fixed point formula for elliptic complexes II: applications," *Annals of Mathematics* **88** (1968), 451–491, for the equivariant signature and the $G$-signature theorem.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the chirality, the Hodge star and the de Rham and signature complexes.
- Phillip A. Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the intersection form, the Hodge–Riemann relations and the signature of a projective manifold.
- Peter B. Gilkey, *Invariance Theory, the Heat Equation and the Atiyah–Singer Index Theorem* (CRC Press, 2nd ed. 1995), for the local index density of the signature operator and the $L$-class.
