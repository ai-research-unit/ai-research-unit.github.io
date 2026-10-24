# __Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with its Hermitian conjugation ${}^{*}$, is a $\mathbb{C}$-algebra with involution whose fixed space is the Hermitian sector $\mathbb{M}_+$ and whose anti-fixed space is the anti-Hermitian sector $\mathbb{M}_-$ (*The Biquaternion Algebra and Its Vector Spaces*, *Introduction to the Remarkable Subspaces*). Its module theory is that of $M_2(\mathbb{C})$: up to isomorphism there is one simple left module, the defining module $S=\mathbb{B}\tilde\Pi_+\cong\mathbb{C}^2$, and every left module is a direct sum $S^{\oplus k}$ (*Modules over the Biquaternion Algebra*). This article adds the **form** to that module theory. A module over an algebra with a dagger can carry the corresponding Hermitian form, and the two structures are tied by a single axiom, that the action be self-adjoint:

$$
\langle t,\tilde Q_3\cdot s\rangle_{*}=\langle\tilde Q_3^{*}\cdot t,s\rangle_{*}
\qquad (\tilde Q_3\in\mathbb{B},\ s,t\in S).
$$

A module carrying such a form is a **Hermitian Clifford module** in the sense of the corpus (*Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*), and the whole content of the biquaternion case is one computation and one contrast.

The computation is that the form of the algebra itself, $\langle\tilde Q,\tilde Q_3\rangle_{*}=\mathrm{Sc}(\tilde Q_3^{*}\tilde Q)$, restricted to the simple module is **positive definite**, with Gram matrix $\tfrac12 I_2$ in the natural basis of the minimal left ideal. The contrast is with the general Clifford algebra, where the same restriction can be **totally isotropic**: for the idempotent $\pi=\tfrac12(1+\vec e_x)$ of the split algebra $\mathrm{Cl}_{1,1}(\mathbb{R})$ one has $\pi^{\dagger}\pi=0$, the Gram matrix on $\mathrm{Cl}\pi$ is the zero matrix, and the naive restriction is not a spinor inner product (*Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*, §*The Isotropic Ideal: a Warning*). In $\mathbb{B}$ that failure cannot occur, for the reason the general theory itself prescribes: the scalar form of the dagger is positive definite, $\mathrm{Sc}(\tilde Q_3^{*}\tilde Q_3)=\sum_\mu\lvert Q_{3\mu}\rvert^{2}$, so every subspace inherits a positive definite restriction; and the standard idempotents are **self-adjoint**, $\tilde\Pi_+^{\dagger}=\tilde\Pi_+$, which is exactly the condition under which the general article resolves the difficulty. The biquaternion algebra is the case in which the resolution is already in force, and the spinor inner product needs no separate construction.

The article closes with the **Dirac element**. On a Hermitian module the Clifford action supplies an operator $D=\sum_\mu\rho(\vec e_\mu)\partial/\partial x_\mu$ whose two factors are skew-adjoint and whose formal adjoint is therefore itself (*Dirac Operators with Hermitian Adjoint*); in the finite-dimensional model, with no derivation, it is $D_{\mathrm{alg}}=\sum_k L_{\vec e_k}$, it is skew-adjoint, its square is $-3\,\mathrm{id}$, and its Hermitian square $D_{\mathrm{alg}}^{*}D_{\mathrm{alg}}=3\,\mathrm{id}$ is positive. The model has no harmonic spinors, and the gap $3$ is the content of the module.

The module theory, the idempotents and the Peirce decomposition are *Modules over the Biquaternion Algebra* and *Ideals and Peirce Decomposition of the Biquaternion Algebra*; the scalar form, the adjoint of the one-sided action and the characterisation of the algebra itself as a module are *One-Sided Operators on the General Plain Sesqualgebra* and *Two-Sided Operators on the General Plain Sesqualgebra*; the positivity of the involution and the cone are *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*; the spinor reading of the module is *Biquaternion Spin Geometry*; and the general statements are *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*, *The Adjoint of the One-Sided Action with Hermitian Adjoint* and *Dirac Operators with Hermitian Adjoint*.

## Hermitian Forms and the Adjointness Axiom

**Definition (Hermitian form on a module).** Let $S$ be a left $\mathbb{B}$-module. A **Hermitian form** on $S$ is a map $(s,t)\mapsto\langle t,s\rangle_{*}:S\times S\to\mathbb{C}$ that is $\mathbb{C}$-linear in the second argument and conjugate-linear in the first,

$$
\langle t\lambda,s\rangle_{*}=\langle t,s\rangle_{*}\lambda,\qquad \langle t,s\lambda\rangle_{*}=\bar{\lambda}\langle t,s\rangle_{*}\qquad(\lambda\in\mathbb{C}),
$$

and Hermitian, $\langle s,t\rangle_{*}=\overline{\langle t,s\rangle_{*}}$. Here $\mathbb{C}$ is the centre $\mathbb{C}_{\mathbb{B}}$ of the algebra, so the scalars act on $S$ from both sides and the two linearity statements are unambiguous.

**Definition (Hermitian Clifford module).** A **Hermitian Clifford module** is a left $\mathbb{B}$-module $S$ with a Hermitian form such that

$$
\langle t,\tilde Q_3\cdot s\rangle_{*}=\langle\tilde Q_3^{*}\cdot t,s\rangle_{*}
\qquad\text{for all } \tilde Q_3\in\mathbb{B},\ s,t\in S .
$$

**Proposition (the axiom is the sector criterion).** The axiom is equivalent to the pair of demands that every element of the anti-Hermitian sector act by a **skew-adjoint** operator and every element of the Hermitian sector act by a **self-adjoint** one:

$$
\boxed{\;\langle t,\tilde Q_3\cdot s\rangle_{*}=-\langle\tilde Q_3\cdot t,s\rangle_{*}\quad (\tilde Q_3\in\mathbb{M}_-),
\qquad
\langle t,\tilde Q_3\cdot s\rangle_{*}=+\langle\tilde Q_3\cdot t,s\rangle_{*}\quad (\tilde Q_3\in\mathbb{M}_+)\;}.
$$

*Proof.* An element with $\tilde Q_3^{*}=-\tilde Q_3$ gives the first identity and an element with $\tilde Q_3^{*}=\tilde Q_3$ the second; conversely the two identities, applied to the components of an arbitrary element in the direct sum $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$, give the axiom. The sum is direct because $2$ is invertible in $\mathbb{C}$.

**Corollary (the action is a $*$-representation).** Write $\rho(\tilde Q_3)$ for the action of $\tilde Q_3$ on $S$ and $\bar{\cdot}$ for the adjoint in $\mathrm{End}_{\mathbb{C}}(S)$ with respect to the form. Then

$$
\rho(\tilde Q_3^{*})=\rho(\tilde Q_3)^{*} ,
$$

so a Hermitian Clifford module is exactly a $*$-representation of the $*$-algebra $(\mathbb{B},{}^{*})$ on a Hermitian space, and the structure theory of $*$-representations applies to it.

**Remark (which sector carries the generators).** In a general Clifford algebra the vectors are the elements negated by the dagger, so the vectors act skew-adjointly and generate the definite group (*Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*). In $\mathbb{B}$ that role is played by the anti-Hermitian sector: the generators $\vec e_x,\vec e_y,\vec e_z$ and the central $ie_t$ are anti-Hermitian, they act by skew-adjoint operators, and their span is the Lie algebra $u(2)$ of the internal group $\mathrm{U}(2)$ (*One-Sided Operators on the General Plain Sesqualgebra*). The Hermitian sector $\mathbb{M}_+$ acts by self-adjoint operators; it is the observable side of the module.

## The Regular Module

**Theorem (the algebra over itself).** On the left regular module ${}_{\mathbb{B}}\mathbb{B}$ the scalar form

$$
\boxed{\;\langle\tilde Q,\tilde Q_3\rangle_{*}=\mathrm{Sc}\bigl(\tilde Q_3^{*}\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}Q_{3\bar{\mu}}Q_\mu\;}
$$

is a Hermitian form, positive definite and non-degenerate, and it satisfies the adjointness axiom; so the algebra over itself is a Hermitian Clifford module.

*Proof.* Sesquilinearity and Hermitian symmetry are assembled from the two commuting involutions: the coefficient conjugation $\bar{\cdot}$ conjugates the scalar of the form and the quaternion conjugation ${}^{\natural}$ negates the three vector coefficients. Positivity is $\mathrm{Sc}(\tilde Q_3^{*}\tilde Q_3)=\sum_{\mu}\lvert Q_{3\mu}\rvert^{2}\ge0$, vanishing only at $\tilde Q_3=0$, so the Gram matrix in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ is the identity and the form is non-degenerate. For the axiom, left multiplication by $\tilde Q_4$ gives

$$
\langle\tilde Q,\tilde Q_4\tilde Q_3\rangle_{*}=\mathrm{Sc}\bigl((\tilde Q_4\tilde Q_3)^{\dagger}\tilde Q\bigr)=\mathrm{Sc}\bigl(\tilde Q_3^{*}\bar{\tilde Q_4}\tilde Q\bigr)=\langle\bar{\tilde Q_4}\tilde Q,\tilde Q_3\rangle_{*},
$$

using that the dagger is an anti-involution and that the scalar part is a trace, $\mathrm{Sc}(\tilde Q_1\tilde Q_2)=\mathrm{Sc}(\tilde Q_2\tilde Q_1)$.

**Remark (what is owed to the companion article).** The identity above is the adjoint theorem of *One-Sided Operators on the General Plain Sesqualgebra*, §*The Form That Makes the Action Self-Adjoint*, where it is proved as the statement $L_{\tilde Q_1}^{*}=L_{\tilde{Q}_1^{*}}$; the corollary there is the module picture used here, and it is not repeated.

**Remark (uniqueness on the regular module).** The form is, up to a positive scalar, the only Hermitian form on $\mathbb{B}$ that is invariant in this sense and positive definite. For a form with Gram matrix $G$ the invariance reads $GA=A^{\dagger}G$ for every matrix $A$ of the algebra; letting $A$ run over the matrix units forces $G$ to be a scalar matrix, and positivity forces the scalar to be positive (*One-Sided Operators on the General Plain Sesqualgebra*).

**Remark (the regular module is not simple).** The algebra is $M_2(\mathbb{C})$, simple and artinian, and the regular module decomposes as ${}_{\mathbb{B}}\mathbb{B}\cong S\oplus S$, the two summands being the two columns (*Modules over the Biquaternion Algebra*). The form of the theorem is the orthogonal sum of the forms of the two copies, and it is the reduction of the module to the simple case that is taken up next.

## The Simple Module and Its Form

**Setting.** Let

$$
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\qquad
\tilde\Pi_-=e_t-\tilde\Pi_+,\qquad
\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y),\qquad
\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y),
$$

be the idempotents and the off-diagonal elements of *Ideals and Peirce Decomposition of the Biquaternion Algebra*. Here $i\vec e_z$ is a root of $+1$, $(i\vec e_z)^2=e_t$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents. They satisfy $\tilde\Pi_+^2=\tilde\Pi_+$, $\tilde\Pi_-^2=\tilde\Pi_-$, $\tilde\Pi_+\tilde\Pi_-=0$, $\tilde\Pi_++\tilde\Pi_-=e_t$, the multiplication table

$$
\tilde\Pi_+\vec\Upsilon_x=\vec\Upsilon_x=\vec\Upsilon_x\tilde\Pi_-,\qquad
\tilde\Pi_-\vec\Upsilon_y=\vec\Upsilon_y=\vec\Upsilon_y\tilde\Pi_+,\qquad
\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+,\qquad
\vec\Upsilon_y\vec\Upsilon_x=\tilde\Pi_-,
$$

together with $\vec\Upsilon_x\tilde\Pi_+=\tilde\Pi_-\vec\Upsilon_x=\tilde\Pi_+\vec\Upsilon_y=\vec\Upsilon_y\tilde\Pi_-=0$ and $\vec\Upsilon_x^2=\vec\Upsilon_y^2=0$. The minimal left ideal

$$
S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_y\}
$$

is the simple left module, of complex dimension two; all minimal left ideals are isomorphic to it (*Modules over the Biquaternion Algebra*).

**Lemma (the idempotents are self-adjoint).** $\tilde\Pi_+^{\dagger}=\tilde\Pi_+$ and $\tilde\Pi_-^{\dagger}=\tilde\Pi_-$; equivalently $i\vec e_z$ and $e_t$ are Hermitian. Also $\vec\Upsilon_y^{*}=\tfrac12(i\vec e_x-\vec e_y)$ and $\vec\Upsilon_y^{*}\vec\Upsilon_y=\tilde\Pi_+$.

*Proof.* On the basis, $e_t^{\dagger}=e_t$ and $\vec e_k^{\dagger}=-\vec e_k$, so $(i\vec e_z)^{\dagger}=i^{*}\vec e_z^{\dagger}=(-i)(-\vec e_z)=i\vec e_z$ and $\tilde\Pi_+^{\dagger}=\tfrac12(e_t+i\vec e_z)=\tilde\Pi_+$; the second idempotent is $e_t-\tilde\Pi_+$ and is fixed with it. Further $\vec\Upsilon_y^{*}=\tfrac12\bigl((i\vec e_x)^{\dagger}+\vec e_y^{\dagger}\bigr)=\tfrac12(i\vec e_x-\vec e_y)$, and multiplying out, using $\vec e_x^2=\vec e_y^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, gives $\vec\Upsilon_y^{*}\vec\Upsilon_y=\tfrac14\bigl(e_t+i\vec e_z+i\vec e_z+e_t\bigr)=\tilde\Pi_+$. The sign that matters is $(i\vec e_x)^{\dagger}=+i\vec e_x$, which is the Hermitian sector meeting the generators.

**Theorem (the restriction is positive definite).** The restriction of the scalar form to $S=\mathbb{B}\tilde\Pi_+$ satisfies the adjointness axiom, and in the basis $\{\tilde\Pi_+,\vec\Upsilon_y\}$ its Gram matrix is

$$
\begin{pmatrix}
\langle\tilde\Pi_+,\tilde\Pi_+\rangle_{*} & \langle\vec\Upsilon_y,\tilde\Pi_+\rangle_{*}\\
\langle\tilde\Pi_+,\vec\Upsilon_y\rangle_{*} & \langle\vec\Upsilon_y,\vec\Upsilon_y\rangle_{*}
\end{pmatrix}
=\frac12\begin{pmatrix}1&0\\0&1\end{pmatrix}.
$$

*Proof.* For $s,t\in S$ and any $\tilde Q_3$ one has $\tilde Q_3s\in S$ and $\tilde Q_3^{*}t\in S$, and $\mathrm{Sc}((\tilde Q_3s)^{\dagger}t)=\mathrm{Sc}(s^{\dagger}\tilde Q_3^{*}t)$, so the restriction inherits the axiom from the regular module and is invariant. For the entries, $\tilde\Pi_+^{\dagger}=\tilde\Pi_+$ and $\tilde\Pi_+^2=\tilde\Pi_+$ give $\langle\tilde\Pi_+,\tilde\Pi_+\rangle_{*}=\mathrm{Sc}(\tilde\Pi_+)=\tfrac12$; the table gives $\tilde\Pi_+\vec\Upsilon_y=0$, so $\langle\vec\Upsilon_y,\tilde\Pi_+\rangle_{*}=\mathrm{Sc}(\tilde\Pi_+^{\dagger}\vec\Upsilon_y)=0$ and the matrix is Hermitian; and the lemma gives $\vec\Upsilon_y^{*}\vec\Upsilon_y=\tilde\Pi_+$, so $\langle\vec\Upsilon_y,\vec\Upsilon_y\rangle_{*}=\mathrm{Sc}(\tilde\Pi_+)=\tfrac12$. Positivity is the restriction of the positive definite form of the regular module to a subspace.

**Corollary (no isotropic ideal in $\mathbb{B}$).** The general theory warns that the restriction of the scalar form to a minimal left ideal may be totally isotropic, and exhibits the example $\pi=\tfrac12(1+\vec e_x)$ in $\mathrm{Cl}_{1,1}(\mathbb{R})$, where $\vec e_x^2=+1$ and the Gram matrix on $\mathrm{Cl}\pi$ is the zero matrix. No such ideal exists in $\mathbb{B}$: the scalar form $\mathrm{Sc}(\tilde Q_3^{*}\tilde Q_3)$ is positive definite, so its restriction to every nonzero subspace is positive definite, and no minimal left ideal is isotropic. The reason is visible in the comparison of the two computations: the general failure is $\pi^{\dagger}\pi=0$ for an idempotent built from a vector that the dagger negates, whereas here $\tilde\Pi_+^{\dagger}=\tilde\Pi_+$ and $\tilde\Pi_+^{\dagger}\tilde\Pi_+=\tilde\Pi_+$ has scalar part $\tfrac12$. The standard idempotents of $\mathbb{B}$ are **self-adjoint**, which is exactly the condition the general article asks for when it prescribes a self-adjoint idempotent as the resolution.

**Remark (every idempotent, every ideal).** Nothing is special to $\tilde\Pi_+$. For any nonzero idempotent $\tilde\Pi$ of $\mathbb{B}$ one has

$$
\langle\tilde\Pi,\tilde\Pi\rangle_{*}=\mathrm{Sc}(\exp(\dagger)\tilde\Pi)=\tfrac12\operatorname{Tr}\bigl(\exp(\dagger)\tilde\Pi\bigr)>0,
$$

since $\exp(\dagger)\tilde\Pi$ is a nonzero positive semidefinite matrix and its trace is the squared Frobenius norm of $\tilde\Pi$. So every minimal left ideal of $\mathbb{B}$ carries a positive definite restriction of the scalar form. Since all minimal left ideals are isomorphic (*Modules over the Biquaternion Algebra*), the form is attached to the isomorphism class of the module and not merely to the representative $\mathbb{B}\tilde\Pi_+$, and it is transported by the automorphisms of the algebra along the projective line $\mathbb{P}^1(\mathbb{C})$ that parametrises them (*Ideals and Peirce Decomposition of the Biquaternion Algebra*).

**Theorem (uniqueness: Schur).** Every Hermitian form on the simple module $S$ satisfying the adjointness axiom is a positive real multiple of the restriction of the scalar form.

*Proof.* Let $\langle\cdot,\cdot\rangle_{*,1}$ and $\langle\cdot,\cdot\rangle_{*,2}$ be two such forms, and for $s\in S$ let $\phi(s)$ be the element representing $s$ in the second form, $\langle t,s\rangle_{*,1}=\langle t,\phi(s)\rangle_{*,2}$; the adjointness of both forms makes $\phi$ commute with the action of $\mathbb{B}$. By Schur's lemma and the irreducibility of $S$, $\phi$ is multiplication by a complex scalar, $\phi=\lambda\,\mathrm{id}$ (*Modules over the Biquaternion Algebra*, where $\operatorname{End}_{\mathbb{B}}(S)\cong\mathbb{C}$), so the two forms differ by $\lambda$. Requiring both forms to be Hermitian makes $\lambda$ real, and requiring both to be positive definite makes it positive. For the normalised form the Gram matrix is a scalar matrix: invariance reads $GA=A^{\dagger}G$ for every matrix $A$ of the algebra, and the matrix units force $G$ to be scalar.

**Corollary (the spinor inner product).** On the simple module the Hermitian form is unique up to a positive scalar, so the **spinor inner product** is well defined with no further choice. With the normalisation of the theorem it is the positive definite form of the module: $S$ is a two-dimensional complex Hilbert space, $\mathbb{B}\cong M_2(\mathbb{C})$ acts on it by all operators, the anti-Hermitian sector acts by the skew-adjoint ones, spanning $u(2)$, and the Hermitian sector acts by the self-adjoint ones. This is the form of the spinor module of *Biquaternion Spin Geometry*, on which the chiral halves appear only after complexification; the form itself is the one the unitary group of the next section preserves.

## The Unitary Slice

**Theorem (the slice acts by unitaries).** Let $U=\{\tilde U\in\mathbb{B}:\tilde{U}^{*}\tilde U=e_t\}=\mathrm{U}(2)$ be the unitary slice. Then left multiplication by $\tilde U$ is a unitary operator on every Hermitian Clifford module, and in particular on $S$:

$$
\boxed{\;\langle\tilde U\cdot t,\tilde U\cdot s\rangle_{*}=\langle t,s\rangle_{*}\qquad\text{for all }s,t\in S\;}.
$$

*Proof.* By the axiom, $\langle\tilde U\cdot t,\tilde U\cdot s\rangle_{*}=\langle\tilde{U}^{*}\cdot(\tilde U\cdot t),s\rangle_{*}=\langle (\tilde{U}^{*}\tilde U)\cdot t,s\rangle_{*}=\langle t,s\rangle_{*}$ for $\tilde{U}^{*}\tilde U=e_t$.

**Corollary (unitary representation and its Lie algebra).** The assignment $\tilde U\mapsto\rho(\tilde U)|_S$ is a unitary representation of $\mathrm{U}(2)$ on the module $S$. Its Lie algebra is the anti-Hermitian sector, $u(2)=\mathbb{M}_-$; the operators $L_{\tilde Q_1}$ with $\tilde Q_1\in\mathbb{M}_-$ are skew-adjoint, they satisfy $[L_{\tilde Q_1},L_{\tilde Q_2}]=L_{\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}}$, and the exponential stays in the family, $\exp(L_{\tilde Q_1})=L_{\exp(\tilde Q_1)}$, so the correspondence is a Lie-algebra homomorphism followed by the exponential map (*One-Sided Operators on the General Plain Sesqualgebra*, *Symmetric and Antisymmetric Decomposition of the Four General Products*).

**Remark (the norm-one slice does not act unitarily).** The norm-one slice $\mathbb{B}^{\times}_1=\{\langle\tilde U,\tilde U\rangle_{\natural}=1\}\cong SL(2,\mathbb{C})$ is *not* a group of unitary operators of the module form: the unitary condition is $\tilde{U}^{*}\tilde U=e_t$, which is the slice $\mathrm{U}(2)$, and it meets $\mathbb{B}^{\times}_1$ in $SU(2)$ only. The obstruction is not an accident of the normalisation. The spinor representation of the Lorentz group preserves no positive definite form — the invariant bilinear form on $S$ is the antisymmetric $\varepsilon$, not the module form — so a positive definite invariant form can be required only of the unitary part, and it is the unitary part that the module form detects. This is the module-level shadow of the statement that the slice is the definite real form, and it is why the module form is used with the unitary group while the interval form of $\mathbb{M}_+$ is used with the Lorentz group (*Two-Sided Operators on the General Plain Sesqualgebra*).

## The Dirac Element

**Definition (the Dirac element of the module).** Let $\vec e_x,\vec e_y,\vec e_z$ be the generators. The **Dirac element** is the sum of the left multiplications by them,

$$
D_{\mathrm{alg}}=\sum_{k\in\{x,y,z\}}L_{\vec e_k},
$$

an operator on the regular module; since each $L_{\vec e_k}$ preserves the left ideals, it restricts to an operator of the simple module, written $D_S$.

**Theorem (skew-adjointness, square, and gap).** On the simple module, in the basis $\{\tilde\Pi_+,\vec\Upsilon_y\}$, the generators act by $c(\vec e_k)=-i\sigma_k$; hence

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

*Proof.* The action of the algebra on $S$ is the defining representation of $M_2(\mathbb{C})$ under the isomorphism $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ (*Modules over the Biquaternion Algebra*), and $-i\sigma_k$ is skew-Hermitian because $\sigma_k$ is Hermitian, so $L_{\vec e_k}$ is skew-adjoint by the sector criterion and $D_S$ is a sum of skew-adjoint operators. For the square, the Pauli matrices anticommute, so $\bigl(\sum_k\sigma_k\bigr)^{2}=3I$ and $D_S^{2}=-3I$; the Hermitian square is $D_S^{*}D_S=-D_S^{2}=3\,\mathrm{id}$, positive. The spectrum of $-i\sum_k\sigma_k$ is $i$ times that of the Hermitian matrix $\sum_k\sigma_k$, whose square is $3I$ and whose trace vanishes, so it is $\{\pm\sqrt3\}$.

**Corollary (the algebraic Dirac element is invertible).** Since $D_S^{2}=-3\,\mathrm{id}$, the kernel of $D_S$ is zero, so the finite regular module is $\operatorname{im}D_{\mathrm{alg}}$ with trivial splitting; the volume element acts on $S$ by the scalar $i$, so no chirality grading exists (*Biquaternion Spin Geometry*).

**Remark (the analytic Dirac operator).** The differential Dirac operator $D=\sum_k\rho(\vec e_k)\partial/\partial x_k$, its formal self-adjointness, its square, its domain and its harmonic spinors are *Dirac Operators with Hermitian Adjoint*, *Dirac Differential Operators* and *Fueter Theory for Biquaternions*; the algebraic Dirac element $D_{\mathrm{alg}}=\sum_kL_{\vec e_k}$ is the finite model of that theory.

## Summary

A **Hermitian Clifford module** over $\mathbb{B}$ is a left $\mathbb{B}$-module with a Hermitian form satisfying the single axiom $\langle t,\tilde Q_3\cdot s\rangle_{*}=\langle\tilde Q_3^{*}\cdot t,s\rangle_{*}$, equivalently with every element of $\mathbb{M}_-$ acting skew-adjointly and every element of $\mathbb{M}_+$ self-adjointly, so that the action is a $*$-representation of $(\mathbb{B},{}^{*})$. The **regular module** ${}_{\mathbb{B}}\mathbb{B}$ with the form $\langle\tilde Q,\tilde Q_3\rangle_{*}=\mathrm{Sc}(\tilde Q_3^{*}\tilde Q)=\sum_\mu Q_{3\bar{\mu}}Q_\mu$ is a Hermitian Clifford module: the form is positive definite, non-degenerate, and unique up to a positive scalar, and its adjoint identity is the theorem $L_{\tilde Q_1}^{*}=L_{\tilde{Q}_1^{*}}$ of the one-sided companion. The **simple module** $S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_y\}$ carries the restriction of that form, with Gram matrix $\tfrac12 I_2$ in the basis $\{\tilde\Pi_+,\vec\Upsilon_y\}$: it is **positive definite**, not isotropic. The general warning that the restriction of a scalar form to a minimal left ideal can be totally isotropic has **no instance in $\mathbb{B}$**, because the scalar form of the dagger is positive definite and because the standard idempotents are **self-adjoint**, $\tilde\Pi_+^{\dagger}=\tilde\Pi_+$; the vanishing case of the general theory requires an idempotent built from a vector that the dagger negates, and $\mathbb{B}$ has none. On the irreducible module the form is unique up to a positive scalar by **Schur's lemma**, so the spinor inner product is canonical.

The **unitary slice** $U=\mathrm{U}(2)$ acts on every Hermitian module by unitary operators, and its Lie algebra is the anti-Hermitian sector $\mathbb{M}_-\cong u(2)$; the norm-one slice $\mathbb{B}^{\times}_1=SL(2,\mathbb{C})$ does not act unitarily, only its unitary part $SU(2)$ does, because the spinor representation preserves no positive definite form. The **Dirac element** $D_{\mathrm{alg}}=\sum_kL_{\vec e_k}$ is skew-adjoint, with $D_S=-i(\sigma_1+\sigma_2+\sigma_3)$, $D_S^{2}=-3\,\mathrm{id}$ and positive Hermitian square $3\,\mathrm{id}$; and the analytic Dirac operator built from it is *Dirac Operators with Hermitian Adjoint*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_y\}$ | The simple left module, $\cong\mathbb{C}^2$; the spinor module |
| $(s,t)\mapsto\langle t,s\rangle_{*}$ | Hermitian form, $\mathbb{C}$-linear in the second argument |
| $\langle t,\tilde Q_3\cdot s\rangle_{*}=\langle\tilde Q_3^{*}\cdot t,s\rangle_{*}$ | Adjointness axiom; $\rho(\tilde Q_3^{*})=\rho(\tilde Q_3)^{*}$ |
| $\mathbb{M}_-$ acts skew, $\mathbb{M}_+$ self-adjoint | The sector criterion for the axiom |
| $\langle\tilde Q,\tilde Q_3\rangle_{*}=\mathrm{Sc}(\tilde Q_3^{*}\tilde Q)=\sum_\mu Q_{3\bar{\mu}}Q_\mu$ | Form of the regular module; positive definite |
| $\tilde\Pi_+^{\dagger}=\tilde\Pi_+$ | The idempotents are self-adjoint; hence no isotropic ideal |
| Gram $=\tfrac12 I_2$ in $\{\tilde\Pi_+,\vec\Upsilon_y\}$ | Positive definite restriction to $S$ |
| $U=\mathrm{U}(2)=\{\tilde{U}^{*}\tilde U=e_t\}$ | Unitary slice, acting by unitaries; Lie algebra $\mathbb{M}_-$ |
| $SL(2,\mathbb{C})$ | Norm-one slice; not unitary on $S$ except on $SU(2)$ |
| $D_{\mathrm{alg}}=\sum_kL_{\vec e_k}$, $D_S=-i(\sigma_1+\sigma_2+\sigma_3)$ | Dirac element and its restriction |
| $D_S^{2}=-3\,\mathrm{id}$, $D_S^{*}D_S=3\,\mathrm{id}$ | Clifford square and positive Hermitian square; gap $3$ |
| $D=\sum_k\rho(\vec e_k)\partial/\partial x_k$ | Dirac operator; formally self-adjoint, $D^{*}=D$ |

## Further Reading

- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the algebra, the four conjugations, the remarkable subspaces and the scalar form.
- [Ideals and Peirce Decomposition of the Biquaternion Algebra](ideals-and-peirce-decomposition-of-the-biquaternion-algebra.html), for the idempotents, the off-diagonal elements, the Peirce decomposition and the minimal left ideals.
- [Modules over the Biquaternion Algebra](modules-over-the-biquaternion-algebra.html), for the classification of the modules, the simple module, the projective-not-free dichotomy and the endomorphism algebra.
- [One-Sided Operators on the General Plain Sesqualgebra](one-sided-operators-on-the-general-plain-sesqualgebra.html), for $L_{\tilde Q_1}^{*}=L_{\tilde{Q}_1^{*}}$, the uniqueness of the invariant form and the module picture of the regular module.
- [Two-Sided Operators on the General Plain Sesqualgebra](two-sided-operators-on-the-general-plain-sesqualgebra.html), for the sandwich, the cone and the definite slice viewed as a group of operators.
- [Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint](positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.html), for the positivity of the involution that makes every restriction positive definite.
- [Biquaternion Spin Geometry](biquaternion-spin-geometry.html), for the spinor module, the chirality, the volume element and the Dirac operator.
- [Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint](hermitian-modules-over-a-hermitian-algebra-with-hermitian-adjoint.html), for the general module axiom, Schur uniqueness and the isotropic ideal.
- [The Adjoint of the One-Sided Action with Hermitian Adjoint](the-adjoint-of-the-one-sided-action-with-hermitian-adjoint.html), for the $*$-structure on the operator algebra.
- [Dirac Operators with Hermitian Adjoint](dirac-operators-with-hermitian-adjoint.html), for the formal self-adjointness, the positivity of the square and the finite-dimensional model.
