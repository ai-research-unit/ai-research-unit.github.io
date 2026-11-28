# __The Content Above $M_C$: Fifteen Connections, Sixteen Weyl Fields and One Hermitian Scalar__

## Introduction

**The question.** [The census](the-census-above-m-c-nineteen-structures-eighteen-admissible-eleven-written.html) counts structures. **Before it can, there must be fields to build them from.** This article states the content, counts its degrees of freedom, and says which masses the content permits.

**The answer.**

$$
\boxed{\;\underbrace{15}_{\text{connections}}+\underbrace{16}_{\text{Weyl fields}}+\underbrace{16}_{4\times4\text{ Hermitian}}=78\ \text{real degrees of freedom}.\;}
$$

**Three fields and no fourth.** One connection in the adjoint of $\mathrm{SU}(4)$, sixteen Weyl fields in two copies of $\mathbf4\oplus\bar{\mathbf4}$, and one Hermitian $4\times4$ matrix. **There is no second scalar, no second connection and no family index**, and each absence is a declaration the census inherits.

## The Connection

**Fifteen real vector fields, all massless, all in one multiplet.**

$$
A_{\imath}=A_{a,\imath}t_{a},\qquad a=1,\dots,15,\qquad [t_{a},t_{b}]=if_{abc}t_{c}.
$$

**Fifteen and not sixteen**: the adjoint of $\mathrm{SU}(4)$ is $\mathbf{15}$, because the group has rank three and $4^{2}-1=15$. **The generators are Hermitian and traceless**, and their normalisation is $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$, which is the convention every trace in this category uses.

**The connection is one field and not fifteen forces.** A local symmetry has one coupling per simple factor; $\mathrm{SU}(4)$ has one factor, so **one $g_{4}$ multiplies all fifteen.** The fifteen directions differ by what they act on and not by what they cost.

**Masslessness is forced here, unlike the fermions.** The term $m^{2}\operatorname{tr}A_{\imath}A^{\imath}$ is a Lorentz scalar of dimension two, **and it is not invariant under the local transformation**: with $A_{\imath}\to UA_{\imath}U^{\dagger}+(i/g_{4})U\partial_{\imath}U^{\dagger}$ the shift contributes a piece linear in $A$ that no quadratic term can cancel. **So the vector mass is forbidden by local invariance and not declined by the author**, and [the force content](the-force-content-of-the-su4-model-one-connection-a-nine-dimensional-kernel-and-rank-five.html) draws the consequence: the fifteen stay massless until a condensate supplies a direction and the gauge is fixed.

**Two degrees of freedom each.** A massless vector in four dimensions carries two polarisations, so the connection contributes $15\times2=30$.

## The Sixteen Weyl Fields

**Two copies of the quartet and its conjugate.**

| representation | Weyl fields | states |
|---|---|---|
| $\mathbf4$ | $2$ per copy value | $8$ |
| $\bar{\mathbf4}$ | $2$ per copy value | $8$ |
| **total** | $\mathbf{16}$ | $\mathbf{32}$ |

**The "two per copy value" is the whole subtlety.** The copy index $\alpha=1,2$ is a two-valued degeneracy and not a family label; **it is the index the Yukawa matrix lives on**, and [the copy index's article](the-scalars-two-indices-and-the-count-sixteen.html) shows it to be a commutant of the gauge action. **No generator sees it.**

**Sixteen Weyl fields carry thirty-two states.** Each Weyl field has two helicities, and **the pair $\mathbf4\oplus\bar{\mathbf4}$ is what makes a Dirac mass possible at all**: a mass needs a left-handed and a right-handed field of the same charge, and the content supplies them. **So the absent fermion mass is a choice and not a prohibition**, which is the one place this phase differs in kind from the Standard Model's.

**The currents are vector currents and their ordinary divergence does not vanish.**

$$
j^{\xi}_{a,\imath}=\sum_{f=1}^{16}\bar\xi_{f}\gamma_{\imath}t_{a}\xi_{f},
\qquad
\partial^{\imath}j^{\xi}_{a,\imath}\neq0,\qquad
D^{\imath}j^{\xi}_{a,\imath}=0 .
$$

**No conserved charge exists in this phase**, and the corpus's conserved charges are properties of the residual group below $M_C$.

## The Scalar

**One Hermitian $4\times4$ matrix, sixteen real components.**

$$
\Xi=\Xi^{\dagger},\qquad \Xi=\Xi_{0}+\tfrac14\bigl(\operatorname{tr}\Xi\bigr)\mathbb 1,\qquad \operatorname{tr}\Xi_{0}=0 .
$$

**Sixteen and not fifteen or twenty-five.** A Hermitian $4\times4$ has $4^{2}=16$ real entries by the diagonal-real, off-diagonal-complex count; **the group acts as $\Xi\to U\Xi U^{\dagger}$**, which is the $\mathbf{15}\oplus\mathbf1$ of $\mathrm{SU}(4)$.

**The split into traceless and trace is the article's working tool.** Fifteen components ride in the traceless part and one in the trace; **[the canonical basis](the-canonical-basis-above-m-c-one-rescaling-three-costs-and-the-numbers-that-are-not-invariants.html) shows the trace mode to be the one that rescales under a field redefinition**, and every basis statement in the category is a statement about it.

**The scalar is not a doublet and the difference is a factor of eight.** A doublet has four real components and two invariants at degree two; **this matrix has sixteen and needs a partition count to enumerate its potential** — $1,2,3,5$ monomials at degrees one to four, eleven in all. **That eleven is the reason this phase's census is not shorter than the broken phase's.**

**Sixteen degrees of freedom and no eaten ones.** Above $M_C$ there is no condensate, so **no Goldstone is absorbed and no scalar is subtracted**; the sixteen are all physical, and the count $30+32+16=78$ is the count of propagating modes.

## What the Content Forbids, Declines and Permits

**Three verdicts, and they are not the same verdict.**

| structure | verdict | reason |
|---|---|---|
| vector mass | **forbidden** | no invariant of dimension two in the adjoint |
| fermion mass | **declined** | allowed by the group, omitted by the ledger |
| scalar mass | **permitted**, two of them | $\operatorname{tr}\Xi^{2}$ and $(\operatorname{tr}\Xi)^{2}$ |
| gravity | **absent** | no slot in the connection |

**The vector mass's prohibition is a theorem and the fermion mass's absence is a choice.** A reader who treats them alike will think the model forbids $\bar\xi\xi$; **it does not, and [the Yukawa sector](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html) says what that costs.** The corpus omits the bare mass because the ledger carries one source of fermion mass and not two.

**The scalar's two masses are the only dimensionful constants in the phase.** Combined with $g_{4}$ they give one scale and one ratio, and **no vacuum expectation value appears** — $v$ is what the restructuring creates, and above $M_C$ the potential's minimum is the symmetric point $\Xi=0$.

## The Ledger

**Every number in the category is downstream of this table.**

| item | count | where it enters |
|---|---|---|
| connections | $15$ | the $AAA$ and $AAAA$ vertices; the $80$ brackets |
| Weyl fields | $16$ | the $\bar\xi A\xi$ block; the Yukawa matrix |
| scalar components | $16$ | the eleven potential monomials; the $\mathbf{15}\oplus\mathbf1$ |
| degrees of freedom | $78$ | the loop count and the thermal count |
| couplings | $1$ | $g_{4}$, in rows $1$, $2$, $3$ |
| dimensionful constants | $2$ | $\mu_{\Phi}^{2}$, $\mu_{2}^{2}$ |

**The content is small and the census is not.** Three fields, one coupling, two masses — **and nineteen structures, because a $4\times4$ matrix admits eleven monomials where a doublet admits two.** The content's size and the census's size are different questions.

## Checks

1. The adjoint. $4^{2}-1=15$.
2. The fermions. $2$ copies $\times\,2$ representations $\times\,2$ chiralities $\times\,4=32$ states in $16$ Weyl fields.
3. The scalar. $4^{2}=16$ real entries; $\mathbf{15}\oplus\mathbf1$ under $\mathrm{SU}(4)$.
4. The degrees of freedom. $30+32+16=78$.
5. The generator normalisation. $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$.
6. The mass verdicts. Vector forbidden, fermion declined, scalar permitted twice.
7. The minimum. $\Xi=0$ above $M_C$; the condensate is the restructuring's.

## Summary

**Fifteen connections, sixteen Weyl fields and one Hermitian $4\times4$ scalar: three fields and seventy-eight real degrees of freedom.** One coupling multiplies the fifteen, and the copy index is a degeneracy no generator sees.

**The three mass verdicts differ and must not be merged.** The vector mass is forbidden by invariance; **the fermion mass is allowed and declined**; the scalar mass is permitted twice, and those two are the phase's only dimensionful constants.

**The scalar's sixteen components are why the census is not small.** A doublet admits two invariants at degree two and this matrix admits eleven monomials at degree four or below, **and that eleven is the whole difference from a Standard Model count.**

## Summary of Notation

| symbol | meaning |
|---|---|
| $A_{a,\imath}$ | the fifteen connection fields, $a=1,\dots,15$ |
| $t_{a}$ | the fifteen Hermitian traceless generators, $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ |
| $\xi_{f}$, $\bar\xi_{f}$ | the sixteen Weyl fields, $f=1,\dots,16$ |
| $\alpha$ | the copy index, $\alpha=1,2$; a degeneracy, not a family |
| $\Xi$ | the Hermitian $4\times4$ scalar, sixteen real components |
| $\Xi_{0}$ | its traceless part |
| $g_{4}$ | the one coupling |

## Further Reading

- [The Census Above $M_C$](the-census-above-m-c-nineteen-structures-eighteen-admissible-eleven-written.html). The nineteen structures this content admits.
- [The Sixteen Weyl Fields Above $M_C$](the-sixteen-weyl-fields-above-m-c.html). Why they are massless and what the choice costs.
- [The Scalars, Two Indices and the Count Sixteen](the-scalars-two-indices-and-the-count-sixteen.html). The index structure of the matrix.
- [The Force Content of the $\mathrm{SU}(4)$ Model](the-force-content-of-the-su4-model-one-connection-a-nine-dimensional-kernel-and-rank-five.html). What one connection means.
- [The Canonical Basis Above $M_C$](the-canonical-basis-above-m-c-one-rescaling-three-costs-and-the-numbers-that-are-not-invariants.html). The trace mode and the basis.
- [The Coefficients Above $M_C$](the-coefficients-above-m-c-fifteen-constants-one-gauge-parameter-and-one-angle-without-a-row.html). The fifteen constants the content carries.
