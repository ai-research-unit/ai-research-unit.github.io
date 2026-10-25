# __The Krein Norm of the Biquaternion Algebra__

## Introduction

The general quaternionic sesquilinear form of the biquaternion algebra is
$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}
=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2}),
\qquad \varepsilon=(1,-1,-1,-1).
$$
It is Hermitian, linear in the first slot and conjugate-linear in the second, and it is non-degenerate. Read at two equal arguments it is the **Krein norm**
$$
\langle\tilde Q\rangle_{\natural*}=\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2,
$$
the real and indefinite companion of the quaternionic norm $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$. It is not multiplicative: the element $e_t+\vec e_x$ is null, while its square $2\vec e_x$ has value $-4$.

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of complex dimension four and real dimension eight. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ and the vector subspace is $\mathbb{V}_{\mathbb{B}}=\mathrm{span}_{\mathbb{C}}\{\vec e_x,\vec e_y,\vec e_z\}$. The Euclidean norm is $\lVert\tilde Q\rVert_E^2=\sum_\mu\lvert Q_\mu\rvert^2$, the real vector parts carry the bilinear dot product $(\vec S,\vec W)=\sum_kS_kW_k$, and the **definite companion** is $\langle\tilde Q_1,\tilde Q_2\rangle_*=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$.

In the coefficient basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the Gram matrix is
$$
G=E=\operatorname{diag}(1,-1,-1,-1),\qquad \det G=-1,
$$
so the inertia is $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$, with negative index $3$ and $6$ and Pontryagin index $1$ and $2$; with the Krein form the algebra is the Pontryagin space $\Pi_6$. The realified matrix is $\operatorname{diag}(\varepsilon,\varepsilon)$ (*The Realification of the General Quaternionic Sesqualgebra*), and the comparison with the other three forms, including the reading of the same sign matrix on the general plain bilinear form, is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

The article reads the form as the form of the algebra: the natural conjugation as its canonical symmetry, the isotropic and the doubly null lines, and the $J$-positive cone of operators. The norm itself, its sign regions, its null set and the cone it closes are *Krein Norm Regularity and Degeneracy in the Biquaternion Algebra*. The general theory of indefinite forms, fundamental decompositions, orthogonality and the classification of subspaces is *Indefinite Inner Product Spaces* and *The Fundamental Symmetry of the Form*; the restrictions are *Remarkable Subspaces under the General Quaternionic Sesqualgebra*; the level sets and their topology are *The Krein Level Sets and the Hyperbolic Structure*; the operator theory is *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*; and the isometry group is *The Krein Isometry Group and Its Cartan Decomposition*.

## The Natural Conjugation as a Fundamental Symmetry

The natural conjugation $J={}^{\natural}$ multiplies the vector part by $-1$, so $J=\operatorname{diag}(1,-1,-1,-1)$ in the coefficient basis. It is a **fundamental symmetry** of the Krein form:
$$
J^2=\mathrm{id},\qquad
\langle\tilde Q_2,J\tilde Q_1\rangle_{\natural*}=\langle J\tilde Q_2,\tilde Q_1\rangle_{\natural*},\qquad
\langle\tilde Q_1,J\tilde Q_1\rangle_{\natural*}=\lVert\tilde Q_1\rVert_E^2>0\quad(\tilde Q_1\neq0).
$$
The definite form it induces is the companion, and the bridge between the indefinite and the definite form is
$$
\boxed{\;\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\langle\tilde Q_2,J\tilde Q_1\rangle_{*}=\langle\tilde Q_2,\tilde Q_1^{\natural}\rangle_{*}\;}
$$
The eigenspaces of $J$ are the centre and the vector subspace, of complex dimensions $1$ and $3$. They are definite of the two signs and Krein-orthogonal, so the centre–vector splitting
$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathbb{V}_{\mathbb{B}}
$$
is a fundamental decomposition. The verification is the sign computation $\varepsilon_\mu^2=1$; the general definitions are *The Fundamental Symmetry of the Form*.

**Theorem (the algebraic member is unique).** The natural conjugation is the unique fundamental symmetry of the Krein form that is a unital $\mathbb{C}$-algebra anti-automorphism.

*Proof.* Let $J$ be such a symmetry. For every $\tilde Q$, $J(\tilde Qe_t)=J(e_t)J(\tilde Q)$ and $J(e_t\tilde Q)=J(\tilde Q)J(e_t)$; since $J$ is bijective, $J(e_t)$ is a two-sided unit, hence $J(e_t)=e_t$. The $+1$-eigenspace of $J$ is the positive part of a fundamental decomposition, of complex dimension one, and it contains $e_t$; it is therefore $\mathbb{C}_{\mathbb{B}}$. Then $J$ is $+\mathrm{id}$ on the centre and $-\mathrm{id}$ on $\mathbb{V}_{\mathbb{B}}$, which is ${}^{\natural}$. Conversely ${}^{\natural}$ is such a symmetry.

**Remark (the other symmetries).** Every fundamental symmetry is the reflection $J_{\mathbb{W}}=2P_{\mathbb{W}}-\mathrm{id}$ in a positive definite line $\mathbb{W}=\mathbb{C}(e_t+\tilde V)$ with $\lVert\tilde V\rVert_E<1$, and $J$ is the member $\tilde V=0$. The general parametrisation is *The Fundamental Symmetry of the Form*, §*Non-Uniqueness and the Angular Operator*; the lines are classified in the next section.

## The Positive Lines

**Theorem (the positive lines).** A positive definite complex subspace has complex dimension at most one, and a positive definite real subspace has real dimension at most two. The positive definite complex lines are exactly
$$
\ell_{\tilde V}=\mathbb{C}(e_t+\tilde V),\qquad \tilde V\in\mathbb{V}_{\mathbb{B}},\quad \lVert\tilde V\rVert_E<1.
$$
Over $\mathbb{R}$ the realification of $\ell_{\tilde V}$ is the positive definite plane $\mathrm{span}_{\mathbb{R}}\{e_t+\tilde V,i(e_t+\tilde V)\}$. The assignment $\tilde V\mapsto\ell_{\tilde V}$ is a bijection onto the positive lines, so the positive lines form the open unit ball of $\mathbb{V}_{\mathbb{B}}$; its complex hyperbolic structure is *The Krein Level Sets and the Hyperbolic Structure*.

*Proof.* A positive definite subspace meets $\mathbb{V}_{\mathbb{B}}$ only at the origin, because the form is negative definite there; it therefore injects into $\mathbb{B}/\mathbb{V}_{\mathbb{B}}\cong\mathbb{C}_{\mathbb{B}}$, of real dimension two, so a complex positive definite subspace has complex dimension at most one and a real one has real dimension at most two. A positive complex line is not contained in $\mathbb{V}_{\mathbb{B}}$, so after scaling it is $\mathbb{C}(e_t+\tilde V)$, and
$$
\langle e_t+\tilde V,e_t+\tilde V\rangle_{\natural*}=1-\lVert\tilde V\rVert_E^2
$$
is positive exactly for $\lVert\tilde V\rVert_E<1$. The real plane is the realification of the complex line.

**Remark (real planes that are not complex).** Over $\mathbb{R}$ the positive index is two, and the realifications displayed are not the only positive definite planes: the graph of a real-linear contraction $\mathbb{C}_{\mathbb{B}}\to\mathbb{V}_{\mathbb{B}}$ is another. The complex classification is the one used by the operator theory, where all maps are $\mathbb{C}$-linear.

## Krein Orthogonality and the Complement

**Definition.** Two elements are **Krein-orthogonal**, written $\tilde Q_1\perp_K\tilde Q_2$, when $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=0$; two subspaces are Krein-orthogonal when every element of one is orthogonal to every element of the other. The **Krein-orthogonal complement** of $\mathbb{W}$ is
$$
\mathbb{W}^{\perp_K}=\{\tilde Q:\langle\tilde Q,\tilde W\rangle_{\natural*}=0\ \text{for every}\ \tilde W\in\mathbb{W}\}.
$$

**Example (a self-orthogonal line).** The line $\mathbb{W}=\mathbb{C}(e_t+\vec e_x)$ is isotropic, $\langle e_t+\vec e_x\rangle_{\natural*}=0$, so $\mathbb{W}\subseteq\mathbb{W}^{\perp_K}$ and $\mathbb{W}+\mathbb{W}^{\perp_K}=\mathbb{W}^{\perp_K}$ has dimension three. The sum is not the algebra, so no direct sum decomposition is obtained from $\mathbb{W}$ alone.

**Criterion.** For $\tilde Q\neq0$ the line $\mathbb{C}\tilde Q$ is non-degenerate exactly when $\langle\tilde Q\rangle_{\natural*}\neq0$. In that case
$$
\mathbb{B}=\mathbb{C}\tilde Q\oplus(\mathbb{C}\tilde Q)^{\perp_K},
\qquad
\dim_{\mathbb{C}}(\mathbb{C}\tilde Q)^{\perp_K}=3,
$$
and the restriction of the form to the line is positive definite when the value is positive and negative definite when it is negative. When the value vanishes the line is isotropic and lies in its own complement.

*Proof.* The Gram matrix of the restriction to the line is the single entry $\langle\tilde Q\rangle_{\natural*}$, so the line is non-degenerate exactly when that entry is non-zero, and its sign is the sign of the entry. For a non-degenerate line the orthogonal complement is non-degenerate and the sum is direct, of dimensions $1$ and $4-1=3$. For a vanishing entry every vector of the line is orthogonal to the line.

## The Totally Isotropic Subspaces and the Witt Index

An element is **isotropic** when $\langle\tilde Q\rangle_{\natural*}=0$; the null set and its two strata are *Krein Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Degenerate Case: The Null Set*.

**Definition.** A subspace $\mathbb{W}$ is **totally isotropic** when $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=0$ for all $\tilde Q_1,\tilde Q_2\in\mathbb{W}$, equivalently when $\mathbb{W}\subseteq\mathbb{W}^{\perp_K}$; it is **maximal** when it is contained in no larger one. The **Witt index** is the common dimension of the maximal totally isotropic subspaces.

**Theorem (the Witt index).** The Witt index is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$. A maximal totally isotropic complex subspace is $\mathbb{C}(e_t+\vec e_x)$, and a maximal totally isotropic real subspace is the plane
$$
\mathbb{W}_{\mathrm{iso}}=\mathrm{span}_{\mathbb{R}}\{e_t+\vec e_x,\ i(e_t+\vec e_x)\}.
$$
Every totally isotropic subspace is contained in a maximal one, and $\mathrm{U}(1,3)$ acts transitively on the maximal ones.

*Proof.* A totally isotropic subspace meets $\mathbb{V}_{\mathbb{B}}$ only at the origin, since a non-zero element of $\mathbb{V}_{\mathbb{B}}$ has negative value; it injects into $\mathbb{B}/\mathbb{V}_{\mathbb{B}}$, of real dimension $2$ and complex dimension $1$. Hence its real dimension is at most $2$ and its complex dimension at most $1$. The displayed line and plane are totally isotropic,
$$
\langle e_t+\vec e_x,e_t+\vec e_x\rangle_{\natural*}=0,\qquad
\langle e_t+\vec e_x,i(e_t+\vec e_x)\rangle_{\natural*}=0,\qquad
\langle i(e_t+\vec e_x),i(e_t+\vec e_x)\rangle_{\natural*}=0,
$$
and they attain the bounds. Witt's extension theorem gives the extension property and the transitivity.

**Remark (the real planes).** Every real totally isotropic plane is the realification of a complex isotropic line. A real plane that is not complex would complexify to a complex totally isotropic plane of dimension two, beyond the Witt index one. The maximal real plane $\mathbb{W}_{\mathrm{iso}}$ is not a Peirce line: it is a real plane and not a complex line, and it contains $e_t+\vec e_x$, of algebraic norm $2$.

## The Doubly Null Lines and the Peirce Lines

**Definition.** A **doubly null line** is an isotropic line that lies in the cone of the algebraic norm as well: a complex line $\mathbb{C}\tilde Q$ with $\langle\tilde Q\rangle_{\natural*}=0$ and $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2=0$.

**Theorem (the doubly null lines are the Peirce lines).** The doubly null lines are exactly the lines $\mathbb{C}(e_t+i\vec u)$ with $\vec u\in S^2$ a real unit vector. They are the **Peirce lines**, spanned by the rank-one Hermitian idempotents
$$
\tilde\Pi_\pm(\tilde\Xi)=\tfrac12\bigl(e_t\pm\tilde\Xi\bigr),\qquad \tilde\Xi=i\vec u .
$$
The idempotents, their Peirce decompositions and their minimal ideals are *Ideals and Peirce Decomposition of the General Plain Sesqualgebra*.

*Proof.* For $\tilde\Xi=i\vec u$ with $\vec u$ a real unit vector, $\tilde\Xi^2=i^2\vec u^2=e_t$ and $\tilde\Xi^{*}=\tilde\Xi$; hence $(e_t\pm\tilde\Xi)^2=2(e_t\pm\tilde\Xi)$ and the displayed elements are Hermitian idempotents, of trace one in the $2\times2$ matrix model and therefore of rank one. The two values are
$$
\langle e_t\pm\tilde\Xi\rangle_{\natural}=1+\langle\tilde\Xi\rangle_{\natural}=1-\lVert\vec u\rVert_E^2=0,
\qquad
\langle e_t\pm\tilde\Xi\rangle_{\natural*}=1-\lVert\tilde\Xi\rVert_E^2=0,
$$
so each line $\mathbb{C}(e_t\pm i\vec u)$ is doubly null. For the converse, write $\tilde Q=c(e_t+\tilde Q_3)$ with $\lVert\tilde Q_3\rVert_E=1$, which is possible on any isotropic line with $c\neq0$; the vanishing of the algebraic norm reads $1+\langle\tilde Q_3\rangle_{\natural}=0$. With $\tilde Q_3=\tilde S+i\tilde W$ and $\tilde S,\tilde W\in\mathbb{V}_{\mathbb{B}}$ real, this is the system
$$
\lVert\tilde S\rVert_E^2+\lVert\tilde W\rVert_E^2=1,\qquad
\lVert\tilde S\rVert_E^2-\lVert\tilde W\rVert_E^2=-1,\qquad
(\tilde S,\tilde W)=0,
$$
which forces $\tilde S=0$ and $\lVert\tilde W\rVert_E=1$. Hence $\tilde Q_3=i\tilde W$ with $\tilde W$ a real unit vector.

## The Operator Cone

**Definition.** An operator $T\in\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is **$J$-positive** when it is $J$-self-adjoint and $\langle\tilde Q,T\tilde Q\rangle_{\natural*}\ge0$ for every $\tilde Q$. The **$J$-positive cone** is
$$
\mathcal P_J=\{T:T^{\dagger}=T,\ \langle\tilde Q,T\tilde Q\rangle_{\natural*}\ge0\ \forall\tilde Q\}.
$$

**Theorem (the cone as the image of the Hilbert cone).** With $J=\natural$ and $S$ ranging over the operators that are self-adjoint and positive semidefinite for the definite companion,
$$
\boxed{\;\mathcal P_J=J\cdot\{S\ge0\}=\{JS:S\ge0\}\;}.
$$
The cone $\mathcal P_J$ is closed and convex, contains $J$, and does not contain the identity.

*Proof.* For any $T$, $\langle\tilde Q,T\tilde Q\rangle_{\natural*}=\langle\tilde Q,JT\tilde Q\rangle_*$, so the positivity and the $J$-self-adjointness of $T$ are exactly the self-adjointness and positivity of $JT$ for the definite form. Hence $T\in\mathcal P_J$ exactly when $JT=S\ge0$, that is $T=JS$; the map $S\mapsto JS$ is linear and bijective and carries the closed convex cone $\{S\ge0\}$ onto $\mathcal P_J$. The identity $T=J$ gives $JT=\mathrm{id}\ge0$, so $J\in\mathcal P_J$; $T=\mathrm{id}$ gives $JT=J$, which has the negative eigenvalue $-1$, so $\mathrm{id}\notin\mathcal P_J$.

The cone sits in the Jordan algebra $\mathfrak{p}=J\cdot\operatorname{Herm}_4$ and governs the $J$-contractions; both are *The Krein Isometry Group and Its Cartan Decomposition*. The indefinite adjoint is $T^{\dagger}=JT^{*}J$ and the indefinite spectral theory is *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*.

## Summary

The Krein form is the general quaternionic sesquilinear form, of Gram matrix $E=\operatorname{diag}(1,-1,-1,-1)$ and inertia $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$. Its Krein norm $\langle\tilde Q\rangle_{\natural*}=\lvert Q_t\rvert^2-\lVert\vec Q\rVert_E^2$ is real, indefinite and not multiplicative; the sign regions, the null set of real dimension seven and the Krein cone it closes are *Krein Norm Regularity and Degeneracy in the Biquaternion Algebra*.

The natural conjugation $J={}^{\natural}$ is the canonical fundamental symmetry, with bridge $\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\langle\tilde Q_2,J\tilde Q_1\rangle_*$, and it is the unique fundamental symmetry that is a unital algebra anti-automorphism. Its eigenspaces are the centre and the vector subspace, the fundamental decomposition of the space. The positive definite lines are $\mathbb{C}(e_t+\tilde V)$ with $\lVert\tilde V\rVert_E<1$.

The isotropic structure is the Krein counterpart of the algebraic one. The Witt index of the form is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$; the maximal real isotropic plane is $\mathrm{span}_{\mathbb{R}}\{e_t+\vec e_x,i(e_t+\vec e_x)\}$. The doubly null lines are exactly the Peirce lines $\mathbb{C}(e_t+i\vec u)$, so the null set of the Krein form meets the algebraic null cone exactly in the Peirce lines. The $J$-positive cone of operators is the image $J\cdot\{S\ge0\}$ of the Hilbert cone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | The Krein form |
| $\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^2$ | The Krein norm |
| $\langle\tilde Q_1,\tilde Q_2\rangle_*=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | The definite companion |
| $E=\operatorname{diag}(1,-1,-1,-1)$ | The Gram matrix; $\det E=-1$ |
| $J={}^{\natural}=\operatorname{diag}(1,-1,-1,-1)$ | The natural conjugation, the canonical fundamental symmetry |
| $\mathbb{C}_{\mathbb{B}}$, $\mathbb{V}_{\mathbb{B}}$ | The $\pm1$-eigenspaces of $J$; centre and vector subspace |
| $\ell_{\tilde V}=\mathbb{C}(e_t+\tilde V)$, $\lVert\tilde V\rVert_E<1$ | The positive definite lines |
| $\mathcal N=\{\langle\tilde Q\rangle_{\natural}=0\}$ | The algebraic null cone, of real dimension $6$ |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec u)$ | The Peirce idempotents; the doubly null lines |
| $\mathcal P_J=J\cdot\{S\ge0\}$ | The $J$-positive cone of operators |

## Further Reading

- [Krein Norm Regularity and Degeneracy in the Biquaternion Algebra](krein-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the Krein norm, its sign regions, the null set, the isotropic elements and the Krein cone.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four forms, their Gram matrices, their signatures and their four null sets.
- [The Fundamental Symmetry of the Form](the-fundamental-symmetry-of-the-form.html), for the general fundamental decomposition, the bridge between the indefinite and the definite form, and the non-uniqueness of the symmetry.
- [The Realification of the General Quaternionic Sesqualgebra](the-realification-of-the-general-quaternionic-sesqualgebra.html), for the real reading of the algebra and the realified matrix of signature $(2,6)$.
- [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the restriction of the form to the six remarkable subspaces.
- [The Krein Level Sets and the Hyperbolic Structure](the-krein-level-sets-and-the-hyperbolic-structure.html), for the level sets, their topology, the positive region and the complex hyperbolic ball.
- [The Krein Isometry Group and Its Cartan Decomposition](the-krein-isometry-group-and-its-cartan-decomposition.html), for the isometry group $\mathrm{U}(1,3)$, the $J$-positive cone in the Jordan algebra, and the $J$-contractions.
- [J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra](j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra.html), for the indefinite adjoint, the $J$-unitary operators and the indefinite spectral data.
