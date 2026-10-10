# __Bilinear Operators on the General Plain Sesqualgebra of Biquaternions__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra with its Hermitian conjugation ${}^{*}$ and the positive definite form $\langle\tilde W,\tilde V\rangle_{*}=\mathrm{Sc}(\tilde{V}^{*}\tilde W)$. The **spinor module** is the minimal left ideal $S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde W\}$, the unique simple left $\mathbb{B}$-module, on which the algebra acts by the left multiplication $L_{\tilde B}(s)=\tilde B\,s$; in the matrix model $\Phi(\mathbb{B})=M_2(\mathbb{C})$ and $S=\mathbb{C}^2$, and the module form is $\langle t,s\rangle_{*}=\mathrm{Sc}(s^{\dagger}t)$ with Gram matrix $\frac12 I_2$ in the basis $\{\tilde\Pi_1,\tilde W\}$ and $s^{\dagger}t$ in the standard column basis (*Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint*, *Biquaternion Ideals and Peirce Decomposition*, *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*).

A **bilinear operator** is the operator $s\mapsto b(s,\cdot)$ induced by a bilinear form $b$ on the spinor module. The general theory of these operators is *Bilinear Operators on a Hermitian Module with Hermitian Adjoint*: the form is **Clifford-equivariant** exactly when it satisfies the adjointness axiom of the module, the action of the algebra on the module is **complete** — the Fierz identity — so that the $2^n$ bilinear covariants $\langle\Gamma_A t,s\rangle_{*}$ span the space of forms, and the covariants are classified by the grade of the blade. This article is the biquaternion instance of that theory.

The instance is exact and degenerate in one helpful way. The biquaternion algebra is a full matrix algebra, $\mathbb{B}\cong M_2(\mathbb{C})$, so the action is not merely injective but **onto** the endomorphisms of the spinor module, and the general completeness theorem is an isomorphism rather than a spanning statement: **every endomorphism of the spinor module is a biquaternion**. The four blade operators are a basis of $\mathrm{End}_{\mathbb{C}}(S)$, the four covariants are a basis of the space of forms, and the covariant expansion of a form is computed by the orthogonality of the blades for the trace form; this is the Fierz rearrangement, and in the biquaternion algebra it is a change of basis in a four-dimensional space. The second consequence is the classification: the dagger is the reversion of the positive definite Clifford structure $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ whose vectors are $ie_k$, so the blades split into one Hermitian covariant — the scalar, which is the module form itself — and three skew-Hermitian ones, and the **space of Hermitian forms is four-dimensional**, isomorphic to the Hermitian sector $\mathbb{M}_+=H_2(\mathbb{C})$ with the interval form and the cone of *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*.

Nothing owned by the companion articles is re-derived. The correspondence between bilinear forms and matrices, the module form and its Gram matrix, the Peirce basis and the matrix model are *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*, *Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint* and *Biquaternion Ideals and Peirce Decomposition*; the adjoint of the action and the two-sided operator are *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* and *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*; the positivity and the cone are *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*; the slice, the definite form and the internal group $U(2)$ are *Biquaternion Versors and the Orthogonal Group* and *Biquaternion Lie Group and Exponential Structure*.

## Forms, Operators and the Matrix Model

**Definition.** A **form** on the spinor module is a map $b:S\times S\to\mathbb{C}$ conjugate-linear in the first argument and linear in the second; the **adjoint form** is $b^{*}(s,t)=\overline{b(t,s)}$, and $b$ is **Hermitian** when $b^{*}=b$. The **bilinear operator** of $b$ is $T_b:S\to S^{*}$, $s\mapsto b(s,\cdot)$, and the two descriptions carry the same data.

**Proposition (the matrix model).** Every form is $b_M(s,t)=s^{\dagger}Mt$ for a unique element $M$ of $\mathbb{B}$, and

$$
b_M \text{ is Hermitian} \iff M \text{ is Hermitian} \iff T_b \text{ is self-adjoint};
$$

a form is alternating exactly when its operator is skew-adjoint, and the Hermitian forms are the fixed points of $b\mapsto b^{*}$.

*Proof.* The assignment $M\mapsto b_M$ is a $\mathbb{C}$-linear isomorphism of the $4$-dimensional algebra onto the space of forms, since $s^{\dagger}Mt$ determines $M$. Conjugating, $\overline{b_M(t,s)}=\overline{t^{\dagger}Ms}=s^{\dagger}M^{\dagger}t=b_{M^{\dagger}}(s,t)$, so $b_M$ is Hermitian exactly when $M^{\dagger}=M$. Under the identification $S^{*}\cong S$ by the module form, $T_b$ is the operator of the matrix $M^{\dagger}$ and its adjoint is $M$, so $(T_b)^{*}=T_{b^{*}}$; a form is Hermitian exactly when its operator is self-adjoint, and alternating exactly when the operator is skew-adjoint.

**Proposition (the equivariant form is the module form).** A form is **Clifford-equivariant**, $b(\tilde V\cdot s,t)=b(s,\tilde{V}^{*}\cdot t)$ for all $\tilde V\in\mathbb{B}$, exactly when $M$ commutes with $\mathbb{B}$:

$$
b \text{ equivariant} \iff \Phi(M)\in \mathbb{B}'=\mathbb{C}\cdot\mathrm{id} .
$$

*Proof.* $\Phi(M)$ commutes with $\Phi(\tilde V)$ for all $\tilde V$ exactly when $M$ is a scalar matrix, and $(\tilde V s)^{\dagger}M t=s^{\dagger}\tilde{V}^{*}Mt=b(s,\tilde{V}^{*}t)$ for all $s,t$ is exactly that. The scalar is real for $b$ Hermitian.

**Remark.** So on the biquaternion spinor module the equivariant Hermitian forms are the multiples of the module form, $\mathbb{R}_{>0}$ up to a phase, which is the Schur uniqueness of the module form read as a commutant statement: the commutant of a full matrix algebra acting on its simple module is the scalars. The general theory's warning about an isotropic spinor form has no instance here, for the reason recorded in *Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint*.

## The Completeness of the Action: the Fierz Identity

**Definition.** The **blades** are the four basis elements $e_0,e_1,e_2,e_3$ of $\mathbb{B}$, and the **bilinear covariants** of the module are

$$
b_{\mu}(s,t)=\langle L_{e_{\mu}}t,s\rangle_{*}=s^{\dagger}\Phi(e_{\mu})\,t ,\qquad \mu=0,1,2,3 .
$$

**Theorem (completeness, the Fierz identity).** The action $L:\mathbb{B}\to\mathrm{End}_{\mathbb{C}}(S)$ is an isomorphism, the four blade operators $L_{e_{\mu}}$ are a basis of $\mathrm{End}_{\mathbb{C}}(S)$, and the four covariants $b_{\mu}$ are a basis of the space of forms on $S$.

*Proof.* The algebra is a full matrix algebra, $\Phi(\mathbb{B})=M_2(\mathbb{C})$, acting faithfully on $S=\mathbb{C}^2$; hence $L$ is injective and $\dim L(\mathbb{B})=\dim\mathbb{B}=4=\dim\mathrm{End}_{\mathbb{C}}(S)$, so $L$ is an isomorphism and carries the basis $\{e_{\mu}\}$ to a basis. The bilinear statement is the same isomorphism read in the dual basis, by the adjunction of forms and operators. The independence was checked in the matrix model: $\Phi(e_0)=I$, $\Phi(e_k)=-i\sigma_k$, and $\{I,\sigma_1,\sigma_2,\sigma_3\}$ is the standard basis of $M_2(\mathbb{C})$, of rank $4$.

**Corollary (the covariant expansion).** Every form $b_M$ is a unique combination of the covariants,

$$
M=\sum_{\mu=0}^{3}c_{\mu}\,\Phi(e_{\mu}),\qquad c_{\mu}=\tfrac12\mathrm{Tr}\bigl(\Phi(e_{\mu})^{\dagger}M\bigr),
$$

because the blades are **orthogonal for the trace form** of the algebra, $\mathrm{Tr}(e_{\mu}^{\dagger}e_{\nu})=2\delta_{\mu\nu}$. The coefficients $c_{\mu}$ are the **Fierz coefficients** of the form, and the expansion is the Fierz rearrangement: a change of basis between the four blades and the four matrix units.

*Proof.* $\mathrm{Tr}(\Phi(e_0)^{\dagger}\Phi(e_0))=\mathrm{Tr}(I)=2$ and $\mathrm{Tr}(\Phi(e_j)^{\dagger}\Phi(e_k))=\mathrm{Tr}(\sigma_j\sigma_k)=2\delta_{jk}$, so the corrected trace pairing is the standard pairing on the orthogonal basis $\{I,\sigma_1,\sigma_2,\sigma_3\}$; the coefficients follow. The reconstruction was verified on random matrices to machine precision, with no mismatch.

**Remark (completeness as the double centraliser).** The Fierz identity and the double centraliser theorem are two readings of one fact. On the spinor module the action is onto, $L(\mathbb{B})=\mathrm{End}_{\mathbb{C}}(S)$, which is the statement that $\mathbb{B}$ is its own bicommutant there; on the regular module $\mathbb{B}$ the left multiplications have the right multiplications as commutant, as *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* records. The endomorphisms of $\mathbb{B}$ used in the two-sided operators are the module-level operators of this article with the parameter running over the algebra.

## The Covariants by Grade

**Theorem (the dagger classification).** The dagger of $\mathbb{B}$ is the reversion of the positive definite Clifford structure $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ whose vectors are the $ie_k$; a blade of degree $d$ in that structure satisfies $e_A^{\dagger}=(-1)^{d(d-1)/2}e_A$. In the biquaternion algebra $e_0$ is the identity and the three $e_k$ are, up to sign, the bivectors of that structure, $e_3=-\gamma_1\gamma_2$ with $\gamma_k=ie_k$, so

$$
e_0^{\dagger}=e_0,\qquad e_k^{\dagger}=-e_k ,\qquad \text{the covariant } b_{\mu} \text{ is Hermitian} \iff \mu=0 .
$$

Hence the four covariants split as **one Hermitian and three skew-Hermitian**:

$$
b_0(s,t)=s^{\dagger}t \ \text{(the module form)},\qquad b_k(s,t)=-i\,s^{\dagger}\sigma_k t .
$$

*Proof.* Reversion reverses the order of a product, so it acts on a degree-$d$ blade by $(-1)^{d(d-1)/2}$: the identity (degree $0$) and the bivectors are fixed and negated respectively. On the basis $e_0=1$ and $e_k=-\gamma_j\gamma_i$ with $\gamma_k=ie_k$ of square $+1$, reversion fixes the $\gamma$'s and negates the bivectors, so $e_0^{\dagger}=e_0$ and $e_k^{\dagger}=-e_k$. The covariant inherits the type from the blade, $b_{\mu}^{*}=b_{\bar{\mu}}$, by the corollary of the completeness theorem. Verified on the generators: $b_0(t,s)=\overline{b_0(s,t)}$ and $b_k(t,s)=-\overline{b_k(s,t)}$.

**Remark (the grade rule and its stability).** The general theory states the classification by the grade of the blade, Hermitian for $|A|\equiv0,3$ and skew-Hermitian for $|A|\equiv1,2\pmod 4$. The biquaternion algebra carries two Clifford structures and the rule is stable across them: in the structure $\mathbb{B}\cong\mathrm{Cl}(\mathbb{C}^2)$ of the generators $e_1,e_2$ with $e_3=e_1e_2$ the degrees are $0,1,1,2$, while in $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ the three $e_k$ are all bivectors of degree $2$; in both, $e_0$ is Hermitian and the three $e_k$ are skew-Hermitian, and the three degrees $1,1,2$ and $2,2,2$ all satisfy $|A|\not\equiv0,3$. The classification is therefore a property of the blade and the dagger, not of the chosen Clifford presentation.

**Theorem (the Hermitian forms are the Hermitian sector).** The space of Hermitian forms on the spinor module is the real four-dimensional space

$$
\mathrm{Bil}_{\mathrm{herm}}(S)=\mathbb{R}\{b_0,\,ib_1,\,ib_2,\,ib_3\}\cong\mathbb{M}_+ = H_2(\mathbb{C}),
$$

with the covariant coefficients of a Hermitian form real in the scalar slot and **purely imaginary** in the three skew slots; under the matrix model the Hermitian forms are the Hermitian matrices, and the interval form and the cone of $\mathbb{M}_+$ are those of *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*.

*Proof.* A Hermitian matrix has the expansion $a_0I+a_k\sigma_k$ with $a_0\in\mathbb{R}$ and $a_k\in\mathbb{R}$; in the blade basis $\sigma_k=i\Phi(e_k)$ this reads $a_0\Phi(e_0)+i\sum_k a_k\Phi(e_k)$, so the coefficients of $b_0$ are real and those of $b_k$ purely imaginary. Conversely a form with real scalar coefficient and imaginary skew coefficients is a real combination of $b_0$ and the $ib_k$, hence Hermitian. Checked over random Hermitian matrices: the scalar coefficient had vanishing imaginary part and the three skew coefficients vanishing real part in every trial.

**Remark (the $1+3$ splitting).** The splitting of the Hermitian forms into the scalar covariant and the three skew covariants is the splitting $\mathbb{M}_+=\mathbb{R}e_0\oplus i\mathbb{R}\{e_1,e_2,e_3\}$ of the Hermitian sector into its centre and its vector part. It is the covariant form of the decomposition $H_2(\mathbb{C})=\mathbb{R}\cdot\mathrm{id}\oplus\mathfrak{su}(2)$ used throughout the series for the Hermitian sector, and the positivity of the form — the cone — is the condition on the pair, not on either summand: the Hermitian form $a_0b_0+\sum_k a_k\,ib_k$ is **positive semidefinite** exactly when $a_0\ge\sqrt{\sum_k a_k^2}$.

## Invariance Under the Unitary Slice

**Theorem (the slice permutes the covariants).** For $\tilde C$ in the unitary slice $U=U(2)$ and every $\mu$,

$$
b_{\mu}(\tilde C\cdot s,\tilde C\cdot t)=b_{\,\tilde{C}^{*}e_{\mu}\tilde C}(s,t),
$$

so the slice acts on the covariants by the conjugation $\Gamma\mapsto \tilde{C}^{*}\Gamma \tilde C$ of the algebra; the scalar covariant $b_0$ is **invariant**, and the three skew covariants transform among themselves as a triplet.

*Proof.* $b_{\mu}(\tilde Cs,\tilde Ct)=(\tilde Cs)^{\dagger}\Phi(e_{\mu})\tilde Ct=s^{\dagger}\tilde{C}^{*}\Phi(e_{\mu})\tilde Ct=b_{\tilde{C}^{*}e_{\mu}\tilde C}(s,t)$ by the adjointness of the action, $\tilde{C}^{*}\Phi(e_{\mu})\tilde C=\Phi(\tilde{C}^{*}e_{\mu}\tilde C)$. For $\mu=0$ the inserted element is $\tilde{C}^{*}\tilde C=e_0$. For the triplet, $\tilde{C}^{*}\Phi(e_k)\tilde C=-i\tilde{C}^{*}\sigma_k \tilde C=-iR_{kl}\sigma_l=\Phi(R_{kl}e_l)$ with $R\in SO(3)$, the adjoint representation of $U(2)$ on $\mathfrak{su}(2)$. Checked on random slice elements for all four covariants, and for the invariance of $b_0$.

**Corollary (the invariants).** The invariants of the slice in the space of Hermitian forms are the multiples of the module form, so the trace pairing and the positivity of the Hermitian forms are slice invariants.

*Proof.* $b_0$ is invariant; a Hermitian form $a_0b_0+\sum_k a_k\,ib_k$ is invariant exactly when the triplet $(a_1,a_2,a_3)$ is fixed by every $R\in SO(3)$, hence is zero, since the adjoint representation of $SO(3)$ on $\mathbb{R}^3$ has no nonzero invariant vector.

**Remark (off the slice).** For an invertible $\tilde{Q}$ outside the slice the transformation of the covariants is the two-sided operator $\Theta_{\tilde{Q}}$ of *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, and the failure of form preservation is the horizontal defect of *Mixed Inner Conjugation and Hermitian Adjoint*: the covariant transforms by the two-sided operator and the form by the right multiplication by $\tilde{Q}\tilde{Q}^{*}$, so the slice is the exact locus on which the covariants are permuted by a conjugation and the forms are preserved.

## Worked Examples

**The scalar covariant is the module form.** $b_0(s,t)=s^{\dagger}t$ is positive definite, Hermitian, and invariant under the whole slice. Its diagonal $b_0(s,s)=\lvert s\rvert^2$ is the norm of the spinor, the quantity normalised to one for a unit spinor; the classification theorem places it alone among the Hermitian covariants.

**The triplet of a unit spinor.** For a spinor $s$ the three numbers $V_k=i\,b_k(s,s)=s^{\dagger}\sigma_k s$ are real, and for a normalised $s$ they form a unit vector $\tilde V=s^{\dagger}\boldsymbol{\sigma}s$; the trace-one element $\rho=\tfrac12\bigl(e_0+i\,V_k e_k\bigr)$ of $\mathbb{M}_+$ is Hermitian, and its three skew covariant coefficients are the coordinates of $\tilde V$. The three skew covariants of the spinor are the components of that vector.

**The vanishing triplet.** $\rho=\frac12 e_0$ has all three skew coefficients zero: the only Hermitian form with vanishing triplet is the centre of $\mathbb{M}_+$. The trace-one slice of the cone and its geometry are *The Bloch Ball as the Trace-One Slice of the Future Light Cone*.

**A null spinor.** A nonzero spinor $s$ with $\langle s,s\rangle_{\natural}=0$ — a zero divisor of the algebra — has a **nonzero** scalar covariant, $b_0(s,s)=s^{\dagger}s>0$. The covariants of this article are built from the positive definite module form and not from the general quaternionic bilinear form $\langle\cdot,\cdot\rangle_{\natural}$, which is the distinction between the two forms of *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*; a spinor is null for the module form only when it vanishes, and the null cone of the algebra lives in the vector part of $\mathbb{M}_+$ and not on the spinor.

## Summary

A **form** on the biquaternion spinor module is given by a $2\times2$ matrix, $b_M(s,t)=s^{\dagger}Mt$, and is Hermitian exactly when the matrix is; the **bilinear operator** $s\mapsto b(s,\cdot)$ has the adjoint form as its adjoint, so the Hermitian forms are the self-adjoint operators, and the **Clifford-equivariant** Hermitian forms are the multiples of the module form by the commutant theorem. The action of the algebra on the spinor module is an **isomorphism** $L:\mathbb{B}\to\mathrm{End}_{\mathbb{C}}(S)$ — the Fierz identity, exact because the biquaternion algebra is a full matrix algebra — so the four blades are a basis of the endomorphisms, the four **bilinear covariants** $b_{\mu}=\langle e_{\mu}t,s\rangle_{*}$ are a basis of the space of forms, and every form is a combination with the **Fierz coefficients** $c_{\mu}=\frac12\mathrm{Tr}(e_{\mu}^{\dagger}M)$, computed by the orthogonality $\mathrm{Tr}(e_{\mu}^{\dagger}e_{\nu})=2\delta_{\mu\nu}$ of the blades. The dagger is the reversion of the positive definite structure $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ at the vectors $ie_k$, so the classification by grade gives $e_0$ Hermitian and $e_1,e_2,e_3$ skew-Hermitian: **one Hermitian covariant, the module form, and three skew-Hermitian covariant ones**, a rule stable across the two Clifford structures the algebra carries. The Hermitian forms are the real four-dimensional space $\mathbb{R}\{b_0,ib_1,ib_2,ib_3\}\cong\mathbb{M}_+=H_2(\mathbb{C})$, with the positivity of $\mathbb{M}_+$ as its cone and the scalar-plus-triplet splitting as its centre-vector splitting. The **unitary slice** $U(2)$ permutes the covariants by $\Gamma\mapsto \tilde{C}^{*}\Gamma \tilde C$, fixes the scalar covariant, and rotates the three skew covariants by the adjoint representation of $SO(3)$, so the invariants are the multiples of the module form; off the slice the permutation is the two-sided operator and its defect.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde W\}$ | The spinor module, the unique simple left ideal |
| $\langle t,s\rangle_{*}=\mathrm{Sc}(s^{\dagger}t)$ | The module form; Hermitian, positive definite |
| $b_M(s,t)=s^{\dagger}Mt$ | A form; Hermitian iff $M$ Hermitian |
| $T_b:S\to S^{*}$, $s\mapsto b(s,\cdot)$ | The bilinear operator of $b$ |
| $b^{*}(s,t)=\overline{b(t,s)}$ | The adjoint form; $(T_b)^{*}=T_{b^{*}}$ |
| $L:\mathbb{B}\to\mathrm{End}_{\mathbb{C}}(S)$ | The action; an isomorphism (the Fierz identity) |
| $b_{\mu}(s,t)=\langle e_{\mu}t,s\rangle_{*}$ | The four bilinear covariants |
| $\mathrm{Tr}(e_{\mu}^{\dagger}e_{\nu})=2\delta_{\mu\nu}$ | Orthogonality of the blades for the trace form |
| $c_{\mu}=\frac12\mathrm{Tr}(e_{\mu}^{\dagger}M)$ | The Fierz coefficients of a form |
| $e_0^{\dagger}=e_0$, $e_k^{\dagger}=-e_k$ | One Hermitian and three skew-Hermitian covariants |
| $\mathbb{R}\{b_0,ib_1,ib_2,ib_3\}\cong\mathbb{M}_+$ | The Hermitian forms; the cone is positivity |
| $b_{\mu}(\tilde Cs,\tilde Ct)=b_{\tilde{C}^{*}e_{\mu}\tilde C}(s,t)$ | Slice covariance; $b_0$ invariant, triplet by $SO(3)$ |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the completeness of the Clifford action, the spinor module and the trace form.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the Fierz identity, the bilinear covariants and the classification by grade.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the double centraliser theorem and the commutant of a full matrix algebra on its simple module.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the spinor module, the invariant forms and the role of the Clifford action on the endomorphisms.
