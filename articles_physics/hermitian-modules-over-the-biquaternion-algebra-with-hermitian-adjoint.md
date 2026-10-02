# __Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the algebra of operators of the framework, and its two distinguished sectors carry the two sides of the physical dictionary: the Hermitian subspace $\mathbb{M}_+$ is the informational sector, the operators of a two-state system, and the anti-Hermitian subspace $\mathbb{M}_-$ is the material sector, Minkowski space (*The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*). Both readings rest on the module theory: $\mathbb{B}\cong M_2(\mathbb{C})$ has one simple module $S\cong\mathbb{C}^2$, the **spinor module**, and the framework's linear structure is that module together with the identification (*Modules over the Biquaternion Algebra*, *The Spinor Module in Biquaternionic Form and Its Lorentz Action*).

This article asks the metric question of that module: when does the spinor module carry a positive definite **inner product** that the algebra acts on by operators with adjoints? The answer is the axiom

$$
(\tilde R\cdot s,t)=\bigl(s,\tilde R^{*}\cdot t\bigr),
$$

which says exactly that the action is a $*$-representation, and it is the condition that makes the informational sector the observables, the generators skew-adjoint, and the Dirac-type operator self-adjoint. The mathematical statement, its proof and its uniqueness are in *Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint* of the mathematical series, cited here; what this article adds is the physical reading, the two traps, and the operator that the axiom produces.

## The Module Axiom as the Physicality of the Inner Product

**Definition (the Hermitian form of the module).** On the spinor module $S$ a **Hermitian form** is a complex sesquilinear form, linear in the second argument and conjugate-linear in the first; the axiom of a **Hermitian Clifford module** is $(\tilde R\cdot s,t)=(s,\tilde R^{*}\cdot t)$ for every element $\tilde R$ and every pair of spinors.

**Physical reading.** The form is the inner product of the internal Hilbert space, and the axiom is the statement that it is the *right* inner product: with it the action of the algebra becomes a $*$-representation, so every operator of the algebra has an adjoint and the framework's linear algebra is Hilbert-space linear algebra. Without the axiom one has a vector space with an action; with it one has the operator algebra of a quantum system. The form is not an extra choice: on the irreducible module it is unique up to a positive scalar (Schur, *Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint*), so the internal inner product is canonical and the Born-rule normalisation is a choice of unit and not a choice of structure.

**Proposition (the sector criterion).** The axiom is equivalent to the two statements that every element of the informational sector acts by a **self-adjoint** operator and every element of the material sector acts by a **skew-adjoint** one:

$$
(\tilde R\cdot s,t)=+(s,\tilde R\cdot t)\ (\tilde R\in\mathbb{M}_+),
\qquad
(\tilde R\cdot s,t)=-(s,\tilde R\cdot t)\ (\tilde R\in\mathbb{M}_-).
$$

**Physical reading.** The informational sector is the observables: Hermitian operators, real expectation values. The material sector is the generators: skew-adjoint operators, purely imaginary spectrum, unitary one-parameter groups $e^{ta}$. The two sectors of the algebra are the two roles an operator can play, and the axiom is what fixes which sector plays which role.

## The Two Traps

**The first trap: the interval form is not the internal form.** The form of this article is the scalar form of the dagger,

$$
(\tilde R,\tilde T)=\mathrm{Sc}(\tilde R^{*}\tilde T)=\sum_{\mu=0}^{3}R_\mu^{*}T_\mu ,
$$

positive definite on the whole eight-dimensional real algebra. The **biquaternion norm** $N(\tilde{Q})=\sum_\mu Q_\mu^{2}$, complex and indefinite, is a different form on the same algebra, and its restriction to the material sector is the Minkowski interval (*Biquaternion Norm and Invertibility*, *The Clifford Structure of the Biquaternion Algebra*). Positivity lives on the internal space, the signature $(1,3)$ on the material space, and no statement of one form transfers to the other. Writing the interval where the inner product belongs is the error that turns the state space into a cone and the symmetry group into the Lorentz group (*Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint*).

**The second trap: the naive spinor form can be isotropic, but not here.** The general theory warns that the restriction of the scalar form to a minimal left ideal can be *totally isotropic* — of Gram matrix zero — in the split signatures, so that the naive construction does not give a spinor inner product (*Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*). In the biquaternion algebra this failure **cannot occur**: the scalar form of the dagger is positive definite, so every subspace inherits a positive definite restriction, and the standard idempotents are self-adjoint, $\tilde\Pi_1^{*}=\tilde\Pi_1$, which is exactly the condition the general construction asks for. Concretely, on the ideal $S=\mathbb{C}\{\tilde\Pi_1,\tilde T\}$ the Gram matrix is $\tfrac12 I_2$ in that basis, positive definite: the spinor inner product exists and needs no correction. The framework is the resolved case, not the exceptional one.

## The Spinor Module and Its Compact Symmetry

**Theorem (the slice acts by unitaries).** The unitary slice $U=\{\tilde A:\tilde A^{*}\tilde A=e_0\}=U(2)$ acts on the spinor module by unitary operators, $(\tilde A\cdot s,\tilde A\cdot t)=(s,t)$, so $\tilde A\mapsto\rho(\tilde A)|_S$ is a unitary representation of $U(2)$ on the internal Hilbert space.

**Physical reading.** The internal symmetry group of the spinor module is the compact group $U(2)$, and it is the group of unitaries of the internal space: the internal rotations, the internal phase, and nothing else. Its Lie algebra is the material sector, $\mathbb{M}_-\cong u(2)$, whose elements are the skew-adjoint generators $e_1,e_2,e_3$ and $ie_0$; the anticommutation and commutation relations of those generators are the internal Clifford relations (*One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*).

**Remark (why the Lorentz group is not the internal symmetry).** The norm-one slice $\mathbb{B}^{\times}_1=SL(2,\mathbb{C})$, the spin group of the material sector, is **not** a group of unitary operators of the internal form: only its compact part $SU(2)$ is. There is no positive definite form preserved by the spinor representation of the Lorentz group — the Lorentz-invariant bilinear pairing of spinors is the antisymmetric $\varepsilon$, not an inner product — and this is the operator-level reason the material symmetry is a symmetry of the *interval* and the internal symmetry is a symmetry of the *inner product*. The two groups act on different structures of the same algebra, and the framework's unitary group of the module is $U(2)$.

## The Dirac Element of the Module

**Definition.** The **Dirac element** of the module is the sum of the left multiplications by the generators,

$$
D_{\mathrm{alg}}=\sum_{k=1}^{3}L_{e_k},
$$

which preserves the left ideals and so acts on the spinor module.

**Theorem (square, adjoint and gap).** On the spinor module the generators act by $c(e_k)=-i\sigma_k$, and

$$
D_S=-i\bigl(\sigma_1+\sigma_2+\sigma_3\bigr),
\qquad
D_S^{*}=-D_S,
\qquad
D_S^{2}=-3\,\mathrm{id},
\qquad
D_S^{*}D_S=3\,\mathrm{id}>0 .
$$

The real operator $iD_S$ is self-adjoint with spectrum $\{\pm\sqrt3\}$ and orthonormal eigenspinors, so the element is invertible, with no zero mode, and a gap of $\sqrt3$.

**Physical reading.** The operator is the internal Clifford element: the sum of the three internal complex structures, an internal "Dirac-type" operator rather than the spacetime Dirac operator. Its two structural properties are the ones the axiom guarantees: it is skew-adjoint, and its Hermitian square is positive. Positivity of the square is the statement that the internal Hilbert space has no negative-norm direction, and invertibility is the statement that the framework has no internal zero mode at this level: the internal Clifford element has a spectral gap. The spacetime Dirac operator $\sum_\mu e_\mu\partial_\mu$, its square and its analysis are a different operator on a different carrier and are in *The Dirac Equation in Biquaternionic Form* and *The Spinor Module in Biquaternionic Form and Its Lorentz Action*; the present one is the algebraic element without derivatives.

**Corollary (formal self-adjointness of the Dirac operator with derivatives).** For the operator $D=\sum_k\rho(e_k)\partial_k$ with $\partial_k^{*}=-\partial_k$ the two sign flips cancel and $D^{*}=D$: the Dirac operator of a Hermitian Clifford module is formally self-adjoint, and its square is the positive operator $\lVert D\cdot\rVert^{2}$. This is the property that makes the framework's Dirac dynamics unitary at the level of the inner product, and its analysis belongs to the analysis of the algebra.

## Summary

The spinor module of the biquaternion algebra carries a canonical positive definite **inner product**, the scalar form of the dagger, and the algebra acts on it by a $*$-representation: the axiom $(\tilde R\cdot s,t)=(s,\tilde R^{*}\cdot t)$ is equivalent to the informational sector acting by observables and the material sector by generators. The form is unique up to a positive scalar on the irreducible module, so the internal inner product is not a choice. The two traps are that the **interval form** $N$, complex and indefinite, must never be used as the internal form, and that the general warning of an *isotropic* spinor form has no instance here, because the scalar form is positive definite and the standard idempotents are self-adjoint: on the minimal left ideal the Gram matrix is $\tfrac12 I_2$. The compact group $U(2)$ acts by unitaries on the module, while the Lorentz spin group $SL(2,\mathbb{C})$ does not — only $SU(2)$ does — because the material symmetry preserves the interval and the internal symmetry preserves the inner product. The **Dirac element** $D_{\mathrm{alg}}=\sum_kL_{e_k}$ acts as $-i(\sigma_1+\sigma_2+\sigma_3)$, is skew-adjoint, has square $-3\,\mathrm{id}$ and positive Hermitian square $3\,\mathrm{id}$; the real operator $iD_{\mathrm{alg}}$ is a self-adjoint internal observable with spectrum $\{\pm\sqrt3\}$, and the module has no zero mode.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S$ | The spinor module, $\cong\mathbb{C}^2$; the internal Hilbert space |
| $(\tilde R\cdot s,t)=(s,\tilde R^{*}\cdot t)$ | The axiom; the action is a $*$-representation |
| $\mathbb{M}_+$ self-adjoint, $\mathbb{M}_-$ skew | Observables and generators |
| $(\tilde R,\tilde T)=\mathrm{Sc}(\tilde R^{*}\tilde T)=\sum_\mu R_\mu^{*}T_\mu$ | The internal form; positive definite |
| $N(\tilde{Q})=\sum_\mu Q_\mu^{2}$ | The interval; indefinite; never the internal form |
| Gram $=\tfrac12 I_2$ on $S=\mathbb{C}\{\tilde\Pi_1,\tilde T\}$ | The spinor inner product; not isotropic |
| $U=U(2)$ | The internal symmetry; unitary on $S$ |
| $SL(2,\mathbb{C})$, $SU(2)$ | Material spin group; only the compact part is unitary on $S$ |
| $D_{\mathrm{alg}}=\sum_kL_{e_k}=-i(\sigma_1+\sigma_2+\sigma_3)$ | Dirac element of the module |
| $D_{\mathrm{alg}}^{2}=-3\,\mathrm{id}$, $D_{\mathrm{alg}}^{*}D_{\mathrm{alg}}=3\,\mathrm{id}$ | Clifford square and positive Hermitian square; gap $\sqrt3$ |

## Further Reading

- *Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/hermitian-modules-over-the-biquaternion-algebra-with-hermitian-adjoint.md`), the mathematical companion, for the axiom, the Gram matrices, Schur uniqueness and the Dirac element.
- *Modules over the Biquaternion Algebra* (`articles_physics/modules-over-the-biquaternion-algebra.md`), for the classification of the modules, the simple module and the two chiralities.
- *The Spinor Module in Biquaternionic Form and Its Lorentz Action* (`articles_physics/the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.md`), for the module, the two chiral halves and the $SL(2,\mathbb{C})$ action.
- *The 2×2 Matrix Element Representation of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-of-biquaternions.md`), for $\Phi(e_k)=-i\sigma_k$ and the matrix realisation.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* (`articles_physics/the-hermitian-subspace-m-plus-as-the-informational-sector.md`), for the observables, the state cone and the Bloch ball.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* (`articles_physics/the-anti-hermitian-subspace-m-as-the-material-sector.md`), for the generators, the four-vectors and the interval.
- *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_physics/one-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the Clifford action, its adjoint and the internal group.
- *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_physics/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the two forms, the amplitude and the observables.
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_physics/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the cone of states, the polar decomposition and the internal conjugation.
- *The Dirac Equation in Biquaternionic Form* (`articles_physics/the-dirac-equation-in-biquaternionic-form.md`), for the spacetime Dirac operator, its square and its dynamics.
