# __Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint__

## Introduction

This is the physics companion of *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint* (`articles_maths/hermitian-forms-over-the-biquaternion-algebra-and-the-unitary-witt-group-with-hermitian-adjoint.md`). The forms and their classification are the same; what changes is the reading. In the framework of these articles the **Hermitian forms of the dagger are the internal forms** — the forms that live on the informational sector and whose positive cone is the set of states — while the **quaternion norm $N$ is the interval**, the form that lives on the material sector and whose cone is the light cone. The mathematics has one classification theorem; the physics has two forms of different type, and the first task of this article is to keep them apart.

The physical statements are: the internal form is positive definite and its cone is the Bloch ball; the isometry group of the internal form is the internal unitary group $U(2)$; the interval is indefinite and its isometry group is the Lorentz group; and the classification invariant of the **states** is the inertia, with the signature playing the role of the causal label. The Witt group statement is the framework's version of "there is only one invariant": the internal form has a single non-degenerate class up to hyperbolic splitting.

## The Two Forms and the Two Sectors

**The internal form.** On the informational sector the relevant form is

$$
h(\tilde R,\tilde T) = \tilde R^{\dagger}\tilde T,\qquad (\tilde R,\tilde T)=\mathrm{Sc}(\tilde R^{\dagger}\tilde T)=R_{0}^{*}T_{0}+R_{1}^{*}T_{1}+R_{2}^{*}T_{2}+R_{3}^{*}T_{3},
$$

positive definite on the whole algebra, with the unit matrix as its Gram matrix. Its positive cone is the set of positive semidefinite elements, which is the state space: the trace-one slice is the **Bloch ball** of *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* and the rank-one boundary is the pure states. The form is the framework's inner product of amplitudes.

**The interval.** On the material sector the relevant form is the **quaternion norm**

$$
N(\tilde R)=R_{0}^{2}+R_{1}^{2}+R_{2}^{2}+R_{3}^{2},
$$

complex-valued on the complexified algebra, indefinite and isotropic on the null cone $\{N=0\}$; it is the form of the interval, and it is **not** a form of the dagger, so it is not in the classification of the mathematics article at all. The reader who puts $N$ and $(\cdot,\cdot)$ in the same table will compute wrong inertias: the first has signature $(1,3)$-type (mostly minus after the standard sign convention) and the second is $(4,0)$.

**Proposition (the two isometry groups).** The isometry group of the internal form is the unitary slice $U(e_{0})=U(2)$, compact, of real dimension four; the isometry group of the interval (up to the phase ambiguity of the double cover) is the Lorentz group, non-compact, of real dimension six. The two groups act on the two sectors and are not subgroups of one another.

*Proof.* $S^{\dagger}S=e_{0}$ for the first; $N(S\tilde R)=N(\tilde R)$ for the second, with $S$ of norm one, is the similarity of the interval of *Biquaternion Rotations and Lorentz Transformations*. Verified in the matrix model.

## Inertia as the Causal Label

**The physical reading of the inertia.** For a Hermitian element $H$ of the informational sector the inertia $(p,q,r)$ of the mathematics article is the triple of the dimensions of the positive, negative and null directions of the internal form restricted to the state space of $H$. In the physics the positive directions of a **state** are its populations and the negative directions of a Hermitian **operator** are the "negative populations" of the indefinite cases; the trace-one slice remembers the sum, not the signs, and the **signature $\sigma=p-q$ is the physical label that the trace forgets**.

**Proposition (the causal classification of an internal form).** A non-degenerate Hermitian element of the informational sector is

- **positive definite** (inertia $(2,0)$): a proper internal state, all directions positive;
- **indefinite** (inertia $(1,1)$): a hyperbolic internal form, with one positive and one negative direction;
- **null** (rank one): a pure state direction plus a null direction, as for the lightlike element $e_{0}+ie_{3}$ of *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*.

The parallel with the causal classification of an interval-like vector is exact in form and different in content: there the cone is the light cone of the material sector, here it is the state cone of the informational sector, and the framework keeps the two cones apart.

**Proposition (the states and the hyperbolic form).** The reader must not read the hyperbolic case as "unphysical". The hyperbolic plane $\mathrm{diag}(1,-1)$ is the internal form of a **signed state** — a state with one positive and one negative internal direction — and it is exactly the form that appears in the signed and mixed two-sided operators of *Mixed Inner Conjugation and Hermitian Adjoint* and in the **fermion parity** sector of the graded articles. The negativity is not an inconsistency; it is the signature of a genuinely two-sector object.

## The Isometry Group and the Internal Symmetries

**Proposition (the internal group is the isometry group of the internal form).** The internal symmetries of the framework, the maps preserving the internal form $(\cdot,\cdot)$, are exactly the elements of $U(2)=U(e_{0})$, and they act on the algebra by the unitary sandwiches $\Theta_{\tilde{Q}}$, $\tilde{Q}\in U$. The Lorentz symmetries, which are the isometries of the **interval**, are not isometries of the internal form except on the compact part: a boost changes $(\cdot,\cdot)$ and preserves $N$.

*Proof.* The first statement is the mathematics article; the second is the comparison of the two invariants, $S^{\dagger}S=e_{0}$ against $N\circ S=N$. Verified: a boost of the corpus satisfies the second and not the first.

**Physical consequence, stated as the article's warning.** Every place where the framework says "the internal group is $U(2)$" is a statement about the isometry group of the **unit form**; every place where it says "the Lorentz group" is a statement about the isometry group of the **norm**. Replacing one by the other changes the theory, and the two forms have different signatures, so no theorem of one passes to the other.

## The Witt Group: One Invariant is Enough

**The physical reading of the classification.** The mathematics article proves that the non-degenerate Hermitian forms of the algebra modulo the hyperbolic ones form $\mathbb{Z}$, generated by the unit form and computed by the signature. The physical reading is the following. **The internal form of the framework has a single classification invariant, the signature, and the hyperbolic forms carry no internal information**: a hyperbolic form, whatever its rank, is equivalent to the trivial form once the hyperbolic summands are dropped. Two internal forms with the same signature are the same form up to a change of the internal basis (up to congruence), and the congruence is exactly the two-sided operator on the form matrix, which is the framework's **change of the internal frame**.

**Physical consequence (the state is the class).** The positive definite class is the class of the unit form and is the class of a **proper state**; the hyperbolic class is the class of a **signed state** and is trivial in the Witt group; the negative classes are the negatives of the positive ones, i.e. the orientation-reversed internal frames. The signature, not the full form, is the observable, and this is the same statement as in the interval sector, where the signature of the metric is the physical content and the metric's coordinate form is not.

## Worked Examples

**A proper state and a signed state.** The unit form $\mathrm{diag}(1,1)$ is the internal form of a proper state; the form $\mathrm{diag}(1,-1)$ is the internal form of a signed state and is the hyperbolic plane. Their signatures $2$ and $0$ distinguish them, and the trace-like normalisations do not: the two have the same rank.

**The collapse under a null frame.** The congruence by the null element $S=e_{0}+ie_{3}$ gives $\mathrm{rank}$-one forms: the internal form degenerates, the state cone collapses onto the null direction, and the rank drop is the algebraic trace of the lightlike degeneracy of the framework. The same computation is in the mathematics article and in *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*.

**A boost against an internal rotation.** A boost $S$ with $N(S)=1$ and $S\notin U$ changes the interval label of an element and leaves the internal form alone in the sense of the congruence class only after the appropriate renormalisation; an internal rotation $S\in U$ preserves both. This is the operational difference between the two groups, and it is the reason the framework never identifies them.

**The Witt class of a superposed state.** A state built as the orthogonal sum of a positive and a negative internal direction has signature zero, i.e. it is hyperbolically equivalent to nothing: the "cancellation" is the algebraic form of a pair of internal sectors cancelling in the invariant, and it is the reason the framework's superalgebra articles can speak of a **graded** internal structure whose total signature is zero while the two sectors are individually non-trivial.

## Summary

The Hermitian forms of the dagger are the **internal forms**, positive definite, with the unit form as the reference and the Bloch ball as the positive cone; the quaternion norm is the **interval**, indefinite and of a different type, and the two must not be placed in the same classification. The isometry group of the internal form is the internal unitary group $U(2)$; the isometry group of the interval is the Lorentz group; the congruence $H\mapsto S^{\dagger}HS$ is the change of the internal frame and is exactly a two-sided operator of the corpus. The classification invariant of an internal form is the **inertia** and its signature, the hyperbolic forms are internally trivial, and the non-degenerate internal forms modulo the hyperbolic ones form the group $\mathbb{Z}$ generated by the unit form. The causal, hyperbolic and null cases of the classification are the proper, signed and lightlike internal states, and the cancellation of signatures is the algebraic form of the graded internal structure of the framework.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\tilde R,\tilde T)=\mathrm{Sc}(\tilde R^{\dagger}\tilde T)$ | The internal form; positive definite; cone the Bloch ball |
| $N(\tilde R)=\sum_{\mu}R_{\mu}^{2}$ | The interval; indefinite; **not** a form of the dagger |
| $U(e_{0})=U(2)$ | Isometry group of the internal form; the internal group |
| Lorentz group | Isometry group of the interval; not of the internal form |
| $(p,q,r)$, $\sigma=p-q$ | Inertia and signature; the physical label of an internal form |
| $\mathrm{Hyp}=\mathrm{diag}(1,-1)$ | The hyperbolic plane; the signed state; Witt class $0$ |
| $H\mapsto S^{\dagger}HS$ | The change of internal frame; a two-sided operator |
| $W\cong\mathbb{Z}$ | Internal forms up to hyperbolic splitting; generated by the unit form |

## Further Reading

- *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint* (`articles_maths/hermitian-forms-over-the-biquaternion-algebra-and-the-unitary-witt-group-with-hermitian-adjoint.md`), the mathematical companion.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* (`articles_physics/the-hermitian-subspace-m-plus-as-the-informational-sector.md`), for the cone, the states and the trace-one slice.
- *Biquaternion Norm and Invertibility* (`articles_physics/biquaternion-norm-and-invertibility.md`), for the interval, its isotropy and the null cone.
- *Biquaternion Versors and the Orthogonal Group* (`articles_physics/biquaternion-versors-and-the-orthogonal-group.md`), for the isometry group of the interval and the double cover.
- *Biquaternion Rotations and Lorentz Transformations* (`articles_physics/biquaternion-rotations-and-lorentz-transformations.md`), for the rotations and boosts used in the examples of the two groups.
- *Biquaternion Lorentzian and Conformal Geometry* (`articles_physics/biquaternion-lorentzian-and-conformal-geometry.md`), for the light cone and the conformal structure of the interval sector.
- *The Sandwich Action in Subspaces* (`articles_physics/the-sandwich-action-in-subspaces.md`), for the action of the congruences on the subspaces of the algebra.
- *The Material/Informational Split as a Superselection Structure in Biquaternionic Form* (`articles_physics/the-material-informational-split-as-a-superselection-structure-in-biquaternionic-form.md`), for the two-sector reading of the two forms.
- *Mixed Inner Conjugation and Hermitian Adjoint* (`articles_maths/mixed-inner-conjugation-and-hermitian-adjoint.md`), for the signed and mixed forms of the internal structure.
- *Biquaternion Spectral Theory* (`articles_physics/biquaternion-spectral-theory.md`), for the element spectra entering the inertia.
