# __Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with its Hermitian conjugation ${}^{*}$, is a $\mathbb{C}$-algebra with involution whose fixed space is the Hermitian sector $\mathbb{M}_+$ and whose anti-fixed space is the anti-Hermitian sector $\mathbb{M}_-$ (*Biquaternions as a Vector Space over $\mathbb{C}$*, *Introduction to the Remarkable Subspaces*). Its module theory is that of $M_2(\mathbb{C})$: up to isomorphism there is one simple left module, the defining module $S=\mathbb{B}\tilde\Pi_1\cong\mathbb{C}^2$, and every left module is a direct sum $S^{\oplus k}$ (*Modules over the General Plain Algebra of Biquaternions*). This article adds the **form** to that module theory. A module over an algebra with a dagger can carry the corresponding Hermitian form, and the two structures are tied by a single axiom, that the action be self-adjoint:

$$
\langle t,\tilde R\cdot s\rangle_{*}=\langle\tilde{R}^{*}\cdot t,s\rangle_{*}
\qquad (\tilde R\in\mathbb{B},\ s,t\in S).
$$

A module carrying such a form is a **Hermitian Clifford module** in the sense of the corpus (*Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*), and the whole content of the biquaternion case is one computation and one contrast.

The computation is that the form of the algebra itself, $\langle\tilde T,\tilde R\rangle_{*}=\mathrm{Sc}(\tilde{R}^{*}\tilde T)$, restricted to the simple module is **positive definite**, with Gram matrix $\tfrac12 I_2$ in the natural basis of the minimal left ideal. The contrast is with the general Clifford algebra, where the same restriction can be **totally isotropic**: for the idempotent $\pi=\tfrac12(1+e_1)$ of the split algebra $\mathrm{Cl}_{1,1}(\mathbb{R})$ one has $\pi^{\dagger}\pi=0$, the Gram matrix on $\mathrm{Cl}\pi$ is the zero matrix, and the naive restriction is not a spinor inner product (*Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*, §*The Isotropic Ideal: a Warning*). In $\mathbb{B}$ that failure cannot occur, for the reason the general theory itself prescribes: the scalar form of the dagger is positive definite, $\mathrm{Sc}(\tilde{R}^{*}\tilde R)=\sum_\mu\lvert R_\mu\rvert^{2}$, so every subspace inherits a positive definite restriction; and the standard idempotents are **self-adjoint**, $\tilde\Pi_1^{\dagger}=\tilde\Pi_1$, which is exactly the condition under which the general article resolves the difficulty. The biquaternion algebra is the case in which the resolution is already in force, and the spinor inner product needs no separate construction.

The article closes with the **Dirac element**. On a Hermitian module the Clifford action supplies an operator $D=\sum_\mu\rho(e_\mu)\partial_\mu$ whose two factors are skew-adjoint and whose formal adjoint is therefore itself (*Dirac Operators with Hermitian Adjoint*); in the finite-dimensional model, with no derivation, it is $D_{\mathrm{alg}}=\sum_k L_{e_k}$, it is skew-adjoint, its square is $-3\,\mathrm{id}$, and its Hermitian square $D_{\mathrm{alg}}^{*}D_{\mathrm{alg}}=3\,\mathrm{id}$ is positive. The model has no harmonic spinors, and the gap $3$ is the content of the module.

The module theory, the idempotents and the Peirce decomposition are *Modules over the General Plain Algebra of Biquaternions* and *Biquaternion Ideals and Peirce Decomposition*; the scalar form, the adjoint of the one-sided action and the characterisation of the algebra itself as a module are *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* and *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*; the positivity of the involution and the cone are *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*; the spinor reading of the module is *Biquaternion Spin Geometry*; and the general statements are *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*, *The Adjoint of the One-Sided Action with Hermitian Adjoint* and *Dirac Operators with Hermitian Adjoint*.

## Hermitian Forms and the Adjointness Axiom

**Definition (Hermitian form on a module).** Let $S$ be a left $\mathbb{B}$-module. A **Hermitian form** on $S$ is a map $(s,t)\mapsto\langle t,s\rangle_{*}:S\times S\to\mathbb{C}$ that is $\mathbb{C}$-linear in the second argument and conjugate-linear in the first,

$$
\langle t\lambda,s\rangle_{*}=\langle t,s\rangle_{*}\lambda,\qquad \langle t,s\lambda\rangle_{*}=\bar{\lambda}\langle t,s\rangle_{*}\qquad(\lambda\in\mathbb{C}),
$$

and Hermitian, $\langle s,t\rangle_{*}=\overline{\langle t,s\rangle_{*}}$. Here $\mathbb{C}$ is the centre $\mathbb{C}_{\mathbb{B}}$ of the algebra, so the scalars act on $S$ from both sides and the two linearity statements are unambiguous.

**Definition (Hermitian Clifford module).** A **Hermitian Clifford module** is a left $\mathbb{B}$-module $S$ with a Hermitian form such that

$$
\langle t,\tilde R\cdot s\rangle_{*}=\langle\tilde{R}^{*}\cdot t,s\rangle_{*}
\qquad\text{for all } \tilde R\in\mathbb{B},\ s,t\in S .
$$

**Proposition (the axiom is the sector criterion).** The axiom is equivalent to the pair of demands that every element of the anti-Hermitian sector act by a **skew-adjoint** operator and every element of the Hermitian sector act by a **self-adjoint** one:

$$
\langle t,\tilde R\cdot s\rangle_{*}=-\langle\tilde R\cdot t,s\rangle_{*}\quad (\tilde R\in\mathbb{M}_-),
\qquad
\langle t,\tilde R\cdot s\rangle_{*}=+\langle\tilde R\cdot t,s\rangle_{*}\quad (\tilde R\in\mathbb{M}_+).
$$

*Proof.* An element with $\tilde{R}^{*}=-\tilde R$ gives the first identity and an element with $\tilde{R}^{*}=\tilde R$ the second; conversely the two identities, applied to the components of an arbitrary element in the direct sum $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$, give the axiom. The sum is direct because $2$ is invertible in $\mathbb{C}$.

**Corollary (the action is a $*$-representation).** Write $\rho(\tilde R)$ for the action of $\tilde R$ on $S$ and $\bar{\cdot}$ for the adjoint in $\mathrm{End}_{\mathbb{C}}(S)$ with respect to the form. Then

$$
\rho(\tilde{R}^{*})=\rho(\tilde R)^{*} ,
$$

so a Hermitian Clifford module is exactly a $*$-representation of the $*$-algebra $(\mathbb{B},{}^{*})$ on a Hermitian space, and the structure theory of $*$-representations applies to it.

**Remark (which sector carries the generators).** In a general Clifford algebra the vectors are the elements negated by the dagger, so the vectors act skew-adjointly and generate the definite group (*Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*). In $\mathbb{B}$ that role is played by the anti-Hermitian sector: the generators $e_1,e_2,e_3$ and the central $ie_0$ are anti-Hermitian, they act by skew-adjoint operators, and their span is the Lie algebra $u(2)$ of the internal group $U(2)$ (*One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*). The Hermitian sector $\mathbb{M}_+$ acts by self-adjoint operators; it is the observable side of the module.

## The Regular Module

**Theorem (the algebra over itself).** On the left regular module ${}_{\mathbb{B}}\mathbb{B}$ the scalar form

$$
\langle\tilde T,\tilde R\rangle_{*}=\mathrm{Sc}\bigl(\tilde{R}^{*}\tilde T\bigr)=\sum_{\mu=0}^{3}R_{\bar{\mu}}T_\mu
$$

is a Hermitian form, positive definite and non-degenerate, and it satisfies the adjointness axiom; so the algebra over itself is a Hermitian Clifford module.

*Proof.* Sesquilinearity and Hermitian symmetry are assembled from the two commuting involutions: the coefficient conjugation $\bar{\cdot}$ conjugates the scalar of the form and the quaternion conjugation ${}^{\natural}$ negates the three vector coefficients. Positivity is $\mathrm{Sc}(\tilde{R}^{*}\tilde R)=\sum_{\mu}\lvert R_\mu\rvert^{2}\ge0$, vanishing only at $\tilde R=0$, so the Gram matrix in the basis $e_0,e_1,e_2,e_3$ is the identity and the form is non-degenerate. For the axiom, left multiplication by $A$ gives

$$
\langle\tilde T,A\tilde R\rangle_{*}=\mathrm{Sc}\bigl((A\tilde R)^{\dagger}\tilde T\bigr)=\mathrm{Sc}\bigl(\tilde{R}^{*}\bar{A}\tilde T\bigr)=\langle\bar{A}\tilde T,\tilde R\rangle_{*},
$$

using that the dagger is an anti-involution and that the scalar part is a trace, $\mathrm{Sc}(\tilde B\tilde C)=\mathrm{Sc}(\tilde C\tilde B)$.

**Remark (what is owed to the companion article).** The identity above is the adjoint theorem of *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, §*The Form That Makes the Action Self-Adjoint*, where it is proved as the statement $L_{\tilde B}^{*}=L_{\tilde{B}^{*}}$; the corollary there is the module picture used here, and it is not repeated.

**Remark (uniqueness on the regular module).** The form is, up to a positive scalar, the only Hermitian form on $\mathbb{B}$ that is invariant in this sense and positive definite. For a form with Gram matrix $G$ the invariance reads $GA=A^{\dagger}G$ for every matrix $A$ of the algebra; letting $A$ run over the matrix units forces $G$ to be a scalar matrix, and positivity forces the scalar to be positive (*One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*).

**Remark (the regular module is not simple).** The algebra is $M_2(\mathbb{C})$, simple and artinian, and the regular module decomposes as ${}_{\mathbb{B}}\mathbb{B}\cong S\oplus S$, the two summands being the two columns (*Modules over the General Plain Algebra of Biquaternions*). The form of the theorem is the orthogonal sum of the forms of the two copies, and it is the reduction of the module to the simple case that is taken up next.

## The Simple Module and Its Form

**Setting.** Let

$$
\tilde\Pi_1=\tfrac12(e_0+ie_3),\qquad
\tilde\Pi_2=e_0-\tilde\Pi_1,\qquad
\tilde R=\tfrac12(ie_1-e_2),\qquad
\tilde T=\tfrac12(ie_1+e_2),
$$

be the idempotents and the off-diagonal elements of *Biquaternion Ideals and Peirce Decomposition*. They satisfy $\tilde\Pi_1^2=\tilde\Pi_1$, $\tilde\Pi_2^2=\tilde\Pi_2$, $\tilde\Pi_1\tilde\Pi_2=0$, $\tilde\Pi_1+\tilde\Pi_2=e_0$, the multiplication table

$$
\tilde\Pi_1\tilde R=\tilde R=\tilde R\tilde\Pi_2,\qquad
\tilde\Pi_2\tilde T=\tilde T=\tilde T\tilde\Pi_1,\qquad
\tilde R\tilde T=\tilde\Pi_1,\qquad
\tilde T\tilde R=\tilde\Pi_2,
$$

together with $\tilde R\tilde\Pi_1=\tilde\Pi_2\tilde R=\tilde\Pi_1\tilde T=\tilde T\tilde\Pi_2=0$ and $\tilde R^2=\tilde T^2=0$. The minimal left ideal

$$
S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde T\}
$$

is the simple left module, of complex dimension two; all minimal left ideals are isomorphic to it (*Modules over the General Plain Algebra of Biquaternions*).

**Lemma (the idempotents are self-adjoint).** $\tilde\Pi_1^{\dagger}=\tilde\Pi_1$ and $\tilde\Pi_2^{\dagger}=\tilde\Pi_2$; equivalently $ie_3$ and $e_0$ are Hermitian. Also $\tilde{T}^{*}=\tfrac12(ie_1-e_2)$ and $\tilde{T}^{*}\tilde T=\tilde\Pi_1$.

*Proof.* On the basis, $e_0^{\dagger}=e_0$ and $e_k^{\dagger}=-e_k$, so $(ie_3)^{\dagger}=i^{*}e_3^{\dagger}=(-i)(-e_3)=ie_3$ and $\tilde\Pi_1^{\dagger}=\tfrac12(e_0+ie_3)=\tilde\Pi_1$; the second idempotent is $e_0-\tilde\Pi_1$ and is fixed with it. Further $\tilde{T}^{*}=\tfrac12\bigl((ie_1)^{\dagger}+e_2^{\dagger}\bigr)=\tfrac12(ie_1-e_2)$, and multiplying out, using $e_1^2=e_2^2=-e_0$ and $e_1e_2=e_3$, gives $\tilde{T}^{*}\tilde T=\tfrac14\bigl(e_0+ie_3+ie_3+e_0\bigr)=\tilde\Pi_1$. The sign that matters is $(ie_1)^{\dagger}=+ie_1$, which is the Hermitian sector meeting the generators.

**Theorem (the restriction is positive definite).** The restriction of the scalar form to $S=\mathbb{B}\tilde\Pi_1$ satisfies the adjointness axiom, and in the basis $\{\tilde\Pi_1,\tilde T\}$ its Gram matrix is

$$
\begin{pmatrix}
\langle\tilde\Pi_1,\tilde\Pi_1\rangle_{*} & \langle\tilde T,\tilde\Pi_1\rangle_{*}\\
\langle\tilde\Pi_1,\tilde T\rangle_{*} & \langle\tilde T,\tilde T\rangle_{*}
\end{pmatrix}
=\frac12\begin{pmatrix}1&0\\0&1\end{pmatrix}.
$$

*Proof.* For $s,t\in S$ and any $\tilde R$ one has $\tilde Rs\in S$ and $\tilde{R}^{*}t\in S$, and $\mathrm{Sc}((\tilde Rs)^{\dagger}t)=\mathrm{Sc}(s^{\dagger}\tilde{R}^{*}t)$, so the restriction inherits the axiom from the regular module and is invariant. For the entries, $\tilde\Pi_1^{\dagger}=\tilde\Pi_1$ and $\tilde\Pi_1^2=\tilde\Pi_1$ give $\langle\tilde\Pi_1,\tilde\Pi_1\rangle_{*}=\mathrm{Sc}(\tilde\Pi_1)=\tfrac12$; the table gives $\tilde\Pi_1\tilde T=0$, so $\langle\tilde T,\tilde\Pi_1\rangle_{*}=\mathrm{Sc}(\tilde\Pi_1^{\dagger}\tilde T)=0$ and the matrix is Hermitian; and the lemma gives $\tilde{T}^{*}\tilde T=\tilde\Pi_1$, so $\langle\tilde T,\tilde T\rangle_{*}=\mathrm{Sc}(\tilde\Pi_1)=\tfrac12$. Positivity is the restriction of the positive definite form of the regular module to a subspace.

**Corollary (no isotropic ideal in $\mathbb{B}$).** The general theory warns that the restriction of the scalar form to a minimal left ideal may be totally isotropic, and exhibits the example $\pi=\tfrac12(1+e_1)$ in $\mathrm{Cl}_{1,1}(\mathbb{R})$, where $e_1^2=+1$ and the Gram matrix on $\mathrm{Cl}\pi$ is the zero matrix. No such ideal exists in $\mathbb{B}$: the scalar form $\mathrm{Sc}(\tilde{R}^{*}\tilde R)$ is positive definite, so its restriction to every nonzero subspace is positive definite, and no minimal left ideal is isotropic. The reason is visible in the comparison of the two computations: the general failure is $\pi^{\dagger}\pi=0$ for an idempotent built from a vector that the dagger negates, whereas here $\tilde\Pi_1^{\dagger}=\tilde\Pi_1$ and $\tilde\Pi_1^{\dagger}\tilde\Pi_1=\tilde\Pi_1$ has scalar part $\tfrac12$. The standard idempotents of $\mathbb{B}$ are **self-adjoint**, which is exactly the condition the general article asks for when it prescribes a self-adjoint idempotent as the resolution.

**Remark (every idempotent, every ideal).** Nothing is special to $\tilde\Pi_1$. For any nonzero idempotent $e$ of $\mathbb{B}$ one has

$$
\langle e,e\rangle_{*}=\mathrm{Sc}(e^{\dagger}e)=\tfrac12\operatorname{Tr}\bigl(e^{\dagger}e\bigr)>0,
$$

since $e^{\dagger}e$ is a nonzero positive semidefinite matrix and its trace is the squared Frobenius norm of $e$. So every minimal left ideal of $\mathbb{B}$ carries a positive definite restriction of the scalar form. Since all minimal left ideals are isomorphic (*Modules over the General Plain Algebra of Biquaternions*), the form is attached to the isomorphism class of the module and not merely to the representative $\mathbb{B}\tilde\Pi_1$, and it is transported by the automorphisms of the algebra along the projective line $\mathbb{P}^1(\mathbb{C})$ that parametrises them (*Biquaternion Ideals and Peirce Decomposition*).

**Theorem (uniqueness: Schur).** Every Hermitian form on the simple module $S$ satisfying the adjointness axiom is a positive real multiple of the restriction of the scalar form.

*Proof.* Let $\langle\cdot,\cdot\rangle_{*,1}$ and $\langle\cdot,\cdot\rangle_{*,2}$ be two such forms, and for $s\in S$ let $\phi(s)$ be the element representing $s$ in the second form, $\langle t,s\rangle_{*,1}=\langle t,\phi(s)\rangle_{*,2}$; the adjointness of both forms makes $\phi$ commute with the action of $\mathbb{B}$. By Schur's lemma and the irreducibility of $S$, $\phi$ is multiplication by a complex scalar, $\phi=\lambda\,\mathrm{id}$ (*Modules over the General Plain Algebra of Biquaternions*, where $\operatorname{End}_{\mathbb{B}}(S)\cong\mathbb{C}$), so the two forms differ by $\lambda$. Requiring both forms to be Hermitian makes $\lambda$ real, and requiring both to be positive definite makes it positive. For the normalised form the Gram matrix is a scalar matrix: invariance reads $GA=A^{\dagger}G$ for every matrix $A$ of the algebra, and the matrix units force $G$ to be scalar.

**Corollary (the spinor inner product).** On the simple module the Hermitian form is unique up to a positive scalar, so the **spinor inner product** is well defined with no further choice. With the normalisation of the theorem it is the positive definite form of the module: $S$ is a two-dimensional complex Hilbert space, $\mathbb{B}\cong M_2(\mathbb{C})$ acts on it by all operators, the anti-Hermitian sector acts by the skew-adjoint ones, spanning $u(2)$, and the Hermitian sector acts by the self-adjoint ones. This is the form of the spinor module of *Biquaternion Spin Geometry*, on which the chiral halves appear only after complexification; the form itself is the one the unitary group of the next section preserves.

## The Unitary Slice

**Theorem (the slice acts by unitaries).** Let $U=\{\tilde E\in\mathbb{B}:\tilde{E}^{*}\tilde E=e_0\}=U(2)$ be the unitary slice. Then left multiplication by $\tilde E$ is a unitary operator on every Hermitian Clifford module, and in particular on $S$:

$$
\langle\tilde E\cdot t,\tilde E\cdot s\rangle_{*}=\langle t,s\rangle_{*}\qquad\text{for all }s,t\in S .
$$

*Proof.* By the axiom, $\langle\tilde E\cdot t,\tilde E\cdot s\rangle_{*}=\langle\tilde{E}^{*}\cdot(\tilde E\cdot t),s\rangle_{*}=\langle (\tilde{E}^{*}\tilde E)\cdot t,s\rangle_{*}=\langle t,s\rangle_{*}$ for $\tilde{E}^{*}\tilde E=e_0$.

**Corollary (unitary representation and its Lie algebra).** The assignment $\tilde E\mapsto\rho(\tilde E)|_S$ is a unitary representation of $U(2)$ on the module $S$. Its Lie algebra is the anti-Hermitian sector, $u(2)=\mathbb{M}_-$; the operators $L_{\tilde B}$ with $\tilde B\in\mathbb{M}_-$ are skew-adjoint, they satisfy $[L_{\tilde B},L_{\tilde C}]=L_{\langle\tilde C,\tilde B\rangle_{\natural*}}$, and the exponential stays in the family, $e^{L_{\tilde B}}=L_{e^{\tilde B}}$, so the correspondence is a Lie-algebra homomorphism followed by the exponential map (*One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, *The 12 Products of the Biquaternion Complex Space*).

**Remark (the norm-one slice does not act unitarily).** The norm-one slice $\mathbb{B}^{\times}_1=\{\langle\tilde E,\tilde E\rangle_{\natural}=1\}\cong SL(2,\mathbb{C})$ is *not* a group of unitary operators of the module form: the unitary condition is $\tilde{E}^{*}\tilde E=e_0$, which is the slice $U(2)$, and it meets $\mathbb{B}^{\times}_1$ in $SU(2)$ only. The obstruction is not an accident of the normalisation. The spinor representation of the Lorentz group preserves no positive definite form — the invariant bilinear form on $S$ is the antisymmetric $\varepsilon$, not the module form — so a positive definite invariant form can be required only of the unitary part, and it is the unitary part that the module form detects. This is the module-level shadow of the statement that the slice is the definite real form, and it is why the module form is used with the unitary group while the interval form of $\mathbb{M}_+$ is used with the Lorentz group (*Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*).

## The Dirac Element

**Definition (the Dirac element of the module).** Let $e_1,e_2,e_3$ be the generators. The **Dirac element** is the sum of the left multiplications by them,

$$
D_{\mathrm{alg}}=\sum_{k=1}^{3}L_{e_k},
$$

an operator on the regular module; since each $L_{e_k}$ preserves the left ideals, it restricts to an operator of the simple module, written $D_S$.

**Theorem (skew-adjointness, square, and gap).** On the simple module, in the basis $\{\tilde\Pi_1,\tilde T\}$, the generators act by $c(e_k)=-i\sigma_k$; hence

$$
D_S=-i\bigl(\sigma_1+\sigma_2+\sigma_3\bigr),
\qquad
D_S^{*}=-D_S,
\qquad
D_S^{2}=-3\,\mathrm{id},
\qquad
D_S^{*}D_S=3\,\mathrm{id}>0 .
$$

The spectrum of $D_S$ is $\{\pm i\sqrt3\}$, the real operator $iD_S$ is self-adjoint with spectrum $\{\pm\sqrt3\}$ and orthonormal eigenspinors, and the same identities hold for $D_{\mathrm{alg}}$ on the two copies of the regular module.

*Proof.* The action of the algebra on $S$ is the defining representation of $M_2(\mathbb{C})$ under the isomorphism $\Phi(e_k)=-i\sigma_k$ (*Modules over the General Plain Algebra of Biquaternions*), and $-i\sigma_k$ is skew-Hermitian because $\sigma_k$ is Hermitian, so $L_{e_k}$ is skew-adjoint by the sector criterion and $D_S$ is a sum of skew-adjoint operators. For the square, the Pauli matrices anticommute, so $\bigl(\sum_k\sigma_k\bigr)^{2}=3I$ and $D_S^{2}=-3I$; the Hermitian square is $D_S^{*}D_S=-D_S^{2}=3\,\mathrm{id}$, positive. The spectrum of $-i\sum_k\sigma_k$ is $i$ times that of the Hermitian matrix $\sum_k\sigma_k$, whose square is $3I$ and whose trace vanishes, so it is $\{\pm\sqrt3\}$.

**Corollary (the algebraic Dirac element is invertible).** Since $D_S^{2}=-3\,\mathrm{id}$, the kernel of $D_S$ is zero, so the finite regular module is $\operatorname{im}D_{\mathrm{alg}}$ with trivial splitting; the volume element acts on $S$ by the scalar $i$, so no chirality grading exists (*Biquaternion Spin Geometry*).

**Remark (the analytic Dirac operator).** The differential Dirac operator $D=\sum_k\rho(e_k)\partial_k$, its formal self-adjointness, its square, its domain and its harmonic spinors are *Dirac Operators with Hermitian Adjoint*, *Dirac Differential Operators* and *Fueter Theory for Biquaternions*; the algebraic Dirac element $D_{\mathrm{alg}}=\sum_kL_{e_k}$ is the finite model of that theory.

## Summary

A **Hermitian Clifford module** over $\mathbb{B}$ is a left $\mathbb{B}$-module with a Hermitian form satisfying the single axiom $\langle t,\tilde R\cdot s\rangle_{*}=\langle\tilde{R}^{*}\cdot t,s\rangle_{*}$, equivalently with every element of $\mathbb{M}_-$ acting skew-adjointly and every element of $\mathbb{M}_+$ self-adjointly, so that the action is a $*$-representation of $(\mathbb{B},{}^{*})$. The **regular module** ${}_{\mathbb{B}}\mathbb{B}$ with the form $\langle\tilde T,\tilde R\rangle_{*}=\mathrm{Sc}(\tilde{R}^{*}\tilde T)=\sum_\mu R_{\bar{\mu}}T_\mu$ is a Hermitian Clifford module: the form is positive definite, non-degenerate, and unique up to a positive scalar, and its adjoint identity is the theorem $L_{\tilde B}^{*}=L_{\tilde{B}^{*}}$ of the one-sided companion. The **simple module** $S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde T\}$ carries the restriction of that form, with Gram matrix $\tfrac12 I_2$ in the basis $\{\tilde\Pi_1,\tilde T\}$: it is **positive definite**, not isotropic. The general warning that the restriction of a scalar form to a minimal left ideal can be totally isotropic has **no instance in $\mathbb{B}$**, because the scalar form of the dagger is positive definite and because the standard idempotents are **self-adjoint**, $\tilde\Pi_1^{\dagger}=\tilde\Pi_1$; the vanishing case of the general theory requires an idempotent built from a vector that the dagger negates, and $\mathbb{B}$ has none. On the irreducible module the form is unique up to a positive scalar by **Schur's lemma**, so the spinor inner product is canonical.

The **unitary slice** $U=U(2)$ acts on every Hermitian module by unitary operators, and its Lie algebra is the anti-Hermitian sector $\mathbb{M}_-\cong u(2)$; the norm-one slice $\mathbb{B}^{\times}_1=SL(2,\mathbb{C})$ does not act unitarily, only its unitary part $SU(2)$ does, because the spinor representation preserves no positive definite form. The **Dirac element** $D_{\mathrm{alg}}=\sum_kL_{e_k}$ is skew-adjoint, with $D_S=-i(\sigma_1+\sigma_2+\sigma_3)$, $D_S^{2}=-3\,\mathrm{id}$ and positive Hermitian square $3\,\mathrm{id}$; and the analytic Dirac operator built from it is *Dirac Operators with Hermitian Adjoint*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde T\}$ | The simple left module, $\cong\mathbb{C}^2$; the spinor module |
| $(s,t)\mapsto\langle t,s\rangle_{*}$ | Hermitian form, $\mathbb{C}$-linear in the second argument |
| $\langle t,\tilde R\cdot s\rangle_{*}=\langle\tilde{R}^{*}\cdot t,s\rangle_{*}$ | Adjointness axiom; $\rho(\tilde{R}^{*})=\rho(\tilde R)^{*}$ |
| $\mathbb{M}_-$ acts skew, $\mathbb{M}_+$ self-adjoint | The sector criterion for the axiom |
| $\langle\tilde T,\tilde R\rangle_{*}=\mathrm{Sc}(\tilde{R}^{*}\tilde T)=\sum_\mu R_{\bar{\mu}}T_\mu$ | Form of the regular module; positive definite |
| $\tilde\Pi_1^{\dagger}=\tilde\Pi_1$ | The idempotents are self-adjoint; hence no isotropic ideal |
| Gram $=\tfrac12 I_2$ in $\{\tilde\Pi_1,\tilde T\}$ | Positive definite restriction to $S$ |
| $U=U(2)=\{\tilde{E}^{*}\tilde E=e_0\}$ | Unitary slice, acting by unitaries; Lie algebra $\mathbb{M}_-$ |
| $SL(2,\mathbb{C})$ | Norm-one slice; not unitary on $S$ except on $SU(2)$ |
| $D_{\mathrm{alg}}=\sum_kL_{e_k}$, $D_S=-i(\sigma_1+\sigma_2+\sigma_3)$ | Dirac element and its restriction |
| $D_S^{2}=-3\,\mathrm{id}$, $D_S^{*}D_S=3\,\mathrm{id}$ | Clifford square and positive Hermitian square; gap $3$ |
| $D=\sum_k\rho(e_k)\partial_k$ | Dirac operator; formally self-adjoint, $D^{*}=D$ |

## Further Reading

- *Biquaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-vector-space-over-c.md`), for the algebra, the four conjugations, the remarkable subspaces and the scalar form.
- *Biquaternion Ideals and Peirce Decomposition* (`articles_maths/biquaternion-ideals-and-peirce-decomposition.md`), for the idempotents, the off-diagonal elements, the Peirce decomposition and the minimal left ideals.
- *Modules over the General Plain Algebra of Biquaternions* (`articles_maths/modules-over-the-general-plain-algebra-of-biquaternions.md`), for the classification of the modules, the simple module, the projective-not-free dichotomy and the endomorphism algebra.
- *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* (`articles_maths/one-sided-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for $L_{\tilde B}^{*}=L_{\tilde{B}^{*}}$, the uniqueness of the invariant form and the module picture of the regular module.
- *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the sandwich, the cone and the definite slice viewed as a group of operators.
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the positivity of the involution that makes every restriction positive definite.
- *Biquaternion Spin Geometry* (`articles_maths/biquaternion-spin-geometry.md`), for the spinor module, the chirality, the volume element and the Dirac operator.
- *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint* (`articles_maths/hermitian-modules-over-a-hermitian-algebra-with-hermitian-adjoint.md`), for the general module axiom, Schur uniqueness and the isotropic ideal.
- *The Adjoint of the One-Sided Action with Hermitian Adjoint* (`articles_maths/the-adjoint-of-the-one-sided-action-with-hermitian-adjoint.md`), for the $*$-structure on the operator algebra.
- *Dirac Operators with Hermitian Adjoint* (`articles_maths/dirac-operators-with-hermitian-adjoint.md`), for the formal self-adjointness, the positivity of the square and the finite-dimensional model.
