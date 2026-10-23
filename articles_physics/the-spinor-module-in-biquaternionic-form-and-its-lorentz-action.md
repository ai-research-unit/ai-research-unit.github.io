# __The Spinor Module in Biquaternionic Form and Its Lorentz Action__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has been read, in the companion articles, in two ways. The article *The Material Sector: Four-Vectors, Interval and Lorentz Action* identifies the anti-Hermitian subspace $\mathbb{M}_-$ with Minkowski space: the four-vectors of relativistic physics live in $\mathbb{M}_-$, and the Lorentz group acts on them by the **rotor conjugation** with $\tilde U_{\mathrm L}$, the unit-norm biquaternion that implements the Lorentz transformation,

$$
\tilde{Q} \;\longmapsto\; \tilde U_{\mathrm L}\,\tilde{Q}\,\tilde U_{\mathrm L}^{*}.
$$

The article *The Informational Sector: States, Observables and Probability* identifies the Hermitian subspace $\mathbb{M}_+$ with the observables of a two-state system, whose products generate its operator algebra. Both accounts rest on a more primitive representation-theoretic fact: $\mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$, so it has a two-dimensional complex module, and the Lorentz group acts on that module by **multiplication**. This module is the **spinor module**. It is the subject of the present article.

The two actions are different in kind. The four-vector action is two-sided — it is a conjugation — while the spinor action is one-sided. The difference is not an accident of notation. It is the algebraic origin of the double cover: the element $-e_t$ of $SL(2,\mathbb{C})$ acts trivially by conjugation on $\mathbb{M}_-$, but it acts as $-\mathrm{id}$ on the spinor module. Consequently the four-vector representation descends to the Lorentz group, while the spinor representation does not: the spinor is a genuine representation of the double cover.

This article develops three things explicitly: the identification of the spinor module inside the biquaternion algebra, the two chiral halves (the left- and right-handed Weyl spinors), and the action of $SL(2,\mathbb{C})$ on the module together with its bilinear pairings. It is written as the foundation for the exercise on chirality and the Weyl spinors: the notation, the module, the two chiral halves, and the action are all defined here, so that the exercise can apply them.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_\mu^2 = -e_t$ and $\vec e_x \vec e_y = \vec e_z$, and the scalar imaginary is $i$. The conjugations are the quaternion conjugate $\tilde{Q}^{\natural}$, the complex conjugate $\tilde{Q}^*$ (conjugation of the coefficients), and the Hermitian conjugate $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$. The anti-Hermitian and Hermitian subspaces are

$$
\mathbb{M}_- = \{\tilde{Q} : \tilde{Q}^{*} = -\tilde{Q}\}, \qquad \mathbb{M}_+ = \{\tilde{Q} : \tilde{Q}^{*} = \tilde{Q}\},
$$

and $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace, the fixed-point set of complex conjugation. The four-vector the article is about lives in $\mathbb{M}_-$; throughout, the symbol $c$ denotes the speed of light in the medium.

## The Algebra and Its Simple Module

### The Matrix Isomorphism

The central structural fact is the isomorphism of $\mathbb{C}$-algebras

$$
\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H} \;\cong\; M_2(\mathbb{C}).
$$

We fix the realization that is used throughout the series. With $\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu$ and $Q_\mu \in \mathbb{C}$,

$$
\mathsf{M}_2:\;\; \tilde{Q} \;\longmapsto\;
\begin{pmatrix}
Q_t - iQ_3 & -iQ_1 - Q_y\\[2pt]
-iQ_1 + Q_y & Q_t + iQ_3
\end{pmatrix},
\qquad
\mathsf{M}_2(e_t) = I_2,\quad \mathsf{M}_2(\vec e_\mu) = -i\sigma_\mu,\quad \mathsf{M}_2(i) = i I_2,
$$

where $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices and, as in the companion article *Quantum Physics in Biquaternionic Form*, the $i$ on the right is the standard imaginary unit of $\mathbb{C}\subset M_2(\mathbb{C})$ (the image of the scalar imaginary of $\mathbb{B}$). Under this convention $i \vec e_\mu$ corresponds to $\sigma_\mu$, and the quaternion relations $\vec e_\mu \vec e_\nu = \sum_\lambda \epsilon_{\mu\nu\lambda}\vec e_\lambda$ hold on both sides. Two properties of $\mathsf{M}_2$ are used repeatedly:

$$
\mathsf{M}_2(\tilde{Q}\tilde Q_1) = \mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde Q_1), \qquad
\det\mathsf{M}_2(\tilde{Q}) = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 = \langle\tilde{Q}\rangle_{\natural},
$$

so that the **biquaternion norm** of $\mathbb{B}$ is the determinant. The isomorphism also intertwines Hermitian conjugation with the conjugate transpose,

$$
\mathsf{M}_2(\tilde{Q}^{*}) = \mathsf{M}_2(\tilde{Q})^{\dagger},
$$

where the ${}^{*}$ on the right is the matrix conjugate transpose. In particular $\mathbb{M}_-$ corresponds to the anti-Hermitian matrices and $\mathbb{M}_+$ to the Hermitian matrices.

### The Unique Simple Module

As a $\mathbb{C}$-algebra, $M_2(\mathbb{C})$ is **simple**: its only two-sided ideals are $0$ and itself. Its finite-dimensional modules are therefore completely reducible, and there is, up to isomorphism, exactly one simple module — the space of column vectors

$$
S = \mathbb{C}^2 = \left\{\psi = \begin{pmatrix}\psi_1\\ \psi_2\end{pmatrix} : \psi_1,\psi_2 \in \mathbb{C}\right\},
$$

on which $\mathbb{B}$ acts by matrix multiplication through $\mathsf{M}_2$. This is the **spinor module**. Its elements are the **spinors**. As a complex vector space $\dim_{\mathbb{C}} S = 2$; regarded as a real vector space by restriction of scalars it is four-dimensional, and Schur's lemma gives $\operatorname{End}_{\mathbb{B}}(S) = \mathbb{C}$, so $S$ is of complex type. A spinor is an element of the module $S$; it is not an element of the algebra $\mathbb{B}$. The distinction is worth keeping: the algebra acts, the module is acted upon.

Every finite-dimensional $\mathbb{B}$-module is a direct sum of copies of $S$. In particular, the left regular module is

$$
\mathbb{B} \;\cong\; S \oplus S,
$$

of complex dimension four. The module $S$ is the carrier of the **defining representation** of the group of units; the spinor is its most elementary inhabitant.

### A Basis and the Explicit Action

Writing a spinor as a column vector, the action of a general biquaternion is

$$
\psi \;\longmapsto\; \mathsf{M}_2(\tilde{Q})\,\psi
=
\begin{pmatrix}
(Q_t - iQ_3)\psi_1 + (-iQ_1 - Q_y)\psi_2\\[2pt]
(-iQ_1 + Q_y)\psi_1 + (Q_t + iQ_3)\psi_2
\end{pmatrix}.
$$

The action is $\mathbb{C}$-linear in $\psi$ and compatible with the algebra product, $\mathsf{M}_2(\tilde{Q})(\mathsf{M}_2(\tilde Q_1)\psi) = \mathsf{M}_2(\tilde{Q}\tilde Q_1)\psi$; this compatibility is the module structure. The algebra is exactly the algebra of all $\mathbb{C}$-linear endomorphisms of $S$: $\mathbb{B}\cong\operatorname{End}_{\mathbb{C}}(S)$.

## The Spinor Module as a Left Ideal

The module $S$ can be exhibited **inside** the algebra, which is often the most convenient realization. Let

$$
\tilde\Pi_+ = \frac{e_t + i \vec e_z}{2}, \qquad \tilde\Pi_- = \frac{e_t - i \vec e_z}{2}.
$$

Here $i\vec e_z$ is a root of $+1$, $(i\vec e_z)^2=e_t$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents. These satisfy

$$
\tilde\Pi_+^2 = \tilde\Pi_+, \qquad \tilde\Pi_-^2 = \tilde\Pi_-, \qquad \tilde\Pi_+\tilde\Pi_- = \tilde\Pi_-\tilde\Pi_+ = 0, \qquad \tilde\Pi_+ + \tilde\Pi_- = e_t,
$$

so $\tilde\Pi_+$ and $\tilde\Pi_-$ are orthogonal idempotents summing to the unit. They are primitive, and they give the Peirce decomposition

$$
\boxed{\;\mathbb{B} = \mathbb{B}\tilde\Pi_+ \oplus \mathbb{B}\tilde\Pi_-, \qquad \mathbb{B}\tilde\Pi_+ \cong \mathbb{B}\tilde\Pi_- \cong S \quad (\text{as left } \mathbb{B}\text{-modules})\;}.
$$

The off-diagonal matrix units are recovered in biquaternion coordinates: with

$$
\vec\Upsilon_x = \frac{i \vec e_x - \vec e_y}{2}, \qquad \vec\Upsilon_y = \frac{i \vec e_x + \vec e_y}{2},
$$

the set $\{\tilde\Pi_+,\vec\Upsilon_x,\vec\Upsilon_y,\tilde\Pi_-\}$ is a $\mathbb{C}$-basis of $\mathbb{B}$ with the matrix-unit relations

$$
E_{11} = \tilde\Pi_+,\quad E_{12} = x,\quad E_{21} = y,\quad E_{22} = \tilde\Pi_-,
\qquad
\tilde\Pi_+\vec\Upsilon_x = \vec\Upsilon_x = \vec\Upsilon_x \tilde\Pi_-,\quad \tilde\Pi_-\vec\Upsilon_y = \vec\Upsilon_y = \vec\Upsilon_y \tilde\Pi_+,\quad \vec\Upsilon_x\vec\Upsilon_y = \tilde\Pi_+,\quad \vec\Upsilon_y\vec\Upsilon_x = \tilde\Pi_-.
$$

Under $\mathsf{M}_2$, $\tilde\Pi_+$ and $\tilde\Pi_-$ are the diagonal matrix units and $\mathbb{B}\tilde\Pi_+$ is the space of matrices whose only nonzero column is the first. A convenient basis of the left ideal is

$$
\{\tilde\Pi_+,\; \vec\Upsilon_y\}, \qquad \vec\Upsilon_y = \vec e_y \tilde\Pi_+ = \frac{i \vec e_x + \vec e_y}{2},
$$

and a general spinor in $\mathbb{B}\tilde\Pi_+$ is

$$
\psi = \psi_1\, \tilde\Pi_+ + \psi_2\, \vec\Upsilon_y, \qquad \psi_1,\psi_2 \in \mathbb{C}.
$$

The coordinate map $\psi\leftrightarrow(\psi_1,\psi_2)^{T}$ is an isomorphism of $\mathbb{B}$-modules: for every $\tilde{Q}\in\mathbb{B}$,

$$
\tilde{Q}\psi = \psi_1(\tilde{Q}\tilde\Pi_+) + \psi_2(\tilde{Q}y) \;\longleftrightarrow\; \mathsf{M}_2(\tilde{Q})\begin{pmatrix}\psi_1\\ \psi_2\end{pmatrix}.
$$

For example $\vec e_z \tilde\Pi_+ = -i \tilde\Pi_+$ and $\vec e_z \vec\Upsilon_y = i \vec\Upsilon_y$, matching $\mathsf{M}_2(\vec e_z) = \operatorname{diag}(-i,i)$; and $\vec e_x \tilde\Pi_+ = -i \vec\Upsilon_y$, matching the first column of $\mathsf{M}_2(\vec e_x)=-i\sigma_1$. The two minimal left ideals $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ are both isomorphic to $S$; the algebra is simple, so all its simple modules are isomorphic.

This ideal model is the precise sense in which "the spinor module lies inside $\mathbb{B}$": a spinor is an element of the algebra that lies in the minimal left ideal $\mathbb{B}\tilde\Pi_+$, and the algebra acts on it by left multiplication. It is not an arbitrary biquaternion.

## The Two Chiral Halves

The spinor module of the preceding sections carries the **defining representation** of $SL(2,\mathbb{C})$. In the classification of the companion article *The Lorentz Group in Biquaternionic Form — Structure and Representations*, this is the representation

$$
V_1 = \left(\tfrac{1}{2}, 0\right), \qquad \dim_{\mathbb{C}} V_1 = 2,
$$

the **left-handed Weyl spinor** module. Its complex conjugate

$$
\bar{S} = \overline{V_1} = \left(0, \tfrac{1}{2}\right), \qquad \dim_{\mathbb{C}}\bar{S} = 2,
$$

is the **right-handed Weyl spinor** module. These are the two **chiral halves**.

Concretely, both modules are carried by $\mathbb{C}^2$, but with different actions. If $\tilde U_{\mathrm L}\in SL(2,\mathbb{C})$ and $g = \mathsf{M}_2(\tilde U_{\mathrm L})$, then

$$
\text{left-handed:}\quad \psi \;\longmapsto\; g\,\psi,
\qquad\qquad
\text{right-handed:}\quad \chi \;\longmapsto\; \mathsf{M}_2(\tilde U_{\mathrm L}^{*})\,\chi,
$$

where $\tilde U_{\mathrm L}^{*}$ is the complex conjugate of the biquaternion (conjugation of its four coefficients). The second action is the conjugate of the first: since $\tilde U_{\mathrm L}\mapsto\tilde U_{\mathrm L}^{*}$ is an automorphism of $SL(2,\mathbb{C})$, the assignment is a genuine representation, and it is equivalent to the entrywise-conjugate action $g\mapsto\bar{g}$ (the two differ by conjugation with the invariant tensor $\epsilon$ introduced below). The chiral halves are exchanged by parity, and they are **not isomorphic** as complex representations of $SL(2,\mathbb{C})$.

Two cautions belong here, because they are often blurred.

**First, the two halves are not the two minimal left ideals.** The ideals $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ are both isomorphic to $S$ as left $\mathbb{B}$-modules: left multiplication by $\tilde U_{\mathrm L}$ acts by the **same** defining representation on each. The chirality distinction is therefore *not* visible to the complex algebra $\mathbb{B}$ alone, which is simple and has a single simple module. It becomes visible only when the real structure — complex conjugation — is taken into account, or when the algebra is complexified.

**Second, the chiral splitting appears in the complexification.** As a real algebra, the complexification of $\mathbb{B}$ splits:

$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B} \;\cong\; M_2(\mathbb{C}) \oplus M_2(\mathbb{C}),
$$

the two central summands being the two chiralities. The corresponding central idempotents are $\tfrac{1}{2}(1\pm i_{\mathbb{C}}\omega)$, with $\omega = \gamma^0\gamma^1\gamma^2\gamma^3$ the volume element; under the correspondence $\mathbb{B}\cong\mathrm{Cl}_{1,3}^{+}$ the volume element is the image of the biquaternion scalar imaginary, so these are the idempotents of the two chiral halves. This is the algebraic form of the statement that the odd part of the Clifford algebra, which is not contained in the even subalgebra $\mathbb{B}$, exchanges the two chiralities (Section *The Even Subalgebra and the Origin of the Action*).

The **Dirac spinor module** is the direct sum of the two halves,

$$
\boxed{\;\Delta = S \oplus \bar{S} = \left(\tfrac{1}{2},0\right)\oplus\left(0,\tfrac{1}{2}\right), \qquad \dim_{\mathbb{C}}\Delta = 4\;},
$$

on which $SL(2,\mathbb{C})$ acts block-diagonally by $g\oplus\mathsf{M}_2(\tilde U_{\mathrm L}^{*})$. Its four complex components are the four components of the Dirac spinor, and its two blocks are the left- and right-handed Weyl spinors. A biquaternion, regarded as a $2\times2$ matrix, may be read as a pair of column spinors, which is the sense in which the algebra itself displays a pair of Weyl spinors; the two columns are two copies of $S$, and it is the pairing of $S$ with its conjugate that constitutes the Dirac module.

## The Unit-Norm Biquaternions and the Double Cover

The group that acts is the group of **unit-norm biquaternions**,

$$
SL(2,\mathbb{C}) \;=\; \{\tilde U_{\mathrm L}\in\mathbb{B} : \tilde U_{\mathrm L}\tilde U_{\mathrm L}^{\natural} = e_t\},
$$

which under $\mathsf{M}_2$ is exactly $\{g\in GL_2(\mathbb{C}) : \det g = 1\}$, because the biquaternion norm is the determinant. It is a simply connected complex Lie group of complex dimension $3$ (real dimension $6$), with Lie algebra $\mathrm{SL}(2,\mathbb{C})$, the traceless $2\times2$ complex matrices.

The subgroups relevant to the series sit inside it as follows:

| Element | Characterization | Subspace |
|---|---|---|
| Pure boost $\tilde U_{\mathrm b} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ | Hermitian, unit norm | $\mathbb{M}_+$ |
| Pure rotation $\tilde u_{\mathrm r} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\vec u_{\mathrm r}$ | Real quaternion, unit norm | $\mathbb{H}_{\mathbb{B}}$ |
| General $\tilde U_{\mathrm L}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | Unit norm | $\mathbb{B}$ |

Pure boosts satisfy $\tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b}$; they do not form a subgroup (the product of two non-collinear boosts is a boost plus a rotation). Pure rotations form the subgroup $SU(2) = SL(2,\mathbb{C})\cap \mathrm{U}(2)$.

The action on the four-vector space is the conjugation map

$$
\pi:\; SL(2,\mathbb{C}) \longrightarrow SO^{+}(1,3), \qquad
\pi(\tilde U_{\mathrm L}):\; \tilde{Q} \;\longmapsto\; \tilde U_{\mathrm L}\,\tilde{Q}\,\tilde U_{\mathrm L}^{*}, \qquad \tilde{Q}\in\mathbb{M}_-.
$$

It is well defined (the image of an anti-Hermitian element is anti-Hermitian), it preserves the biquaternion norm, and it is a group homomorphism. Its kernel is

$$
\ker\pi = \{\pm e_t\} \cong \mathbb{Z}/2\mathbb{Z},
$$

since $-e_t$ is central, $(-\tilde U_{\mathrm L})\tilde{Q}(-\tilde U_{\mathrm L})^{*} = \tilde U_{\mathrm L}\tilde{Q}\tilde U_{\mathrm L}^{*}$ for every $\tilde{Q}$ (the two signs cancel). Hence $\pi$ is **two-to-one** onto the proper orthochronous Lorentz group,

$$
SO^{+}(1,3) \;\cong\; SL(2,\mathbb{C})/\{\pm e_t\},
$$

and $SL(2,\mathbb{C})$ is the **double cover** of the restricted Lorentz group.

The spinor action is by contrast **faithful**. On $S$, the element $-e_t$ acts as

$$
\mathsf{M}_2(-e_t) = -I_2,
$$

so $\pm\tilde U_{\mathrm L}$ act differently on every spinor. The defining representation therefore does **not** descend to $SO^{+}(1,3)$: it is a genuine representation of the double cover. This is the exact sense in which the spinor action and the four-vector action differ by the double cover.

## The Lorentz Action on the Spinor Module

### The Action

The Lorentz group acts on the spinor module by **left multiplication**:

$$
\boxed{\;\psi \;\longmapsto\; \tilde U_{\mathrm L}\,\psi \;=\; \mathsf{M}_2(\tilde U_{\mathrm L})\,\psi,
\qquad \tilde U_{\mathrm L}\in SL(2,\mathbb{C}),\quad \psi\in S\;}.
$$

Equivalently, in the ideal model, $\psi\in\mathbb{B}\tilde\Pi_+$ is sent to $\tilde U_{\mathrm L}\psi\in\mathbb{B}\tilde\Pi_+$; the ideal is stable because $\mathbb{B}(\mathbb{B}\tilde\Pi_+)\subseteq\mathbb{B}\tilde\Pi_+$. The action is $\mathbb{C}$-linear, and it is a group action:

$$
\tilde U_{\mathrm L,2}(\tilde U_{\mathrm L,1}\psi) = (\tilde U_{\mathrm L,2}\tilde U_{\mathrm L,1})\psi.
$$

No conjugation appears. This is the defining feature of the spinor representation.

### Boosts and Rotations Explicitly

For a boost along $\vec u_{\mathrm b}$ with rapidity $\psi$,

$$
\mathsf{M}_2(\tilde U_{\mathrm b}) = \cosh\frac{\psi}{2}\,I_2 + \sinh\frac{\psi}{2}\,\vec u_{\mathrm b}\cdot\boldsymbol{\sigma},
$$

as follows from $\mathsf{M}_2(i\vec u_{\mathrm b}) = \vec u_{\mathrm b}\cdot\boldsymbol{\sigma}$. For $\vec u_{\mathrm b} = \vec u_z$ this is the diagonal matrix $\operatorname{diag}(\exp(\psi/2),\exp(-\psi/2))$, which stretches one spinor component and contracts the other. For a rotation about $\vec u_{\mathrm r}$ by angle $\theta$,

$$
\mathsf{M}_2(\tilde u_{\mathrm r}) = \cos\frac{\theta}{2}\,I_2 - i\sin\frac{\theta}{2}\,\vec u_{\mathrm r}\cdot\boldsymbol{\sigma},
$$

the standard $SU(2)$ rotation matrix. A rotation by $2\pi$ sends $\mathsf{M}_2(\tilde u_{\mathrm r})$ to $-I_2$: it is the identity in the four-vector representation but not on the spinor module. A rotation by $4\pi$ is the identity on both.

### The Infinitesimal Action

Differentiating at the identity gives the action of the Lie algebra. The generators of $SL(2,\mathbb{C})$ are the traceless matrices, and in the biquaternion basis

$$
\mathrm{SL}(2,\mathbb{C}) = \operatorname{span}_{\mathbb{R}}\{\,\vec e_x,\vec e_y,\vec e_z\,\} \;\oplus\; \operatorname{span}_{\mathbb{R}}\{\,i\vec e_x,i\vec e_y,i\vec e_z\,\},
$$

the first summand being the rotations (the compact subalgebra $\mathrm{SU}(2)\cong\mathrm{SO}(3)$ and $\mathbb{H}_{\mathbb{B}}$) and the second the boosts (the non-compact part, in $\mathbb{M}_+$). Under $\mathsf{M}_2$,

$$
\vec e_\mu \longmapsto -i\sigma_\mu, \qquad i \vec e_\mu \longmapsto \sigma_\mu,
$$

so the anti-Hermitian generators $-i\sigma_k$ and the Hermitian generators $\sigma_k$ both act on $S$ by matrix multiplication. On the spinor module the infinitesimal generators act as the Pauli matrices and their multiples, which is the familiar statement that the spin-$\frac{1}{2}$ representation is the fundamental representation of $\mathrm{SL}(2,\mathbb{C})$.

The **compact subgroup** $SU(2)\subset SL(2,\mathbb{C})$ consists of the unit-norm biquaternions with real vector part (the unit quaternions), for which $\tilde u_{\mathrm r}^{*}\tilde u_{\mathrm r} = e_t$. Its action on $S$ is unitary with respect to the Hermitian inner product $\langle\psi,\phi\rangle = \psi^\dagger\phi$, and it is the double cover of the spatial rotation group $SO(3)$. The boosts, by contrast, are not unitary, and they do not preserve that inner product; this is the representation-theoretic expression of the non-compactness of the Lorentz group.

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

The form $\varepsilon$ is a nondegenerate **invariant bilinear form** on $S$. It identifies $S$ with its dual, $S^{*}\cong S$: the defining module is **self-dual**. This is the spinor metric behind the invariant antisymmetric contraction of a pair of left-handed spinors. Self-duality is not self-conjugacy: $S^{*}\cong S$, but $\bar{S}\not\cong S$.

### The Hermitian Form

The Hermitian inner product

$$
h(\psi,\phi) = \psi^{\dagger}\phi = \psi_1^{*}\phi_1 + \psi_2^{*}\phi_2
$$

is positive definite, but it is **not** invariant under all of $SL(2,\mathbb{C})$:

$$
h(g\psi, g\phi) = \psi^{\dagger} g^{*} g\,\phi.
$$

It is invariant exactly when $g^{*}g = I_2$, i.e. on the compact subgroup $SU(2)$. For a boost, $g^{*}g\neq I_2$, and $h$ is not preserved. The hermitian form therefore selects the maximal compact subgroup; it does not define a Lorentz-invariant structure on a single chiral half.

### The Mixed Pairing

There is, however, an invariant pairing between the two chiral halves. Let $\psi\in S$ transform as $\psi\mapsto g\psi$ and let $\chi\in\bar{S}$ transform as $\chi\mapsto\mathsf{M}_2(\tilde U_{\mathrm L}^{*})\chi$. Then the sesquilinear pairing

$$
\mathfrak{b}(\psi,\chi) = \psi^{\dagger}\chi
$$

is invariant. Indeed,

$$
b(g\psi,\, \mathsf{M}_2(\tilde U_{\mathrm L}^{*})\chi)
= \psi^{\dagger}\, \mathsf{M}_2(\tilde U_{\mathrm L})^{\dagger}\,\mathsf{M}_2(\tilde U_{\mathrm L}^{*})\,\chi
= \psi^{\dagger}\,\mathsf{M}_2\!\left(\tilde U_{\mathrm L}^{*}\tilde U_{\mathrm L}^{*}\right)\chi
= \psi^{\dagger}\chi,
$$

because $\tilde U_{\mathrm L}^{*}\tilde U_{\mathrm L}^{*} = (\tilde U_{\mathrm L}^{\natural}\tilde U_{\mathrm L})^{*} = e_t^{*} = e_t$ for a unit-norm biquaternion. This mixed pairing is the invariant scalar bilinear of the Dirac spinor; it pairs a left-handed spinor with a right-handed one.

### The Spinor-to-Vector Map

Finally, the outer product of a spinor with its conjugate lands in the algebra. For $u,v\in S$, the matrix

$$
\tilde{Q} = u\,v^{\dagger} \;\in\; M_2(\mathbb{C}) \;\cong\; \mathbb{B}
$$

is a rank-one element of the algebra, and under the Lorentz action $u\mapsto gu$ on the first spinor and the conjugate (right-handed) entry $v^{\dagger}\mapsto v^{\dagger}g^{*}$ it transforms as

$$
\tilde{Q} = u\,v^{\dagger} \;\longmapsto\; (gu)(gv)^{*} = g\,\tilde{Q}\,g^{*}.
$$

This is exactly the transformation law of the **rotor conjugation** on the material sector. It must be read as a statement about the equivariance of the whole algebra $M_2(\mathbb{C})$, however, and not as the vector representation itself; two cautions are in order. First, the real span of the outer products $u v^{\dagger}$ as $u$ and $v$ range over $S$ is all of $M_2(\mathbb{C})$, of real dimension $8$, not the Hermitian subspace of real dimension $4$: the matrices $E_{12}$ and $iE_{12}$ are each a single outer product, realized by $u = \vec e_x$, $v = \vec e_y$ and by $u = \vec e_x$, $v = -i\vec e_y$ respectively, and they are independent over the reals. Second, $u v^{\dagger}$ is Hermitian **only** when the two spinors are proportional by a real factor, $v = \lambda u$ with $\lambda \in \mathbb{R}$; for a generic pair $i\,uv^{\dagger}$ does not lie in $\mathbb{M}_-$ at all, and is therefore not a four-vector.

The Hermitian subspace $\mathbb{M}_+$ is the **real** span of the self-pair products $u\,u^{\dagger}$, of real dimension $4$. For a general pair the object that transforms as a four-vector is the symmetrised product

$$
H = \tfrac{1}{2}\left(u\,v^{\dagger} + v\,u^{\dagger}\right) \;\in\; \mathbb{M}_+,
\qquad
V = iH \;\in\; \mathbb{M}_-,
$$

which is Hermitian for every pair and reduces to the outer product $u\,u^{\dagger}$ when $v = u$. The four-vector associated with the spinor pair is thus $iH$, which replaces the outer product $i\,uv^{\dagger}$ and agrees with it when the pair is (anti)parallel (up to the conventions of the $ict'$ description). The map $S\otimes\bar{S}\to\mathbb{B}$, $u\otimes v^{\dagger}\mapsto uv^{\dagger}$, is an isomorphism of $SL(2,\mathbb{C})$-representations onto the algebra, while the four-vector representation is the real form of it carried by the Hermitian slice, and it realizes the vector representation as the tensor product of the two chiral halves,

$$
\left(\tfrac{1}{2},\tfrac{1}{2}\right) = \left(\tfrac{1}{2},0\right)\otimes\left(0,\tfrac{1}{2}\right).
$$

This is the algebraic link between the one-sided spinor action and the two-sided four-vector action, and its algebra-level form is the Hermitian form $\tilde{Q}\tilde{Q}^{*}\in\mathbb{M}_+$ of the companion articles.

The transformation laws are collected in the following table.

| Pairing | Domain | Transformation | Invariance |
|---|---|---|---|
| $\varepsilon(\psi,\phi) = \psi^{T}\epsilon\phi$ | $S\times S\to\mathbb{C}$ | invariant | $g^{T}\epsilon g = \epsilon$ |
| $h(\psi,\phi) = \psi^{\dagger}\phi$ | $S\times S\to\mathbb{C}$ | $\psi^{\dagger}g^{*}g\,\phi$ | invariant iff $g\in SU(2)$ |
| $\mathfrak{b}(\psi,\chi) = \psi^{\dagger}\chi$ | $S\times\bar{S}\to\mathbb{C}$ | invariant | $\tilde U_{\mathrm L}^{*}\tilde U_{\mathrm L}^{*}=e_t$ |
| $\tilde{Q} = u\,v^{\dagger}$ | $S\times\bar{S}\to\mathbb{B}$ | $g\,\tilde{Q}\,g^{*}$ | equivariant |
| $H = \tfrac{1}{2}(uv^{\dagger}+vu^{\dagger})$ | $S\times\bar{S}\to\mathbb{M}_+$ | $g\,H\,g^{*}$ | Hermitian; four-vector is $iH$ |

### The Indefinite Pairing and the Hyperboloids

The pairings above are invariant under the full $SL(2,\mathbb{C})$ or under its maximal compact subgroup. A third pairing, indefinite rather than definite, is invariant exactly under the rank-one subgroup $SU(1,1)\cong SL(2,\mathbb{R})\cong Sp(2,\mathbb{R})$ — the double cover of $SO(1,2)$ and the dynamical group of the oscillator's squeezings — and it is the one that models the hyperboloids of three-dimensional Minkowski space on the same module.

**The indefinite pairing.** With the Pauli matrices of the matrix realisation $\mathsf{M}_2(\vec e_\mu)=-i\sigma_\mu$ established above, put
$$
[u|v]=u^{\dagger}\sigma_3v=\bar u_xv_1-\bar u_yv_2 .
$$
This form is Hermitian of signature $(1,1)$; it is **not** invariant under all of $SL(2,\mathbb{C})$, and its isometry group inside $SL(2,\mathbb{C})$ is exactly $SU(1,1)$. Unlike the definite form $h$ it selects the non-compact subgroup, and unlike $\varepsilon$ it is Hermitian rather than alternating. The pair $(h,[\,\cdot\,|\,\cdot\,])$ is the pair (definite, indefinite) whose invariance groups are the two real forms $SU(2)$ and $SU(1,1)$ of the same complex group.

**The vector maps.** Let
$$
\varsigma=(\sigma_3,\,i\sigma_2,\,-i\sigma_1)=\sigma_3(1,\sigma_1,\sigma_2),
$$
a Hermitian triple satisfying $\varsigma^i\varsigma^j=\eta^{ij}-i\varepsilon^{ijk}\eta_{kl}\varsigma^l$ with $\eta=\mathrm{diag}(1,-1,-1)$ — the analogue for $SU(1,1)$ of the quaternion relations for $SU(2)$; both this identity and the Hermiticity of $\sigma_3\varsigma^i$ were verified here. The three homogeneous spaces are then modelled on spinors of the module:
$$
v^i=\langle z|\sigma^i|z\rangle\ \ (S^2),\qquad
v^i=\tfrac12\,\langle z|\sigma_3\varsigma^i|z\rangle\ \ (H^\pm),\qquad
v^i=\langle z_2|\sigma_3\varsigma^i|z_1\rangle\ \ (H^{sl}),
$$
where $\langle z|(\,\cdot\,)|z\rangle$ abbreviates $z^{\dagger}(\,\cdot\,)z$. The first is the pure-state correspondence of the Bloch-ball article — one Weyl spinor with the definite pairing gives the sphere, with $|v|^2=1$ — and the second uses one Weyl spinor with the indefinite pairing and gives the two-sheeted time-like hyperboloid $H^\pm\subset\mathbb{R}^{1,2}$. The third uses a **pair** of spinors and gives the one-sheeted hyperboloid $H^{sl}$, and it is here that the Majorana condition enters: a real structure commuting with $SU(1,1)$ takes the place of the complex conjugation of the other two cases. The reason the one-sheeted case takes a pair, in the external interpretation cited below, is that a single Weyl spinor with either pairing forces one sign of the area spectrum, and only the pair carries the sign a time-like surface needs.

**The closure.** Under the symplectic form
$$
\omega=i\,\sigma_3^{ij}\,dz_i\wedge dz_j
$$
on the doubled spinor space $\mathbb{C}^2\oplus\bar{\mathbb{C}}^2$ — the pairing that makes the coordinates of the two factors conjugate to one another, and a different form from the invariant $\varepsilon$ above — the bilinears close into the Poisson algebra of $\mathfrak{so}(1,2)\cong\mathfrak{su}(1,1)$, displayed in the source as
$$
\{v^i,v^j\}=-\varepsilon^{ijk}\eta_{kl}v^l ,
$$
where the overall sign is the conventional one for $\omega$. This was recomputed here on generic elements: the brackets of the three bilinears reproduce the structure constants, so the map $z\mapsto v(z)$ is a moment-map-like realisation of the Lie algebra on the spinor space, not merely an equivariant map to the vectors. Its use in the spinfoam programme — the area-constrained symplectomorphism to $T^*SU(1,1)$ — is recorded in *Quantum Gravity under the Biquaternion Framework — A Research Agenda*.

## Spinor Action Versus Rotor Conjugation

It is worth stating the contrast in one place, since it is the conceptual centre of the article.

| Feature | Four-vector action on $\mathbb{M}_-$ | Spinor action on $S$ |
|---|---|---|
| Formula | $\tilde{Q}\mapsto\tilde U_{\mathrm L}\tilde{Q}\tilde U_{\mathrm L}^{*}$ | $\psi\mapsto\tilde U_{\mathrm L}\psi$ |
| Number of factors of $\tilde U_{\mathrm L}$ | two (quadratic) | one (linear) |
| Kernel of the action | $\{\pm e_t\}$ | $\{e_t\}$ |
| Image group | $SO^{+}(1,3)$ | $SL(2,\mathbb{C})$ |
| Action of $-e_t$ | $+\mathrm{id}$ | $-\mathrm{id}$ |
| Descends to the Lorentz group? | yes | no |

The two actions do not "differ by the double cover" in the sense that one is a cover of the other; rather, the four-vector action **factors through** the double cover while the spinor action does not. The conjugate parameter $\tilde U_{\mathrm L}$ and $-\tilde U_{\mathrm L}$ describe the same Lorentz transformation of every four-vector, but opposite transformations of every spinor. For this reason the spinor representation is the representation of the **double cover** $SL(2,\mathbb{C})$, and the sign of the spinor is a genuine degree of freedom that no four-vector can see. The relation between the two actions is the bilinear map $\tilde{Q} = u v^{\dagger}$ of the preceding section: the four-vector is a *pair* of spinors, and the two one-sided actions on the pair combine into the two-sided action on their product.

A concrete illustration is the composition of two transformations. If $\tilde U_{\mathrm L,1}$ and $\tilde U_{\mathrm L,2}$ are rotors, then on four-vectors

$$
\tilde U_{\mathrm L,2}(\tilde U_{\mathrm L,1}\tilde{Q}\tilde U_{\mathrm L,1}^{*})\tilde U_{\mathrm L,2}^{*} = (\tilde U_{\mathrm L,2}\tilde U_{\mathrm L,1})\tilde{Q}(\tilde U_{\mathrm L,2}\tilde U_{\mathrm L,1})^{*},
$$

while on spinors

$$
\tilde U_{\mathrm L,2}(\tilde U_{\mathrm L,1}\psi) = (\tilde U_{\mathrm L,2}\tilde U_{\mathrm L,1})\psi.
$$

Both compose by multiplication of the rotors; the difference is only that the four-vector formula has a pair of rotors, and hence a sign that cancels, while the spinor formula has one, and hence a sign that does not.

## The Even Subalgebra and the Origin of the Action

The reason the spinor action is one-sided, and the four-vector action two-sided, is the place of $\mathbb{B}$ in the Clifford algebra. As in the companion article on the Dirac equation, $\mathbb{B}$ is isomorphic, as a real algebra, to the **even subalgebra** of $\mathrm{Cl}_{1,3}$:

$$
\mathbb{B} \;\cong\; \mathrm{Cl}_{1,3}^{+}(\mathbb{R}),
\qquad
\vec e_x\mapsto\gamma^2\gamma^3,\quad \vec e_y\mapsto\gamma^3\gamma^1,\quad \vec e_z\mapsto\gamma^2\gamma^1,\quad i\mapsto\gamma^0\gamma^1\gamma^2\gamma^3 .
$$

The full Clifford algebra acts on its spinor module by **left multiplication**; restricting to the even subalgebra $\mathbb{B}$ gives the action considered in this article. The spin group sits inside the even subalgebra,

$$
\operatorname{Spin}(1,3) \;\cong\; SL(2,\mathbb{C}) \;\subset\; \mathbb{B} \;\subset\; \mathrm{Cl}_{1,3}.
$$

Two distinct actions are then visible in the Clifford picture. The spin group acts on the spinor module by left multiplication — one-sided, because a Clifford module is a module and the action is linear. The same group acts on the vector space $W\subset\mathrm{Cl}_{1,3}$ (spanned by the odd generators) by a **two-sided conjugation** — the signed inner conjugation, $v\mapsto\tilde U_{\mathrm L}v\tilde U_{\mathrm L}^{-1}$, written in the read-list conventions as the rotor conjugation $\tilde{Q}\mapsto\tilde U_{\mathrm L}\tilde{Q}\tilde U_{\mathrm L}^{*}$ — which is two-sided because a vector is being conjugated inside the algebra. The vector representation is the tensor product of the spinor representation with its conjugate in the sense of the preceding section; the even subalgebra is exactly the algebra generated by the bivectors, and the bivectors are the Lie algebra of the spin group.

This correspondence between the biquaternion algebra and the even Clifford subalgebra is the algebraic origin of the whole structure. It explains at once:

1. why a spinor transforms one-sidedly (it is an element of a Clifford module, and modules are acted on linearly);
2. why a four-vector transforms two-sidedly (it is an element of the odd part, acted on by signed inner conjugation);
3. why $-e_t$ acts as $-\mathrm{id}$ on spinors but trivially on four-vectors (a single factor of the central unit versus two);
4. why the two chiralities are not visible to the complex algebra $\mathbb{B}$ but appear on complexification: the chirality operator $\gamma_5 = i_{\mathbb{C}}\omega$ (the scalar imaginary of the complexified Clifford algebra times the volume element $\omega$) is not an element of the even subalgebra, and it anticommutes with the generators; the odd part therefore exchanges the two half-spin modules, while the even part $\mathbb{B}$ preserves them. The complexified even algebra splits accordingly,
$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B} \cong M_2(\mathbb{C})\oplus M_2(\mathbb{C}),
$$
with the two summands the two chiral halves.

In this interpretation the spinor module is not an add-on to the biquaternion framework; it is the module that the framework was built to carry, and the material and informational sectors are its bilinear and operator shadows.

## Open Questions

1. **The spinor module and the informational sector.** The article on $\mathbb{M}_+$ interprets the Hermitian subspace as the observables of a qubit. The spinor module developed here is the representation space on which those operators act. The precise relation between the qubit states of the informational sector and the Weyl spinors of the Lorentz group — whether they are the same module under different real structures — is not settled here.
2. **The covariance of the biquaternion Dirac equation.** The companion article on the Dirac equation formulates the equation as the linear chiral pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ but leaves open the transformation law of the biquaternion-valued field $\tilde{\Psi}$.

A natural candidate is the module action defined here; its compatibility with the mass term requires the relationship between the one-sided action and the conjugate module to be fixed by a convention.
3. **The biquaternion form of the symplectic pairing.** The invariant form $\varepsilon$ is presented here in matrix coordinates. Its expression as a bigeneral quaternionic bilinear on the ideal $\mathbb{B}\tilde\Pi_+$ follows from the coordinate map, but the cleanest biquaternion formula is a matter of convention.
4. **Majorana and reality conditions.** In Lorentzian signature the Dirac module is self-conjugate but the two Weyl halves are a conjugate pair, so Majorana spinors exist while Majorana–Weyl spinors do not. How these reality conditions read as conditions on biquaternion-valued fields is a natural continuation.
5. **Curved spacetime.** The module and its action are pointwise algebraic. Whether the spinor module globalizes to a bundle over a curved biquaternionic background is open, in parallel with the open questions of the companion articles.
6. **The indefinite pairing and the framework's own interpretation.** The pairing $[u|v]=u^{\dagger}\sigma_3v$, the triple $\varsigma$ and the hyperboloid models come from the external interpretation cited in *Quantum Gravity under the Biquaternion Framework — A Research Agenda*. Whether the framework gives them an independent meaning — in particular whether the Majorana pair of the one-sheeted case is the module real structure of *The Neutrino and Majorana Fermions in Biquaternionic Form* — is not settled here, and the two articles are consistent but not yet joined.

## Summary

The biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has a unique simple module, the two-dimensional complex **spinor module** $S=\mathbb{C}^2$, on which $\mathbb{B}$ acts by matrix multiplication. Inside the algebra, $S$ is realized as the minimal left ideal $\mathbb{B}\tilde\Pi_+$, $\tilde\Pi_+ = \tfrac{1}{2}(e_t+i\vec e_z)$, whose elements are the spinors; the algebra acts by left multiplication, and the action is one-sided.

The **left-handed Weyl spinor** is the defining module $(\tfrac12,0)$; the **right-handed Weyl spinor** is its complex conjugate $(0,\tfrac12)$. These are the two **chiral halves**; their direct sum is the four-component Dirac spinor module. The two halves are not isomorphic as complex representations of $SL(2,\mathbb{C})$ (they are conjugate to one another), and the chirality distinction is a real-structure distinction that appears on complexification, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$.

The group of unit-norm biquaternions is $SL(2,\mathbb{C})$, the double cover of the restricted Lorentz group $SO^{+}(1,3)$. It acts on the spinor module by

$$
\psi \longmapsto \tilde U_{\mathrm L}\psi,
\qquad \tilde U_{\mathrm L}\in SL(2,\mathbb{C}),\quad \psi\in S,
$$

with $\pm\tilde U_{\mathrm L}$ acting differently ($-e_t$ acts as $-\mathrm{id}$). The four-vector action of the companion articles, $\tilde{Q}\mapsto\tilde U_{\mathrm L}\tilde{Q}\tilde U_{\mathrm L}^{*}$ on $\mathbb{M}_-$, is recovered from the Hermitian part of the spinor bilinear, $H = \tfrac{1}{2}(uv^{\dagger}+vu^{\dagger})$, which transforms as $gHg^{\dagger}$ and whose four-vector image is $iH$. The spinor action is faithful and does not descend to the Lorentz group; the four-vector action has kernel $\{\pm e_t\}$ and does. This is the double cover, seen from the module side.

The spinor module carries three bilinear structures and one equivariant bilinear map: the symplectic form $\varepsilon$ (invariant, and the source of self-duality $S^{*}\cong S$), the Hermitian form $h$ (invariant only on the compact subgroup $SU(2)$), the mixed pairing $b:S\times\bar{S}\to\mathbb{C}$ (invariant, the Dirac scalar bilinear), and the outer product $S\times\bar{S}\to\mathbb{B}$, whose Hermitian part $H$ carries the vector representation. A fourth pairing, the indefinite $[u|v]=u^{\dagger}\sigma_3v$ of signature $(1,1)$, is invariant exactly under the subgroup $SU(1,1)\cong SL(2,\mathbb{R})\cong Sp(2,\mathbb{R})$ that fixes a space-like direction, and its bilinears model the sphere $S^2$ and the two hyperboloids $H^\pm$, $H^{sl}$ of three-dimensional Minkowski space on the module; under the symplectic form $\omega$ they close into $\mathfrak{so}(1,2)\cong\mathfrak{su}(1,1)$.

The algebraic origin of the one-sided spinor action and the two-sided four-vector action is the identification $\mathbb{B}\cong\mathrm{Cl}_{1,3}^{+}$: the spin group lies in the even subalgebra and acts on a Clifford module by left multiplication, while it acts on the odd part by signed inner conjugation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^2=-e_t$, $\vec e_x \vec e_y=\vec e_z$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | Matrix realization, $\mathsf{M}_2(\vec e_\mu)=-i\sigma_\mu$ |
| $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \det\mathsf{M}_2(\tilde{Q})$ | Biquaternion norm |
| $S = \mathbb{C}^2$ | Spinor module (unique simple module), $\dim_{\mathbb{C}}S=2$ |
| $V_1 = (\tfrac12,0)$ | Left-handed Weyl (defining) representation |
| $\bar{S} = \overline{V_1} = (0,\tfrac12)$ | Right-handed Weyl (conjugate) representation |
| $\Delta = S\oplus\bar{S}$ | Dirac spinor module, $\dim_{\mathbb{C}}\Delta=4$ |
| $\tilde\Pi_+ = \tfrac12(e_t+i\vec e_z),\ \tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$ | Primitive orthogonal idempotents, $\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-$ |
| $\vec\Upsilon_x = \tfrac12(i\vec e_x-\vec e_y),\ \vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)=\vec e_y\tilde\Pi_+$ | Matrix units $E_{12},E_{21}$; basis $\{\tilde\Pi_+,\vec\Upsilon_y\}$ of $S$ |
| $SL(2,\mathbb{C}) = \{\tilde U_{\mathrm L}:\tilde U_{\mathrm L}\tilde U_{\mathrm L}^{\natural}=e_t\}$ | Unit-norm biquaternions, double cover of $SO^{+}(1,3)$ |
| $\tilde U_{\mathrm b} = \cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ | Boost rotor (Hermitian, in $\mathbb{M}_+$) |
| $\tilde u_{\mathrm r} = \cos\frac{\theta}{2}+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ | Rotation rotor (in $\mathbb{H}_{\mathbb{B}}$) |
| $\psi\mapsto\tilde U_{\mathrm L}\psi$ | Lorentz action on the spinor module |
| $\varepsilon(\psi,\phi)=\psi^{T}\epsilon\phi$ | Invariant symplectic pairing on $S$ |
| $h(\psi,\phi)=\psi^{\dagger}\phi$ | Hermitian form (invariant on $SU(2)$) |
| $\mathfrak{b}(\psi,\chi)=\psi^{\dagger}\chi$ | Invariant pairing $S\times\bar{S}\to\mathbb{C}$ |
| $H = \tfrac{1}{2}(uv^{\dagger}+vu^{\dagger})\mapsto gHg^{\dagger}$ | Spinor bilinear; four-vector is $iH$ |
| $\mathbb{B}\cong\mathrm{Cl}_{1,3}^{+}$ | Even Clifford subalgebra correspondence |
| $[u|v]=u^{\dagger}\sigma_3v$ | Indefinite $SU(1,1)$-invariant pairing, signature $(1,1)$ |
| $SU(1,1)\cong SL(2,\mathbb{R})\cong Sp(2,\mathbb{R})$ | Isometry group of the indefinite pairing; double cover of $SO(1,2)$ |
| $\varsigma=(\sigma_3,i\sigma_2,-i\sigma_1)$ | Hermitian triple; $\varsigma^i\varsigma^j=\eta^{ij}-i\varepsilon^{ijk}\eta_{kl}\varsigma^l$ |
| $S^2$, $H^\pm$, $H^{sl}$ | Sphere and the two hyperboloids modelled on the module |
| $\omega=i\sigma_3^{ij}dz_i\wedge dz_j$ | Symplectic form on the doubled spinor space; $\{v^i,v^j\}=-\varepsilon^{ijk}\eta_{kl}v^l$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the standard two-component spinor calculus, the invariant $\epsilon$-form, and the Weyl spinors.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford-algebra construction of spinors as minimal left ideals and the double cover of the Lorentz group.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of the Lorentz group and the relation between spinors and four-vectors.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of spinors and Lorentz transformations in the even subalgebra.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original spinor representation of the electron.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the representation theory of the Lorentz group and the construction of the Dirac spinor from two Weyl spinors.
- Julius Wess and Jonathan Bagger, *Supersymmetry and Supergravity* (Princeton, 1992), for the two-component spinor conventions.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the modules of $M_2(\mathbb{C})$, the highest-weight classification, and the Clebsch–Gordan rule.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for simple modules, Schur's lemma, and the structure of matrix algebras.
- J. D. Simão, "Biquaternions, Majorana spinors and time-like spin-foams," arXiv:2401.10324 [gr-qc] (2024), for the indefinite pairing $[u|v]$, the $\varsigma$ triple, the Weyl- and Majorana-spinor models of $S^2$, $H^\pm$ and $H^{sl}$, the symplectic form $\omega$ and the $\mathfrak{su}(1,1)$ closure of the bilinears. External; cited for the pairing and the bilinears only.
