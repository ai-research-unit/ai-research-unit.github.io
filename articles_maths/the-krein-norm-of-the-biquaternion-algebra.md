# __The Krein Norm of the Biquaternion Algebra__

## Introduction

The general quaternionic sesquilinear form of the biquaternion algebra is
$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}
=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2}),
\qquad \varepsilon=(1,-1,-1,-1).
$$
It is linear in the first argument and conjugate-linear in the second, and it is non-degenerate, of signature $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$. Read at the two equal arguments it is the **Krein norm** $\langle\tilde Q\rangle_{\natural*}=\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2$, the indefinite companion of the quaternionic norm. Indefiniteness runs through everything below: the form has a canonical involution, its orthogonal complement is not a complement, it has isotropic elements and totally isotropic subspaces, and its non-negative set is a cone. This article reads the form whole and the norm it carries: the inertia, the involution, the orthogonality, the isotropy and the cone.

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of complex dimension four and real dimension eight. The centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ and the vector subspace is $\mathbb{V}_{\mathbb{B}}=\mathrm{span}_{\mathbb{C}}\{\vec e_x,\vec e_y,\vec e_z\}$. An element is written $\tilde Q=c+\vec v$ with $c=Q_t\in\mathbb{C}$ and $\vec v=(Q_x,Q_y,Q_z)\in\mathbb{C}^3$. The Euclidean norm is $\lVert\tilde Q\rVert_E^2=\sum_\mu\lvert Q_\mu\rvert^2$. The **definite companion** is
$$
\langle\tilde Q_1,\tilde Q_2\rangle_*=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}},
$$
and the **fundamental symmetry** is $J={}^{\natural}=\operatorname{diag}(1,-1,-1,-1)$ in the coefficient basis.

The restrictions to the remarkable subspaces are *Remarkable Subspaces under the General Quaternionic Sesqualgebra*; the global level sets and the hyperbolic ball are *The Krein Level Sets and the Hyperbolic Structure*; the operator theory is *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*; the isometry group and the Cartan decomposition are *The Krein Isometry Group and Its Cartan Decomposition*; and the comparison with the other three pairings is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*. This article owns the form itself and its indefinite structure.

## The Form and Its Gram Matrix

**Definition.** The **Gram matrix** of the form in a basis $u_1,\dots,u_n$ is $G_{\mu\nu}=\langle u_\mu,u_\nu\rangle_{\natural*}$.

**Theorem (the coefficient Gram matrix).** In the coefficient basis $e_t,\vec e_x,\vec e_y,\vec e_z$,
$$
\boxed{\; G=\operatorname{diag}(1,-1,-1,-1)=E\; },
$$
so the basis is orthogonal, the diagonal entries are $1,-1,-1,-1$, and $\det G=-1$.

*Proof.* $\langle e_\mu,e_\nu\rangle_{\natural*}=\sum_\lambda\varepsilon_\lambda (e_\mu)_\lambda\overline{(e_\nu)_\lambda}=\varepsilon_\mu\delta_{\mu\nu}$: the units are orthogonal, and each carries its own sign. The determinant is the product $\varepsilon_t\varepsilon_x\varepsilon_y\varepsilon_z=-1$.

**Remark (the real basis and the other forms).** The passage to the real basis, the realified matrix and the signature $(2,6)$ are treated in *The Realification of the General Quaternionic Sesqualgebra*; the four Gram matrices and the four isometry groups are those of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

## Inertia and Positive Subspaces

**Theorem (the signature and the two indices).** Over $\mathbb{C}$ the form has signature $(1,3)$, negative index $3$ and Pontryagin index $1$; over $\mathbb{R}$ it has signature $(2,6)$, negative index $6$ and Pontryagin index $2$, and with the Krein form the algebra is the Pontryagin space $\Pi_{6}$. The passage from the complex reading to the real one doubles both entries and preserves neither.

*Proof.* The eigenspace splitting of $J={}^{\natural}$ is a fundamental decomposition, with positive part the centre $\mathbb{C}_{\mathbb{B}}$ and negative part the vector subspace $\mathbb{V}_{\mathbb{B}}$ (§*The Eigenspaces and the Fundamental Decomposition*), of complex dimensions $1$ and $3$ and therefore of real dimensions $2$ and $6$. The smaller of the two is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$; the subscript of $\Pi_{6}$ records the negative index. The definitions of the signature, of the negative index and of the Pontryagin index, and Sylvester's law, are *The Indefinite Case and the Signature*.

**Theorem (the maximal positive subspaces).** A positive definite subspace has complex dimension at most $1$, and real dimension at most $2$, by the dimension theorem of §*The Classification of Subspaces*. The maximal ones are exactly the lines
$$
\ell_{\tilde V}=\mathbb{C}(e_t+\tilde V),\qquad \tilde V\in\mathbb{V}_{\mathbb{B}},\quad \lVert\tilde V\rVert_E<1,
$$
and over $\mathbb{R}$ the realification of such a line is the positive definite plane $\mathrm{span}_{\mathbb{R}}\{e_t+\tilde V,i(e_t+\tilde V)\}$.

*Proof.* The dimension bound is the theorem of §*The Classification of Subspaces*. A positive definite line has a nonzero scalar coordinate, since $Q_t=0$ gives $\langle\tilde Q,\tilde Q\rangle_{\natural*}=-\lVert\vec Q\rVert_E^2<0$; scaling, the line is $\mathbb{C}(e_t+\tilde V)$ and
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

The natural conjugation is the quaternion conjugation, a unital $\mathbb{C}$-linear anti-automorphism of order two; that, the isometry, its commutation with the other involutions and its exchange of the left and right multiplications are treated in *The Group of Involutions*.

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

## Fundamental Decompositions and the Family of Symmetries

**Definition.** A **fundamental decomposition** of $\mathbb{B}$ is a Krein-orthogonal splitting $\mathbb{B}=\mathbb{W}_+\perp_K\mathbb{W}_-$ into a positive definite and a negative definite subspace. Its **fundamental symmetry** is the involution $J_{\mathbb{W}}$ acting as $+\mathrm{id}$ on $\mathbb{W}_+$ and as $-\mathrm{id}$ on $\mathbb{W}_-$.

**Theorem (the symmetry of a positive line).** Let $\mathbb{W}=\mathbb{C}w$ be a positive definite line, $w=e_t+\tilde V$ with $\lVert\tilde V\rVert_E<1$. Then
$$
J_{\mathbb{W}}(\tilde Q)=\frac{2\langle\tilde Q,w\rangle_{\natural*}}{\langle w,w\rangle_{\natural*}}\,w-\tilde Q,
\qquad
J_{\mathbb{W}}^2=\mathrm{id},
$$
$J_{\mathbb{W}}$ is self-adjoint for the form, has eigenvalue $+1$ of multiplicity $2$ and $-1$ of multiplicity $6$ over $\mathbb{R}$, with eigenspaces $\mathbb{W}$ and $\mathbb{W}^{\perp_K}$, and is self-adjoint for the positive definite **companion of the decomposition**
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

*Proof.* Let $J$ be a fundamental symmetry and a unital $\mathbb{C}$-algebra anti-automorphism. For every $\tilde Q$, $J(\tilde Q e_t)=J(e_t)J(\tilde Q)$ and $J(e_t\tilde Q)=J(\tilde Q)J(e_t)$; since $J$ is bijective, $J(e_t)$ is a two-sided unit. The algebra has the unique unit $e_t$, so $J(e_t)=e_t$. The $+1$-eigenspace of $J$ is a complex subspace of dimension one (the positive index) and contains $e_t$; hence it is $\mathbb{C}_{\mathbb{B}}$, and $J$ is $+\mathrm{id}$ on the centre and $-\mathrm{id}$ on the vector subspace, which is ${}^{\natural}$. Conversely ${}^{\natural}$ is such a symmetry by §*The Natural Conjugation as a Fundamental Symmetry* and a unital anti-automorphism by *The Group of Involutions*.

## Krein Orthogonality and the Complement

**Definition.** Two elements are **Krein-orthogonal**, written $\tilde Q_1\perp_K\tilde Q_2$, when $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=0$; two subspaces are Krein-orthogonal when every element of one is orthogonal to every element of the other. The **Krein-orthogonal complement** of $\mathbb{W}$ is
$$
\mathbb{W}^{\perp_K}=\{\tilde Q:\langle\tilde Q,\tilde W\rangle_{\natural*}=0\ \text{for every}\ \tilde W\in\mathbb{W}\}.
$$

**Example (a self-orthogonal line).** The line $\mathbb{W}=\mathbb{C}(e_t+\vec e_x)$ is isotropic, so $\mathbb{W}\subseteq\mathbb{W}^{\perp_K}$ and $\mathbb{W}+\mathbb{W}^{\perp_K}=\mathbb{W}^{\perp_K}$, of dimension three; the line and its complement span four dimensions only together with a vector outside both, and no direct sum decomposition of the algebra is obtained from $\mathbb{W}$ alone. The dimension formula and the non-degeneracy criterion in general are those of *Indefinite Inner Product Spaces*; the failure above is the biquaternion instance.

## The Classification of Subspaces

**Definition.** A subspace $\mathbb{W}$ is **positive definite** when $\langle\tilde Q,\tilde Q\rangle_{\natural*}>0$ for every nonzero $\tilde Q\in\mathbb{W}$, **negative definite** when the inequality is reversed, and **definite** when it is one of the two. It is **neutral** or **totally isotropic** when the form vanishes on it identically, and **degenerate** when it contains a nonzero element orthogonal to all of itself. A nonzero element with $\langle\tilde Q,\tilde Q\rangle_{\natural*}=0$ is **isotropic**.

**Theorem (the definite dimensions).** A positive definite subspace has complex dimension at most $1$ and real dimension at most $2$; a negative definite subspace has complex dimension at most $3$ and real dimension at most $6$. The bounds are attained by $\mathbb{C}_{\mathbb{B}}$ and by $\mathbb{V}_{\mathbb{B}}$.

*Proof.* A definite subspace meets a definite subspace of the opposite sign only at the origin, since a nonzero vector cannot have both a positive and a negative value. A positive definite subspace therefore injects into $\mathbb{B}/\mathbb{V}_{\mathbb{B}}$, of complex dimension $1$, and a negative definite one into $\mathbb{B}/\mathbb{C}_{\mathbb{B}}$, of complex dimension $3$. The centre and the vector subspace attain the bounds.

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

**Remark (the two cones).** The null set is not the cone of the algebraic norm $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$, of real dimension $6$; the two meet in the doubly null lines below. The comparison of the two geometries is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* and *The Krein Level Sets and the Hyperbolic Structure*.

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

## The Krein Cone

**Definition.** The **Krein cone** is
$$
P_K=\{\tilde Q\in\mathbb{B}:\langle\tilde Q,\tilde Q\rangle_{\natural*}\ge0\}
=\{\tilde Q:\lVert c\rVert_E\ge\lVert\vec v\rVert_E\}.
$$

**Theorem (the shape of the cone).** The Krein cone is closed, invariant under multiplication by positive real scalars, star-shaped with respect to the origin, and contractible. Its interior is the **positive region** $\{\lVert c\rVert_E>\lVert\vec v\rVert_E\}$ and its boundary is the null set $\mathcal K$. It is neither convex nor pointed: it is invariant under $\tilde Q\mapsto-\tilde Q$, so $P_K\cap(-P_K)=P_K$, which is larger than $\{0\}$.

*Proof.* Closedness is the closedness of the inequality, and homogeneity is $\langle\lambda\tilde Q,\lambda\tilde Q\rangle_{\natural*}=\lvert\lambda\rvert^2\langle\tilde Q,\tilde Q\rangle_{\natural*}$ for real $\lambda$. The straight-line homotopy $\tilde Q\mapsto t\tilde Q$ preserves the inequality, so the cone is star-shaped and contractible. The interior is the strict inequality and the boundary the equality. The failure of pointedness is the sign invariance, since the defining inequality is even; the failure of convexity is exhibited below. The level sets and the homotopy type of the interior are *The Krein Level Sets and the Hyperbolic Structure*.

**Example (the cone is not convex).** The elements $e_t+\vec e_y$ and $-e_t+\vec e_y$ both lie in $P_K$, with form value $1-1=0$; their midpoint $\vec e_y$ has form value $-1$, so it lies outside. The cone is therefore not convex, although it is star-shaped.

## The Intersection with the Hermitian Cone

**Setting.** The Hermitian subspace is $\mathbb{M}_+=\{\tilde Q:\tilde Q^{*}=\tilde Q\}$, with coordinates $Q_t=q_t$ real and $Q_k=iq'_k$ with $q'_k$ real. Its **Hermitian cone** is $P=\{q_t\ge\lVert\vec q'\rVert_E\}$, the cone of the positive semidefinite Hermitian elements (*Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*).

**Theorem (the intersection).** On $\mathbb{M}_+$ the Krein form is the interval form $q_t^2-\sum_k(q'_k)^2$, and
$$
P_K\cap\mathbb{M}_+=\{q_t^2\ge(q'_x)^2+(q'_y)^2+(q'_z)^2\},
$$
the full closed cone of the interval form, whose future nappe is the Hermitian cone $P$. In particular $P\subseteq P_K$.

*Proof.* On $\mathbb{M}_+$ the coefficients are $(q_t,iq'_x,iq'_y,iq'_z)$, so $\lvert Q_t\rvert^2=q_t^2$ and $\lvert Q_k\rvert^2=(q'_k)^2$; the form reads $q_t^2-\sum_k(q'_k)^2$, and the Krein inequality is the displayed cone. The identification of $P$ with the future nappe is the cited article.

## The Operator Cone

**Definition.** An operator $T\in\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is **$J$-positive** when it is $J$-self-adjoint and $\langle\tilde Q,T\tilde Q\rangle_{\natural*}\ge0$ for every $\tilde Q$. The **$J$-positive cone** is
$$
\mathcal P_J=\{T:T^{\dagger}=T,\ \langle\tilde Q,T\tilde Q\rangle_{\natural*}\ge0\ \forall\tilde Q\}.
$$

**Theorem (the cone as the image of the Hilbert cone).** With $J=\natural$ and $S$ ranging over the self-adjoint operators that are positive semidefinite for the definite companion,
$$
\boxed{\;\mathcal P_J=J\cdot\{S\ge0\}=\{JT:S\ge0\}\; }.
$$
The cone $\mathcal P_J$ is closed and convex, contains $J$, and does not contain the identity.

*Proof.* For any $T$, $\langle\tilde Q,T\tilde Q\rangle_{\natural*}=\langle\tilde Q,JT\tilde Q\rangle_*$, so the positivity and the $J$-self-adjointness of $T$ are exactly the self-adjointness and positivity of $JT$ for the definite form. Hence $T\in\mathcal P_J$ exactly when $JT=S\ge0$, that is $T=JS$; the map $S\mapsto JS$ is linear and bijective and carries the closed convex cone $\{S\ge0\}$ onto $\mathcal P_J$. The identity $T=J$ gives $JT=\mathrm{id}\ge0$, so $J\in\mathcal P_J$; $T=\mathrm{id}$ gives $JT=J$, which has the negative eigenvalue $-1$, so $\mathrm{id}\notin\mathcal P_J$.

**Remark (the two cones are different).** Neither of $\mathcal P_J$ and the Hilbert cone $\{S\ge0\}$ contains the other: $J$ lies in the first and not the second, the identity lies in the second and not the first. The cone $\mathcal P_J$ is the image of the Hilbert cone under the sign involution, not an enlargement of it.

**Remark (the group involution).** The involution $\theta_J(T)=(T^{\dagger})^{-1}$ of $\mathrm{GL}_4(\mathbb{C})$, with fixed group the $J$-unitary group $\mathrm{U}_J(\mathbb{B})\cong\mathrm{U}(1,3)$, the Cartan involution $\theta_0(T)=(T^{*})^{-1}$ and the Cartan decomposition are *The Krein Isometry Group and Its Cartan Decomposition*; $\theta_J$ is not a Cartan involution, since its fixed group is non-compact.

## Worked Examples

**An isotropic element that is not a zero divisor.** $\tilde Q=e_t+\vec e_x$: value $0$, norm $2$, square $2\vec e_x$. The line $\mathbb{C}\tilde Q$ is maximal totally isotropic.

**A zero divisor that is not isotropic.** $\tilde Q=\vec e_x+i\vec e_y$: value $-2$, norm $0$. The norm cone and the Krein null set are different.

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

## Summary

The Krein form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ is the general quaternionic sesquilinear form, non-degenerate of signature $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$, with negative index $3$ and $6$ and Pontryagin index $1$ and $2$. Its coefficient Gram matrix is $E=\operatorname{diag}(1,-1,-1,-1)$, of determinant $-1$; the realified form, with its matrix of signature $(2,6)$, is treated in *The Realification of the General Quaternionic Sesqualgebra*.

The fundamental symmetry is the natural conjugation $J={}^{\natural}$, with bridge $\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\langle\tilde Q_2,J\tilde Q_1\rangle_{*}$ and eigenspaces the centre and the vector subspace; it is the unique fundamental symmetry that is an algebra anti-automorphism. The other fundamental symmetries are the reflections in the positive definite lines $\mathbb{C}(e_t+\tilde V)$ with $\lVert\tilde V\rVert_E<1$, and they fix no algebra structure. The Krein-orthogonal complement need not be a complement: the isotropic line $\mathbb{C}(e_t+\vec e_x)$ lies in its own complement. The null set is the real cone $\lVert c\rVert_E=\lVert\vec v\rVert_E$, of dimension seven and smooth off the apex, with Witt index $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$, the maximal real isotropic subspace being the plane $\mathrm{span}_{\mathbb{R}}\{e_t+\vec e_x,i(e_t+\vec e_x)\}$; the doubly null lines are the Peirce lines $\mathbb{C}(e_t\pm i\vec u)$. The Krein cone $\lVert c\rVert_E\ge\lVert\vec v\rVert_E$ is closed, star-shaped and contractible, and it is neither convex nor pointed; its intersection with the Hermitian subspace is the full closed cone of the interval form, whose future nappe is the Hermitian cone $P$. On operators the $J$-positive cone is $J\cdot\{S\ge0\}$, closed and convex, containing $J$ and not the identity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | The Krein form |
| $\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^2$ | The Krein norm; the form at two equal arguments |
| $\langle\tilde Q_1,\tilde Q_2\rangle_*=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | The definite companion |
| $G=E=\operatorname{diag}(1,-1,-1,-1)$ | The Gram matrix in the coefficient basis; $\det G=-1$ |
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
| $(n,m)=(1,3)$ over $\mathbb{C}$, $(2,6)$ over $\mathbb{R}$ | The signature; $m$ the negative index, $\min(n,m)$ the Pontryagin index |

## Further Reading

- [The Fundamental Symmetry](the-fundamental-symmetry.html), for the general theory and the angular operator.
- [Krein Spaces](krein-spaces.html) and [Pontryagin Spaces](pontryagin-spaces.html), for the general theory of the fundamental symmetry and the two indices.
- [Indefinite Inner Product Spaces](indefinite-inner-product-spaces.html), for the fundamental decomposition and the classification of subspaces.
- [The Group of Involutions](the-group-of-involutions.html) and [Comparison of the Remarkable Subspaces](comparison-of-the-remarkable-subspaces.html), for the four involutions and their fixed spaces.
- [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the restrictions, their signatures, their null cones and the four real forms.
- [Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint](positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.html), for the cone of squares and its identification with the future nappe.
- [The Krein Level Sets and the Hyperbolic Structure](the-krein-level-sets-and-the-hyperbolic-structure.html), for the level sets, the ball and the sphere of isotropic lines.
- [J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra](j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra.html), for the operator theory of the form.
- [The Krein Isometry Group and Its Cartan Decomposition](the-krein-isometry-group-and-its-cartan-decomposition.html), for the isometry group, the Cartan involution and the symmetric-space decomposition.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the comparison of the Krein form with the other three pairings.
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the fundamental decomposition and the classification of subspaces.
- Thomas Ya. Azizov and Iosif S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the Krein space, the Witt index and the operator cone.
