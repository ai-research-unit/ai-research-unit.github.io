# __The Spinor Module in Biquaternionic Form and Its Lorentz Action__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has been read, in the companion articles, in two ways. The article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* identifies the anti-Hermitian subspace $\mathbb{M}_-$ with Minkowski space: the four-vectors of relativistic physics live in $\mathbb{M}_-$, and the Lorentz group acts on them by the **rotor conjugation**

$$
\tilde{X} \;\longmapsto\; \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^{\dagger}.
$$

The article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* identifies the Hermitian subspace $\mathbb{M}_+$ with the operator algebra of a two-state system. Both accounts rest on a more primitive representation-theoretic fact: $\mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$, so it has a two-dimensional complex module, and the Lorentz group acts on that module by **multiplication**. This module is the **spinor module**. It is the subject of the present article.

The two actions are different in kind. The four-vector action is two-sided — it is a conjugation — while the spinor action is one-sided. The difference is not an accident of notation. It is the algebraic origin of the double cover: the element $-e_0$ of $SL(2,\mathbb{C})$ acts trivially by conjugation on $\mathbb{M}_-$, but it acts as $-\mathrm{id}$ on the spinor module. Consequently the four-vector representation descends to the Lorentz group, while the spinor representation does not: the spinor is a genuine representation of the double cover.

This article develops three things explicitly: the identification of the spinor module inside the biquaternion algebra, the two chiral halves (the left- and right-handed Weyl spinors), and the action of $SL(2,\mathbb{C})$ on the module together with its bilinear pairings. It is written as the foundation for the exercise on chirality and the Weyl spinors: the notation, the module, the two chiral halves, and the action are all defined here, so that the exercise can apply them.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1 e_2 = e_3$, and the scalar imaginary is $i$. The conjugations are the quaternion conjugate $\bar{\tilde{Q}}$, the complex conjugate $\tilde{Q}^*$ (conjugation of the coefficients), and the Hermitian conjugate $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$. The anti-Hermitian and Hermitian subspaces are

$$
\mathbb{M}_- = \{\tilde{Q} : \tilde{Q}^\dagger = -\tilde{Q}\}, \qquad \mathbb{M}_+ = \{\tilde{Q} : \tilde{Q}^\dagger = \tilde{Q}\},
$$

and $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace, the fixed-point set of complex conjugation. The four-vector the article is about lives in $\mathbb{M}_-$; throughout, the symbol $c$ denotes the speed of light in the medium.

## The Algebra and Its Simple Module

### The Matrix Isomorphism

The central structural fact is the isomorphism of $\mathbb{C}$-algebras

$$
\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H} \;\cong\; M_2(\mathbb{C}).
$$

We fix the realization that is used throughout the series. With $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ and $Q_\mu \in \mathbb{C}$,

$$
\Phi:\;\; \tilde{Q} \;\longmapsto\;
\begin{pmatrix}
Q_0 - iQ_3 & -iQ_1 - Q_2\\[2pt]
-iQ_1 + Q_2 & Q_0 + iQ_3
\end{pmatrix},
\qquad
\Phi(e_0) = I_2,\quad \Phi(e_k) = -i\sigma_k,\quad \Phi(i) = i I_2,
$$

where $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices and, as in the companion article *Quantum Mechanics in Biquaternionic Form*, the $i$ on the right is the standard imaginary unit of $\mathbb{C}\subset M_2(\mathbb{C})$ (the image of the scalar imaginary of $\mathbb{B}$). Under this convention $i e_k$ corresponds to $\sigma_k$, and the quaternion relations $e_j e_k = \sum_l \epsilon_{jkl}e_l$ hold on both sides. Two properties of $\Phi$ are used repeatedly:

$$
\Phi(\tilde{Q}\tilde{R}) = \Phi(\tilde{Q})\Phi(\tilde{R}), \qquad
\det\Phi(\tilde{Q}) = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = N(\tilde{Q}),
$$

so that the **norm form** of $\mathbb{B}$ is the determinant. The isomorphism also intertwines Hermitian conjugation with the conjugate transpose,

$$
\Phi(\tilde{Q}^\dagger) = \Phi(\tilde{Q})^{\dagger},
$$

where the $\dagger$ on the right is the matrix conjugate transpose. In particular $\mathbb{M}_-$ corresponds to the anti-Hermitian matrices and $\mathbb{M}_+$ to the Hermitian matrices.

### The Unique Simple Module

As a $\mathbb{C}$-algebra, $M_2(\mathbb{C})$ is **simple**: its only two-sided ideals are $0$ and itself. Its finite-dimensional modules are therefore completely reducible, and there is, up to isomorphism, exactly one simple module — the space of column vectors

$$
S = \mathbb{C}^2 = \left\{\psi = \begin{pmatrix}\psi_1\\ \psi_2\end{pmatrix} : \psi_1,\psi_2 \in \mathbb{C}\right\},
$$

on which $\mathbb{B}$ acts by matrix multiplication through $\Phi$. This is the **spinor module**. Its elements are the **spinors**. As a complex vector space $\dim_{\mathbb{C}} S = 2$; regarded as a real vector space by restriction of scalars it is four-dimensional, and Schur's lemma gives $\operatorname{End}_{\mathbb{B}}(S) = \mathbb{C}$, so $S$ is of complex type. A spinor is an element of the module $S$; it is not an element of the algebra $\mathbb{B}$. The distinction is worth keeping: the algebra acts, the module is acted upon.

Every finite-dimensional $\mathbb{B}$-module is a direct sum of copies of $S$. In particular, the left regular module is

$$
\mathbb{B} \;\cong\; S \oplus S,
$$

of complex dimension four. The module $S$ is the carrier of the **defining representation** of the group of units; the spinor is its most elementary inhabitant.

### A Basis and the Explicit Action

Writing a spinor as a column vector, the action of a general biquaternion is

$$
\psi \;\longmapsto\; \Phi(\tilde{Q})\,\psi
=
\begin{pmatrix}
(Q_0 - iQ_3)\psi_1 + (-iQ_1 - Q_2)\psi_2\\[2pt]
(-iQ_1 + Q_2)\psi_1 + (Q_0 + iQ_3)\psi_2
\end{pmatrix}.
$$

The action is $\mathbb{C}$-linear in $\psi$ and compatible with the algebra product, $\Phi(\tilde{Q})(\Phi(\tilde{R})\psi) = \Phi(\tilde{Q}\tilde{R})\psi$; this compatibility is the module structure. The algebra is exactly the algebra of all $\mathbb{C}$-linear endomorphisms of $S$: $\mathbb{B}\cong\operatorname{End}_{\mathbb{C}}(S)$.

## The Spinor Module as a Left Ideal

The module $S$ can be exhibited **inside** the algebra, which is often the most convenient realization. Let

$$
p = \frac{e_0 + i e_3}{2}, \qquad q = \frac{e_0 - i e_3}{2}.
$$

Since $(ie_3)^2 = 1$, these satisfy

$$
p^2 = p, \qquad q^2 = q, \qquad pq = qp = 0, \qquad p + q = e_0,
$$

so $p$ and $q$ are orthogonal idempotents summing to the unit. They are primitive, and they give the Peirce decomposition

$$
\mathbb{B} = \mathbb{B}p \oplus \mathbb{B}q, \qquad \mathbb{B}p \cong \mathbb{B}q \cong S \quad (\text{as left } \mathbb{B}\text{-modules}).
$$

The off-diagonal matrix units are recovered in biquaternion coordinates: with

$$
x = \frac{i e_1 - e_2}{2}, \qquad y = \frac{i e_1 + e_2}{2},
$$

the set $\{p,x,y,q\}$ is a $\mathbb{C}$-basis of $\mathbb{B}$ with the matrix-unit relations

$$
E_{11} = p,\quad E_{12} = x,\quad E_{21} = y,\quad E_{22} = q,
\qquad
px = x = xq,\quad qy = y = yp,\quad xy = p,\quad yx = q.
$$

Under $\Phi$, $p$ and $q$ are the diagonal matrix units and $\mathbb{B}p$ is the space of matrices whose only nonzero column is the first. A convenient basis of the left ideal is

$$
\{p,\; y\}, \qquad y = e_2 p = \frac{i e_1 + e_2}{2},
$$

and a general spinor in $\mathbb{B}p$ is

$$
\tilde{\psi} = \psi_1\, p + \psi_2\, y, \qquad \psi_1,\psi_2 \in \mathbb{C}.
$$

The coordinate map $\tilde{\psi}\leftrightarrow(\psi_1,\psi_2)^{T}$ is an isomorphism of $\mathbb{B}$-modules: for every $\tilde{Q}\in\mathbb{B}$,

$$
\tilde{Q}\tilde{\psi} = \psi_1(\tilde{Q}p) + \psi_2(\tilde{Q}y) \;\longleftrightarrow\; \Phi(\tilde{Q})\begin{pmatrix}\psi_1\\ \psi_2\end{pmatrix}.
$$

For example $e_3 p = -i p$ and $e_3 y = i y$, matching $\Phi(e_3) = \operatorname{diag}(-i,i)$; and $e_1 p = -i y$, matching the first column of $\Phi(e_1)=-i\sigma_1$. The two minimal left ideals $\mathbb{B}p$ and $\mathbb{B}q$ are both isomorphic to $S$; the algebra is simple, so all its simple modules are isomorphic.

This ideal model is the precise sense in which "the spinor module lies inside $\mathbb{B}$": a spinor is an element of the algebra that lies in the minimal left ideal $\mathbb{B}p$, and the algebra acts on it by left multiplication. It is not an arbitrary biquaternion.

## The Two Chiral Halves

The spinor module of the preceding sections carries the **defining representation** of $SL(2,\mathbb{C})$. In the classification of the companion article *Biquaternion Representation Theory*, this is the representation

$$
V_1 = \left(\tfrac{1}{2}, 0\right), \qquad \dim_{\mathbb{C}} V_1 = 2,
$$

the **left-handed Weyl spinor** module. Its complex conjugate

$$
\bar{S} = \overline{V_1} = \left(0, \tfrac{1}{2}\right), \qquad \dim_{\mathbb{C}}\bar{S} = 2,
$$

is the **right-handed Weyl spinor** module. These are the two **chiral halves**.

Concretely, both modules are carried by $\mathbb{C}^2$, but with different actions. If $\tilde{\Lambda}\in SL(2,\mathbb{C})$ and $g = \Phi(\tilde{\Lambda})$, then

$$
\text{left-handed:}\quad \psi \;\longmapsto\; g\,\psi,
\qquad\qquad
\text{right-handed:}\quad \chi \;\longmapsto\; \Phi(\tilde{\Lambda}^{*})\,\chi,
$$

where $\tilde{\Lambda}^{*}$ is the complex conjugate of the biquaternion (conjugation of its four coefficients). The second action is the conjugate of the first: since $\tilde{\Lambda}\mapsto\tilde{\Lambda}^{*}$ is an automorphism of $SL(2,\mathbb{C})$, the assignment is a genuine representation, and it is equivalent to the entrywise-conjugate action $g\mapsto\bar{g}$ (the two differ by conjugation with the invariant tensor $\epsilon$ introduced below). The chiral halves are exchanged by parity, and they are **not isomorphic** as complex representations of $SL(2,\mathbb{C})$.

Two cautions belong here, because they are often blurred.

**First, the two halves are not the two minimal left ideals.** The ideals $\mathbb{B}p$ and $\mathbb{B}q$ are both isomorphic to $S$ as left $\mathbb{B}$-modules: left multiplication by $\tilde{\Lambda}$ acts by the **same** defining representation on each. The chirality distinction is therefore *not* visible to the complex algebra $\mathbb{B}$ alone, which is simple and has a single simple module. It becomes visible only when the real structure — complex conjugation — is taken into account, or when the algebra is complexified.

**Second, the chiral splitting appears in the complexification.** As a real algebra, the complexification of $\mathbb{B}$ splits:

$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B} \;\cong\; M_2(\mathbb{C}) \oplus M_2(\mathbb{C}),
$$

the two central summands being the two chiralities. The corresponding central idempotents are $\tfrac{1}{2}(1\pm i_{\mathbb{C}}\omega)$, with $\omega = \gamma^0\gamma^1\gamma^2\gamma^3$ the volume element; under the correspondence $\mathbb{B}\cong\mathrm{Cl}_{1,3}^{+}$ the volume element is the image of the biquaternion scalar imaginary, so these are the projectors onto the two chiral halves. This is the algebraic form of the statement that the odd part of the Clifford algebra, which is not contained in the even subalgebra $\mathbb{B}$, exchanges the two chiralities (Section *The Even Subalgebra and the Origin of the Action*).

The **Dirac spinor module** is the direct sum of the two halves,

$$
\Delta = S \oplus \bar{S} = \left(\tfrac{1}{2},0\right)\oplus\left(0,\tfrac{1}{2}\right), \qquad \dim_{\mathbb{C}}\Delta = 4,
$$

on which $SL(2,\mathbb{C})$ acts block-diagonally by $g\oplus\Phi(\tilde{\Lambda}^{*})$. Its four complex components are the four components of the Dirac spinor, and its two blocks are the left- and right-handed Weyl spinors. A biquaternion, regarded as a $2\times2$ matrix, may be read as a pair of column spinors, which is the sense in which the algebra itself displays a pair of Weyl spinors; the two columns are two copies of $S$, and it is the pairing of $S$ with its conjugate that constitutes the Dirac module.

## The Unit-Norm Biquaternions and the Double Cover

The group that acts is the group of **unit-norm biquaternions**,

$$
SL(2,\mathbb{C}) \;=\; \{\tilde{\Lambda}\in\mathbb{B} : \tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0\},
$$

which under $\Phi$ is exactly $\{g\in GL_2(\mathbb{C}) : \det g = 1\}$, because the norm form is the determinant. It is a simply connected complex Lie group of complex dimension $3$ (real dimension $6$), with Lie algebra $\mathfrak{sl}(2,\mathbb{C})$, the traceless $2\times2$ complex matrices.

The subgroups relevant to the series sit inside it as follows:

| Element | Characterization | Subspace |
|---|---|---|
| Pure boost $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ | Hermitian, unit norm | $\mathbb{M}_+$ |
| Pure rotation $\tilde{R} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\hat{\mathbf{n}}$ | Real quaternion, unit norm | $\mathbb{H}_{\mathbb{B}}$ |
| General $\tilde{\Lambda}$ | Unit norm | $\mathbb{B}$ |

Pure boosts satisfy $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$; they do not form a subgroup (the product of two non-collinear boosts is a boost plus a rotation). Pure rotations form the subgroup $SU(2) = SL(2,\mathbb{C})\cap U(2)$.

The action on the four-vector space is the conjugation map

$$
\pi:\; SL(2,\mathbb{C}) \longrightarrow SO^{+}(1,3), \qquad
\pi(\tilde{\Lambda}):\; \tilde{X} \;\longmapsto\; \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^{\dagger}, \qquad \tilde{X}\in\mathbb{M}_-.
$$

It is well defined (the image of an anti-Hermitian element is anti-Hermitian), it preserves the norm form, and it is a group homomorphism. Its kernel is

$$
\ker\pi = \{\pm e_0\} \cong \mathbb{Z}/2\mathbb{Z},
$$

since $-e_0$ is central, $(-\tilde{\Lambda})\tilde{X}(-\tilde{\Lambda})^\dagger = \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ for every $\tilde{X}$ (the two signs cancel). Hence $\pi$ is **two-to-one** onto the proper orthochronous Lorentz group,

$$
SO^{+}(1,3) \;\cong\; SL(2,\mathbb{C})/\{\pm e_0\},
$$

and $SL(2,\mathbb{C})$ is the **double cover** of the restricted Lorentz group.

The spinor action is by contrast **faithful**. On $S$, the element $-e_0$ acts as

$$
\Phi(-e_0) = -I_2,
$$

so $\pm\tilde{\Lambda}$ act differently on every spinor. The defining representation therefore does **not** descend to $SO^{+}(1,3)$: it is a genuine representation of the double cover. This is the exact sense in which the spinor action and the four-vector action differ by the double cover.

## The Lorentz Action on the Spinor Module

### The Action

The Lorentz group acts on the spinor module by **left multiplication**:

$$
\psi \;\longmapsto\; \tilde{\Lambda}\,\psi \;=\; \Phi(\tilde{\Lambda})\,\psi,
\qquad \tilde{\Lambda}\in SL(2,\mathbb{C}),\quad \psi\in S.
$$

Equivalently, in the ideal model, $\tilde{\psi}\in\mathbb{B}p$ is sent to $\tilde{\Lambda}\tilde{\psi}\in\mathbb{B}p$; the ideal is stable because $\mathbb{B}(\mathbb{B}p)\subseteq\mathbb{B}p$. The action is $\mathbb{C}$-linear, and it is a group action:

$$
\tilde{\Lambda}_2(\tilde{\Lambda}_1\psi) = (\tilde{\Lambda}_2\tilde{\Lambda}_1)\psi.
$$

No conjugation appears. This is the defining feature of the spinor representation.

### Boosts and Rotations Explicitly

For a boost along $\hat{\mathbf{u}}$ with rapidity $\psi$,

$$
\Phi(\tilde{\Lambda}) = \cosh\frac{\psi}{2}\,I_2 + \sinh\frac{\psi}{2}\,\hat{\mathbf{u}}\cdot\boldsymbol{\sigma},
$$

as follows from $\Phi(i\hat{\mathbf{u}}) = \hat{\mathbf{u}}\cdot\boldsymbol{\sigma}$. For $\hat{\mathbf{u}} = \hat{\mathbf{e}}_3$ this is the diagonal matrix $\operatorname{diag}(e^{\psi/2},e^{-\psi/2})$, which stretches one spinor component and contracts the other. For a rotation about $\hat{\mathbf{n}}$ by angle $\theta$,

$$
\Phi(\tilde{R}) = \cos\frac{\theta}{2}\,I_2 - i\sin\frac{\theta}{2}\,\hat{\mathbf{n}}\cdot\boldsymbol{\sigma},
$$

the standard $SU(2)$ rotation matrix. A rotation by $2\pi$ sends $\Phi(\tilde{R})$ to $-I_2$: it is the identity in the four-vector representation but not on the spinor module. A rotation by $4\pi$ is the identity on both.

### The Infinitesimal Action

Differentiating at the identity gives the action of the Lie algebra. The generators of $SL(2,\mathbb{C})$ are the traceless matrices, and in the biquaternion basis

$$
\mathfrak{sl}(2,\mathbb{C}) = \operatorname{span}_{\mathbb{R}}\{\,e_1,e_2,e_3\,\} \;\oplus\; \operatorname{span}_{\mathbb{R}}\{\,ie_1,ie_2,ie_3\,\},
$$

the first summand being the rotations (the compact subalgebra $\mathfrak{su}(2)\cong\mathfrak{so}(3)$ and $\mathbb{H}_{\mathbb{B}}$) and the second the boosts (the non-compact part, in $\mathbb{M}_+$). Under $\Phi$,

$$
e_k \longmapsto -i\sigma_k, \qquad i e_k \longmapsto \sigma_k,
$$

so the anti-Hermitian generators $-i\sigma_k$ and the Hermitian generators $\sigma_k$ both act on $S$ by matrix multiplication. On the spinor module the infinitesimal generators act as the Pauli matrices and their multiples, which is the familiar statement that the spin-$\frac{1}{2}$ representation is the fundamental representation of $\mathfrak{sl}(2,\mathbb{C})$.

The **compact subgroup** $SU(2)\subset SL(2,\mathbb{C})$ consists of the unit-norm biquaternions with real vector part (the unit quaternions), for which $\tilde{R}^\dagger\tilde{R} = e_0$. Its action on $S$ is unitary with respect to the Hermitian inner product $\langle\psi,\phi\rangle = \psi^\dagger\phi$, and it is the double cover of the spatial rotation group $SO(3)$. The boosts, by contrast, are not unitary, and they do not preserve that inner product; this is the representation-theoretic expression of the non-compactness of the Lorentz group.

## Bilinear Pairings and the Vector Representation

The spinor module carries two natural invariant pairings and one equivariant bilinear map to the algebra. They are the algebraic ancestors of the Dirac bilinears.

### The Symplectic Form

Define

$$
\varepsilon(\psi,\phi) = \psi_1\phi_2 - \psi_2\phi_1 = \psi^{T}\epsilon\,\phi,
\qquad
\epsilon = \begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix}.
$$

Since $\det g = 1$ for $g\in SL(2,\mathbb{C})$, one has $g^{T}\epsilon\, g = (\det g)\,\epsilon = \epsilon$, and therefore

$$
\varepsilon(g\psi, g\phi) = \psi^{T} g^{T}\epsilon\, g\,\phi = \varepsilon(\psi,\phi).
$$

The form $\varepsilon$ is a nondegenerate **invariant bilinear form** on $S$. It identifies $S$ with its dual, $S^{*}\cong S$: the defining module is **self-dual**. This is the spinor metric used to raise and lower Weyl indices, and it is the reason a pair of left-handed spinors has an invariant antisymmetric contraction. Self-duality is not self-conjugacy: $S^{*}\cong S$, but $\bar{S}\not\cong S$.

### The Hermitian Form

The Hermitian inner product

$$
h(\psi,\phi) = \psi^{\dagger}\phi = \psi_1^{*}\phi_1 + \psi_2^{*}\phi_2
$$

is positive definite, but it is **not** invariant under all of $SL(2,\mathbb{C})$:

$$
h(g\psi, g\phi) = \psi^{\dagger} g^{\dagger} g\,\phi.
$$

It is invariant exactly when $g^{\dagger}g = I_2$, i.e. on the compact subgroup $SU(2)$. For a boost, $g^{\dagger}g\neq I_2$, and $h$ is not preserved. The hermitian form therefore selects the maximal compact subgroup; it does not define a Lorentz-invariant structure on a single chiral half.

### The Mixed Pairing

There is, however, an invariant pairing between the two chiral halves. Let $\psi\in S$ transform as $\psi\mapsto g\psi$ and let $\chi\in\bar{S}$ transform as $\chi\mapsto\Phi(\tilde{\Lambda}^{*})\chi$. Then the sesquilinear pairing

$$
b(\psi,\chi) = \psi^{\dagger}\chi
$$

is invariant. Indeed,

$$
b(g\psi,\, \Phi(\tilde{\Lambda}^{*})\chi)
= \psi^{\dagger}\, \Phi(\tilde{\Lambda})^{\dagger}\,\Phi(\tilde{\Lambda}^{*})\,\chi
= \psi^{\dagger}\,\Phi\!\left(\tilde{\Lambda}^{\dagger}\tilde{\Lambda}^{*}\right)\chi
= \psi^{\dagger}\chi,
$$

because $\tilde{\Lambda}^{\dagger}\tilde{\Lambda}^{*} = (\bar{\tilde{\Lambda}}\tilde{\Lambda})^{*} = e_0^{*} = e_0$ for a unit-norm biquaternion. This mixed pairing is the invariant scalar bilinear of the Dirac spinor; it pairs a left-handed spinor with a right-handed one.

### The Spinor-to-Vector Map

Finally, the outer product of a spinor with its conjugate lands in the algebra. For $u,v\in S$, the matrix

$$
X = u\,v^{\dagger} \;\in\; M_2(\mathbb{C}) \;\cong\; \mathbb{B}
$$

is a rank-one element of the algebra, and under the Lorentz action $u\mapsto gu$ on the first spinor and the conjugate (right-handed) entry $v^{\dagger}\mapsto v^{\dagger}g^{\dagger}$ it transforms as

$$
X = u\,v^{\dagger} \;\longmapsto\; (gu)(gv)^{\dagger} = g\,X\,g^{\dagger}.
$$

This is exactly the transformation law of the **rotor conjugation** on the material sector. It must be read as a statement about the equivariance of the whole algebra $M_2(\mathbb{C})$, however, and not as the vector representation itself; two cautions are in order. First, the real span of the outer products $u v^{\dagger}$ as $u$ and $v$ range over $S$ is all of $M_2(\mathbb{C})$, of real dimension $8$, not the Hermitian subspace of real dimension $4$: the matrices $E_{12}$ and $iE_{12}$ are each a single outer product, realized by $u = e_1$, $v = e_2$ and by $u = e_1$, $v = -ie_2$ respectively, and they are independent over the reals. Second, $u v^{\dagger}$ is Hermitian **only** when the two spinors are proportional by a real factor, $v = \lambda u$ with $\lambda \in \mathbb{R}$; for a generic pair $i\,uv^{\dagger}$ does not lie in $\mathbb{M}_-$ at all, and is therefore not a four-vector.

The Hermitian subspace $\mathbb{M}_+$ is the **real** span of the self-pair products $u\,u^{\dagger}$, of real dimension $4$. For a general pair the object that transforms as a four-vector is the symmetrised product

$$
H = \tfrac{1}{2}\left(u\,v^{\dagger} + v\,u^{\dagger}\right) \;\in\; \mathbb{M}_+,
\qquad
V = iH \;\in\; \mathbb{M}_-,
$$

which is Hermitian for every pair and reduces to the outer product $u\,u^{\dagger}$ when $v = u$. The four-vector associated with the spinor pair is thus $iH$, which replaces the outer product $i\,uv^{\dagger}$ and agrees with it when the pair is (anti)parallel (up to the conventions of the $ict$ description). The map $S\otimes\bar{S}\to\mathbb{B}$, $u\otimes v^{\dagger}\mapsto uv^{\dagger}$, is an isomorphism of $SL(2,\mathbb{C})$-representations onto the algebra, while the four-vector representation is the real form of it carried by the Hermitian slice, and it realizes the vector representation as the tensor product of the two chiral halves,

$$
\left(\tfrac{1}{2},\tfrac{1}{2}\right) = \left(\tfrac{1}{2},0\right)\otimes\left(0,\tfrac{1}{2}\right).
$$

This is the algebraic link between the one-sided spinor action and the two-sided four-vector action, and its algebra-level form is the Hermitian form $\tilde{Q}\tilde{Q}^{\dagger}\in\mathbb{M}_+$ of the companion articles.

The transformation laws are collected in the following table.

| Pairing | Domain | Transformation | Invariance |
|---|---|---|---|
| $\varepsilon(\psi,\phi) = \psi^{T}\epsilon\phi$ | $S\times S\to\mathbb{C}$ | invariant | $g^{T}\epsilon g = \epsilon$ |
| $h(\psi,\phi) = \psi^{\dagger}\phi$ | $S\times S\to\mathbb{C}$ | $\psi^{\dagger}g^{\dagger}g\,\phi$ | invariant iff $g\in SU(2)$ |
| $b(\psi,\chi) = \psi^{\dagger}\chi$ | $S\times\bar{S}\to\mathbb{C}$ | invariant | $\tilde{\Lambda}^{\dagger}\tilde{\Lambda}^{*}=e_0$ |
| $X = u\,v^{\dagger}$ | $S\times\bar{S}\to\mathbb{B}$ | $g\,X\,g^{\dagger}$ | equivariant |
| $H = \tfrac{1}{2}(uv^{\dagger}+vu^{\dagger})$ | $S\times\bar{S}\to\mathbb{M}_+$ | $g\,H\,g^{\dagger}$ | Hermitian; four-vector is $iH$ |

## Spinor Action Versus Rotor Conjugation

It is worth stating the contrast in one place, since it is the conceptual centre of the article.

| Feature | Four-vector action on $\mathbb{M}_-$ | Spinor action on $S$ |
|---|---|---|
| Formula | $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^{\dagger}$ | $\psi\mapsto\tilde{\Lambda}\psi$ |
| Number of factors of $\tilde{\Lambda}$ | two (quadratic) | one (linear) |
| Kernel of the action | $\{\pm e_0\}$ | $\{e_0\}$ |
| Image group | $SO^{+}(1,3)$ | $SL(2,\mathbb{C})$ |
| Action of $-e_0$ | $+\mathrm{id}$ | $-\mathrm{id}$ |
| Descends to the Lorentz group? | yes | no |

The two actions do not "differ by the double cover" in the sense that one is a cover of the other; rather, the four-vector action **factors through** the double cover while the spinor action does not. The conjugate parameter $\tilde{\Lambda}$ and $-\tilde{\Lambda}$ describe the same Lorentz transformation of every four-vector, but opposite transformations of every spinor. For this reason the spinor representation is the representation of the **double cover** $SL(2,\mathbb{C})$, and the sign of the spinor is a genuine degree of freedom that no four-vector can see. The relation between the two actions is the bilinear map $X = u v^{\dagger}$ of the preceding section: the four-vector is a *pair* of spinors, and the two one-sided actions on the pair combine into the two-sided action on their product.

A concrete illustration is the composition of two transformations. If $\tilde{\Lambda}_1$ and $\tilde{\Lambda}_2$ are rotors, then on four-vectors

$$
\tilde{\Lambda}_2(\tilde{\Lambda}_1\tilde{X}\tilde{\Lambda}_1^{\dagger})\tilde{\Lambda}_2^{\dagger} = (\tilde{\Lambda}_2\tilde{\Lambda}_1)\tilde{X}(\tilde{\Lambda}_2\tilde{\Lambda}_1)^{\dagger},
$$

while on spinors

$$
\tilde{\Lambda}_2(\tilde{\Lambda}_1\psi) = (\tilde{\Lambda}_2\tilde{\Lambda}_1)\psi.
$$

Both compose by multiplication of the rotors; the difference is only that the four-vector formula has a pair of rotors, and hence a sign that cancels, while the spinor formula has one, and hence a sign that does not.

## The Even Subalgebra and the Origin of the Action

The reason the spinor action is one-sided, and the four-vector action two-sided, is the place of $\mathbb{B}$ in the Clifford algebra. As in the companion article on the Dirac equation, $\mathbb{B}$ is isomorphic, as a real algebra, to the **even subalgebra** of $\mathrm{Cl}_{1,3}$:

$$
\mathbb{B} \;\cong\; \mathrm{Cl}_{1,3}^{+}(\mathbb{R}),
\qquad
e_1\mapsto\gamma^2\gamma^3,\quad e_2\mapsto\gamma^3\gamma^1,\quad e_3\mapsto\gamma^2\gamma^1,\quad i\mapsto\gamma^0\gamma^1\gamma^2\gamma^3 .
$$

The full Clifford algebra acts on its spinor module by **left multiplication**; restricting to the even subalgebra $\mathbb{B}$ gives the action considered in this article. The spin group sits inside the even subalgebra,

$$
\operatorname{Spin}(1,3) \;\cong\; SL(2,\mathbb{C}) \;\subset\; \mathbb{B} \;\subset\; \mathrm{Cl}_{1,3}.
$$

Two distinct actions are then visible in the Clifford picture. The spin group acts on the spinor module by left multiplication — one-sided, because a Clifford module is a module and the action is linear. The same group acts on the vector space $W\subset\mathrm{Cl}_{1,3}$ (spanned by the odd generators) by a **two-sided conjugation** — the twisted adjoint, $v\mapsto\tilde{\Lambda}v\tilde{\Lambda}^{-1}$, written in the read-list conventions as the rotor conjugation $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^{\dagger}$ — which is two-sided because a vector is being conjugated inside the algebra. The vector representation is the tensor product of the spinor representation with its conjugate in the sense of the preceding section; the even subalgebra is exactly the algebra generated by the bivectors, and the bivectors are the Lie algebra of the spin group.

This correspondence between the biquaternion algebra and the even Clifford subalgebra is the algebraic origin of the whole structure. It explains at once:

1. why a spinor transforms one-sidedly (it is an element of a Clifford module, and modules are acted on linearly);
2. why a four-vector transforms two-sidedly (it is an element of the odd part, acted on by twisted conjugation);
3. why $-e_0$ acts as $-\mathrm{id}$ on spinors but trivially on four-vectors (a single factor of the central unit versus two);
4. why the two chiralities are not visible to the complex algebra $\mathbb{B}$ but appear on complexification: the chirality operator $\gamma_5 = i_{\mathbb{C}}\omega$ (the scalar imaginary of the complexified Clifford algebra times the volume element $\omega$) is not an element of the even subalgebra, and it anticommutes with the generators; the odd part therefore exchanges the two half-spin modules, while the even part $\mathbb{B}$ preserves them. The complexified even algebra splits accordingly,
$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B} \cong M_2(\mathbb{C})\oplus M_2(\mathbb{C}),
$$
with the two summands the two chiral halves.

In this reading the spinor module is not an add-on to the biquaternion framework; it is the module that the framework was built to carry, and the material and informational sectors are its bilinear and operator shadows.

## Open Questions

1. **The spinor module and the informational sector.** The article on $\mathbb{M}_+$ interprets the Hermitian subspace as the operator algebra of a qubit. The spinor module developed here is the representation space on which those operators act. The precise relation between the qubit states of the informational sector and the Weyl spinors of the Lorentz group — whether they are the same module under different real structures — is not settled here.
2. **The covariance of the biquaternion Dirac equation.** The companion article on the Dirac equation formulates the equation as the linear chiral pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$ but leaves open the transformation law of the biquaternion-valued field $\tilde{\Psi}$.

A natural candidate is the module action defined here; its compatibility with the mass term requires the relationship between the one-sided action and the conjugate module to be fixed by a convention.
3. **The biquaternion form of the symplectic pairing.** The invariant form $\varepsilon$ is presented here in matrix coordinates. Its expression as a biquaternion bilinear on the ideal $\mathbb{B}p$ follows from the coordinate map, but the cleanest biquaternion formula is a matter of convention.
4. **Majorana and reality conditions.** In Lorentzian signature the Dirac module is self-conjugate but the two Weyl halves are a conjugate pair, so Majorana spinors exist while Majorana–Weyl spinors do not. How these reality conditions read as conditions on biquaternion-valued fields is a natural continuation.
5. **Curved spacetime.** The module and its action are pointwise algebraic. Whether the spinor module globalizes to a bundle over a curved biquaternionic background is open, in parallel with the open questions of the companion articles.

## Summary

The biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has a unique simple module, the two-dimensional complex **spinor module** $S=\mathbb{C}^2$, on which $\mathbb{B}$ acts by matrix multiplication. Inside the algebra, $S$ is realized as the minimal left ideal $\mathbb{B}p$, $p = \tfrac{1}{2}(e_0+ie_3)$, whose elements are the spinors; the algebra acts by left multiplication, and the action is one-sided.

The **left-handed Weyl spinor** is the defining module $(\tfrac12,0)$; the **right-handed Weyl spinor** is its complex conjugate $(0,\tfrac12)$. These are the two **chiral halves**; their direct sum is the four-component Dirac spinor module. The two halves are not isomorphic as complex representations of $SL(2,\mathbb{C})$ (they are conjugate to one another), and the chirality distinction is a real-structure distinction that appears on complexification, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$.

The group of unit-norm biquaternions is $SL(2,\mathbb{C})$, the double cover of the restricted Lorentz group $SO^{+}(1,3)$. It acts on the spinor module by

$$
\psi \longmapsto \tilde{\Lambda}\psi,
\qquad \tilde{\Lambda}\in SL(2,\mathbb{C}),\quad \psi\in S,
$$

with $\pm\tilde{\Lambda}$ acting differently ($-e_0$ acts as $-\mathrm{id}$). The four-vector action of the companion articles, $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^{\dagger}$ on $\mathbb{M}_-$, is recovered from the Hermitian part of the spinor bilinear, $H = \tfrac{1}{2}(uv^{\dagger}+vu^{\dagger})$, which transforms as $gHg^{\dagger}$ and whose four-vector image is $iH$. The spinor action is faithful and does not descend to the Lorentz group; the four-vector action has kernel $\{\pm e_0\}$ and does. This is the double cover, seen from the module side.

The spinor module carries three bilinear structures and one equivariant bilinear map: the symplectic form $\varepsilon$ (invariant, and the source of self-duality $S^{*}\cong S$), the Hermitian form $h$ (invariant only on the compact subgroup $SU(2)$), the mixed pairing $b:S\times\bar{S}\to\mathbb{C}$ (invariant, the Dirac scalar bilinear), and the outer product $S\times\bar{S}\to\mathbb{B}$, whose Hermitian part $H$ carries the vector representation. The algebraic origin of the one-sided spinor action and the two-sided four-vector action is the identification $\mathbb{B}\cong\mathrm{Cl}_{1,3}^{+}$: the spin group lies in the even subalgebra and acts on a Clifford module by left multiplication, while it acts on the odd part by twisted conjugation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ | Matrix realization, $\Phi(e_k)=-i\sigma_k$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \det\Phi(\tilde{Q})$ | Norm form |
| $S = \mathbb{C}^2$ | Spinor module (unique simple module), $\dim_{\mathbb{C}}S=2$ |
| $V_1 = (\tfrac12,0)$ | Left-handed Weyl (defining) representation |
| $\bar{S} = \overline{V_1} = (0,\tfrac12)$ | Right-handed Weyl (conjugate) representation |
| $\Delta = S\oplus\bar{S}$ | Dirac spinor module, $\dim_{\mathbb{C}}\Delta=4$ |
| $p = \tfrac12(e_0+ie_3),\ q=\tfrac12(e_0-ie_3)$ | Primitive orthogonal idempotents, $\mathbb{B}=\mathbb{B}p\oplus\mathbb{B}q$ |
| $x = \tfrac12(ie_1-e_2),\ y=\tfrac12(ie_1+e_2)=e_2p$ | Matrix units $E_{12},E_{21}$; basis $\{p,y\}$ of $S$ |
| $SL(2,\mathbb{C}) = \{\tilde{\Lambda}:\tilde{\Lambda}\bar{\tilde{\Lambda}}=e_0\}$ | Unit-norm biquaternions, double cover of $SO^{+}(1,3)$ |
| $\tilde{\Lambda} = \cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ | Boost rotor (Hermitian, in $\mathbb{M}_+$) |
| $\tilde{R} = \cos\frac{\theta}{2}+\sin\frac{\theta}{2}\hat{\mathbf{n}}$ | Rotation rotor (in $\mathbb{H}_{\mathbb{B}}$) |
| $\psi\mapsto\tilde{\Lambda}\psi$ | Lorentz action on the spinor module |
| $\varepsilon(\psi,\phi)=\psi^{T}\epsilon\phi$ | Invariant symplectic pairing on $S$ |
| $h(\psi,\phi)=\psi^{\dagger}\phi$ | Hermitian form (invariant on $SU(2)$) |
| $b(\psi,\chi)=\psi^{\dagger}\chi$ | Invariant pairing $S\times\bar{S}\to\mathbb{C}$ |
| $H = \tfrac{1}{2}(uv^{\dagger}+vu^{\dagger})\mapsto gHg^{\dagger}$ | Spinor bilinear; four-vector is $iH$ |
| $\mathbb{B}\cong\mathrm{Cl}_{1,3}^{+}$ | Even Clifford subalgebra correspondence |

## Further Reading

- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the standard two-component spinor calculus, the invariant $\epsilon$-form, and the Weyl spinors.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford-algebra construction of spinors as minimal left ideals and the double cover of the Lorentz group.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of the Lorentz group and the relation between spinors and four-vectors.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of spinors and Lorentz transformations in the even subalgebra.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original spinor representation of the electron.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the representation theory of the Lorentz group and the construction of the Dirac spinor from two Weyl spinors.
- Julius Wess and Jonathan Bagger, *Supersymmetry and Supergravity* (Princeton, 1992), for the two-component (dotted and undotted) spinor conventions.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the modules of $M_2(\mathbb{C})$, the highest-weight classification, and the Clebsch–Gordan rule.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for simple modules, Schur's lemma, and the structure of matrix algebras.
