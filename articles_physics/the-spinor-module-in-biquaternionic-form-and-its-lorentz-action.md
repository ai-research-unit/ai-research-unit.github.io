# __The Spinor Module in Biquaternionic Form and Its Lorentz Action__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has been read, in the companion articles, in two ways. The article [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) identifies the anti-Hermitian subspace $\mathbb{M}_-$ with Minkowski space: the four-vectors of relativistic physics live in $\mathbb{M}_-$, and the Lorentz group acts on them by the **Hermitian sandwich** with $\tilde U^{\mathrm{lor}}$, the unit-norm biquaternion that implements the Lorentz transformation,

$$
\tilde{Q} \;\longmapsto\; \tilde U^{\mathrm{lor}}\,\tilde{Q}\,\tilde U^{\mathrm{lor}}{}^{*}.
$$

The article [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) identifies the Hermitian subspace $\mathbb{M}_+$ with the observables of a two-state system, whose products generate its operator algebra. Both accounts rest on a more primitive representation-theoretic fact: $\mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$, so it has a two-dimensional complex module, and the Lorentz group acts on that module by **multiplication**. This module is the **spinor module**. It is the subject of the present article.

The two actions are different in kind. The four-vector action is two-sided — it is a Hermitian sandwich — while the spinor action is one-sided. The difference is not an accident of notation. It is the algebraic origin of the double cover: the element $-e_t$ of $SL(2,\mathbb{C})$ acts trivially by the Hermitian sandwich on $\mathbb{M}_-$, but it acts as $-\mathrm{id}$ on the spinor module. Consequently the four-vector representation descends to the Lorentz group, while the spinor representation does not: the spinor is a genuine representation of the double cover.

The article is written in the **cell algebra**. A **cell** is the two-sided multiplier

$$
L_aR_b:\ X\;\longmapsto\; aXb,
\qquad L_a=L_aR_{e_t}^{\mathrm{axf}},\quad R_b=L_{e_t}^{\mathrm{axf}}R_b,
$$

and two cells compose by $L_aR_b\,L_cR_d=L_{ac}R_{db}$, the right factors in reverse order. The spinor action of the Lorentz group is the **one-sided cell** $L_{\tilde U}$; the four-vector action is the **two-sided cell**

$$
\Theta_{\tilde U}=L_{\tilde U}R_{\tilde U^{*}},
\qquad
\Theta_{\tilde U}(\tilde{Q})=\tilde U\,\tilde{Q}\,\tilde U^{*}.
$$

In the operator symbols the Lorentz label is suppressed, $L_{\tilde U}:=L_{\tilde U^{\mathrm{lor}}}$ and $R_{\tilde U^{*}}:=R_{\tilde U^{\mathrm{lor}}{}^{*}}$. The $2\times2$ matrices $\mathsf{M}_2$ are the frame in which the one-sided action on the simple module is computed, and the five gamma matrices are a frame of the cell algebra on the regular module, displayed once in §*The Legacy Gamma Formulation*. No gamma symbol appears in the body of the article.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_k^2 = -e_t$ and $\vec e_x \vec e_y = \vec e_z$ cyclically, and the scalar imaginary is $i$, with $i^2=-1$. The conjugations are the quaternion conjugate $\tilde{Q}^{\natural}$, the coefficientwise complex conjugate $\bar{\tilde{Q}}$, and the Hermitian conjugate $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$. The anti-Hermitian and Hermitian subspaces are

$$
\mathbb{M}_- = \{\tilde{Q} : \tilde{Q}^{*} = -\tilde{Q}\}, \qquad \mathbb{M}_+ = \{\tilde{Q} : \tilde{Q}^{*} = \tilde{Q}\},
$$

and $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace, the fixed-point set of complex conjugation. The material sector is $\mathbb{M}_-$ and the informational sector is $\mathbb{M}_+$.

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
Q_t - iQ_z & -iQ_x - Q_y\\[2pt]
-iQ_x + Q_y & Q_t + iQ_z
\end{pmatrix},
\qquad
\mathsf{M}_2(e_t) = I_2,\quad \mathsf{M}_2(\vec e_k) = -i\sigma_k,\quad \mathsf{M}_2(i) = i I_2,
$$

where $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices and, as in the companion article [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), the $i$ on the right is the standard imaginary unit of $\mathbb{C}\subset M_2(\mathbb{C})$ (the image of the scalar imaginary of $\mathbb{B}$). Under this convention $i \vec e_k$ corresponds to $\sigma_k$, and the quaternion relations $\vec e_x\vec e_y=\vec e_z$ hold on both sides. Two properties of $\mathsf{M}_2$ are used repeatedly:

$$
\mathsf{M}_2(\tilde{Q}\tilde Q_1) = \mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde Q_1), \qquad
\det\mathsf{M}_2(\tilde{Q}) = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 = \langle\tilde{Q}\rangle_{\natural},
$$

so that the **biquaternion norm** of $\mathbb{B}$ is the determinant. The isomorphism also intertwines Hermitian conjugation with the conjugate transpose,

$$
\mathsf{M}_2(\tilde{Q}^{*}) = \mathsf{M}_2(\tilde{Q})^{\dagger},
$$

where the ${}^{\dagger}$ on the right is the matrix conjugate transpose; this is the only sense in which the dagger is written on a matrix in this article, the star being reserved for the Hermitian conjugation of the algebra. In particular $\mathbb{M}_-$ corresponds to the anti-Hermitian matrices and $\mathbb{M}_+$ to the Hermitian matrices.

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

Writing a spinor as a column vector, the action of a general biquaternion is the one-sided cell $L_{\tilde Q}$,

$$
\psi \;\longmapsto\; L_{\tilde Q}\psi=\mathsf{M}_2(\tilde{Q})\,\psi
=
\begin{pmatrix}
(Q_t - iQ_z)\psi_1 + (-iQ_x - Q_y)\psi_2\\[2pt]
(-iQ_x + Q_y)\psi_1 + (Q_t + iQ_z)\psi_2
\end{pmatrix}.
$$

The action is $\mathbb{C}$-linear in $\psi$ and compatible with the algebra product,

$$
L_{\tilde Q}L_{\tilde Q_1}=L_{\tilde Q\tilde Q_1},
\qquad
\mathsf{M}_2(\tilde{Q})(\mathsf{M}_2(\tilde Q_1)\psi) = \mathsf{M}_2(\tilde{Q}\tilde Q_1)\psi;
$$

this compatibility is the module structure. The algebra is exactly the algebra of all $\mathbb{C}$-linear endomorphisms of $S$: $\mathbb{B}\cong\operatorname{End}_{\mathbb{C}}(S)$.

## The Spinor Module as a Left Ideal

The module $S$ can be exhibited **inside** the algebra, which is often the most convenient realization. Let

$$
\tilde\Pi_+ = \frac{e_t + i \vec e_z}{2}, \qquad \tilde\Pi_- = \frac{e_t - i \vec e_z}{2}.
$$

Here $i\vec e_z$ is a root of $+1$, because $(i\vec e_z)^2=i^2\vec e_z^2=(-1)(-e_t)=e_t$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents. These satisfy

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
E_{11} = \tilde\Pi_+,\quad E_{12} = \vec\Upsilon_x,\quad E_{21} = \vec\Upsilon_y,\quad E_{22} = \tilde\Pi_-,
$$

$$
\tilde\Pi_+\vec\Upsilon_x = \vec\Upsilon_x = \vec\Upsilon_x \tilde\Pi_-,
\qquad
\tilde\Pi_-\vec\Upsilon_y = \vec\Upsilon_y = \vec\Upsilon_y \tilde\Pi_+,
$$

$$
\vec\Upsilon_x\vec\Upsilon_y = \tilde\Pi_+,
\qquad
\vec\Upsilon_y\vec\Upsilon_x = \tilde\Pi_-.
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
\tilde{Q}\psi = \psi_1(\tilde{Q}\tilde\Pi_+) + \psi_2(\tilde{Q}\vec\Upsilon_y) \;\longleftrightarrow\; \mathsf{M}_2(\tilde{Q})\begin{pmatrix}\psi_1\\ \psi_2\end{pmatrix}.
$$

The action is the one-sided cell $L_{\tilde Q}$; no right multiplication acts on the left module $S$. For example $\vec e_z \tilde\Pi_+ = -i \tilde\Pi_+$ and $\vec e_z \vec\Upsilon_y = i \vec\Upsilon_y$, matching $\mathsf{M}_2(\vec e_z) = \operatorname{diag}(-i,i)$; and $\vec e_x \tilde\Pi_+ = -i \vec\Upsilon_y$, matching the first column of $\mathsf{M}_2(\vec e_x)=-i\sigma_1$. The two minimal left ideals $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ are both isomorphic to $S$; the algebra is simple, so all its simple modules are isomorphic.

This carrier model is the precise sense in which "the spinor module lies inside $\mathbb{B}$": a spinor is an element of the algebra that lies in the Peirce carrier $\mathbb{B}\tilde\Pi_+$, which is the minimal left ideal here, and the algebra acts on it by the one-sided cell $L_{\tilde Q}$. It is not an arbitrary biquaternion.

## The Two Chiral Halves

The spinor module of the preceding sections carries the **defining representation** of $SL(2,\mathbb{C})$. In the classification of the companion article [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html), this is the representation

$$
V_1 = \left(\tfrac{1}{2}, 0\right), \qquad \dim_{\mathbb{C}} V_1 = 2,
$$

the **left-handed Weyl spinor** module. Its complex conjugate

$$
\bar{S} = \overline{V_1} = \left(0, \tfrac{1}{2}\right), \qquad \dim_{\mathbb{C}}\bar{S} = 2,
$$

is the **right-handed Weyl spinor** module. These are the two **chiral halves**.

Concretely, both modules are carried by $\mathbb{C}^2$, but with different actions. If $\tilde U^{\mathrm{lor}}\in SL(2,\mathbb{C})$ and $g = \mathsf{M}_2(\tilde U^{\mathrm{lor}})$, then

$$
\text{left-handed:}\quad \psi \;\longmapsto\; g\,\psi=L_{\tilde U}\psi,
\qquad\qquad
\text{right-handed:}\quad \varphi \;\longmapsto\; \mathsf{M}_2(\bar{\tilde U}^{\mathrm{lor}})\,\varphi=(g^{\dagger})^{-1}\varphi,
$$

where $\bar{\tilde U}^{\mathrm{lor}}=(\tilde U^{\mathrm{lor}}{}^{*})^{\natural}$ is the **coefficientwise complex conjugate** of the biquaternion, written with the corpus's complex conjugation $\bar{\cdot}$, and $g^{\dagger}$ is the conjugate transpose of $g$. The star alone is the Hermitian conjugation of the algebra; the bar is the coefficient conjugation, and its matrix is **not** the entrywise conjugate $\bar g$, because the realization carries $-i$ in its quaternion part and conjugating the coefficients therefore twists the Pauli part as well. The second action is the conjugate of the first — since $\tilde U^{\mathrm{lor}}\mapsto\bar{\tilde U}^{\mathrm{lor}}$ is an automorphism of $SL(2,\mathbb{C})$, the assignment is a genuine representation — and its matrix is

$$
\mathsf{M}_2(\bar{\tilde U}^{\mathrm{lor}}) = \epsilon^{-1}\bar{g}\,\epsilon = (g^{\dagger})^{-1},
$$

the inverse conjugate transpose, which is equivalent to the entrywise-conjugate action $g\mapsto\bar{g}$ (the two differ by conjugation with the invariant tensor $\epsilon$ introduced below). The chiral halves are exchanged by parity — a transformation of the full Lorentz group, not of $SO^{+}(1,3)$ — and they are **not isomorphic** as complex representations of $SL(2,\mathbb{C})$.

Two cautions belong here, because they are often blurred.

**First, the two halves are not the two minimal left ideals.** The ideals $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ are both isomorphic to $S$ as left $\mathbb{B}$-modules: left multiplication by $\tilde U^{\mathrm{lor}}$ acts by the **same** defining representation on each. The chirality distinction is therefore *not* visible to the complex algebra $\mathbb{B}$ alone, which is simple and has a single simple module. It becomes visible only after the real algebra $\mathbb{B}_{\mathbb{R}}$ is complexified, which introduces the central root $\tilde\Xi_{\mathrm{ad}}$, and on the module it is the charge conjugation $\mathcal{C}:S\leftrightarrow\bar{S}$ that relates the two halves.

**Second, the chiral splitting appears in the complexification.** The complexification of the real algebra $\mathbb{B}_{\mathbb{R}}$ splits:

$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}} \;\cong\; M_2(\mathbb{C}) \oplus M_2(\mathbb{C}),
$$

the two central summands being the two chiralities. The corresponding central idempotents are

$$
e_+=\tfrac{1}{2}(e_t+\chi),\qquad e_-=\tfrac{1}{2}(e_t-\chi),\qquad \chi=i\tilde\Xi_{\mathrm{ad}},
$$

with $\tilde\Xi_{\mathrm{ad}}^2=-e_t$ a central root of $-1$ in the complexification, so $\chi^2=e_t$. Under the correspondence $\mathbb{B}\cong\mathrm{Cl}_{1,3}^{+}$, the biquaternion scalar imaginary maps to $-\omega$ in the chosen extension, and the Clifford image of $\chi$ is $i_{\mathbb{C}}\omega$; the two signs $i_{\mathbb{C}}$ and $\omega$ square to $-1$, so their product squares to $+1$. These are the idempotents of the two chiral halves. This is the algebraic form of the statement that the odd part of the Clifford algebra, which is not contained in the even subalgebra $\mathbb{B}$, exchanges the two chiralities (Section *The Even Subalgebra and the Origin of the Action*).

**The chirality cell.** On the Dirac module the chiral sign is represented by the cell

$$
\Gamma=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}},
\qquad
\Gamma\Psi=-i\,\Psi\,\vec e_z .
$$

It satisfies $\Gamma^2=I_4$, because $(-i)^2=-1$ and $\vec e_z^2=-e_t$:

$$
\Gamma^2=(-i)^2L_{e_t}^{\mathrm{axf}}R_{\vec e_z^2}^{\mathrm{axf}}=(-1)L_{e_t}^{\mathrm{axf}}R_{-e_t}^{\mathrm{axf}}=I_4 .
$$

The **chiral projectors** are

$$
P_L=\tfrac{1}{2}(I_4-\Gamma),\qquad P_R=\tfrac{1}{2}(I_4+\Gamma),
\qquad
P_L^2=P_L,\quad P_R^2=P_R,\quad P_LP_R=0,\quad P_L+P_R=I_4,
$$

and on $\Delta$ the cell acts as $\operatorname{diag}(-I_2,I_2)$ in the basis of the two halves, so there $P_L$ projects onto $S$ and $P_R$ onto $\bar S$. The carrier matters at this point, and the two carriers must not be confused. On the regular module $\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-$ the same cell has the Peirce eigenspaces $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$, which are **two copies of $S$**, and there it equals $-$ the inner Peirce sign $R_{i\vec e_z}^{\mathrm{axf}}$; the two eigenspaces are isomorphic, so no chiral distinction is produced. On $\Delta$ the two eigenspaces are $S$ and $\bar S$, which are not isomorphic, and the distinction is real. The difference is the carrier: $\Delta$ is a module for the **group** $SL(2,\mathbb{C})$, not for the algebra $\mathbb{B}$. A $\mathbb{B}$-module cannot split into $S\oplus\bar S$, because $\mathbb{B}\cong M_2(\mathbb{C})$ is simple and $\bar S$ is not a $\mathbb{B}$-module. The chiral sign is the **central** grading of the complexification, and it is not an element of $\mathbb{B}$.

The **Dirac spinor module** is the direct sum of the two halves,

$$
\boxed{\;\Delta = S \oplus \bar{S} = \left(\tfrac{1}{2},0\right)\oplus\left(0,\tfrac{1}{2}\right), \qquad \dim_{\mathbb{C}}\Delta = 4\;},
$$

on which $SL(2,\mathbb{C})$ acts block-diagonally by $g\oplus(g^{\dagger})^{-1}$, the second block being the inverse conjugate transpose of the first. Its four complex components are the four components of the Dirac spinor, and its two blocks are the left- and right-handed Weyl spinors. A biquaternion, regarded as a $2\times2$ matrix, may be read as a pair of column spinors; the two columns are two copies of $S$, not $S$ and $\bar S$, and it is the pairing of $S$ with its conjugate that constitutes the Dirac module.

## The Unit-Norm Biquaternions and the Double Cover

The group that acts is the group of **unit-norm biquaternions**,

$$
SL(2,\mathbb{C}) \;=\; \{\tilde U^{\mathrm{lor}}\in\mathbb{B} : \tilde U^{\mathrm{lor}}\tilde U^{\mathrm{lor}}{}^{\natural} = e_t\},
$$

which under $\mathsf{M}_2$ is exactly $\{g\in GL_2(\mathbb{C}) : \det g = 1\}$, because the biquaternion norm is the determinant. It is a simply connected complex Lie group of complex dimension $3$ (real dimension $6$), with Lie algebra $\mathfrak{sl}(2,\mathbb{C})$, the traceless $2\times2$ complex matrices.

The subgroups relevant to the series sit inside it as follows:

| Element | Characterization | Subspace |
|---|---|---|
| Pure boost $\tilde U_{\mathrm b} = \cosh\frac{\xi}{2}\,e_t + i\sinh\frac{\xi}{2}\vec u_{\mathrm b}$ | Hermitian, unit norm | $\mathbb{M}_+$ |
| Pure rotation $\tilde u_{\mathrm r} = \cos\frac{\theta}{2}\,e_t + \sin\frac{\theta}{2}\vec u_{\mathrm r}$ | Real quaternion, unit norm | $\mathbb{H}_{\mathbb{B}}$ |
| General $\tilde U^{\mathrm{lor}}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | Unit norm | $\mathbb{B}$ |

Pure boosts satisfy $\tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b}$; they do not form a subgroup (the product of two non-collinear boosts is a boost plus a rotation). Pure rotations form the subgroup $SU(2) = SL(2,\mathbb{C})\cap \mathrm{U}(2)$.

The action on the four-vector space is the two-sided cell $\Theta_{\tilde U}=L_{\tilde U}R_{\tilde U^{*}}$,

$$
\pi:\; SL(2,\mathbb{C}) \longrightarrow SO^{+}(1,3), \qquad
\pi(\tilde U^{\mathrm{lor}}):\; \tilde{Q} \;\longmapsto\; \tilde U^{\mathrm{lor}}\,\tilde{Q}\,\tilde U^{\mathrm{lor}}{}^{*}, \qquad \tilde{Q}\in\mathbb{M}_-.
$$

It is well defined (the image of an anti-Hermitian element is anti-Hermitian), it preserves the biquaternion norm, and it is a group homomorphism. Its kernel is

$$
\ker\pi = \{\pm e_t\} \cong \mathbb{Z}/2\mathbb{Z},
$$

since $-e_t$ is central, $(-\tilde U^{\mathrm{lor}})\tilde{Q}(-\tilde U^{\mathrm{lor}})^{*} = \tilde U^{\mathrm{lor}}\tilde{Q}\tilde U^{\mathrm{lor}}{}^{*}$ for every $\tilde{Q}$ (the two signs cancel). Hence $\pi$ is **two-to-one** onto the proper orthochronous Lorentz group,

$$
SO^{+}(1,3) \;\cong\; SL(2,\mathbb{C})/\{\pm e_t\},
$$

and $SL(2,\mathbb{C})$ is the **double cover** of the restricted Lorentz group.

The spinor action is by contrast **faithful**. On $S$, the element $-e_t$ acts as

$$
\mathsf{M}_2(-e_t) = -I_2,
$$

so $\pm\tilde U^{\mathrm{lor}}$ act differently on every spinor. The defining representation therefore does **not** descend to $SO^{+}(1,3)$: it is a genuine representation of the double cover. This is the exact sense in which the spinor action and the four-vector action differ by the double cover.

## The Lorentz Action on the Spinor Module

### The Action

The Lorentz group acts on the spinor module by the **one-sided cell** $L_{\tilde U}$:

$$
\boxed{\;\psi \;\longmapsto\; L_{\tilde U}\psi=\tilde U^{\mathrm{lor}}\,\psi \;=\; \mathsf{M}_2(\tilde U^{\mathrm{lor}})\,\psi,
\qquad \tilde U^{\mathrm{lor}}\in SL(2,\mathbb{C}),\quad \psi\in S\;}.
$$

Equivalently, in the ideal model, $\psi\in\mathbb{B}\tilde\Pi_+$ is sent to $\tilde U^{\mathrm{lor}}\psi\in\mathbb{B}\tilde\Pi_+$; the ideal is stable because $\mathbb{B}(\mathbb{B}\tilde\Pi_+)\subseteq\mathbb{B}\tilde\Pi_+$. The action is $\mathbb{C}$-linear, and it is a group action:

$$
L_{\tilde U_2}L_{\tilde U_1}=L_{\tilde U_2\tilde U_1},
\qquad
\tilde U^{\mathrm{lor}}_{2}(\tilde U^{\mathrm{lor}}_{1}\psi) = (\tilde U^{\mathrm{lor}}_{2}\tilde U^{\mathrm{lor}}_{1})\psi.
$$

No two-sided action appears. This is the defining feature of the spinor representation.

### Boosts and Rotations Explicitly

For a boost along $\vec u_{\mathrm b}$ with rapidity $\xi$,

$$
\mathsf{M}_2(\tilde U_{\mathrm b}) = \cosh\frac{\xi}{2}\,I_2 + \sinh\frac{\xi}{2}\,\vec u_{\mathrm b}\cdot\boldsymbol{\sigma},
$$

as follows from $\mathsf{M}_2(i\vec u_{\mathrm b}) = \vec u_{\mathrm b}\cdot\boldsymbol{\sigma}$. For $\vec u_{\mathrm b} = \vec u_z$ this is the diagonal matrix

$$
\mathsf{M}_2(\tilde U_{\mathrm b})=\operatorname{diag}\left(e^{\xi/2},e^{-\xi/2}\right),
$$

which stretches one spinor component and contracts the other. For a rotation about $\vec u_{\mathrm r}$ by angle $\theta$,

$$
\mathsf{M}_2(\tilde u_{\mathrm r}) = \cos\frac{\theta}{2}\,I_2 - i\sin\frac{\theta}{2}\,\vec u_{\mathrm r}\cdot\boldsymbol{\sigma},
$$

the standard $SU(2)$ rotation matrix. A rotation by $2\pi$ sends $\mathsf{M}_2(\tilde u_{\mathrm r})$ to $-I_2$: it is the identity in the four-vector representation but not on the spinor module. A rotation by $4\pi$ is the identity on both.

### The Infinitesimal Action

Differentiating at the identity gives the action of the Lie algebra. The Lie algebra $\mathfrak{sl}(2,\mathbb{C})$ consists of the traceless matrices, and in the biquaternion basis

$$
\mathfrak{sl}(2,\mathbb{C}) = \operatorname{span}_{\mathbb{R}}\{\,\vec e_x,\vec e_y,\vec e_z\,\} \;\oplus\; \operatorname{span}_{\mathbb{R}}\{\,i\vec e_x,i\vec e_y,i\vec e_z\,\},
$$

the first summand being the rotations, the compact subalgebra $\mathfrak{su}(2)\cong\mathfrak{so}(3)$ (the pure quaternions), and the second the boosts, the non-compact part in $\mathbb{M}_+$. Under $\mathsf{M}_2$,

$$
\vec e_k \longmapsto -i\sigma_k, \qquad i \vec e_k \longmapsto \sigma_k, \qquad k=1,2,3,
$$

so the anti-Hermitian generators $-i\sigma_k$ and the Hermitian generators $\sigma_k$ both act on $S$ by matrix multiplication. On the spinor module the infinitesimal generators act as the Pauli matrices and their multiples, which is the familiar statement that the spin-$\frac{1}{2}$ representation is the fundamental representation of $\mathrm{SL}(2,\mathbb{C})$.

The **compact subgroup** $SU(2)\subset SL(2,\mathbb{C})$ consists of the unit-norm biquaternions with real vector part (the unit quaternions), for which $\tilde u_{\mathrm r}^{*}\tilde u_{\mathrm r} = e_t$. Its action on $S$ is $*$-unitary with respect to the Hermitian inner product $\langle\psi,\phi\rangle = \psi^\dagger\phi$, and it is the double cover of the spatial rotation group $SO(3)$. The boosts, by contrast, are not $*$-unitary, and they do not preserve that inner product; this is the representation-theoretic expression of the non-compactness of the Lorentz group.

## Bilinear Pairings and the Vector Representation

The spinor module carries four pairings — three on $S$ and one between the two chiral halves — and one equivariant bilinear map to the algebra. They are the algebraic ancestors of the Dirac bilinears. What distinguishes them is the subgroup that leaves each invariant: $\varepsilon$ and the mixed pairing under all of $SL(2,\mathbb{C})$, the Hermitian form $h$ only under the compact $SU(2)$, the indefinite form $[\,\cdot\,|\,\cdot\,]$ only under $SU(1,1)$. Three of those groups are proper subgroups of $SL(2,\mathbb{C})$, and the two of them that are not conjugate — $SU(2)$ compact, $SU(1,1)$ non-compact — cannot be traded for one another by a change of basis, so the four forms are genuinely four and not one form in four costumes.

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
h(\psi,\phi) = \psi^{\dagger}\phi = \bar\psi_1\phi_1 + \bar\psi_2\phi_2
$$

is positive definite, but it is **not** invariant under all of $SL(2,\mathbb{C})$:

$$
h(g\psi, g\phi) = \psi^{\dagger} g^{\dagger} g\,\phi.
$$

It is invariant exactly when $g^{\dagger}g = I_2$, i.e. on the compact subgroup $SU(2)$. For a boost, $g^{\dagger}g\neq I_2$, and $h$ is not preserved. The Hermitian form therefore selects the maximal compact subgroup; it does not define a Lorentz-invariant structure on a single chiral half.

### The Mixed Pairing

There is, however, an invariant pairing between the two chiral halves. Let $\psi\in S$ transform as $\psi\mapsto g\psi$ and let $\varphi\in\bar{S}$ transform as $\varphi\mapsto\mathsf{M}_2\big((\tilde U^{\mathrm{lor}}{}^{*})^{\natural}\big)\varphi=(g^{\dagger})^{-1}\varphi$. Then the sesquilinear pairing

$$
b(\psi,\varphi) = \psi^{\dagger}\varphi
$$

The right-handed spinor is written $\varphi$ in this article. Some of the companion articles write it $\chi$; here $\chi$ is reserved for the central chirality grading $i\tilde\Xi_{\mathrm{ad}}$, and the two objects must not be read as one symbol.

is invariant. Indeed,

$$
b\big(g\psi,\, \mathsf{M}_2((\tilde U^{\mathrm{lor}}{}^{*})^{\natural})\varphi\big)
= \psi^{\dagger}\, \mathsf{M}_2(\tilde U^{\mathrm{lor}})^{\dagger}\,\mathsf{M}_2\big((\tilde U^{\mathrm{lor}}{}^{*})^{\natural}\big)\,\varphi
= \psi^{\dagger}\,g^{\dagger}(g^{\dagger})^{-1}\,\varphi
= \psi^{\dagger}\varphi,
$$

because $\tilde U^{\mathrm{lor}}{}^{*}(\tilde U^{\mathrm{lor}}{}^{*})^{\natural} = e_t$ for a unit-norm biquaternion, so that $\mathsf{M}_2\big((\tilde U^{\mathrm{lor}}{}^{*})^{\natural}\big) = (\mathsf{M}_2(\tilde U^{\mathrm{lor}})^{\dagger})^{-1}$ is the inverse conjugate transpose of $g$. The pairing is therefore not between two copies of $S$ with the same action, but between $S$ with $g$ and the second half with $(g^{\dagger})^{-1}$. The latter is the contragredient of $g$; it is equivalent to the conjugate $\bar{g}$ through $\epsilon$, and it is the action of the right-handed half. With $\varphi\mapsto g^{\dagger}\varphi$ instead, the product would transform as $\psi^{\dagger}(g^{\dagger})^2\varphi$, and invariance would require $(g^{\dagger})^2=I_2$, which fails for a general $g\in SL(2,\mathbb{C})$; $g^{\dagger}$ is the inverse of $(g^{\dagger})^{-1}$ only on the compact subgroup. This mixed pairing is the invariant scalar bilinear of the Dirac spinor; it pairs a left-handed spinor with a right-handed one.

### The Spinor-to-Vector Map

Finally, the outer product of a spinor with its conjugate lands in the algebra. For $u,v\in S$, the matrix

$$
\tilde{Q} = u\,v^{\dagger} \;\in\; M_2(\mathbb{C}) \;\cong\; \mathbb{B}
$$

is a rank-one element of the algebra, and under the Lorentz action $u\mapsto gu$ on the first spinor and $v^{\dagger}\mapsto v^{\dagger}g^{\dagger}$ on the conjugate row it transforms as

$$
\tilde{Q} = u\,v^{\dagger} \;\longmapsto\; gu\,(gv)^{\dagger} = g\,\tilde{Q}\,g^{\dagger}.
$$

This is exactly the transformation law of the **Hermitian sandwich** on the material sector. It must be read as a statement about the equivariance of the whole algebra $M_2(\mathbb{C})$, however, and not as the vector representation itself; two cautions are in order. First, the real span of the outer products $u v^{\dagger}$ as $u$ and $v$ range over $S$ is all of $M_2(\mathbb{C})$, of real dimension $8$, not the Hermitian subspace of real dimension $4$: writing $e_1,e_2$ for the standard basis of $S$, the matrices $E_{12}=e_1e_2^{\dagger}$ and $iE_{12}=(ie_1)e_2^{\dagger}$ are each a single outer product and are independent over the reals. Second, $u v^{\dagger}$ is Hermitian **only** when the two spinors are proportional by a real factor, $v = \lambda u$ with $\lambda \in \mathbb{R}$; for a generic pair $i\,uv^{\dagger}$ does not lie in $\mathbb{M}_-$ at all, and is therefore not a four-vector.

The Hermitian subspace $\mathbb{M}_+$ is the **real** span of the self-pair products $u\,u^{\dagger}$, of real dimension $4$. For a general pair the object that transforms as a four-vector is the symmetrised product

$$
H = \tfrac{1}{2}\left(u\,v^{\dagger} + v\,u^{\dagger}\right) \;\in\; \mathbb{M}_+,
\qquad
V = iH \;\in\; \mathbb{M}_-,
$$

which is Hermitian for every pair and reduces to the outer product $u\,u^{\dagger}$ when $v = u$. The four-vector associated with the spinor pair is thus $iH$, which replaces the outer product $i\,uv^{\dagger}$ and agrees with it when the pair is (anti)parallel with a real factor (up to the conventions of the $ict'$ description). The map $S\otimes\bar{S}\to\mathbb{B}$, $u\otimes v^{\dagger}\mapsto uv^{\dagger}$, is an isomorphism of $SL(2,\mathbb{C})$-representations onto the algebra, while the four-vector representation is the real form of it carried by the Hermitian slice, and it realizes the vector representation as the tensor product of the two chiral halves,

$$
\left(\tfrac{1}{2},\tfrac{1}{2}\right) = \left(\tfrac{1}{2},0\right)\otimes\left(0,\tfrac{1}{2}\right).
$$

This is the algebraic link between the one-sided spinor action and the two-sided four-vector action, and its algebra-level form is the Hermitian form $\tilde{Q}\tilde{Q}^{*}\in\mathbb{M}_+$ of the companion articles.

The transformation laws are collected in the following table.

| Pairing | Domain | Transformation | Invariance |
|---|---|---|---|
| $\varepsilon(\psi,\phi) = \psi^{T}\epsilon\phi$ | $S\times S\to\mathbb{C}$ | invariant | $g^{T}\epsilon g = \epsilon$ |
| $h(\psi,\phi) = \psi^{\dagger}\phi$ | $S\times S\to\mathbb{C}$ | $\psi^{\dagger}g^{\dagger}g\,\phi$ | invariant iff $g\in SU(2)$ |
| $b(\psi,\varphi) = \psi^{\dagger}\varphi$ | $S\times\bar{S}\to\mathbb{C}$ | invariant | $\tilde U^{\mathrm{lor}}{}^{*}(\tilde U^{\mathrm{lor}}{}^{*})^{\natural}=e_t$ |
| $\tilde{Q} = u\,v^{\dagger}$ | $S\times\bar{S}\to\mathbb{B}$ | $g\,\tilde{Q}\,g^{\dagger}$ | equivariant |
| $H = \tfrac{1}{2}(uv^{\dagger}+vu^{\dagger})$ | $S\times\bar{S}\to\mathbb{M}_+$ | $g\,H\,g^{\dagger}$ | Hermitian; four-vector is $iH$ |

### The Indefinite Pairing and the Hyperboloids

The pairings above are invariant under the full $SL(2,\mathbb{C})$ or under its maximal compact subgroup. A third pairing, indefinite rather than definite, is invariant exactly under the rank-one subgroup $SU(1,1)\cong SL(2,\mathbb{R})\cong Sp(2,\mathbb{R})$ — the double cover of $SO(1,2)$ and the dynamical group of the oscillator's squeezings — and it is the one that models the hyperboloids of three-dimensional Minkowski space on the same module.

**The indefinite pairing.** With the Pauli matrices of the matrix realisation $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ established above, put

$$
[u|v]=u^{\dagger}\sigma_3v=\bar u_1v_1-\bar u_2v_2 .
$$

This form is Hermitian of signature $(1,1)$; it is **not** invariant under all of $SL(2,\mathbb{C})$, and its isometry group inside $SL(2,\mathbb{C})$ is exactly $SU(1,1)$. Unlike the definite form $h$ it selects the non-compact subgroup, and unlike $\varepsilon$ it is Hermitian rather than alternating. The pair $(h,[\,\cdot\,|\,\cdot\,])$ is the pair (definite, indefinite) whose invariance groups are the two real forms $SU(2)$ and $SU(1,1)$ of the same complex group.

**The vector maps.** Let

$$
\varsigma_1=\sigma_3,\qquad \varsigma_2=i\sigma_2,\qquad \varsigma_3=-i\sigma_1,\qquad \varsigma=\sigma_3(1,\sigma_1,\sigma_2),
$$

a triple satisfying

$$
\varsigma_i\varsigma_j=\eta_{ij}I_2-i\sum_{k,l}\varepsilon_{ijk}\,\eta_{kl}\,\varsigma_l ,
$$

with $\eta=\mathrm{diag}(1,-1,-1)$ — the analogue for $SU(1,1)$ of the quaternion relations for $SU(2)$; the signs of the contraction are carried by $\eta_{kl}$, which is why the sum is written out. The compact form $\varsigma=\sigma_3(1,\sigma_1,\sigma_2)$ in the display is the useful one, because it gives

$$
\sigma_3\varsigma_i=(1,\sigma_1,\sigma_2)_i ,
$$

so each product $\sigma_3\varsigma_i$ is a Pauli matrix and therefore Hermitian, while $\varsigma_2$ and $\varsigma_3$ themselves are not, being Pauli matrices times $i$. That is why the bilinears $\langle z|\sigma_3\varsigma_i|z\rangle$ used below are real, and why the vector maps land in $\mathbb{R}^{1,2}$ and not in $\mathbb{C}^3$. Both the product identity, on all nine index pairs, and the Hermiticity of $\sigma_3\varsigma_i$ were verified here.

The three homogeneous spaces are then modelled on spinors of the module:

$$
v_i=\langle z|\sigma_i|z\rangle\ \ (S^2),\qquad
v_i=\pm\langle z|\sigma_3\varsigma_i|z\rangle\ \ (H^\pm),\qquad
v_i=\langle z_2|\sigma_3\varsigma_i|z_1\rangle\ \ (H^{sl}),
$$

where $\langle z|(\,\cdot\,)|z\rangle$ abbreviates $z^{\dagger}(\,\cdot\,)z$ and $[z|w]=z^{\dagger}\sigma_3w$.

**One identity governs all three.** In every case the invariant norm of the bilinear is the square of the invariant pairing of the spinors:

$$
v_1^2+v_2^2+v_3^2=\big(z^{\dagger}z\big)^2\ \ (S^2),
\qquad
v_1^2-v_2^2-v_3^2=\big([z|z]\big)^2\ \ (H^\pm),
\qquad
v_1^2-v_2^2-v_3^2=\big([z_2|z_1]\big)^2\ \ (H^{sl}).
$$

All three were checked here on generic spinors, to machine precision. The reason is a Fierz identity. Since $\sigma_3\varsigma=(I_2,\sigma_1,\sigma_2)$ is the identity together with the two real Pauli matrices, the bilinears of a general pair satisfy

$$
\big(z^{\dagger}\sigma_3w\big)^2=\big(z^{\dagger}w\big)^2-\big(z^{\dagger}\sigma_1w\big)^2-\big(z^{\dagger}\sigma_2w\big)^2,
$$

whose diagonal case $w=z$ is the Bloch-sphere identity; contracting with $\eta$ therefore reproduces the square of the pairing, and nothing else. This was checked here for generic pairs. The three constructions differ not in the identity but in **which components of $v$ are real**, and that is what selects the surface.

*The sphere.* At $z^{\dagger}z=1$ the identity gives $v_1^2+v_2^2+v_3^2=1$, so the first is the pure-state correspondence of the Bloch-ball article: one Weyl spinor with the definite pairing, all three components real.

*The time-like sheets.* At $[z|z]=\pm1$ the identity gives

$$
v_1^2-v_2^2-v_3^2=1,
$$

so the surface is the time-like hyperboloid $H^\pm\subset\mathbb{R}^{1,2}$, with all three components real and the overall sign of $v$ selecting the sheet.

*The space-like sheet, and the Majorana condition.* Here the identity is empty on its own, because for a generic pair the pairing $[z_2|z_1]$ is free and so is the norm; the failure was checked here and is sharp, the norm varying from pair to pair. Two further conditions make the third case a surface, and both are the source's. First, both spinors are fixed by a real structure, $R=\sigma_1$ with $R^2=I_2$ and $Rg=\bar gR$ for $g\in SU(1,1)$ — the two Majorana halves $z\pm Rz$ of a Weyl spinor. Second, the second spinor is tied to the first by $z_2=\sigma_3z_1$, with $\sigma_3$ anticommuting with $R$. With that tie the identity holds exactly, and one further fact does the work: $v_1$ and $v_2$ come out **real** while $v_3$ comes out **purely imaginary**. Writing $v_3=i\beta$, the level set is

$$
v_1^2-v_2^2+\beta^2=1
$$

at $[z_2|z_1]=\pm1$, and it is this imaginary component that makes the surface the source's, written in the mirrored signature

$$
t^2-x^2+y^2=-1,
$$

the overall sign there depending on the normalization of the pair, which the article does not fix. Both facts — the exactness of the identity and the purity of $v_3$ — were checked here on generic Majorana pairs. The reason the one-sheeted case needs a pair, in that interpretation, is that a single Weyl spinor with either pairing forces one sign of the area spectrum, and only the pair carries the sign a space-like surface needs.

**The closure.** Under the symplectic form

$$
\omega=i\sum_{i,j}(\sigma_3)_{ij}\,dz_i\wedge d\bar z_j
=i\left(dz_1\wedge d\bar z_1-dz_2\wedge d\bar z_2\right)
$$

on the doubled spinor space $\mathbb{C}^2\oplus\bar{\mathbb{C}}^2$ — the pairing that makes the coordinates of the two factors conjugate to one another, and a different form from the invariant $\varepsilon$ above — the bilinears close into the Poisson algebra of $\mathfrak{so}(1,2)\cong\mathfrak{su}(1,1)$:

$$
\{v_i,v_j\}=-2\sum_{k,l}\varepsilon_{ijk}\,\eta_{kl}\,v_l .
$$

The constant is not a sign but a normalization, and it is fixed by the coefficient of $\omega$: $\omega=i(\ldots)$ here carries the factor $2$ that $\frac{i}{2}(\ldots)$ would not, and halving $\omega$ halves the bracket. What was recomputed here on generic elements is the structure, not the constant: for every pair $(i,j)$ the bracket is exactly proportional to $\sum_{k,l}\varepsilon_{ijk}\eta_{kl}v_l$, with the same constant for all pairs and no residual terms, so the three bilinears span a Lie algebra under the Poisson bracket and the map $z\mapsto v(z)$ is a moment-map-like realisation of it on the spinor space, not merely an equivariant map to the vectors. The source writes the relation with its own normalization of $\omega$ and of $v$, in which the constant is $1$. Its use in the spinfoam programme — the area-constrained symplectomorphism to $T^*SU(1,1)$ — is recorded in [Quantum Gravity under the Biquaternion Framework — A Research Agenda](quantum-gravity-under-the-biquaternion-framework-a-research-agenda.html).

## Spinor Action Versus the Hermitian Sandwich

The preceding sections separate two actions that are often conflated. The comparison is worth stating once in a table.

| Question | Spinor action | Hermitian sandwich |
|---|---|---|
| Object acted on | $\psi\in S$ | $\tilde{Q}\in\mathbb{M}_-$ |
| Operator | $L_{\tilde U}$ | $\Theta_{\tilde U}=L_{\tilde U}R_{\tilde U^{*}}$ |
| Formula | $\psi\mapsto\tilde U^{\mathrm{lor}}\psi$ | $\tilde{Q}\mapsto\tilde U^{\mathrm{lor}}\tilde{Q}\tilde U^{\mathrm{lor}}{}^{*}$ |
| Factors of $\tilde U^{\mathrm{lor}}$ | one | two |
| Action of $-e_t$ | $-\mathrm{id}$ | $+\mathrm{id}$ |
| Kernel | $\{e_t\}$ | $\{\pm e_t\}$ |
| Image group | $SL(2,\mathbb{C})$ | $SO^{+}(1,3)$ |
| Descends to $SO^{+}(1,3)$ | no | yes |

The entries are not a list of conventions; they are the content of the double cover. The parameters $\tilde U^{\mathrm{lor}}$ and $-\tilde U^{\mathrm{lor}}$ describe the same Lorentz transformation of every four-vector, but opposite transformations of every spinor. A representation of $SO^{+}(1,3)$ cannot see the sign; a representation of $SL(2,\mathbb{C})$ can.

A common mistake is to "fix" the spinor action by composing it with the Hermitian sandwich, in the hope of making it two-sided. That composition changes the representation: it multiplies the number of factors of $\tilde U^{\mathrm{lor}}$ by two, and it carries the spinor into the algebra. A spinor transforms in $(\tfrac12,0)$; an algebra element $\tilde U^{\mathrm{lor}}\tilde{Q}\tilde U^{\mathrm{lor}}{}^{*}$ transforms in $(\tfrac12,0)\otimes(0,\tfrac12)=(\tfrac12,\tfrac12)$, which is the complexified vector representation. The four-vector is its Hermitian slice. The spinor representation is therefore not a vector representation in disguise; it is the fundamental representation from which the vector representation is built by tensor product.

The composition laws make the same point. For unit-norm biquaternions,

$$
L_{\tilde U_2}L_{\tilde U_1}=L_{\tilde U_2\tilde U_1},
\qquad
\Theta_{\tilde U_2}\Theta_{\tilde U_1}=\Theta_{\tilde U_2\tilde U_1},
$$

the second because the right factors are applied in reverse order, $\tilde U_2(\tilde U_1\tilde{Q}\tilde U_1^{*})\tilde U_2^{*}=\tilde U_2\tilde U_1\tilde{Q}(\tilde U_2\tilde U_1)^{*}$. Both are group actions; they are actions on different objects, and neither reduces to the other.

## The Even Subalgebra and the Origin of the Action

The spinor module is not an accident of the matrix realisation. It has a Clifford-algebra origin, which the series records once, here.

The even subalgebra of the Clifford algebra of four-dimensional Minkowski space is isomorphic to the biquaternion algebra,

$$
\mathrm{Cl}_{1,3}^{+}(\mathbb{R}) \;\cong\; \mathbb{B},
$$

with the three quaternion generators $\vec e_x,\vec e_y,\vec e_z$ mapping to the three spacelike bivectors. The full Clifford algebra acts on its spinor module by **left multiplication**; restricting to the even subalgebra $\mathbb{B}$ gives the action considered in this article. The spin group sits inside the even subalgebra,

$$
\operatorname{Spin}(1,3) \;\cong\; SL(2,\mathbb{C}) \;\subset\; \mathbb{B} \;\subset\; \mathrm{Cl}_{1,3},
$$

and its left multiplication on the Clifford module is the defining spinor action.

Two distinct actions are then visible in the Clifford picture. The spin group acts on the spinor module by left multiplication — one-sided, because a Clifford module is a module and the action is linear. The same group acts on the four-vector subspace $\mathbb{M}_-\subset\mathbb{B}$, spanned by the volume element and the three spacelike bivectors, by a **two-sided action** — multiplied on the left by $\tilde U^{\mathrm{lor}}$ and on the right by its Hermitian conjugate, because a four-vector is an element of the algebra and not a module element. In the read-list conventions the Clifford adjoint is the biquaternion dagger, so the action is the Hermitian sandwich

$$
\tilde{Q}\;\longmapsto\;\tilde U^{\mathrm{lor}}\,\tilde{Q}\,\tilde U^{\mathrm{lor}}{}^{*}
=\Theta_{\tilde U}(\tilde{Q}).
$$

The vector representation is the tensor product of the spinor representation with its conjugate in the sense of the preceding section; the even subalgebra is exactly the algebra generated by the bivectors, and the bivectors are the Lie algebra of the spin group.

The distinction between the two actions matters for four reasons.

1. **It is the double cover.** The kernel of the vector action is $\{\pm e_t\}$; the kernel of the spinor action is $\{e_t\}$. The sign that the vector action cannot see is exactly the sign that distinguishes a spinor from its negative.
2. **It is the difference between a sandwich and a product.** The four-vector action is a sandwich, and it maps $\mathbb{M}_-$ into itself. The spinor action is a single left multiplication by an element of the even subalgebra, and the even subalgebra does not preserve the exterior grading: a bivector multiplied into a vector produces a vector plus a trivector, so grades are mixed in pairs. The spinor module is a Clifford module, not an exterior module.
3. **It is a difference of real form.** Both representations are four-real-dimensional, and they are different in kind. The vector representation is a **real form**: it is real four-dimensional, and its complexification is $S\otimes\bar{S}=(\tfrac12,\tfrac12)$, of complex dimension four; the four-vector space is the Hermitian slice of that complex representation. The spinor representation is genuinely complex two-dimensional, and it carries no invariant real structure, because such a structure would be an isomorphism $S\cong\bar{S}$ and the two halves are not isomorphic. Equal real dimension, different kind.
4. **It is the origin of chirality.** The odd part of the Clifford algebra, which is not contained in the even subalgebra $\mathbb{B}$, exchanges the two chiralities. The chirality is the cell $\Gamma=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, which on the Dirac module acts as $\operatorname{diag}(-I_2,I_2)$; its central form is the grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ of the complexified algebra, which is a cell and not an element of $\mathbb{B}$ and which the frame of §*The Legacy Gamma Formulation* displays as the fifth of its five cells. The Peirce sign $R_{i\vec e_z}^{\mathrm{axf}}$ is a different, inner sign; it grades the two minimal left ideals, not the two chiral halves.

The last point is the precise sense in which "the gamma matrices" and "the spinor module" are not two theories. The gamma matrices are a frame of the same cell algebra that contains $L_{\tilde U}$; the spinor module is the carrier on which the one-sided cells act. The frame is displayed once, in the next section, and the body of the article needs none of it.

## Open Questions

1. **The informational sector.** The companion article [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) identifies $\mathbb{M}_+$ with the Hermitian observables of a two-state system. The spinor module constructed here is the carrier on which those observables act, but the identification of a **state** with a spinor is not made in this article. The pure states are the rank-one projectors $uu^{\dagger}$; the spinor $u$ is a square root of the projector, defined up to a phase. Whether the phase is physical, and whether the informational sector requires the double cover or only its image in $SO^{+}(1,3)$, is left open.

2. **The covariance of the biquaternion Dirac equation.** The companion article [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) carries two equations, and they are not the same operator. The corpus's own equation is the **one-sided chiral pair**

    $$
    \tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
    \qquad
    \tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R,
    $$
    
    in which the gradient acts by left multiplication on the Dirac field $\tilde\Psi=\tilde\Psi_L+\tilde\Psi_R\in\Delta=S\oplus\bar S$ and the mass is the off-diagonal pairing of the two chiral halves. Kravchenko's equation is the **two-sided** single equation on $\mathbb{B}$,
    
    $$
    \mathcal{N}F=\left(i\frac{\partial}{\partial t'}+D_3\right)F-mi\,\overline{F}\,\vec e_z=0,
    $$

    in which the derivative acts on the left, the mass acts on the right through $\vec e_z$, and the conjugation supplies the antilinear part. The two are related by the dictionary, but the transformation law of the biquaternion-valued field $\tilde\Psi$ is still open. A natural candidate is the one-sided cell $L_{\tilde U}$ defined here; its compatibility with the mass term requires the relation between the one-sided action and the conjugate module to be fixed by a convention. The one-sided pair is the definition; the two-sided form is a representation in which the mass is a right multiplication.

3. **The biquaternion form of the symplectic pairing.** The invariant form $\varepsilon$ is presented here in matrix coordinates. Its expression as a bigeneral quaternionic bilinear on the ideal $\mathbb{B}\tilde\Pi_+$ follows from the coordinate map, but the cleanest biquaternion formula is a matter of convention.

4. **Majorana spinors and the real structure.** A Majorana spinor is a spinor fixed by a real structure commuting with the Lorentz action. The module $S$ has such a structure only after a choice of conjugation, and the choice is not unique. The companion article [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html) treats the physical case; the representation-theoretic classification of the possible real structures on $S$ is not attempted here.

5. **Curved spacetime.** The construction is flat-spacetime representation theory. The soldering of the spinor module to a curved manifold — a spin structure, a covariant derivative, and the conversion of the constant cells $L_{\tilde U}$ into local frames — is the subject of the companion articles on the Einstein equation and on gravity, and is not repeated here.

6. **The indefinite pairing and the physical signature.** The pairings $\varepsilon$, $h$ and $[\,\cdot\,|\,\cdot\,]$ are three different invariant forms on the same two-dimensional complex space. Only the last has an indefinite signature, and the indefinite signature is the one that matches the Lorentzian geometry of $\mathbb{R}^{1,2}$. Which of the three is the "physical" one is a question about the interpretation of the module, not about its representation theory; the article records all three and leaves the choice to the applications.

## The Legacy Gamma Formulation

The gamma matrices are a **frame** of the same cell algebra, written as $4\times4$ matrices on the regular module. They are displayed once, here, so that the body of the article can be read without them.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$, not a different algebra. In cell notation,

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\qquad
\gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\qquad
\gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
$$

Each is a one-cell product, and each satisfies the Clifford relations appropriate to the signature: $\gamma_0^2=I_4$, $\gamma_k^2=-I_4$ for $k=1,2,3$, and $\gamma_\mu\gamma_\nu+\gamma_\nu\gamma_\mu=2\eta_{\mu\nu}I_4$. The fifth is the product of the other four, $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$, and it satisfies $\gamma_5^2=I_4$. As an operator, $\gamma_5$ **is** the chirality cell $\Gamma=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ of §*The Two Chiral Halves* — one operator, written once as a cell and once as a matrix of the frame. The algebra element behind the cell is the central grading $\chi$ of the complexification, which is not a gamma matrix; the body of the article uses $\chi$ and never needs a gamma symbol.

A single cell $L_aR_b$ is a pure tensor of $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$, of tensor rank one; as an operator on $\Delta$ its rank is four whenever $a$ and $b$ are invertible, so the two ranks must not be confused. The pure cells form the seven-dimensional cone of rank at most one, and a general element is a sum of at most four of them. Two cells multiply by $L_aR_b\,L_cR_d=L_{ac}R_{db}$, the right factors in reverse order, and the products of the four frame cells $\gamma_0,\dots,\gamma_3$ give the usual sixteen-element Clifford basis. Every sign among them comes from $i^2=-1$ together with $\vec e_k^2=-e_t$: for instance

$$
\gamma_0\gamma_1=i^2L_{e_t\vec e_x}^{\mathrm{pau}}R_{\vec e_y\vec e_x}^{\mathrm{pau}}=-L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y\vec e_x}^{\mathrm{pau}}=L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}},
$$

In the axis-free display:

$$
\gamma_0\gamma_1=i^2L_{e_t\vec e_x}^{\mathrm{axf}}R_{\vec e_y\vec e_x}^{\mathrm{axf}}=-L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y\vec e_x}^{\mathrm{axf}}=L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},
$$

and the same four steps give $\gamma_0\gamma_1\gamma_2\gamma_3=-i\Gamma$, that is $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$ with $\Gamma$ the chirality cell.

The dictionary is complex-linear: the five cells are a complex frame, and their sixteen products are the sixteen-element Clifford basis. What the frame does **not** fix is the real slice. Both $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$ are real forms of the same complex algebra $\mathrm{Cl}_{4}(\mathbb{C})\cong M_4(\mathbb{C})$, and they are not isomorphic to one another. The signs in the display above are the ones that make $\vec e_x,\vec e_y,\vec e_z$ spacelike bivectors, that is the signature $(1,3)$; the other choice of signs describes the other real form, and the complex frame cannot tell the two apart. The choice is made once, in [Matrix Representations: Conventions](matrix-representations-conventions.html), and it is held throughout the series.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The spinor module is the unique simple module of $\mathbb{B}\cong M_2(\mathbb{C})$. It is the carrier of the defining representation of $SL(2,\mathbb{C})$ and of its conjugate, and it is the object on which the Lorentz group acts by the one-sided cell $L_{\tilde U}$. The main results are:

- **The algebra is $M_2(\mathbb{C})$.** The matrix realisation $\mathsf{M}_2$ is an isomorphism of $\mathbb{C}$-algebras, with $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ and $\mathsf{M}_2(i\vec e_k)=\sigma_k$; the biquaternion norm is the determinant, and Hermitian conjugation is the conjugate transpose.
- **There is one simple module.** $S=\mathbb{C}^2$ is the unique simple $\mathbb{B}$-module; the regular module is $S\oplus S$, and the minimal left ideals $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ are both copies of $S$.
- **The Lorentz action is one-sided.** $\psi\mapsto L_{\tilde U}\psi=\tilde U^{\mathrm{lor}}\psi$; the four-vector action is the two-sided cell $\Theta_{\tilde U}=L_{\tilde U}R_{\tilde U^{*}}$, $\tilde{Q}\mapsto\tilde U^{\mathrm{lor}}\tilde{Q}\tilde U^{\mathrm{lor}}{}^{*}$.
- **The double cover is the kernel.** $\ker\pi=\{\pm e_t\}$ acts trivially on $\mathbb{M}_-$ and as $-\mathrm{id}$ on $S$; the spinor action is faithful, the vector action is not.
- **The chiral halves are $S$ and $\bar S$.** They are the two Weyl modules $(\frac12,0)$ and $(0,\frac12)$, paired by $\psi^{\dagger}\varphi$; the chirality cell is $\Gamma=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, with $\Gamma^2=I_4$ and projectors $P_{L,R}=\frac12(I_4\mp\Gamma)$. The two minimal left ideals are **not** the two chiral halves; they are two copies of $S$, and the distinction requires the real structure.
- **The invariant forms are three on $S$, plus one between the halves.** $\varepsilon$ is the alternating form that makes $S$ self-dual; $h$ is the definite Hermitian form invariant only under $SU(2)$; $[\,\cdot\,|\,\cdot\,]$ is the indefinite Hermitian form invariant under $SU(1,1)$; and the mixed pairing $\psi^{\dagger}\varphi$ is invariant between $S$ and $\bar S$.
- **The vector representation is the tensor square.** $S\otimes\bar S\cong\mathbb{B}$ as $SL(2,\mathbb{C})$-representations, and the four-vector representation is its Hermitian slice, $(\frac12,\frac12)=(\frac12,0)\otimes(0,\frac12)$.
- **The gamma matrices are a frame, not the subject.** They are the five cells displayed once in §*The Legacy Gamma Formulation*; the body of the article is written in the cells $L_{\tilde U}$ and $\Theta_{\tilde U}$.

What the article does **not** supply is a dynamics. It supplies the carrier, the action, the invariant pairings and the map to four-vectors; the Dirac equation, the mass terms and the gauge couplings are the subjects of the companion articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\bar{\tilde{Q}}$, $\tilde{Q}^{\natural}$, $\tilde{Q}^{*}$ | Coefficientwise complex, quaternion, and Hermitian conjugates; $\tilde{Q}^{*}=\overline{\tilde{Q}^{\natural}}$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian and Hermitian subspaces; material and informational sectors |
| $\mathsf{M}_2$ | Matrix realisation, $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, $\mathsf{M}_2(i\vec e_k)=\sigma_k$ |
| $\langle\tilde{Q}\rangle_{\natural}$ | Biquaternion norm $=\det\mathsf{M}_2(\tilde{Q})$ |
| $L_a$, $R_b$, $L_aR_b$ | Left, right and two-sided cells, $X\mapsto aX$, $X\mapsto Xb$, $X\mapsto aXb$ |
| $\Theta_{\tilde U}=L_{\tilde U}R_{\tilde U^{*}}$ | Hermitian sandwich, four-vector action |
| $S=\mathbb{C}^2$ | Spinor module, defining representation $(\frac12,0)$ |
| $\bar S$ | Conjugate spinor module, $(0,\frac12)$; written $S^{\mathrm c}$ in some companion articles |
| $\varphi\in\bar S$ | Right-handed spinor; written $\chi$ in some companion articles |
| $\Delta=S\oplus\bar S$ | Dirac spinor module |
| $\tilde\Pi_\pm=\frac12(e_t\pm i\vec e_z)$ | Peirce idempotents |
| $\vec\Upsilon_x,\vec\Upsilon_y$ | Matrix units $E_{12},E_{21}$ |
| $\Gamma=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell, $\Gamma^2=I_4$ |
| $P_{L,R}=\frac12(I_4\mp\Gamma)$ | Chiral projectors |
| $\chi=i\tilde\Xi_{\mathrm{ad}}$ | Central chirality of the complexification, $\chi^2=e_t$ |
| $\tilde U^{\mathrm{lor}}$ | Unit-norm biquaternion, $SL(2,\mathbb{C})$ |
| $g=\mathsf{M}_2(\tilde U^{\mathrm{lor}})$ | Its matrix, $\det g=1$ |
| $\varepsilon(\psi,\phi)=\psi_1\phi_2-\psi_2\phi_1$ | Invariant alternating form |
| $h(\psi,\phi)=\psi^{\dagger}\phi$ | Definite Hermitian form |
| $[u\vert v]=u^{\dagger}\sigma_3v$ | Indefinite Hermitian form invariant under $SU(1,1)$ |
| $\varsigma_1=\sigma_3,\varsigma_2=i\sigma_2,\varsigma_3=-i\sigma_1$ | Triple with $\varsigma_i\varsigma_j=\eta_{ij}I_2-i\sum_{k,l}\varepsilon_{ijk}\eta_{kl}\varsigma_l$, $\eta=\mathrm{diag}(1,-1,-1)$; $\sigma_3\varsigma=(I_2,\sigma_1,\sigma_2)$ |
| $\omega=i\sum_{i,j}(\sigma_3)_{ij}dz_i\wedge d\bar z_j$ | Symplectic form on $\mathbb{C}^2\oplus\bar{\mathbb{C}}^2$ |
| $\mathbb{B}\cong\mathrm{Cl}_{1,3}^{+}(\mathbb{R})$ | Even Clifford algebra |

## Further Reading

**Companion articles.**

- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) — the two-sided action on $\mathbb{M}_-$ and the identification of the four-vector.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) — the Hermitian observables and the two-state system.
- [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html) — the classification $(\tfrac12,0)$ and $(0,\tfrac12)$ used here.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) — the one-sided chiral pair and its two-sided Kravchenko form.
- [The Unpolarized Module of the Biquaternion Algebra](../articles_maths/the-unpolarized-module-of-the-biquaternion-algebra.html) — the central sign of the complexification and the chiral projectors.
- [The Reflection and the Rotation in Biquaternionic Form](the-reflection-and-the-rotation-in-biquaternionic-form.html) — the discrete symmetries that exchange the two chiral halves.
- [Matrix Representations: Conventions](matrix-representations-conventions.html) — the five-gamma frame and the two real Clifford algebras.

**External references.**

- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the standard two-component spinor calculus, the invariant $\epsilon$-form, and the Weyl spinors.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford-algebra construction of spinors from idempotents and the double cover of the Lorentz group.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of the Lorentz group and the relation between spinors and four-vectors.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of spinors and Lorentz transformations in the even subalgebra.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original spinor representation of the electron.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the representation theory of the Lorentz group and the construction of the Dirac spinor from two Weyl spinors.
- Julius Wess and Jonathan Bagger, *Supersymmetry and Supergravity* (Princeton, 1992), for the two-component spinor conventions.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the modules of $M_2(\mathbb{C})$, the highest-weight classification, and the Clebsch–Gordan rule.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for simple modules, Schur's lemma, and the structure of matrix algebras.
- J. D. Simão, "Biquaternions, Majorana spinors and time-like spin-foams," arXiv:2401.10324 [gr-qc] (2024), for the indefinite pairing $[u|v]$, the $\varsigma$ triple, the Weyl- and Majorana-spinor models of $S^2$, $H^\pm$ and $H^{sl}$, the symplectic form $\omega$ and the $\mathfrak{su}(1,1)$ closure of the bilinears. External; cited for the pairing and the bilinears only.
