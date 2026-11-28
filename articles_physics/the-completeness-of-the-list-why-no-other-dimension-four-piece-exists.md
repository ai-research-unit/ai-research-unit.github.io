# __The Completeness of the List: Why No Other Dimension-Four Piece Exists__

## Introduction

**The claim.** The forty-seven pieces of [The Census Rule](the-census-rule-dimension-four-residual-invariance-and-one-canonical-term-per-field.html) are all of them. This article proves it by a method that cannot miss a term: it sorts every candidate by how many fermions it carries and how many derivatives, lists the members of each class by mass dimension, and then answers for each one whether it is in the list, forbidden, a total derivative, or removable.

**The answer.**

$$
\boxed{\;\text{admissible}=\{\text{in the list}\}\cup\{\text{total derivatives}\}\cup\{\text{removable by a field redefinition}\}\;}
$$

**Why the two conditions, not one.** The four conditions of the census rule — Lorentz scalar, residual invariance, dimension at most four, built from the mass eigenstates — admit candidates that are not in the Standard Model. Two are $hF_{\mu\nu}F^{\mu\nu}$ and $hF_{\mu\nu}\tilde F^{\mu\nu}$: both are residual invariants of dimension five, so dimension already excludes them, but $hF\tilde F$ would be admitted at dimension three if the photon had a mass, and the point stands. The condition that removes this whole family is descent: every piece must be the image of a dimension-four invariant of the *unbroken* group. Residual invariance plus descent is the criterion; either alone is too weak.

**What the article is not.** It is not a proof from first principles of the Standard Model's content. The content is an input, fixed elsewhere. What is proved is that, given the content, the list is exhausted.

## The Method

**Two quantum numbers and one dimension.** Every candidate is classified by the number of fermion fields $n_F\in\{0,2,4\}$, by the number of derivatives $n_D\in\{0,1,2\}$, and by its mass dimension. With $[V_\mu]=1$, $[h]=1$, $[\psi]=\tfrac32$ and $[\partial]=1$, the dimension is

$$
[\mathcal{O}]=n_V+n_h+\tfrac32n_F+n_D ,
$$

and the condition is $[\mathcal{O}]\le4$. Lorentz invariance forces $n_F$ even and fixes how the spinor indices are contracted; gauge invariance fixes how the internal indices are contracted. What remains is the arithmetic of the table.

**Why the classification cannot miss a term.** A monomial is determined by its field content and its derivative count. The table lists every field content with $n_F$ even and dimension at most four, so every monomial appears exactly once.

## The Bosonic Classes Without Derivatives

**$n_F=0$, $n_D=0$.** The candidates, by field content.

| Fields | Dimension | In the list? | Reason |
|---|---|---|---|
| none | $0$ | no | vacuum energy; not a particle term, and fixed by renormalisation |
| $V_\mu V^\mu$ | $2$ | $W$, $Z$ only | forbidden for $\gamma$ and $G^a$ by residual invariance |
| $h^2$ | $2$ | yes | the Higgs mass piece |
| $h^3$ | $3$ | yes | the cubic self-coupling |
| $h\,V_\mu V^\mu$ | $3$ | $W$, $Z$ only | the two $hVV$ pieces; $M_\gamma=M_g=0$ |
| $h^4$ | $4$ | yes | the quartic self-coupling |
| $h^2V_\mu V^\mu$ | $4$ | $W$, $Z$ only | the two $hhVV$ pieces |
| $V_\mu V^\mu V_\nu V^\nu$ | $4$ | $W$ only | four charged vectors; two of the four quartic structures |

**The vector mass row is the one that needs care.** $A_\mu A^\mu$ is forbidden because $A_\mu$ is a connection of the unbroken $U(1)_{\mathrm{em}}$, and a mass term for a connection is not invariant — the argument is one argument with four instantiations, stated in [One Obstruction, Four Groups](one-obstruction-four-groups-the-gauge-mass-that-is-never-admitted.html). $Z_\mu Z^\mu$ and $W^+_\mu W^{-\mu}$ are in the list only as the unitary-gauge image of the scalar kinetic term, which is the subject of [The Two Vector Masses](the-two-vector-masses-proca-as-the-representative-of-the-condensate.html). At the level of the unbroken group those two rows have no ancestor that is not the scalar kinetic term, and that is exactly what descent says.

**The $V^4$ row and the counting convention.** With self-interactions folded into the curvatures, the four-vector structures are not separate rows; they are vertices. The row is listed here because the completeness question is asked of monomials, and the four monomials exist. [The Gauge Self-Interactions](the-gauge-self-interactions-two-triple-vertices-and-four-quartic-vertices.html) writes them.

## The Bosonic Classes With Two Derivatives

**$n_F=0$, $n_D=2$.**

| Fields | Dimension | In the list? | Reason |
|---|---|---|---|
| $V_\mu V_\nu$ | $4$ | yes, four | the four field-strength pieces |
| $V_\mu V_\nu$ mixed, $Z_{\mu\nu}F^{\mu\nu}$ | $4$ | no | removable by the rotation to mass eigenstates |
| $h\,h$ | $4$ | yes | the Higgs kinetic piece |
| $h\,V_\mu$ | $3$ | no | total derivative, or removable by a shift of $V$ |
| $h\,h\,V_\mu$ | $4$ | no | total derivative |
| $h\,V_\mu V_\nu$ | $5$ | no | dimension; this is the loop-induced family of The Loop-Induced Pieces |

**The mixed curvature row is a redundancy and not an absence.** Before the rotation, the neutral kinetic terms are $-\tfrac14W_{3,\mu\nu}W_3^{\mu\nu}-\tfrac14B_{\mu\nu}B^{\mu\nu}$, and a term $W_{3,\mu\nu}B^{\mu\nu}$ is forbidden by the product structure of the two factors. After the rotation to $A$ and $Z$ the same two pieces are diagonal, and a mixed term $Z_{\mu\nu}F^{\mu\nu}$ would be a third. Its absence is the statement that the rotation was performed, not that a term was forbidden.

**The $h\partial h V$ row is the sharpest redundancy.** A term $\partial_\mu h\,Z^\mu$ has dimension three and is a residual invariant, so the four conditions admit it. It is absent in unitary gauge because the Goldstone field it would mix with has been set to zero, and in a general gauge it is removed by the shift $Z_\mu\mapsto Z_\mu+\partial_\mu h$ at the cost of a shift in the $Z$ mass term. It is a redundancy, and the corpus's gauge-fixing article states where it goes.

## The Fermionic Classes

**$n_F=2$.**

| Fields | $n_D$ | Dimension | In the list? | Reason |
|---|---|---|---|---|
| $\bar\psi\psi$ | $0$ | $3$ | nine of twelve | a mass; no ancestor for the neutrino |
| $\bar\psi\psi h$ | $0$ | $4$ | nine | the Higgs–fermion pieces |
| $\bar\psi\psi h$, pseudoscalar | $0$ | $4$ | no | removable by a chiral rotation |
| $\bar\psi\gamma_\mu\psi\,V^\mu$ | $0$ | $4$ | yes, five | QCD, QED, the two charged currents, the neutral current |
| $\bar\psi\gamma_\mu\psi\,\partial^\mu$ | $1$ | $4$ | yes, twelve | the kinetic pieces |
| $\bar\psi\sigma_{\mu\nu}\psi\,V^{\mu\nu}$ | $0$ | $5$ | no | dimension; the dipole family |
| $\bar\psi\psi\,h^2$ | $0$ | $5$ | no | dimension |

**$n_F=4$.** Every four-fermion monomial has dimension six and is excluded by dimension alone. This is the class the effective field theory adds, and [What the List Omits](what-the-list-omits-ghosts-the-theta-term-neutrino-mass-and-gravity.html) records it.

**$n_F$ odd.** Excluded by Lorentz invariance: a Lorentz scalar needs an even number of spinors, and a single spinor has no scalar contraction. The one exception in principle is a spin-$\tfrac32$ field, which the content does not carry.

## The Exclusions, One at a Time

**Five candidates that a reader will look for, and the answer for each.**

| Candidate | Dimension | Why it is not in the list |
|---|---|---|
| $m_\gamma^2A_\mu A^\mu$ | $2$ | forbidden: a mass for an unbroken connection |
| $m_g^2G^a_\mu G^{a\mu}$ | $2$ | forbidden, the same argument, colour adjoint |
| $\tfrac12m_\nu\bar\nu^c_L\nu_L$ | $3$ | no dimension-four ancestor: the operator is dimension five before breaking |
| $hF_{\mu\nu}F^{\mu\nu}$ | $5$ | dimension, and no ancestor; generated at one loop |
| $\bar\psi\sigma_{\mu\nu}\psi F^{\mu\nu}$ | $5$ | dimension; the anomalous moment is a loop effect |

**The neutrino mass deserves its own paragraph, because the residual criterion admits it.** $\tfrac12m_\nu\bar\nu^c_L\nu_L$ carries no colour, no charge and dimension three. It is a perfectly good invariant of $SU(3)_c\times U(1)_{\mathrm{em}}$, and a list built on residual invariance alone would contain it. It is excluded because the broken-phase term has to come from somewhere: its only ancestor is the Weinberg operator $\frac{c_{ab}}{\Lambda}(L^T i\tau_2H)(L^T i\tau_2H)$, of dimension five, which is not in the symmetric-phase list either. The absence is therefore a statement about the unbroken theory. It is not a statement that neutrinos are massless in nature, and [The Nine Dirac Masses](the-nine-dirac-masses-and-the-tenth-the-minimal-model-omits.html) says so.

**$hF\tilde F$ is the exclusion that tests descent.** It is dimension three if written with a massless photon and a single $h$, it is CP-odd, and it is invariant under colour and electromagnetism. Nothing in the residual criterion removes it. What removes it is descent: the CP-odd dimension-four objects of the unbroken group are $G\tilde G$, $W\tilde W$ and $B\tilde B$, and all three are total derivatives. There is no CP-odd dimension-four operator with an $h$ in it, so there is none below. The same argument covers $hZ\tilde F$ and $hZ\tilde Z$.

## Three Ways a Term Leaves the List Without Being Forbidden

**A candidate can be admissible and still not be a piece.** Three mechanisms do this, and keeping them apart from the exclusions is what makes the theorem precise.

| Mechanism | What it does | Example |
|---|---|---|
| total derivative | changes no equation of motion and no vertex | $F_{\mu\nu}\tilde F^{\mu\nu}$, $G\tilde G$, $\partial_\mu(h\partial^\mu h)$ |
| field redefinition | moves the term into others without changing any observable | $Z_{\mu\nu}F^{\mu\nu}$ removed by the $\gamma$–$Z$ rotation |
| equation of motion | vanishes on the free equations, so it can be removed order by order | $h\,\partial_\mu Z^\mu$ after the shift of $Z$ |

**The total derivative class is where $\theta_{\mathrm{QCD}}$ lives.** $G^a_{\mu\nu}\tilde G^{a\mu\nu}$ is a total derivative and contributes no vertex at any order in the tree expansion; its effect is entirely quantum and is the subject of [The Theta Parameter and Strong CP](the-theta-parameter-and-strong-cp-in-biquaternionic-form.html). It is a parameter of the theory and not a piece of the list, which is why the count of parameters is nineteen and the count of pieces is forty-seven.

**The distinction has a measurable consequence.** A forbidden term is absent at every order. A redundant term is present in intermediate steps and cancels in the answer. A total derivative is present in the Lagrangian and absent from every amplitude. Three different statements, and a reader who runs them together will think the $\theta$ term is forbidden, which it is not.

## Checks

1. The dimension formula. Recomputed on each row: $[V_\mu V^\mu]=2$, $[h^3]=3$, $[h^2V^2]=4$, $[\bar\psi\psi]=3$, $[\bar\psi\sigma\psi V]=5$, $[\bar\psi\psi h]=4$.
2. The class count. Five bosonic classes without derivatives, three with two derivatives, four two-fermion classes with an admitted member, and two excluded fermionic classes: nine rows carry a member of the list.
3. The arithmetic of the list. The admitted rows of the tables give $2+1+1+2+2+4+4+1+1$ bosonic and $9+9+5+12$ fermionic pieces, which regroup into the ten groups of the summation.
4. The vector-mass row against the obstruction. $A_\mu A^\mu$ and $G^a_\mu G^{a\mu}$ fail the invariance argument of [One Obstruction, Four Groups](one-obstruction-four-groups-the-gauge-mass-that-is-never-admitted.html); $W$ and $Z$ do not, because their mass arrives through the scalar kinetic term.
5. The neutrino row against the Weinberg operator. The dimension-five operator is the only ancestor, and it requires a right-handed neutrino or an inverse scale; either way it is absent from a renormalisable symmetric phase.
6. The $hF\tilde F$ row against the CP-odd inventory. The three CP-odd dimension-four objects of the unbroken group are all total derivatives, so the family has no ancestor.
7. The four-fermion row. Every monomial has dimension six, since $4\times\tfrac32=6$.
8. Consistency with the assembly. The six ancestors of [The Standard Model and the Lagrangian](the-standard-model-and-the-lagrangian-four-sectors-in-one-expression.html) are all dimension four, and every admitted row of this article's tables is an image of one of them.

## Summary

The list is complete, and the proof is an enumeration. Every candidate is sorted by the number of fermions, the number of derivatives and the mass dimension; the bosonic classes without derivatives give the scalar potential, the vector masses and the four-vector structures; the bosonic classes with two derivatives give the four field strengths, the scalar kinetic piece and two redundancies; the two-fermion classes give the kinetic, mass, Yukawa and current pieces; the four-fermion class and the dipole family are excluded by dimension; odd fermion numbers are excluded by Lorentz invariance.

Two conditions are needed and neither suffices alone. Residual invariance admits the Majorana neutrino mass and $hF\tilde F$; descent excludes both, because neither has a dimension-four ancestor in the unbroken theory. Descent alone would not fix the count, because residual invariance is what decides that the photon and the gluon take no mass and no $hVV$ piece.

Three mechanisms remove admissible candidates without forbidding them: a total derivative changes no amplitude, a field redefinition moves a term into others, and a term proportional to a free equation of motion can be removed order by order. The $\theta$ term is in the first class, the $\gamma$–$Z$ mixing in the second, and the $h\partial Z$ mixing in the third.

Five candidates a reader looks for are absent for five different reasons: the photon and gluon masses are forbidden, the neutrino mass and the dipole moments have no dimension-four ancestor, and $h\gamma\gamma$ is dimension five and generated only at one loop.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $n_F$, $n_D$ | Number of fermion fields and of derivatives in a candidate |
| $[V_\mu]=1$, $[h]=1$, $[\psi]=\tfrac32$, $[\partial]=1$ | Mass dimensions |
| $[\mathcal{O}]=n_V+n_h+\tfrac32n_F+n_D$ | The dimension formula |
| $F_{\mu\nu}\tilde F^{\mu\nu}$ | The dual contraction, a total derivative |
| $hF\tilde F$ | The CP-odd scalar–photon operator, excluded by descent |
| $\bar\nu^c_L\nu_L$ | The Majorana mass, admitted by residual invariance alone |

## Further Reading

- [The Census Rule](the-census-rule-dimension-four-residual-invariance-and-one-canonical-term-per-field.html). The criterion and the four counting conventions this article proves sufficient.
- [One Obstruction, Four Groups: The Gauge Mass That Is Never Admitted](one-obstruction-four-groups-the-gauge-mass-that-is-never-admitted.html). The argument that removes $A_\mu A^\mu$ and $G^a_\mu G^{a\mu}$.
- [The Standard Model and the Lagrangian: Four Sectors in One Expression](the-standard-model-and-the-lagrangian-four-sectors-in-one-expression.html). The six ancestors, and the audit that the sum is invariant.
- [The Theta Parameter and Strong CP in Biquaternionic Form](the-theta-parameter-and-strong-cp-in-biquaternionic-form.html). The total-derivative class, and why its parameter is counted apart.
- [The Nine Dirac Masses and the Tenth the Minimal Model Omits](the-nine-dirac-masses-and-the-tenth-the-minimal-model-omits.html). The neutrino exclusion, in full.
- The Loop-Induced Pieces the Tree-Level Census Omits. The $hVV$ family that descent removes and loops restore.
