# __The Krein Form of the Biquaternion Algebra__

## Introduction

The general quaternionic sesquilinear form of the biquaternion algebra is
$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}
=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2}),
\qquad \varepsilon=(1,-1,-1,-1).
$$
It is linear in the first argument and conjugate-linear in the second, and it is non-degenerate, of signature $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$. Indefiniteness runs through everything below: the form has a canonical involution, its orthogonal complement is not a complement, it has isotropic elements and totally isotropic subspaces, and its non-negative set is a cone. This article reads the form whole: the matrices, the inertia, the involution, the orthogonality, the isotropy and the cone.

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of complex dimension four and real dimension eight. The centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ and the vector subspace is $\mathbb{V}_{\mathbb{B}}=\mathrm{span}_{\mathbb{C}}\{\vec e_x,\vec e_y,\vec e_z\}$. An element is written $\tilde Q=c+\vec v$ with $c=Q_t\in\mathbb{C}$ and $\vec v=(Q_x,Q_y,Q_z)\in\mathbb{C}^3$. The Euclidean norm is $\lVert\tilde Q\rVert_E^2=\sum_\mu\lvert Q_\mu\rvert^2$. The **definite companion** is
$$
\langle\tilde Q_1,\tilde Q_2\rangle_*=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}},
$$
and the **fundamental symmetry** is $J={}^{\natural}=\operatorname{diag}(1,-1,-1,-1)$ in the coefficient basis.

The restrictions to the remarkable subspaces are *Remarkable Subspaces under the General Quaternionic Sesqualgebra*; the global level sets and the hyperbolic ball are *The Krein Level Sets and the Hyperbolic Structure*; the operator theory is *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*; the Cartan decomposition is *The Krein Cartan Decomposition of the Operator Algebra*; and the comparison with the other three pairings is *The Four Forms and the Four Algebraic Norms*. This article owns the form itself and its indefinite structure.

## The Form and Its Gram Matrices

**Definition.** The **Gram matrix** of the form in a basis $u_1,\dots,u_n$ is $G_{\mu\nu}=\langle u_\mu,u_\nu\rangle_{\natural*}$.

**Theorem (the coefficient Gram matrix).** In the coefficient basis $e_t,\vec e_x,\vec e_y,\vec e_z$,
$$
\boxed{\; G=\operatorname{diag}(1,-1,-1,-1)=E\; },
$$
so the basis is orthogonal, the diagonal entries are $1,-1,-1,-1$, and $\det G=-1$.

*Proof.* $\langle e_\mu,e_\nu\rangle_{\natural*}=\sum_\lambda\varepsilon_\lambda (e_\mu)_\lambda\overline{(e_\nu)_\lambda}=\varepsilon_\mu\delta_{\mu\nu}$: the units are orthogonal, and each carries its own sign. The determinant is the product $\varepsilon_t\varepsilon_x\varepsilon_y\varepsilon_z=-1$.

**Theorem (the real basis).** In the real basis
$$
e_t,\ \vec e_x,\ \vec e_y,\ \vec e_z,\ ie_t,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z
$$
of the realification $\mathbb{B}_{\mathbb{R}}$, the entries of the complex Gram matrix are
$$
\langle e_\mu,e_\nu\rangle_{\natural*}=\varepsilon_\mu\delta_{\mu\nu},\qquad
\langle e_\mu,ie_\nu\rangle_{\natural*}=-i\varepsilon_\mu\delta_{\mu\nu},\qquad
\langle ie_\mu,e_\nu\rangle_{\natural*}=i\varepsilon_\mu\delta_{\mu\nu},\qquad
\langle ie_\mu,ie_\nu\rangle_{\natural*}=\varepsilon_\mu\delta_{\mu\nu}.
$$
The mixed entries are purely imaginary, so the matrix of the realified form, that is of $\operatorname{Re}\langle\cdot,\cdot\rangle_{\natural*}$, is
$$
G_{\mathbb{R}}=\begin{pmatrix}E&0\\0&E\end{pmatrix}
=\operatorname{diag}(1,-1,-1,-1,\,1,-1,-1,-1),
$$
of signature $(2,6)$.

*Proof.* The diagonal identities are the coefficient computation, with $\lvert i\rvert^2=1$ in the last. For the mixed entry, $(e_\mu)_\mu=1$ and $(ie_\nu)_\mu=i\delta_{\mu\nu}$, so $\langle e_\mu,ie_\nu\rangle_{\natural*}=\varepsilon_\mu\overline{i\delta_{\mu\nu}}=-i\varepsilon_\mu\delta_{\mu\nu}$; the conjugate entry is its conjugate. The realified form reads the real part of the complex form on real vectors, so the purely imaginary mixed block contributes nothing, and the real matrix is the two diagonal blocks $E,E$.

**Remark (the complex matrix on the real basis is not the form's matrix).** The full complex matrix of the entries above,
$$
\tilde G=\begin{pmatrix}E&-iE\\ iE&E\end{pmatrix},
$$
is Hermitian but singular: its determinant is $\det(E^2-E^2)=0$. It is the table of values on a real basis, not the matrix of a $\mathbb{C}$-bilinear form, and it is not the matrix that carries the signature. The form is sesquilinear, so its invariants are read on the realification, whose matrix $G_{\mathbb{R}}$ is block diagonal and non-singular. The mixed entries are the bookkeeping of the conjugate-linearity; they disappear on taking the real part.

**Corollary (the two real slices).** On the real slice $\mathbb{H}_{\mathbb{B}}$ the form is the real Krein form $q_t^2-q_x^2-q_y^2-q_z^2$, of signature $(1,3)$, and on the second slice $i\mathbb{H}_{\mathbb{B}}$ it is the same form in the imaginary coefficients. The realification is the orthogonal sum of the two slices and has signature $(1,3)+(1,3)=(2,6)$.

*Proof.* The tensor product $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}_{\mathbb{B}}$ identifies the coefficient basis with the complexification of the real basis of $\mathbb{H}_{\mathbb{B}}$. On $\mathbb{H}_{\mathbb{B}}$ the coefficients are real, so the form is the displayed real quadratic form; on $i\mathbb{H}_{\mathbb{B}}$ the coefficients are purely imaginary, and $\lvert i\rvert^2=1$ gives the same signs. The two slices are the two diagonal blocks of $G_{\mathbb{R}}$.

**Remark (the four forms).** The algebra carries four pairings, and their Gram matrices separate them cleanly: the plain bilinear form $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ has $E$; the Hermitian form $\langle\cdot,\cdot\rangle_*$ has $\mathrm{I}_4$; the quaternionic bilinear form $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$ has $\mathrm{I}_4$; and the Krein form has $E$. The second slot, identity or conjugate transpose, decides whether the form is bilinear or sesquilinear, and the first slot, identity or natural conjugation, decides the sign matrix. The table and the isometry groups are *The Four Forms and the Four Algebraic Norms*.

## The Form in the Matrix Representation

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

*Proof.* $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\overline{\tilde Q_2}\tilde Q_1)=\mathrm{Sc}\bigl((\tilde Q_2^{\natural})^{*}\tilde Q_1\bigr)$, because $(\tilde Q^{\natural})^{*}=\overline{\tilde Q}$; the trace identity $\mathrm{Sc}(\tilde Q_3\tilde S)=\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde Q_3)\mathsf{M}_2(\tilde S))$ of *The Matrix Element Representation and the Biquaternion Dynamics* gives the result, and $\mathsf{M}_2(\tilde Q^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q)$ gives the second form.

**Corollary (the three trace expressions).** The plain bilinear form, the Hermitian form and the Krein form are the three pairings
$$
\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q_1)\operatorname{adj}\mathsf{M}_2(\tilde Q_2)\bigr),
\qquad
\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2)^{\dagger}\bigr),
\qquad
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2)^{\dagger}\bigr).
$$
The adjugate acts on the second factor for the bilinear form, the conjugate transpose on the second factor for the Hermitian form, and both on the Krein form, with the adjugate on the first factor.

**Remark (the adjugate marks the Krein case).** The identity $\operatorname{adj}(MN)=\operatorname{adj}(N)\operatorname{adj}(M)$ is the matrix form of the anti-automorphism $\natural$, and the same adjugate is the fundamental symmetry in the matrix model: $\mathsf{M}_2(\tilde Q^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q)$. The three expressions above differ only by which factor is adjugated and which is conjugated.

## Inertia, Indices and Positive Subspaces

**Theorem (Sylvester).** Every basis can be replaced by an orthonormal one, and the numbers $n$ of $+1$ and $m$ of $-1$ are invariants of the form: over $\mathbb{C}$, $(n,m)=(1,3)$; over $\mathbb{R}$, $(n,m)=(2,6)$. The coefficient basis is already orthonormal, with one $+1$ and three $-1$ in the complex reading, and with two $+1$ and six $-1$ in the real reading.

*Proof.* Diagonalising by congruence and scaling each basis vector to value $\pm1$ gives an orthonormal basis; inertia is invariant by Sylvester's law (*Quadratic Forms and Polarisation*, §*Sylvester's Law of Inertia*). The counts are the signs of $G$ and of $G_{\mathbb{R}}$.

**Definition.** Let $n$ and $m$ be the dimensions of the positive and of the negative definite part of a fundamental decomposition. The pair $(n,m)$ is the **signature**, $m$ is the **negative index**, and $\min(n,m)$ is the **Pontryagin index**.

**Theorem (the signature and the two indices).** Over $\mathbb{C}$, $(n,m)=(1,3)$, the negative index is $3$ and the Pontryagin index is $1$; over $\mathbb{R}$, $(n,m)=(2,6)$, the negative index is $6$ and the Pontryagin index is $2$. With the Krein form the algebra has finite negative index, denoted $\Pi_{6}$ over $\mathbb{R}$.

*Proof.* The eigenspace splitting of $J={}^{\natural}$ is a fundamental decomposition, with positive part the centre $\mathbb{C}_{\mathbb{B}}$ and negative part the vector subspace $\mathbb{V}_{\mathbb{B}}$ (§*The Eigenspaces and the Fundamental Decomposition*), of complex dimensions $1$ and $3$ and therefore of real dimensions $2$ and $6$. The smaller of the two is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$; the subscript of $\Pi_{6}$ records the negative index.

**Remark (the two readings are different invariants).** Over $\mathbb{C}$ the form is a Hermitian form on a complex space of dimension four, and its signature counts complex dimensions, $(1,3)$; over $\mathbb{R}$ it is a real symmetric form on a real space of dimension eight, and its signature counts real dimensions, $(2,6)$. The passage from one reading to the other doubles both entries; it does not preserve them. The negative index is $3$ over $\mathbb{C}$ and $6$ over $\mathbb{R}$, and the Pontryagin index is $1$ and $2$. The name $\Pi_{6}$ carries the real negative index.

**Theorem (the maximal positive subspaces).** A positive definite subspace has complex dimension at most $1$, and real dimension at most $2$. The maximal ones are exactly the lines
$$
\ell_{\tilde V}=\mathbb{C}(e_t+\tilde V),\qquad \tilde V\in\mathbb{V}_{\mathbb{B}},\quad \lVert\tilde V\rVert_E<1,
$$
and over $\mathbb{R}$ the realification of such a line is the positive definite plane $\mathrm{span}_{\mathbb{R}}\{e_t+\tilde V,i(e_t+\tilde V)\}$.

*Proof.* A positive definite subspace meets the negative definite vector subspace $\mathbb{V}_{\mathbb{B}}$ only at the origin, so it injects into $\mathbb{B}/\mathbb{V}_{\mathbb{B}}$, of complex dimension $1$; hence its complex dimension is at most one, and its real dimension at most two. A positive definite line has a nonzero scalar coordinate, since $Q_t=0$ gives $\langle\tilde Q,\tilde Q\rangle_{\natural*}=-\lVert\vec Q\rVert_E^2<0$; scaling, the line is $\mathbb{C}(e_t+\tilde V)$ and
$$
\langle e_t+\tilde V,e_t+\tilde V\rangle_{\natural*}=1-\lVert\tilde V\rVert_E^2
$$
is positive exactly for $\lVert\tilde V\rVert_E<1$. The real plane is the realification of the complex line, and it is maximal because the real positive index is two.

**Remark (real planes that are not complex).** Over $\mathbb{R}$ the positive index is two, and the real planes $\mathrm{span}_{\mathbb{R}}\{e_t+\tilde V,i(e_t+\tilde V)\}$ are the realifications of the complex lines. The realification carries further maximal positive planes that are not complex, the graphs of real-linear maps $\mathbb{C}_{\mathbb{B}}\to\mathbb{V}_{\mathbb{B}}$ of norm less than one. The complex classification above is the one used by the operator theory, where all maps are $\mathbb{C}$-linear.

## The Natural Conjugation as a Fundamental Symmetry

**Definition.** A **fundamental symmetry** of an indefinite inner product is a $\mathbb{C}$-linear involution $J$, self-adjoint for the form, such that $\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\langle\tilde Q_2,J\tilde Q_1\rangle_{*}$ and $\langle\tilde Q_1,J\tilde Q_1\rangle_{\natural*}>0$ for $\tilde Q_1\neq0$.

**Theorem (the natural conjugation is one).** The natural conjugation $J={}^{\natural}$ is a fundamental symmetry of the Krein form:
$$
\boxed{\; J^{2}=\mathrm{id},\qquad \langle\tilde Q_2,J\tilde Q_1\rangle_{\natural*}=\langle J\tilde Q_2,\tilde Q_1\rangle_{\natural*},\qquad \langle\tilde Q_1,J\tilde Q_1\rangle_{\natural*}=\lVert\tilde Q_1\rVert_E^{2}>0\ (\tilde Q_1\neq0) \;},
$$
and the definite form it induces is the Hermitian companion,
$$
\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\langle\tilde Q_2,J\tilde Q_1\rangle_{*}=\langle\tilde Q_2,\tilde Q_1^{\natural}\rangle_{*} .
$$

*Proof.* $J$ is $\mathbb{C}$-linear and an involution because it multiplies each coefficient by the real sign $\varepsilon_\mu$. For the self-adjointness, $\langle\tilde Q_2,J\tilde Q_1\rangle_{\natural*}=\langle\tilde Q_2,J^{2}\tilde Q_1\rangle_{*}=\langle\tilde Q_2,\tilde Q_1\rangle_{*}$ and $\langle J\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\langle J\tilde Q_2,J\tilde Q_1\rangle_{*}=\sum_\mu\varepsilon_\mu^{2}Q_{2\mu}\overline{Q_{1\mu}}=\langle\tilde Q_2,\tilde Q_1\rangle_{*}$, using $(J\tilde Q_1)_\mu=\varepsilon_\mu Q_{1\mu}$. For positivity, $\langle\tilde Q_1,J\tilde Q_1\rangle_{\natural*}=\sum_\mu\varepsilon_\mu^{2}\lvert Q_{1\mu}\rvert^{2}=\lVert\tilde Q_1\rVert_E^{2}$. The bridge identity is the first computation.

**Corollary (an isometry of both forms).** $J$ preserves the Krein form and the Hermitian companion,
$$
\langle J\tilde Q_2,J\tilde Q_1\rangle_{\natural*}=\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*},\qquad \langle J\tilde Q_2,J\tilde Q_1\rangle_{*}=\langle\tilde Q_2,\tilde Q_1\rangle_{*},
$$
and it is orthogonal for the Euclidean norm, $\lVert J\tilde Q_1\rVert_E=\lVert\tilde Q_1\rVert_E$.

*Proof.* Both forms are sums of $\lvert Q_\mu\rvert^2$ with signs and of off-diagonal pairings; $J$ multiplies each coefficient by a real sign, and $\varepsilon_\mu^2=1$ removes it from every diagonal expression, while off-diagonal pairings receive the same sign in both factors.

**Proposition (the natural conjugation is an anti-automorphism).** ${}^{\natural}$ is a $\mathbb{C}$-linear algebra anti-automorphism of order two: ${}^{\natural}(e_t)=e_t$ and
$$
(\tilde Q_1\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1^{\natural}.
$$
It commutes with the complex conjugation and with the dagger, ${}^{\natural}\bar{\cdot}=\bar{\cdot}\,{}^{\natural}$ and ${}^{\natural}{}^{*}={}^{*}{}^{\natural}$, and it exchanges the sides of the left and right multiplications,
$$
{}^{\natural}L_{\tilde Q_1}{}^{\natural}=R_{\tilde Q_1^{\natural}},\qquad
{}^{\natural}R_{\tilde Q_2}{}^{\natural}=L_{\tilde Q_2^{\natural}}.
$$

*Proof.* ${}^{\natural}$ is quaternion conjugation on the coefficients, and quaternion conjugation reverses products; on the units, $\vec e_\mu^{\natural}=-\vec e_\mu$ and $(-\vec e_\mu)(-\vec e_\nu)=\vec e_\mu\vec e_\nu=-(\vec e_\nu\vec e_\mu)$ for $\mu\neq\nu$. The commutation with $\bar{\cdot}$ is that $i$ is fixed and $\bar{\cdot}$ acts on the coefficients, and ${}^{*}={}^{\natural}\circ\bar{\cdot}$ commutes with ${}^{\natural}$ because $\bar{\cdot}$ does and ${}^{\natural}{}^{2}=\mathrm{id}$. For the last identities, $\bigl({}^{\natural}L_{\tilde Q_1}{}^{\natural}\bigr)(\tilde Q_3)={}^{\natural}(\tilde Q_1\tilde Q_3^{\natural})=\tilde Q_3\tilde Q_1^{\natural}=R_{\tilde Q_1^{\natural}}\tilde Q_3$; the second is the same computation.

**Remark (the matrix picture).** Under $\mathsf{M}_2$ the natural conjugation is the adjugate, $\mathsf{M}_2(\tilde Q^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q)=\mathsf{A}\,\mathsf{M}_2(\tilde Q)^{\mathsf T}\mathsf{A}^{-1}$ with $\mathsf{A}=i\sigma_2$, and the anti-automorphism property is $\operatorname{adj}(MN)=\operatorname{adj}(N)\operatorname{adj}(M)$.

## The Eigenspaces and the Fundamental Decomposition

**Theorem (the decomposition is the $\natural$-splitting).** The eigenspaces of $J$ are
$$
\mathbb{B}_{+}=\ker(J-\mathrm{id})=\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{C}}\{e_t\},\qquad
\mathbb{B}_{-}=\ker(J+\mathrm{id})=\mathbb{V}_{\mathbb{B}}=\{Q_{1t}=0\},
$$
the centre and the vector subspace. They are the positive and the negative definite parts of the fundamental decomposition
$$
\boxed{\; \mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathbb{V}_{\mathbb{B}},\qquad \mathbb{C}_{\mathbb{B}}\perp\mathbb{V}_{\mathbb{B}} \;},
$$
of complex dimensions $(1,3)$ and real dimensions $(2,6)$.

*Proof.* An element is fixed by $J$ exactly when its vector coefficients vanish, that is when it lies in the centre, and it is negated exactly when its scalar coefficient vanishes. $J^{2}=\mathrm{id}$ gives the direct sum, and orthogonality is the sign computation of the form. The dimensions are read from the coefficients.

**Corollary (the spectrum).** The eigenvalues of $J$ are $+1$ and $-1$, with multiplicities $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$.

**Corollary (the fundamental decomposition is algebra data).** The fundamental decomposition is exactly the eigenspace splitting of one of the four involutions of the algebra; the remarkable subspaces and their dimensions determine it, and it needs no choice. The centre is the positive part and the vector subspace the negative part.

*Proof.* The statement is the theorem together with the identification of the fixed and anti-fixed spaces of ${}^{\natural}$ in *Comparison of the Remarkable Subspaces*.

## Fundamental Decompositions and the Family of Symmetries

**Definition.** A **fundamental decomposition** of $\mathbb{B}$ is a Krein-orthogonal splitting $\mathbb{B}=\mathbb{W}_+\perp_K\mathbb{W}_-$ into a positive definite and a negative definite subspace. Its **fundamental symmetry** is the involution $J_{\mathbb{W}}$ acting as $+\mathrm{id}$ on $\mathbb{W}_+$ and as $-\mathrm{id}$ on $\mathbb{W}_-$.

**Theorem (the symmetry of a positive line).** Let $\mathbb{W}=\mathbb{C}w$ be a positive definite line, $w=e_t+\tilde V$ with $\lVert\tilde V\rVert_E<1$. Then
$$
J_{\mathbb{W}}(\tilde Q)=\frac{2\langle\tilde Q,w\rangle_{\natural*}}{\langle w,w\rangle_{\natural*}}\,w-\tilde Q,
\qquad
J_{\mathbb{W}}^2=\mathrm{id},
$$
$J_{\mathbb{W}}$ is self-adjoint for the form, has signature $(2,6)$ over $\mathbb{R}$, has $+1$-eigenspace $\mathbb{W}$ and $-1$-eigenspace $\mathbb{W}^{\perp_K}$, and is self-adjoint for the positive definite **companion of the decomposition**
$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\mathbb{W}}=\langle\tilde Q_1,J_{\mathbb{W}}\tilde Q_2\rangle_{\natural*},
\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\langle J_{\mathbb{W}}\tilde Q_1,\tilde Q_2\rangle_{\mathbb{W}}.
$$
It coincides with $J=\natural$ exactly for $\tilde V=0$, and only then does its companion coincide with the fixed companion $\langle\cdot,\cdot\rangle_*$.

*Proof.* The Krein-orthogonal projection onto $\mathbb{W}$ along $\mathbb{W}^{\perp_K}$ is $P_{\mathbb{W}}(\tilde Q)=\langle\tilde Q,w\rangle_{\natural*}/\langle w,w\rangle_{\natural*}\,w$, since $\tilde Q-P_{\mathbb{W}}\tilde Q$ is orthogonal to $w$; the reflection in the two eigenspaces is $2P_{\mathbb{W}}-\mathrm{id}$, which is the displayed formula. An orthogonal projection is self-adjoint for the form, hence so is the reflection, and $J_{\mathbb{W}}^2=4P_{\mathbb{W}}^2-4P_{\mathbb{W}}+\mathrm{id}=\mathrm{id}$. The signature is $(1,3)$ in complex dimension, that is $(2,6)$ over $\mathbb{R}$, because the two eigenspaces have those dimensions. The companion is positive definite: for $\tilde Q=w_++w_-$ with $w_\pm\in\mathbb{W}_\pm$ one has $J_{\mathbb{W}}\tilde Q=w_+-w_-$ and hence $\langle\tilde Q,\tilde Q\rangle_{\mathbb{W}}=\langle w_+,w_+\rangle_{\natural*}-\langle w_-,w_-\rangle_{\natural*}>0$. The reflection is self-adjoint for it because $\langle J_{\mathbb{W}}\tilde Q_1,\tilde Q_2\rangle_{\mathbb{W}}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\langle\tilde Q_1,J_{\mathbb{W}}\tilde Q_2\rangle_{\mathbb{W}}$, using $J_{\mathbb{W}}^2=\mathrm{id}$ and its isometry for the form. At $\tilde V=0$ the line is the centre and the reflection is $J$; for $\tilde V\neq0$ the line is not the centre and $J_{\mathbb{W}}\neq J$. The companion coincides with $\langle\cdot,\cdot\rangle_*$ only when $J_{\mathbb{W}}=J$, since the two companion forms determine their symmetries.

**Corollary (the family of fundamental symmetries).** The map $\tilde V\mapsto J_{\mathbb{W}(\tilde V)}$ is a bijection from the open unit ball $\{\tilde V\in\mathbb{V}_{\mathbb{B}}:\lVert\tilde V\rVert_E<1\}$ onto the set of $\mathbb{C}$-linear fundamental symmetries of the Krein form. Every such symmetry is a reflection in a positive definite line, and the algebraic member of the family is $J=\natural$.

*Proof.* Every $\mathbb{C}$-linear fundamental decomposition has a positive definite part of complex dimension one, which is a line $\ell_{\tilde V}$ with $\lVert\tilde V\rVert_E<1$ by the theorem on the positive lines, and its symmetry is the reflection displayed. Distinct $\tilde V$ give distinct lines, hence distinct reflections, and every $\tilde V$ in the ball gives a symmetry. The last statement is the case $\tilde V=0$.

**Theorem (the algebraic member is unique).** The natural conjugation ${}^{\natural}=J_0$ is the unique fundamental symmetry of the Krein form that is a $\mathbb{C}$-algebra anti-automorphism, equivalently the unique one that fixes the identity and satisfies $J(\tilde Q_1\tilde Q_2)=J(\tilde Q_2)J(\tilde Q_1)$. In the parametrisation above it is the member $\tilde V=0$.

*Proof.* Let $J$ be a fundamental symmetry and a unital $\mathbb{C}$-algebra anti-automorphism. For every $\tilde Q$, $J(\tilde Q e_t)=J(e_t)J(\tilde Q)$ and $J(e_t\tilde Q)=J(\tilde Q)J(e_t)$; since $J$ is bijective, $J(e_t)$ is a two-sided unit. The algebra has the unique unit $e_t$, so $J(e_t)=e_t$. The $+1$-eigenspace of $J$ is a complex subspace of dimension one (the positive index) and contains $e_t$; hence it is $\mathbb{C}_{\mathbb{B}}$, and $J$ is $+\mathrm{id}$ on the centre and $-\mathrm{id}$ on the vector subspace, which is ${}^{\natural}$. Conversely ${}^{\natural}$ is such a symmetry by the two preceding sections.

**Corollary (the tilted symmetries are not algebraic).** For $\tilde V\neq0$ the symmetry $J_{\mathbb{W}(\tilde V)}$ fixes no algebra structure: it does not preserve the multiplication, and it does not even fix $e_t$, since $e_t\notin\ell_{\tilde V}$.

*Proof.* $e_t\in\ell_{\tilde V}$ would force $\tilde V\in\mathbb{V}_{\mathbb{B}}\cap\mathbb{C}_{\mathbb{B}}=0$.

## Krein Orthogonality and the Complement

**Definition.** Two elements are **Krein-orthogonal**, written $\tilde Q_1\perp_K\tilde Q_2$, when $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=0$; two subspaces are Krein-orthogonal when every element of one is orthogonal to every element of the other. The **Krein-orthogonal complement** of $\mathbb{W}$ is
$$
\mathbb{W}^{\perp_K}=\{\tilde Q:\langle\tilde Q,\tilde W\rangle_{\natural*}=0\ \text{for every}\ \tilde W\in\mathbb{W}\}.
$$

**Example (a self-orthogonal line).** The line $\mathbb{W}=\mathbb{C}(e_t+\vec e_x)$ is isotropic, so $\mathbb{W}\subseteq\mathbb{W}^{\perp_K}$ and $\mathbb{W}+\mathbb{W}^{\perp_K}=\mathbb{W}^{\perp_K}$, of dimension three; the line and its complement span four dimensions only together with a vector outside both, and no direct sum decomposition of the algebra is obtained from $\mathbb{W}$ alone.

**Theorem (the dimension formula).** Let $\mathbb{W}$ be a subspace of complex dimension $k$. Then $\dim_{\mathbb{C}}\mathbb{W}^{\perp_K}=4-k$, and over $\mathbb{R}$, for a real subspace of dimension $k_{\mathbb{R}}$, $\dim_{\mathbb{R}}\mathbb{W}^{\perp_K}=8-k_{\mathbb{R}}$. Consequently
$$
\boxed{\;\dim\mathbb{W}+\dim\mathbb{W}^{\perp_K}=\dim\mathbb{B},\qquad
\mathbb{B}=\mathbb{W}\oplus\mathbb{W}^{\perp_K}\iff\mathbb{W}\cap\mathbb{W}^{\perp_K}=\{0\}\; }.
$$

*Proof.* The form is non-degenerate, so the map $\Phi:\mathbb{B}\to\mathbb{W}^{*}$, $\Phi(\tilde Q)(\tilde W)=\langle\tilde Q,\tilde W\rangle_{\natural*}$, is surjective: every antilinear functional on $\mathbb{W}$ extends to $\mathbb{B}$, and the Riesz isomorphism of the non-degenerate form supplies a preimage. Its kernel is $\mathbb{W}^{\perp_K}$, so $\dim\mathbb{W}^{\perp_K}=4-\dim\mathbb{W}^{*}=4-k$, and over $\mathbb{R}$ the same count gives $8-k_{\mathbb{R}}$. The sum is direct exactly when the intersection is zero.

**Corollary (the non-degeneracy criterion).** The restriction of the form to $\mathbb{W}$ is non-degenerate if and only if $\mathbb{W}\cap\mathbb{W}^{\perp_K}=\{0\}$, and then $\mathbb{B}=\mathbb{W}\oplus\mathbb{W}^{\perp_K}$ with both summands non-degenerate and $(\mathbb{W}^{\perp_K})^{\perp_K}=\mathbb{W}$.

*Proof.* A vector of $\mathbb{W}$ orthogonal to all of $\mathbb{W}$ is exactly an element of $\mathbb{W}\cap\mathbb{W}^{\perp_K}$, so the restriction is non-degenerate exactly when that intersection vanishes. The dimension formula then gives the direct sum. For the double complement, $\mathbb{W}\subseteq(\mathbb{W}^{\perp_K})^{\perp_K}$ and both sides have dimension $k$ once $\mathbb{W}^{\perp_K}$ is non-degenerate, which follows by applying the criterion to it.

**Remark (the two complements).** The Krein-orthogonal complement is not the Euclidean one, and it is not a lattice-theoretic complement: the map $\mathbb{W}\mapsto\mathbb{W}^{\perp_K}$ is order-reversing, but $\mathbb{W}\cap\mathbb{W}^{\perp_K}$ may be nonzero and $\mathbb{W}+\mathbb{W}^{\perp_K}$ may be proper, as the isotropic line shows.

## The Classification of Subspaces

**Definition.** A subspace $\mathbb{W}$ is **positive definite** when $\langle\tilde Q,\tilde Q\rangle_{\natural*}>0$ for every nonzero $\tilde Q\in\mathbb{W}$, **negative definite** when the inequality is reversed, and **definite** when it is one of the two. It is **neutral** or **totally isotropic** when the form vanishes on it identically, and **degenerate** when it contains a nonzero element orthogonal to all of itself. A nonzero element with $\langle\tilde Q,\tilde Q\rangle_{\natural*}=0$ is **isotropic**.

**Theorem (the definite dimensions).** A positive definite subspace has complex dimension at most $1$ and real dimension at most $2$; a negative definite subspace has complex dimension at most $3$ and real dimension at most $6$. The bounds are attained by $\mathbb{C}_{\mathbb{B}}$ and by $\mathbb{V}_{\mathbb{B}}$.

*Proof.* A definite subspace meets a definite subspace of the opposite sign only at the origin, since a nonzero vector cannot have both a positive and a negative value. A positive definite subspace therefore injects into $\mathbb{B}/\mathbb{V}_{\mathbb{B}}$, of complex dimension $1$, and a negative definite one into $\mathbb{B}/\mathbb{C}_{\mathbb{B}}$, of complex dimension $3$. The centre and the vector subspace attain the bounds.

**Theorem (the inertia of a definite complement).** Let $\mathbb{W}$ be positive definite of complex dimension $k$. Then $\mathbb{W}$ is non-degenerate and $\mathbb{W}^{\perp_K}$ has signature $(1-k,3)$; at $k=1$ the complement is negative definite of dimension three. Over $\mathbb{R}$, a positive definite plane has a negative definite complement of dimension six.

*Proof.* Non-degeneracy is the vanishing of $\mathbb{W}\cap\mathbb{W}^{\perp_K}$, and the inertia is additive over an orthogonal direct sum: the ambient signature $(1,3)$ is the sum of the signatures of $\mathbb{W}$ and $\mathbb{W}^{\perp_K}$. At $k=1$ the complement has signature $(0,3)$, and its realification $(0,6)$.

**Remark (the indefinite rows).** The quaternion, anti-quaternion, Hermitian and anti-Hermitian subspaces are non-degenerate of signature $(1,3)$ and are neither definite nor neutral; their restriction matrices and null cones are *Remarkable Subspaces under the General Quaternionic Sesqualgebra*.

## The Krein Projections

**Definition.** An operator $P$ is a **Krein-orthogonal projection** when $P^2=P$ and $\operatorname{ran}P\perp_K\ker P$. It is a **$J$-self-adjoint idempotent** when in addition $P^{\dagger}=P$, where $T^{\dagger}=JT^{*}J$ is the adjoint for the Krein form.

**Theorem (the $J$-self-adjoint idempotents).** For an idempotent $P$ the following are equivalent: $P^{\dagger}=P$; $\operatorname{ran}P$ is non-degenerate and $P$ is the Krein-orthogonal projection onto it along $(\operatorname{ran}P)^{\perp_K}$; $\ker P=(\operatorname{ran}P)^{\perp_K}$. The class is strictly larger than the class of definite-orthogonal projections commuting with $J$.

*Proof.* If $P^2=P$ and $P^{\dagger}=P$ then, for $\tilde Q\in\operatorname{ran}P$ and $\tilde Q_3\in\ker P$,
$$
\langle\tilde Q,\tilde Q_3\rangle_{\natural*}=\langle P\tilde Q,\tilde Q_3\rangle_{\natural*}=\langle\tilde Q,P\tilde Q_3\rangle_{\natural*}=0,
$$
so the range and the kernel are orthogonal; $\mathbb{B}=\operatorname{ran}P\oplus\ker P$ because $P$ is idempotent, and $\ker P=(\operatorname{ran}P)^{\perp_K}$ by the dimension formula. The range is non-degenerate: if $\tilde Q\in\operatorname{ran}P$ is orthogonal to the range, then it is orthogonal to the kernel as well, because the range and the kernel are orthogonal; hence $\langle\tilde Q,\tilde Q_3\rangle_{\natural*}=0$ for every $\tilde Q_3\in\mathbb{B}$, and $\tilde Q=0$ by non-degeneracy of the ambient form. Conversely, a Krein-orthogonal projection onto a non-degenerate range satisfies $\langle P\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\langle\tilde Q_1,P\tilde Q_2\rangle_{\natural*}$ by decomposing both arguments along range and kernel, so $P^{\dagger}=P$. A definite-orthogonal projection commuting with $J$ has a $J$-invariant range, hence a range that is a sum of eigenspaces of $J$; it is $J$-self-adjoint, so the definite-orthogonal projections commuting with $J$ form a proper subclass. The projection onto $\mathbb{C}(e_t+\tfrac12\vec e_x)$ along its complement is $J$-self-adjoint but does not commute with $J$.

**Remark (the spectral projections).** The projections $\pi_+=\tfrac12(\mathrm{id}+J)$ and $\pi_-=\tfrac12(\mathrm{id}-J)$ onto the centre and the vector subspace are the two spectral projections of $J$; both are $J$-self-adjoint idempotents. The idempotents with $J$-invariant range are $0,\pi_+,\pi_-,\mathrm{id}$; all the others mix the two eigenspaces, among them the projections onto the positive definite lines $\mathbb{C}(e_t+\tilde V)$ with $\tilde V\neq0$ and the indefinite ranges such as $\mathrm{span}\{e_t,\vec e_x\}$.

## The Krein Gram–Schmidt Process

**Theorem (orthogonalisation).** Let $\mathbb{W}$ be a non-degenerate subspace with a basis $w_1,\dots,w_k$. If $w_1$ is not isotropic, the replacements
$$
w_j\longmapsto w_j-\frac{\langle w_j,w_1\rangle_{\natural*}}{\langle w_1,w_1\rangle_{\natural*}}\,w_1,
\qquad j=2,\dots,k,
$$
leave the span unchanged, make $w_1$ Krein-orthogonal to the rest, and reduce the problem to the non-degenerate subspace $\mathbb{W}\cap w_1^{\perp_K}$; induction gives a Krein-orthogonal basis. If the basis consists of isotropic vectors, a hyperbolic pair $u,v$ with $\langle u,v\rangle_{\natural*}=1$ is chosen first, and the process is applied to the orthogonal complement of $\mathrm{span}\{u,v\}$.

*Proof.* The displayed element is orthogonal to $w_1$ by construction, and the transition matrix from the original basis is unitriangular, so the span is unchanged. The intersection $\mathbb{W}\cap w_1^{\perp_K}$ has dimension $k-1$ because $w_1$ is non-isotropic and $\mathbb{W}$ is non-degenerate, and the restriction to it is non-degenerate by the criterion. A hyperbolic pair exists in a non-degenerate subspace carrying an isotropic vector: some $v$ has $\langle u,v\rangle_{\natural*}\neq0$, and scaling $v$ gives the value one. The induction terminates because the dimension drops by one at each step, or by two when a hyperbolic pair is removed.

**Corollary (definite bases).** Every definite subspace has an orthonormal basis, each vector of form value $+1$ in the positive case and $-1$ in the negative case. An isotropic vector has $\langle\tilde Q,\tilde Q\rangle_{\natural*}=0$ and cannot be normalised to either sign, which is the only obstruction to the process.

## The Isotropic Elements

**Definition.** The **null set** of the Krein form is
$$
\mathcal K=\{\tilde Q\in\mathbb{B}:\langle\tilde Q,\tilde Q\rangle_{\natural*}=0\}.
$$

**Theorem (the equation of the null set).** Writing $\tilde Q=c+\vec v$ with $c\in\mathbb{C}$ and $\vec v\in\mathbb{C}^3$,
$$
\boxed{\;\langle\tilde Q,\tilde Q\rangle_{\natural*}=\lvert c\rvert^2-\lVert\vec v\rVert_E^2
=\lvert Q_t\rvert^2-\sum_{k}\lvert Q_k\rvert^2\; }.
$$
The null set is the set $\lVert c\rVert_E=\lVert\vec v\rVert_E$, a real algebraic cone with apex the origin, of real dimension $7$, and the apex is its only singular point.

*Proof.* The formula is the definition with $Q_{1\mu}=Q_{2\mu}$, and the left side is real. The set is the zero set of one non-constant real polynomial in the eight real coordinates, homogeneous of degree two. Its gradient with respect to the real coordinates of $c$ and of $\vec v$ is $2(c,-v)$, which vanishes only at the origin, so the zero set is a smooth hypersurface away from the apex, of real dimension $8-1=7$.

**Example (two isotropic elements and one that is not).** $e_t+\vec e_x$ is isotropic, with $\langle e_t+\vec e_x,e_t+\vec e_x\rangle_{\natural*}=1-1=0$, and its square is $2\vec e_x$, so it is not a zero divisor. $\vec e_x+i\vec e_y$ is not isotropic, with value $-1-1=-2$, although its norm $\langle\vec e_x+i\vec e_y\rangle_{\natural}=1+i^2=0$ vanishes: it is a zero divisor, and its line is negative definite. $e_t+i\vec e_x$ is isotropic and a zero divisor, with square $2(e_t+i\vec e_x)$; the half $\tfrac12(e_t+i\vec e_x)$ is the idempotent of the Peirce line.

**Remark (the two cones).** The null set is not the cone of the algebraic norm $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$, of real dimension $6$; the two meet in the doubly null lines of the next section. The comparison of the two geometries is *The Four Forms and the Four Algebraic Norms* and *The Krein Level Sets and the Hyperbolic Structure*.

## The Totally Isotropic Subspaces and the Witt Index

**Definition.** A subspace $\mathbb{W}$ is **totally isotropic** when $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=0$ for all $\tilde Q_1,\tilde Q_2\in\mathbb{W}$, equivalently when $\mathbb{W}\subseteq\mathbb{W}^{\perp_K}$; it is **maximal** when it is contained in no larger one. The **Witt index** is the common dimension of the maximal totally isotropic subspaces.

**Theorem (the Witt index).** The Witt index is $\min(1,3)=1$ over $\mathbb{C}$ and $\min(2,6)=2$ over $\mathbb{R}$. A maximal totally isotropic complex subspace is $\mathbb{C}(e_t+\vec e_x)$, and a maximal totally isotropic real subspace is the plane
$$
\mathbb{W}_{\mathrm{iso}}=\mathrm{span}_{\mathbb{R}}\{e_t+\vec e_x,\ i(e_t+\vec e_x)\}.
$$
Every totally isotropic subspace is contained in a maximal one, and the automorphism group $\mathrm{U}(1,3)$ acts transitively on the maximal ones.

*Proof.* A totally isotropic subspace meets a definite subspace only at the origin, since a nonzero element of a definite subspace has a nonzero value. It therefore injects into $\mathbb{B}/\mathbb{V}_{\mathbb{B}}$, of complex dimension $1$, and into $\mathbb{B}/\mathbb{C}_{\mathbb{B}}$, of complex dimension $3$; hence its complex dimension is at most $1$, and over $\mathbb{R}$ its real dimension is at most $2$. The line and the plane displayed are totally isotropic:
$$
\langle e_t+\vec e_x,e_t+\vec e_x\rangle_{\natural*}=0,\qquad
\langle i(e_t+\vec e_x),e_t+\vec e_x\rangle_{\natural*}=i-i=0,\qquad
\langle i(e_t+\vec e_x),i(e_t+\vec e_x)\rangle_{\natural*}=1-1=0.
$$
They attain the bounds. Witt's extension theorem for general plain sesquilinear forms gives the extension property and the transitivity.

**Remark (the real index).** The real plane is a complex line, closed under multiplication by $i$; it is the realification of $\mathbb{C}(e_t+\vec e_x)$. Every real totally isotropic plane is such a realification: if a real plane $\mathbb{W}$ were totally isotropic and not complex, then $\mathbb{W}+i\mathbb{W}$ would be a complex totally isotropic plane of dimension two, beyond the Witt index one. The Witt index counts the largest dimension and is two over $\mathbb{R}$.

## The Doubly Null Lines and the Peirce Lines

**Definition.** A **doubly null line** is an isotropic line that lies in the cone of the algebraic norm as well: a complex line $\mathbb{C}\tilde Q$ with $\langle\tilde Q,\tilde Q\rangle_{\natural*}=0$ and $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2=0$.

**Theorem (the Peirce lines).** For every real unit vector $\vec u\in\mathbb{V}_{\mathbb{B}}$, with $\tilde\Xi=i\vec u$, the elements
$$
\tilde\Pi_\pm(\tilde\Xi)=\tfrac12\bigl(e_t\pm\tilde\Xi\bigr)
$$
are rank-one Hermitian idempotents, $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\tilde\Pi_\pm^{*}=\tilde\Pi_\pm$, with $\langle\tilde\Pi_\pm\rangle_{\natural}=0$ and $\langle\tilde\Pi_\pm,\tilde\Pi_\pm\rangle_{\natural*}=0$. Each line $\mathbb{C}\tilde\Pi_\pm(\tilde\Xi)$ is a maximal totally isotropic complex subspace and a doubly null line; it is a **Peirce line** of the algebra, generating the minimal left ideal $\mathbb{B}\tilde\Pi_\pm(\tilde\Xi)$ and the minimal right ideal $\tilde\Pi_\pm(\tilde\Xi)\mathbb{B}$, of complex dimension two, every element of which is a zero divisor.

*Proof.* A real unit vector has $\vec u^2=-e_t$, so $\tilde\Xi^2=i^2\vec u^2=e_t$ and $(e_t\pm\tilde\Xi)^2=e_t\pm2\tilde\Xi+\tilde\Xi^2=2(e_t\pm\tilde\Xi)$, whence $\tilde\Pi_\pm^2=\tilde\Pi_\pm$. The idempotent is Hermitian because $\tilde\Xi^{*}=\tilde\Xi$, and rank one because its matrix model has trace one and its square is itself. For the two values,
$$
\langle e_t\pm\tilde\Xi\rangle_{\natural}=1+\langle\tilde\Xi\rangle_{\natural}=1-\lVert\vec u\rVert_E^2=0,
\qquad
\langle e_t\pm\tilde\Xi,e_t\pm\tilde\Xi\rangle_{\natural*}=1-\lVert\tilde\Xi\rVert_E^2=0.
$$
The minimal ideals are the standard rank-one ideals of the algebra, of complex dimension two, and their elements $X\tilde\Pi_\pm$ satisfy $\langle X\tilde\Pi_\pm\rangle_{\natural}=\langle X\rangle_{\natural}\langle\tilde\Pi_\pm\rangle_{\natural}=0$, so they are zero divisors.

**Corollary (the doubly null lines are the Peirce lines).** The doubly null lines are exactly the lines $\mathbb{C}(e_t+i\vec u)$ and $\mathbb{C}(e_t-i\vec u)$ with $\vec u$ a real unit vector.

*Proof.* Write $\tilde Q=c(e_t+\tilde Q_3)$ with $\lVert\tilde Q_3\rVert_E=1$, which is possible on any isotropic line. The norm condition reads $1+\langle\tilde Q_3\rangle_{\natural}=0$. Writing $\tilde Q_3=\tilde S+i\tilde W$ with $\tilde S,\tilde W\in\mathbb{V}_{\mathbb{B}}$ real, this is the system
$$
\lVert\tilde S\rVert_E^2+\lVert\tilde W\rVert_E^2=1,\qquad
\lVert\tilde S\rVert_E^2-\lVert\tilde W\rVert_E^2=-1,\qquad
\langle\tilde S,\tilde W\rangle=0,
$$
which forces $\tilde S=0$ and $\lVert\tilde W\rVert_E=1$; hence $\tilde Q_3=i\tilde W$ with $\tilde W$ a real unit vector, and the line is $\mathbb{C}(e_t+i\vec W)$.

**Remark (the real maximal plane is not a Peirce line).** The maximal totally isotropic real plane $\mathrm{span}_{\mathbb{R}}\{e_t+\vec e_x,i(e_t+\vec e_x)\}$ is generated by an element of norm $2$, not a zero divisor; it is not a Peirce line, and the Peirce lines are the norm-null part of the isotropic lines. The zero divisors and the minimal ideals are *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## The Isotropic Lines

**Theorem (the isotropic lines form $S^5$).** The isotropic complex lines are exactly the lines $\mathbb{C}(e_t+\tilde Q_1)$ with $\lVert\tilde Q_1\rVert_E=1$, and the assignment $\tilde Q_1\mapsto\mathbb{C}(e_t+\tilde Q_1)$ is a bijection from the unit sphere of $\mathbb{V}_{\mathbb{B}}\cong\mathbb{C}^3$, a copy of $S^5$, onto the set of isotropic lines.

*Proof.* An isotropic line $\mathbb{C}\tilde Q$ has $\lVert c\rVert_E=\lVert\vec v\rVert_E$, so it is not contained in $\mathbb{V}_{\mathbb{B}}$ and admits a representative with nonzero scalar part; scaling gives exactly one representative of the form $e_t+\tilde Q_1$. For that representative $\langle e_t+\tilde Q_1,e_t+\tilde Q_1\rangle_{\natural*}=1-\lVert\tilde Q_1\rVert_E^2$, so the line is isotropic exactly for $\lVert\tilde Q_1\rVert_E=1$. Distinct points of the unit sphere give distinct lines, since $e_t+\tilde Q_1$ and $e_t+\tilde Q_1'$ span the same line only if $\tilde Q_1=\tilde Q_1'$.

**Corollary (the boundary of the ball).** The isotropic lines are the boundary of the open ball $\{\lVert\tilde V\rVert_E<1\}$ that parametrises the maximal positive definite subspaces: the ball is the unit ball of $\mathbb{V}_{\mathbb{B}}\cong\mathbb{C}^3$ and its boundary is the sphere $S^5$. The identification of the boundary, the ball and the hyperbolic metric is *The Krein Level Sets and the Hyperbolic Structure*.

## The Krein Cone

**Definition.** The **Krein cone** is
$$
P_K=\{\tilde Q\in\mathbb{B}:\langle\tilde Q,\tilde Q\rangle_{\natural*}\ge0\}
=\{\tilde Q:\lVert c\rVert_E\ge\lVert\vec v\rVert_E\}.
$$

**Theorem (the shape of the cone).** The Krein cone is closed, invariant under multiplication by positive real scalars, star-shaped with respect to the origin, and contractible. Its interior is the **positive region** $\{\lVert c\rVert_E>\lVert\vec v\rVert_E\}$, its boundary is the null set $\mathcal K$, and its interior is homotopy equivalent to a circle,
$$
P_K^{\circ}\simeq S^1.
$$
It is neither convex nor pointed: it is invariant under $\tilde Q\mapsto-\tilde Q$, so $P_K\cap(-P_K)=P_K$, which is larger than $\{0\}$.

*Proof.* Closedness is the closedness of the inequality, and homogeneity is $\langle\lambda\tilde Q,\lambda\tilde Q\rangle_{\natural*}=\lvert\lambda\rvert^2\langle\tilde Q,\tilde Q\rangle_{\natural*}$ for real $\lambda$. The straight-line homotopy $\tilde Q\mapsto t\tilde Q$ preserves the inequality, so the cone is star-shaped and contractible. The interior is the strict inequality and the boundary the equality. For the homotopy type, the map $\tilde Q\mapsto\tilde Q/\sqrt{\langle\tilde Q,\tilde Q\rangle_{\natural*}}$ retracts the interior onto the level set $\{\langle\tilde Q,\tilde Q\rangle_{\natural*}=1\}=\{\lVert c\rVert_E^2-\lVert\vec v\rVert_E^2=1\}$, in which $c$ runs over a circle of radius $\sqrt{1+\lVert\vec v\rVert_E^2}$ and $\vec v$ over all of $\mathbb{C}^3$; the level set is therefore $S^1\times\mathbb{R}^6$, and it retracts further onto $S^1$. The failure of pointedness is the sign invariance, since the defining inequality is even; the failure of convexity is exhibited below.

**Example (the cone is not convex).** The elements $e_t+\vec e_y$ and $-e_t+\vec e_y$ both lie in $P_K$, with form value $1-1=0$; their midpoint $\vec e_y$ has form value $-1$, so it lies outside. The cone is therefore not convex, although it is star-shaped.

**Remark (the level sets inside the cone).** The positive level set of level $t>0$ is a hyperboloid sheet inside the interior of $P_K$, the negative level set lies outside, and the null set is the boundary. The cone is the union of the positive level sets of all $t\ge0$, rescaled to $t=1$ by positive real scaling; the global geometry is *The Krein Level Sets and the Hyperbolic Structure*.

## The Intersection with the Hermitian Cone

**Definition.** The Hermitian subspace is $\mathbb{M}_+=\{\tilde Q:\tilde Q^{*}=\tilde Q\}$, with coordinates $Q_t=q_t$ real and $Q_k=iq'_k$ with $q'_k$ real. The **Hermitian cone** is
$$
P=\{\tilde Q\in\mathbb{M}_+:\mathsf{M}_2(\tilde Q)\succeq0\}
=\{q_t\ge0,\ q_t^2\ge (q'_x)^2+(q'_y)^2+(q'_z)^2\},
$$
the cone of the positive semidefinite Hermitian matrices.

**Theorem (the intersection).** On $\mathbb{M}_+$ the Krein form is the interval form $q_t^2-\sum_k(q'_k)^2$, and
$$
P_K\cap\mathbb{M}_+=\{q_t^2\ge(q'_x)^2+(q'_y)^2+(q'_z)^2\},
$$
the full closed cone of the interval form, whose future nappe is the Hermitian cone $P$. In particular $P\subseteq P_K$.

*Proof.* On $\mathbb{M}_+$ the coefficients are $(q_t,iq'_x,iq'_y,iq'_z)$, so $\lvert Q_t\rvert^2=q_t^2$ and $\lvert Q_k\rvert^2=(q'_k)^2$; the form reads $q_t^2-\sum_k(q'_k)^2$, and the Krein inequality is the displayed cone. The matrix $\mathsf{M}_2(\tilde Q)=q_t\mathrm{I}_2+q'_x\sigma_x+q'_y\sigma_y+q'_z\sigma_z$ is Hermitian with eigenvalues $q_t\pm\lVert\vec q'\rVert_E$, so positive semidefiniteness is $q_t\ge\lVert\vec q'\rVert_E$, which is the future nappe.

**Remark (the other real forms).** On each of the other three real forms the form is the same interval form in the coordinates of its row, so the intersection of $P_K$ with each is the corresponding Lorentzian cone; the signatures and the coordinates are *Remarkable Subspaces under the General Quaternionic Sesqualgebra*.

## The Operator Cone and the Cartan Involution

**Definition.** An operator $T\in\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is **$J$-positive** when it is $J$-self-adjoint, $T^{\dagger}=T$, and $\langle\tilde Q,T\tilde Q\rangle_{\natural*}\ge0$ for every $\tilde Q$. The **$J$-positive cone** is
$$
\mathcal P_J=\{T:T^{\dagger}=T,\ \langle\tilde Q,T\tilde Q\rangle_{\natural*}\ge0\ \forall\tilde Q\}.
$$

**Theorem (the cone as the image of the Hilbert cone).** With $J=\natural$ and $S$ ranging over the self-adjoint operators that are positive semidefinite for the definite companion,
$$
\boxed{\;\mathcal P_J=J\cdot\{S\ge0\}=\{JT:S\ge0\}\; }.
$$
The cone $\mathcal P_J$ is closed and convex, contains $J$, and does not contain the identity. Its extreme rays are the rank-one operators $J\lvert\tilde Q\rangle\langle\tilde Q\rvert$ with $\lVert\tilde Q\rVert_E=1$. Its idempotents are the Krein-orthogonal projections onto the positive definite subspaces, and the only idempotents of $\mathcal P_J$ that commute with $J$ are $\pi_+$ and $0$.

*Proof.* For any $T$, $\langle\tilde Q,T\tilde Q\rangle_{\natural*}=\langle\tilde Q,JT\tilde Q\rangle_*$, so the positivity and the $J$-self-adjointness of $T$ are exactly the self-adjointness and positivity of $JT$ for the definite form. Hence $T\in\mathcal P_J$ exactly when $JT=S\ge0$, that is $T=JS$; the map $S\mapsto JS$ is linear and bijective and carries the closed convex cone $\{S\ge0\}$ onto $\mathcal P_J$. The identity $T=J$ gives $JT=\mathrm{id}\ge0$, so $J\in\mathcal P_J$; $T=\mathrm{id}$ gives $JT=J$, which has the negative eigenvalue $-1$, so $\mathrm{id}\notin\mathcal P_J$. A bijective linear map carries extreme rays to extreme rays, and the extreme rays of the positive semidefinite cone are the rank-one operators $\lvert\tilde Q\rangle\langle\tilde Q\rvert$. The idempotent statement is the theorem on the $J$-self-adjoint idempotents together with the criterion of positive definiteness of the range.

**Remark (the two cones are different).** Neither of $\mathcal P_J$ and the Hilbert cone $\{S\ge0\}$ contains the other: $J$ lies in the first and not the second, the identity lies in the second and not the first. The cone $\mathcal P_J$ is the image of the Hilbert cone under the sign involution, not an enlargement of it.

**Remark (the Cartan involution).** On $\mathrm{GL}_4(\mathbb{C})$ the **$J$-Cartan involution** is $\theta_J(T)=(T^{\dagger})^{-1}$. It is an involutive automorphism, its fixed group is the $J$-unitary group $\mathrm{U}_J(\mathbb{B})=\{T:T^{\dagger}T=\mathrm{id}\}\cong\mathrm{U}(1,3)$, and at the identity its differential is $-\dagger$, with fixed Lie algebra the $J$-skew part $\mathfrak u_J\cong\mathfrak u(1,3)$. On $\mathrm{U}_J$ the map $\theta_J$ is the identity; the Cartan involution of the Lie group $\mathrm{U}(1,3)$ itself is the different map $T\mapsto JTJ$, whose fixed subgroup is $\mathrm{U}(1)\times\mathrm{U}(3)$. The two are *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra* and *The Krein Cartan Decomposition of the Operator Algebra*.

## Worked Examples

**A positive vector.** $\tilde Q=e_t+2ie_t$: $\langle\tilde Q,\tilde Q\rangle_{\natural*}=1+4=5>0$, in the centre.

**A negative vector.** $\tilde Q=\vec e_x+\vec e_y$: $\langle\tilde Q,\tilde Q\rangle_{\natural*}=-1-1=-2<0$, in the vector subspace.

**An isotropic element that is not a zero divisor.** $\tilde Q=e_t+\vec e_x$: value $0$, norm $2$, square $2\vec e_x$. The line $\mathbb{C}\tilde Q$ is maximal totally isotropic.

**A zero divisor that is not isotropic.** $\tilde Q=\vec e_x+i\vec e_y$: value $-2$, norm $0$. The norm cone and the Krein null set are different.

**A Peirce idempotent.** With $\vec u=\vec e_x$, $\tilde\Pi_+=\tfrac12(e_t+i\vec e_x)$: $\tilde\Pi_+^2=\tilde\Pi_+$, $\tilde\Pi_+^{*}=\tilde\Pi_+$, $\langle\tilde\Pi_+\rangle_{\natural}=0$, $\langle\tilde\Pi_+,\tilde\Pi_+\rangle_{\natural*}=0$. The line $\mathbb{C}\tilde\Pi_+$ is doubly null.

**A Krein projection that is not definite-orthogonal.** The projection onto $\mathbb{C}(e_t+\tfrac12\vec e_x)$ along its complement has the matrix
$$
P=\begin{pmatrix}4/3&-2/3&0&0\\2/3&-1/3&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
$$
so $P^2=P$, $P^{\dagger}=P$, $P^{*}=P^{\mathsf T}\neq P$, and $PJ\neq JP$.

**A fundamental symmetry at $\tilde V=\tfrac12\vec e_x$.** With $w=e_t+\tfrac12\vec e_x$ and $\langle w,w\rangle_{\natural*}=3/4$,
$$
J_{\mathbb{W}}=\frac{2}{3/4}\langle\cdot,w\rangle_{\natural*}\,w-\mathrm{id}
=\begin{pmatrix}5/3&-4/3\\4/3&-5/3\end{pmatrix}
$$
in the basis $e_t,\vec e_x$; its square is the identity, it is self-adjoint for the form and for its own companion, and it is not $J$.

**The cone is not convex.** $e_t+\vec e_y$ and $-e_t+\vec e_y$ are in $P_K$ and their midpoint $\vec e_y$ is not.

## Summary

The Krein form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ is the general quaternionic sesquilinear form, non-degenerate of signature $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$, with negative index $3$ and $6$ and Pontryagin index $1$ and $2$. Its coefficient Gram matrix is $E=\operatorname{diag}(1,-1,-1,-1)$, of determinant $-1$; in the real basis the complex entries are Hermitian with purely imaginary mixed blocks, and the realified form is $\operatorname{diag}(E,E)$, of signature $(2,6)$. In the $2\times2$ model it is the adjugated Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_2(\tilde Q_2)^{\dagger}\mathsf{M}_2(\tilde Q_1))$, and the adjugate is $J$ itself.

The fundamental symmetry is the natural conjugation $J={}^{\natural}$, with bridge $\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\langle\tilde Q_2,J\tilde Q_1\rangle_{*}$ and eigenspaces the centre and the vector subspace; it is the unique fundamental symmetry that is an algebra anti-automorphism. The other fundamental symmetries are the reflections in the positive definite lines $\mathbb{C}(e_t+\tilde V)$ with $\lVert\tilde V\rVert_E<1$, and they fix no algebra structure. The Krein-orthogonal complement has the dimension formula, and it is a direct complement exactly when the intersection with the subspace vanishes. The null set is the real cone $\lVert c\rVert_E=\lVert\vec v\rVert_E$, of dimension seven, with Witt index $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$; the doubly null lines are the Peirce lines $\mathbb{C}(e_t\pm i\vec u)$, and the isotropic lines form $S^5$. The Krein cone $\lVert c\rVert_E\ge\lVert\vec v\rVert_E$ is closed, star-shaped and contractible, with interior homotopy equivalent to $S^1$, and it is neither convex nor pointed; its intersection with the Hermitian subspace is the closed cone of the interval form. On operators the $J$-positive cone is $J\cdot\{S\ge0\}$, closed and convex, containing $J$ and not the identity, and the $J$-Cartan involution has fixed group $\mathrm{U}(1,3)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | The Krein form |
| $\langle\tilde Q_1,\tilde Q_2\rangle_*=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | The definite companion |
| $G=E=\operatorname{diag}(1,-1,-1,-1)$ | The Gram matrix in the coefficient basis; $\det G=-1$ |
| $G_{\mathbb{R}}=\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1)$ | The matrix of the realified form; signature $(2,6)$ |
| $J={}^{\natural}=\operatorname{diag}(1,-1,-1,-1)$ | The fundamental symmetry; $\langle\cdot,\cdot\rangle_{\natural*}=\langle\cdot,J\cdot\rangle_*$ |
| $\mathbb{C}_{\mathbb{B}}$, $\mathbb{V}_{\mathbb{B}}$ | The $\pm1$-eigenspaces of $J$; centre and vector subspace |
| $\ell_{\tilde V}=\mathbb{C}(e_t+\tilde V)$, $\lVert\tilde V\rVert_E<1$ | The positive definite lines |
| $J_{\mathbb{W}}=2P_{\mathbb{W}}-\mathrm{id}$ | The symmetry of a fundamental decomposition |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\mathbb{W}}=\langle\tilde Q_1,J_{\mathbb{W}}\tilde Q_2\rangle_{\natural*}$ | The positive definite companion of the decomposition |
| $\mathcal K=\{\langle\tilde Q,\tilde Q\rangle_{\natural*}=0\}$ | The null set; $\lvert Q_t\rvert^2=\sum_k\lvert Q_k\rvert^2$ |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | The algebraic norm; its zero set is the zero-divisor cone |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec u)$ | The Peirce idempotents; the doubly null lines |
| $P_K=\{\lVert c\rVert_E\ge\lVert\vec v\rVert_E\}$ | The Krein cone |
| $P$ | The Hermitian cone, the future nappe of $P_K\cap\mathbb{M}_+$ |
| $\mathcal P_J=J\cdot\{S\ge0\}$ | The $J$-positive cone of operators |
| $\theta_J(T)=(T^{\dagger})^{-1}$ | The $J$-Cartan involution; fixed group $\mathrm{U}_J$ |
| $(n,m)=(1,3)$ over $\mathbb{C}$, $(2,6)$ over $\mathbb{R}$ | The signature; $m$ the negative index, $\min(n,m)$ the Pontryagin index |

## Further Reading

- [The Fundamental Symmetry](the-fundamental-symmetry.html), for the general theory and the angular operator.
- [Krein Spaces](krein-spaces.html) and [Pontryagin Spaces](pontryagin-spaces.html), for the general theory of the fundamental symmetry and the two indices.
- [Indefinite Inner Product Spaces](indefinite-inner-product-spaces.html), for the fundamental decomposition and the classification of subspaces.
- [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the restrictions, their signatures, their null cones and the four real forms.
- [The Krein Level Sets and the Hyperbolic Structure](the-krein-level-sets-and-the-hyperbolic-structure.html), for the level sets, the ball and the sphere of isotropic lines.
- [J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra](j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra.html), for the operator theory of the form.
- [The Krein Cartan Decomposition of the Operator Algebra](the-krein-cartan-decomposition-of-the-operator-algebra.html), for the Cartan involution and the symmetric-space decomposition.
- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the comparison of the Krein form with the other three pairings.
- [The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$](the-general-quaternionic-sesqualgebra-in-the-2x2-matrix-element-representation.html), for the adjugated trace identities.
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the fundamental decomposition, the Krein-orthogonal projections and the classification of subspaces.
- Thomas Ya. Azizov and Iosif S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the Krein space, the Witt index and the operator cone.
