
# __The Dirac Operator and Its Adjoint__

## Introduction

The Cauchy–Riemann operator of a spin manifold is assembled from two structures that the metric puts on the spinor bundle: the Clifford multiplication, which is skew-adjoint for the spinor inner product, and the spin connection, which is compatible with it. The product is **formally self-adjoint**: the adjoint of the operator is minus itself twice, hence the operator itself, and the self-adjointness is what makes the operator a Dirac-type operator in the analytic sense — discrete real spectrum, orthogonal eigenspinors, and two chiral halves that are mutual adjoints. The adjoint of the positive half is the negative half, $\operatorname{coker}D^{+}=\ker D^{-}$, and the index counts the chiral zero modes; the twisted operator and its adjoint satisfy the same identities with the twisted connection, and the square of the operator is the Lichnerowicz Laplacian, whose self-adjointness gives the vanishing theorem for the harmonic spinors.

The article treats the spinor inner product and the formal adjoint, the self-adjointness of the Cauchy–Riemann operator, the adjoint of the chiral halves and the resulting form of the index, the twisted operator and its adjoint, and the place of the adjoint in the Lichnerowicz formula and the vanishing theorem. The operator on the manifold, its chirality, the Lichnerowicz formula and the $\hat A$-genus are *The Dirac Operator on a Manifold*; the spin structure and the spinor bundle are *Spin Geometry*; the algebraic **Hermitian structure** of the operator — the module form, the self-adjointness on a Hermitian Clifford module, the spinor adjoint $s\mapsto(s,\cdot)$ and the Dirac adjoint $\bar\psi=\psi^{\dagger}\gamma_0$ — belongs to the Part II articles *Dirac Operators with Hermitian Adjoint* and *Spinor Adjoints and the Dirac Adjoint with Hermitian Adjoint*, and is cited here; the parallel article for the de Rham complex is *The Adjoint of the Signature Operator*.

The prerequisites are *The Dirac Operator on a Manifold* for the operator, the spinor bundle and the index; *Spin Geometry* for the spin connection and the Clifford multiplication; *The Formal Adjoint of a Differential Operator* and *The L2 Adjoint of a Differential Operator* for the formal and $L^{2}$ adjoints; *The Codifferential* and *The Adjoint of the Signature Operator* for the differential-geometric adjoint of a Dirac-type operator; *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*, *Dirac Operators with Hermitian Adjoint* and *Spinor Adjoints and the Dirac Adjoint with Hermitian Adjoint* for the algebraic Hermitian structure; and *The Atiyah–Singer Index Theorem and K-Theory* for the index. The analytic domain theory belongs to Part III and is cited; the metric is chosen. No physics is invoked.

## The Spinor Inner Product and the Formal Adjoint

Let $(M,g)$ be a closed spin manifold of dimension $n$, with spinor bundle $\mathcal{S}$ and Clifford multiplication $c:TM\otimes\mathcal{S}\to\mathcal{S}$, $c(v)^{2}=-|v|^{2}$. The spinor bundle carries a Hermitian metric $(\cdot,\cdot)_{\mathcal{S}}$, the **spinor inner product**, for which the Clifford multiplication is skew-adjoint,

$$
(c(v)s,t)_{\mathcal{S}}=-(s,c(v)t)_{\mathcal{S}},
$$

and the spin connection is compatible with the metric and with the Clifford multiplication,

$$
X(s,t)_{\mathcal{S}}=(\nabla^{\mathcal{S}}_{X}s,t)_{\mathcal{S}}+(s,\nabla^{\mathcal{S}}_{X}t)_{\mathcal{S}},\qquad
\nabla^{\mathcal{S}}_{X}\bigl(c(Y)s\bigr)=c(\nabla_{X}Y)s+c(Y)\nabla^{\mathcal{S}}_{X}s .
$$

The $L^{2}$ inner product on the spinors is

$$
\langle s,t\rangle=\int_{M}(s,t)_{\mathcal{S}}\,\mathrm{vol}_g ,
$$

a positive definite Hermitian form on $\Gamma(\mathcal{S})$.

**Theorem.** The **formal adjoint** of the Cauchy–Riemann operator $D=\sum_ic(e_i)\nabla^{\mathcal{S}}_{e_i}$, with respect to the spinor inner product, is

$$
D^{*}=\sum_i\nabla^{\mathcal{S},*}_{e_i}c(e_i)^{*}=\sum_i\Bigl(-\nabla^{\mathcal{S}}_{e_i}-\operatorname{div}e_i\Bigr)\bigl(-c(e_i)\bigr)=D ,
$$

the divergence term vanishing on a closed manifold; hence $D$ is **formally self-adjoint**, $D^{*}=D$. The adjoint of the operator with respect to the module form of a Hermitian Clifford module is the same statement algebraically, and it is the content of *Dirac Operators with Hermitian Adjoint*.

**Proof.** The formal adjoint of a composition is the composition of the adjoints in reverse order; the adjoint of $\nabla^{\mathcal{S}}_{e_i}$ is $-\nabla^{\mathcal{S}}_{e_i}-\operatorname{div}e_i$, and the adjoint of $c(e_i)$ is $-c(e_i)$ for the spinor metric; the divergence integrates to zero on a closed manifold, and the two minus signs cancel, leaving $\sum_ic(e_i)\nabla^{\mathcal{S}}_{e_i}=D$. The algebraic form of the identity is the self-adjointness of the Dirac operator on a Hermitian Clifford module, which is the theorem of *Dirac Operators with Hermitian Adjoint*. $\square$

**Remark.** The two factors contribute two skew-adjoint properties: the Clifford multiplication is skew-adjoint and the covariant derivative is skew-adjoint up to the divergence, and the product of two skew-adjoint operators is self-adjoint. This is exactly the mechanism of *Dirac Operators with Hermitian Adjoint*, where the operator is the product of the skew-adjoint Clifford action and a formally skew-adjoint first-order operator; the differential-geometric statement is the same identity with the spin connection in place of the abstract first-order operator.

## Self-Adjointness of the Cauchy–Riemann Operator

**Theorem.** On a closed spin manifold the Cauchy–Riemann operator is self-adjoint as an unbounded operator on $L^{2}(\mathcal{S})$ with domain the Sobolev space $H^{1}(\mathcal{S})$; its spectrum is real and discrete, its eigenspinors form a complete orthonormal basis, and its square satisfies $D^{2}\geq0$ with $\ker D=\ker D^{2}$ the space of harmonic spinors.

**Proof.** The formal self-adjointness of the preceding theorem and the ellipticity of $D$, whose symbol $\sigma_D(\xi)=i\,c(\xi)$ is invertible for $\xi\neq0$, make $D$ a closed self-adjoint operator with compact resolvent on the closed manifold; the completeness is the spectral theorem for self-adjoint operators with compact resolvent, and $D^{2}\geq0$ because $D$ is self-adjoint. The equivalence $\ker D=\ker D^{2}$ is $(D^{2}s,s)=\|Ds\|^{2}$. The domain theory is that of *The L2 Adjoint of a Differential Operator* and of *Dirac Operators with Hermitian Adjoint*. $\square$

**Theorem (spectral symmetry).** In even dimensions the chirality $\tau$ anticommutes with the operator, $\tau D\tau^{-1}=-D$, so the spectrum is symmetric about the origin: if $D s=\lambda s$ then $D(\tau s)=-\lambda(\tau s)$, and the nonzero eigenvalues occur in pairs $\pm\lambda$ with eigenspinors exchanged by the chirality; the kernel is graded by $\tau$ into the two chiral zero-mode spaces.

**Proof.** The anticommutation was established in *The Dirac Operator on a Manifold*; applying $D$ to $\tau s$ and using $\tau D=-D\tau$ gives the pairing, and the grading of the kernel is the eigenvalue decomposition of the involution $\tau$ on $\ker D$. $\square$

## The Adjoint of the Chiral Halves and the Index

**Theorem.** In even dimensions the operator is odd for the chirality and splits into the two halves

$$
D^{+}:\Gamma(\mathcal{S}^{+})\to\Gamma(\mathcal{S}^{-}),\qquad
D^{-}:\Gamma(\mathcal{S}^{-})\to\Gamma(\mathcal{S}^{+}),
$$

which are mutual adjoints,

$$
(D^{+})^{*}=D^{-},\qquad
\operatorname{coker}D^{+}=\ker(D^{+})^{*}=\ker D^{-},
$$

and the index of the positive half is the difference of the chiral zero-mode spaces,

$$
\operatorname{ind}D^{+}=\dim\ker D^{+}-\dim\ker D^{-}=\int_{M}\hat A(TM),
$$

the $\hat A$-genus of the spin manifold.

**Proof.** The oddness of $D$ for the chirality restricts it to the two halves; the adjoint of $D^{+}$ is the restriction of the adjoint $D^{*}=D$ to the opposite chirality, namely $D^{-}$; the cokernel of $D^{+}$ is the kernel of its adjoint by the Fredholm alternative, which is $\ker D^{-}$; and the identification of the index with the $\hat A$-genus is the Atiyah–Singer theorem of *The Dirac Operator on a Manifold*. $\square$

**Corollary.** The index of the positive half is the trace of the chirality on the kernel,

$$
\operatorname{ind}D^{+}=\operatorname{tr}(\tau\mid\ker D),
$$

the difference of the dimensions of the two chiral zero-mode spaces; unlike the signature operator on the de Rham complex, there is no contribution from other degrees, because the operator acts on the single spinor bundle, and the kernel splits directly into the two chirality eigenspaces. The spectral symmetry of the preceding theorem pairs the nonzero eigenvalues and their eigenspinors, so the index is entirely carried by the zero modes.

## The Twisted Operator and Its Adjoint

**Definition.** Let $E\to M$ be a Hermitian vector bundle with connection $\nabla^{E}$ and curvature $F^{E}$. The **twisted Cauchy–Riemann operator** is

$$
D_{E}=\sum_{i}c(e_i)\,\nabla^{\mathcal{S}\otimes E}_{e_i}:\Gamma(\mathcal{S}\otimes E)\to\Gamma(\mathcal{S}\otimes E),
$$

the operator of the connection $\nabla^{\mathcal{S}}\otimes1+1\otimes\nabla^{E}$; it is the operator with coefficients in the Clifford module $E$, in the sense of *Clifford Modules and the Twisted Cauchy–Riemann Operator*.

**Theorem.** The twisted operator is formally self-adjoint, $D_{E}^{*}=D_{E}$; in even dimensions it is odd for the chirality of the spinor factor and splits into the mutually adjoint halves $(D_{E}^{+})^{*}=D_{E}^{-}$, with index

$$
\operatorname{ind}D_{E}^{+}=\int_{M}\hat A(TM)\operatorname{ch}(E),
$$

the $\hat A$-genus paired with the Chern character of the twisting bundle; the twisted square satisfies the Weitzenböck formula

$$
D_{E}^{2}=\nabla^{\mathcal{S}\otimes E,*}\nabla^{\mathcal{S}\otimes E}+\mathcal{R}^{E},\qquad
\mathcal{R}^{E}=\tfrac14\operatorname{scal}\cdot\mathrm{id}+c(F^{E}),
$$

the Lichnerowicz curvature of the twisting.

**Proof.** The formal self-adjointness is the same computation as for the untwisted operator, with the connection $\nabla^{\mathcal{S}\otimes E}$ in place of $\nabla^{\mathcal{S}}$ and the metric on $E$ in place of the spinor metric; the twisted Weitzenböck formula and the twisted index are those of *Clifford Modules and the Twisted Cauchy–Riemann Operator* and *The Dirac Operator on a Manifold*. $\square$

**Remark.** The adjoint of the twisted operator is computed with the adjoint of the twisting connection, which is $-\nabla^{E}-\operatorname{div}$; the twisting curvature enters the square through the Clifford multiplication of the two-form $F^{E}$, and the sign convention is the one of *Clifford Modules and the Twisted Cauchy–Riemann Operator*.

## The Adjoint and the Lichnerowicz Formula

**Theorem.** The square of the Cauchy–Riemann operator is the self-adjoint Lichnerowicz Laplacian

$$
D^{2}=\nabla^{*}\nabla+\tfrac14\operatorname{scal}\cdot\mathrm{id},
$$

whose adjoint is itself, $D^{2,*}=D^{2}$; for a harmonic spinor $\psi$ the formula gives the Bochner identity

$$
0=\|D\psi\|^{2}=\|\nabla\psi\|^{2}+\tfrac14\int_{M}\operatorname{scal}|\psi|^{2},
$$

and the vanishing theorem follows: a closed spin manifold of positive scalar curvature has no nonzero harmonic spinor, and its operator has no chiral zero modes.

**Proof.** The square of the self-adjoint operator $D$ is self-adjoint with $(D^{2})^{*}=D^{*}D^{*}=D^{2}$; the Lichnerowicz formula is that of *The Dirac Operator on a Manifold* and *Spin Geometry*; integrating the formula against $\psi$ and using the compatibility of the connection with the metric gives the Bochner identity, and the positivity of the scalar curvature forces $\|\nabla\psi\|^{2}=0$ and $\psi=0$. $\square$

**Corollary (the adjoint and the index).** The self-adjointness of $D^{2}$ makes the harmonic spinors the kernel of the self-adjoint positive operator $D^{2}$, and the index of $D^{+}$ is the index of the pair (kernel of $D^{2}$, chirality); in particular the index is unchanged by the adjoint operation, $\operatorname{ind}(D^{+})^{*}=\operatorname{ind}D^{-}=-\operatorname{ind}D^{+}$, and the vanishing of the index is the vanishing of the chiral zero modes.

## The Hermitian Structure of the Adjoint

The differential-geometric self-adjointness is the analytic shadow of the algebraic Hermitian structure of the Clifford module, and the corpus has built that structure in Part II.

**Theorem (algebraic form).** On a Hermitian Clifford module the Dirac operator is self-adjoint for the module form, its square is a positive operator, its spectrum is real and its eigenspinors are orthogonal; the **spinor adjoint** $s\mapsto(s,\cdot)$ is the Clifford-equivariant identification of the module with its dual, and the **Dirac adjoint** $s,t\mapsto\operatorname{Sc}(s^{\dagger}\gamma t)$ is the pairing obtained by inserting a fixed vector before the form, whose scalar part $\bar\psi\psi$ is invariant. The differential-geometric operator $D$ of a spin manifold is the curved-space member of the same family, with the module form the fibrewise spinor inner product and the identification with the dual the metric on $\mathcal{S}$.

**Proof.** The algebraic statements are those of *Dirac Operators with Hermitian Adjoint* and *Spinor Adjoints and the Dirac Adjoint with Hermitian Adjoint*; the passage to the manifold is the passage from a module to a bundle of modules, and the module form becomes the fibrewise Hermitian metric integrated against the volume form. $\square$

**Remark.** The two adjoints are distinct: the **spinor adjoint** is the conjugate-linear metric identification of the spinors with their dual, the analytic object that gives the $L^{2}$ inner product, while the **Dirac adjoint** is the bilinear pairing with the inserted vector, the invariant pairing of the spinor module. Both are the Hermitian structure of the operator, and the self-adjointness is stated for the first and the invariant form $\bar\psi\psi$ for the second.

## Examples

**Example (the flat torus).** On the flat torus $T^{n}$ with the product spin structure the spinor bundle is trivial and the operator is the constant-coefficient operator $D=\sum_ic(e_i)\partial_i$; it is self-adjoint, its adjoint is itself, its spectrum is the set of $\pm|\xi|$ for the Fourier modes $\xi$, and the nonzero eigenvalues occur in opposite pairs; the kernels of $D^{\pm}$ have equal dimension and the index vanishes, as the $\hat A$-genus of a flat torus does.

**Example (the round sphere).** On $S^{n}$ with the round metric the operator is self-adjoint with $\tau D\tau^{-1}=-D$, so its spectrum is symmetric; the square is the Lichnerowicz Laplacian with the constant positive scalar curvature, and the vanishing theorem gives the absence of harmonic spinors; the adjoint of $D^{+}$ is $D^{-}$ and the index is zero.

**Example (a $K3$ surface).** On a $K3$ surface the operator is self-adjoint with index $\hat A[K3]=2$; the kernels of $D^{+}$ and $D^{-}$ have dimensions differing by $2$, and the spectral symmetry pairs the nonzero eigenvalues. The twisted operator $D_{E}$ has index $\int\hat A\operatorname{ch}(E)$; with $E$ the trivial bundle the untwisted value $2$ is recovered.

**Example (the twisted operator and the vanishing).** For a line bundle $L$ of negative degree over a Riemann surface of genus $g$ the twisted operator has vanishing kernel, and its index is by Riemann–Roch the Euler characteristic $\deg L+1-g$; the adjoint's kernel is therefore of dimension $g-1-\deg L$. The example shows the chiral asymmetry of the two kernels and the role of the adjoint in computing the index.

## Summary

The **Cauchy–Riemann operator** $D=\sum_ic(e_i)\nabla^{\mathcal{S}}_{e_i}$ of a spin manifold, classically the **Dirac operator**, is **formally self-adjoint**, $D^{*}=D$, because the Clifford multiplication is skew-adjoint for the spinor metric and the spin connection is compatible with it, and the divergence vanishes on a closed manifold; it is self-adjoint as an unbounded operator with discrete real spectrum, orthogonal eigenspinors and $D^{2}\geq0$. In even dimensions the chirality makes the operator odd, splitting it into the **mutually adjoint** halves $(D^{+})^{*}=D^{-}$, with $\operatorname{coker}D^{+}=\ker D^{-}$ and index $\operatorname{ind}D^{+}=\operatorname{tr}(\tau\mid\ker D)=\int_M\hat A(TM)$; the spectrum is symmetric about the origin and the index is carried by the chiral zero modes alone. The **twisted operator** $D_{E}$ is self-adjoint with the same identities, the index $\int_M\hat A\operatorname{ch}(E)$ and the Weitzenböck square $\mathcal{R}^{E}=\tfrac14\operatorname{scal}+c(F^{E})$; the **Lichnerowicz formula** $D^{2}=\nabla^{*}\nabla+\tfrac14\operatorname{scal}$ is self-adjoint and gives the Bochner identity and the vanishing theorem for positive scalar curvature. The differential-geometric adjoint is the curved form of the algebraic **Hermitian structure** of *Dirac Operators with Hermitian Adjoint* and *Spinor Adjoints and the Dirac Adjoint with Hermitian Adjoint*: the spinor adjoint is the metric identification giving the $L^{2}$ inner product, the Dirac adjoint is the invariant pairing $\bar\psi\psi$ with the inserted vector, and the operator is self-adjoint for the module form in both cases.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\cdot,\cdot)_{\mathcal{S}}$, $\langle s,t\rangle$ | Spinor inner product and its $L^{2}$ form |
| $c(v)^{*}=-c(v)$ | Clifford multiplication is skew-adjoint |
| $D=\sum_ic(e_i)\nabla^{\mathcal{S}}_{e_i}$, $D^{*}=D$ | Cauchy–Riemann operator; formally self-adjoint |
| $\tau D\tau^{-1}=-D$ | Chirality anticommutation; symmetric spectrum $\pm\lambda$ |
| $(D^{+})^{*}=D^{-}$, $\operatorname{coker}D^{+}=\ker D^{-}$ | Mutually adjoint chiral halves |
| $\operatorname{ind}D^{+}=\operatorname{tr}(\tau\mid\ker D)=\int_M\hat A(TM)$ | Index as the chirality trace |
| $D_{E}=\sum_ic(e_i)\nabla^{\mathcal{S}\otimes E}_{e_i}$, $D_{E}^{*}=D_{E}$ | Twisted operator, self-adjoint |
| $D_{E}^{2}=\nabla^{E,*}\nabla^{E}+\mathcal{R}^{E}$, $\mathcal{R}^{E}=\tfrac14\operatorname{scal}+c(F^{E})$ | Twisted Weitzenböck/Lichnerowicz formula |
| $D^{2}=\nabla^{*}\nabla+\tfrac14\operatorname{scal}$; $0=\|\nabla\psi\|^{2}+\tfrac14\int\operatorname{scal}|\psi|^{2}$ | Lichnerowicz formula and Bochner identity |
| $s\mapsto(s,\cdot)$; $s,t\mapsto\operatorname{Sc}(s^{\dagger}\gamma t)$ | Spinor adjoint; Dirac adjoint |

## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the spinor inner product, the self-adjointness and the Lichnerowicz formula.
- Thomas Friedrich, *Dirac Operators in Riemannian Geometry*, Graduate Studies in Mathematics 25 (American Mathematical Society, 2000), for the self-adjointness, the spectrum and the twisted operators.
- Michael F. Atiyah and Isadore M. Singer, "The index of elliptic operators I, III," *Annals of Mathematics* **87** (1968), 484–530 and 546–604, for the index of the chiral operator and the $\hat A$-genus.
- Nicole Berline, Ezra Getzler and Michèle Vergne, *Heat Kernels and Dirac Operators* (Springer, 1992), for the self-adjointness, the heat kernel and the local index theorem.
- André Lichnerowicz, "Spineurs harmoniques," *Comptes Rendus de l'Académie des Sciences* **257** (1963), 7–9, for the formula $D^{2}=\nabla^{*}\nabla+\tfrac14\operatorname{scal}$ and the vanishing of the harmonic spinors.
- John Roe, *Elliptic Operators, Topology and Asymptotic Methods*, Pitman Research Notes in Mathematics 179 (Longman, 1988), for the differential-geometric adjoints, the domains and the elliptic theory.
