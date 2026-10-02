# __Mixed Inner Conjugation on the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

An internal observable is an element of the algebra, and an internal amplitude acts on it in one of four ways, according to two independent binary choices: whether the left factor is conjugated by the real structure and whether the right factor is inverted or dagged. Writing $\Phi^{\theta,\rho}_{\tilde{Q}}(\tilde T)=\theta(\tilde{Q})\tilde T\rho(\tilde{Q})$ with $\theta$ equal to the identity or to the coefficient conjugation $\bar{\cdot}$ and $\rho$ equal to the inverse or the Hermitian conjugation ${}^{*}$, the four operators are the inner conjugation, the signed inner conjugation, the Hermitian sandwich and the signed Hermitian sandwich. The mathematics is *Mixed Inner Conjugation on the Biquaternion Algebra with Hermitian Adjoint*; the unsigned members, their composition, kernel, image and cone, are *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, and the rotation reading of the inner conjugation is *Biquaternion Versors and the Orthogonal Group*. Nothing owned by those articles is re-derived.

The physical identification of the twist is the corpus's: **the coefficient conjugation $\bar{\cdot}$ is the charge-conjugation real structure**, the only conjugate-linear automorphism of the algebra, with fixed points the real quaternions $\mathbb{H}_{\mathbb{B}}$ and with the property that it exchanges the defining module $S$ and its conjugate $\bar{S}$ (*The Neutrino and Majorana Fermions in Biquaternionic Form*, *Biquaternion Ideals and Peirce Decomposition*). So the family is: conjugate an operator by an amplitude, with or without the charge-conjugation twist, and with the amplitude inverted or undone by the dagger. The two facts that the article carries are then physical statements about $\mathbb{B}$.

The first is that **the dagger sandwich differs from the conjugation by the state that the amplitude prepares**: the exact identity $\Phi^{\theta,{}^{*}}_{\tilde{Q}}=R_{\tilde{Q}\tilde{Q}^{*}}\circ\Phi^{\theta,\mathrm{inv}}_{\tilde{Q}}$ says that passing from the conjugating description to the Hermitian one is the right multiplication by the cone element $\tilde{Q}\tilde{Q}^{*}$, the positive semidefinite Hermitian element of *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, which is the density matrix of the state the amplitude prepares.

The second, and the reason the instance is worth separating from the general theory, is that **the charge-conjugation twist is invisible on the internal rotations and detected by the global phase**. On the unitary slice $U(2)$ the four operators collapse in two steps: the untwisted pair becomes the inner conjugation $\mathrm{Ad}_{\tilde{Q}}$ on all of $U(2)$, and the charge-conjugation-twisted pair joins it exactly on the rotation group $SU(2)=U(2)\cap\mathbb{H}_{\mathbb{B}}$. The phase, which is the quotient $U(1)$, is exactly what the twist detects. This is the operator-level form of the statement that charge conjugation acts trivially on the rotation subgroup and flips the phase, and it sharpens the general collapse theorem of the mathematical source, which absorbs the twist into a sign.

## The Four Operators as Descriptions of One Action

**The inner conjugation** $\tilde{Q}\mapsto\tilde{Q}\tilde T\tilde{Q}^{-1}$ is the internal rotation of the observable. **The Hermitian sandwich** $\tilde{Q}\mapsto\tilde{Q}\tilde T\tilde{Q}^{*}$ is the same action written with the dagger, and it is the channel operator of *Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint*; it is the description in which an observable is transported by an amplitude rather than conjugated by a group element. **The signed inner conjugation** $\Phi^{\bar{\cdot},\mathrm{inv}}_{\tilde{Q}}(\tilde T)=\tilde{Q}^{*}\tilde T\tilde{Q}^{-1}$ is the rotation followed by the charge-conjugation twist on the left. **The signed Hermitian sandwich** $\Phi^{\bar{\cdot},{}^{*}}_{\tilde{Q}}(\tilde T)=\tilde{Q}^{*}\tilde T\tilde{Q}^{*}$ is the twisted channel.

**Proposition (the twist acts on the amplitude, not on the observable).** All four operators are $\mathbb{C}$-linear in the observable $\tilde T$; the twist conjugates the amplitude. In physical terms the twist is a property of the transformation, not of the quantity transformed.

*Proof.* The complex scalars are central and pass through both the conjugation and the product; the twist is $\mathbb{C}$-antilinear in the amplitude alone. Verified in the matrix model.

**Remark (the four coincide on the real quaternions).** For an amplitude in $\mathbb{H}_{\mathbb{B}}$ — a rotation — the twist is inert, $\bar{\cdot}(\tilde{Q})=\tilde{Q}$, and the signed members are the unsigned ones. The real-quaternion subspace is the natural home of the untwisted theory, and $SU(2)$ is its unitary part.

## The Two Defects

**Theorem (the horizontal defect).** For every $\theta$ and invertible $\tilde{Q}$, the dagger sandwich is the conjugation followed by the right multiplication by the prepared state,

$$
\Phi^{\theta,{}^{*}}_{\tilde{Q}}=R_{\tilde{Q}\tilde{Q}^{*}}\circ\Phi^{\theta,\mathrm{inv}}_{\tilde{Q}} .
$$

**Physical reading.** The element $\tilde{Q}\tilde{Q}^{*}$ is the prepared state; the identity says that the difference between the two right factors of the family is exactly that state, acting by multiplication on the right. On the slice $\tilde{Q}\tilde{Q}^{*}=e_0$ and the two descriptions coincide; off it, the offset is the density matrix of *The Bloch Ball as the Trace-One Slice of the Future Light Cone*. A boost, which lies outside the slice, is the case in which the offset is a genuine state and not the identity: this is the same amplification that appears in the covariance of the internal bilinears in *Bilinear Operators on the Biquaternion Algebra with Hermitian Adjoint*.

**Theorem (the vertical defect).** For every $\rho$ the twist is one left factor,

$$
\Phi^{\bar{\cdot},\rho}_{\tilde{Q}}=L_{\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}}\circ\Phi^{\mathrm{id},\rho}_{\tilde{Q}} .
$$

**Physical reading.** The **charge-conjugation defect** $\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}$ is the element that measures how strongly the amplitude is not its own charge conjugate. It is $e_0$ exactly on the real quaternions, so it vanishes on every internal rotation; it is the scalar $\pm e_0$ on the homogeneous elements, so on a bosonic amplitude it is a sign; and on a central unit it is the inverse-square phase, so the twist detects the global phase. Charge conjugation is thus invisible on the rotation group and visible exactly on the phase.

## The Collapse: The Rotations and the Phase

**Theorem (the collapse).** For $\tilde{Q}\in U(2)$ the four operators form two pairs, and each pair is a single operator:

$$
\Phi^{\mathrm{id},\mathrm{inv}}_{\tilde{Q}}=\Phi^{\mathrm{id},{}^{*}}_{\tilde{Q}}=\mathrm{Ad}_{\tilde{Q}},
\qquad
\Phi^{\bar{\cdot},\mathrm{inv}}_{\tilde{Q}}=\Phi^{\bar{\cdot},{}^{*}}_{\tilde{Q}}=L_{\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}}\circ\mathrm{Ad}_{\tilde{Q}} ,
$$

and the two pairs agree exactly on the rotation group,

$$
\Phi^{\bar{\cdot},\rho}_{\tilde{Q}}=\Phi^{\mathrm{id},\rho}_{\tilde{Q}} \iff \tilde{Q}\in U(2)\cap\mathbb{H}_{\mathbb{B}}=SU(2) .
$$

*Proof.* On the slice the dagger is the inverse, the horizontal defect trivialises and each pair collapses; the two pairs are separated by the charge-conjugation defect, which vanishes exactly on $\mathbb{H}_{\mathbb{B}}$. Verified over random slice elements and their phase-twisted products: the collapse held on $SU(2)$ and failed at the central phase $ie_0$, which is in $U(2)$ but not in $SU(2)$.

**Physical reading (the twist is blind to the rotation and sensitive to the phase).** The two collapse loci are the two subgroups the physics uses, and their quotient is the phase:

$$
U(2)/SU(2)\cong U(1),\qquad \text{the central phase} .
$$

So the charge-conjugation twist commutes with every internal rotation and is detected exactly by the global phase. The phase of an amplitude is invisible to the internal rotation and to the untwisted channel — the inner conjugation is blind to a central scalar — but it is precisely what the twist sees, since the defect of a central unit of phase $\omega$ is $\overline{\omega}^{2}e_0$. The same asymmetry is what makes $C$ a non-trivial real structure on the module while it acts trivially on the internal rotation group (*The Neutrino and Majorana Fermions in Biquaternionic Form*). The phase is thus the internal quantity conjugate to the charge conjugation, which is the operator statement behind the use of $\bar{\cdot}$ as the charge-conjugation real structure.

**Remark (the charge conjugate of an amplitude).** On the slice the charge conjugate of an amplitude differs from the amplitude by a unit scalar alone: writing $\tilde{Q}=\omega q$ with $q$ a rotation and $\lvert\omega\rvert=1$, one has $\tilde{Q}^{*}=\overline{\omega}^{2}\tilde{Q}$, and the charge-conjugation defect is the central unit $\overline{\omega}^{2}e_0$. So the charge conjugate of an amplitude induces the **same** inner conjugation and the **same** untwisted channel, because the inner conjugation is blind to the central phase, while the twisted members are the untwisted ones multiplied by $\overline{\omega}^{2}$. The pair identity $\Phi^{\bar{\cdot},\rho}_{\tilde{Q}}=\Phi^{\mathrm{id},\rho}_{\tilde{Q}}$ therefore holds exactly when $\overline{\omega}^{2}=1$, that is exactly when $\det\tilde{Q}=\omega^{2}=1$, which is the rotation group $SU(2)$: the same locus as in the collapse theorem, here read as the statement that the charge conjugate of an amplitude reproduces the amplitude itself only on the rotations.

## Worked Examples

**A central phase.** For $\tilde{Q}=\omega e_0$ with $\lvert\omega\rvert=1$ the inner conjugation is the identity and the signed family is the scalar $\overline{\omega}^{2}$:

$$
\Phi^{\mathrm{id},\rho}_{\omega e_0}=\mathrm{id},\qquad \Phi^{\bar{\cdot},\rho}_{\omega e_0}=\overline{\omega}^{2}\mathrm{id},\qquad \rho\in\{\mathrm{inv},{}^{*}\}.
$$

The whole of $U(1)=U(2)/SU(2)$ is of this form, so the example exhibits the failure of the collapse at the first non-trivial phase, and shows that the phase enters the twisted family as the unit $\overline{\omega}^{2}$.

**A rotation, and a rotation with a phase.** For $\tilde{Q}=e_1$ the twist is inert and the four operators are the rotation $\mathrm{Ad}_{e_1}$ through $\pi$ about the $e_1$ axis, the exact case of the collapse. For $\tilde{Q}=ie_1$ the twist element is $-e_0$ and every member of the signed pair is the negative of that rotation. The two amplitudes $e_1$ and $ie_1$ differ by the phase $i$, give the **same** inner conjugation — the rotation — and the **opposite** signed inner conjugation. The phase is exactly what separates them, and it is the phase that the rotation cannot see.

**A boost.** For a boost the amplitude lies outside $U(2)$, both defects are non-trivial, and no member of the family is an internal symmetry: the horizontal defect is the prepared state and the vertical defect is a genuine unit. This is the operator face of the fact that the Lorentz group does not act unitarily on the internal space, only its compact subgroup $SU(2)$ does.

## Honest Limits

Two limits must be stated, and they are the content of the article as much as the theorem is. First, **the twist of this article is not the parity twist of the framework**. Parity is the grading of the ambient $\mathrm{Cl}_{1,3}$, and its grade involution is the identity on the even part, which is $\mathbb{B}$ itself: on the algebra parity does nothing, and its carrier is the odd slot that a theory written only in $\mathbb{B}$ does not contain (*The Graded Algebra, Fermion Parity and the Two Sectors with Signed Inner Conjugation in Biquaternionic Form*). The twist $\bar{\cdot}$ used here is the grading of the other Clifford structure, $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, and it is nontrivial on $\mathbb{B}$. The two gradings of one algebra give the two different collapse theorems, and conflating them is the error the article is written to prevent. Second, the physical identification of $\bar{\cdot}$ with charge conjugation is the corpus's real-structure reading of *The Neutrino and Majorana Fermions in Biquaternionic Form*, not a derivation of a charge-conjugation symmetry of any particular dynamics; the article proves the operator identities and states the reading, and it does not claim that the internal theory contains a physical $C$ that is conserved.

## Summary

The internal amplitude acts on an observable by the mixed inner conjugation $\Phi^{\theta,\rho}_{\tilde{Q}}(\tilde T)=\theta(\tilde{Q})\tilde T\rho(\tilde{Q})$, with the twist $\theta$ equal to the identity or to the charge-conjugation real structure $\bar{\cdot}$; the four members are the inner conjugation (the rotation), the Hermitian sandwich (the channel), and the two charge-conjugation-twisted versions. The twist acts on the amplitude and not on the observable, and it is inert on the real quaternions, hence on every rotation. Two exact defects govern the family: the **horizontal** defect, which says that the Hermitian description differs from the conjugating one by the right multiplication by the prepared state $\tilde{Q}\tilde{Q}^{*}$, trivial exactly on the unitary slice; and the **vertical** defect $\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}$, the charge-conjugation defect, trivial exactly on the real quaternions and equal to the inverse-square phase on a central unit. On the slice $U(2)$ the family **collapses in two steps**: the untwisted pair is the inner conjugation $\mathrm{Ad}_{\tilde{Q}}$ on all of $U(2)$, and the twisted pair joins it exactly on the rotation group $SU(2)$, so the phase $U(2)/SU(2)=U(1)$ is exactly the quantity the charge conjugation detects. Charge conjugation is thus blind to the internal rotations and sensitive to the global phase, which is the operator statement of its role as the real structure that exchanges the defining module and its conjugate. The twist of this article must not be confused with the parity twist, which is trivial on the algebra and lives on the odd slot.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi^{\mathrm{id},\mathrm{inv}}_{\tilde{Q}}=\mathrm{Ad}_{\tilde{Q}}$ | Inner conjugation; the internal rotation |
| $\Phi^{\mathrm{id},{}^{*}}_{\tilde{Q}}$ | Hermitian sandwich; the internal channel |
| $\Phi^{\bar{\cdot},\mathrm{inv}}_{\tilde{Q}},\ \Phi^{\bar{\cdot},{}^{*}}_{\tilde{Q}}$ | The charge-conjugation-twisted rotation and channel |
| $\tilde{Q}\tilde{Q}^{*}$ | Horizontal defect; the prepared state, a cone element |
| $\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}$ | Vertical defect; the charge-conjugation defect |
| $U(2)/SU(2)\cong U(1)$ | The phase, exactly what the twist detects |

## Further Reading

- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 10th anniversary ed. 2010), for the phase as the ambiguity of a state and the Pauli transfer matrix of a channel.
- Claude Cohen-Tannoudji, Bernard Diu and Franck Laloë, *Quantum Mechanics*, Vol. 1 (Wiley, 1977), for the rotation group, its representation on observables and the inner automorphism.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for charge conjugation as a conjugate-linear real structure on the Dirac module and the exchange of the two chiralities.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the grading involution and the inner automorphism group of a Clifford algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the conjugation anti-involutions and their fixed subspaces.
