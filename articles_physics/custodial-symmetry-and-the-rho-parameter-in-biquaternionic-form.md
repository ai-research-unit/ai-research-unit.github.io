# __Custodial Symmetry and the Rho Parameter in Biquaternionic Form__

## Introduction

The **$\rho$ parameter** is the ratio of the charged to the neutral weak-boson masses divided by the cosine of the weak mixing angle,

$$
\rho = \frac{M_W^2}{M_Z^2\cos^2\theta_W} ,
$$

and its measured value is one to better than a part in a thousand. In the Standard Model this is not an accident of the numbers: it follows from a symmetry of the scalar sector called **custodial symmetry**, an approximate global $SU(2)$ that rotates the components of the scalar multiplet and is broken only by the weak hypercharge coupling and by the mass splittings within multiplets. The custodial symmetry is the diagonal of an $SU(2)_L\times SU(2)_R$ that acts on the scalar doublet, and the vacuum expectation value of that doublet is invariant under the diagonal, so the diagonal survives and ties the charged and neutral mass matrices together. The $\rho$ parameter is the precise measure of how well it survives.

This article asks what the biquaternion framework $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ contributes to custodial symmetry and to $\rho$. The algebra's multiplication carries exactly the structure that custodial symmetry uses: a scalar field valued in the real quaternions $\mathbb{H}_{\mathbb{B}}$ admits a **left and a right** action of $SU(2)$,

$$
\tilde H \;\longmapsto\; g_L\,\tilde H\,g_R^{-1},
\qquad g_{L,R}\in\mathbb{H}^1_{\mathbb{B}} ,
$$

and a central vacuum expectation value $\langle\tilde H\rangle = \frac{v}{\sqrt2}e_0$ is invariant under the diagonal $g_L = g_R$. That is the custodial mechanism in the framework's own multiplication. The framework's actual scalar, however, is the central field $\tilde\Phi = \varphi\,e_0$, which is a singlet of every non-abelian group and cannot be the doublet that the construction requires. The algebra therefore supplies the custodial action, and the framework's scalar sector does not supply the field on which it would act.

The findings are the following.

- **Established, and recomputed below.** The quaternion-valued scalar $\tilde H\in\mathbb{H}_{\mathbb{B}}$ carries the left–right action $\tilde H\mapsto g_L\tilde H g_R^{-1}$ of $SU(2)_L\times SU(2)_R$, and a central $\langle\tilde H\rangle = \frac{v}{\sqrt2}e_0$ is invariant under the diagonal $SU(2)_V = \{g_L = g_R\}$. With the hypercharge coupling set to zero the two gauge-boson mass matrices are proportional to the identity in the custodial basis, so $M_W = M_Z\cos\theta_W$ and $\rho = 1$ at tree level. The general multiplet formula
$$
\rho = \frac{\sum_i v_i^2\left[T_i(T_i+1)-T_{3i}^2\right]}{\sum_i 2v_i^2\,T_{3i}^2}
$$
gives $\rho = 1$ for the doublet, $\rho > 1$ for a $T = 1$, $T_3 = 0$ triplet admixture and $\rho = \tfrac12$ for a $T = 1$, $T_3 = 1$ one; all of these were recomputed.
- **Interpretation.** Identifying the custodial group with the diagonal of the framework's left–right multiplication, and the vacuum expectation value with a central element invariant under conjugation, is the interpretive link. The identification is exact at the level of the algebra and is labelled where the Standard Model's quantum numbers are involved.
- **Gap, left visible.** The framework's scalar is central and hence a singlet; it cannot transform in a doublet and cannot break $SU(2)_L$. Moreover the framework's non-abelian action on matter is left multiplication, which is vector-like, so its $\mathfrak{su}(2)$ is not the weak isospin. Custodial symmetry is therefore present in the framework as an algebraic action on the real-quaternion space and is absent as a property of the framework's scalar sector; the doublet, the hypercharge and the weak mixing angle are imports, as the companion agendas record.

- Companion article *The Higgs Mechanism in Biquaternionic Form*, for the symmetry-breaking potential and the vacuum expectation value.
- Companion article *Goldstone's Theorem in Biquaternionic Form*, for the Goldstone direction and the decay constant.
- Companion article *The Nonlinear Sigma Model in Biquaternionic Form*, for the left–right action, its invariant metric and its currents.
- Companion article *The Pion and the Chiral Lagrangian in Biquaternionic Form*, for the adjoint isospin action on a triplet and the relation of the custodial group to the chiral group.
- Companion article *The Gauge Principle in Biquaternionic Form*, for the non-abelian gauge construction and its left-multiplication action on matter.
- Companion article *Non-Abelian Gauge Fields in Biquaternionic Form*, for the field strength and the adjoint representation.
- Companion article *The Standard Model under the Biquaternion Framework — A Research Agenda*, for the boundary that this article states — no doublet, no hypercharge, no chiral $SU(2)_L$.
- Companion article *Electroweak Theory under the Biquaternion Framework — A Research Agenda*, for the vector-like obstruction and the electroweak quantum numbers.

**Conventions.** We use those of the companion articles throughout. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_ae_b = -\delta_{ab}e_0 + \varepsilon_{abc}e_c$, and $i$ is the central scalar imaginary. The sectors are $\mathbb{M}_-$ (anti-Hermitian, material) and $\mathbb{M}_+$ (Hermitian, informational); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}}$ its center. The compact group is the unit real quaternions $\mathbb{H}^1_{\mathbb{B}}\cong SU(2)$, with Lie algebra $\mathrm{span}_\mathbb{R}\{e_a\}\subset\mathbb{M}_-$; the standard Hermitian generators are $T_a = \tfrac{i}{2}e_a$, with $\mathrm{Tr}(T_aT_b) = \tfrac12\delta_{ab}$ and $[T_a,T_b] = i\varepsilon_{abc}T_c$. The trace is $\mathrm{Tr} = 2\,\mathrm{Sc}$ and the $ict$ metric is $\eta = \mathrm{diag}(-1,+1,+1,+1)$. The symbols $SU(2)_L$, $U(1)_Y$, $T$, $T_3$, $Y$, $\theta_W$, $W^\pm$, $Z$, $H$ and $v$ are **standard electroweak notation, not framework objects**; they are used where standard structures are quoted or named as missing, following the agenda articles. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value, and natural units $\hbar = c = 1$ are used in the mass formulas.

## The Custodial Symmetry of a Scalar Sector

The custodial symmetry is a property of the scalar sector of a spontaneously broken gauge theory, and it is worth stating in its standard form before it is read in the framework.

**The scalar multiplet as a matrix.** A complex $SU(2)_L$ doublet of hypercharge $Y = \tfrac12$ has four real components. They may be arranged in a $2\times2$ matrix

$$
H = \begin{pmatrix} \phi^{0*} & \phi^{+} \\ -\phi^{+*} & \phi^{0} \end{pmatrix},
$$

so that the electroweak group acts on the left and the hypercharge acts on the right,

$$
H \;\longmapsto\; e^{\,i\alpha^a T^a_L}\,H\,e^{\,i\beta T_3^{R}} ,
\qquad
T^a_L = \frac{\tau^a}{2},\quad T_3^R = \frac{\tau^3}{2} .
$$

The point of the arrangement is that the left action is the full $SU(2)_L$ and the right action is an $SU(2)_R$ whose $T_3^R$ is the hypercharge. With this normalisation the kinetic term is the framework's norm form of the derivative,

<!-- CONVENTION — norm-form kinetic term: the contraction $\mathrm{Tr}(\partial_\mu H^\dagger\partial_\mu H)$ is summed over the four coordinate derivatives with both indices down, and the overall minus sign is what makes the kinetic energy positive. Much of the standard literature writes the same term with a plus and a mostly-minus contraction. Do not "fix" the minus sign. -->

$$
-\,\frac12\,\mathrm{Tr}\!\left(\partial_\mu H^\dagger\,\partial_\mu H\right)
= -\,\partial_\mu\phi^{0*}\partial_\mu\phi^0 - \partial_\mu\phi^{+*}\partial_\mu\phi^{+} ,
$$

canonical for the two complex components, and if the hypercharge coupling is ignored it is invariant under the full $SU(2)_L\times SU(2)_R$, acting as $H\mapsto g_LHg_R^{-1}$. This is the **custodial group**. The hypercharge interaction gauges the $T_3^R$ direction and therefore breaks $SU(2)_R$ explicitly, but only as a subgroup: $U(1)_Y\subset SU(2)_R$, and the breaking is proportional to the hypercharge coupling $g'$.

**The vacuum and the unbroken diagonal.** The electroweak vacuum has $\langle\phi^+\rangle = 0$ and $\langle\phi^0\rangle = v/\sqrt2$, so the matrix expectation is proportional to the identity,

$$
\langle H\rangle = \frac{v}{\sqrt2}\,I_2 ,
\qquad
\frac12\,\mathrm{Tr}\!\left(\langle H\rangle^\dagger\langle H\rangle\right) = \frac{v^2}{2} .
$$

This is the crucial fact: a matrix proportional to the identity is invariant under the **diagonal** action $H\mapsto g\,H\,g^{-1}$ for every $g\in SU(2)$, so the diagonal subgroup

$$
SU(2)_V = \left\{\,g_L = g_R = g\,\right\}
$$

is unbroken, while the axial directions are broken and supply the three Goldstone bosons that become the longitudinal $W^\pm$ and $Z$. The unbroken $U(1)_{em}$ is the $T_3$ subgroup of the diagonal, and the diagonal's being unbroken is what makes the three would-be Goldstone directions transform as a triplet.

**The consequence for the masses.** The gauge-boson mass matrix is generated by the scalar kinetic term evaluated at the vacuum. Under the unbroken diagonal, the triplet of gauge fields $(W^1,W^2,W^3)$ transforms in the adjoint, and the hypercharge field $B$ is a singlet of $SU(2)_L$ but not of $SU(2)_R$; with $g' = 0$ the mass matrix is $SO(3)$-invariant, hence proportional to the identity, and

$$
M_W^2 = M_Z^2\cos^2\theta_W
\qquad\Longleftrightarrow\qquad
\rho = 1 .
$$

With $g'\neq0$ the equality is violated only through the mixing with the hypercharge field, which is a subgroup of the broken $SU(2)_R$, and the violation is a loop effect and a multiplet-splitting effect, not a tree-level one. This is the standard custodial mechanism (Weinberg 1976; Sikivie, Susskind, Voloshin, and Zakharov 1980), and it is imported.

## The Custodial Action in the Biquaternion Algebra

The structure above is a left and a right multiplication of a two-by-two matrix, and that is exactly what the biquaternion algebra's multiplication is. This section makes the identification precise.

**The scalar as a quaternion.** A complex doublet has four real components, and the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ has four real dimensions. The natural carrier is therefore the real quaternion

$$
\tilde H = h_0\,e_0 + h_1\,e_1 + h_2\,e_2 + h_3\,e_3 \in \mathbb{H}_{\mathbb{B}} ,
\qquad h_k\in\mathbb{R},
$$

on which the unit real quaternions act on the left and on the right,

$$
\tilde H \;\longmapsto\; g_L\,\tilde H\,g_R^{-1} ,
\qquad g_L, g_R\in\mathbb{H}^1_{\mathbb{B}} .
$$

This is an action of $SU(2)_L\times SU(2)_R$ on a real four-dimensional space — the vector representation, or the $(\tfrac12,\tfrac12)$ of the two factors — and it is the framework's own multiplication rather than an import. The invariant bilinear is the norm,

$$
\tilde H\bar{\tilde H} = \left(h_0^2+h_1^2+h_2^2+h_3^2\right)e_0 ,
$$

or equivalently $\mathrm{Sc}(\tilde H^\dagger\tilde H)$, which the two-sided action preserves because $\mathrm{Sc}(g_L\tilde H g_R^{-1}\overline{g_L\tilde H g_R^{-1}}) = \mathrm{Sc}(\tilde H\bar{\tilde H})$: the scalar part of a product is invariant under a similarity, and the two outer factors cancel.

**The left action and the sector structure.** The left multiplication by $g_L$ and the right multiplication by $g_R^{-1}$ act on the four components of $\tilde H$ as a pair of independent rotations. The left action is the framework's non-abelian gauge action of the companion articles, and the right action is the one that the framework's four-component objects have always carried: it is the same two-sided multiplication that the rotor conjugation of the Lorentz and gauge articles uses. The **diagonal** $g_L = g_R = g$ is the conjugation

$$
\tilde H \;\longmapsto\; g\,\tilde H\,g^{-1} ,
$$

which is the framework's similarity transformation, and it is the algebraic image of $SU(2)_V$.

**The central vacuum.** A vacuum expectation value that is central,

$$
\langle\tilde H\rangle = \frac{v}{\sqrt2}\,e_0 \in \mathbb{C}_{\mathbb{B}} ,
$$

is invariant under the diagonal because it commutes with every $g$, so

$$
g\,\frac{v}{\sqrt2}e_0\,g^{-1} = \frac{v}{\sqrt2}\,e_0 ,
$$

and the diagonal is unbroken. It is not invariant under a general left or right action, since $g_L\frac{v}{\sqrt2}e_0g_R^{-1} = \frac{v}{\sqrt2}g_Lg_R^{-1}$ equals the vacuum only when $g_L = g_R$; the axial directions are therefore broken, and their Goldstone bosons are the three would-be longitudinal gauge modes. The pivotal object is thus a central element, exactly as the Higgs mechanism's vacuum is central in the framework, and the difference is that the field carrying it is a general quaternion rather than a central scalar.

**Verification.** The invariance of the central vacuum under the diagonal was checked numerically for random unit quaternions $g$ generated from unnormalised four-vectors: the products $g\left(\frac{v}{\sqrt2}e_0\right)g^{-1}$ returned the original central element to better than $10^{-12}$. The invariance of the norm $\mathrm{Sc}(\tilde H^\dagger\tilde H)$ under $\tilde H\mapsto g_L\tilde H g_R^{-1}$ was checked in the same run for random unit $g_L, g_R$ and a random $\tilde H$, with the same accuracy. The computation used the real four-dimensional representation of $\mathbb{H}$.

## The Mass Matrices and the Value of $\rho$

The value of $\rho$ is read off the gauge-boson mass matrix, and the custodial invariance of that matrix is what makes it one.

**The mass matrix from the kinetic term.** The gauge fields of the two factors couple to the scalar through the covariant derivative, and at the vacuum the kinetic term produces the quadratic form

$$
\mathcal{L}_\text{mass} = \frac{v^2}{8}\left[g^2\left(W^1_\mu W^{1\mu} + W^2_\mu W^{2\mu}\right) + \left(gW^3_\mu - g'B_\mu\right)^2\right] + \cdots ,
$$

which is the standard result in the standard normalisation of the doublet. The charged combination $W^\pm = (W^1\mp iW^2)/\sqrt2$ obtains

$$
M_W^2 = \frac{g^2v^2}{4} ,
$$

and the neutral matrix in the $(W^3,B)$ basis is

$$
\mathcal{M}^2 = \frac{v^2}{4}
\begin{pmatrix} g^2 & -gg' \\ -gg' & g'^2 \end{pmatrix},
\qquad
\det\mathcal{M}^2 = 0,\qquad
\mathrm{tr}\,\mathcal{M}^2 = \frac{v^2}{4}\left(g^2+g'^2\right),
$$

whose nonzero eigenvalue is $M_Z^2 = \frac{v^2}{4}(g^2+g'^2)$. Hence

$$
\rho = \frac{M_W^2}{M_Z^2\cos^2\theta_W} = \frac{g^2v^2/4}{\frac{v^2}{4}(g^2+g'^2)\cdot\frac{g^2}{g^2+g'^2}} = 1 ,
$$

using $\cos^2\theta_W = g^2/(g^2+g'^2)$. The zero eigenvalue is the photon, and the equality of the two masses is the statement that the neutral and charged mass matrices have the same custodial structure. The framework's contribution to this computation is the identifying of the scalar's $SU(2)_L\times SU(2)_R$ action with the left–right multiplication of the algebra; the mass formulas themselves are standard.

**Departures from custodial symmetry.** The relation $\rho = 1$ holds when the scalar sector consists of any number of $SU(2)$ doublets with $Y = \pm\tfrac12$ and vanishing relative hypercharge, because each doublet contributes equally to the charged and neutral matrices in the custodial limit. It fails when the scalar sector contains a multiplet of higher isospin with nonvanishing vacuum expectation value, and the general formula is

$$
\rho = \frac{\sum_i v_i^2\left[T_i\left(T_i+1\right)-T_{3i}^2\right]}{\sum_i 2\,v_i^2\,T_{3i}^2},
$$

where the sum runs over the components that acquire vacuum expectation values, with isospin $T_i$ and third component $T_{3i}$. The electroweak $U(1)_Y$ breaks custodial symmetry explicitly, so the formula is exact only at tree level in the limit $g'\to0$; the hypercharge and the multiplet splittings generate corrections at higher order.

**Verification.** The formula was evaluated for the standard cases. A single doublet with $T = \tfrac12$, $T_3 = -\tfrac12$ and $v^2 = 1$ gives $\rho = 1$ exactly; a $T = 1$, $T_3 = 0$ triplet alone gives an infinite ratio (the neutral mass matrix receives no contribution from it while the charged matrix does), and a doublet plus a small triplet with $v_t^2 = 0.04\,v_d^2$ gives $\rho = 1.16 > 1$; a $T = 1$, $T_3 = 1$ multiplet alone gives $\rho = \tfrac12$; and two equal doublets again give $\rho = 1$. These are the standard expectations: doublets preserve $\rho = 1$, a $T_3 = 0$ triplet raises it, and a doubly-charged vacuum component lowers it.

**The relation to the pion's isospin.** The same $SU(2)$ that appears here is the framework's compact group, and the triplet $\tilde\pi$ of the companion pion article transforms in its adjoint. The custodial triplet of would-be Goldstone modes and the pion triplet are both adjoints of the framework's $SU(2)$; the difference is that the custodial triplet is eaten by the gauge bosons while the pion triplet is physical, which is a statement about the gauging and the explicit breaking and not about the algebra. The framework's algebra carries both triplets; it does not by itself decide which is which.

## Custodial Symmetry and the Chiral Lagrangian

The custodial group and the chiral group of the pion sector are the same group, and the reason is structural. Both are the diagonal of an $SU(2)_L\times SU(2)_R$: in the scalar sector the two factors act on the doublet as left and right multiplication, and in the fermion sector they act on the two chiralities of the quarks. When the quark condensate forms, the chiral group breaks to the diagonal, and the pions are the Goldstone bosons of the broken directions; when the scalar acquires its vacuum expectation value, the same diagonal survives and protects $\rho$. The two statements are the two faces of one breaking, and the biquaternion framework exhibits the coincidence cleanly: the left–right action $\tilde U\mapsto g_L\tilde U g_R^{-1}$ on a unit real quaternion is the chiral transformation of the pion field, and the left–right action $\tilde H\mapsto g_L\tilde H g_R^{-1}$ on a real quaternion is the custodial transformation of the scalar. Both are the algebra's multiplication, and the diagonal is the conjugation in both cases.

**What follows from the coincidence.** Because the unbroken diagonal is the isospin $SU(2)_V$ in both cases, the framework's statement about the pion triplet and its statement about the custodial triplet are statements about the same group and the same adjoint. The pion article's trace identity $\mathrm{Tr}(T_aT_b) = \tfrac12\delta_{ab}$ is the normalisation that both use; the custodial mass matrices and the pion kinetic term are both built from it. The framework therefore does not need a second group for custodial symmetry — it needs only the recognition that the chiral group it already hosts for the pions has the custodial diagonal. This is an economy of the algebra's group structure, and it is exact.

**The oblique parameters.** The custodial-violating corrections of the Standard Model are collected in the oblique parameters $S$, $T$ and $U$, of which $T$ is essentially the deviation of $\rho$ from one, $\rho-1\approx\alpha T$. These are standard electroweak observables (Peskin and Takeuchi 1990; Altarelli and Grunewald 2004) and are quoted, not derived here; they require the same multiplet content and hypercharge assignments that the framework does not supply, and their computation is therefore outside what the framework can currently address. What the framework supplies is the group-theoretic reason why $T$ is small at tree level: the diagonal of the chiral group is unbroken in both the scalar and the fermion sectors, and the breaking that produces the Goldstone bosons leaves it intact.

## What the Framework Supplies and What It Does Not

The construction above is the standard custodial mechanism written in the framework's multiplication. The framework's own scalar sector is smaller, and the difference should be stated without softening.

**The framework's scalar is central.** The scalar of *The Higgs Mechanism in Biquaternionic Form* is $\tilde\Phi = \varphi\,e_0\in\mathbb{C}_{\mathbb{B}}$, a central field carrying only the abelian central phase. It commutes with every element of $\mathbb{B}$ and is therefore a **singlet** of the compact $SU(2)\subset\mathbb{M}_-$: the left and right actions both act trivially on it, $g\,\tilde\Phi\,g^{-1} = \tilde\Phi$. A singlet cannot break a non-abelian symmetry, so the framework's scalar cannot be the doublet whose vacuum expectation value gives the $W$ and $Z$ their masses. The quaternion-valued field $\tilde H$ of the previous sections is a **different object** from the framework's scalar: it is the natural carrier of the custodial action, and it is not the field that the framework's scalar sector builds.

**The non-abelian action is vector-like.** Even granting a quaternion-valued scalar, the framework's non-abelian gauge action on matter is left multiplication, and on the framework's spinor module left multiplication acts on both chiral halves with the same representation. The companion agendas show that this action is vector-like and that the $SU(2)$ doublet is pseudoreal, so the framework's $\mathfrak{su}(2)$ is not the chiral $SU(2)_L$: it cannot give the left-handed and right-handed fermions inequivalent representations. The custodial symmetry of the electroweak sector is a symmetry of a chiral gauge theory, and the framework's non-abelian structure does not reach the chiral gauge theory in the first place.

**Hypercharge is not supplied.** The custodial group's right factor is broken to its $T_3^R$ subgroup by the hypercharge interaction, and the framework derives no hypercharge, no assignment of it, and no mixing angle. The $\rho$ parameter's custodial protection is a statement about the relative size of the charged and neutral mass matrices, and it presupposes an abelian factor whose charge assignment is fixed; the framework supplies the central abelian factor but not the assignment that makes it hypercharge.

**What is genuinely the framework's.** Two things are. First, the custodial action is the algebra's left–right multiplication, so the framework supplies the **action** on the real-quaternion space rather than borrowing it: given a quaternion-valued scalar, the custodial $SU(2)_L\times SU(2)_R$, its diagonal, and its central-invariant vacuum are all there. Second, the relation between the custodial triplet and the pion triplet is a statement about adjoints of the framework's compact group, and the framework supplies both. The gap is the field content, not the group theory, and it is the same gap that the Higgs-mechanism and agenda articles leave open.

## Empirical Status

The $\rho$ parameter is measured to be one within about a part in a thousand by the electroweak precision observables, and the small deviation is accounted for by the hypercharge and multiplet-splitting corrections of the Standard Model; the value is a standard literature result and is quoted, not derived here. In the framework the situation is the one the previous section describes: $\rho = 1$ would follow from a quaternion-valued scalar with a central vacuum, which the framework does not build, and its corrections would require the hypercharge and the multiplet content, which the framework does not derive. The framework therefore makes no prediction for $\rho$ that can be compared with the measurement, and the agreement of the measured value with one is, in the framework's terms, an imported success of the Standard Model's scalar sector.

## Open Questions

1. **Can a quaternion-valued scalar be built in the framework?** The carrier of the custodial action is $\mathbb{H}_{\mathbb{B}}$, and a scalar potential on it that is invariant under $SU(2)_L\times SU(2)_R$ and has a central minimum is not constructed. Whether such a potential exists and whether its scalar is the framework's natural doublet is open.

2. **Does the framework's scalar sector admit a doublet at all?** The central scalar is a singlet; a doublet would have to be a different field. The agenda's classification is "known route, blocked" and the block is the chiral action and the hypercharge, not the algebra.

3. **The mixing angle.** The value $\rho = 1$ is independent of $\theta_W$, but the comparison with data needs $\theta_W$, which the framework does not derive. Whether the framework's two couplings (the central $q$ and the non-abelian $\kappa$) fix a mixing angle once an embedding is declared is open.

4. **Loop corrections to $\rho$.** The custodial-violating corrections are finite and calculable once the multiplet content is specified; whether the framework's trace structure reproduces the standard correction is a finite check that has not been performed.

5. **The pion–custodial relation.** The custodial triplet and the pion triplet are both adjoints of the framework's $SU(2)$; whether the framework's gauging distinguishes them, or whether the distinction is entirely a matter of the hypercharge embedding, is not settled.

6. **Empirical contact.** The framework predicts no value for $\rho$; whether any framework-specific deviation survives once the Standard Model content is supplied is the recurring open question.

## Summary

The $\rho$ parameter is the measure of custodial symmetry, the approximate global $SU(2)_V$ that survives the breaking of $SU(2)_L\times U(1)_Y$ when the scalar vacuum is a custodial singlet. In the Standard Model the vacuum is $\langle H\rangle = \frac{v}{\sqrt2}I_2$, a matrix proportional to the identity, which is invariant under the diagonal of the $SU(2)_L\times SU(2)_R$ acting on the scalar, and the gauge-boson mass matrices in the custodial limit are proportional to the identity, giving $M_W = M_Z\cos\theta_W$ and $\rho = 1$. The general multiplet formula is

$$
\rho = \frac{\sum_i v_i^2\left[T_i(T_i+1)-T_{3i}^2\right]}{\sum_i 2\,v_i^2\,T_{3i}^2},
$$

which was recomputed: it gives $\rho = 1$ for one or several doublets, $\rho > 1$ (here $1.16$) for a doublet with a $T = 1$, $T_3 = 0$ triplet admixture, and $\rho = \tfrac12$ for a $T = 1$, $T_3 = 1$ multiplet.

In the biquaternion framework the custodial action is the algebra's own left–right multiplication on the real-quaternion space,

$$
\tilde H \;\longmapsto\; g_L\,\tilde H\,g_R^{-1} ,
\qquad g_{L,R}\in\mathbb{H}^1_{\mathbb{B}} ,
$$

with the diagonal $g_L = g_R$ the unbroken $SU(2)_V$ and the central vacuum $\langle\tilde H\rangle = \frac{v}{\sqrt2}e_0$ invariant under it; both invariances were verified numerically to better than $10^{-12}$. The framework therefore supplies the **action** and its invariant vacuum. It does not supply the **field**: its scalar is the central $\tilde\Phi = \varphi\,e_0$, a singlet of the compact $SU(2)$ that cannot break a non-abelian symmetry; its non-abelian gauge action on matter is vector-like and is not the chiral $SU(2)_L$; and it derives no hypercharge and no mixing angle. The custodial symmetry is thus present in the algebra and absent from the framework's scalar sector, and the framework makes no prediction for $\rho$ to compare with the measured value of one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_ae_b = -\delta_{ab}e_0+\varepsilon_{abc}e_c$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{H}^1_{\mathbb{B}}$ | Real quaternions; unit real quaternions $\cong SU(2)$ |
| $\mathbb{C}_{\mathbb{B}}$ | Center; home of the central vacuum |
| $T_a = \tfrac{i}{2}e_a$, $\mathrm{Tr}(T_aT_b) = \tfrac12\delta_{ab}$ | Standard Hermitian generators of the compact group |
| $\tilde H = h_0e_0 + h_ke_k\in\mathbb{H}_{\mathbb{B}}$ | Quaternion-valued scalar (carrier of the custodial action) |
| $\tilde H\mapsto g_L\tilde H g_R^{-1}$ | Left–right $SU(2)_L\times SU(2)_R$ action |
| $SU(2)_V = \{g_L = g_R\}$ | Custodial (diagonal) subgroup |
| $\langle\tilde H\rangle = \frac{v}{\sqrt2}e_0$ | Central vacuum; custodial invariant |
| $\tilde\Phi = \varphi\,e_0\in\mathbb{C}_{\mathbb{B}}$ | Framework's actual scalar; a singlet |
| $-\frac12\mathrm{Tr}(\partial_\mu H^\dagger\partial_\mu H)$ | Custodial-invariant kinetic term of the doublet matrix $H$ (norm form of the derivative) |
| $M_W^2 = g^2v^2/4$ | Charged weak-boson mass (standard) |
| $M_Z^2 = (g^2+g'^2)v^2/4$ | Neutral weak-boson mass (standard) |
| $\cos^2\theta_W = g^2/(g^2+g'^2)$ | Weak mixing angle (standard) |
| $\rho = M_W^2/(M_Z^2\cos^2\theta_W)$ | $\rho$ parameter |
| $\rho = \frac{\sum_i v_i^2[T_i(T_i+1)-T_{3i}^2]}{\sum_i 2v_i^2T_{3i}^2}$ | General multiplet formula |
| $g, g'$ | Weak and hypercharge couplings (standard notation; framework couplings are $\kappa$ and $q$) |
| $T, T_3, Y$ | Isospin, third component, hypercharge (standard; not framework objects) |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | $ict$ metric for index contractions |
| $\mathrm{Tr} = 2\,\mathrm{Sc}$ | Trace convention |

## Further Reading

- S. Weinberg, "Implications of dynamical symmetry breaking: an addendum," *Physical Review D* **19** (1979) 1277–1280, for the custodial symmetry and its consequences for the $\rho$ parameter.
- P. Sikivie, L. Susskind, M. B. Voloshin, and V. Zakharov, "Isospin breaking in technicolor models," *Nuclear Physics B* **173** (1980) 189–207, for the custodial $SU(2)$ of the scalar sector and the multiplet formula for $\rho$.
- M. Veltman, "Limit on mass differences in the Weinberg model," *Nuclear Physics B* **123** (1977) 89–99, for the $\rho$ parameter and the radiative corrections that test it.
- M. E. Peskin and T. Takeuchi, "Estimation of oblique electroweak corrections," *Physical Review D* **46** (1992) 381–409, for the $S$, $T$ and $U$ parameters and the relation of $T$ to $\rho$.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the electroweak mass matrices, the mixing angle, and the tree-level relation $\rho = 1$.
- C. Quigg, *Gauge Theories of the Strong, Weak, and Electromagnetic Interactions* (Benjamin/Cummings, 1983), for the custodial symmetry and the general multiplet analysis.
- J. F. Donoghue, E. Golowich, and B. R. Holstein, *Dynamics of the Standard Model* (Cambridge, 1992), for the scalar sector, the $\rho$ parameter, and the electroweak precision observables.
- G. Altarelli and M. W. Grunewald, "Precision electroweak tests of the Standard Model," *Physics Reports* **403–404** (2004) 189–201, for the measured $\rho$ parameter and the electroweak fit.
- Particle Data Group (R. L. Workman et al.), "Review of Particle Physics," *Progress of Theoretical and Experimental Physics* **2022** (2022) 083C01, for the measured values of $M_W$, $M_Z$, $\theta_W$ and $\rho$.
- H. Georgi, *Weak Interactions and Modern Particle Theory* (Benjamin/Cummings, 1984), for the chiral gauge theory and the scalar sector's electroweak quantum numbers.
- P. Langacker, *The Standard Model and Beyond* (CRC Press, 2010), for the electroweak symmetry breaking, the custodial symmetry, and the oblique corrections.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 2: *Modern Applications* (Cambridge, 1996), for the spontaneous breaking of gauge symmetries and the vector-boson masses.
