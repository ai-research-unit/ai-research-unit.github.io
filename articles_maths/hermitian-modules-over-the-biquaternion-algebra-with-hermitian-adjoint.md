# __Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with its Hermitian conjugation ${}^{*}$, is a $\mathbb{C}$-algebra with involution whose fixed space is the Hermitian sector $\mathbb{M}_+$ and whose anti-fixed space is the anti-Hermitian sector $\mathbb{M}_-$ (*Biquaternions as a Vector Space over $\mathbb{C}$*, *Introduction to the Six Subspaces*). Its module theory is that of $M_2(\mathbb{C})$: up to isomorphism there is one simple left module, the defining module $S=\mathbb{B}\tilde\Pi_1\cong\mathbb{C}^2$, and every left module is a direct sum $S^{\oplus k}$ (*Modules over the Biquaternion Algebra*). This article adds the **metric** to that module theory. A module over an algebra with a dagger can carry the corresponding Hermitian form, and the two structures are tied by a single axiom, that the action be self-adjoint:

$$
(\tilde R\cdot s,t)=\bigl(s,\tilde{R}^{*}\cdot t\bigr)
\qquad (\tilde R\in\mathbb{B},\ s,t\in S).
$$

A module carrying such a form is a **Hermitian Clifford module** in the sense of the corpus (*Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*), and the whole content of the biquaternion case is one computation and one contrast.

The computation is that the form of the algebra itself, $(\tilde R,\tilde T)=\mathrm{Sc}(\tilde{R}^{*}\tilde T)$, restricted to the simple module is **positive definite**, with Gram matrix $\tfrac12 I_2$ in the natural basis of the minimal left ideal. The contrast is with the general Clifford algebra, where the same restriction can be **totally isotropic**: for the idempotent $\pi=\tfrac12(1+e_1)$ of the split algebra $\mathrm{Cl}_{1,1}(\mathbb{R})$ one has $\pi^{\dagger}\pi=0$, the Gram matrix on $\mathrm{Cl}\pi$ is the zero matrix, and the naive restriction is not a spinor inner product (*Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*, §*The Isotropic Ideal: a Warning*). In $\mathbb{B}$ that failure cannot occur, for the reason the general theory itself prescribes: the scalar form of the dagger is positive definite, $\mathrm{Sc}(\tilde{R}^{*}\tilde R)=\sum_\mu\lvert R_\mu\rvert^{2}$, so every subspace inherits a positive definite restriction; and the standard idempotents are **self-adjoint**, $\tilde\Pi_1^{\dagger}=\tilde\Pi_1$, which is exactly the condition under which the general article resolves the difficulty. The biquaternion algebra is the case in which the resolution is already in force, and the spinor inner product needs no separate construction.

The article closes with the **Dirac element**. On a Hermitian module the Clifford action supplies an operator $D=\sum_\mu\rho(e_\mu)\partial_\mu$ whose two factors are skew-adjoint and whose formal adjoint is therefore itself (*Dirac Operators with Hermitian Adjoint*); in the finite-dimensional model, with no derivation, it is $D_{\mathrm{alg}}=\sum_k L_{e_k}$, it is skew-adjoint, its square is $-3\,\mathrm{id}$, and its Hermitian square $D_{\mathrm{alg}}^{*}D_{\mathrm{alg}}=3\,\mathrm{id}$ is positive. The model has no harmonic spinors, and the gap $3$ is the metric content of the module.

The module theory, the idempotents and the Peirce decomposition are *Modules over the Biquaternion Algebra* and *Biquaternion Ideals and Peirce Decomposition*; the scalar form, the adjoint of the one-sided action and the characterisation of the algebra itself as a module are *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* and *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*; the positivity of the involution and the cone are *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*; the spinor reading of the module is *Biquaternion Spin Geometry*; and the general statements are *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*, *The Adjoint of the One-Sided Action with Hermitian Adjoint* and *Dirac Operators with Hermitian Adjoint*.

## Hermitian Forms and the Adjointness Axiom

**Definition (Hermitian form on a module).** Let $S$ be a left $\mathbb{B}$-module. A **Hermitian form** on $S$ is a map $(\cdot,\cdot):S\times S\to\mathbb{C}$ that is $\mathbb{C}$-linear in the second argument and conjugate-linear in the first,

$$
(s,t\lambda)=(s,t)\lambda,\qquad (s\lambda,t)=\bar{\lambda}(s,t)\qquad(\lambda\in\mathbb{C}),
$$

and Hermitian, $(t,s)^{*}=(s,t)$. Here $\mathbb{C}$ is the centre $\mathbb{C}_{\mathbb{B}}$ of the algebra, so the scalars act on $S$ from both sides and the two linearity statements are unambiguous.

**Definition (Hermitian Clifford module).** A **Hermitian Clifford module** is a left $\mathbb{B}$-module $S$ with a Hermitian form such that

$$
(\tilde R\cdot s,t)=\bigl(s,\tilde{R}^{*}\cdot t\bigr)
\qquad\text{for all } \tilde R\in\mathbb{B},\ s,t\in S .
$$

**Proposition (the axiom is the sector criterion).** The axiom is equivalent to the pair of demands that every element of the anti-Hermitian sector act by a **skew-adjoint** operator and every element of the Hermitian sector act by a **self-adjoint** one:

$$
(\tilde R\cdot s,t)=-(s,\tilde R\cdot t)\quad (\tilde R\in\mathbb{M}_-),
\qquad
(\tilde R\cdot s,t)=+(s,\tilde R\cdot t)\quad (\tilde R\in\mathbb{M}_+).
$$

*Proof.* An element with $\tilde{R}^{*}=-\tilde R$ gives the first identity and an element with $\tilde{R}^{*}=\tilde R$ the second; conversely the two identities, applied to the components of an arbitrary element in the direct sum $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$, give the axiom. The sum is direct because $2$ is invertible in $\mathbb{C}$.

**Corollary (the action is a $*$-representation).** Write $\rho(\tilde R)$ for the action of $\tilde R$ on $S$ and $\bar{\cdot}$ for the adjoint in $\mathrm{End}_{\mathbb{C}}(S)$ with respect to the form. Then

$$
\rho(\tilde{R}^{*})=\rho(\tilde R)^{*} ,
$$

so a Hermitian Clifford module is exactly a $*$-representation of the $*$-algebra $(\mathbb{B},{}^{*})$ on a Hermitian space, and the structure theory of $*$-representations applies to it.

**Remark (which sector carries the generators).** In a general Clifford algebra the vectors are the elements negated by the dagger, so the vectors act skew-adjointly and generate the compact group (*Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*). In $\mathbb{B}$ that role is played by the anti-Hermitian sector: the generators $e_1,e_2,e_3$ and the central $ie_0$ are anti-Hermitian, they act by skew-adjoint operators, and their span is the Lie algebra $u(2)$ of the internal group $U(2)$ (*One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*). The Hermitian sector $\mathbb{M}_+$ acts by self-adjoint operators; it is the observable side of the module.

## The Regular Module

**Theorem (the algebra over itself).** On the left regular module ${}_{\mathbb{B}}\mathbb{B}$ the scalar form

$$
(\tilde R,\tilde T)=\mathrm{Sc}\bigl(\tilde{R}^{*}\tilde T\bigr)=\sum_{\mu=0}^{3}R_{\bar{\mu}}T_\mu
$$

is a Hermitian form, positive definite and non-degenerate, and it satisfies the adjointness axiom; so the algebra over itself is a Hermitian Clifford module.

*Proof.* Sesquilinearity and Hermitian symmetry are assembled from the two commuting involutions: the coefficient conjugation $\bar{\cdot}$ conjugates the scalar of the form and the quaternion conjugation ${}^{\natural}$ negates the three vector coefficients. Positivity is $\mathrm{Sc}(\tilde{R}^{*}\tilde R)=\sum_{\mu}\lvert R_\mu\rvert^{2}\ge0$, vanishing only at $\tilde R=0$, so the Gram matrix in the basis $e_0,e_1,e_2,e_3$ is the identity and the form is non-degenerate. For the axiom, left multiplication by $A$ gives

$$
(A\tilde R,\tilde T)=\mathrm{Sc}\bigl((A\tilde R)^{\dagger}\tilde T\bigr)=\mathrm{Sc}\bigl(\tilde{R}^{*}\bar{A}\tilde T\bigr)=\bigl(\tilde R,\bar{A}\tilde T\bigr),
$$

using that the dagger is an anti-involution and that the scalar part is a trace, $\mathrm{Sc}(\tilde B\tilde C)=\mathrm{Sc}(\tilde C\tilde B)$.

**Remark (what is owed to the companion article).** The identity above is the adjoint theorem of *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, §*The Form That Makes the Action Self-Adjoint*, where it is proved as the statement $L_{\tilde B}^{*}=L_{\tilde{B}^{*}}$; the corollary there is the module picture used here, and it is not repeated.

**Remark (uniqueness on the regular module).** The form is, up to a positive scalar, the only Hermitian form on $\mathbb{B}$ that is invariant in this sense and positive definite. For a form with Gram matrix $G$ the invariance reads $GA=A^{\dagger}G$ for every matrix $A$ of the algebra; letting $A$ run over the matrix units forces $G$ to be a scalar matrix, and positivity forces the scalar to be positive (*One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*).

**Remark (the regular module is not simple).** The algebra is $M_2(\mathbb{C})$, simple and artinian, and the regular module decomposes as ${}_{\mathbb{B}}\mathbb{B}\cong S\oplus S$, the two summands being the two columns (*Modules over the Biquaternion Algebra*). The form of the theorem is the orthogonal sum of the forms of the two copies, and it is the reduction of the module to the simple case that is taken up next.

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

is the simple left module, of complex dimension two; all minimal left ideals are isomorphic to it (*Modules over the Biquaternion Algebra*).

**Lemma (the idempotents are self-adjoint).** $\tilde\Pi_1^{\dagger}=\tilde\Pi_1$ and $\tilde\Pi_2^{\dagger}=\tilde\Pi_2$; equivalently $ie_3$ and $e_0$ are Hermitian. Also $\tilde{T}^{*}=\tfrac12(ie_1-e_2)$ and $\tilde{T}^{*}\tilde T=\tilde\Pi_1$.

*Proof.* On the basis, $e_0^{\dagger}=e_0$ and $e_k^{\dagger}=-e_k$, so $(ie_3)^{\dagger}=i^{*}e_3^{\dagger}=(-i)(-e_3)=ie_3$ and $\tilde\Pi_1^{\dagger}=\tfrac12(e_0+ie_3)=\tilde\Pi_1$; the second idempotent is $e_0-\tilde\Pi_1$ and is fixed with it. Further $\tilde{T}^{*}=\tfrac12\bigl((ie_1)^{\dagger}+e_2^{\dagger}\bigr)=\tfrac12(ie_1-e_2)$, and multiplying out, using $e_1^2=e_2^2=-e_0$ and $e_1e_2=e_3$, gives $\tilde{T}^{*}\tilde T=\tfrac14\bigl(e_0+ie_3+ie_3+e_0\bigr)=\tilde\Pi_1$. The sign that matters is $(ie_1)^{\dagger}=+ie_1$, which is the Hermitian sector meeting the generators.

**Theorem (the restriction is positive definite).** The restriction of the scalar form to $S=\mathbb{B}\tilde\Pi_1$ satisfies the adjointness axiom, and in the basis $(\tilde\Pi_1,\tilde T)$ its Gram matrix is

$$
\begin{pmatrix}
(\tilde\Pi_1,\tilde\Pi_1) & (\tilde\Pi_1,\tilde T)\\
(\tilde T,\tilde\Pi_1) & (\tilde T,\tilde T)
\end{pmatrix}
=\frac12\begin{pmatrix}1&0\\0&1\end{pmatrix}.
$$

*Proof.* For $s,t\in S$ and any $\tilde R$ one has $\tilde Rs\in S$ and $\tilde{R}^{*}t\in S$, and $\mathrm{Sc}((\tilde Rs)^{\dagger}t)=\mathrm{Sc}(s^{\dagger}\tilde{R}^{*}t)$, so the restriction inherits the axiom from the regular module and is invariant. For the entries, $\tilde\Pi_1^{\dagger}=\tilde\Pi_1$ and $\tilde\Pi_1^2=\tilde\Pi_1$ give $(\tilde\Pi_1,\tilde\Pi_1)=\mathrm{Sc}(\tilde\Pi_1)=\tfrac12$; the table gives $\tilde\Pi_1\tilde T=0$, so $(\tilde\Pi_1,\tilde T)=\mathrm{Sc}(\tilde\Pi_1^{\dagger}\tilde T)=0$ and the matrix is Hermitian; and the lemma gives $\tilde{T}^{*}\tilde T=\tilde\Pi_1$, so $(\tilde T,\tilde T)=\mathrm{Sc}(\tilde\Pi_1)=\tfrac12$. Positivity is the restriction of the positive definite form of the regular module to a subspace.

**Corollary (no isotropic ideal in $\mathbb{B}$).** The general theory warns that the restriction of the scalar form to a minimal left ideal may be totally isotropic, and exhibits the example $\pi=\tfrac12(1+e_1)$ in $\mathrm{Cl}_{1,1}(\mathbb{R})$, where $e_1^2=+1$ and the Gram matrix on $\mathrm{Cl}\pi$ is the zero matrix. No such ideal exists in $\mathbb{B}$: the scalar form $\mathrm{Sc}(\tilde{R}^{*}\tilde R)$ is positive definite, so its restriction to every nonzero subspace is positive definite, and no minimal left ideal is isotropic. The reason is visible in the comparison of the two computations: the general failure is $\pi^{\dagger}\pi=0$ for an idempotent built from a vector that the dagger negates, whereas here $\tilde\Pi_1^{\dagger}=\tilde\Pi_1$ and $\tilde\Pi_1^{\dagger}\tilde\Pi_1=\tilde\Pi_1$ has scalar part $\tfrac12$. The standard idempotents of $\mathbb{B}$ are **self-adjoint**, which is exactly the condition the general article asks for when it prescribes a self-adjoint idempotent as the resolution.

**Remark (every idempotent, every ideal).** Nothing is special to $\tilde\Pi_1$. For any nonzero idempotent $e$ of $\mathbb{B}$ one has

$$
(e,e)=\mathrm{Sc}(e^{\dagger}e)=\tfrac12\operatorname{Tr}\bigl(e^{\dagger}e\bigr)>0,
$$

since $e^{\dagger}e$ is a nonzero positive semidefinite matrix and its trace is the squared Frobenius norm of $e$. So every minimal left ideal of $\mathbb{B}$ carries a positive definite restriction of the scalar form. Since all minimal left ideals are isomorphic (*Modules over the Biquaternion Algebra*), the form is attached to the isomorphism class of the module and not merely to the representative $\mathbb{B}\tilde\Pi_1$, and it is transported by the automorphisms of the algebra along the projective line $\mathbb{P}^1(\mathbb{C})$ that parametrises them (*Biquaternion Ideals and Peirce Decomposition*).

**Theorem (uniqueness: Schur).** Every Hermitian form on the simple module $S$ satisfying the adjointness axiom is a positive real multiple of the restriction of the scalar form.

*Proof.* Let $(\cdot,\cdot)_1$ and $(\cdot,\cdot)_2$ be two such forms, and for $s\in S$ let $\phi(s)$ be the element representing $s$ in the second form, $(s,t)_1=(\phi(s),t)_2$; the adjointness of both forms makes $\phi$ commute with the action of $\mathbb{B}$. By Schur's lemma and the irreducibility of $S$, $\phi$ is multiplication by a complex scalar, $\phi=\lambda\,\mathrm{id}$ (*Modules over the Biquaternion Algebra*, where $\operatorname{End}_{\mathbb{B}}(S)\cong\mathbb{C}$), so the two forms differ by $\lambda$. Requiring both forms to be Hermitian makes $\lambda$ real, and requiring both to be positive definite makes it positive. For the normalised form the Gram matrix is a scalar matrix: invariance reads $GA=A^{\dagger}G$ for every matrix $A$ of the algebra, and the matrix units force $G$ to be scalar.

**Corollary (the spinor inner product).** On the simple module the Hermitian form is unique up to a positive scalar, so the **spinor inner product** is well defined with no further choice. With the normalisation of the theorem it is the positive definite form of the module: $S$ is a two-dimensional complex Hilbert space, $\mathbb{B}\cong M_2(\mathbb{C})$ acts on it by all operators, the anti-Hermitian sector acts by the skew-adjoint ones, spanning $u(2)$, and the Hermitian sector acts by the self-adjoint ones. This is the *metric* form of the spinor module of *Biquaternion Spin Geometry*, on which the chiral halves appear only after complexification; the form itself is the one the compact group of the next section preserves.

## The Unitary Slice

**Theorem (the slice acts by unitaries).** Let $U=\{\tilde E\in\mathbb{B}:\tilde{E}^{*}\tilde E=e_0\}=U(2)$ be the unitary slice. Then left multiplication by $\tilde E$ is a unitary operator on every Hermitian Clifford module, and in particular on $S$:

$$
(\tilde E\cdot s,\tilde E\cdot t)=(s,t)\qquad\text{for all }s,t\in S .
$$

*Proof.* By the axiom, $(\tilde E\cdot s,\tilde E\cdot t)=(s,\tilde{E}^{*}\cdot(\tilde E\cdot t))=(s,(\tilde{E}^{*}\tilde E)\cdot t)=(s,t)$ for $\tilde{E}^{*}\tilde E=e_0$.

**Corollary (unitary representation and its Lie algebra).** The assignment $\tilde E\mapsto\rho(\tilde E)|_S$ is a unitary representation of $U(2)$ on the Hilbert space $S$. Its Lie algebra is the anti-Hermitian sector, $u(2)=\mathbb{M}_-$; the operators $L_{\tilde B}$ with $\tilde B\in\mathbb{M}_-$ are skew-adjoint, they satisfy $[L_{\tilde B},L_{\tilde C}]=L_{[\tilde B,\tilde C]}$, and the exponential stays in the family, $e^{L_{\tilde B}}=L_{e^{\tilde B}}$, so the correspondence is a Lie-algebra homomorphism followed by the exponential map (*One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, *Biquaternion Lie Algebras*).

**Remark (the non-compact slice does not act unitarily).** The norm-one slice $\mathbb{B}^{\times}_1=\{N(\tilde E)=1\}\cong SL(2,\mathbb{C})$ is *not* a group of unitary operators of the module form: the unitary condition is $\tilde{E}^{*}\tilde E=e_0$, which is the slice $U(2)$, and it meets $\mathbb{B}^{\times}_1$ in $SU(2)$ only. The obstruction is not an accident of the normalisation. The spinor representation of the Lorentz group preserves no positive definite form — the invariant bilinear form on $S$ is the antisymmetric $\varepsilon$, not the module form — so a positive definite invariant form can be required only of the compact part, and it is the compact part that the module form detects. This is the module-level shadow of the statement that the slice is the compact real form, and it is why the module form is used with the compact group while the interval form of $\mathbb{M}_+$ is used with the Lorentz group (*Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*).

## The Dirac Element

**Definition (the Dirac element of the module).** Let $e_1,e_2,e_3$ be the generators. The **Dirac element** is the sum of the left multiplications by them,

$$
D_{\mathrm{alg}}=\sum_{k=1}^{3}L_{e_k},
$$

an operator on the regular module; since each $L_{e_k}$ preserves the left ideals, it restricts to an operator of the simple module, written $D_S$.

**Theorem (skew-adjointness, square, and gap).** On the simple module, in the basis $(\tilde\Pi_1,\tilde T)$, the generators act by $c(e_k)=-i\sigma_k$; hence

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

*Proof.* The action of the algebra on $S$ is the defining representation of $M_2(\mathbb{C})$ under the isomorphism $\Phi(e_k)=-i\sigma_k$ (*Modules over the Biquaternion Algebra*), and $-i\sigma_k$ is skew-Hermitian because $\sigma_k$ is Hermitian, so $L_{e_k}$ is skew-adjoint by the sector criterion and $D_S$ is a sum of skew-adjoint operators. For the square, the Pauli matrices anticommute, so $\bigl(\sum_k\sigma_k\bigr)^{2}=3I$ and $D_S^{2}=-3I$; the Hermitian square is $D_S^{*}D_S=-D_S^{2}=3\,\mathrm{id}$, positive. The spectrum of $-i\sum_k\sigma_k$ is $i$ times that of the Hermitian matrix $\sum_k\sigma_k$, whose square is $3I$ and whose trace vanishes, so it is $\{\pm\sqrt3\}$.

**Corollary (formal self-adjointness of the Dirac operator).** Let $D=\sum_k\rho(e_k)\partial_k$ be the Dirac operator built from the Clifford action and first-order operators with formal adjoints $\partial_k^{*}=-\partial_k$. Then each coefficient is skew-adjoint, $\rho(e_k)^{*}=\rho(e_k^{\dagger})=-\rho(e_k)$, the two signs cancel in the product, and

$$
D^{*}=D,
$$

so $D$ is formally self-adjoint; its Hermitian square is positive, $(D^{2}s,s)=(Ds,Ds)=\lVert Ds\rVert^{2}\ge0$, and the module splits as $S=\ker D\oplus\overline{\operatorname{im}D}$. The analytic theory of the operator — its domain, closure, essential self-adjointness and spectrum — is *Dirac Differential Operators* and *Fueter Theory for Biquaternions*, and is not repeated here.

**Corollary (no harmonic spinors in the finite model).** The finite-dimensional operator is invertible, with $\lVert D_S^{-1}\rVert=1/\sqrt3$, and $\ker D_S=0$: the model has no **harmonic spinors**, and the regular module is $S\oplus S=\operatorname{im}D_{\mathrm{alg}}$ with the Hodge splitting trivial. There is no chirality grading to make the vanishing of the index a spectral statement: the volume element acts on $S$ by the scalar $i$ and cuts nothing (*Biquaternion Spin Geometry*), so the index is not defined on the module and the conclusion is the emptiness of the kernel alone. The gap $3$ is the metric content of the smallest definite model whose spin group is non-abelian (*Dirac Operators with Hermitian Adjoint*, §*The Finite-Dimensional Model*).

## Summary

A **Hermitian Clifford module** over $\mathbb{B}$ is a left $\mathbb{B}$-module with a Hermitian form satisfying the single axiom $(\tilde R\cdot s,t)=(s,\tilde{R}^{*}\cdot t)$, equivalently with every element of $\mathbb{M}_-$ acting skew-adjointly and every element of $\mathbb{M}_+$ self-adjointly, so that the action is a $*$-representation of $(\mathbb{B},{}^{*})$. The **regular module** ${}_{\mathbb{B}}\mathbb{B}$ with the form $(\tilde R,\tilde T)=\mathrm{Sc}(\tilde{R}^{*}\tilde T)=\sum_\mu R_{\bar{\mu}}T_\mu$ is a Hermitian Clifford module: the form is positive definite, non-degenerate, and unique up to a positive scalar, and its adjoint identity is the theorem $L_{\tilde B}^{*}=L_{\tilde{B}^{*}}$ of the one-sided companion. The **simple module** $S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde T\}$ carries the restriction of that form, with Gram matrix $\tfrac12 I_2$ in the basis $(\tilde\Pi_1,\tilde T)$: it is **positive definite**, not isotropic. The general warning that the restriction of a scalar form to a minimal left ideal can be totally isotropic has **no instance in $\mathbb{B}$**, because the scalar form of the dagger is positive definite and because the standard idempotents are **self-adjoint**, $\tilde\Pi_1^{\dagger}=\tilde\Pi_1$; the vanishing case of the general theory requires an idempotent built from a vector that the dagger negates, and $\mathbb{B}$ has none. On the irreducible module the form is unique up to a positive scalar by **Schur's lemma**, so the spinor inner product is canonical.

The **unitary slice** $U=U(2)$ acts on every Hermitian module by unitary operators, and its Lie algebra is the anti-Hermitian sector $\mathbb{M}_-\cong u(2)$; the non-compact slice $\mathbb{B}^{\times}_1=SL(2,\mathbb{C})$ does not act unitarily, only its compact part $SU(2)$ does, because the spinor representation preserves no positive definite form. The **Dirac element** $D_{\mathrm{alg}}=\sum_kL_{e_k}$ is skew-adjoint, with $D_S=-i(\sigma_1+\sigma_2+\sigma_3)$, $D_S^{2}=-3\,\mathrm{id}$ and positive Hermitian square $3\,\mathrm{id}$; the differential Dirac operator $D=\sum_k\rho(e_k)\partial_k$ is formally self-adjoint, its square is positive, and the finite model has no harmonic spinors — its kernel is empty and the index is not defined, because the volume element acts as a scalar and does not grade the module.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde T\}$ | The simple left module, $\cong\mathbb{C}^2$; the spinor module |
| $(\cdot,\cdot)$ | Hermitian form, $\mathbb{C}$-linear in the second argument |
| $(\tilde R\cdot s,t)=(s,\tilde{R}^{*}\cdot t)$ | Adjointness axiom; $\rho(\tilde{R}^{*})=\rho(\tilde R)^{*}$ |
| $\mathbb{M}_-$ acts skew, $\mathbb{M}_+$ self-adjoint | The sector criterion for the axiom |
| $(\tilde R,\tilde T)=\mathrm{Sc}(\tilde{R}^{*}\tilde T)=\sum_\mu R_{\bar{\mu}}T_\mu$ | Form of the regular module; positive definite |
| $\tilde\Pi_1^{\dagger}=\tilde\Pi_1$ | The idempotents are self-adjoint; hence no isotropic ideal |
| Gram $=\tfrac12 I_2$ in $(\tilde\Pi_1,\tilde T)$ | Positive definite restriction to $S$ |
| $U=U(2)=\{\tilde{E}^{*}\tilde E=e_0\}$ | Unitary slice, acting by unitaries; Lie algebra $\mathbb{M}_-$ |
| $SL(2,\mathbb{C})$ | Norm-one slice; not unitary on $S$ except on $SU(2)$ |
| $D_{\mathrm{alg}}=\sum_kL_{e_k}$, $D_S=-i(\sigma_1+\sigma_2+\sigma_3)$ | Dirac element and its restriction |
| $D_S^{2}=-3\,\mathrm{id}$, $D_S^{*}D_S=3\,\mathrm{id}$ | Clifford square and positive Hermitian square; gap $3$ |
| $D=\sum_k\rho(e_k)\partial_k$ | Dirac operator; formally self-adjoint, $D^{*}=D$ |

## Further Reading

- *Biquaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-vector-space-over-c.md`), for the algebra, the four conjugations, the six subspaces and the scalar form.
- *Biquaternion Ideals and Peirce Decomposition* (`articles_maths/biquaternion-ideals-and-peirce-decomposition.md`), for the idempotents, the off-diagonal elements, the Peirce decomposition and the minimal left ideals.
- *Modules over the Biquaternion Algebra* (`articles_maths/modules-over-the-biquaternion-algebra.md`), for the classification of the modules, the simple module, the projective-not-free dichotomy and the endomorphism algebra.
- *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/one-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for $L_{\tilde B}^{*}=L_{\tilde{B}^{*}}$, the uniqueness of the invariant form and the module picture of the regular module.
- *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the sandwich, the cone and the compact slice viewed as a group of operators.
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the positivity of the involution that makes every restriction positive definite.
- *Biquaternion Spin Geometry* (`articles_maths/biquaternion-spin-geometry.md`), for the spinor module, the chirality, the volume element and the Dirac operator.
- *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint* (`articles_maths/hermitian-modules-over-a-hilbert-algebra-with-hermitian-adjoint.md`), for the general module axiom, Schur uniqueness and the isotropic ideal.
- *The Adjoint of the One-Sided Action with Hermitian Adjoint* (`articles_maths/the-adjoint-of-the-one-sided-action-with-hermitian-adjoint.md`), for the $*$-structure on the operator algebra.
- *Dirac Operators with Hermitian Adjoint* (`articles_maths/dirac-operators-with-hermitian-adjoint.md`), for the formal self-adjointness, the positivity of the square and the finite-dimensional model.
