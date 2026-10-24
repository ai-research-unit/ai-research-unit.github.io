# __The Krein Gram Matrix of the Biquaternion Algebra__

## Introduction

The general quaternionic sesquilinear form of the biquaternion algebra is
$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}
=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2}),
\qquad \varepsilon=(1,-1,-1,-1).
$$
It is a general plain sesquilinear form of signature $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$. This article collects its matrix side: the **Gram matrix** in the coefficient basis, which is the sign matrix $E$; the Gram matrix in the real basis; the matrix-trace representation; Sylvester's law and the inertia; and the discriminant.

The scope is the form itself. The restrictions to the remarkable subspaces, their signatures, their four real forms and their null cones are *Remarkable Subspaces under the General Quaternionic Sesqualgebra*; the Krein-orthogonal complement, the isotropic structure, the Witt index and the Krein cone are *Krein Orthogonality, Isotropy and the Krein Cone of the Biquaternion Algebra*; the fundamental symmetry $J=\natural$ and the bridge to the definite companion are *The Fundamental Symmetry of the Biquaternion Algebra*; and the comparison of the Krein form with the bilinear, Hermitian and general plain forms is *The Four Forms and the Four Algebraic Norms*.

Two conventions are fixed here. An element is written $\tilde Q=c+\vec v$ with $c=Q_t\in\mathbb{C}$ and $\vec v=(Q_x,Q_y,Q_z)\in\mathbb{C}^3$; the form is linear in the first argument and conjugate-linear in the second. The **definite companion** is $\langle\tilde Q_1,\tilde Q_2\rangle_*=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$, and the bridge is $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\langle\tilde Q_1,J\tilde Q_2\rangle_*$ with $J=\natural=\operatorname{diag}(1,-1,-1,-1)$.

## The Gram Matrix in the Coefficient Basis

**Definition.** The **Gram matrix** of the form in a basis $u_1,\dots,u_n$ is $G_{\mu\nu}=\langle u_\mu,u_\nu\rangle_{\natural*}$.

**Theorem (the Gram matrix is the sign matrix).** In the coefficient basis $e_t,\vec e_x,\vec e_y,\vec e_z$,
$$
\boxed{\; G=\operatorname{diag}(1,-1,-1,-1)=E\; },
$$
so the basis is orthogonal, the diagonal entries are $1,-1,-1,-1$, and $\det G=-1$.

*Proof.* $\langle e_\mu,e_\nu\rangle_{\natural*}=\sum_\lambda\varepsilon_\lambda (e_\mu)_\lambda\overline{(e_\nu)_\lambda}=\varepsilon_\mu\delta_{\mu\nu}$: the units are orthogonal, and each carries its own sign. The determinant is the product $\varepsilon_t\varepsilon_x\varepsilon_y\varepsilon_z=-1$.

**Theorem (the real basis and the mixed entries).** In the real basis
$$
e_t,\ \vec e_x,\ \vec e_y,\ \vec e_z,\ ie_t,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z
$$
of the realification $\mathbb{B}_{\mathbb{R}}$, the entries are
$$
\langle e_\mu,e_\nu\rangle_{\natural*}=\varepsilon_\mu\delta_{\mu\nu},\qquad
\langle e_\mu,ie_\nu\rangle_{\natural*}=-i\varepsilon_\mu\delta_{\mu\nu},\qquad
\langle ie_\mu,ie_\nu\rangle_{\natural*}=\varepsilon_\mu\delta_{\mu\nu}.
$$
The mixed entries are purely imaginary, and the matrix of the realified form is
$$
G_{\mathbb{R}}=\operatorname{diag}(1,-1,-1,-1,\,1,-1,-1,-1),
$$
of signature $(2,6)$.

*Proof.* The first and third identities are the coefficient computation of the preceding theorem, with $\lvert i\rvert^2=1$ in the third. For the mixed entry, $(e_\mu)_\mu=1$ and $(ie_\nu)_\mu=i\delta_{\mu\nu}$, so the entry is $\varepsilon_\mu\overline{i\delta_{\mu\nu}}=-i\varepsilon_\mu\delta_{\mu\nu}$, purely imaginary. The realified form reads the real part of the complex form on real vectors, so the mixed block, being purely imaginary, contributes nothing, and the real matrix is the two diagonal blocks $E,E$.

**Corollary (the complex and the real signature).** On the real slice $\mathbb{H}_{\mathbb{B}}$ the form is the real Krein form of signature $(1,3)$, and on the second slice $i\mathbb{H}_{\mathbb{B}}$ it is the same form in the imaginary coefficients. The realification is the orthogonal sum of the two slices and has signature $(1,3)+(1,3)=(2,6)$. The complex Hermitian form has signature $(1,3)$ in complex dimension four, while its realification has real signature $(2,6)$: the two counts are different invariants of the same form, not two readings of one count.

*Proof.* The tensor product $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}_{\mathbb{B}}$ identifies the coefficient basis with the complexification of the real basis of $\mathbb{H}_{\mathbb{B}}$. On $\mathbb{H}_{\mathbb{B}}$ the coefficients are real, so the form is the real symmetric form $q_t^2-q_x^2-q_y^2-q_z^2$; on $i\mathbb{H}_{\mathbb{B}}$ the coefficients are purely imaginary, and the same signs appear because $\lvert i\rvert^2=1$. The real basis splits into the two slices, and $G_{\mathbb{R}}$ is their two diagonal blocks; the complex dimension is four and the real dimension eight.

**Remark (the three Gram matrices).** The three pairings of *The Four Forms and the Four Algebraic Norms* have Gram matrices $\mathrm{I}_4$ (bilinear), $\mathrm{I}_4$ (Hermitian) and $E$ (Krein). The Krein form is the only one of the three whose coefficient basis is already orthogonal with signs; the matrix $E$ is also the Gram matrix of the scalar product $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, and it is $J$ written in the coefficient basis.

## The Krein Form in the Matrix Representation

**Proposition (the form as a matrix trace).** For all biquaternions,
$$
\boxed{\;\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}
=\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf{M}_2(\tilde Q_2)^{\dagger}\,\mathsf{M}_2(\tilde Q_1)\bigr)
=\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q_2^{\natural})^{\dagger}\mathsf{M}_2(\tilde Q_1)\bigr)\; },
$$
where $\dagger$ is the conjugate transpose in the matrix algebra. For $\tilde Q=e_t+i\vec e_x$ the model is
$$
\mathsf{M}_2(\tilde Q)=\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
\operatorname{adj}\mathsf{M}_2(\tilde Q)=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
\operatorname{adj}\mathsf{M}_2(\tilde Q)^{\dagger}\mathsf{M}_2(\tilde Q)=0,
$$
of trace $0$, matching $\langle\tilde Q,\tilde Q\rangle_{\natural*}=\lvert1\rvert^2-\lvert i\rvert^2=0$: the element is isotropic and its matrix is singular, of rank one.

*Proof.* $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\overline{\tilde Q_2}\tilde Q_1)=\mathrm{Sc}\bigl((\tilde Q_2^{\natural})^{*}\tilde Q_1\bigr)$, because $(\tilde Q^{\natural})^{*}=\overline{\tilde Q}$; the trace identity $\mathrm{Sc}(\tilde Q_3\tilde S)=\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde Q_3)\mathsf{M}_2(\tilde S))$ of *The Matrix Element Representation and the Biquaternion Dynamics* gives the result, and $\mathsf{M}_2(\tilde Q^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q)$, with $\mathsf{M}_2$ a $*$-homomorphism, gives the second form.

**Corollary (the three trace expressions).** The bilinear form, the general plain sesquilinear form and the general quaternionic sesquilinear form are the three pairings
$$
\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q_1)\operatorname{adj}\mathsf{M}_2(\tilde Q_2)\bigr),
\qquad
\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2)^{\dagger}\bigr),
\qquad
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2)^{\dagger}\bigr),
$$
so that each pairing is a Hilbert–Schmidt pairing of $\mathsf{M}_2(\tilde Q_1)$ with $\mathsf{M}_2(\tilde Q_2)$: the adjugate acts on the second factor for the bilinear form, the conjugate transpose on the second factor for the plain form, and the adjugate on the first with the conjugate transpose on the second for the Krein form.

**Remark (the adjugate marks the Krein case).** The three pairings differ only by which factor is adjugated and which is conjugated. The Krein form is the adjugated Hilbert–Schmidt pairing, and the identity $\operatorname{adj}(MN)=\operatorname{adj}(N)\operatorname{adj}(M)$ is the matrix form of the anti-automorphism $\natural$; the same adjugate is the fundamental symmetry in the matrix model.

## The Canonical Basis and Sylvester's Law

**Definition.** A basis is **orthogonal** for the form when $\langle u_k,u_j\rangle_{\natural*}=0$ for $j\neq k$, and **orthonormal** when in addition each $\langle u_j,u_j\rangle_{\natural*}=\pm1$.

**Theorem (Sylvester).** Every basis can be replaced by an orthonormal one, and the numbers $n$ of $+1$ and $m$ of $-1$ are invariants of the form: over $\mathbb{C}$, $(n,m)=(1,3)$; over $\mathbb{R}$, $(n,m)=(2,6)$. The coefficient basis is already orthonormal with one $+1$ and three $-1$ in the complex reading, and with two $+1$ and six $-1$ in the real reading.

*Proof.* Diagonalising by congruence and scaling each basis vector to square $\pm1$ gives an orthonormal basis; inertia is invariant by Sylvester's law (*Quadratic Forms and Polarisation*, §*Sylvester's Law of Inertia*). The counts are the signs of $G$ and of $G_{\mathbb{R}}$.

**Corollary (the positive index).** A positive definite subspace meets the negative definite vector subspace $\mathbb{V}_{\mathbb{B}}$ only at the origin, so its complex dimension is at most the codimension $1$ of $\mathbb{V}_{\mathbb{B}}$, and at most $2$ over $\mathbb{R}$. The bounds are attained by the centre and by the realification of the centre; the lines $\mathbb{C}(e_t+\tilde V)$ with $\lVert\tilde V\rVert_E<1$ are the maximal positive definite complex subspaces, and each gives a maximal positive definite real plane $\mathrm{span}_{\mathbb{R}}\{e_t+\tilde V,i(e_t+\tilde V)\}$.

*Proof.* A nonzero vector of a positive definite subspace has a positive square and a nonzero vector of $\mathbb{V}_{\mathbb{B}}$ has a negative square, so the intersection is zero and the dimension bound follows. The centre is positive definite of complex dimension one, and the line $\mathbb{C}(e_t+\tilde V)$ has square $1-\lVert\tilde V\rVert_E^2>0$; the bound is attained. The real plane is the realification of the complex line, of real dimension two, and it is maximal because the real positive index is two.

**Remark (the classification of the positive lines).** The full parametrisation of the maximal positive definite subspaces, the family of fundamental symmetries $J_{\mathbb{W}}$ and the Krein projections are *Krein Orthogonality, Isotropy and the Krein Cone of the Biquaternion Algebra*; the symmetry $J=\natural$ and its eigenspaces are *The Fundamental Symmetry of the Biquaternion Algebra*.

## The Discriminant

**Definition.** The **discriminant** of a non-degenerate symmetric or general plain sesquilinear form of rank $n$ and Gram matrix $G$ is the class of $(-1)^{n(n-1)/2}\det G$ modulo squares of the field.

**Theorem (the discriminant of the Krein form).** Over $\mathbb{R}$ the discriminant of the general quaternionic sesquilinear form is the class of $-1$; over $\mathbb{C}$ it is trivial.

*Proof.* For the form $n=4$ and $\det G=-1$, so $(-1)^{6}(-1)=-1$. Over $\mathbb{C}$ the class of $-1$ is the class of $1$, because $i^{2}=-1$.

**Remark (the restrictions).** Each of the six restrictions tabulated in *Remarkable Subspaces under the General Quaternionic Sesqualgebra* has Gram determinant $\pm1$ and discriminant the class of $-1$ over $\mathbb{R}$: the centre has $n=2$ and determinant $1$, the vector subspace $n=6$ and determinant $1$, and each four-dimensional row has determinant $-1$. The invariance of the class across the restrictions is the matrix form of the fact that the restrictions are the forms of a Lorentzian plane, a six-dimensional definite space and four copies of Lorentzian space. The unimodularity of the coefficient lattice, $\det G=\pm1$, is the same statement read on the units.

## Worked Examples

**A positive vector.** $\tilde Q=e_t+2ie_t$: $\langle\tilde Q,\tilde Q\rangle_{\natural*}=\lvert1\rvert^{2}+\lvert2\rvert^{2}=5>0$, in the centre.

**A negative vector.** $\tilde Q=\vec e_x+\vec e_y$: $\langle\tilde Q,\tilde Q\rangle_{\natural*}=-1-1=-2<0$, in the vector subspace.

**A Lorentzian causal vector.** $\tilde Q=e_t+\tfrac12\vec e_x$: $\langle\tilde Q,\tilde Q\rangle_{\natural*}=1-\tfrac14=\tfrac34>0$, timelike in the quaternion slice $\mathbb{H}_{\mathbb{B}}$, where the form is real.

**A null element of the form only.** $\tilde Q=e_t+\vec e_x$: $\langle\tilde Q,\tilde Q\rangle_{\natural*}=0$ while the norm is $\langle\tilde Q\rangle_{\natural}=2$.

**A null element of the norm only.** $\tilde Q=\vec e_x+i\vec e_y$: $\langle\tilde Q,\tilde Q\rangle_{\natural*}=-2$ while $\langle\tilde Q\rangle_{\natural}=0$; the element is a zero divisor and definite for the form.

**The two readings of one vector.** $\tilde Q=\vec e_x$: $\langle\tilde Q,\tilde Q\rangle_*=1>0$ while $\langle\tilde Q,\tilde Q\rangle_{\natural*}=-1$; the vector is positive in the algebra reading and negative in the form reading.

**A mixed entry.** $\langle e_t,ie_t\rangle_{\natural*}=-i$ and $\langle e_t,ie_x\rangle_{\natural*}=0$: the first is purely imaginary, the second vanishes, which is the real-basis block structure of the theorem.

**A matrix trace.** $\tilde Q=e_t+i\vec e_x$ has $\mathsf{M}_2(\tilde Q)$ of rank one and $\operatorname{adj}\mathsf{M}_2(\tilde Q)^{\dagger}\mathsf{M}_2(\tilde Q)=0$, so the trace formula returns the isotropic value $0$.

## Summary

In the coefficient basis the general quaternionic sesquilinear form has the Gram matrix $G=\operatorname{diag}(1,-1,-1,-1)=E$, of determinant $-1$; in the real basis the mixed entries are $-i\varepsilon_\mu\delta_{\mu\nu}$, purely imaginary, and the realified Gram matrix is $\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1)$, of signature $(2,6)$. In the $2\times2$ matrix representation the form is the adjugated Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_2(\tilde Q_2)^{\dagger}\mathsf{M}_2(\tilde Q_1))$, the adjugate and the conjugate transpose marking the Krein case among the three pairings. Sylvester's law gives $(n,m)=(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$, the coefficient basis already being orthonormal; a positive definite subspace has complex dimension at most one, and the maximal ones are the lines $\mathbb{C}(e_t+\tilde V)$ with $\lVert\tilde V\rVert_E<1$, whose realifications are maximal positive planes. The discriminant is the class of $-1$ over $\mathbb{R}$ and trivial over $\mathbb{C}$, and the same class is carried by each restriction. The restrictions themselves, their signatures and their four real forms are *Remarkable Subspaces under the General Quaternionic Sesqualgebra*; the orthogonality, isotropy and cone are *Krein Orthogonality, Isotropy and the Krein Cone of the Biquaternion Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G=E=\operatorname{diag}(1,-1,-1,-1)$ | The Gram matrix in the coefficient basis; $\det G=-1$ |
| $G_{\mathbb{R}}=\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1)$ | The Gram matrix in the real basis; signature $(2,6)$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | The general quaternionic sesquilinear form |
| $\langle\tilde Q_1,\tilde Q_2\rangle_*=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | The definite companion |
| $J=\natural=\operatorname{diag}(1,-1,-1,-1)$ | The fundamental symmetry; $\langle\cdot,\cdot\rangle_{\natural*}=\langle\cdot,J\cdot\rangle_*$ |
| $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_2(\tilde Q_2)^{\dagger}\mathsf{M}_2(\tilde Q_1))$ | The form in the $2\times2$ matrix representation |
| $(n,m)=(1,3)$ over $\mathbb{C}$, $(2,6)$ over $\mathbb{R}$ | The inertia (Sylvester) |
| $(-1)^{n(n-1)/2}\det G$ | The discriminant; the class of $-1$ over $\mathbb{R}$ |

## Further Reading

- [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the restrictions, their signatures, their null cones and the four real forms.
- [Krein Orthogonality, Isotropy and the Krein Cone of the Biquaternion Algebra](krein-orthogonality-isotropy-and-the-krein-cone-of-the-biquaternion-algebra.html), for the indefinite structure of the form.
- [The Fundamental Symmetry of the Biquaternion Algebra](the-fundamental-symmetry-of-the-biquaternion-algebra.html), for $J=\natural$ and its eigenspaces.
- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the three Gram matrices and the four pairings compared.
- [The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$](the-general-quaternionic-sesqualgebra-in-the-2x2-matrix-element-representation.html), for the adjugated trace identities.
- [Quadratic Forms and Polarisation](quadratic-forms-and-polarisation.html), for Sylvester's law, congruence and the discriminant.
- [The Krein Level Sets and the Hyperbolic Structure](the-krein-level-sets-and-the-hyperbolic-structure.html), for the level sets and the hyperbolic reading of the form.
