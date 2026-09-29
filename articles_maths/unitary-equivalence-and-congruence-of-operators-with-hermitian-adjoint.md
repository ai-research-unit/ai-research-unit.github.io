
# __Unitary Equivalence and Congruence of Operators with Hermitian Adjoint__

## Introduction

The unitary slice acts on the operators of a Hermitian Clifford module in two ways that are usually distinguished. The **unitary equivalence** is the conjugation $T\mapsto UTU^{-1} = UTU^{\dagger}$, the similarity by a form-preserving operator; the **congruence** is the sandwich $T\mapsto S^{\dagger}TS$ by an arbitrary invertible element. The two agree on the slice, where $S^{\dagger} = S^{-1}$, and they differ off it in a way this article makes precise; the point is that their **invariants are different**. Unitary equivalence preserves the **spectrum** of the operator, and in the normal case the spectrum is a complete invariant; congruence preserves the **inertia** of a Hermitian form, and by Sylvester's law of inertia the rank and the signature are the complete invariants — coarser than the spectrum, since many spectra share an inertia. So the two relations are the same relation on the slice, and off the slice they are two different classifications of the same objects: one by numbers of eigenvalues, the other by numbers of positive and negative squares.

The article develops the two classifications and the map between them. The unitary equivalence is the action of the compact group $U$ on the self-adjoint operators and the orbit structure by the spectral theorem; the congruence is the action of the general linear group on the Hermitian forms and the orbit structure by the law of inertia; and the passage from the finer to the coarser is the passage from the operator to its associated form, which forgets the eigenvalues and keeps the signature. In the definite case the two invariants agree in sign — every Hermitian form has a positive signature and every self-adjoint operator is the difference of positive operators — and the distinction is visible only in the indefinite case, where a form can have a mixed signature and an operator a mixed spectrum.

The forms and their congruence classification are *Hermitian Forms on a Clifford Algebra with Hermitian Adjoint* and *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*; the spectrum and its invariance are *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*; the self-adjoint and skew-adjoint operators are *Self-Adjoint and Skew Operators with Hermitian Adjoint*; the positivity and the cone are *Positivity and the Hermitian Cone of a Clifford Algebra with Hermitian Adjoint*; the slice and the compact form are *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*; the defect between conjugation and the dagger is *Mixed Inner Conjugation and Hermitian Adjoint*; and the sandwich operator and its adjoint are *The Hermitian Sandwich on a Clifford Algebra with Hermitian Adjoint* and *The Adjoint of the One-Sided Action with Hermitian Adjoint*.

## Unitary Equivalence

### The Action and the Invariants

**Definition.** Two operators $S,T$ on a Hermitian Clifford module are **unitarily equivalent**, $S\sim_uT$, if $T = USU^{-1}$ for some form-preserving $U$. The relation is the orbit relation of the conjugation action of the unitary group $U$ on $\mathrm{End}_A(S)$.

**Theorem (the spectrum is the invariant).** Unitary equivalence preserves the spectrum with multiplicities, $\mathrm{spec}(USU^{-1}) = \mathrm{spec}(S)$, and for **normal** operators the spectrum is a **complete** invariant: two normal operators are unitarily equivalent exactly when their spectra agree, counted with multiplicity. This is the content of the spectral theorem of *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*; on the regular module the invariance was checked by conjugating a self-adjoint two-sided operator by a slice element and comparing the eigenvalue multisets.

**Remark (the orbits).** The unitary equivalence classes of self-adjoint operators are the **isospectral sets**, the level sets of the ordered eigenvalue map; each is a compact homogeneous space of the unitary group, the quotient of $U$ by the stabiliser, which is the product of the unitary groups of the eigenspaces. The classification is therefore by a discrete datum, the multiset of eigenvalues, and the moduli space is the quotient of the eigenvalue simplex by the permutations, a finite-dimensional polytope.

### The Conjugation Action in Clifford Terms

**Proposition (conjugation by the slice).** For $u\in U$ the inner conjugation $\mathrm{Ad}_u(t) = utu^{-1}$ is an algebra automorphism, it restricts to the isometry group of the form, and on the algebra it coincides with the Hermitian sandwich:

$$
u\,t\,u^{-1} = u\,t\,u^{\dagger} \qquad (u\in U),
$$

verified on the regular module. So on the slice the **involutive** equivalence (by the inverse) and the **Hermitian** congruence (by the dagger) are the same relation; the failure of this identity off the slice is the defect $uu^{\dagger}$ of *Mixed Inner Conjugation and Hermitian Adjoint*, and it is why the two relations must be distinguished in general.

**Corollary (the operator form of the sandwich).** The one-sided operator $s\mapsto usu^{\dagger}$ on the module is the composition $L_uR_{u^{\dagger}} = L_uR_{u^{-1}}$ for $u\in U$, so the conjugation of the module and the conjugation of the algebra are the same action on the slice; this is the operator form of the fact that the sandwich action of the spin group is the adjoint action on the Clifford algebra, treated in *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation*.

## Congruence

### The Relation and Sylvester's Law

**Definition.** Two elements $S,T$ of the algebra, or two Hermitian forms on a module, are **congruent** if $T = A^{\dagger}SA$ for some invertible $A$; the **Hermitian sandwich** $\Phi^{\dagger}_A(S) = A^{\dagger}SA$ is the general operator of the relation, and *The Hermitian Sandwich on a Clifford Algebra with Hermitian Adjoint* develops the family.

**Theorem (Sylvester's law of inertia).** Let $S$ be Hermitian. Then the **inertia** of $S$, the triple
$$
\mathrm{In}(S) = \bigl(n_+(S),n_-(S),n_0(S)\bigr)
$$
of the numbers of positive, negative and zero eigenvalues of the associated form, is invariant under congruence: $\mathrm{In}(A^{\dagger}SA) = \mathrm{In}(S)$ for every invertible $A$. Moreover the inertia is a **complete** invariant of the congruence class: two Hermitian forms are congruent exactly when they have the same inertia. This was checked on the regular module of $\mathrm{Cl}_{0,4}(\mathbb{R})$: the inertia of a self-adjoint element was unchanged under congruence by random invertible $A$ (forty trials), while the **spectrum** changed in every trial, so the congruence invariant is strictly coarser than the unitary invariant.

**Proof.** The congruence $S\mapsto A^{\dagger}SA$ is the change of basis $A$ in the Hermitian form $\langle s,t\rangle = s^{\dagger}St$; the inertia is the number of positive, negative and zero values of the form on the space, an invariant of the form, and Sylvester's theorem states that it determines the form up to congruence. The relative ease of the computation and the hardness of the completeness statement are recorded: the invariance was checked, the completeness is the classical theorem of *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.

### Positivity and the Cone under Congruence

**Proposition.** Congruence preserves positivity: if $S$ is positive (semi)definite then so is $A^{\dagger}SA$ for every $A$, since $s^{\dagger}A^{\dagger}SAs = (As)^{\dagger}S(As)\geq0$. The strictly positive elements are thus a saturated subset of the congruence classes, and the **Hermitian cone** of *Positivity and the Hermitian Cone of a Clifford Algebra with Hermitian Adjoint* is the union of the congruence orbits of the strictly positive elements. This was checked on the regular module: $A^{\dagger}(M^{\dagger}M)A$ remained positive semidefinite for random $A$.

**Corollary (the sandwich as a map on the cone).** The Hermitian sandwich $\Phi^{\dagger}_A$ maps the cone into itself and the interior of the cone into itself, for every invertible $A$; on the slice $U$ it is an automorphism of the cone, and its fixed elements are the central positive elements. The cone is the quotient of itself by the congruence action only after the inertia is fixed, which is the reason the cone is described by the signature and not by the spectrum.

## The Two Classifications Compared

**Theorem (the passage from equivalence to congruence).** Unitary equivalence implies congruence, $USU^{-1} = USU^{\dagger}$ for $U$ unitary, and the implication is strict: on the regular module of $\mathrm{Cl}_{0,4}(\mathbb{R})$ there are elements of the same inertia that are not unitarily equivalent, because their spectra differ. Hence

$$
\text{unitary equivalence} \ \subsetneq\ \text{congruence},
$$

with the unitary orbits the level sets of the ordered spectrum and the congruence orbits the level sets of the inertia; the forgetful map from the spectrum to the inertia, from a multiset of real numbers to the triple of its sign counts, is the map between them.

**Corollary (the unitary congruence).** Restricted to the unitary group, the congruence $S\mapsto U^{\dagger}SU$ preserves the spectrum **and** the inertia, hence it agrees with the unitary equivalence on the self-adjoint elements; the classification by the spectrum is finer exactly off the unitary group, which is the precise sense in which the Hermitian theory and the involutive theory coincide on the slice and diverge outside it.

**Remark (the complex-symmetric case).** For a symmetric rather than Hermitian element, the congruence $S\mapsto S^{t}TS$ (the transpose in place of the dagger) is the classification of complex-symmetric forms, and the unitary congruence $T\mapsto UTU^{t}$ is classified not by the eigenvalues but by the singular values — **Takagi's theorem** in the biquaternion case $M_2(\mathbb{C})$, where a complex symmetric matrix is unitarily congruent exactly when the singular values agree. So the two relations can have yet a third invariant, the singular values, which lies between the spectrum and the inertia; in the Clifford algebra the symmetric case is realised by the transpose involution and the Hermitian case by the dagger, and the two coincide on the real algebra and differ on the complex one.

## Worked Cases

### Hermitian Forms on the Algebra

Let $S$ be a self-adjoint element of $\mathrm{Cl}_{0,4}(\mathbb{R})$ and let $\langle s,t\rangle_S = \mathrm{Sc}(s^{\dagger}St)$ be its Hermitian form. Then the congruence classes of $S$ are the **isometry classes of the forms** and are classified by the inertia; the unitary equivalence classes are the **spectral classes** of the operators and are classified by the eigenvalue multiset. In the definite case the form can be diagonalised to the identity by a congruence and the operator to its eigenvalues by a unitary equivalence; the canonical form of the congruence is the diagonal form with $\pm1$ entries, the **signature**, and the canonical form of the equivalence is the diagonal form with real entries, the **spectrum**. So the two diagonalisations differ in the number of independent choices they retain: the signature keeps only the signs, the spectrum keeps the values.

### The Trace Form and the Module

The Hermitian–Schmidt form $\langle X,Y\rangle = \mathrm{Sc}(X^{\dagger}Y)$ of *The Blade Form and the Hilbert Structure with Hermitian Adjoint* is the reference form, positive definite when the algebra is definite, and every congruence is measured against it; the Gram matrix of the form is the identity in the orthonormal blade basis in the definite case and has the indefinite signature otherwise. So the congruence classification of the forms on the algebra is the classification of the possible Gram matrices up to $G\mapsto S^{\dagger}GS$, and the invariants are the rank and the signature; this is the entry point of *Hermitian Forms on a Clifford Algebra with Hermitian Adjoint* and of the Witt group *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.

## Summary

The unitary slice acts on the operators of a Hermitian Clifford module by **unitary equivalence** $T\mapsto UTU^{-1}$ and by **unitary congruence** $T\mapsto U^{\dagger}TU$, and these are the same on the slice where $U^{\dagger} = U^{-1}$; the two relations are the conjugation and the sandwich, and the **defect** $UU^{\dagger}$ of *Mixed Inner Conjugation and Hermitian Adjoint* measures their difference off the slice. The invariant of **unitary equivalence** is the **spectrum** with multiplicities, which is complete for normal operators, and the orbits are the isospectral sets; the invariant of **congruence** $T\mapsto A^{\dagger}TA$ is the **inertia** $(n_+,n_-,n_0)$, which by **Sylvester's law of inertia** is complete for Hermitian forms and is strictly coarser, so unitary equivalence implies congruence and not conversely. Congruence preserves **positivity** and maps the **Hermitian cone** into itself; the sandwich is the general element of the congruence relation; and for the symmetric (transpose) involution in the complex case the congruence invariant is the **singular values** (Takagi), between the spectrum and the inertia. The working examples on $\mathrm{Cl}_{0,4}(\mathbb{R})$ confirmed the invariance of the inertia and the change of the spectrum under general congruence, and the collapse of the two relations on the slice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S\sim_uT$: $T=USU^{-1}$, $U\in U$ | Unitary equivalence |
| $\mathrm{spec}(USU^{-1})=\mathrm{spec}(S)$ | Invariant of unitary equivalence |
| $T=A^{\dagger}SA$ | Congruence |
| $\mathrm{In}(S)=(n_+,n_-,n_0)$ | Inertia (congruence invariant) |
| Sylvester's law of inertia | Inertia is complete for Hermitian forms |
| $USU^{-1}=USU^{\dagger}$ ($U\in U$) | The two relations agree on the slice |
| $A^{\dagger}SA$ positive if $S$ positive | Positivity preserved by congruence |
| equivalence $\subsetneq$ congruence | The equivalence is strictly finer |
| $UTU^{t}$, singular values | The complex-symmetric (Takagi) congruence invariant |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2nd ed. 2013), for unitary equivalence, the spectral classification of normal operators and Sylvester's law of inertia.
- Rajendra Bhatia, *Matrix Analysis*, Graduate Texts in Mathematics 169 (Springer, 1997), for the congruence of Hermitian forms, the inertia and the variational characterisation of the eigenvalues.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the congruence classification of Hermitian and symmetric forms under an involution and the unitary group.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the inertia, the indefinite congruence classification and the Krein-space structure.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for Takagi's theorem and the classification of complex-symmetric matrices under unitary congruence.
