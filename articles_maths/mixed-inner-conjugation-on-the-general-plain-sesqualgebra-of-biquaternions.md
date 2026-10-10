# __Mixed Inner Conjugation on the General Plain Sesqualgebra of Biquaternions__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra with its Hermitian conjugation ${}^{*}$ and with complex conjugation $\bar{\cdot}$. The two are the $\mathbb{C}$-independent order-two conjugations of the algebra: $\bar{\cdot}$ is the $\mathbb{C}$-antilinear automorphism $i\mapsto-i$, $e_k\mapsto e_k$ which is the **grade involution** of the Clifford structure $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ is the $\mathbb{C}$-antilinear anti-automorphism negating both signs, the map whose fixed space is the Hermitian subspace $\mathbb{M}_+$ and whose form is the positive definite one of the theory (*The Clifford Algebra Representation*, *Introduction to the Remarkable Subspaces*).

An element $\tilde{Q}$ of the algebra acts on the algebra in four ways, according to whether the **left** factor is twisted by $\bar{\cdot}$ and whether the **right** factor is inverted or dagged:

$$
\Phi^{\theta,\rho}_{\tilde{Q}}(\tilde T)=\theta(\tilde{Q})\,\tilde T\,\rho(\tilde{Q}),\qquad \theta\in\{\mathrm{id},\bar{\cdot}\},\quad \rho\in\{\mathrm{inv},{}^{*}\},
$$

namely the **inner conjugation** $\Phi^{\mathrm{id},\mathrm{inv}}_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{-1}$, the **signed inner conjugation** $\Phi^{\bar{\cdot},\mathrm{inv}}_{\tilde{Q}}(\tilde T)=\bar{\tilde{Q}}\tilde T\tilde{Q}^{-1}$, the **Hermitian sandwich** $\Phi^{\mathrm{id},{}^{*}}_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{*}$, and the **signed Hermitian sandwich** $\Phi^{\bar{\cdot},{}^{*}}_{\tilde{Q}}(\tilde T)=\bar{\tilde{Q}}\tilde T\tilde{Q}^{*}$. This article is the biquaternion instance of the general theory of these four operators, *Mixed Inner Conjugation and Hermitian Adjoint*.

The unsigned members are owned elsewhere and are cited only. The inner conjugation $\tilde{Q}\tilde T\tilde{Q}^{-1}$ is the algebra form of the orthogonal action of *Biquaternion Versors and the Orthogonal Group*; the Hermitian sandwich is the operator $\Theta_{\tilde{Q}}$ of *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, whose composition law, adjoint, kernel, image and cone are recorded there and are not repeated here.

The instance is not a restatement of the general case, and the reason is a **fork in the twist**. The general theory's twist $\alpha$ is the grading involution of the Clifford algebra, and it acts as the scalar $\pm1$ on the homogeneous elements; that is why its collapse theorem can absorb the twist into a sign. In the biquaternion algebra the twist $\theta=\bar{\cdot}$ is nontrivial for a reason that has no counterpart in the general statement: the basis elements $e_0,e_1,e_2,e_3$ have the $\mathrm{Cl}_{3,0}$-degrees $0,2,2,2$, so $\bar{\cdot}$ fixes $e_0$ and each $e_k$ and negates the generators $ie_k$ and the volume element $i$. The two readings of the algebra then give two different collapse theorems. In the reading $\mathbb{B}=\mathrm{Cl}^{+}_{1,3}$ the grading is the identity on the even part — reversion and Clifford conjugation coincide there for exactly this reason (*The Clifford Algebra Representation*) — the signed members coincide with the unsigned ones, and everything collapses on the slice $U(2)$; the twist then lives on the odd slot that the algebra does not contain, and the signed theory of *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation* and *Two-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint* degenerates to the unsigned one on $\mathbb{B}$. In the reading $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ the twist is $\bar{\cdot}$ and the collapse splits: **on the unitary slice the family collapses in two steps, the unsigned pair on $U(2)$ and the signed pair one step lower, on the rotation group $SU(2)=U(2)\cap\mathbb{H}_{\mathbb{B}}$.** The quotient $U(2)/SU(2)=U(1)$ — the central phase — is thereby identified as exactly the quantity that the twist detects, and that is the sharpening this article records.

## The Four Operators

**Definition.** For $\tilde{Q}\in\mathbb{B}^{\times}$ the **mixed family** of $\tilde{Q}$ is the set $\{\Phi^{\theta,\rho}_{\tilde{Q}}\}$ of the four operators above, from $\mathbb{B}$ to $\mathbb{B}$. The word *mixed* records that the left and the right factors are conjugated independently, whereas the two-sided operator of the companion article conjugates both by the same anti-involution.

**Proposition (linearity in the argument).** Each $\Phi^{\theta,\rho}_{\tilde{Q}}$ is $\mathbb{C}$-linear in its argument; the twist $\theta$ acts on the parameter and not on the argument, because $\theta(\tilde{Q})$ is an element and the complex scalars are central.

*Proof.* $\Phi^{\theta,\rho}_{\tilde{Q}}(\lambda \tilde T)=\theta(\tilde{Q})(\lambda \tilde T)\rho(\tilde{Q})=\lambda\,\theta(\tilde{Q})\tilde T\rho(\tilde{Q})=\lambda\,\Phi^{\theta,\rho}_{\tilde{Q}}(\tilde T)$, the scalar passing through by centrality. Note that the same computation run on the parameter would fail: $\tilde{Q}\mapsto\Phi^{\theta,\rho}_{\tilde{Q}}$ is not $\mathbb{C}$-linear for $\theta=\bar{\cdot}$, since $\bar{\cdot}$ is antilinear.

**Remark (the four are distinct).** For a generic $\tilde{Q}$ the four operators are four different operators, and no two of them agree; the identifications occur only on the loci computed below. For $\tilde{Q}\in\mathbb{H}_{\mathbb{B}}$ the twist is inert, $\bar{\cdot}(\tilde{Q})=\tilde{Q}$, so $\Phi^{\bar{\cdot},\rho}_{\tilde{Q}}=\Phi^{\mathrm{id},\rho}_{\tilde{Q}}$ on that subspace, which is the reason the real-quaternion subspace is the natural domain of the unsigned theory.

## Multiplicativity in the Parameter

**Theorem (the family is multiplicative).** For each pair $(\theta,\rho)$ and all invertible $\tilde{Q},\tilde{R}$,

$$
\Phi^{\theta,\rho}_{\tilde{Q}\tilde{R}}=\Phi^{\theta,\rho}_{\tilde{Q}}\circ\Phi^{\theta,\rho}_{\tilde{R}} .
$$

*Proof.* $\bar{\cdot}(\tilde{Q}\tilde{R})=\bar{\cdot}(\tilde{Q})\bar{\cdot}(\tilde{R})$ because the coefficient conjugation is an automorphism, and $(\tilde{Q}\tilde{R})^{\dagger}=\tilde{R}^{*}\tilde{Q}^{*}$ because the dagger is an anti-automorphism. Then $\Phi^{\theta,\rho}_{\tilde{Q}}(\Phi^{\theta,\rho}_{\tilde{R}}(\tilde T))=\theta(\tilde{Q})\theta(\tilde{R})\,\tilde T\,\rho(\tilde{R})\rho(\tilde{Q})$, and the two middle factors combine into $\theta(\tilde{Q}\tilde{R})$ and $\rho(\tilde{Q}\tilde{R})$ respectively. Verified in the matrix model for all four pairs over random invertible parameters.

**Corollary (the parameter rule).** For a central scalar $A$ and an invertible $\tilde{Q}$,

$$
\Phi^{\mathrm{id},\mathrm{inv}}_{A\tilde{Q}}=\Phi^{\mathrm{id},\mathrm{inv}}_{\tilde{Q}},\qquad
\Phi^{\bar{\cdot},\mathrm{inv}}_{A\tilde{Q}}=\frac{\overline{A}}{A}\,\Phi^{\bar{\cdot},\mathrm{inv}}_{\tilde{Q}},\qquad
\Phi^{\mathrm{id},{}^{*}}_{A\tilde{Q}}=\lvert A\rvert^{2}\Phi^{\mathrm{id},{}^{*}}_{\tilde{Q}},\qquad
\Phi^{\bar{\cdot},{}^{*}}_{A\tilde{Q}}=\overline{A}^{2}\,\Phi^{\bar{\cdot},{}^{*}}_{\tilde{Q}} .
$$

So the inner conjugation is **blind to the central phase**, and the twist is not: for $\lvert A\rvert=1$ the inner conjugation and the unsigned sandwich are unchanged, while the signed members are multiplied by the units $\overline{A}/A$ and $\overline{A}^{2}$, which are $1$ only at $A=\pm1$. For $A=i$ this is the statement that the inner conjugation satisfies $\Phi^{\mathrm{id},\mathrm{inv}}_{i\tilde{Q}}=\Phi^{\mathrm{id},\mathrm{inv}}_{\tilde{Q}}$ while the signed inner conjugation is negated, $\Phi^{\bar{\cdot},\mathrm{inv}}_{i\tilde{Q}}=-\Phi^{\bar{\cdot},\mathrm{inv}}_{\tilde{Q}}$.

*Proof.* $A$ is central. For $\rho=\mathrm{inv}$ use $(A\tilde{Q})^{-1}=A^{-1}\tilde{Q}^{-1}$: the computation gives $\theta(A)A^{-1}\Phi^{\theta,\mathrm{inv}}_{\tilde{Q}}$, which is $1$ for $\theta=\mathrm{id}$ and $\overline{A}/A$ for $\theta=\bar{\cdot}$. For $\rho={}^{*}$ use $(A\tilde{Q})^{\dagger}=\overline{A}\tilde{Q}^{*}$: the computation gives $\theta(A)\overline{A}\,\Phi^{\theta,{}^{*}}_{\tilde{Q}}$, which is $A\overline{A}=\lvert A\rvert^{2}$ for $\theta=\mathrm{id}$ and $\overline{A}^{2}$ for $\theta=\bar{\cdot}$. Verified numerically on random parameters and central phases.

## The Two Defects

**Theorem (the horizontal defect).** For every $\theta$ and every invertible $\tilde{Q}$,

$$
\Phi^{\theta,{}^{*}}_{\tilde{Q}}\circ\bigl(\Phi^{\theta,\mathrm{inv}}_{\tilde{Q}}\bigr)^{-1}=R_{\tilde{Q}\tilde{Q}^{*}},
$$

the right multiplication by $\tilde{Q}\tilde{Q}^{*}$. The two right factors of the family differ by the right multiplication by the Hermitian element $\tilde{Q}\tilde{Q}^{*}$, and that element is the image of the identity under the sandwich, $\Theta_{\tilde{Q}}(e_0)$.

*Proof.* Let $\tilde A=\Phi^{\theta,\mathrm{inv}}_{\tilde{Q}}(\tilde T)=\theta(\tilde{Q})\tilde T\tilde{Q}^{-1}$, so that $\tilde T$ is recovered by acting with the inverse. Then $\Phi^{\theta,{}^{*}}_{\tilde{Q}}(\tilde T)=\theta(\tilde{Q})\tilde T\tilde{Q}^{*}=\tilde A\,\tilde{Q}\tilde{Q}^{*}=R_{\tilde{Q}\tilde{Q}^{*}}(\tilde A)$, using $\tilde{Q}^{-1}\tilde{Q}=e_0$. On the slice the defect is trivial because $\tilde{Q}\tilde{Q}^{*}=e_0$; off it, it is the positive semidefinite element of the cone of *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*. Verified for both $\theta$ over random parameters.

**Theorem (the vertical defect).** For every $\rho$ and every invertible $\tilde{Q}$,

$$
\Phi^{\bar{\cdot},\rho}_{\tilde{Q}}=L_{\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}}\circ\Phi^{\mathrm{id},\rho}_{\tilde{Q}},
$$

the left multiplication by the **twist element** $\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}$.

*Proof.* $\bar{\cdot}(\tilde{Q})\tilde T\rho(\tilde{Q})=(\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1})\,\tilde{Q}\tilde T\rho(\tilde{Q})$. Verified for both $\rho$ over random parameters.

**Corollary (homogeneous elements and the sign of the twist).** Let $\tilde{Q}$ have the $\mathrm{Cl}_{3,0}$-degree $g\in\{0,1,2,3\}$, so that $\bar{\cdot}(\tilde{Q})=(-1)^{g}\tilde{Q}$. Then $\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}=(-1)^{g}e_0$ is central, and

$$
\Phi^{\bar{\cdot},\rho}_{\tilde{Q}}=(-1)^{g}\,\Phi^{\mathrm{id},\rho}_{\tilde{Q}} .
$$

In particular the signed inner conjugation is the ordinary one for even $\tilde{Q}$ and its negative for odd $\tilde{Q}$, and $\Phi^{\bar{\cdot},\mathrm{inv}}_{\tilde{Q}}$ is an algebra automorphism of $\mathbb{B}$ (multiplicative in its argument) exactly for even $\tilde{Q}$. This is the graded multiplicativity that the name *signed* records, and it is the sense in which the general theory's twist is absorbed into a sign: on the homogeneous elements the defect is a scalar. Explicitly the twist element $\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}$ is $+e_0$ on the grade $0$ element $e_0$ and on the grade $2$ elements $e_1,e_2,e_3$, and $-e_0$ on the grade $1$ elements $ie_1,ie_2,ie_3$ and on the grade $3$ element $i$, in agreement with the sign table of *The Clifford Algebra Representation*.

**Remark (the defect is not central in general).** For a non-homogeneous unit $\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}$ is a genuine unit and the signed family is not proportional to the unsigned one. The twist element is $e_0$ exactly on the real-quaternion subspace,

$$
\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}=e_0 \iff \bar{\cdot}(\tilde{Q})=\tilde{Q} \iff \tilde{Q}\in\mathbb{H}_{\mathbb{B}},
$$

and it detects the central phase: it is the inverse-square phase for a central unit, $\bar{\cdot}(A e_0)(Ae_0)^{-1}=(\overline{A}/A)e_0$, so that the twist vanishes on the central phase only at $A=\pm1$.

## The Adjoint and the Types

**Theorem (the adjoint of a dagger sandwich).** With the scalar form $(\tilde T,\tilde S)=\mathrm{Sc}(\tilde{T}^{*}\tilde S)$ of the algebra, the adjoint of a dagger sandwich is the sandwich of the dagged parameter,

$$
\bigl(\Phi^{\theta,{}^{*}}_{\tilde{Q}}\bigr)^{*}=\Phi^{\theta,{}^{*}}_{\tilde{Q}^{*}} .
$$

*Proof.* The scalar form satisfies $\mathrm{Sc}(\tilde T\tilde S)=\mathrm{Sc}(\tilde S\tilde T)$. For the left-hand side, $\bigl(\Phi^{\theta,{}^{*}}_{\tilde{Q}}(\tilde T)\bigr)^{\dagger}=\bigl(\theta(\tilde{Q})\tilde T\tilde{Q}^{*}\bigr)^{\dagger}=\tilde{Q}\,\tilde{T}^{*}\,\theta(\tilde{Q})^{\dagger}$, so $(\Phi^{\theta,{}^{*}}_{\tilde{Q}}(\tilde T),\tilde S)=\mathrm{Sc}\bigl(\tilde{Q} \tilde{T}^{*}\theta(\tilde{Q})^{\dagger}\tilde S\bigr)=\mathrm{Sc}\bigl(\tilde{T}^{*}\theta(\tilde{Q})^{\dagger}\tilde S\tilde{Q}\bigr)$ by the cyclic invariance. The right-hand side is $(\tilde T,\Phi^{\theta,{}^{*}}_{\tilde{Q}^{*}}(\tilde S))=\mathrm{Sc}\bigl(\tilde{T}^{*}\theta(\tilde{Q}^{*})\tilde S\tilde{Q}\bigr)$ because $(\tilde{Q}^{*})^{\dagger}=\tilde{Q}$. The two agree for all $\tilde T,\tilde S$ exactly when $\theta(\tilde{Q})^{\dagger}=\theta(\tilde{Q}^{*})$, which holds for both values of the twist: for $\theta=\mathrm{id}$ it is the tautology $\tilde{Q}^{*}=\tilde{Q}^{*}$, and for $\theta=\bar{\cdot}$ both sides equal the quaternion conjugation $\tilde{Q}^{\natural}$ of $\tilde{Q}$, since $\bar{\cdot}$ and ${}^{*}$ commute. Verified for both $\theta$ over random parameters and arguments.

**Corollary (the unitary slice).** Both dagger sandwiches are automorphisms of the scalar form on the slice $U=\{\tilde{Q}:\tilde{Q}^{*}\tilde{Q}=e_0\}$, and on the slice the two members of each pair coincide; the unsigned sandwich is there the inner automorphism $\mathrm{Ad}_{\tilde{Q}}$, and the signed one is its left translate by the twist element. Off the slice the unsigned sandwich is neither a form-preserving map nor a homomorphism. The slice is the unitary group $U(2)$ in the matrix model, of real dimension four, whose determinant-one part is $SU(2)$ (*The Unitary Slice and the Compact Real Form with Hermitian Adjoint*, *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*).

*Proof.* On the slice $\tilde{Q}^{*}=\tilde{Q}^{-1}$, so $\Phi^{\mathrm{id},{}^{*}}_{\tilde{Q}}=\Phi^{\mathrm{id},\mathrm{inv}}_{\tilde{Q}}=\mathrm{Ad}_{\tilde{Q}}$ is an inner automorphism and a form-preserving map, and $\Phi^{\bar{\cdot},{}^{*}}_{\tilde{Q}}=\Phi^{\bar{\cdot},\mathrm{inv}}_{\tilde{Q}}$ is its translate by the vertical defect. Failure of multiplicativity and of automorphism off the slice is the criterion for the unsigned sandwich recorded in *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*; both dagger sandwiches were checked to preserve the form on the slice over random unitary parameters.

## The Collapse and Its Two Loci

**Theorem (the collapse).** Let $\tilde{Q}\in U(2)$. Then the four operators fall into two pairs,

$$
\Phi^{\mathrm{id},\mathrm{inv}}_{\tilde{Q}}=\Phi^{\mathrm{id},{}^{*}}_{\tilde{Q}}=\mathrm{Ad}_{\tilde{Q}},
\qquad
\Phi^{\bar{\cdot},\mathrm{inv}}_{\tilde{Q}}=\Phi^{\bar{\cdot},{}^{*}}_{\tilde{Q}}=L_{\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}}\circ\mathrm{Ad}_{\tilde{Q}},
$$

and the two pairs agree exactly on the rotation group,

$$
\Phi^{\bar{\cdot},\rho}_{\tilde{Q}}=\Phi^{\mathrm{id},\rho}_{\tilde{Q}} \iff \bar{\cdot}(\tilde{Q})=\tilde{Q} \iff \tilde{Q}\in U(2)\cap\mathbb{H}_{\mathbb{B}}=SU(2) .
$$

*Proof.* On the slice $\tilde{Q}^{*}=\tilde{Q}^{-1}$, so the horizontal defect trivialises and the two members of each pair coincide. The vertical defect then separates the pairs by the left multiplication by $\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}$, which is $e_0$ exactly on $\mathbb{H}_{\mathbb{B}}$. The intersection $U(2)\cap\mathbb{H}_{\mathbb{B}}$ is the group of unit real quaternions, $\mathrm{Sp}(1)\cong SU(2)$. Verified over random slice elements and their phase-twisted products: the collapse held on $SU(2)$ and failed at the element $ie_0$, which lies in $U(2)$ but not in $SU(2)$.

**Corollary (the phase is what the twist detects).** The two collapse loci are the two distinguished subgroups of the theory, the unitary slice $U(2)$ and the rotation group $SU(2)$, and their quotient is the central circle,

$$
U(2)/\bigl(U(2)\cap\mathbb{H}_{\mathbb{B}}\bigr)=U(2)/SU(2)\cong U(1),
$$

the group of central phases. The family therefore collapses in two steps: the untwisted pair on the whole slice, and the twisted pair only on the subgroup on which the phase has been divided out. Equivalently, **the twist is invisible on the rotations and visible on the phase**, and the phase is precisely the ambiguity that the inner conjugation cannot see.

**Remark (the fork and the general theorem).** The general source states that all four operators collapse on the unitary slice for homogeneous parameters. Read on $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ with the twist $\bar{\cdot}$, that statement is exact on the even degrees and must be corrected by the sign $(-1)^{g}$ on the odd ones: the signed pair is then $(-1)^{g}\mathrm{Ad}_{\tilde{Q}}$, and for a non-homogeneous parameter of the slice the twist element is a genuine unit and the signed pair is not proportional to the unsigned one at all — unless the parameter is a real quaternion, where the collapse is exact. Read on $\mathbb{B}=\mathrm{Cl}^{+}_{1,3}$, where the grading is the identity, the twist element is always $e_0$ and the general theorem is exact but vacuous: the signed members are the unsigned ones. The two readings are the two sides of the fork, and they agree exactly where the theory is stated on the even slot.

## Worked Examples

**A central phase.** For $\tilde{Q}=\omega e_0$ with $\lvert\omega\rvert=1$, the inner conjugation is the identity and the signed inner conjugation is the scalar $\overline{\omega}/\omega=\overline{\omega}^{2}$:

$$
\Phi^{\mathrm{id},\rho}_{\omega e_0}=\mathrm{id},\qquad \Phi^{\bar{\cdot},\rho}_{\omega e_0}=\overline{\omega}^{2}\,\mathrm{id},\qquad \rho\in\{\mathrm{inv},{}^{*}\}.
$$

The whole of $U(2)$ modulo $SU(2)$ is of this form, and the example shows the collapse failing at the first non-trivial phase: the two families differ by the unit scalar $\overline{\omega}^{2}$, which is $1$ only at $\pm e_0$.

**An even element.** For $\tilde{Q}=e_1$, of $\mathrm{Cl}_{3,0}$-degree two, the twist is inert, $\bar{\cdot}(e_1)=e_1$, and the four operators coincide:

$$
\Phi^{\theta,\rho}_{e_1}(\tilde T)=e_1\,\tilde T\,e_1^{-1}=-e_1\tilde Te_1=\mathrm{Ad}_{e_1}(\tilde T),
$$

the rotation through $\pi$ about the $e_1$ axis of *Biquaternion Versors and the Orthogonal Group*; the horizontal defect also trivialises because $e_1\in U(2)$. This is the exact case of the collapse.

**An odd element.** For $\tilde{Q}=ie_1$, of degree one, $\bar{\cdot}(ie_1)=-ie_1$, and the twist element is $-e_0$. The four operators are two pairs, and each pair is minus the value of the even example:

$$
\Phi^{\theta,\rho}_{ie_1}(\tilde T)=(-1)^{1}\,\mathrm{Ad}_{e_1}(\tilde T)=-\mathrm{Ad}_{e_1}(\tilde T).
$$

Now $e_1$ and $ie_1$ give the **same** inner conjugation, because the inner conjugation cannot see the central phase, and the **opposite** signed inner conjugation. This is the mechanism of the collapse corollary in one line: the twist distinguishes what the inner conjugation identifies.

**A non-homogeneous slice element.** For a random $\tilde{Q}\in U(2)$ the twist element $\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}$ is a genuine unitary element of $\mathbb{B}$ and the signed pair is its left translate of the unsigned pair; it is $e_0$ exactly for the real-quaternion parameters, which are the rotations. The horizontal defect is trivial throughout, so the two elements of each pair always agree; it is the vertical defect alone that separates the pairs.

## Honest Limits

Two limits are worth stating plainly. First, the collapse theorem is a statement about the four **operators on the algebra**, not about the module; the passage to the spinor module is the article *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, where the sign of the twist is the statement that the left multiplication is an antirepresentation on the odd slot, and no collapse of that kind is available there. Second, the twist $\bar{\cdot}$ of this article is not the parity twist of the physics corpus. Parity is the grading of $\mathrm{Cl}_{1,3}$, trivial on its even part $\mathbb{B}$, and its carrier is the odd slot that $\mathbb{B}$ does not contain; the twist $\bar{\cdot}$ is the grading of $\mathrm{Cl}_{3,0}$ and is nontrivial on $\mathbb{B}$ itself. The two gradings of one algebra give the two collapse theorems, and conflating them is the single error this article is written to prevent. Where the physics corpus says that the twist is invisible on the algebra, it means the parity grading; where this article says that the twist is visible on the algebra, it means the coefficient conjugation.

## Summary

The biquaternion algebra carries four mixed operators $\Phi^{\theta,\rho}_{\tilde{Q}}(\tilde T)=\theta(\tilde{Q})\tilde T\rho(\tilde{Q})$, with the twist $\theta$ equal to the identity or to the complex conjugation $\bar{\cdot}$, which is the grade involution of the structure $\mathbb{B}\cong\mathrm{Cl}_{3,0}$; $\rho$ equal to the inverse or to the dagger gives the two-family split inside each twist. The assignment is multiplicative in the parameter for each of the four pairs, and $\mathbb{C}$-linear in the argument with the twist acting on the parameter. The family is governed by **two exact defects**: the horizontal defect $\Phi^{\theta,{}^{*}}_{\tilde{Q}}=R_{\tilde{Q}\tilde{Q}^{*}}\circ\Phi^{\theta,\mathrm{inv}}_{\tilde{Q}}$, the right multiplication by the cone element $\tilde{Q}\tilde{Q}^{*}$, trivial exactly on the slice; and the vertical defect $\Phi^{\bar{\cdot},\rho}_{\tilde{Q}}=L_{\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}}\circ\Phi^{\mathrm{id},\rho}_{\tilde{Q}}$, the left multiplication by the twist element, which is the scalar $(-1)^{g}$ on a homogeneous parameter and $e_0$ exactly on the real-quaternion subspace. The dagger sandwiches have adjoint $({\Phi^{\theta,{}^{*}}_{\tilde{Q}}})^{*}=\Phi^{\theta,{}^{*}}_{\tilde{Q}^{*}}$ and preserve the form and are automorphisms on the slice. On the slice the family **collapses in two steps**: the untwisted pair becomes the inner conjugation $\mathrm{Ad}_{\tilde{Q}}$ on the whole of $U(2)$, and the twisted pair joins it exactly on $SU(2)=U(2)\cap\mathbb{H}_{\mathbb{B}}$, so that the two collapse loci are the two distinguished subgroups of the theory and their quotient $U(1)$ is the central phase that the twist detects. This is the sharpening of the general case: in the reading $\mathbb{B}=\mathrm{Cl}^{+}_{1,3}$ the grading is trivial and the general collapse theorem holds vacuously, while in the reading $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ the general theorem splits into the two-locus statement above, and the fork is exactly where the two gradings of the algebra differ.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi^{\theta,\rho}_{\tilde{Q}}(\tilde T)=\theta(\tilde{Q})\tilde T\rho(\tilde{Q})$ | The mixed family; $\theta\in\{\mathrm{id},\bar{\cdot}\}$, $\rho\in\{\mathrm{inv},{}^{*}\}$ |
| $\Phi^{\mathrm{id},\mathrm{inv}}_{\tilde{Q}}=\mathrm{Ad}_{\tilde{Q}}$ | Inner conjugation; the orthogonal action |
| $\Phi^{\mathrm{id},{}^{*}}_{\tilde{Q}}=\Theta_{\tilde{Q}}$ | Hermitian sandwich; the operator of the combined article |
| $\Phi^{\bar{\cdot},\mathrm{inv}}_{\tilde{Q}},\ \Phi^{\bar{\cdot},{}^{*}}_{\tilde{Q}}$ | Signed inner conjugation and signed Hermitian sandwich |
| $R_{\tilde{Q}\tilde{Q}^{*}}$ | Horizontal defect; the right multiplication by the cone element |
| $\bar{\cdot}(\tilde{Q})\tilde{Q}^{-1}$ | Vertical defect, or twist element; $e_0$ exactly on $\mathbb{H}_{\mathbb{B}}$ |
| $({-1})^{g}$ | The twist element on a parameter of $\mathrm{Cl}_{3,0}$-degree $g$ |
| $U(2)$, $SU(2)=\mathrm{Sp}(1)$ | The two collapse loci; $U(2)/SU(2)\cong U(1)$ |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the graded structure of a Clifford algebra, the standard involutions and the inner automorphism group.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the conjugation anti-involutions and their fixed spaces.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270 (Springer, 1985), for the unitary group of a general plain sesquilinear form and its determinant-one part.
- Emil Artin, *Geometric Algebra* (Interscience, 1957; reprint Wiley, 1988), for the orthogonal group as an inner automorphism group and the role of the spinor norm.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 10th anniversary ed. 2010), for the unitary group, its centre and the phase as the ambiguity of a state.
