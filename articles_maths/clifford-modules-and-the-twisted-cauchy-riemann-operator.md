
# __Clifford Modules and the Twisted Cauchy–Riemann Operator__

## Introduction

A Clifford module is a module over a Clifford algebra, and over a manifold it becomes a bundle of modules twisted by the spinor bundle. On such a twisted module there is a canonical first-order operator, formed by contracting the covariant derivative with Clifford multiplication, which generalises both the Cauchy–Riemann operator of complex analysis and its Clifford-analytic relatives. This article builds the operator, shows that it is elliptic and odd for the natural grading, computes the square — the Weitzenböck formula — and evaluates the index of the resulting elliptic complex.

The Clifford-module theory used here — modules over $\mathrm{Cl}(V,q)$, the spinor module, the chirality grading and the half-spin modules — is from *Spin Representations and Clifford Modules*. The differential-geometric input — connections, curvature, the Levi-Civita connection and the Chern–Weil characteristic classes — is. The Clifford-analytic Cauchy–Riemann operator of the hypercomplex theory, with its symbol and ellipticity, is, and its biquaternion form is; the operator of this article is the manifold-valued and twisted form of those operators, and the untwisted biquaternion operator with its Cauchy integral formula is not reproduced here. The general index theorem that the computation feeds is the subject, and only the twisted case is treated here.

## Clifford Modules

**Definition.** Let $(V,q)$ be a quadratic space over $\mathbb{R}$ or $\mathbb{C}$. A **Clifford module** for $\mathrm{Cl}(V,q)$ is a vector space $E$ with an algebra homomorphism $\mathrm{Cl}(V,q)\to\operatorname{End}(E)$, equivalently a linear map $c\colon V\to\operatorname{End}(E)$ with

$$
c(v)^2=q(v)\,\mathrm{id}_{E}, \qquad c(v)c(w)+c(w)c(v)=2B(v,w)\,\mathrm{id}_{E},
$$

where $B$ is the polar form.

**Definition.** A **$\mathbb{Z}/2$-graded Clifford module** is a Clifford module $E=E_0\oplus E_1$ such that $c(v)$ is odd, $c(v)E_j\subseteq E_{1-j}$. The **chirality operator** of an even-dimensional module is the Clifford action of the volume element, and its $\pm1$-eigenspaces are the **half-modules** $E_\pm$.

**Theorem (structure of Clifford modules).** Let $(V,q)$ be a non-degenerate real quadratic space of dimension $n$ and let $S$ be its spinor module. If $\mathrm{Cl}(V,q)$ is simple — that is, for $n$ even, and for $n$ odd with $d=p-q\equiv3,7\bmod8$ — every finite-dimensional Clifford module $E$ is a direct sum of copies of the unique irreducible module $S$. If $n$ is odd with $d\equiv1,5\bmod8$, where the algebra is a product of two simple factors, then $E$ is a direct sum of copies of each of the two irreducible modules. In the simple case, in particular in the even case, this reads $E\cong S\otimes W$ for a vector space $W$, with the Clifford action $c(v)=c_S(v)\otimes\mathrm{id}_W$.

**Proof.** The Clifford algebra is central simple over $\mathbb{R}$ for $n$ even, is simple with center $\mathbb{C}$ for $n$ odd with $d\equiv3,7\bmod8$, and is a product of two simple algebras for $n$ odd with $d\equiv1,5\bmod8$, by the classification of the preceding articles; over a simple algebra every module is a direct sum of copies of the simple module, and over a product of two simple algebras it is a direct sum of copies of the simple module of each factor. The tensor form of the action is the definition of the tensor product action. $\square$

**Definition.** The vector space $W$ is the **twisting space**, and $E=S\otimes W$ is the **twisted Clifford module**; a Clifford module is **untwisted** when $W$ is one-dimensional.

**Remark.** The structure theorem is the reason the twisting space is useful: in the simple case, in particular in even dimensions, a general Clifford module is a spinor module tensored with an arbitrary coefficient space, so any statement about Clifford modules reduces to a statement about the spinor module and a coefficient representation; in the odd non-simple case it reduces to two such statements, one for each simple factor. Over a manifold this becomes a statement about a vector bundle $W\to M$ tensored with the spinor bundle, and the operator of this article is the one that acts on the resulting sections.

## The Clifford Bundle and the Spinor Bundle

**Definition.** Let $(M,g)$ be a Riemannian manifold. The **Clifford bundle** is the bundle $\mathrm{Cl}(TM)\to M$ whose fibre at $x$ is $\mathrm{Cl}(T_xM,g_x)$; the **spinor bundle** $S\to M$ is the bundle of spinor modules, when $M$ is spin and a spin structure has been chosen.

**Definition.** A **Clifford module bundle** is a bundle $E\to M$ of Clifford modules, that is, a Hermitian vector bundle with a bundle map $c\colon TM\otimes E\to E$ satisfying $c(v)^2=\langle v,v\rangle\mathrm{id}$ fibrewise. A **twisted Clifford module bundle** is $E=S\otimes W$ for a Hermitian vector bundle $W\to M$ with a connection.

**Theorem.** Let $(M,g)$ be a spin Riemannian manifold with spinor bundle $S$ and Levi-Civita connection $\nabla$. There is a unique connection $\nabla^S$ on $S$ that is compatible with the metric and the Clifford multiplication, $X\bigl(c(v)s\bigr)=c(\nabla_Xv)s+c(v)\nabla^S_Xs$ for all vector fields $X,v$ and sections $s$. For a twisted Clifford module bundle $E=S\otimes W$ with a connection $\nabla^W$ on $W$, the tensor connection $\nabla^E=\nabla^S\otimes\mathrm{id}+\mathrm{id}\otimes\nabla^W$ is compatible with the metric and the Clifford action.

**Proof.** The spin connection is constructed by lifting the Levi-Civita connection to the spin structure; the compatibility condition determines it uniquely because the spin representation is faithful and the Clifford algebra generates the endomorphisms of the spinor fibre. The tensor connection satisfies the Leibniz rule and is compatible with the metric, and compatibility with the Clifford action is inherited from $\nabla^S$. $\square$

## The Twisted Cauchy–Riemann Operator

**Definition.** Let $E=S\otimes W\to M$ be a twisted Clifford module bundle over a spin Riemannian manifold, and let $\nabla^E$ be a compatible connection. The **twisted Cauchy–Riemann operator** is

$$
D_E=\sum_{i=1}^{n}c(e_i)\nabla^E_{e_i}\colon\Gamma(E)\longrightarrow\Gamma(E),
$$

where $e_1,\dots,e_n$ is a local orthonormal frame and $c$ is Clifford multiplication.

**Theorem.** The operator $D_E$ is well defined and independent of the choice of orthonormal frame, and it is the composition of the covariant derivative with Clifford multiplication,

$$
D_E=c\circ\nabla^{E}\colon\Gamma(E)\xrightarrow{\ \nabla^E\ }\Gamma(T^*M\otimes E)\xrightarrow{\ \cong\ }\Gamma(TM\otimes E)\xrightarrow{\ c\ }\Gamma(E),
$$

where $T^*M$ is identified with $TM$ by the metric. When $E$ is $\mathbb{Z}/2$-graded and the grading is preserved by parallel transport, $D_E$ is odd, $D_E\Gamma(E_\pm)\subseteq\Gamma(E_\mp)$.

**Proof.** The sum $\sum_ic(e_i)\nabla^E_{e_i}$ is a geometric first-order operator: a change of orthonormal frame replaces $e_i$ by $O_{ij}e_j$ with $O$ orthogonal, and the contracted expression is invariant because $c$ is linear and $\sum_iO_{ij}O_{ik}=\delta_{jk}$. Compatibility of $\nabla^E$ with the Clifford action identifies the sum with the composition displayed; oddness is the statement that $c(v)$ is odd and that $\nabla^E$ preserves the grading. $\square$

**Example (the classical cases).** For $M=\mathbb{R}^2$ with the complex structure and $W$ trivial, the operator $D=\partial_0+i\partial_1$ is the classical Cauchy–Riemann operator, and its kernel is the holomorphic functions; for $M=\mathbb{R}^n$ with trivial twisting it is the generalised Cauchy–Riemann operator. The construction of this article is thus the co-ordinate-free and twisted form of those operators.

## The Weitzenböck Formula

The square of the twisted Cauchy–Riemann operator is a Laplace-type operator, and the difference from the raw Laplacian is a curvature term.

**Theorem (Weitzenböck).** With the conventions above,

$$
D_E^{2}=\nabla^{E,*}\nabla^{E}+\mathcal{R}^{E},
$$

where $\nabla^{E,*}\nabla^E$ is the connection Laplacian (the covariant Laplacian, non-negative on compactly supported sections) and $\mathcal{R}^E$ is an endomorphism-valued zeroth-order term, the **Weitzenböck curvature**, built from the curvature $R^S$ of the spin connection and the curvature $F^W$ of the twisting connection:

$$
\mathcal{R}^{E}=\tfrac14 s\,\mathrm{id}+c(F^{W}),
$$

in the untwisted case $\mathcal{R}=\tfrac14 s\,\mathrm{id}$ with $s$ the scalar curvature, and in general $\mathcal{R}^E=\tfrac14s\,\mathrm{id}+\sum_{i<j}c(e_i)c(e_j)F^W_{ij}$, where $F^W$ is the curvature two-form of the twisting connection; the Clifford multiplication of a two-form is the sum of its coefficients against the corresponding bivectors, $c(F^W)=\sum_{i<j}c(e_i)c(e_j)F^W_{ij}$.

**Proof sketch.** Compute $D_E^2=\sum_{i,j}c(e_i)c(e_j)\nabla^E_i\nabla^E_j$; split the sum into the symmetric and antisymmetric parts. The symmetric part is the connection Laplacian by the Clifford relation, and the antisymmetric part is a curvature term: the commutator $[\nabla^E_i,\nabla^E_j]$ is the curvature, Clifford-multiplied. The trace of the curvature over the spinorial indices gives the scalar curvature, and the twisting curvature enters through $c(F^W)$. $\square$

**Corollary.** In the untwisted case the **Lichnerowicz formula** holds:

$$
D^2=\nabla^{*}\nabla+\tfrac14 s,
$$

and if $s>0$ pointwise then $D$ has no harmonic spinors, $\ker D=0$, since $\int_M\langle D^2s,s\rangle=\int_M|\nabla s|^2+\tfrac14\int_M s|s|^2>0$ for nonzero $s$.

**Proof.** The formula is the untwisted case of the theorem; integrating the identity $D^2=\nabla^*\nabla+\tfrac14s$ against a spinor and integrating by parts gives the positivity. $\square$

**Remark.** The Weitzenböck formula is the bridge between the operator and the geometry: the harmonic spinors of $D_E$ are the solutions of a second-order equation whose potential is the curvature, and the vanishing or non-vanishing of the kernel is controlled by the sign of the curvature. In the twisted case the twisting curvature $F^W$ shifts the potential, and the index measures the net effect.

## Ellipticity and the Elliptic Complex

**Theorem.** The principal symbol of $D_E$ at a covector $\xi\in T_x^*M$ is Clifford multiplication by $i\xi$,

$$
\sigma(D_E)(x,\xi)=i\,c(\xi)\colon E_x\to E_x,
$$

and this endomorphism is invertible for every $\xi\neq0$. Hence $D_E$ is elliptic.

**Proof.** The symbol of a first-order operator $\sum_ic(e_i)\nabla_i$ is $\sum_ic(e_i)\xi_i=c(\xi)$ up to the factor $i$ from the Fourier convention. The square is $\sigma(D_E)^2=-c(\xi)^2=-|\xi|^2\mathrm{id}$, so the symbol is invertible with inverse $-c(\xi)/|\xi|^2$ for $\xi\neq0$. A differential operator whose principal symbol is invertible for all nonzero covectors is elliptic by definition. $\square$

**Theorem.** On a closed spin Riemannian manifold with a $\mathbb{Z}/2$-graded twisted Clifford module bundle $E=E_+\oplus E_-$, the operator restricts to an elliptic operator

$$
D_+\colon\Gamma(E_+)\to\Gamma(E_-),
$$

and the **index**

$$
\operatorname{ind}(D_+)=\dim\ker D_+-\dim\operatorname{coker}D_+
$$

is a finite integer, equal to $\dim\ker D_+-\dim\ker D_-$ because $D_E$ is self-adjoint and $D_-=D_+^{*}$.

**Proof.** $D_E$ is odd and formally self-adjoint with respect to the $L^2$ inner products, so its off-diagonal blocks are adjoint to one another, and $\operatorname{coker}D_+=\ker D_+^{*}=\ker D_-$. Ellipticity on a closed manifold gives finite-dimensional kernel and cokernel by the standard regularity theory. $\square$

**Remark.** The index is the analytic datum of the elliptic complex $0\to\Gamma(E_+)\xrightarrow{D_+}\Gamma(E_-)\to0$, and it is invariant under continuous deformations of the operator within the class of elliptic operators, because the kernel dimension can jump only by the same amount as the cokernel dimension. This stability is what makes the index computable by topological means, and the computation is the subject of the next section.

## The Index Computation

**Theorem (McKean–Singer).** For $t>0$ the index is given by the heat-kernel supertrace

$$
\operatorname{ind}(D_+)=\operatorname{Tr}\bigl(e^{-tD_-D_+}\bigr)-\operatorname{Tr}\bigl(e^{-tD_+D_-}\bigr),
$$

and the right-hand side is independent of $t$.

**Proof.** The nonzero eigenvalues of $D_-D_+$ and $D_+D_-$ coincide, with the same multiplicities, by the standard argument: if $D_+D_-v=\lambda v$ with $\lambda\neq0$ then $D_-v$ is an eigenvector of $D_-D_+$ with the same eigenvalue, and the map is a bijection between the eigenspaces. The trace difference therefore selects only the eigenvalue $0$; the kernel of $D_-D_+$ is $\ker D_+$ and the kernel of $D_+D_-$ is $\ker D_-$, so the difference is $\dim\ker D_+-\dim\ker D_-$. Since the nonzero spectra agree, the difference is $t$-independent. $\square$

**Theorem (twisted index formula).** Let $(M,g)$ be a closed spin manifold of even dimension $n=2m$, and let $E=S\otimes W$ be a twisted Clifford module bundle with $W$ a Hermitian vector bundle. Then

$$
\operatorname{ind}(D_+)=\int_M\hat{A}(TM)\,\operatorname{ch}(W),
$$

where $\hat{A}(TM)$ is the $\hat{A}$-class of the tangent bundle, expressed in the Pontryagin classes, and $\operatorname{ch}(W)$ is the Chern character of $W$.

**Proof sketch.** By the McKean–Singer formula the index is the $t\to\infty$ (equivalently, the $t$-independent) supertrace of the heat kernel. The local index theorem of Atiyah–Singer–Patodi identifies the $t\to0$ limit of the pointwise supertrace as the top-degree part of $\hat{A}(TM)\operatorname{ch}(W)$, so integrating gives the stated formula. The untwisted case $\operatorname{ch}(W)=1$ is the statement that the index of the Cauchy–Riemann operator on the spinor bundle is the $\hat{A}$-genus. $\square$

**Example (compact Riemann surface).** Let $M$ be a closed Riemann surface, spin with $S=K^{1/2}\oplus K^{-1/2}$, and let $W=L$ be a complex line bundle of degree $k=\int_Mc_1(L)$. The $\hat{A}$-class of a surface is $1$, so

$$
\operatorname{ind}(D_+)=\int_M\operatorname{ch}(L)=\int_M\bigl(1+c_1(L)\bigr)=k.
$$

The index of the twisted operator is therefore the degree of the twisting line bundle; it is an integer, and the theorem produces the integrality rather than assuming it.

**Example (a four-dimensional spin manifold).** Let $M$ be a closed spin $4$-manifold, untwisted. The $\hat{A}$-class is $\hat{A}(TM)=1-\tfrac{1}{24}p_1(TM)$, and the top-degree part is the $4$-form $-\tfrac{1}{24}p_1$. Hence

$$
\operatorname{ind}(D_+)=-\frac{1}{24}\int_Mp_1(TM)=-\frac{\sigma(M)}{8},
$$

where $\sigma$ is the signature, by the signature theorem; for a $K3$ surface, $\sigma=-16$ and the index is $2$.

**Remark.** The twisted index formula is the model for the general Atiyah–Singer theorem: the analytic index, which is a difference of kernel dimensions, is computed by a purely topological integral of characteristic classes. The operator here is the one associated with the Clifford module, and the twist by $W$ shows how the coefficient bundle enters. The general statement, its $K$-theoretic formulation and the local index formula are.

## Summary

A Clifford module is a module over a Clifford algebra, and every Clifford module is the spinor module tensored with a twisting space; over a manifold this becomes a Hermitian vector bundle $E=S\otimes W$ with a Clifford action and a compatible connection. The twisted Cauchy–Riemann operator is

$$
D_E=\sum_ic(e_i)\nabla^E_{e_i},
$$

well defined, geometric, and, on a $\mathbb{Z}/2$-graded module, odd. Its symbol is $i\,c(\xi)$, invertible for $\xi\neq0$, so $D_E$ is elliptic; on a closed manifold the graded operator $D_+\colon\Gamma(E_+)\to\Gamma(E_-)$ has finite-dimensional kernel and cokernel and a well-defined index.

The square of the operator satisfies the Weitzenböck formula $D_E^2=\nabla^{E,*}\nabla^E+\mathcal{R}^E$, with $\mathcal{R}^E=\tfrac14s+c(F^W)$; in the untwisted case this is the Lichnerowicz formula, and positive scalar curvature forces the kernel to vanish. The index is computed by the McKean–Singer supertrace, independent of $t$, and the local index theorem gives

$$
\operatorname{ind}(D_+)=\int_M\hat{A}(TM)\operatorname{ch}(W).
$$

On a compact Riemann surface this reduces to the degree of the twisting line bundle; on a closed spin four-manifold, untwisted, it is minus one eighth of the signature, giving $2$ for a $K3$ surface.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Cl}(V,q)$, $c(v)$ | Clifford algebra and Clifford multiplication, $c(v)^2=q(v)$ |
| $S$ | Spinor module or spinor bundle |
| $E=S\otimes W$ | Twisted Clifford module, $W$ the twisting bundle |
| $E_\pm$ | Half-modules, eigenspaces of the chirality operator |
| $\nabla^S,\nabla^W,\nabla^E$ | Spin, twisting and tensor connections |
| $D_E=\sum_ic(e_i)\nabla^E_{e_i}$ | Twisted Cauchy–Riemann operator |
| $\sigma(D_E)(x,\xi)=i\,c(\xi)$ | Principal symbol, invertible for $\xi\neq0$ |
| $D_+:\Gamma(E_+)\to\Gamma(E_-)$ | Graded operator whose index is taken |
| $\operatorname{ind}(D_+)$ | $\dim\ker D_+-\dim\operatorname{coker}D_+$ |
| $D_E^2=\nabla^{E,*}\nabla^E+\mathcal{R}^E$ | Weitzenböck formula |
| $\mathcal{R}^E=\tfrac14s+c(F^W)$ | Weitzenböck curvature, $s$ the scalar curvature |
| $D^2=\nabla^*\nabla+\tfrac14s$ | Lichnerowicz formula, untwisted case |
| $\operatorname{Tr}(e^{-tD_-D_+})-\operatorname{Tr}(e^{-tD_+D_-})$ | McKean–Singer supertrace, equal to the index |
| $\hat{A}(TM)$ | $\hat{A}$-class of the tangent bundle |
| $\operatorname{ch}(W)$ | Chern character of the twisting bundle |
| $\int_M\hat{A}(TM)\operatorname{ch}(W)$ | Twisted index formula |
| $\sigma(M)$ | Signature of a closed oriented $4$-manifold |



## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for Clifford modules, the spinor bundle, the twisted operator and the Weitzenböck formula.
- Michael F. Atiyah, Raoul Bott and Vijay K. Patodi, "On the heat equation and the index theorem," *Inventiones Mathematicae* **19** (1973), 279–330, for the heat-kernel proof of the index theorem and the local index formula.
- Peter B. Gilkey, *Invariance Theory, the Heat Equation and the Atiyah–Singer Index Theorem* (CRC Press, 2nd ed. 1995), for the McKean–Singer formula and the local computation of the supertrace.
- Michael F. Atiyah and Isadore M. Singer, "The index of elliptic operators I, III," *Annals of Mathematics* **87** (1968), 484–530 and 546–604, for the index theorem and its topological formulation.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Riemann surface computation and the Riemann–Roch theorem in its characteristic-class form.
