# __The Twelve Fermion Kinetic Pieces: Nine Massive Species, Three Neutrinos and Their Currents__

## Introduction

**The claim.** The list has twelve fermion kinetic pieces, one per species: six quarks summed over colour, three charged leptons, three neutrinos.

$$
\mathcal{L}_{\mathrm{ferm}}=\sum_{f=1}^{12}i\,\bar\psi_f\gamma^\mu\partial_\mu\psi_f ,
\qquad
\psi_f\in\{u,c,t,d,s,b,e,\mu,\tau,\nu_e,\nu_\mu,\nu_\tau\} .
$$

**Why twelve and not nine.** Nine species have a mass and three do not. All twelve propagate. A list that gives a field a coupling to a current and no free term is not a Lagrangian, and the count of kinetic pieces is the count of fields and not the count of masses.

**The answer.**

$$
\boxed{\;12=6+3+3,\qquad 12\ \text{kinetic pieces},\quad 9\ \text{mass pieces}\;}
$$

**The standing.** The free Dirac equation and its bilinears are the corpus's, in [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html). This article writes the twelve pieces in the mass basis, states the one structural difference between the nine and the three, and counts the currents they define.

## The Twelve Pieces

**One line, twelve rows.**

| Species | Colour | Chirality | Piece |
|---|---|---|---|
| $u,c,t$ | $\mathbf3$ | $L$, $R$ | $i\bar q\gamma^\mu\partial_\mu q$, summed over colour and flavour |
| $d,s,b$ | $\mathbf3$ | $L$, $R$ | the same, with the down-type flavour sum |
| $e,\mu,\tau$ | $\mathbf1$ | $L$, $R$ | $i\bar\ell\gamma^\mu\partial_\mu\ell$ |
| $\nu_e,\nu_\mu,\nu_\tau$ | $\mathbf1$ | $L$ only | $i\bar\nu_L\gamma^\mu\partial_\mu\nu_L$ |

**The coefficient is one for all twelve.** This is the one place in the list where twelve rows share a coefficient, and the coefficient is fixed by the canonical anticommutator rather than measured. It is why the twelve can be written as one sum and still counted as twelve rows: [The Census Rule](the-census-rule-dimension-four-residual-invariance-and-one-canonical-term-per-field.html) counts canonical terms, and a canonical term with unit coefficient is still a term.

**The colour sum is inside one piece.** A quark kinetic term summed over three colours is one row, because the three colours share one coefficient and one mass. The same convention makes the six flavours of the up type one row and the six of the down type one row.

## The Difference Between the Nine and the Three

**The nine are Dirac, the three are Weyl.**

$$
i\bar\psi_f\gamma^\mu\partial_\mu\psi_f
\qquad\text{and}\qquad
i\bar\nu_{L}\gamma^\mu\partial_\mu\nu_L=\tfrac12\,i\bar\nu\gamma^\mu(1-\gamma_5)\partial_\mu\nu .
$$

**Why the difference.** A Dirac field has two chiral components and a mass term couples them. A neutrino in this content has one, because there is no right-handed neutrino to couple to. The kinetic term survives the loss of the second component; the mass term does not.

**Why the difference is not a defect.** The kinetic term of a Weyl field is a perfectly good dimension-four invariant of the residual group: $\nu_L$ has $Q=0$ and no colour, so $i\bar\nu_L\slashed\partial\nu_L$ is invariant. It is the *mass* term that the content forbids, and [The Nine Dirac Masses](the-nine-dirac-masses-and-the-tenth-the-minimal-model-omits.html) shows that the exclusion is a statement about the unbroken theory and not about this piece.

**The projector is idempotent.** $\tfrac12(1-\gamma_5)$ squares to itself, so writing the Weyl piece with the projector twice would give the same term; the display uses it once, which is why the factor is $\tfrac12$ and not $\tfrac14$.

## The Two Currents Each Piece Defines

**Vector and axial.**

$$
j^{\mu}_{V,f}=\bar\psi_f\gamma^\mu\psi_f ,
\qquad
j^{\mu}_{A,f}=\bar\psi_f\gamma^\mu\gamma_5\psi_f .
$$

**Eleven and one.** A Dirac species defines both. A left-handed neutrino defines one combination only, $j_V-j_A$, because $(1-\gamma_5)$ acting on a left-handed field returns twice the field. The count of independent currents is therefore

$$
9\times2+3\times1=21 .
$$

**Why the currents matter here rather than in the interaction articles.** Each interaction piece of the list couples one of these currents to one connection: the photon to $j_V$ with the charge as coefficient, the gluon to the colour current, the $Z$ to a fixed combination of $j_V$ and $j_A$, and the $W$ to the left-handed charged current. The kinetic pieces are what make the currents conserved, and current conservation is what the Ward identities of the gauge sector need.

**The axial current is not conserved by the mass.** $\partial_\mu j^\mu_{A,f}=2im_f\bar\psi_f\gamma_5\psi_f$, so the mass pieces break the axial symmetry explicitly. The divergence is the axial anomaly's classical partner, and the interplay of the two is the subject of [Anomalies and Anomaly Cancellation](anomalies-and-anomaly-cancellation.html).

## Why the Pieces Are Not Nine

**The propagation argument.** A field that appears in a current must have a propagator, and the propagator is the inverse of the quadratic operator that the kinetic piece supplies. Deleting the three neutrino kinetic terms would leave the neutral-current and charged-current pieces with external neutrino legs and no internal ones, which is not a theory of anything.

**The counting argument.** The forty-seven is a count of the terms of one Lagrangian. A term that couples $\bar\nu$ to $e$ and $W$ is in the list, and a term that propagates $\nu$ is not; the second is required for the first to be usable. The asymmetry would also show up in the count of parameters: the three neutrino kinetic pieces carry no parameter, so deleting them would remove three rows and no constants, and the parameter map of [The Coefficients the List Carries](the-coefficients-the-list-carries-eighteen-constants-and-the-one-that-multiplies-no-piece.html) would be unchanged while the piece count fell to forty-six.

**The one reading under which nine is correct.** If the census counted only pieces with free parameters, the neutrino kinetics, the photon kinetic, the gluon kinetic and the $W$ kinetic would all be excluded, and the count would be a count of parameters in disguise. The category does not use that convention, and it says so once in the census rule.

## Checks

1. The count. $6+3+3=12$.
2. The colour sum. Three colours inside one quark piece, and one coefficient for all three.
3. The dimension. $\bar\psi\slashed\partial\psi$ has dimension $3+1=4$.
4. The Hermiticity. $i\bar\psi\gamma^\mu\partial_\mu\psi$ is Hermitian up to a total derivative, which is why the $i$ is there and why the coefficient is real.
5. The projector. $\bigl[\tfrac12(1-\gamma_5)\bigr]^2=\tfrac12(1-\gamma_5)$, so the Weyl piece is written once with a factor $\tfrac12$.
6. The current count. $9\times2+3\times1=21$.
7. The axial divergence. $\partial_\mu j^\mu_{A,f}=2im_f\bar\psi_f\gamma_5\psi_f$, nonzero exactly for the nine massive species.
8. The equation of motion. $i\slashed\partial\psi_f=0$ for the three neutrinos and $i\slashed\partial\psi_f=m_f\psi_f$ for the nine, which is the content of the twelve pieces alone.
9. The parameter independence. The twelve pieces carry one coefficient between them, and it is not one of the eighteen.
10. The corpus's writing. $\bar{\tilde\Xi}i\tilde\nabla_\Phi\tilde\Xi$ per Weyl field, forty-five of them, which is the same count as twelve Dirac species plus three left-handed neutrinos.

## Summary

There are twelve fermion kinetic pieces, one per species, with unit coefficient fixed by the canonical anticommutator: six quarks summed over colour, three charged leptons, three neutrinos. The colour and flavour sums are inside single pieces, which is why the count is twelve and not forty-five.

Nine of the twelve are Dirac and three are Weyl. The difference is the absence of a right-handed neutrino, and it affects the mass piece and not the kinetic one. The Weyl piece carries a single projector and a factor of $\tfrac12$.

Each Dirac species defines a vector and an axial current, and each neutrino defines one combination of them, so the list carries twenty-one independent currents. The interactions couple these currents to the connections, and the gauge sector's Ward identities are what the conservation of the vector currents supplies.

The three neutrino kinetic pieces are in the list because a field that is coupled must propagate. A census that counted only pieces with free parameters would delete them and would also delete four other pieces, and the category does not use that convention.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\psi_f$ | A Dirac species, summed over colour where it has colour |
| $\nu_{L}$ | A left-handed neutrino, one Weyl field |
| $\gamma^\mu$, $\gamma_5$ | The Dirac matrices of the frame |
| $j^\mu_{V,f}$, $j^\mu_{A,f}$ | Vector and axial currents |
| $21$ | The count of independent currents, $9\times2+3$ |

## Further Reading

- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html). The free equation, the bilinears and the sign conventions used above.
- [The Nine Dirac Masses and the Tenth the Minimal Model Omits](the-nine-dirac-masses-and-the-tenth-the-minimal-model-omits.html). Why nine of the twelve have a mass piece.
- [The Neutral-Current Piece](the-neutral-current-piece-two-coefficient-tables-and-the-two-zeros-that-are-not-the-same.html). Where the twenty-one currents are coupled.
- [Anomalies and Anomaly Cancellation](anomalies-and-anomaly-cancellation.html). The axial divergence and the conditions on the content.
- [The Minimal Coupling in Biquaternionic Form](the-minimal-coupling-in-biquaternionic-form.html). The gradient that replaces the derivative in the interacting pieces.
