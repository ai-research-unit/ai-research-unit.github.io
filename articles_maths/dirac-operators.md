
# __Dirac Operators__

## Introduction

A Dirac operator is a formally self-adjoint first-order elliptic operator whose square is a Laplace-type operator. In this corpus the flat operator $e_\mu\partial_\mu$ is named the **Cauchy–Riemann operator**; the classical name *Dirac operator*, glossed once in *Clifford Analysis*, is reserved for the family of operators studied here: the operator $D=\sum_\mu c_\mu\partial_\mu+\cdots$ assembled from Clifford multiplication by the coefficients of a connection, including the spin Dirac operator of a Riemannian manifold, its twists by auxiliary bundles, and its flat Euclidean model. The present article treats that family as mathematics.

The content of the article is the **analytic theory** of these operators: formal self-adjointness and essential self-adjointness, the domain and the closure, the spectrum and its structure, the compactness of the resolvent on a closed manifold, the finite-dimensionality of the kernel, and the relation between the operator and the index of its chiral part. The geometric constructions — spin structures, Clifford modules, the Lichnerowicz formula as a geometric identity, the Atiyah–Singer theorem — belong to Part II and are cited; the article states the analysis that those constructions support, and it states it for the general Dirac-type operator before specialising to the flat model and to examples whose spectrum can be computed exactly.

The boundaries are these. The flat Cauchy–Riemann operator of the corpus, with its scalar direction and its one-sided regularity, is *Clifford Analysis*; here the same operator appears as the flat model of the self-adjoint family, and the difference between the two — the presence of the scalar direction, which makes the corpus operator elliptic but not symmetric — is stated once and then set aside. The spectral theorem for unbounded self-adjoint operators and the theory of the graph and the adjoint are *Unbounded Operators and Spectral Measures*, and the Fredholm theory and the index of an elliptic operator are *Fredholm Theory* and the Part II article on the Atiyah–Singer theorem; all three are cited. Spinors, Clifford modules and the twisted operator's elliptic complex are Part II. The article is mathematics: \(D\) is an operator on sections of a bundle over a Riemannian manifold, and no physical reading of it is used.

## The Family of Dirac-Type Operators

### Clifford Multiplication and the Definition

Let $M$ be a Riemannian manifold of dimension $m$ with metric $g$, and let $S\to M$ be a bundle of modules over the Clifford bundle $\mathrm{Cl}(TM,g)$; the fibre $S_x$ is a Clifford module over $\mathrm{Cl}(T_xM,g_x)$, as in *Clifford Modules and the Twisted Cauchy–Riemann Operator*. Write $c(\xi)$ for Clifford multiplication by a tangent vector $\xi$, so that

$$
c(\xi)c(\eta)+c(\eta)c(\xi)=-2g(\xi,\eta)\,1_S ,
$$

the sign convention being the one of the flat Euclidean Clifford algebra with $e_i^2=-1$ used throughout the corpus. Suppose $S$ carries a Hermitian metric $\langle\cdot,\cdot\rangle$ with respect to which every $c(\xi)$ is skew, $c(\xi)^*=-c(\xi)$; such a metric exists for a Clifford module and is the metric in which the theory below is stated. Let $\nabla$ be a connection on $S$ compatible with the Clifford action, meaning $\nabla_\xi(c(\eta)s)=c(\nabla^{TM}_\xi\eta)s+c(\eta)\nabla_\xi s$, where $\nabla^{TM}$ is the Levi-Civita connection.

**Definition.** The **Dirac operator** associated with the pair $(S,\nabla)$ is the composition of the connection with Clifford multiplication,

$$
D = \sum_{j=1}^{m}c(e_j)\,\nabla_{e_j} ,
$$

where $e_1,\dots,e_m$ is a local orthonormal frame; the sum is independent of the frame. An operator is of **Dirac type** if it is $D$ plus an endomorphism of $S$ (a zeroth-order term).

**Remark (why the definition is framed this way).** Three properties are built into it. The coefficients are Clifford multiplications, so the symbol of $D$ is $c(\xi)$ and satisfies $c(\xi)^2=-|\xi|^2$, which is elliptic and makes the square of the symbol a scalar; the connection is compatible, so differentiating a Clifford product obeys the Leibniz rule; and the fibre metric makes each coefficient skew, which is exactly the condition for $D$ to be formally self-adjoint. Any one of the three is a hypothesis that fails in an interesting way for a general first-order operator, and the corpus's Cauchy–Riemann operator fails the third, as the last section records.

**Remark (the geometric input).** A spin structure on $M$ and the spinor bundle $\Sigma M$ give the fundamental pair $(S,\nabla)$ with $S=\Sigma M$ and $\nabla$ the spin connection; the resulting $D$ is the **spin Dirac operator**, the operator of *Spin Geometry*. A Clifford module and a Clifford connection give the twisted operator $D_E$ of *Clifford Modules and the Twisted Cauchy–Riemann Operator*, whose square carries the curvature of the twist, and whose associated elliptic complex has an index. The constructions are Part II's; what the present article does with them is to analyse the operator.

### The Weitzenböck Identity and the Square

**Theorem (Weitzenböck–Lichnerowicz).** For the Dirac operator of a Clifford module with a Clifford connection,

$$
D^2 = \nabla^*\nabla+\mathcal{R} ,
$$

where $\nabla^*\nabla=-\sum_j\nabla_{e_j}\nabla_{e_j}+\cdots$ is the connection Laplacian (a nonnegative operator) and $\mathcal{R}$ is the endomorphism of $S$ determined by the curvature of $\nabla$ and, in the spin case, by the scalar curvature: $\mathcal{R}=\tfrac14\mathrm{scal}\cdot1_S$ for the spin Dirac operator.

*Proof.* Quoted as standard. The proof expands $D^2$ in a local frame, uses the Clifford relations to isolate the second-order part, recognises the second-order part as the connection Laplacian up to the zeroth-order term produced by the frame derivatives, and identifies the remaining first-order term as an endomorphism via the Clifford relations. That the remaining term is a scalar multiple of the identity in the spin case is the Lichnerowicz computation. $\square$

**Corollary (spectral consequences).** If $\mathcal{R}\ge0$ as an endomorphism, then $D^2\ge0$ and $\ker D=\ker D^2$ consists of the parallel sections annihilated by $\mathcal{R}$; in particular if the scalar curvature of a spin manifold is positive then the spin Dirac operator has no harmonic spinors.

*Proof.* For a self-adjoint $D$, $\langle D^2s,s\rangle=\|Ds\|^2\ge0$, and the identity gives $\|Ds\|^2=\langle\nabla^*\nabla s,s\rangle+\langle\mathcal{R}s,s\rangle=\|\nabla s\|^2+\langle\mathcal{R}s,s\rangle$; both terms are nonnegative under the hypothesis, and the sum vanishes only if both do. $\square$

## Self-Adjointness

### The Flat Model

The flat case is the model on which every statement can be checked by Fourier analysis. Let $M=\mathbb{R}^m$ with the Euclidean metric, let $\mathcal{S}$ be a module over $\mathrm{Cl}_{0,m}$ with a Hermitian metric for which $e_1,\dots,e_m$ are skew, and let $D=\sum_{j=1}^{m}e_j\partial_j$ act on $C_c^\infty(\mathbb{R}^m;\mathcal{S})$.

**Proposition (formal self-adjointness).** For $f,g\in C_c^\infty(\mathbb{R}^m;\mathcal{S})$,

$$
\langle Df,g\rangle = \langle f,Dg\rangle .
$$

*Proof.* Since $e_j$ is skew and constant, $\langle e_j\partial_jf,g\rangle=-\langle\partial_jf,e_jg\rangle$; integrating by parts, the boundary term vanishing for compact support, gives $+\langle f,e_j\partial_jg\rangle$, and summing over $j$ gives the claim. $\square$

**Theorem (essential self-adjointness and domain).** The operator $D$ with domain $C_c^\infty$ is essentially self-adjoint; its closure has domain the Sobolev space $H^1(\mathbb{R}^m;\mathcal{S})$ and is self-adjoint with $D^2=-\Delta$, the positive Laplacian.

*Proof.* The Clifford relations give $D^2=\sum_{j,k}e_je_k\partial_j\partial_k=\sum_je_j^2\partial_j^2=-\Delta$, since the off-diagonal terms cancel. Hence for $f\in C_c^\infty$,

$$
\|Df\|^2 = \langle D^2f,f\rangle = \langle-\Delta f,f\rangle = \|\nabla f\|^2 ,
$$

so the graph norm $\|f\|^2+\|Df\|^2$ is equivalent to the $H^1$ norm. A symmetric operator whose graph norm is equivalent to a norm in which the space is complete has a self-adjoint closure with that domain; the adjoint has the same domain because the formal adjoint and $D$ coincide on $C_c^\infty$ and the boundary terms at infinity vanish for $H^1$ functions. $\square$

**Theorem (the spectrum of the flat model).** The self-adjoint operator $D$ has spectrum $\mathbb{R}$, purely absolutely continuous, with no eigenvalues; the unitary Fourier transform diagonalises it,

$$
\widehat{Df}(\xi) = i\,\sigma(\xi)\,\hat f(\xi) , \qquad \sigma(\xi)=\sum_{j=1}^{m}e_j\xi_j ,
$$

and the multiplier $i\sigma(\xi)$ is Hermitian with eigenvalues $\pm|\xi|$.

*Proof.* The Fourier transform is unitary on $L^2(\mathbb{R}^m;\mathcal{S})$ and turns $\partial_j$ into multiplication by $i\xi_j$, hence $D$ into multiplication by $i\sigma(\xi)$. Since $\sigma(\xi)^2=-|\xi|^2$ and $e_j$ is skew, $i\sigma(\xi)$ is Hermitian, so it is diagonalisable with real eigenvalues; its eigenvalues are the square roots of $|\xi|^2$, namely $\pm|\xi|$. The spectrum of a direct-integral multiplication operator is the closure of the union of the spectra of its fibres, here $\overline{\bigcup_{\xi}\{-|\xi|,|\xi|\}}=\mathbb{R}$. There are no eigenvalues because the fibres are invertible for $\xi\neq0$; absolute continuity follows from the explicit direct-integral form. $\square$

**Corollary (Weyl-type asymptotics on a torus).** On the flat torus $\mathbb{T}^m=\mathbb{R}^m/\mathbb{Z}^m$, with the same operator acting on smooth sections, the spectrum is $\{\pm|\xi|:\xi\in\mathbb{Z}^m\}$ with the multiplicities of the fibre eigenvalues, and the counting function satisfies $\#\{\text{eigenvalues of }|D|\le\lambda\}\sim c_m\lambda^m$ with $c_m$ the volume of the unit ball; this is Weyl's law for a first-order elliptic operator, in which the exponent is the dimension, not half of it.

*Proof.* The spectrum of the torus operator is the union of the spectra of the constant-coefficient operators on the Fourier modes, which are the fibres at integer frequencies; the counting statement is the standard lattice-point count for the ball of radius $\lambda$, with the multiplicity of the Clifford module as a constant. $\square$

**Example (the circle).** For $m=1$ and $\mathcal{S}=\mathbb{C}$ with $e_1=i$, the operator is $D=i\,d/d\theta$ and the eigenfunctions are $e^{in\theta}$ with eigenvalues $-n$, so the spectrum is $\mathbb{Z}$ with multiplicity one: $D$ is self-adjoint, its spectrum is discrete, and the resolvent is compact. This is the smallest Dirac operator, and it shows that self-adjointness and nonnegativity are independent: $D^2\ge0$ while $D$ has both signs.

### The General Case

**Theorem (self-adjointness on a complete manifold).** Let $M$ be complete and $S$ a Clifford module with a Clifford connection and a Hermitian metric making the Clifford coefficients skew. Then the Dirac operator $D$, defined on $C_c^\infty(M;S)$, is essentially self-adjoint, and its closure has domain the first Sobolev space $H^1(M;S)$.

*Proof.* Quoted as standard (Chernoff; the argument of the flat case, with the graph norm of $D$ recognised as a first-order elliptic graph norm and completeness replacing the Fourier argument). The essential point is that the symbol is skew-Hermitian, so the formal adjoint is $D$ itself, and that $D^2$ is a Laplace-type operator with a positive leading part, so the graph norm is controlled by the elliptic norm. $\square$

**Remark (when self-adjointness can fail).** The hypotheses are not automatic. A connection that is not Clifford-compatible, an indefinite metric on the fibres, or a non-complete manifold can produce an operator that is merely symmetric with unequal deficiency indices; the self-adjoint extensions are then indexed by boundary data at infinity, and different extensions have different spectra. The deficiency index computation and the parametrisation of the self-adjoint extensions are the theory of *Unbounded Operators and Spectral Measures*; what the Dirac setting supplies is the geometric meaning of the boundary data.

## The Spectrum on a Closed Manifold

**Theorem (compact resolvent and discreteness).** Let $M$ be closed and let $D$ be a Dirac-type operator on a Clifford module. Then $D$ is self-adjoint with domain $H^1(M;S)$, its resolvent is compact, its spectrum is a discrete subset of $\mathbb{R}$ without finite accumulation point, each eigenspace is finite-dimensional, and the eigenvalues form an unbounded two-sided sequence $\lambda_1\le\lambda_2\le\cdots$, $\lambda_k\to+\infty$ and $\lambda_{-k}\to-\infty$.

*Proof.* A self-adjoint elliptic operator on a closed manifold has compact resolvent: the domain embeds compactly in $L^2$ by the Rellich–Kondrachov theorem, so the resolvent is the composition of a bounded map into $H^1$ with a compact embedding. Compact self-adjointness gives a discrete spectrum with finite-dimensional eigenspaces; ellipticity gives the regularity of the eigenfunctions, and the two-sidedness follows from $c(\xi)\mapsto -c(\xi)$ symmetry. $\square$

**Definition.** Suppose $S=S^+\oplus S^-$ is a $\mathbb{Z}_2$-grading by which every $c(\xi)$ reverses the summands — the **chirality** splitting. Then $D$ is odd with respect to the grading,

$$
D = \begin{pmatrix}0&D^-\\ D^+&0\end{pmatrix} , \qquad D^\pm:\Gamma(S^\pm)\to\Gamma(S^\mp) ,
$$

and each of $D^\pm$ is elliptic.

**Theorem (Fredholm and index).** In the situation above, $D^\pm$ are Fredholm operators between the Sobolev spaces, $\ker D^\pm$ are finite-dimensional, and

$$
\operatorname{ind}D^+ = \dim\ker D^+-\dim\ker D^- = \dim\ker D^+-\dim\mathrm{coker}\,D^+
$$

is unchanged by continuous deformations of the operator within the class of Dirac-type operators; it is the **analytic index** of the pair. The chiral Dirac operator has compact resolvent and its index is a topological invariant, computed by the Atiyah–Singer theorem of *The Atiyah–Singer Index Theorem and K-Theory*.

*Proof.* The Fredholm property and the stability of the index under deformation are the general theory of *Fredholm Theory*; ellipticity gives the finite-dimensionality of the kernel and the cokernel. The identification of the index with a topological invariant is the Atiyah–Singer theorem, quoted from Part II. $\square$

**Remark (the index as a spectral asymmetry).** The index of $D^+$ measures the asymmetry of the spectrum of $D$ about the origin: it is the difference between the number of zero eigenvalues in the two chiral halves. The heat-kernel proof of the index theorem computes it from the small-time asymptotics of the heat kernel of $D^2$; the local form of the computation and the characteristic classes that appear are Part II's. For the spin Dirac operator on a spin manifold, the index of $D^+$ is the $\hat A$-genus, and the Lichnerowicz corollary of the Weitzenböck identity shows that it vanishes whenever the scalar curvature is positive.

**Example (spectra on low-dimensional closed manifolds).** On $S^1$ the spectrum of $D=i\,d/d\theta$ is $\mathbb{Z}$, as above. On the flat torus $\mathbb{T}^m$ the spectrum is $\{\pm|\xi|:\xi\in\mathbb{Z}^m\}$. On the round sphere $S^2$ with its spin structure the Dirac operator has spectrum the nonzero integers $\pm1,\pm2,\dots$, again symmetric about zero and growing linearly; there is no zero eigenvalue, as the Lichnerowicz corollary requires, since the round sphere has positive scalar curvature, and the vanishing of the index in dimension two is the symmetry of the spectrum about the origin rather than the presence of a harmonic spinor. On $S^4$ the same computation exhibits a nonzero index for the twisted operator with a suitable twist, which is the analytic content of the index theorem in that dimension.

## The Flat Cauchy–Riemann Operator

The corpus's flat operator and the self-adjoint operator of this article differ in one coordinate direction, and the difference is worth isolating.

**Remark (the scalar direction).** Let $A=\mathrm{Cl}_{0,m}$ and let $D=\partial_0+\sum_{j=1}^{m}e_j\partial_j$ be the Cauchy–Riemann operator of *Clifford Analysis*. Its coefficients are $1,e_1,\dots,e_m$: the vector coefficients are skew for the standard metric on the module, but the coefficient $1$ of the scalar direction is Hermitian and not skew. Consequently the formal adjoint is not $D$ but $-\partial$, where $\partial=\partial_0-\sum_je_j\partial_j$ is the conjugate operator: integration by parts gives

$$
\langle Df,g\rangle = -\langle f,\partial_0g\rangle+\sum_{j=1}^{m}\langle f,e_j\partial_jg\rangle = \Bigl\langle f,\Bigl(-\partial_0+\sum_{j=1}^{m}e_j\partial_j\Bigr)g\Bigr\rangle ,
$$

so $D^*=-\partial$, where $\partial=\partial_0-\sum_je_j\partial_j$ is the conjugate operator. Splitting into Hermitian parts, the self-adjoint part of $D$ is the vector operator $D_{\mathrm{sa}}=\sum_je_j\partial_j$ and its skew-adjoint part is $\partial_0$. The operator $D$ is elliptic — its symbol is invertible, as *Regularity and the Cauchy–Riemann Operator* shows — but it is not symmetric, and it is the sum of a self-adjoint and a skew-adjoint operator, so it is not normal either; the self-adjoint Dirac operator of the family is $D_{\mathrm{sa}}$, and the corpus's operator is the same operator with one direction treated as a Hermitian rather than an anti-Hermitian coefficient.

**Remark (the two factorisations).** Both facts can be read in one line. The corpus's operator satisfies $D\bar D=\bar DD=\Delta$, so its square with its conjugate is the Laplacian; the self-adjoint vector operator satisfies $D_{\mathrm{sa}}^2=-\Delta$, so its own square is the Laplacian. In the first case the Laplacian is produced by a product of two distinct operators and the individual operator has no spectral theory of the usual self-adjoint kind; in the second the Laplacian is produced by the square of one self-adjoint operator, whose spectral theory is the subject of this article. The two theories are the two faces of the factorisation of the Laplacian, and the passage between them is the passage between a Hermitian and an anti-Hermitian treatment of the scalar coordinate.

**Remark (the twisted operator and the general principle).** Replacing the spinor bundle by a Clifford module and the connection by a Clifford connection produces the twisted operator, whose square is the connection Laplacian plus the twist curvature; the analytic statements of this article — essential self-adjointness, discreteness of the spectrum on a closed manifold, the Fredholm and index theory of the chiral part — apply verbatim, and the geometric content enters only through the endomorphism $\mathcal R$ in the Weitzenböck formula. This is the sense in which the Dirac operator is a family and not a single object: the analysis is uniform, and the geometry is carried by the twist.

## Summary

A Dirac-type operator is $D=\sum_jc(e_j)\nabla_{e_j}+$zeroth order, with Clifford multiplication by an orthonormal frame and a Clifford connection, the coefficients being skew for the fibre metric; the spin Dirac operator and the twisted Dirac operator of a Clifford module are the two fundamental examples, and the constructions of the bundles and the Lichnerowicz formula as a geometric identity are Part II's. The Weitzenböck identity $D^2=\nabla^*\nabla+\mathcal R$ makes the square a Laplace-type operator; for the spin Dirac operator $\mathcal R=\tfrac14\mathrm{scal}$, and positive scalar curvature kills the harmonic spinors. The flat model $D=\sum_je_j\partial_j$ on $\mathbb{R}^m$ is essentially self-adjoint on $C_c^\infty$, with closure the self-adjoint operator on $H^1$ and with $D^2=-\Delta$; its spectrum is all of $\mathbb{R}$, purely absolutely continuous, with no eigenvalues, and the Fourier transform diagonalises it as multiplication by the Hermitian multiplier $i\sigma(\xi)$ with $\sigma(\xi)=\sum_je_j\xi_j$ and eigenvalues $\pm|\xi|$. On a closed manifold a Dirac-type operator is self-adjoint with compact resolvent, hence has discrete spectrum, finite-dimensional eigenspaces and finite-dimensional kernel; with a chirality grading it is odd, and the index of its chiral part is a deformation invariant computed by the Atiyah–Singer theorem, with the Fredholm theory supplied by *Fredholm Theory* and the spectral theory by *Unbounded Operators and Spectral Measures*. The corpus's Cauchy–Riemann operator $e_\mu\partial_\mu$ is the flat elliptic operator with one Hermitian coefficient; it is not symmetric, its self-adjoint part is the vector operator $\sum e_j\partial_j$, and the two are the two faces of the factorisation of the Laplacian, the first producing $\Delta$ as $D\bar D$ and the second as $D_{\mathrm{sa}}^2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$, $g$, $m$ | Riemannian manifold, metric, dimension |
| $S$, $\mathcal{S}$ | Clifford module bundle over $M$; its fibre |
| $c(\xi)$ | Clifford multiplication, $c(\xi)^2=-|\xi|^2$, $c(\xi)^*=-c(\xi)$ |
| $\nabla$, $\nabla^*\nabla$ | Clifford connection and connection Laplacian |
| $D=\sum_jc(e_j)\nabla_{e_j}$ | Dirac operator |
| $D^2=\nabla^*\nabla+\mathcal R$ | Weitzenböck identity; $\mathcal R=\frac14\mathrm{scal}$ in the spin case |
| $S^\pm$, $D^\pm$ | Chirality splitting and chiral parts |
| $H^1(M;S)$ | Sobolev domain of the closure |
| $\sigma(\xi)=\sum_je_j\xi_j$ | Symbol in the flat case |
| $\operatorname{ind}D^+$ | Analytic index, $\dim\ker D^+-\dim\ker D^-$ |
| $e_\mu\partial_\mu$, $\partial_0+\sum_je_j\partial_j$ | Cauchy–Riemann operator of the corpus (flat, non-symmetric) |
| $D_{\mathrm{sa}}=\sum_je_j\partial_j$ | Self-adjoint vector part |

## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for spin structures, the spin Dirac operator, the Lichnerowicz formula and the index theorem.
- Nicole Berline, Ezra Getzler and Michèle Vergne, *Heat Kernels and Dirac Operators* (Springer, 1992), for the heat-kernel proof of the index theorem and the local index formula.
- John Roe, *Elliptic Operators, Topology and Asymptotic Methods* (Longman, 2nd ed. 1998), for the analytic theory of Dirac operators and the Fredholm and index properties.
- Michael F. Atiyah and Isadore M. Singer, "The Index of Elliptic Operators I", *Annals of Mathematics* 87 (1968), 484–530, for the index theorem in its general form.
- Michael F. Atiyah, V. K. Patodi and Isadore M. Singer, "Spectral Asymmetry and Riemannian Geometry I", *Mathematical Proceedings of the Cambridge Philosophical Society* 77 (1975), 43–69, for the index of Dirac operators on manifolds with boundary and the boundary correction.
- Paul R. Chernoff, "Essential Self-Adjointness of Powers of Generators of Hyperbolic Equations", *Journal of Functional Analysis* 12 (1973), 401–414, for the essential self-adjointness of Dirac-type operators on complete manifolds.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the spectral theory of unbounded self-adjoint operators and compact resolvents.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the flat operator, its symbol and the elliptic regularity that connects the two settings.
