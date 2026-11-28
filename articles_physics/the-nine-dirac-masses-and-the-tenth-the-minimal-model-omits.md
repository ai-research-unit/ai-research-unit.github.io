# __The Nine Dirac Masses and the Tenth the Minimal Model Omits__

## Introduction

**The claim.** Nine pieces of the list are mass terms, one per massive species, and the tenth candidate is excluded by a condition that is not the one usually quoted.

$$
\mathcal{L}_{\mathrm{mass},f}=-\sum_{f=1}^{9}m_f\bar\psi_f\psi_f ,
\qquad
m_f=\frac{y_fv}{\sqrt2} .
$$

**Why the reason matters.** The usual sentence is "the neutrino mass is dimension five and therefore forbidden". That sentence is true of the *ancestor* and false of the broken-phase term: $\tfrac12m_\nu\bar\nu^c_L\nu_L$ has dimension three and is invariant under $SU(3)_c\times U(1)_{\mathrm{em}}$. A list built on residual symmetry alone would contain it. What excludes it is descent, the second half of the criterion of [The Census Rule](the-census-rule-dimension-four-residual-invariance-and-one-canonical-term-per-field.html).

**The answer.**

$$
\boxed{\;9\ \text{mass pieces},\qquad \text{the tenth has no dimension-four ancestor}\;}
$$

**The standing.** The nine masses are standard, and the diagonalisation that produces them is [The Yukawa Sector of the $\mathrm{SU}(4)$ Model](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html). What this article adds is the exact status of the tenth, stated as two tests so that a reader can see which one fails.

## The Nine Pieces

**Written out, one per species.**

| Species | Mass piece | Coupling |
|---|---|---|
| $u,c,t$ | $-m_u\bar uu-m_c\bar cc-m_t\bar tt$ | $m_f=y_fv/\sqrt2$ |
| $d,s,b$ | the same for the down type | the same |
| $e,\mu,\tau$ | the same for the charged leptons | the same |

**Where they come from.** The Yukawa terms $-\bar QHY_dd-\bar Q\tilde HY_uu-\bar LHY_ee+\mathrm{h.c.}$ become, at $H=(0,v/\sqrt2)$,

$$
-\bar d_L\frac{vY_d}{\sqrt2}d_R-\bar u_L\frac{vY_u}{\sqrt2}u_R-\bar e_L\frac{vY_e}{\sqrt2}e_R+\mathrm{h.c.},
$$

and a bi-unitary rotation of each pair of chiral fields brings each matrix to a diagonal with real non-negative entries. The entries are the nine masses.

**Why nine and not eighteen.** The matrix is diagonalised by two unitary rotations, one on the left-handed field and one on the right-handed one, and the singular values are real. The eighteen real numbers of a complex $3\times3$ matrix become nine masses plus the rotation angles, and the angles are absorbed into the definition of the mass-basis fields. What survives as a physical mixing is the mismatch between the up-type and down-type rotations, which is the CKM matrix and not a mass.

**Why the masses are positive.** A singular value is non-negative by construction. A negative sign in a mass term can be removed by a chiral rotation of the field, which is one of the rotations already spent, so there is no physical sign.

## The Tenth Candidate

**Two terms, and they fail for different reasons.**

*Dirac.* A term $y_\nu\bar L\tilde H\nu_R$ requires a right-handed neutrino. The content of [The Broken-Phase Content](the-broken-phase-content-twelve-gauge-fields-one-scalar-twelve-species-in-twenty-four-fields.html) has none, so the term is not written. This is an exclusion by content, and it is a modelling choice in the minimal model.

*Majorana.* A term $\tfrac12m_\nu\bar\nu^c_L\nu_L$ requires no new field. Its charges are zero under colour and electromagnetism, and its dimension is three. It passes every test of the residual criterion.

**The test that excludes it.** Its only ancestor is the Weinberg operator

$$
\frac{c_{ab}}{\Lambda}\bigl(L_{L,a}^T i\tau_2 H\bigr)\bigl(L_{L,b}^T i\tau_2 H\bigr),
$$

whose field content has dimension five: two lepton doublets and two scalars give $2\times\tfrac32+2\times1=5$, and the operator is made dimension four by one power of a scale. There is no dimension-four invariant of the unbroken group that produces a neutrino mass, so the broken list has no such row.

**The two statements in one table.**

| Test | Dirac candidate | Majorana candidate |
|---|---|---|
| residual invariance | passes, if $\nu_R$ exists | passes |
| dimension at most four | passes | passes |
| built from the content | fails, no $\nu_R$ | passes |
| descent from a dimension-four invariant | fails | fails |

**What the exclusion does not say.** That neutrinos are massless. It says that the minimal renormalisable content has no operator for the mass, and the measured mass is evidence for content or operators beyond it. [The Seesaw Mechanism and Majorana Mass](the-seesaw-mechanism-and-majorana-mass-in-biquaternionic-form.html) writes the two standard extensions and counts what each costs.

## What the Tenth Would Cost

**Three routes, three prices.**

- A right-handed neutrino per generation: three kinetic pieces, three Dirac mass pieces and three Higgs–fermion pieces, plus a leptonic mixing matrix with its own parameters. The piece count rises by nine and the parameter count by thirteen or more.
- The Weinberg operator alone: no new piece in the broken list, one new mass matrix, and a non-renormalisable ancestor. The piece count is unchanged and the theory is no longer renormalisable.
- A triplet scalar: new scalar pieces, a new gauge multiplet's worth of couplings, and a tree-level contribution to the $\rho$ parameter.

**Why the price is quoted here and not paid.** The category is the list of the minimal model, and the minimal model is the one whose pieces number forty-seven. A category that quietly added a right-handed neutrino would have a different count under the same name.

## Checks

1. The count. Nine mass pieces, and each of the twelve species has one except the three neutrinos.
2. The singular values. A complex $3\times3$ matrix has nine real parameters; diagonalisation leaves three non-negative singular values and six angles, and the angles are basis choices.
3. The positivity. A singular value is non-negative, and a sign can be removed by a chiral rotation.
4. The dimension of the mass term. $\bar\psi\psi$ has dimension three, and the coefficient $m_f$ carries one unit.
5. The dimension of the ancestor. Two lepton doublets and two scalars give $3+2=5$, and one power of $\Lambda$ makes the operator dimension four.
6. The residual test. $\bar\nu^c_L\nu_L$ carries $Q=0$ and no colour, so it passes.
7. The descent test. No dimension-four invariant of the unbroken group produces it, so it fails.
8. The Dirac route. It fails the content test, because $\nu_R$ is absent.
9. The proportionality. $m_f=y_fv/\sqrt2$ in each of the nine rows, and the same $v$ in all nine.
10. The mass-basis statement. In the mass basis the matrices $Y_f$ are diagonal, so the mass pieces are diagonal and the only flavour-changing piece is the charged current.

## Summary

There are nine Dirac mass pieces, one per massive species, each of the form $-m_f\bar\psi_f\psi_f$ with $m_f=y_fv/\sqrt2$. The nine numbers are the singular values of three complex Yukawa matrices, and the rotations that produce them are absorbed into the mass-basis fields, leaving the CKM matrix as the only residue.

The tenth candidate, a neutrino mass, is excluded by two different conditions in its two forms. The Dirac form fails because the content has no right-handed neutrino. The Majorana form passes every test of residual invariance — it is dimension three, neutral under colour and electromagnetism — and fails only descent, because its sole ancestor is the dimension-five Weinberg operator.

The exclusion is therefore a statement about the unbroken theory and about the minimal content, not a statement that neutrinos are massless. Adding a right-handed neutrino, or the Weinberg operator, or a triplet scalar, changes the piece count and the parameter count, and each of the three is priced in the literature rather than here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $m_f$ | A fermion mass, one of nine |
| $y_f$ | The corresponding Yukawa eigenvalue |
| $M_f=vY_f/\sqrt2$ | The mass matrix before diagonalisation |
| $\bar\nu^c_L\nu_L$ | The Majorana mass bilinear, dimension three |
| $\frac{c}{\Lambda}(LH)^2$ | The Weinberg operator, dimension five before suppression |
| $\Lambda$ | The scale of the new physics, absent from the minimal model |

## Further Reading

- [The Yukawa Sector of the $\mathrm{SU}(4)$ Model: One Matrix and Its Diagonalisation](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html). The diagonalisation that produces the nine.
- [The CKM Matrix and CP Violation in Biquaternionic Form](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html). The residue of the two diagonalisations.
- [The Seesaw Mechanism and Majorana Mass in Biquaternionic Form](the-seesaw-mechanism-and-majorana-mass-in-biquaternionic-form.html). The two standard extensions and their prices.
- [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html). The bilinear and its algebra.
- [The Completeness of the List](the-completeness-of-the-list-why-no-other-dimension-four-piece-exists.html). The descent condition, and the other candidates it removes.
