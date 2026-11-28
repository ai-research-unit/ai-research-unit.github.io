# __The Gauge Self-Interactions: Two Triple Vertices and Four Quartic Vertices Inside Four Field Strengths__

## Introduction

**The claim.** The four field strengths contain six interaction structures in the electroweak sector — two triple vertices and four quartic — and the gluon field strength contains the colour analogues of two of them. No new constant appears. Every coefficient is a product of couplings that the quadratic pieces already carry.

**The answer.**

$$
\boxed{\;\{3g,4g\}\subset-\tfrac14GG,\qquad\{\gamma WW,ZWW,W^4,WWAA,WWZZ,WWAZ\}\subset-\tfrac12W^+W^-\;}
$$

**Why eight and not six.** A count that begins at the electroweak sector finds six: two triple and four quartic. The gluon piece contributes two more, the three-gluon and four-gluon vertices, and they are the colour analogues of the first two. The census of [The Census Rule](the-census-rule-dimension-four-residual-invariance-and-one-canonical-term-per-field.html) separates the six electroweak structures, which is why the piece count is forty-seven, the family count four and the vertex count fifty-three.

**The standing.** All eight are standard, and the corpus's own derivations are [The Lagrangian and Quantum Chromodynamics](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html) for the gluon pair and [The Lagrangian and the W and Z Bosons](the-lagrangian-and-the-w-and-z-bosons.html) for the electroweak six. What this article adds is the statement that the eight are one family, with one tensor structure for the triples and one for the quartics, and that no coefficient is free.

## The Gluon Pair

**Three gluons, one constant.**

$$
\Gamma^{abc}_{\mu\nu\rho}(k_1,k_2,k_3)=-\,g_s f^{abc}\bigl[g_{\mu\nu}(k_1-k_2)_\rho+g_{\nu\rho}(k_2-k_3)_\mu+g_{\rho\mu}(k_3-k_1)_\nu\bigr],
$$

with all momenta incoming. The colour factor is the structure constant and nothing else; the Lorentz structure is antisymmetric under the exchange of two legs, as the colour factor is.

**Four gluons.**

$$
\Gamma^{abcd}_{\mu\nu\rho\sigma}=-\,i\,g_s^2\bigl[f^{abe}f^{cde}(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho})+\text{two permutations}\bigr].
$$

**The two coefficients are one number squared and one number.** The four-gluon vertex is the square of the three-gluon vertex's colour factor, because both come from the same commutator term. A theory with a three-gluon vertex of strength $\kappa g_s$ would have a four-gluon vertex of strength $\kappa^2g_s^2$, and the equality is the statement that the curvature is the commutator of one covariant derivative and not an independent object.

## The Electroweak Triples

**The photon and the $Z$, each with the charged pair.**

$$
\Gamma^{\mu\nu\rho}_{\gamma WW}=ie\bigl[g^{\mu\nu}(k_1-k_2)^\rho+g^{\nu\rho}(k_2-k_3)^\mu+g^{\rho\mu}(k_3-k_1)^\nu\bigr],
$$

and the $Z$ rule is the same with $e$ replaced by $g\cos\theta_W$.

**One tensor structure, two coefficients, and one ratio.**

$$
\frac{g_{ZWW}}{g_{\gamma WW}}=\frac{g\cos\theta_W}{e}=\frac{\cos\theta_W}{\sin\theta_W}=\cot\theta_W .
$$

**Why there is no three-$W$ vertex.** Charge conservation. Three $W$ fields carry charges $\pm1$ and cannot sum to zero unless one is neutral, and the neutral member of the triplet is $W^3$, whose couplings are the $\gamma$ and $Z$ rules above. The absence is not an accident of the normalisation; it is the $U(1)_{\mathrm{em}}$ selection rule.

## The Electroweak Quartics

**Four structures, one tensor bracket, four coefficients.**

$$
\Gamma_{4V}=-\,i\,c_{4V}\bigl[2g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho}\bigr],
$$

with $c_{4V}$ one of the four entries of the table and the indices $\mu\nu$ on one $W$ pair and $\rho\sigma$ on the other.

| Structure | $c_{4V}$ | Written with $e$ and $\theta_W$ |
|---|---|---|
| $W^+W^-W^+W^-$ | $g^2$ | $e^2/\sin^4\theta_W$ is not the useful form; the coefficient is $g^2$ |
| $W^+W^-AA$ | $e^2$ | $g^2\sin^2\theta_W$ |
| $W^+W^-ZZ$ | $g^2\cos^2\theta_W$ | $e^2\cot^2\theta_W$ |
| $W^+W^-AZ$ | $eg\cos\theta_W$ | $e^2\cot\theta_W$ |

**The four coefficients are one product.** Each is the product of the two couplings that the corresponding pair of legs carries: the charged pair carries $g$ twice, through its two $W^3$ couplings, and the neutral pair carries whichever of $e$ and $g\cos\theta_W$ its two legs have. The $W^+W^-AZ$ entry is the cross term and carries one of each.

**The ratio test.** The four coefficients satisfy $c_{WWAA}c_{WWZZ}=c_{WWWZ}^2$, because the middle entry is a geometric mean. That identity is a one-line check that the four come from one square and not from four independent parameters.

## Four Families and Eight Monomials

**The two counts, and which one the census uses.** The eight monomials of this article group by tensor structure: one triple-gluon monomial, one quartic-gluon monomial, two triple electroweak monomials sharing one structure, and four quartic electroweak monomials sharing one structure. That is four families, and it is the six electroweak structures that the census adds to the piece count, giving $47+6=53$. The finer count that separates all eight monomials, gluon pair included, gives $47+8=55$ on the invariant rows, and it is the count used below whenever a single coefficient is being discussed.

**Why the family is the useful unit.** A family is the object that one gauge invariance constrains: the two triple electroweak couplings are tied by the same rotation angle, and the four quartic ones by the same two couplings. Counting families counts constraints, and counting monomials counts measurement channels.

## Why No New Constant

**Gauge invariance is the reason, and it is a counting statement.** The eight coefficients are functions of three numbers: $g_s$ for the gluon pair, and $e$ and $\theta_W$ for the six electroweak structures. A theory with independent triple and quartic couplings would fail the Ward identities that the gauge invariance of the four kinetic pieces enforces.

**The precise form of the constraint.** If the triple coupling is written $\kappa\,g\cos\theta_W$ and the quartic $g^2\cos^2\theta_W$, then $\kappa\ne1$ is a theory in which the curvature is not the commutator of the covariant derivative that couples to the fermions. The deviation is measurable — it changes the $W$ pair production cross section — and the measurement is a measurement of $\kappa=1$ and not of a new parameter.

**What the corpus's framework adds.** Nothing. The eight coefficients are imported with the rest, and the algebra's role is exhausted at the $\mathrm{U}(2)$ ceiling of [The Compact Sector of the Biquaternions Is $\mathfrak{u}(2)$](the-compact-sector-of-the-biquaternions-is-u2.html). The one structural statement the corpus makes is that the gluon pair has no algebra element to live in, and its colour factor is therefore written with indices external to $\mathbb{B}$.

## What the Structures Cost

**One row of the list, eight vertices.** The pieces do not change: the four kinetic pieces are four rows of the forty-seven. The vertex count does change, which is why the census prints both numbers and states which rule produces which.

| Count | Value | What it counts |
|---|---|---|
| pieces | $4$ | the four squared curvatures |
| structures inside them | $8$ | the eight of this article |
| vertices of the list | $53=47+6$ | pieces plus the six electroweak structures |

**The eight are not eight parameters.** They are eight functions of three. A reader who counts vertices and calls them parameters will overcount the theory by five, and the parameter count of [The Coefficients the List Carries](the-coefficients-the-list-carries-eighteen-constants-and-the-one-that-multiplies-no-piece.html) is the correction.

## Checks

1. The count. Two gluon structures plus six electroweak structures is eight, and they group into four families: one triple-gluon, one quartic-gluon, one triple electroweak with two members and one quartic electroweak with four.
2. The tensor structures. One for the triples (three terms, each with one momentum difference) and one for the quartics (three terms, each a product of two metrics).
3. The ratio of triples. $g\cos\theta_W/e=\cot\theta_W$.
4. The geometric-mean identity. $c_{WWAA}c_{WWZZ}=e^2g^2\cos^2\theta_W=(eg\cos\theta_W)^2=c_{WWWZ}^2$.
5. The no-three-$W$ rule. Charge conservation on three charged fields.
6. The colour factor. $f^{abc}$ for the triple and $f^{abe}f^{cde}$ for the quartic, so the second is the square of the first in the same sense that the electroweak quartic is the square of the electroweak triple.
7. The vertex total. $47+6=53$, and the finer monomial total over all eight structures is $47+8=55$.
8. The parameter total. Three couplings for the eight structures, and no nineteenth.
9. The corpus's ceiling. No element of $\mathbb{B}$ carries three colour lines, so the gluon pair is written with external indices and the electroweak six are not.
10. The measurement statement. $\kappa=1$ is a prediction of the four kinetic pieces and not a parameter of the list.

## Summary

The four kinetic pieces contain eight interaction structures. The gluon piece contains the three-gluon and four-gluon vertices, with coefficients $g_s$ and $g_s^2$. The electroweak pieces contain the $\gamma W^+W^-$ and $ZW^+W^-$ triples, with $e$ and $g\cos\theta_W$, and the four quartics $W^4$, $WWAA$, $WWZZ$ and $WWAZ$, with $g^2$, $e^2$, $g^2\cos^2\theta_W$ and $eg\cos\theta_W$.

The eight are one family. The triples share a tensor structure and differ only in the coupling of the neutral leg; the quartics share a tensor structure and differ only in the product of the couplings of the two pairs. The four quartic coefficients satisfy a geometric-mean identity, which is the algebraic trace of their common origin in one square.

No coefficient is free. The eight are functions of $g_s$, $e$ and $\theta_W$, and a deviation in any of them is a deviation from the statement that the curvature is the commutator of the covariant derivative. There is no three-$W$ vertex, by charge conservation.

The eight structures do not add rows to the list. They group into four families, one per tensor structure with its couplings, and the four families are what the census adds, which is why the vertex count is fifty-three and the piece count is forty-nine.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $f^{abc}$, $\varepsilon^{abc}$ | Structure constants |
| $g_s$, $e$, $g$, $\theta_W$ | Couplings and mixing angle |
| $\Gamma_{\gamma WW}$, $\Gamma_{ZWW}$ | Triple gauge vertices |
| $c_{4V}$ | The quartic coefficient, one of $g^2$, $e^2$, $g^2\cos^2\theta_W$, $eg\cos\theta_W$ |
| $55$ | The monomial count, $47+8$ |
| $\kappa$ | A deviation of the triple coupling from one, excluded |

## Further Reading

- [The Lagrangian and Quantum Chromodynamics: The Triplet, the Octet and the Feynman Rules](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html). The gluon pair, derived.
- [The Lagrangian and the W and Z Bosons](the-lagrangian-and-the-w-and-z-bosons.html). The electroweak triple and quartic, derived.
- [The Four Field Strengths](the-four-field-strengths-one-kinetic-piece-per-gauge-field.html). The pieces these structures live in.
- [The Compact Sector of the Biquaternions Is $\mathfrak{u}(2)$: No $\mathfrak{su}(3)$ Among the Operators](the-compact-sector-of-the-biquaternions-is-u2.html). Why the colour factor is written externally.
- [The Complete Lagrangian](the-census-in-one-display-forty-seven-terms-fifty-three-vertices-twenty-blocks-and-nineteen-parameters.html). The counts, with the rule that produces each.
