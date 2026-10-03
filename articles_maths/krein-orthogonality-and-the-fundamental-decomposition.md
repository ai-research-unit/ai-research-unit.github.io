# __Krein Orthogonality and the Fundamental Decomposition__

## Introduction

The Krein form $[\tilde{Q},\tilde{Q}']=\sum_{\mu}\varepsilon_{\mu}\bar Q_{\mu}Q'_{\mu}$ is an indefinite Hermitian form, and its **orthogonality** is not the orthogonality of a Euclidean space: isotropic vectors exist, a subspace and its complement can meet, and a projection can be Krein-orthogonal without being definite-orthogonal. This article develops the three notions that organise the indefinite geometry of the algebra — the Krein-orthogonal complement, the classification of subspaces by the inertia of the restricted form, and the **fundamental decomposition** $\mathbb{B}=\mathbb{W}\,{[+]_K}\,\mathbb{W}^{\perp_{K}}$ attached to a maximal positive definite subspace $\mathbb{W}$ — together with the projections that belong to them. The Gram matrix of the form and the signatures of its restrictions are in *The Krein Gram Matrix and the Restrictions of the Form*; the totally isotropic subspaces are the subject of *The Isotropic Structure of the Krein Form*; and the global geometry of the maximal definite subspaces is in *The Krein Level Sets and the Hyperbolic Structure*.

**Conventions.** $e_0=1$, $e_k^{2}=-e_0$, central scalar imaginary $i$, $\mathrm{Sc}$ the scalar part, $\langle\tilde{Q},\tilde{Q}'\rangle=\sum_{\mu}\bar Q_{\mu}Q'_{\mu}$ the positive definite Hermitian form, $[\cdot,\cdot]$ the Krein form, and $J={}^{\natural}$ the fundamental symmetry, so that $[\tilde{Q},\tilde{Q}']=\langle J\tilde{Q},\tilde{Q}'\rangle$ and $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathbb{V}_{\mathbb{B}}$ is the splitting into the centre and the vector subspace.

## Orthogonality and Complements

**Definition.** Elements $\tilde{Q},\tilde{Q}'$ are **Krein-orthogonal**, written $\tilde{Q}\perp_{K}\tilde{Q}'$, when $[\tilde{Q},\tilde{Q}']=0$. A subspace is **Krein-orthogonal** to another, $\mathbb{W}\perp_{K}\mathbb{Z}$, when every element of one is Krein-orthogonal to every element of the other. The **Krein-orthogonal complement** of $\mathbb{W}$ is

$$
\mathbb{W}^{\perp_{K}}=\{\tilde{Z}\in\mathbb{B}:[\tilde{Q},\tilde{Z}]=0\ \text{for all}\ \tilde{Q}\in\mathbb{W}\}.
$$

**Theorem (the complement).** For every subspace $\mathbb{W}$,

$$
\dim\mathbb{W}+\dim\mathbb{W}^{\perp_{K}}=\dim\mathbb{B},
\qquad
\mathbb{W}\subseteq(\mathbb{W}^{\perp_{K}})^{\perp_{K}},
\qquad
(\mathbb{W}^{\perp_{K}})^{\perp_{K}}=\mathbb{W}\ \text{if and only if}\ \mathbb{W}\cap\mathbb{W}^{\perp_{K}}=\{0\}.
$$

In particular $\mathbb{C}_{\mathbb{B}}^{\perp_{K}}=\mathbb{V}_{\mathbb{B}}$ and $\mathbb{V}_{\mathbb{B}}^{\perp_{K}}=\mathbb{C}_{\mathbb{B}}$.

**Proof.** The map $\mathbb{B}\to\mathbb{W}^{*}$, $\tilde{Z}\mapsto[\cdot,\tilde{Z}]$, has kernel $\mathbb{W}^{\perp_{K}}$ and rank $\dim\mathbb{W}$, because the ambient form is non-degenerate and every linear form on $\mathbb{W}$ extends; rank–nullity gives the dimension formula. The inclusion and the criterion for equality are formal consequences. The last line is the computation $[e_0,e_k]=0$ with the dimensions.

**Remark (the contrast with a Euclidean space).** In a positive definite space $\mathbb{W}\cap\mathbb{W}^{\perp}=\{0\}$ for every $\mathbb{W}$; here the intersection can be non-trivial, and it is exactly the radical of the restricted form.

## The Classification of Subspaces

**Definition.** Write $[\,\cdot,\cdot\,]_{\mathbb{W}}$ for the restriction of the Krein form to a subspace $\mathbb{W}$. The subspace is **non-degenerate** when the restriction is non-degenerate, equivalently when $\mathbb{W}\cap\mathbb{W}^{\perp_{K}}=\{0\}$; **degenerate** otherwise; **positive definite**, **negative definite**, or **definite** when the restriction is; **neutral** when it is non-degenerate and the restriction is indefinite; and **totally isotropic** when the restriction vanishes, $[\tilde{Q},\tilde{Q}']=0$ for all $\tilde{Q},\tilde{Q}'\in\mathbb{W}$.

**Theorem (definite implies non-degenerate; the converse fails).** A definite subspace is non-degenerate. The converse is false: the real plane $\mathbb{W}=\mathrm{span}_{\mathbb{R}}\{e_0+e_1,\ e_0-e_1\}$ is non-degenerate and neutral, since $[e_0+e_1,e_0+e_1]=[e_0-e_1,e_0-e_1]=0$ while $[e_0+e_1,e_0-e_1]=2$.

**Proof.** If $\mathbb{W}$ is positive definite and $\tilde{Z}\in\mathbb{W}\cap\mathbb{W}^{\perp_{K}}$ then $[\tilde{Z},\tilde{Z}]>0$ unless $\tilde{Z}=0$, while $\tilde{Z}\in\mathbb{W}^{\perp_{K}}$ gives $[\tilde{Z},\tilde{Z}]=0$; the negative definite case is the same with the sign reversed. For the plane, the two displayed values give a restriction of Gram matrix $\begin{pmatrix}0&2\\2&0\end{pmatrix}$, of determinant $-4\neq0$ and of inertia $(1,1)$.

**Theorem (the dimension of a definite subspace).** A positive definite subspace has complex dimension at most $1$ (real dimension at most $2$), and a negative definite subspace has complex dimension at most $3$ (real dimension at most $6$); the bounds are the inertia indices $p$ and $q$ of *The Krein Gram Matrix and the Restrictions of the Form*.

**Proof.** A positive definite subspace meets the maximal negative definite subspace $\mathbb{V}_{\mathbb{B}}$ only at $0$, so its dimension is at most the codimension of $\mathbb{V}_{\mathbb{B}}$, which is $1$; the negative statement is the same with the centre.

## Maximal Definite Subspaces

**Definition.** A positive definite subspace is **maximal** when it is contained in no larger one; equivalently, when its dimension is the positive index $p$.

**Theorem (the maximal positive definite subspaces).** Over $\mathbb{C}$ the maximal positive definite subspaces are the lines $\mathbb{C}(e_0+\tilde{V})$ with $\tilde{V}\in\mathbb{V}_{\mathbb{B}}$ and $\|\tilde{V}\|_E<1$, and over $\mathbb{R}$ they are the real planes of the same form. The map $\tilde{V}\mapsto\mathbb{C}(e_0+\tilde{V})$ is a bijection onto the set of maximal positive definite subspaces, so that set is the open unit ball of $\mathbb{V}_{\mathbb{B}}\cong\mathbb{C}^{3}$.

**Proof.** $[e_0+\tilde{V},e_0+\tilde{V}]=1-\|\tilde{V}\|_E^{2}$ by the bridge $[\tilde{Q},\tilde{Q}]=\sum_{\mu}\varepsilon_{\mu}|Q_{\mu}|^{2}$, so the line is positive definite exactly for $\|\tilde{V}\|_E<1$ and is maximal by the dimension bound; conversely a maximal positive definite line has a vector with $\tilde{Q}_0\neq0$, since it meets $\mathbb{V}_{\mathbb{B}}$ only at $0$, and can be scaled to the form $e_0+\tilde{V}$. The classification of the fundamental symmetries in *The Fundamental Symmetry of the Biquaternion Algebra* is the same parametrisation read on the operators.

## The Fundamental Decomposition

**Definition.** A **fundamental decomposition** of $\mathbb{B}$ is a pair $(\mathbb{W},\mathbb{W}^{\perp_{K}})$ of complementary Krein-orthogonal subspaces, the first positive definite and maximal. Its **fundamental symmetry** is the operator

$$
J_{\mathbb{W}}=
\begin{cases}
+\mathrm{id} & \text{on }\mathbb{W},\\
-\mathrm{id} & \text{on }\mathbb{W}^{\perp_{K}} .
\end{cases}
$$

**Theorem (the fundamental symmetry of a decomposition).** For every fundamental decomposition $(\mathbb{W},\mathbb{W}^{\perp_{K}})$ the operator $J_{\mathbb{W}}$ is a $J$-self-adjoint involution with $J_{\mathbb{W}}^{2}=\mathrm{id}$, its signature is $(2,6)$ over $\mathbb{R}$, and it reproduces the Krein form from the Hermitian one,

$$
[\tilde{Q},\tilde{Q}']=\langle J_{\mathbb{W}}\tilde{Q},\tilde{Q}'\rangle,
\qquad
[J_{\mathbb{W}}\tilde{Q},\tilde{Q}]=\langle\tilde{Q},\tilde{Q}\rangle .
$$

The canonical fundamental decomposition is $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp_{K}\mathbb{V}_{\mathbb{B}}$, with $J_{\mathbb{C}_{\mathbb{B}}}=J={}^{\natural}$.

**Proof.** The operator is well defined because $\mathbb{B}=\mathbb{W}\oplus\mathbb{W}^{\perp_{K}}$, and it is an involution by construction. For the first identity, split $\tilde{Q}=\tilde{W}+\tilde{Z}$ and $\tilde{Q}'=\tilde{W}'+\tilde{Z}'$: $[\tilde{Q},\tilde{Q}']=[\tilde{W},\tilde{W}']+[\tilde{Z},\tilde{Z}']$ and $\langle J_{\mathbb{W}}\tilde{Q},\tilde{Q}'\rangle=\langle\tilde{W},\tilde{W}'\rangle-\langle\tilde{Z},\tilde{Z}'\rangle$; on the positive definite $\mathbb{W}$ the two forms agree and on the negative definite $\mathbb{W}^{\perp_{K}}$ they agree up to the sign $-$ because $[\tilde{Z},\tilde{Z}']=-\langle\tilde{Z},\tilde{Z}'\rangle$ there. The second identity is the first with $J_{\mathbb{W}}^{2}=\mathrm{id}$ and $\langle J_{\mathbb{W}}\tilde{Q},\tilde{Q}'\rangle=[\tilde{Q},\tilde{Q}']$. The signature is that of the form, and the canonical pair is the sign comparison of the two conjugations.

**Corollary (the family of symmetries).** The fundamental symmetries of $\mathbb{B}$ are the involutions whose $+1$-eigenspace is positive definite of dimension $p$; through the parametrisation of the maximal positive definite subspaces they are indexed by the open unit ball of $\mathbb{V}_{\mathbb{B}}$, the canonical one $-1$ of them being $J$ itself. Any two fundamental symmetries are congruent by an isometry of the Krein form.

## The Krein Projections

**Definition.** Let $\mathbb{W}$ be non-degenerate. The **Krein-orthogonal projection** onto $\mathbb{W}$ is the projection with range $\mathbb{W}$ and kernel $\mathbb{W}^{\perp_{K}}$.

**Theorem (the Krein projections are exactly the $J$-self-adjoint idempotents).** An idempotent $P$ of $\mathbb{B}$ is $J$-self-adjoint, $P^{\dagger}=P$, if and only if it is the Krein-orthogonal projection onto a non-degenerate subspace.

**Proof.** If $P^{\dagger}=P$ and $P^{2}=P$, then $[P\tilde{X},\tilde{Y}]=[\tilde{X},P\tilde{Y}]$; for $\tilde{X}\in\ker P$ this gives $[\tilde{X},\tilde{Y}']=0$ for every $\tilde{Y}'$ in the range, so $\ker P\subseteq(\mathrm{ran}\,P)^{\perp_{K}}$, and the two sides have the same dimension because the form is non-degenerate, whence equality. Conversely, for the projection onto a non-degenerate $\mathbb{W}$ along $\mathbb{W}^{\perp_{K}}$, writing $\tilde{X}=\tilde{W}+\tilde{Z}$ and $\tilde{Y}=\tilde{W}'+\tilde{Z}'$ gives $[P\tilde{X},\tilde{Y}]=[\tilde{W},\tilde{W}']=[\tilde{X},P\tilde{Y}]$, so $P^{\dagger}=P$.

**Theorem (Krein-orthogonality is not definite-orthogonality).** The definite-orthogonal projections that commute with $J$ are the Krein-orthogonal projections with $J$-invariant range, and they are a proper subclass: for $\mathbb{W}=\mathbb{C}(e_0+\tfrac12e_1)$, the Krein-orthogonal projection onto $\mathbb{W}$ is $J$-self-adjoint, is not self-adjoint for $\langle\cdot,\cdot\rangle$, and does not commute with $J$.

**Proof.** If $P^{*}=P$ and $PJ=JP$ then $P^{\dagger}=JP^{*}J=JPJ=P$, so such projections are Krein-orthogonal; their range is $J$-invariant. For the counterexample, in the coefficient basis the projection onto $\mathbb{C}(e_0+\tfrac12e_1)$ along its complement is the matrix with rows $(4/3,-2/3,0,0)$ and $(2/3,-1/3,0,0)$; it is idempotent, it satisfies $P^{\dagger}=P$ because conjugation by $J$ changes the signs of exactly the off-diagonal entries, and $P^{*}=P^{\mathsf T}\neq P$ shows that it is not definite-orthogonal, while $PJ\neq JP$ shows that it does not commute with $J$.

## The Krein Gram–Schmidt Process

**Theorem (orthonormalisation).** Every basis of $\mathbb{B}$ can be replaced by an orthonormal one, carrying $p$ vectors with $[u,u]=+1$ and $q$ with $[u,u]=-1$; the numbers $p,q$ do not depend on the basis.

**Proof.** Sylvester's law of inertia (*Quadratic Forms and Polarisation*, §*Sylvester's Law of Inertia*) applied to the Hermitian form. Explicitly, if a vector $u$ with $[u,u]\neq0$ is found, replace the current basis by its Krein-orthogonal projection on $u^{\perp_{K}}$ together with $u$, and rescale $u$ so that $[u,u]=\pm1$; if the residual form is nonzero, repeat. The process stops because each step lowers the dimension by one, and at the end the remaining vectors, if any, are isotropic and span a totally isotropic subspace (*The Isotropic Structure of the Krein Form*).

**Worked example.** The basis $e_0,e_1,e_2,e_3$ is already orthonormal, with $p=1$ and $q=3$ over $\mathbb{C}$. Starting instead from $u_0=e_0+e_1$ and $u_1=e_0-e_1$: $[u_0,u_0]=0$ shows that $u_0$ is isotropic and the process cannot start with it; the pair spans a neutral non-degenerate plane and must be replaced by the orthonormal pair $e_0,e_1$.

## Worked Examples

**A degenerate subspace.** $\mathbb{W}=\mathbb{C}(e_0+e_1)$: $[e_0+e_1,e_0+e_1]=0$, so $\mathbb{W}\subseteq\mathbb{W}^{\perp_{K}}$ and the restriction vanishes; $\dim\mathbb{W}+\dim\mathbb{W}^{\perp_{K}}=1+3=4$ reads the complement.

**A positive definite subspace.** $\mathbb{W}=\mathbb{C}(e_0+0.5e_1)$: $[\tilde{Q},\tilde{Q}]=1-0.25=0.75>0$, non-degenerate, maximal, with fundamental symmetry different from $J$.

**A neutral non-degenerate subspace.** $\mathrm{span}_{\mathbb{R}}\{e_0+e_1,\,e_0-e_1\}$, of Gram matrix $\begin{pmatrix}0&2\\2&0\end{pmatrix}$.

**A definite subspace of each sign.** The centre $\mathbb{C}_{\mathbb{B}}$, positive, and the vector subspace $\mathbb{V}_{\mathbb{B}}$, negative.

**Two orthogonal distinctions.** $\mathbb{C}_{\mathbb{B}}\perp_{K}\mathbb{V}_{\mathbb{B}}$, while $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ are not Krein-orthogonal, $[e_0,ie_0]=i\neq0$.

## Summary

The Krein-orthogonal complement satisfies $\dim\mathbb{W}+\dim\mathbb{W}^{\perp_{K}}=\dim\mathbb{B}=4$ over $\mathbb{C}$, and $\mathbb{W}\cap\mathbb{W}^{\perp_{K}}=\{0\}$ characterises the non-degenerate subspaces, which are exactly those whose restricted form is non-degenerate. Definite subspaces are non-degenerate, the converse failing on the neutral plane $\mathrm{span}_{\mathbb{R}}\{e_0+e_1,e_0-e_1\}$; a positive definite subspace has complex dimension at most $1$, a negative definite one at most $3$, and the maximal positive definite subspaces are the lines $\mathbb{C}(e_0+\tilde{V})$ with $\|\tilde{V}\|_E<1$, so they form the open unit ball of $\mathbb{C}^{3}$. Each of them gives a fundamental decomposition $\mathbb{B}=\mathbb{W}\perp_{K}\mathbb{W}^{\perp_{K}}$ and a fundamental symmetry $J_{\mathbb{W}}=\pm\mathrm{id}$ on the two parts, reproducing the Krein form from the Hermitian one, $[\tilde{Q},\tilde{Q}']=\langle J_{\mathbb{W}}\tilde{Q},\tilde{Q}'\rangle$; the canonical symmetry is $J={}^{\natural}$. The $J$-self-adjoint idempotents are exactly the Krein-orthogonal projections onto the non-degenerate subspaces, a class strictly larger than the definite-orthogonal projections commuting with $J$; the projection onto $\mathbb{C}(e_0+\tfrac12e_1)$ is the smallest counterexample. Orthonormal bases exist, with $p=1$ signs $+1$ and $q=3$ signs $-1$ over $\mathbb{C}$, and the Krein Gram–Schmidt process produces one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{Q}\perp_{K}\tilde{Q}'$ | $[\tilde{Q},\tilde{Q}']=0$ |
| $\mathbb{W}^{\perp_{K}}$ | The Krein-orthogonal complement of $\mathbb{W}$ |
| $\mathbb{W}\cap\mathbb{W}^{\perp_{K}}=\{0\}$ | Non-degeneracy of $\mathbb{W}$ |
| Definite, neutral, degenerate, totally isotropic | The classification of subspaces by the restricted form |
| $\mathbb{C}(e_0+\tilde{V})$, $\lVert\tilde{V}\rVert_E<1$ | The maximal positive definite subspaces |
| $J_{\mathbb{W}}=\pm\mathrm{id}$ | The fundamental symmetry of a fundamental decomposition |
| $[\tilde{Q},\tilde{Q}']=\langle J_{\mathbb{W}}\tilde{Q},\tilde{Q}'\rangle$ | The bridge through a fundamental symmetry |
| $P^{\dagger}=P$, $P^{2}=P$ $\iff$ $P$ Krein-orthogonal projection | The $J$-self-adjoint idempotents |

## Further Reading

- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the Gram matrices and the inertia
- *The Isotropic Structure of the Krein Form* (`articles_maths/the-isotropic-structure-of-the-krein-form.md`), for the totally isotropic subspaces
- *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for the family of fundamental symmetries
- *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra* (`articles_maths/indefinite-positivity-and-the-krein-cone-of-the-biquaternion-algebra.md`), for the $J$-self-adjoint idempotents inside the cone
- *The Krein Level Sets and the Hyperbolic Structure* (`articles_maths/the-krein-level-sets-and-the-hyperbolic-structure.md`), for the global geometry of the maximal definite subspaces
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for orthogonality, the classification of subspaces and the fundamental decompositions of a Krein space
